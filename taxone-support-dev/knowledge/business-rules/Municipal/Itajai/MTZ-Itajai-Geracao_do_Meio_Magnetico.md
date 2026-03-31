# MTZ-Itajai-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-Itajai-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-12-29
- **Tamanho:** 55 KB

---

# Itajaí \- Geração do Meio Magnético

__Atenção: Regras ajustadas da OS3470\-I1 estão no novo documento de regras dos módulos municipais – DE\-PARA – Municipal\.xls\.__

__Documento disponível no diretório do CVS: documentacao funcional\\Documento Matriz\\Municipal\\Regras Gerais__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3503

Geração do Meio Magnético Itajaí

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético de Itajaí que irá conter as informações de serviços prestados e de serviços contratados\.

OS3470\-I1F

Ajuste nas regras gerais de recuperação do responsável pela retenção:Tomador ou Prestador \- Demais validadores

MUNICIPAL

Este documento tem como objetivo ajustar a regras de tipo de recolhimento e também migrar essa regra para um novo documento DE\-PARA de regras\.

OS3926\-R

Geração do Meio Magnético Itajaí \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o municípios atendido pelo validador Itajaí\.

CH11539\_2014

Tratamento no campo Série para documentos Emitidos e Recebidos

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>Este documento tem como objetivo tratar o campo Série de documentos Emitidos e Recebidos, quando não houver o preenchimento do mesmo\.

MFS\_2071

DW \- MUNICIPAL \- Itajaí – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Itajaí” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de Itajaí”\.

