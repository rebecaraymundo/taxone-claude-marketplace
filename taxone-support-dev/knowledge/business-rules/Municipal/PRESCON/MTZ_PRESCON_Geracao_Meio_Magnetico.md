# MTZ_PRESCON_Geracao_Meio_Magnetico

- **Fonte:** MTZ_PRESCON_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-03-09
- **Tamanho:** 120 KB

---

THOMSON REUTERS

Municipal

PRESCON \- <a id="_Hlk515023597"></a>Sistema de NFS\-e \- Desenvolvido por Prescon Informática

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-18480

Julyana Perrucini

Alteração do município Artur Nogueira/ SP que será atendido a partir do validador da PRESCON\.

MFS\-19971

Julyana Perrucini

Alteração do município Ubatuba/ SP que será atendido a partir do validador da PRESCON\.

MFS\-21211

João Henrique

Inclusão do município Campos do Jordão que será atendido a partir do validador da PRESCON\.

MFS\-60904

Rogério Ohashi

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de Campos do Jordão, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\. \( RN56\.a\)

MFS\-62575

Andréa Rocha

Inclusão de parâmetro para indicar a forma de preencher a tag <numeroNotaFiscal>\.

MFS\-71795

Rogério Ohashi

Tratamento da forma de preenchimento da tag <devidoForaMunic>, específico para o Município de Campos do Jordão\.

MFS\-97892

Elisabete Costa

Inclusão do município de Vinhedo que será atendido a partir do validador da PRESCON

MFS\-751724

Bruna Ribeiro

Esta demanda tem como objetivo incluirmos a tag <codigoatividade> para o município de Vinhedo/SP \- Validador Prescon\. 

__MFS\-839887__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1065315__

Rosemeire Santos

Este documento tem como objetivo, incluir o município de Rio Grande da Serra\-SP, no validador PRESCON\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Estrutura de menus do módulo PRESCON:__

Deverão ser criados os seguintes menu e sub\-menus no módulo PRESCON:

- Arquivo    
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS\-18480

RN02

__Regra de criação do nome do arquivo__

Em cada arquivo magnético é permitido até 250 notas fiscais, então a cada 250 notas atingidas dentro do arquivo o mesmo deverá ser quebrado em vários e gerar uma sequencial, assim como, tratamos para o município de Indaiatuba, entre outros\. 

__Serviços Prestados:__

__ SP\_PRESCON EMPRESA\_ ESTABELECIMENTO\_MUNICIPIO\_DDMMAAAA\_SEQ\.XML__, onde:

__      SP__: representa a obrigação que está sendo gerada\. Apenas registros de serviços prestados

__       EMPRESA: __Representa o prestador de serviço

__       ESTABELECIMENTO: __Representa o prestador de serviço

       __MUNICIPIO__: representa o município que está sendo gerado

       __DDMMAAAA__: representa a data inicial da geração

       __SEQ__: representa a sequência de quebra do arquivo quando atingida mais de 250 notas fiscais

       __\.XML__: extensão do arquivo\.

*Exemplo:* SP\_PRESCONEMPRESA\_ESTABELECIMENTO\_ARTUR\_NOGUEIRA\_01012010\_1\.XML

__Serviços Tomados:__

__ST\_PRESCONEMPRESA\_ ESTABELECIMENTO\_MUNICIPIO\_DDMMAAAA\_SEQ\.XML__, onde:

__       EMPRESA: __Representa o tomador de serviço

__       ESTABELECIMENTO: __Representa o tomador de serviço

      __ST__: Representa a obrigação que está sendo gerada\.

       __MUNICIPIO__: representa o município que está sendo gerado

       __DDMMAAAA__: representa a data inicial da geração

       __SEQ__: representa a sequência de quebra do arquivo quando atingida mais de 250 notas fiscais

       __\.XML__: extensão do arquivo\.

*Exemplo:* ST\_PRESCON\_EMPRESA\_ESTABELECIMENTO\_ARTUR\_NOGUEIRA\_01012010\_1\.XML

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_PRESCON EMPRESA\_ ESTABELECIMENTO\_MUNICIPIO\_DDMMAAAA\_SEQ\_MMAAAA\.XML__, onde:

__       EMPRESA: __Representa o tomador de serviço

__       ESTABELECIMENTO: __Representa o tomador de serviço

__        ST__: Representa a obrigação que está sendo gerada

__        MUNICIPIO__: Representa o município que está sendo gerado

        __DDMMAAAA__: Representa a data inicial da geração

        __SEQ__: Representa a sequência de quebra do arquivo quando atingida mais de 250 notas fiscais

__        MMAAAA:__ Mês da competência referente à nota gerada

        __\.XML__: Extensão do arquivo\.

Ex: ST\_PRESCON\_EMPRESA\_ESTABELECIMENTO\_ARTUR\_NOGUEIRA\_01012014\_1\_122013\.XML

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-18480

__MFS\-839887__

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Data Envio Arquivo:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o campo zerado para preenchimento do usuário\.

__Gerar Serviços Prestados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__\[MFS62575\] __Inclusão do parâmetro para definir a forma de gerar o número do documento fiscal

