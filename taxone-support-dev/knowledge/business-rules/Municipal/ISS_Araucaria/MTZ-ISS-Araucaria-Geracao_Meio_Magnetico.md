# MTZ-ISS-Araucaria-Geracao_Meio_Magnetico

- **Fonte:** MTZ-ISS-Araucaria-Geracao_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 56 KB

---

# ISS Araucária \- Geração do Meio Magnético

__Atenção: Regras ajustadas da OS3470\-I1E estão no novo documento de regras dos módulos municipais – DE\-PARA – Municipal\.xls\.__

__Documento disponível no diretório do CVS: documentacao funcional\\Documento Matriz\\Municipal\\Regras Gerais__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3153

ISS Araucária \- Geração do Meio Magnético

Este documento tem por objetivo criar o novo módulo “ISS Araucária” que irá gerar o meio magnético com as informações de serviços prestados e de serviços tomados no mês de referência\.

OS3470\-I1E

Ajuste nas regras gerais de recuperação do responsável pela retenção \- Tomador ou Prestador

Este documento tem como objetivo ajustar a regras de tipo de recolhimento e também migrar essa regra para um novo documento DE\-PARA de regras\.

CH10651\_2012

 ARAUCÁRIA \- Geração dos campos 8, 9 e 11 incorreta

Este documento tem como objetivo ajustar as regras para a geração dos campos 8, 9 e 11\.

OS3926\-A1

Geração do Meio Magnético Canoas \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os município atendido pelo validador ISS \- ARAUCARIA\.

__OS4224__

ISS Araucária \- Geração do Meio Magnético\. I

Inclusão de parametrização de Modelo do Documento, inclusão da parametrização do campo série e correção da ordem que estava invertida entre o campo Série e campo Modelo\.

MFS\_2071

DW \- MUNICIPAL – ISS Araucária – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Regra p/ criação do novo módulo

O novo módulo “ISS Araucária” deve ficar localizado no grupo “Municipal” abaixo do módulo “ISISS Vitória”\.

A descrição funcional do módulo será: “O Sistema Eletrônico de Gerenciamento do ISSQN, destina\-se a escrituração mensal das declarações de dados econômico\-fiscal de todas as operações que envolvam prestações de serviços, tributáveis ou não, e emissão da guia de recolhimento”\.

__OS3153__

__RN02__

__Regra p/ abertura do novo módulo__