OS3503

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “8203” \(Itajaí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Itajaí, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3503__

__RN03__

__Estrutura de menus do módulo Itajaí:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Itajaí:

- Arquivo
- Manutenção
- Cadastro de Sócios
- Informações Econômicas
- Obrigações
	- Meio Magnético
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3503 OS3926 \- R__

__RN04__

__Regra de criação do nome do arquivo__

__ITAJAI\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __ITAJAI__: representa a obrigação que está sendo gerada, no caso Itajaí\.

       __\.txt__: extensão do arquivo\.

Ex: ITAJAI\_01012010\.txt

__OS3503__

__RN05__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Tabela Complemento de Cadastro \(Sócios e Atividades\): deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Tabela de Notas Fiscais Emitidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Tabela de Notas Fiscais Recebidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Tabela de Notas Fiscais Canceladas ou Extraviadas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Itajaí, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3503__

__MFS\_2071__

__RN06__

__Regras referentes à estrutura do Arquivo:__

O arquivo de importação deve ser feito no formato texto \(\.txt\), com delimitadores de campo\. O delimitador utilizado é o “\#” \(sustenido\)\. A primeira coluna de cada deve identificar a tabela que está sendo importada, conforme segue:

10 = Tabela de Cadastro de Pessoas \(Físicas e Jurídicas\)

11 = Tabela de Complemento do Cadastro \(Sócios e Atividades\)

20 = Tabela de Notas Fiscais Emitidas

21 = Tabela de Itens das Notas Fiscais Emitidas

30 = Tabela de Notas Fiscais Recebidas

31 = Tabela de Itens de Notas Fiscais Recebidas

50 = Tabela de Notas Fiscais Canceladas / Extraviadas

60 = Tabela de Informações Econômicas Anuais \(declaração de maio\)

O arquivo não poderá conter linhas em branco\.

Números com casas decimais devem utilizar ponto \(\.\) para separar as casas decimais\.

Não deverão ser inseridos espaços \(   \) para completar o tamanho máximo dos caracteres do campo\.

Não deverá haver espaços entre os \#\. A maneira correta é \# \#, quando o campo não for obrigatório\.

Não é necessária a colocação de \# para trocar de tabela\. Deve\-se iniciar uma nova linha \(sem deixar linhas em branco\) com o número da tabela que deseja inserir os próximos registros\.

Os campos marcados comop Obrig\. na coluna Valid\. Devem ser obrigatoriamente informados\.

__OS3503__

__RN07__

__Regras referentes à formatação dos campos do Arquivo:__

__*Campos numéricos: *__apenas números, utilizando ponto \(\.\) para separar as casas decimais\. Não deve ser utilizado separador de milhar\. Ex: 10125\.20 \(dez mil, cento e vinte e cinco inteiros e vinte centésimos\)

__*Campos Inteiros: *__Apenas números, mas sem decimais\. Ex: 120 \(centro e vinte inteiros\)

__*String: *__Caracteres texto\.

__*Data:*__ Data, no formato DD/MM/AAAA\. Ex: 31/03/2011

__OS3503__

__RN08__

__Regra geral p/ Registro 10: Tabela de Cadastro – Contribuinte / Fornecedor / Cliente__

A primeira linha desse registro deve ser obrigatoriamente uma linha do tipo EMC, recuperando as informações da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

As demais linhas desse registros devem ser do tipo EIM ou EFM, recuperando as informações da tabela X04\_PESSOA\_FIS\_JUR referente as pessoas fis/jur cadastradas nas notas fiscais\.

Obs: Apenas devem ser recuperadas nesse registro as pessoas fis/jur que estão relacionadas nas notas fiscais informadas nos demais registros\.

Ex: 

1012345678912345EMC\.\.\.

1098765432114554EIM\.\.\.

1098765432114554EFM\.\.\.

1098765432114554EIM\.\.\.

1098765432114554EIM\.\.\.

__OS3503__

__RN09__

__Regra p/ campo 10 – Identificador de Tabela__

Preencher com “10”\.

__OS3503__

__RN10__

__Regra p/ campo 10 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN11__

__Regra p/ o campo 10 – Tipo de Cadastro__

A primeira linha do arquivo deve ser preenchida com “EMC”\.

As demais linhas devem ser preenchidas com:

“EIM”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual a Itajaí\.

“EFM”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for diferente de Itajaí\.

__OS3503__

__RN12__

__Regra p/ o campo 10 – Inscrição Municipal__

Se o Tipo de Cadastro = “EMC”, preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN13__

__Regra p/ o campo 10 – Razão Social / Nome __

Se o Tipo de Cadastro = “EMC”, preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN14__

__Regra p/ o campo 10 – Nome Fantasia__

Se o Tipo de Cadastro = “EMC”, preencher com o campo NOME\_FANTASIA da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN15__

__Regra p/ o campo 10 – Logradouro__

Se o Tipo de Cadastro = “EMC”, preencher com o campo ENDERECO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN16__

__Regra p/ o campo 10 – Número do Logradouro__

Se o Tipo de Cadastro = “EMC”, preencher com o campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN17__

__Regra p/ o campo 10 – Complemento __

Se o Tipo de Cadastro = “EMC”, preencher com o campo COMPL\_ENDERECO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN18__

__Regra p/ o campo 10 – Bairro __

Se o Tipo de Cadastro = “EMC”, preencher com o campo BAIRRO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN19__

__Regra p/ o campo 10 – Município __

Se o Tipo de Cadastro = “EMC”, preencher com o campo CIDADE da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN20__

__Regra p/ o campo 10 – CEP __

Se o Tipo de Cadastro = “EMC”, preencher com o campo CEP da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN21__

__Regra p/ o campo 10 – UF __

Se o Tipo de Cadastro = “EMC”, preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN22__

__Regra p/ o campo 10 – Telefone__

Se o Tipo de Cadastro = “EMC”, preencher com o campo TELEFONE da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN23__

__Regra p/ o campo 10 – Fax __

Se o Tipo de Cadastro = “EMC”, preencher com o campo FAX da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo FAX da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN24__

__Regra p/ o campo 10 – E\-mail __

Se o Tipo de Cadastro = “EMC”, preencher com o campo E\_MAIL da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN25__

__Regra p/ o campo 10 – Home Page__

Preencher com brancos\.

__OS3503__

__RN26__

__Regra p/ o campo 10 – Código Município__

Se o Tipo de Cadastro = “EMC”, preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Se o Tipo de Cadastro = “EIM” ou “EFM”, preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3503__

__RN27__

__Regra geral p/ Registro 11: Tabela de Complemento de Cadastro \(Sócios e Atividades\)__

Recuperar as informações cadastradas na tela Manutenção – Cadastro de Sócios para o estabelecimento escolhido na tela de geração\.

Essa tabela complementa a tabela 10\. Nela devem constar os dados do sócio responsável\.

__OS3503__

__RN28__

__Regra p/ o campo 11 – Identificador de Tabela__

Preencher com “11”\.

__OS3503__

__RN29__

__Regra p/ o campo 11 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN30__

__Regra p/ o campo 11 – Nome do Sócio Responsável__

Preencher com o campo Nome da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN31__

__Regra p/ o campo 11 – CNPJ/CPF do Sócio Responsável__

Preencher com o campo CNPJ/CPF da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN32__

__Regra p/ o campo 11 – Logradouro do Sócio__

Preencher com o campo Logradouro da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN33__

__Regra p/ o campo 11 – Número do Sócio__

Preencher com o campo Número da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN34__

__Regra p/ o campo 11 – Complemento do Sócio__

Preencher com o campo Complemento da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN35__

__Regra p/ o campo 11 – Bairro do Sócio__

Preencher com o campo Bairro da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN36__

__Regra p/ o campo 11 – Cidade do Sócio__

Preencher com o campo Cidade da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN37__

__Regra p/ o campo 11 – CEP do Sócio__

Preencher com o campo CEP da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN38__

__Regra p/ o campo 11 – UF Sócio__

Preencher com o campo UF da tela Manutenção – Cadastro de Sócios\.

__OS3503__

__RN39__

__Regra geral p/ Registro 20: Tabela de Notas Fiscais Emitidas__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar Tabela de Notas Fiscais Emitidas” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Situação <> ‘S’ 

Essa tabela refere\-se aos documentos fiscais emitidos pelo declarante \(serviços prestados\)\. Sempre que informado um registro do tipo 20, o arquivo de importação deverá trazer pelo menos um ou mais registros do tipo 21 correspondentes\.

__OS3503__

__RN40__

__Regra p/ o campo 20 – Identificador da Tabela__

Preencher com “20”

__OS3503__

__RN41__

__Regra p/ o campo 20 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN42__

__Regra p/ o campo 20 – Série da Nota Fiscal__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>__\[CH11539\_2014\]__

__Tratamento:__

Quando não houver o preenchimento da série no documento fiscal, ou seja, campo igual null ou branco, deve ser preenchido no arquivo magnético igual a “0”\.

__OS3503__

__CH11539\_2014__

__RN43__

__Regra p/ o campo 20 – Nº da Nota Fiscal__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3503__

RN44

__Regra p/ o campo 20 – CNPJ/CPF do Cliente__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. Quando esse campo não estiver preenchido deve\-se preencher com o número 9 \(nove, apenas um dígito\)\.

OS3503

__RN45__

__Regra p/ o campo 20 – Data de Emissão da Nota Fiscal__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: DD/MM/AAAA\.

__OS3503__

__RN46__

__Regra p/ o campo 20 – CFPS__

Preencher com “0” \(zero\)\.

__OS3503__

__RN47__

__Regra p/ o campo 20 – Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN48__

__Regra p/ o campo 20 – Valor da Base de Cálculo ISS__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN49__

__Regra p/ o campo 20 – Valor do ISS Retido na Fonte__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN50__

__Regra p/ o campo 20 – Valor da Base de Cálculo do ISS Retido na Fonte__

Preencher com o somatório do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN51__

__Regra p/ o campo 20 – Valor Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN52__

__Regra p/ o campo 20 – Valor das Mercadorias__

Preencher com 0 \(zero\)\.

__OS3503__

__RN53__

__Regra p/ o campo 20 – Valor Total da Nota Fiscal__

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN54__

__Regra p/ o campo 20 – Nota Fiscal Complementar?__

Preencher com “N”\.

__OS3503__

__RN55__

__Regra p/ o campo 20 – Local da Prestação do Serviço__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido,  preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o numero da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3503__

__RN56__

__Regra geral p/ Registro 21: Tabela de Itens das Notas Fiscais Emitidas__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar Tabela de Notas Fiscais Emitidas” estiver marcado e deve conter todos os itens das notas fiscais com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Situação <> ‘S’ 

Essa tabela também refere\-se aos documentos fiscais emitidos pelo declarante, complementando a tabela 20\. Para informar um registro do tipo 21, já deve haver um registro do tipo 20 correspondente numa linha anterior\. Poderão constar um ou mais registros do tipo 21 para cada registro do tipo 20, sendo que o valor total deles deve bater com o valor informado no registro 20\.

__OS3503__

__RN57__

__Regra p/ o campo 21 – Identificador de Tabela__

Preencher com “21”\.

__OS3503__

__RN58__

__Regra p/ o campo 21 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN59__

__Regra p/ o campo 21 – Série da NF Emitida__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[CH11539\_2014\]__

__Tratamento:__

Quando não houver o preenchimento da série no documento fiscal, ou seja, campo igual null ou branco, deve ser preenchido no arquivo magnético igual a “0”\.

__OS3503__

__CH11539\_2014__

__RN60__

__Regra p/ o campo 21 – Nº da NF Emitida__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3503__

__RN61__

__Regra p/ o campo 21 – Item da NF__

Preencher com o campo NUM\_ITEM da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN62__

__Regra p/ o campo 21 – Descrição do Serviço__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código do serviço cadastrado no item da nota fiscal\.

__OS3503__

__RN63__

__Regra p/ o campo 21 – Alíquota do ISS__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN64__

__Regra p/ o campo 21 – Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN65__

__Regra p/ o campo 21 – Valor do Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN66__

__Regra p/ o campo 21 – Código do Item da Lista de Serviços__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

__OS3503__

__RN67__

__Regra p/ o campo 21 – Código da Situação Tributária__

Preencher com:

14, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “01” ou “04”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

18, quando o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

19, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

15, quando:

- O local da prestação de serviço <> Itajaí \(vide regra de local da prestação – RN67\.a\)
- Pelo menos umas das seguintes opções seja verdadeira:
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

OS3503

__RN67__

__Regra p/ o campo 21 – Código da Situação Tributária \(cont\.\)__

10, quando:

- o campo IND\_ISS da tabela ESTABELECIMENTO = “07”
- Pelo menos umas das seguintes opções seja verdadeira:
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

11, quando pelo menos umas das seguintes opções seja verdadeira:

- 
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

17, quando:

- o campo IND\_ISS da tabela ESTABELECIMENTO = “07”
- Nenhuma das seguintes opções seja verdadeira:
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

12, quando:

- O COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR = Itajaí
- Nenhuma das seguintes opções seja verdadeira:
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

13, quando:

- O COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR <> Itajaí
- Nenhuma das seguintes opções seja verdadeira:
	- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
	- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
	- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

16, não será tratado\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3503__

__OS\-3470\-I1F__

__RN67\.a__

__Regra Local da Prestação__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o numero da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Senão recuperar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3503__

__RN68__

__Regra geral p/ Registro 30: Tabela de Notas Fiscais Recebidas__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Situação <> ‘S’ 

Quando a nota não tiver itens não deve ser recuperada\.

Essa tabela refere\-se aos documentos fiscais recebidos pelo declarante \(serviços tomados\)\. Sempre que informado um registro do tipo 30, o arquivo de importação deverá trazer pelo menos um ou mais registros do tipo 31 correspondentes\.

__OS3503__

__RN69__

__Regra p/ o campo 30 – Identificador da Tabela__

Preencher com “30”

__OS3503__

__RN70__

__Regra p/ o campo 30 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN71__

__Regra p/ o campo 30 – Série da Nota Fiscal__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[CH11539\_2014\]__

__Tratamento:__

Quando não houver o preenchimento da série no documento fiscal, ou seja, campo igual null ou branco, deve ser preenchido no arquivo magnético igual a “0”\.

__OS3503__

__CH11539\_2014__

__RN72__

__Regra p/ o campo 30 – Nº da Nota Fiscal__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3503__

__RN73__

__Regra p/ o campo 30 – CNPJ/CPF do Fornecedor__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. Quando esse campo não estiver preenchido deve\-se preencher com o número 9 \(nove, apenas um dígito\)\.

__OS3503__

__RN74__

__Regra p/ o campo 30 – Data de Emissão da Nota Fiscal__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: DD/MM/AAAA\.

__OS3503__

__RN75__

__Regra p/ o campo 30 – CFPS__

Preencher com “0” \(zero\)\.

__OS3503__

__RN76__

__Regra p/ o campo 30 – Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN77__

__Regra p/ o campo 30 – Valor da Base de Cálculo ISS__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN78__

__Regra p/ o campo 30 – Valor do ISS Retido na Fonte__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN79__

__Regra p/ o campo 30 – Valor da Base de Cálculo do ISS Retido na Fonte__

Preencher com o somatório do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN80__

__Regra p/ o campo 30 – Valor Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN81__

__Regra p/ o campo 30 – Valor das Mercadorias__

Preencher com 0 \(zero\)\.

__OS3503__

__RN82__

__Regra p/ o campo 30 – Valor Total da Nota Fiscal__

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL\. Se não houver, preencher com 0 \(zero\)\.

__OS3503__

__RN83__

__Regra p/ o campo 30 – Nota Fiscal Complementar?__

Preencher com “N”\.

__OS3503__

__RN84__

__Regra p/ o campo 30 – Local da Prestação do Serviço__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido,  preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o numero da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(completando com zero até as 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3503__

__RN85__

__Regra geral p/ Registro 31: Tabela de Itens das Notas Fiscais Recebidas__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar Tabela de Notas Fiscais Recebidas” estiver marcado e deve conter todos os itens das notas fiscais com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Situação <> ‘S’ 

Essa tabela também refere\-se aos documentos fiscais recebidos pelo declarante, complementando a tabela 30\. Para informar um registro do tipo 31, já deve haver um registro do tipo 20 correspondente numa linha anterior\. Poderão constar um ou mais registros do tipo 31 para cada registro do tipo 30, sendo que o valor total deles deve bater com o valor informado no registro 30\.

__OS3503__

__RN86__

__Regra p/ o campo 31 – Identificador de Tabela__

Preencher com “31”

__OS3503__

__RN87__

__Regra p/ o campo 31 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN88__

__Regra p/ o campo 31 – Série da NF Recebida__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[CH11539\_2014\]__

__Tratamento:__

Quando não houver o preenchimento da série no documento fiscal, ou seja, campo igual null ou branco, deve ser preenchido no arquivo magnético igual a “0”\.

__OS3503__

__CH11539\_2014__

__RN89__

__Regra p/ o campo 31 – Nº da NF Recebida__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3503__

__RN90__

__Regra p/ o campo 31 – Item da NF__

Preencher com o campo NUM\_ITEM da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN91__

__Regra p/ o campo 31 – CNPJ/CPF do Fornecedor__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal

__OS3503__

__RN92__

__Regra p/ o campo 31 – Descrição do Serviço__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código do serviço cadastrado no item da nota fiscal\.

__OS3503__

__RN93__

__Regra p/ o campo 31 – Alíquota do ISS__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN94__

__Regra p/ o campo 31 – Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN95__

__Regra p/ o campo 31 – Valor do Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__OS3503__

__RN96__

__Regra p/ o campo 31 – Código do Item da Lista de Serviços__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

__OS3503__

__RN97__

__Regra p/ o campo 31 – Código da Situação Tributária__

Preencher com:

25, quando nenhuma das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

24, quando:

- O local da prestação de serviço <> Itajaí \(vide regra de local da prestação – RN67\.a\)
- Pelo menos umas das seguintes opções seja verdadeira:
- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

21, quando:

- O COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR = Itajaí
- Pelo menos uma das seguintes opções seja verdadeira:
- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

22, quando:

- O COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR <> Itajaí
- Pelo menos uma das seguintes opções seja verdadeira:
- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

23, não será tratada\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(R1\-RN0001\)__

__OS3503__

__OS3470\-I1F__

__RN98__

__Regra geral p/ Registro 50: Tabela de Notas Fiscais Canceladas ou Extraviadas__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar Tabela de Notas Fiscais Canceladas ou Extraviadas” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Situação = ‘S’ ou IND\_NOTA\_SERVICO = ‘E’

 Essa tabela deve trazer informações sobre Notas Fiscais de Serviços Emitidas que foram Canceladas \(documentos estão com o contribuinte mas foram inutilizadas por algum motivo\) ou Extraviadas \(documentos foram perdidos, furtados ou roubados\)\.

__OS3503__

__RN99__

__Regra p/ o campo 50 – Identificador de Tabela__

Preencher com “50”

__OS3503__

__RN100__

__Regra p/ o campo 50 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN101__

__Regra p/ o campo 50 – Série da NF Emitida__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[CH11539\_2014\]__

__Tratamento:__

Quando não houver o preenchimento da série no documento fiscal, ou seja, campo igual null ou branco, deve ser preenchido no arquivo magnético igual a “0”\.

__OS3503__

__CH11539\_2014__

__RN102__

__Regra p/ o campo 50 – Nº da NF Emitida__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3503__

__RN103__

__Regra p/ o campo 50 – Tipo de Anulação__

Preencher com:

EXTRAVIADA, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’

CANCELADA, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”

__OS3503__

__RN104__

__Regra p/ o campo 50 – Data do Cancelamento ou Extravio__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: DD/MM/AAAA\.

__OS3503__

__RN105__

__Regra p/ o campo 50 – Observações__

Não será preenchido\.

__OS3503__

__RN106__

__Regra geral p/ Registro 60: Tabela de Informações Econômicas \(Anuais\)__

Recuperar as informações cadastradas na tela Manutenção – Informações Econômicas para o estabelecimento escolhido na tela de geração\.

Essa tabela deve trazer informações sobre a declaração anual de informações econômicas\. Esse tipo de registro deve ser informado apenas na declaração de maio de cada ano, e se refere ao ano imediatamente anterior\. Essa tabela é obrigatória apenas a partir do ano de 2012\.

__OS3503__

__RN107__

__Regra p/ o campo 60 – Identificador de Tabela__

Preencher com “60”

__OS3503__

__RN108__

__Regra p/ o campo 60 – CNPJ/CPF Declarante__

Preencher com o campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento escolhido na tela de geração\.

__OS3503__

__RN109__

__Regra p/ o campo 60 – Ano__

Preencher com o campo Ano da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN110__

__Regra p/ o campo 60 – Total Despesas__

Preencher com o campo Total Despesas da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN111__

__Regra p/ o campo 60 – Outras Receitas__

Preencher com o campo Outras Receitas da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN112__

__Regra p/ o campo 60 – Valor do Ativo__

Preencher com o campo Valor do Ativo da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN113__

__Regra p/ o campo 60 – Valor do Passivo__

Preencher com o campo Valor do Pasivo da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN114__

__Regra p/ o campo 60 – Patrimônio Líquido__

Preencher com o campo Patrimônio Líquido da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN115__

__Regra p/ o campo 60 – Capital Social__

Preencher com o campo Capital Social da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN116__

__Regra p/ o campo 60 – Número de empregados no primeiro dia de janeiro__

Preencher com o campo Número de empregados no primeiro dia de janeiro da tela Manutenção – Informações Econômicas\.

__OS3503__

__RN117__

__Regra p/ o campo 60 – Número de empregados no último dia de dezembro__

Preencher com o campo Número de empregados no último dia de dezembro da tela Manutenção – Informações Econômicas\.

__OS3503__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