__Considerar 6 Últimas Posições da Nota Fiscal:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__*Tratamentos:* __

- Cada campo padrão deverá exibir mensagens existentes caso de não preenchimento;
- O campo “Data Envio Arquivo” é novo e seu preenchimento é obrigatório, caso não for preenchido emitir a mensagem de aviso na tela: *“Informe Data Envio Arquivo\.”\.*

MFS\-18480

MFS\-62575

RN04

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos:

O arquivo a ser gerado para importação dever ser no formato __‘XML’\.__

- Campos de valor que não houver preenchimento, gravar “0\.00”;
- Campos numéricos que não houver preenchimento, gravar “0”;
- Campos alfanuméricos que não possuírem informação deixar TAGS vazias\.

MFS\-18480

RN05

__Regra p/ Recuperação das notas fiscais de serviços prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Prestados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

O agrupamento deve ocorrer por <aliquotaIss>, <descricaoServico> e <devido>\.

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-18480

RN06

__Estrutura do Arquivo:__

<?xml version="1\.0" encoding="ISO\-8859\-1"?>

<retencao>

	<lancamento>

		<servico>P</servico>

		<devido>DP</devido>

		<codigoNotaFiscal></codigoNotaFiscal>

		<numeroNotaFiscal>111111</numeroNotaFiscal>

		<dataNotaFiscal>30/05/2014</dataNotaFiscal>

		<logradouroServico>RUA TESTE 1</logradouroServico>

		<numeroServico>120</numeroServico>

		<complementoServico>SALA 5</complementoServico>

		<bairroServico>JARDIM AMERICA</bairroServico>

		<cidadeServico>UBATUBA</cidadeServico>

		<estadoServico>SP</estadoServico>

		<cepServico>11680\-000</cepServico>

		<descricaoServico>Serviço de desenvolvimento de portais Web\.</descricaoServico>

		<dataArquivo>15/01/2014</dataArquivo>

		<valorServico>900\.00</valorServico>

		<valorAbatimentoLegal>0\.00</valorAbatimentoLegal>

		<aliquotaIss>2\.00</aliquotaIss>

		<tipoDocumentoPrestador>J</tipoDocumentoPrestador>

		<documentoPrestador>26\.782\.918/0001\-23</documentoPrestador>

		<nomePrestador>Info Solution Informatica</nomePrestador>

		<logradouroPrestador>Rua das Valquirias</logradouroPrestador>

		<numeroPrestador>1234</numeroPrestador>

		<complementoPrestador>Sala 5</complementoPrestador>

		<bairroPrestador>Vale do Silicio</bairroPrestador>

		<cidadePrestador>Belo Horizonte</cidadePrestador>

		<estadoPrestador>MG</estadoPrestador>

		<cepPrestador>11963\-300</cepPrestador>

		<telefonePrestador>38324963</telefonePrestador>

		<emailPrestador>teste@gmail\.com</emailPrestador>

		<tipoDocumentoTomador>J</tipoDocumentoTomador>

		<documentoTomador>14\.046\.166/0001\-53</documentoTomador>

		<nomeTomador>Sondas Espaciais SA</nomeTomador>

		<logradouroTomador>Ruas das Aboboras</logradouroTomador>

		<numeroTomador>741</numeroTomador>

		<complementoTomador>Sala 5</complementoTomador>

		<bairroTomador>Novo Poder</bairroTomador>

		<cidadeTomador>Caraguatatuba</cidadeTomador>

		<estadoTomador>SP</estadoTomador>

		<cepTomador>11680\-900</cepTomador>

		<telefoneTomador>12997336252</telefoneTomador>

		<emailTomador>tomador@gmail\.com</emailTomador>

		<devidoForaMunic>0</devidoForaMunic>

	</lancamento>

</retencao>

MFS\-18480

RN07

__Regra p/ o cabeçalho do arquivo:__

Preencher com o tag <?xml version="1\.0" encoding="ISO\-8859\-1"?>

MFS\-18480

RN08

__Regra para tag <retencao> __Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas fiscais declaradas com o texto fixo: __<retencao>\.__

TAG obrigatória\.

MFS\-18480

RN09

__Regra para tag <lancamento> __Tag relacionada à abertura dos dados de lançamento do serviço com o texto fixo: __<lancamento>\.__

TAG obrigatória\.

MFS\-18480

RN10

__Regra p/ tag <servico> </servico>__

Identifica o tipo de serviço\.

Preencher com:

“__P__” para serviços prestados de acordo com o critério de seleção\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN11

__Regra p/ tag <devido> </devido>__

Identifica para quem o serviço é devido\.

Preencher com:

“__DP__”, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “__2__” e o município do local de prestação do serviço \(campo 73 da SAFX07\) for igual ao município do módulo selecionado;

“__DT__”, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “__1__” e o município do local de prestação do serviço \(campo 73 da SAFX07\) for igual ao município do módulo selecionado\.

__Tratamento:__