Se o estabelecimento selecionado no Manager não pertencer ao estado do Paraná \(UF = “PR”\) e ao município de Araucária \(Cod Município IBGE = 1804\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Araucária, Paraná\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__OS3153__

__RN03__

__Regra p/ hierarquia de menus__

Deverão ser criados os seguintes menus e sub\-menus no módulo ISS Araucária:

- Arquivo
- Parâmetros
	- Modelo Msaf x Série ISS
	- Classificação de Serviços
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3153 / OS3926\-A1 / __

__OS4224__

__RN04__

__Regra p/ abertura da tela Parâmetros – Modelo Msaf x Série ISS:__

Ao clicar no menu Parâmetros – Modelo Msaf x Modelo ISS, o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos modelos que serão parametrizados\.

__OS3153__

__OS4224__

__RN05__

__Regra do campo Modelo MasterSAF da tela Parâmetros – Modelo Msaf x Série ISS:__

Deverá recuperar as informações da tabela x2024\_modelo\_docto\. Somente serão recuperadas informações cadastradas no grupo escolhido\. A recuperação dos modelos deve ser realizado através da pastinha amarela\.

__OS3153__

__OS4224__

__RN06__

__Regra do campo Modelo ISS da tela Parâmetros – Modelo Msaf x Série ISS:__

Deverá exibir os modelos definidos no “Manual de Layout”\. Exibir as opções da tabela PRT\_SERIE\_OBRIG \(TFIX83\) referentes ao COD\_MODULO = ‘072’

__OS3153__

__OS4224__

__RN07__

__Regra do campo Validade da tela Parâmetros – Modelo Msaf x Série ISS:__

Irá permitir que o mesmo modelo cadastrado no MasterSAF possam ser relacionados com diferentes modelos da ISS Araucária para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\.

__OS3153__

__OS4224__

__RN08__

__Regra da tela Parâmetros – Modelo Msaf x Série ISS:__

O sistema não permite que os mesmos modelos sejam relacionados com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que os mesmos modelos sejam relacionados com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3153__

__OS4224__

__RN09__

__Regra do relatório da tela Parâmetros – Modelo Msaf x Série ISS:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os modelos cadastrados no MasterSAF e os modelos solicitados pela ISS\.

__OS3153__

__OS4224__

__RN10__

__Regra p/ abertura da tela Parâmetros –  Classificação de Serviços:__

Ao clicar no menu Parâmetros – Classificação de Serviços, o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos serviços que serão classificados\.

__OS3153__

__OS4224__

__RN11__

__Regra p/ tela Parâmetros –  Classificação de Serviços:__

Após a seleção do Estabelecimento/Grupo/Validade, o sistema deve exibir a tela de classificação de serviços, contendo os seguintes campos: UF, município, Parâmetro, Serviços, Selecionar Todos e Desmarcar Todos\. Essa tela deve armazenar os dados cadastrados na tabela PRT\_SERVICO\_MUNIC\_MSAF\.

__OS3153__

__OS4224__

__RN12__

__Regra p/ opções da tela Parâmetros –  Classificação de Serviços:__

Essa tela deve oferecer as seguintes opções ao usuário: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá um registro existente\. A tela de critério de seleção deve conter todos dos campos da tabela PRT\_SERVICO\_MUNIC\_OBRIG\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3153__

__OS4224__

__RN13__

__Regra p/ campo UF da tela Parâmetros –  Classificação de Serviços:__

O campo “UF” deve ser um combo Box e deve exibir todas as UFs cadastradas na tabela ESTADO\. 

__OS3153__

__OS4224__

	

__RN14__

__Regra p/ campo Município da tela Parâmetros –  Classificação de Serviços:__

O campo “Município” deve ser composto por um text Box que permitirá a digitação do código do município \+ pasta amarela para seleção de municípios \+ um text Box desabilitado que irá exibir a descrição do município informado\.

Quando o usuário clicar na pastinha amarela, o sistema de recuperar todos os municípios correspondentes a UF previamente selecionada\. 

__OS3153__

__OS4224__

__RN15__

__Regra p/ campo Parâmetro da tela Parâmetros –  Classificação de Serviços:__

O campo Parâmetro deve ser exibido através de um ListBox e deve exibir as seguintes opções:

- Serviços Isentos – cod\_param = 433
- Serviços sujeitos à não incidência – cod\_param = 432
- Serviços Imunes – cod\_param = 420
- Serviços Prestados e Devidos em outro Município – cod\_param = 465

__OS3153__

__OS4224__

__RN16__

__Regra p/ campo Serviço da tela Parâmetros –  Classificação de Serviços:__

O campo Serviços deve permitir que o usuário marque quantos serviços forem necessários para a classificação desejada\. O campo deve exibir os campos COD\_SERVICO \+ ‘ – ’ \+ DESCRICAO da tabela X2018\_SERVICOS\.

__OS3153__

__OS4224__

__RN17__

__Regra p/ botão Selecionar Todos da tela Parâmetros –  Classificação de Serviços:__

O botão Selecionar Todos deve permitir que o usuário possa selecionar todos os serviços de uma vez\.

__OS3153__

__OS4224__

__RN18__

__Regra p/ botão Desmarcar Todos da tela Parâmetros –  Classificação de Serviços:__

O botão Desmarcar Todos deve permitir que o usuário possa desmarcar todos os serviços de uma vez\.

__OS3153__

__OS4224__

__RN19__

__Regra de criação do nome do arquivo__

Cada arquivo corresponderá a apenas uma DMS e será identificado por:

__ISS\_ARAUCARIA\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

      __ISS\_ARAUCARIA__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: ISS\_ARAUCARIA \_01012010\.txt

__OS3153__

__RN20__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

*Data Inicial:* deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

*Data Final:* deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

*Gerar Registro “E” – Documentos Emitidos: *Esse campo deve ser um check Box, com as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Quando o campo estivar marcado \(= “S”\), o registro do tipo “E” – Documentos Emitidos deve ser gerado no meio magnético para o período informado\.

Quando o campo estivar desmarcado \(= “N”\), o registro do tipo “E” – Documentos Emitidos não deve ser gerado no meio magnético para o período informado\.

*Gerar Registro “R” – Documentos Recebidos: *Esse campo deve ser um check Box, com as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Quando o campo estivar marcado \(= “S”\), o registro do tipo “R” – Documentos Recebidos deve ser gerado no meio magnético para o período informado\.

Quando o campo estivar desmarcado \(= “N”\), o registro do tipo “R” – Documentos Recebidos não deve ser gerado no meio magnético para o período informado\.

*Estabelecimento:* o sistema deve exibir os estabelecimentos pertencentes ao município de Araucária, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3153__

__MFS\_2071__

__RN21__

__Regra de formatação do arquivo__

Cada linha do arquivo equivale a um registro\. O primeiro caracter de cada linha indica o tipo do registro: “H” cabeçalho, “E” documentos fiscais emitidos e “R” documentos fiscais recebidos\. Todos os campos possuem tamanho fixo e são identificados pela posição dos caracteres, conforme especificado no layout\.

Para indicar o final de cada linha, deverá ser incluído o caracter de retorno \(Código ASCII 13\)

__OS3153__

__RN22__

__Regra p/ geração do registro Cabeçalho__

A primeira linha do arquivo será o cabeçalho \(header\) e deve apresentar as informações referentes ao estabelecimento escolhido na tela de geração do meio magnético\.

__OS3153__

__RN23__

__Regra p/ registro Cabeçalho – Identificação do registro__

Preencher com “H”

__OS3153__

__RN24__

__Regra p/ registro Cabeçalho – CMC – Inscrição Municipal__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

__OS3153__

__RN25__

__Regra p/ registro Cabeçalho – Versão do arquivo de layout__

Preencher com “001”

__OS3153__

__RN26__

__Regra p/ geração do registro Documentos Fiscais Emitidos__

Cada documento fiscal emitido \(nota fiscal, cupom fiscal, etc\.\) corresponde a uma linha \(registro\) deste tipo\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

__OS3153__

__RN27__

__Regra p/ registro Documentos Fiscais Emitidos – Identificação do registro__

Preencher com “E”

__OS3153__

__RN28__

__Regra p/ registro Documentos Fiscais Emitidos – Data de Emissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)

