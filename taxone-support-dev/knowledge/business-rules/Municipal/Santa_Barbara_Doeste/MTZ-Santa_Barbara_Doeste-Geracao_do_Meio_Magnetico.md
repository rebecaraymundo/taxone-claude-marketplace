# MTZ-Santa_Barbara_Doeste-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-Santa_Barbara_Doeste-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 50 KB

---

# Santa Bárbara D'Oeste \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3394

Geração do Meio Magnético Santa Bárbara D’Oeste

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético Santa Bárbara D’Oeste que irá conter as informações de serviços prestados e de serviços contratados, assim como RPS e Serviços Bancários\.

OS3926\-V

Geração do Meio Magnético Santa Barbara D’oeste \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o município atendido pelo validador STA BARBARA\.

__OS3341\-A4__

Geração do Meio Magnético para nota fiscais com número de documento com mais de 12 posições\.  

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

__MFS\_2071__

DW \- MUNICIPAL – Santa Bárbara D’Oeste – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO 

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Santa Bárbara D’Oeste” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de Santa Bárbara D’Oeste”\.

__OS3394__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “45803” \(Santa Bárbara D’Oeste\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Santa Bárbara D’Oeste, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3394__

__RN03__

__Estrutura de menus do módulo __Santa Bárbara D’Oeste__:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Santa Bárbara D’Oeste:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Geração do Meio Magnético – RPS 
	- Geração do Meio Magnético – Bancos 
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3394 OS3926\-V__

__RN04__

__Regra de criação do nome do arquivo__

__SANTA\_BARBARA\_DOESTE\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __SANTA\_BARBARA\_DOESTE__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: SANTA\_BARBARA\_DOESTE\_01012010\.txt

__OS3394__

__RN05__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Notas Emitidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Notas Recebidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Santa Bárbara D’Oeste, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3394__

__MFS\_2071__

__RN06__

__Regras referentes à formatação dos registros gerados no meio magnético:__

As informações dos campos deverão vir separadas por um identificador\. Utilizaremos o separador | \(pipe\)\. Como as colunas são separadas por um delimitador, não é necessário que os campos sejam completados com zeros à esquerda \(no caso de campos numéricos\), nem com brancos no final \(no caso de campos alfanuméricos\)\.

Se não possuir a informação de algum campo, basta deixar vazio \(no caso de campo alfanumérico\) ou informar zero \(caso de campo numérico\)\.

Ex: 2201|2|1|||100\.\.\.

__OS3394__

__RN07__

__Regra p/ Recuperar notas fiscais de serviços prestados__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar notas emitidas” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

__OS3394__

__RN08__

__Regra p/ Recuperar notas fiscais de serviços contratados__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar notas recebidas” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

__OS3394__

__RN09__

__Regra p/ o campo Identificação do prestador__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente a pessoa fis/jur cadastrada na nota\. Se esse campo não estiver preenchido, preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

__OS3394__

__RN10__

__Regra p/ o campo Tipo identificação__

Preencher com:

“0”, se o campo CGC da tabela ESTABELECIMENTO estiver preenchido e tiver 14 posições\.

“1”, não será tratado\.

“2”, se o campo CGC da tabela ESTABELECIMENTO não estiver preenchido e o campo INSC\_MUNICIPAL estiver preenchido\.

__OS3394__

__RN11__

__Regra p/ o campo Tipo__

Preencher com:

“1”, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = ‘9’

“2”, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> ‘9’

__OS3394__

__RN12__

__Regra p/ o campo Número __

__Tela\-A__ 🡸__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3394__

__OS3341\-A4__

__RN13__

__Regra p/ o campo Série \(emitida\)  ou documento fiscal \(recebida\)__

Para notas emitidas:

Preencher de acordo com a parametrização de séries realizada no menu Parâmetros por Município – Série Msaf x Série\.

Para notas recebidas:

Preencher de acordo com a parametrização de tipo de documento realizada no menu Parâmetros por Município – Tipo Docto Msaf x Tipo Docto

__OS3394__

__RN14__

__Regra p/ o campo Data de emissão da nota __

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: AAAAMMDD\.

__OS3394__

__RN15__

__Regra p/ o campo Mês de referência__

Preencher com o mês informado no campo Data Inicial da tela de geração do meio magnético\. Formato: MM\.

__OS3394__

__RN16__

__Regra p/ o campo Ano de referência__

Preencher com o ano informado no campo Data Inicial da tela de geração do meio magnético\. Formato: AAAA\.

__OS3394__

__RN17__

__Regra p/ o campo Status__

Para notas emitidas

Preencher com:

“1”, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’

“2”, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

Para notas recebidas, preencher com “0”\.

__OS3394__

__RN18__

__Regra p/ o campo Data do cancelamento __

Preencher com o campo DAT\_CANCELAMENTO da tabela DWT\_DOCTO\_FISCAL\. Formato: AAAAMMDD\.

__OS3394__

__RN19__

__Regra p/ o campo Natureza da Operação __

Preencher com:

“1”, quando o campo COD\_CLASS\_DOC\_FIS = ‘2’

“2”, quando o campo COD\_CLASS\_DOC\_FIS = ‘3’

__OS3394__

__RN20__

__Regra p/ o campo Valor Total __

Preencher com o somatório do campo VRL\_TOT da tabela DWT\_ITENS\_SERV\. Campo numérico com 11 casas, sendo que duas representam os decimais\. Valor sem separador de decimais \(, ou \.\)

__OS3394__

__RN21__

__Regra p/ o campo Valor dos Serviços__

Preencher com o somatório do campo VRL\_SERVICO da tabela DWT\_ITENS\_SERV\. Campo numérico com 11 casas, sendo que duas representam os decimais\. Valor sem separador de decimais \(, ou \.\)

__OS3394__

__RN22__

__Regra p/ o campo Valor dos impostos__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Campo numérico com 11 casas, sendo que duas representam os decimais\. Valor sem separador de decimais \(, ou \.\)

__OS3394__

__RN23__

__Regra p/ o campo Recolhimento do imposto__

__*Para notas emitidas:*__

Preencher com:

“0”, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

“1”, quando pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. E1\-RN0001

“2”, não será tratado

“3”, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “07”

__*Para notas recebidas:*__

Preencher com:

“1”, Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “”\.

“2”, Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “”\.

“4”, Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “”\.

Se nenhuma das situações acima for atendida, sistema deve exibir no log a seguinte mensagem: O campo “Recolhimento do Imposto'' é um campo obrigatório e não está preenchido\. Favor verificar\.'

__OS3394__

__OS3470\-I1D__

__RN24__

__Regra p/ o campo Atividade__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo COD\_SERVICO da tabela X2018\_SERVICOS referente ao serviço cadastrado no item\.

__OS3394__

__RN25__

__Regra p/ o campo Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3394__

__RN26__

__Regra p/ o campo Razão social prestador__

Para notas emitidas:

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

Para notas recebidas:

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3394__

__RN27__

__Regra p/ o campo Cidade prestador__

Para notas emitidas:

Preencher com o campo CIDADE da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

Para notas recebidas:

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3394__

__RN28__

__Regra p/ o campo UF prestador__

Para notas emitidas:

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela ESTABELECIMENTO\.

Para notas recebidas:

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3394__

__RN29__

__Regra p/ o campo Local Prestador__

Para notas emitidas:

Preencher com:

“0”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual a “Santa Bárbara D’Oeste”

“1”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for diferente de “Santa Bárbara D’Oeste”

“2”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO não estiver preenchido\.

Para notas recebidas:

Preencher com:

“0”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual a “Santa Bárbara D’Oeste”

“1”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for diferente de “Santa Bárbara D’Oeste”

“2”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.

__OS3394__

__RN30__

__Regra p/ o campo Identificação tomador__

Para notas emitidas:

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. Se esse campo não estiver preenchido, preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

Para notas recebidas:

Preencher com o campo CGC da tabela ESTABELECIMENTO\. Se esse campo não estiver preenchido, preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

__OS3394__

__RN31__

__Regra p/ o campo Tipo identificação tomador__

Para notas emitidas:

Preencher com:

“0”, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR estiver preenchido e tiver 14 posições\.

“1”, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR estiver preenchido e tiver 11 posições\.

“2”, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido e o campo INSC\_MUNICIPAL estiver preenchido\.

Para notas recebidas:

Preencher com:

“0”, se o campo CGC da tabela ESTABELECIMENTO estiver preenchido e tiver 14 posições\.

“1”, não será tratado\.

“2”, se o campo CGC da tabela ESTABELECIMENTO não estiver preenchido e o campo INSC\_MUNICIPAL estiver preenchido\.

__OS3394__

__RN34__

__Regra p/ o campo Razão Social tomador__

Para notas emitidas:

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Para notas recebidas:

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

__OS3394__

__RN35__

__Regra p/ o campo Cidade Tomador__

Para notas emitidas:

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Para notas recebidas:

Preencher com o campo CIDADE da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

__OS3394__

__RN36__

__Regra p/ o campo UF Tomador__

Para notas emitidas:

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Para notas recebidas:

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela ESTABELECIMENTO\.

__OS3394__

__RN37__

__Regra p/ o campo Local Tomador__

Para notas emitidas:

Preencher com:

“0”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual a “Santa Bárbara D’Oeste”

“1”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for diferente de “Santa Bárbara D’Oeste”

“2”, quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.

“3”, não será tratado

Para notas recebidas:

Preencher com:

“0”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual a “Santa Bárbara D’Oeste”

“1”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for diferente de “Santa Bárbara D’Oeste”

“2”, quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO não estiver preenchido\.

“3”, não será tratado

__OS3394__

__RN38__

__Regra p/ o campo RPS__

Não será tratado\.

__OS3394__

__RN39__

__Regra p/ o campo RPS Tipo__

Não será tratado\.

__OS3394__

__RN40__

__Regra p/ o campo RPS Série__

Não será tratado\.

__OS3394__

__RN41__

__Regra p/ o campo Hora__

Não será tratado\.

__OS3394__

__RN42__

__Regra p/ o campo RPS Data__

Não será tratado\.

__OS3394__

__RN43__

__Regra p/ o campo Hashcode__

Não será tratado\.

__OS3394__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