- Se o município do local de prestação do serviço \(campo 73 da SAFX07\) for diferente do município do módulo selecionado, gerar o campo da seguinte forma:
- “__DP__”, se a tag <servico> for igual a __P__;
- “__DT__”, se a tag <servico> for igual a __T__\.
- Além disso, deverá ser emitida a seguinte mensagem de aviso no log: *“Talvez o ISS devido esteja incorreto porque o local de prestação de serviço deve ser igual o município do estabelecimento e para essa nota fiscal consta diferente, favor verificar\! Em caso de situação específica, ignorar a mensagem\. <<NF>>, <<Série>>, <<Data Fiscal>>, <<PFJ>>, <<Local de Prestação>>”*\.

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN12

__Regra p/ tag <codigoNotaFiscal> </codigoNotaFiscal>__

Identifica o código da nota fiscal gerada pelo Prestador \(apenas preencher quando o prestador cancelar sua nota\)\.

Preencher com o conteúdo do campo COD\_MOTIVO da tabela DWT\_DOCTO\_FISCAL \(campo 138 da SAFX07\) quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) for igual a “S”\.

__Observações:__

- Não recuperamos notas fiscais canceladas nas entradas, então essa situação só será atendida para serviços prestados;
- Não emitiremos mensagem de log porque o campo é não obrigatório e não consta que pode ser obrigatório se a nota for cancelada, por esse motivo não será tratado no momento\.

Campo não obrigatório

Formato: XXXXXXXXXX

Tipo: Texto

Tamanho: 10

MFS\-18480

RN13

__Regra p/ tag <numeroNotaFiscal> </numeroNotaFiscal>__

Identifica o número da nota fiscal\.

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 06 primeiras posições;
- Se o campo ultrapassar 06 posições, emitir a mensagem de log: *“O campo número do documento ultrapassou o tamanho máximo permitido pelo layout \(06 posições\) <<Nº documento>> <<Série>> <<Data Fiscal>>\.”*\.

Campo obrigatório

Formato: 999999

Tipo: Numérico

Tamanho: 6

MFS\-18480

RN14

__Regra p/ tag <dataNotaFiscal> </dataNotaFiscal>__

Identifica a data da nota fiscal\.

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAX07\)\.

Campo obrigatório

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: 10

MFS\-18480

RN15

__Regra p/ tag <logradouroServico> </logradouroServico>__

Identifica o logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroServico é obrigatória, favor preencher endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN16

__Regra p/ tag <numeroServico> </numeroServico>__

Identifica o número do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroServico permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroServico é obrigatória, favor preencher o número do endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN17

__Regra p/ tag <complementoServico> </complementoServico>__

Identifica o complemento do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 30 primeiras posições;
- Se o campo estiver preenchido com mais de 30 posições emitir a seguinte mensagem de log:* “A TAG complementoServico permite até 30 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoServico é obrigatória, favor preencher complemento do endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN18

__Regra p/ tag <bairroServico> </bairroServico>__

Identifica o bairro do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroServico é obrigatória, favor preencher bairro da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN19

__Regra p/ tag <cidadeServico> </cidadeServico>__

Identifica a cidade do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadeServico permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadeServico é obrigatória, favor preencher cidade da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN20

__Regra p/ tag <estadoServico> </estadoServico>__

Identifica o estado do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoServico é obrigatória, favor preencher estado da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN21

__Regra p/ tag <cepServico> </cepServico>__

Identifica o estado do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepServico é obrigatória, favor preencher CEP da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN22

__Regra p/ tag <descricaoServico> </descricaoServico>__

Identifica a descrição do serviço\.

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Não é necessário preencher o restante do campo com espaços em branco\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG descricaoServico é obrigatória, favor preencher o serviço da lei 116 no serviço que foi cadastrado no item da nota fiscal\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<Nº Item>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 1000

MFS\-18480

RN23

__Regra p/ tag <dataArquivo> </dataArquivo>__

Identifica a data em que foi enviado o arquivo\.

Preencher com o conteúdo do campo Data Envio Arquivo informado na tela de geração do arquivo magnético\.

Campo obrigatório

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: 10

MFS\-18480

RN24

__Regra p/ tag <valorServico> </valorServico>__

Identifica o valor do serviço\.

Preencher com o conteúdo do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV \(campo 14 da SAFX09\)\.

__Tratamento:__

- Se o campo ultrapassar o tamanho permitido pelo layout, deverá ser truncado considerando o valor da direita para a esquerda e exibir uma mensagem de log padrão\.

Campo obrigatório

Formato: 999999999\.99

Tipo: Decimal

Tamanho: 9,2

MFS\-18480

RN25

__Regra p/ tag <valorAbatimentoLegal> </valorAbatimentoLegal>__

Identifica o valor do abatimento Legal \(somente notas emitidas com a opção de Construção Civil\)\.

Preencher com o conteúdo do campo VLR\_MAT\_PROP da tabela DWT\_ITENS\_SERV \(campo 55 da SAFX09\)\.

__Tratamento:__

- Se o campo ultrapassar o tamanho permitido pelo layout, deverá ser truncado considerando o valor da direita para a esquerda e exibir uma mensagem de log padrão\.

Campo não obrigatório \(obrigatório apenas para construção civil\)

Formato: 999999999\.99

Tipo: Decimal

Tamanho: 9,2

MFS\-18480

RN26

__Regra p/ tag <aliquotaIss> </aliquotaIss>__