__OS3153__

__RN29__

__Regra p/ registro Documentos Fiscais Emitidos – Série do documento__

Preencher com o campo Modelo ISS da tela Parâmetros – Modelo Msaf x Modelo ISS referente ao modelo cadastrado na nota\.

Preencher com o campo “Série ISS Araucária” da tela: Municipal>Parâmetros para Município>Menu:__ __Parâmetros >Série Msaf x Série, referente a Série cadastrada na nota\.

OBS: Se a série não estiver parametrizada, deverá exibir uma menssagem no Log, informando que a série deve ser parametrizada\.

__OS3153__

__OS4224__

__RN30__

__Regra p/ registro Documentos Fiscais Emitidos – Modelo do Documento__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)

Preencher com o campo “Modelo ISS Araucária” da tela: Municipal>Parâmetros para Município>Menu:__ __Parâmetros >Modelo Msaf x Modelo, referente ao modelo cadastrado na nota\.

Obs\.: Se o modelo parametrizado for “__0__”, o sistema deverá substituir por espaço em branco no arquivo gerado\.

Se o modelo não estiver parametrizado, deverá exibir uma mensagem no Log, informando que o modelo deve ser parametrizado\.

__OS3153__

__OS4224__

__RN31__

__Regra p/ registro Documentos Fiscais Emitidos – Tipo do Documento__

Preencher com:

D – Devolução, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = “2”\. \(campo 04 da SAFX07\)

C – Isenta ou Imune, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” OU quando o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

E – Não Incidência, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “06”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

F – Sociedade de Profissionais, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “08”\.

G – Serviços Prestados e Devidos em outro município, quando o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “465” e o campo IND\_ISS da tabela ESTABELECIMENTO não estiver preenchido\.

Caso nenhuma das opções acima sejam verdadeiras, preencher com:

A – Serviços, quando o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = “2”\. \(campo 12 da SAFX07\)

B – Materiais e Serviços, quando o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = “3”\. \(campo 12 da SAFX07\)

__OS3153__

__RN32__

__Regra p/ registro Documentos Fiscais Emitidos – Número do Documento __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

__OS3153__

__RN33__

__Regra p/ registro Documentos Fiscais Emitidos – Valor Total do Documento__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. \(campo 15 da SAFX09\)

__OS3153__

__RN34__

__Regra p/ registro Documentos Fiscais Emitidos – Valor do Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

__OS3153__

__RN35__

__Regra p/ registro Documentos Fiscais Emitidos – Tipo de Recolhimento__

Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”, preencher com “I”

Senão,

  Preencher com “A”, quando pelo menos uma das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

  Preencher com “R”, quando nenhuma das opões seja verdadeira\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3153__

__OS3470\-I1E__

__RN36__

__Regra p/ registro Documentos Fiscais Emitidos – Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)

__OS3153__

__RN37__

__Regra p/ registro Documentos Fiscais Emitidos – CMC Inscrição municipal do Tomador__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 09 da SAFX04\)

__OS3153__

__RN38__

__Regra p/ registro Documentos Fiscais Emitidos – CNPJ do Tomador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal, quando tiver 14 posições\. \(campo 06 da SAFX04\)

__OS3153__

__RN39__

__Regra p/ registro Documentos Fiscais Emitidos – CPF do Tomador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal, quando tiver 11 posições\. \(campo 06 da SAFX04\)

__OS3153__

__RN40__

__Regra p/ registro Documentos Fiscais Emitidos – Nome do Tomador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 05 da SAFX04\)

__OS3153__

__RN41__

__Regra p/ registro Documentos Fiscais Emitidos – Tipo de Logradouro__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 42 da SAFX04\)

__OS3153__

__RN42__

__Regra p/ registro Documentos Fiscais Emitidos – Logradouro__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 12 da SAFX04\)

__OS3153__

__RN43__

__Regra p/ registro Documentos Fiscais Emitidos – Número Predial__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 13 da SAFX04\)

__OS3153__

__RN44__

__Regra p/ registro Documentos Fiscais Emitidos – Complemento do Endereço__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 14 da SAFX04\)

__OS3153__

__RN45__

__Regra p/ registro Documentos Fiscais Emitidos – Tipo de bairro__

Preencher com o campo TP\_BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 44 da SAFX04\)

__OS3153__

__RN46__

__Regra p/ registro Documentos Fiscais Emitidos – Bairro__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 15 da SAFX04\)

__OS3153__

__RN47__

__Regra p/ registro Documentos Fiscais Emitidos – Cidade__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao Campo COD\_MUNICPIO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo25 da SAFX04\)

__OS3153__

__RN48__

__Regra p/ registro Documentos Fiscais Emitidos – UF__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 19 da SAFX04\)

__OS3153__

__RN49__

__Regra p/ registro Documentos Fiscais Emitidos – CEP__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente ao tomador cadastrado na nota fiscal\. \(campo 20 da SAFX04\)

__OS3153__

__RN50__

__Regra p/ geração do registro Documentos Fiscais Recebidos__

Cada documento fiscal recebido corresponde a uma linha \(registro\) deste tipo\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

__OS3153__

__RN51__

__Regra p/ registro Documentos Fiscais Recebidos – Identificação do registro__

Preencher com “R”

__OS3153__

__RN52__

__Regra p/ registro Documentos Fiscais Recebidos – Data de Retenção__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\), quando pelo menos uma das opções abaixo seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota utilizando o município cadastrado no estabelecimento\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)

Se o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\) não estiver preenchido, a geração deve preencher esse campo com a DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)

E exibir uma mensagem no log informando esse preenchimento\.

__OS3153__

__RN53__

__Regra p/ registro Documentos Fiscais Recebidos – Data de Emissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)

__OS3153__

__RN54__

__Regra p/ registro Documentos Fiscais Recebidos – Série do documento__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)

Preencher com o campo “Série ISS Araucária” da tela: Municipal>Parâmetros para Município>Menu:__ __Parâmetros >Série Msaf x Série, referente a Série cadastrada na nota\.

OBS: Se a série não estiver parametrizada, deverá exibir uma menssagem no Log, informando que a série deve ser parametrizada\.

__OS3153__

__OS4224__

__RN55__

__Regra p/ registro Documentos Fiscais Recebidos – Modelo do Documento__

Preencher com o campo Modelo ISS da tela Parâmetros – Modelo Msaf x Modelo ISS referente ao modelo cadastrado na nota\.

Preencher com o campo “Modelo ISS Araucária” da tela: Municipal>Parâmetros para Município>Menu:__ __Parâmetros >Modelo Msaf x Modelo, referente ao modelo cadastrado na nota\.

Obs\.: Se o modelo parametrizado for “__0__”, o sistema deverá substituir por espaço em branco no arquivo gerado\.

Se o modelo não estiver parametrizado, deverá exibir uma mensagem no Log, informando que o modelo deve ser parametrizado\.

__OS3153__

__OS4224__

__RN56__

__Regra p/ registro Documentos Fiscais Recebidos – Tipo do Documento__

Preencher com:

C – Isenta ou Imune, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\. OU quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