Identifica a alíquota do ISS\.

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout\.
- Se o campo não estiver preenchido, preencher a TAG com “0\.00” \(zeros\) e emitir a seguinte mensagem de log: *“A TAG aliquotaIss é obrigatória, favor preencher no item da nota fiscal\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<Nº Item>>”\.*

Campo obrigatório

Formato: 999\.99

Tipo: Decimal

Tamanho: 3,2

MFS\-18480

RN27

__Regra p/ tag <tipoDocumentoPrestador> </tipoDocumentoPrestador>__

Identifica o tipo do documento do Prestador vinculado a nota fiscal\.

Preencher fixo com “__J__”\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN28

__Regra p/ tag <documentoPrestador> </documentoPrestador>__

Identifica o CNPJ ou o CPF do Prestador do serviço\.

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: 99999999999\.\.\.

Tipo: Numérico

Tamanho: 20

MFS\-18480

RN29

__Regra p/ tag <nomePrestador> </nomePrestador>__

Identifica o Nome ou Razão Social do Prestador do serviço\.

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN30

__Regra p/ tag <logradouroPrestador> </logradouroPrestador>__

Identifica o logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroPrestador é obrigatória, favor preencher endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN31

__Regra p/ tag <numeroPrestador> </numeroPrestador>__

Identifica o número do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroPrestador permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroPrestador é obrigatória, favor preencher o número do endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN32

__Regra p/ tag <complementoPrestador> </complementoPrestador>__

Identifica o complemento do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoPrestador é obrigatória, favor preencher complemento do endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN33

__Regra p/ tag <bairroPrestador> </bairroPrestador>__

Identifica o bairro do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroPrestador é obrigatória, favor preencher bairro do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN34

__Regra p/ tag <cidadePrestador> </cidadePrestador>__

Identifica a cidade do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadePrestador permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadePrestador é obrigatória, favor preencher cidade do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN35

__Regra p/ tag <estadoPrestador> </estadoPrestador>__

Identifica o estado do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoPrestador é obrigatória, favor preencher estado do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN36

__Regra p/ tag <cepPrestador> </cepPrestador>__

Identifica o CEP do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo CEP da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepPrestador é obrigatória, favor preencher CEP do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN37

__Regra p/ tag <telefonePrestador> </telefonePrestador>__

Identifica o telefone do Prestador do serviço\.

Preencher com a concatenação do conteúdo dos campos DDD\+TELEFONE da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG telefonePrestador é obrigatória, favor preencher telefone do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 15

MFS\-18480

RN38

__Regra p/ tag <emailPrestador> </emailPrestador>__

Identifica o e\-mail do Prestador do serviço\.

Preencher com o conteúdo do campo EMAIL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG emailPrestador é obrigatória, favor preencher e\-mail do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 50

MFS\-18480

RN39

__Regra p/ tag <tipoDocumentoTomador> </tipoDocumentoTomador >__

Identifica o tipo do documento do Tomador vinculado a nota fiscal\.

Preencher com:

“__F__”, se o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) possuir 11 posições\.

“__J__”, se o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) possuir 14 posições\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN40

__Regra p/ tag <documentoTomador> </documentoTomador >__

Identifica o CNPJ ou o CPF do Tomador do serviço\.

Preencher com o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: 99999999999\.\.\.

Tipo: Numérico

Tamanho: 20

MFS\-18480

RN41

__Regra p/ tag <nomeTomador> </nomeTomador >__

Identifica o Nome ou Razão Social do Tomador do serviço\.

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN42

__Regra p/ tag <logradouroTomador> </logradouroTomador >__

Identifica o logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroTomador é obrigatória, favor preencher endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN43

__Regra p/ tag <numeroTomador> </numeroTomador >__

Identifica o número do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroTomador permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroTomador é obrigatória, favor preencher o número do endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN44

__Regra p/ tag <complementoTomador> </complementoTomador >__

Identifica o complemento do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 30 primeiras posições;
- Se o campo estiver preenchido com mais de 30 posições emitir a seguinte mensagem de log:* “A TAG complementoTomador permite até 30 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoTomador é obrigatória, favor preencher complemento do endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN45

__Regra p/ tag <bairroTomador> </bairroTomador >__

Identifica o bairro do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroTomador é obrigatória, favor preencher bairro do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN46

__Regra p/ tag <cidadeTomador> </cidadeTomador >__

Identifica a cidade do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadeTomador permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadeTomador é obrigatória, favor preencher cidade do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN47

__Regra p/ tag <estadoTomador> </estadoTomador >__

Identifica o estado do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoTomador é obrigatória, favor preencher estado do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN48

__Regra p/ tag <cepTomador> </cepTomador>__

Identifica o estado do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepTomador é obrigatória, favor preencher CEP do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN49

__Regra p/ tag <telefoneTomador> </telefoneTomador>__

Identifica o telefone do Tomador do serviço\.

Preencher com a concatenação do conteúdo dos campos DDD\+TELEFONE da tabela X04\_PESSOA\_FIS\_JUR \(campo 23 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG telefoneTomador é obrigatória, favor preencher telefone do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 15

MFS\-18480

RN50

__Regra p/ tag <emailTomador> </emailTomador >__

Identifica o e\-mail do Prestador do serviço\.

Preencher com o conteúdo do campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR \(campo 40 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG emailTomador é obrigatória, favor preencher e\-mail do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 50

MFS\-18480

RN51

__Regra p/ tag <devidoForaMunic> </devidoForaMunic>__

Identifica se o serviço é devido fora do município\.

Preencher fixo com “__0__”, pois conforme verificado não existe tratamento e o validador só aceita esse valor\.

Campo não obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-18480

RN52

__Regra para tag </lancamento> __Tag relacionada à fechamento dos dados de lançamento do serviço com o texto fixo: __</lancamento>\.__

TAG obrigatória\.

MFS\-18480

RN53

__Regra para tag </retencao> __Tag relacionada à fechamento da formatação do arquivo e que deve receber as informações das notas fiscais declaradas com o texto fixo: __</retencao>\.__

TAG obrigatória\.

MFS\-18480

RN54

__Regra p/ Recuperação das notas fiscais de serviços tomados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Tomados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

O agrupamento deve ocorrer por <aliquotaIss>, <descricaoServico> e <devido>\.

*Observação: *Quando a nota fiscal __não tiver itens__ não deve ser considerada\.

MFS\-18480

RN54\.a

__Regra p/ Recuperação das notas fiscais de serviços tomados para o município de Campos do Jordão / Vinhedo/Rio Grande da Serra__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Tomados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

__\[MFS\-60904\] __

-  Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Campos do Jordão/SP = 9700\., Vinhedo e Rio Grande d Serra\.

       

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E  __o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

O agrupamento deve ocorrer por <aliquotaIss>, <descricaoServico> e <devido>\.

*Observação: *Quando a nota fiscal __não tiver itens__ não deve ser considerada\.

MFS\-60904

MFS\-97892

__MFS\-1065315__

RN55

__Estrutura do Arquivo:__

<?xml version="1\.0" encoding="ISO\-8859\-1"?>

<retencao>

	<lancamento>

		<servico>T</servico>

		<devido>DT</devido>

		<codigoNotaFiscal></codigoNotaFiscal>

		<numeroNotaFiscal>222222</numeroNotaFiscal>

		<dataNotaFiscal>05/06/2014</dataNotaFiscal>

		<logradouroServico>RUA PETROPOLIS</logradouroServico>

		<numeroServico>1150</numeroServico>

		<complementoServico>SALA 8</complementoServico>

		<bairroServico>JARDIM FERREIRA</bairroServico>

		<cidadeServico>UBATUBA</cidadeServico>

		<estadoServico>SP</estadoServico>

		<cepServico>11680\-000</cepServico>

		<descricaoServico>Serviço de desenvolvimento de portais Web\.</descricaoServico>

		<dataArquivo>15/01/2014</dataArquivo>

		<valorServico>800\.00</valorServico>

		<valorAbatimentoLegal>0\.00</valorAbatimentoLegal>

		<aliquotaIss>4\.00</aliquotaIss>

		<tipoDocumentoPrestador>F</tipoDocumentoPrestador>

		<documentoPrestador>339\.8884\.898\-24</documentoPrestador>

		<nomePrestador>HALLAN CHRISTIAN</nomePrestador>

		<logradouroPrestador>Rua das Valquirias</logradouroPrestador>

		<numeroPrestador>1234</numeroPrestador>

		<complementoPrestador>Sala 5</complementoPrestador>

		<bairroPrestador>Vale do Silicio</bairroPrestador>

		<cidadePrestador>Belo Horizonte</cidadePrestador>

		<estadoPrestador>MG</estadoPrestador>

		<cepPrestador>11963\-300</cepPrestador>

		<telefonePrestador>38324963</telefonePrestador>

		<emailPrestador>teste@gmail\.com</emailPrestador>

		<tipoDocumentoTomador>J</tipoDocumentoTomador>

		<documentoTomador>26\.782\.918/0001\-23</documentoTomador>

		<nomeTomador>Info Solution Informatica</nomeTomador>

		<logradouroTomador>Ruas das Aboboras</logradouroTomador>

		<numeroTomador>741</numeroTomador>

		<complementoTomador>Sala 5</complementoTomador>

		<bairroTomador>Novo Poder</bairroTomador>

		<cidadeTomador>Caraguatatuba</cidadeTomador>

		<estadoTomador>SP</estadoTomador>

		<cepTomador>11680\-900</cepTomador>

		<telefoneTomador>12997336252</telefoneTomador>

		<emailTomador>tomador@gmail\.com</emailTomador>

		<devidoForaMunic>0</devidoForaMunic>

	</lancamento>

</retencao>

MFS\-18480

RN56

__Regra p/ o cabeçalho do arquivo:__

Preencher com o tag <?xml version="1\.0" encoding="ISO\-8859\-1"?>

MFS\-18480

RN57

__Regra para tag <retencao> __Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas fiscais declaradas com o texto fixo: __<retencao>\.__

TAG obrigatória\.

MFS\-18480

RN58

__Regra para tag <lancamento> __Tag relacionada à abertura dos dados de lançamento do serviço com o texto fixo: __<lancamento>\.__

TAG obrigatória\.

MFS\-18480

RN59

__Regra p/ tag <servico> </servico>__

Identifica o tipo de serviço\.

Preencher com:

“__T__” para __serviços tomados__ de acordo com o critério de seleção\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN60

__Regra p/ tag <devido> </devido>__

Identifica para quem o serviço é devido\.

Preencher com:

“DP”, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “2” e o município do local de prestação do serviço \(campo 73 da SAFX07\) for igual ao município do módulo selecionado;

“DT”, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “1” e o município do local de prestação do serviço \(campo 73 da SAFX07\) for igual ao município do módulo selecionado\.

__Tratamento:__

- Se o município do local de prestação do serviço \(campo 73 da SAFX07\) for diferente do município do módulo selecionado, gerar o campo da seguinte forma:
- “__DP__”, se a tag <servico> for igual a __P__;
- “__DT__”, se a tag <servico> for igual a __T__\.
- Além disso, deverá ser emitida a seguinte mensagem de aviso no log: *“Talvez o ISS devido esteja incorreto porque o local de prestação de serviço deve ser igual o município do estabelecimento e para essa nota fiscal consta diferente, favor verificar\! Em caso de situação específica, ignorar a mensagem\. <<NF>>, <<Série>>, <<Data Fiscal>>, <<PFJ>>, <<Local de Prestação>>”*\.

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN61

__Regra p/ tag <codigoNotaFiscal> </codigoNotaFiscal>__

Para Serviços Tomados esse campo não será preenchido\.

Campo não obrigatório

Formato: XXXXXXXXXX

Tipo: Texto

Tamanho: 10

MFS\-18480

RN62

__Regra p/ tag <numeroNotaFiscal> </numeroNotaFiscal>__

Identifica o número da nota fiscal\.

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

__\[MFS62575\] __Inclusão do parâmetro para definir a forma de gerar o número do documento fiscal

Se o parâmetro “Considerar 6 Últimas Posições da Nota Fiscal” estiver desmarcado

     Considerar as 06 primeiras posições do campo

Senão

      Considerar as 06 últimas posições do campo

Se o campo ultrapassar 06 posições, emitir a mensagem de log: *“O campo número do documento <<Nº documento>> <<Série>> <<Data Fiscal>> ultrapassou o tamanho máximo permitido pelo layout \(06 posições\)\.”*\.

Campo obrigatório

Formato: 999999

Tipo: Numérico

Tamanho: 6

MFS\-18480

MFS\-62575

RN63

__Regra p/ tag <dataNotaFiscal> </dataNotaFiscal>__

Identifica a data da nota fiscal\.

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAX07\)\.

Campo obrigatório

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: 10

MFS\-18480

RN64

__Regra p/ tag <logradouroServico> </logradouroServico>__

Identifica o logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroServico é obrigatória, favor preencher endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN65

__Regra p/ tag <numeroServico> </numeroServico>__

Identifica o número do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroServico permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroServico é obrigatória, favor preencher o número do endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.  *

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN66

__Regra p/ tag <complementoServico> </complementoServico>__

Identifica o complemento do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 30 primeiras posições;
- Se o campo estiver preenchido com mais de 30 posições emitir a seguinte mensagem de log:* “A TAG complementoServico permite até 30 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoServico é obrigatória, favor preencher complemento do endereço de prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN67

__Regra p/ tag <bairroServico> </bairroServico>__

Identifica o bairro do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroServico é obrigatória, favor preencher bairro da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN68

__Regra p/ tag <cidadeServico> </cidadeServico>__

Identifica a cidade do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadeServico permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadeServico é obrigatória, favor preencher cidade da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN69

__Regra p/ tag <estadoServico> </estadoServico>__

Identifica o estado do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoServico é obrigatória, favor preencher estado da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN70

__Regra p/ tag <cepServico> </cepServico>__

Identifica o estado do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepServico é obrigatória, favor preencher CEP da prestação do serviço\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN71

__Regra p/ tag <descricaoServico> </descricaoServico>__

Identifica a descrição do serviço\.

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Não é necessário preencher o restante do campo com espaços em branco\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG descricaoServico é obrigatória, favor preencher o serviço da lei 116 no serviço que foi cadastrado no item da nota fiscal\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<Nº Item>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 1000

MFS\-18480

RN72

__Regra p/ tag <dataArquivo> </dataArquivo>__

Identifica a data em que foi enviado o arquivo\.

Preencher com o conteúdo do campo Data Envio Arquivo informado na tela de geração do arquivo magnético\.

Campo obrigatório

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: 10

MFS\-18480

RN73

__Regra p/ tag <valorServico> </valorServico>__

Identifica o valor do serviço\.

Preencher com o conteúdo do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV \(campo 14 da SAFX09\)\.

__Tratamento:__

- Se o campo ultrapassar o tamanho permitido pelo layout, deverá ser truncado considerando o valor da direita para a esquerda e exibir uma mensagem de log padrão\.

Campo obrigatório

Formato: 999999999\.99

Tipo: Decimal

Tamanho: 9,2

MFS\-18480

RN74

__Regra p/ tag <valorAbatimentoLegal> </valorAbatimentoLegal>__

Identifica o valor do abatimento Legal \(somente notas emitidas com a opção de Construção Civil\)\.

Preencher com o conteúdo do campo VLR\_MAT\_PROP da tabela DWT\_ITENS\_SERV \(campo 55 da SAFX09\)\.

__Tratamento:__

- Se o campo ultrapassar o tamanho permitido pelo layout, deverá ser truncado considerando o valor da direita para a esquerda e exibir uma mensagem de log padrão\.

Campo não obrigatório \(obrigatório apenas para construção civil\)

Formato: 999999999\.99

Tipo: Decimal

Tamanho: 9,2

MFS\-18480

RN75

__Regra p/ tag <aliquotaIss> </aliquotaIss>__

Identifica a alíquota do ISS\.

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout\.
- Se o campo não estiver preenchido, preencher a TAG com “0\.00” \(zeros\) e emitir a seguinte mensagem de log: *“A TAG aliquotaIss é obrigatória, favor preencher no item da nota fiscal\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<Nº Item>>”\.*

Campo obrigatório

Formato: 999\.99

Tipo: Decimal

Tamanho: 3,2

MFS\-18480

RN76

__Regra p/ tag <tipoDocumentoPrestador> </tipoDocumentoPrestador>__

Identifica o tipo do documento do Prestador vinculado a nota fiscal\.

Preencher com:

“__F__”, se o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAF04\) possuir 11 posições\.