D – Devolução, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = “2”\. \(campo 04 da SAFX07\)

E – Não Incidência, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

F – Sociedade de Profissionais, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “06”\.

G – Serviços Prestados e Devidos em outro município, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “465”

H – Autônomos com Inscrição Municipal, quando o campo IDENT\_CBO da tabela X04\_PESSOA\_FIS\_JUR \(campo 34 da SAF04\) estiver preenchido e o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 09 da SAF04\) estiver preenchido\.

I – Autônomos SEM Inscrição Municipal, quando o campo IDENT\_CBO da tabela X04\_PESSOA\_FIS\_JUR \(campo 34 da SAFX04\) estiver preenchido e o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 09 da SAFX04\) não estiver preenchido ou estiver preenchido com ISENTO ou ISENTA\.

A – Serviços, quando o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = “2”\. \(campo 12 da SAFX07\)

B – Materiais e Serviços, quando o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = “3”\. \(campo 12 da SAFX07\)

__OS3153__

__RN57__

__Regra p/ registro Documentos Fiscais Recebidos – Número do Documento__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

__OS3153__

__RN58__

__Regra p/ registro Documentos Fiscais Recebidos – Valor Total do Documento__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. \(campo 15 da SAFX09\)

Preenchimento: alinhado a direita e com zeros a esquerda e os centavos \(duas casas\) separados por virgula\.

__OS3153__

__CH10651\_2012__

__RN59__

__Regra p/ registro Documentos Fiscais Recebidos – Valor do Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)\.

Preenchimento: alinhado a direita e com zeros a esquerda e os centavos \(duas casas\) separados por virgula\.

__OS3153__

__CH10651\_2012__

__RN60__

__Regra p/ registro Documentos Fiscais Recebidos – Tipo de Recolhimento__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”, preencher com “I”

Senão,

  Preencher com “R”, quando pelo menos uma das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido

  Preencher com “E”, quando nenhuma das opões seja verdadeira\.

__OS3153__

__OS3470\-I1E__

__RN61__

__Regra p/ registro Documentos Fiscais Recebidos – Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)\.

Preenchimento: alinhado a direita e com zeros a esquerda e os centavos \(duas casas\) separados por virgula\.

__OS3153__

__CH10651\_2012__

__RN62__

__Regra p/ registro Documentos Fiscais Recebidos – CMC Inscrição municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 09 da SAFX04\)

__OS3153__

__RN63__

__Regra p/ registro Documentos Fiscais Recebidos – CNPJ do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal, quando tiver 14 posições\. \(campo 06 da SAFX04\)

__OS3153__

__RN64__

__Regra p/ registro Documentos Fiscais Recebidos – CPF do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal, quando tiver 11 posições\. \(campo 06 da SAFX04\)

__OS3153__

__RN65__

__Regra p/ registro Documentos Fiscais Recebidos – Nome do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 05 da SAFX04\)

__OS3153__

__RN66__

__Regra p/ registro Documentos Fiscais Recebidos – Tipo de Logradouro__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 42 da SAFX04\)

__OS3153__

__RN67__

__Regra p/ registro Documentos Fiscais Recebidos – Logradouro__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 12 da SAFX04\)

__OS3153__

__RN68__

__Regra p/ registro Documentos Fiscais Recebidos – Número Predial__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 13 da SAFX04\)

__OS3153__

__RN69__

__Regra p/ registro Documentos Fiscais Recebidos – Complemento do Endereço__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 14 da SAFX04\)

__OS3153__

__RN70__

__Regra p/ registro Documentos Fiscais Recebidos – Tipo de bairro__

Preencher com o campo TP\_BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 44 da SAFX04\)

__OS3153__

__RN71__

__Regra p/ registro Documentos Fiscais Recebidos – Bairro__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 15 da SAFX04\)

__OS3153__

__RN72__

__Regra p/ registro Documentos Fiscais Recebidos – Cidade__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao Campo COD\_MUNICPIO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo25 da SAFX04\)

__OS3153__

__RN73__

__Regra p/ registro Documentos Fiscais Recebidos – UF__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 19 da SAFX04\)

__OS3153__

__RN74__

__Regra p/ registro Documentos Fiscais Recebidos – CEP__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente ao prestador cadastrado na nota fiscal\. \(campo 20 da SAFX04\)

__OS3153__

__RN75__

__Regra p/ importação de nova TFIX__

A rotina de importação de TFIXs e TACESs deve ser alterada para incluir a importação na nova TFIX\.

__OS3153__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