“__J__”, se o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) possuir 14 posições\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN77

__Regra p/ tag <documentoPrestador> </documentoPrestador>__

Identifica o CNPJ ou o CPF do Prestador do serviço\.

Preencher com o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: 99999999999\.\.\.

Tipo: Numérico

Tamanho: 20

MFS\-18480

RN78

__Regra p/ tag <nomePrestador> </nomePrestador>__

Identifica o Nome ou Razão Social do Prestador do serviço\.

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN79

__Regra p/ tag <logradouroPrestador> </logradouroPrestador>__

Identifica o logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroPrestador é obrigatória, favor preencher endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN80

__Regra p/ tag <numeroPrestador> </numeroPrestador>__

Identifica o número do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroPrestador permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroPrestador é obrigatória, favor preencher o número do endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN81

__Regra p/ tag <complementoPrestador> </complementoPrestador>__

Identifica o complemento do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 30 primeiras posições;
- Se o campo estiver preenchido com mais de 30 posições emitir a seguinte mensagem de log:* “A TAG complementoPrestador permite até 30 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoPrestador é obrigatória, favor preencher complemento do endereço do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN82

__Regra p/ tag <bairroPrestador> </bairroPrestador>__

Identifica o bairro do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroPrestador é obrigatória, favor preencher bairro do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN83

__Regra p/ tag <cidadePrestador> </cidadePrestador>__

Identifica a cidade do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadePrestador permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadePrestador é obrigatória, favor preencher cidade do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN84

__Regra p/ tag <estadoPrestador> </estadoPrestador>__

Identifica o estado do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoPrestador é obrigatória, favor preencher estado do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN85

__Regra p/ tag <cepPrestador> </cepPrestador>__

Identifica o estado do logradouro do Prestador do serviço\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepPrestador é obrigatória, favor preencher CEP do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN86

__Regra p/ tag <telefonePrestador> </telefonePrestador>__

Identifica o telefone do Prestador do serviço\.

Preencher com a concatenação do conteúdo dos campos DDD\+TELEFONE da tabela X04\_PESSOA\_FIS\_JUR \(campo 23 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG telefonePrestador é obrigatória, favor preencher telefone do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 15

MFS\-18480

RN87

__Regra p/ tag <emailPrestador> </emailPrestador>__

Identifica o e\-mail do Prestador do serviço\.

Preencher com o conteúdo do campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR \(campo 40 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG emailPrestador é obrigatória, favor preencher e\-mail do prestador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 50

MFS\-18480

<a id="_Hlk516835647"></a>RN88

__Regra p/ tag <tipoDocumentoTomador> </tipoDocumentoTomador >__

Identifica o tipo do documento do Tomador vinculado a nota fiscal\.

Preencher fixo com “__J__”\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-18480

RN89

__Regra p/ tag <documentoTomador> </documentoTomador >__

Identifica o CNPJ do Tomador do serviço\.

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: 99999999999\.\.\.

Tipo: Numérico

Tamanho: 20

MFS\-18480

RN90

__Regra p/ tag <nomeTomador> </nomeTomador >__

Identifica a Razão Social do Tomador do serviço\.

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN91

__Regra p/ tag <logradouroTomador> </logradouroTomador >__

Identifica o logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG logradouroTomador é obrigatória, favor preencher endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 80

MFS\-18480

RN92

__Regra p/ tag <numeroTomador> </numeroTomador >__

Identifica o número do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições;
- Se o campo estiver preenchido com mais de 7 posições emitir a seguinte mensagem de log:* “A TAG numeroTomador permite até 7 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG numeroTomador é obrigatória, favor preencher o número do endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-18480

RN93

__Regra p/ tag <complementoTomador> </complementoTomador >__

Identifica o complemento do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG complementoTomador é obrigatória, favor preencher complemento do endereço do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

MFS\-18480

RN94

__Regra p/ tag <bairroTomador> </bairroTomador >__

Identifica o bairro do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG bairroTomador é obrigatória, favor preencher bairro do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN95

__Regra p/ tag <cidadeTomador> </cidadeTomador >__

Identifica a cidade do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo DESCRICAO da tabela MUNICIPIO de acordo com o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 40 primeiras posições;
- Se o campo estiver preenchido com mais de 40 posições emitir a seguinte mensagem de log:* “A TAG cidadeTomador permite até 40 posições, favor verificar\! <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”;*
- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cidadeTomador é obrigatória, favor preencher cidade do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 40

MFS\-18480

RN96

__Regra p/ tag <estadoTomador> </estadoTomador >__

Identifica o estado do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela MUNICIPIO para o COD\_MUNICIPIO da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG estadoTomador é obrigatória, favor preencher estado do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XX

Tipo: Texto

Tamanho: 2

MFS\-18480

RN97

__Regra p/ tag <cepTomador> </cepTomador>__

Identifica o estado do logradouro do Tomador do serviço\.

Preencher com o conteúdo do campo CEP da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG cepTomador é obrigatória, favor preencher CEP do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

__*Observação:*__

Apesar do campo considerar 10 posições será preenchida com as 8 posições da tabela do Mastersaf DW considerando o formato\. *Exemplo:* 05784\-020\.

Campo obrigatório

Formato: 99999\-999

Tipo: Numérico

Tamanho: 10

MFS\-18480

RN98

__Regra p/ tag <telefoneTomador> </telefoneTomador>__

Identifica o telefone do Tomador do serviço\.

Preencher com a concatenação do conteúdo dos campos DDD\+TELEFONE da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG telefoneTomador é obrigatória, favor preencher telefone do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 15

MFS\-18480

RN99

__Regra p/ tag <emailTomador> </emailTomador >__

Identifica o e\-mail do Tomador do serviço\.

Preencher com o conteúdo do campo EMAIL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: *“A TAG emailTomador é obrigatória, favor preencher e\-mail do tomador\. <<Nº NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”\.*

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 50

MFS\-18480

RN100

__Regra p/ tag <devidoForaMunic> </devidoForaMunic>__

Identifica se o serviço é devido fora do município\.

Preencher fixo com “__0__”, pois conforme verificado não existe tratamento e o validador só aceita esse valor\.

Campo não obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-18480

RN100\.a

__Regra p/ tag <devidoForaMunic> </devidoForaMunic> Específico p/ Município de Campos do Jordão / Vinhedo / Rio Grande da Serra\.__

Identifica se o serviço é devido fora do município\.

__\[ALTERAÇÃO\-__ __MFS71795\] __Tratamento quando o Serviço é Devido em outro Município\.

__Tratamento:__

Preencher com ‘__1__’:

__Se__ o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “2” ;

  __E__ se o município do local de prestação do serviço \(campo 73 da SAFX07\) for diferente do município do módulo selecionado;

Senão preencher com ‘0’

Formato: 9

Tipo: Numérico

Tamanho: 1

__MFS\-71795__

__MFS\-97892__

__MFS\-1065315__

RN100\.b

RN101

__Regra p/ tag <codigoatividade> Específico para o município de Vinhedo e Rio Grande da Serra\.__

Preencher com o campo 07 \- COD\_ATIVIDADE da tabela SAFX04__\.__

Campo não obrigatório

Formato: 9999999999

Tamanho: 30 posições

Tipo: Alfanumérico__ __

MFS\-751724

__MFS\-1065315__

RN102

__Regra para tag </lancamento> __Tag relacionada à fechamento dos dados de lançamento do serviço com o texto fixo: __</lancamento>\.__

TAG obrigatória\.

MFS\-18480

RN103

__Regra para tag </retencao> __Tag relacionada à fechamento da formatação do arquivo e que deve receber as informações das notas fiscais declaradas com o texto fixo: __</retencao>\.__

TAG obrigatória\.

MFS\-18480

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

MFS\-18480

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-18480

__IM03__

Código IBGE: __3802 – __Município/UF:__ ARTUR NOGUEIRA / SP__

A descrição funcional do módulo será: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Arthur Nogueira*”\.

MFS\-18480

__IM04__

Código IBGE: __55406 – __Município/UF:__ UBATUBA / SP__

A descrição funcional do módulo será: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Ubatuba*”\.

MFS\-19971

__IM05__

Código IBGE: __9700 – __Município/UF:__ CAMPOS DO JORDÃO / SP__

A descrição funcional do módulo será: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Campos do Jordão*”\.

MFS\-21211

__IM06__

Código IBGE: __56701 – __Município/UF:__ VINHEDO / SP__

A descrição funcional do módulo será: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Vinhedo*”\.

MFS\-97892

__IM06__

Código IBGE: __44103 – __Município/UF:__ RIO GRANDE DA SERRA / SP__

A descrição funcional do módulo será: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Rio Grande da Serra*”\.

__MFS\-1065315__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

