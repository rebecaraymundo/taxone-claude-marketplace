# MTZ_REMESSA_PMSJP_Geracao_Meio_Magnetico

- **Fonte:** MTZ_REMESSA_PMSJP_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-10-07
- **Tamanho:** 120 KB

---

THOMSON REUTERS

Remessa de Escrituração – PMSJP

São José dos Pinhais

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS4263

Julyana Perrucini

Criação do município São José dos Pinhais atendido pela Remessa de Escrituração\.

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager__

O novo módulo São José dos Pinhais deve ficar localizado no grupo “Municipal”\.

Descrição do módulo São José dos Pinhais: *“Consiste na entrega das informações sobre os serviços tomados na Remessa de Escrituração do município de São José dos Pinhais”\.*

MFS4263

RN02

__Regra p/ abertura do novo módulo no Manager__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PR” e ao código de município do IBGE igual a “25506” \(São José dos Pinhais\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São José dos Pinhais, Paraná\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS4263

RN03

__Estrutura de menus do módulo DMS__

Deverão ser criados os seguintes itens de menu e no módulo REMESSA PMSJP:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS4263

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_REMESSAPMSJP\_DDMMAAAA\.TXT__, onde:

__ST\_REMESSAPMSJP__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_REMESSAPMSJP\_01012013\.TXT

Caso o parâmetro “Quebrar Arquivo por Data de Emissão” estiver marcado deverá ser realizada a seguinte verificação:

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivo de acordo com as competências geradas, e nesse caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas\. 

A nomenclatura desses arquivos deverá ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

<a id="_Hlk210581811"></a>Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__ST\_REMESSAPMSJP\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__ST\_REMESSAPMSJP__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__MMAAAA:__ representa o mês da competência referente à nota fiscal gerada\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_REMESSAPMSJP\_01012013\_122012\.TXT

MFS4263

MFS829438     

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Quebrar Arquivos por Data de Emissão:__ O campo deve ser um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de São José dos Pinhais, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS4263

RN06

__Regras referentes à formatação dos registros gerados no meio magnético__

- Os campos do tipo Texto devem ser alinhados a direita e ser completados por caracteres de espaço a esquerda até completar seu tamanho máximo;
- Os campos do tipo inteiro ou decimal devem ser alinhados a esquerda e ser completados com zero a direita até completar seu tamanho máximo;
- Os campos de valor, informar sem ponto milhar e decimal e sem o símbolo da moeda, informando sempre os centavos\.

MFS4263

__Serviço Tomado de Prestador Residente no País Com Nota Fiscal__

RN07

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF diferente de “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal diferente de “1”

MFS4263

RN08

__Campo Indicador de Registro__

Preencher valor fixo “T”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN09

__Campo Número da Nota Fiscal inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN10

__Campo Série da Nota Fiscal__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN11

__Campo Data da emissão da Nota Fiscal__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN12

__Campo Tipo da Nota Fiscal__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN13

__Campo Valor da Nota Fiscal__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN14

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN15

__Campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN16

__Campo Prestador estabelecido no Município__

Preencher com:

S\-Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for igual ao município do estabelecimento selecionado na tela de geração;

N\-Não Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for diferente do município do estabelecimento selecionado na tela de geração\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela SAFX04 não estiver preenchido, gravar branco e emitir a mensagem de log: “O campo Prestador estabelecido no Município do Registro T não foi preenchido, falta cadastrar o código do município no Cadastro de Pessoas Físicas/ Jurídicas\. <<Nº NF>>, <<Data de Emissão>>, <<Código FIS/JUR>>\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN17

__Campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN18

__Campo Inscrição municipal do prestador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo estiver preenchido com ISENT%, gravar zeros\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN19

__Campo Dígito da inscrição Municipal__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar das posições 11 a 12;
- Se não houver posições 11 a 12, gravar branco;
- Se a posição 11 estiver preenchida e a 12 não, completar com brancos a esquerda\.

 

Tipo: Numérico

Tamanho: 2

MFS4263

RN20

__Campo CNPJ ou CPF do prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS4263

RN21

__Campo Prestador isento de inscrição estadual__

Preencher com S\-Isento quando o campo INSC\_ESTADUAL da tabela SAFX04 estiver preenchido com ISENT%, caso contrário preencher com N\-Não Isento\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN22

__Campo Inscrição estadual do prestador__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__*Observação:*__

- Será gerado esse campo apenas quando o campo “Prestador isento de inscrição estadual” for igual a N\.

Tipo: Numérico

Tamanho: 15

Campo obrigatório\.

MFS4263

RN23

__Campo CEP referente ao logradouro do prestador__

Preencher com o conteúdo do campo CEP da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 8

Campo obrigatório\.

MFS4263

RN24

__Campo Tipo de logradouro do prestador__

Preencher com o conteúdo do campo TP\_LOGRADOURO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 5 primeiras posições\.

Tipo: Texto

Tamanho: 5

Campo obrigatório\.

MFS4263

RN25

__Campo Título do logradouro do prestador__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 5

MFS4263

RN26

__Campo Logradouro do prestador__

Preencher com o conteúdo do campo ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN27

__Campo Complemento do logradouro do prestador__

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se ultrapassar 40 posições, truncar à direita\.

Tipo: Texto

Tamanho: 40

MFS4263

RN28

__Campo Número do logradouro do prestador__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN29

__Campo Bairro referente ao logradouro do prestador__

Preencher com o conteúdo do campo BAIRRO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN30

__Campo Estado\(UF\) referente ao logradouro do prestador__

Preencher com o conteúdo do campo UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN31

__Campo Cidade referente ao logradouro do prestador__

Preencher com o conteúdo do campo CIDADE da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN32

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN33

__Campo Prestador Optante pelo Simples Nacional__

Preencher com:

S\-Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N\-Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Texto

Tamanho: 1

MFS4263

RN34

__Campo Aliquota do Simples Nacional__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 00\.00

Tipo: Numérico

Tamanho: 5

MFS4263

__Serviço Tomado de Prestador Residente no País Sem Nota Fiscal__

RN35

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 8 ou 9 ou Tipo de Documento = RPA
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF diferente de “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal diferente de “1”

MFS4263

RN36

__Campo Indicador de Registro__

Preencher valor fixo “P”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN37

__Campo Número do Documento__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN38

__Campo Data da emissão do documento__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN39

__Campo Tipo do Documento__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN40

__Campo Valor do Documento__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN41

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN42

__Campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN43

__Campo Prestador estabelecido no Município__

Preencher com:

S\-Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for igual ao município do estabelecimento selecionado na tela de geração;

N\-Não Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for diferente do município do estabelecimento selecionado na tela de geração\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela SAFX04 não estiver preenchido, gravar branco e emitir a mensagem de log: “O campo Prestador estabelecido no Município do Registro T não foi preenchido, falta cadastrar o código do município no Cadastro de Pessoas Físicas/ Jurídicas\. <<Nº NF>>, <<Data de Emissão>>, <<Código FIS/JUR>>\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN44

__Campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN45

__Campo Inscrição municipal do prestador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo estiver preenchido com ISENT%, gravar zeros\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN46

__Campo Dígito da inscrição Municipal__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar das posições 11 a 12;
- Se não houver posições 11 a 12, gravar branco;
- Se a posição 11 estiver preenchida e a 12 não, completar com brancos a esquerda\.

 

Tipo: Numérico

Tamanho: 2

MFS4263

RN47

__Campo CNPJ ou CPF do prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS4263

RN48

__Campo Prestador isento de inscrição estadual__

Preencher com S\-Isento quando o campo INSC\_ESTADUAL da tabela SAFX04 estiver preenchido com ISENT%, caso contrário preencher com N\-Não Isento\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN49

__Campo Inscrição estadual do prestador__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__*Observação:*__

- Será gerado esse campo apenas quando o campo “Prestador isento de inscrição estadual” for igual a N\.

Tipo: Numérico

Tamanho: 15

Campo obrigatório\.

MFS4263

RN50

__Campo CEP referente ao logradouro do prestador__

Preencher com o conteúdo do campo CEP da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 8

Campo obrigatório\.

MFS4263

RN51

__Campo Tipo de logradouro do prestador__

Preencher com o conteúdo do campo TP\_LOGRADOURO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 5 primeiras posições\.

Tipo: Texto

Tamanho: 5

Campo obrigatório\.

MFS4263

RN52

__Campo Título do logradouro do prestador__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 5

MFS4263

RN53

__Campo Logradouro do prestador__

Preencher com o conteúdo do campo ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN54

__Campo Complemento do logradouro do prestador__

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se ultrapassar 40 posições, truncar à direita\.

Tipo: Texto

Tamanho: 40

MFS4263

RN55

__Campo Número do logradouro do prestador__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN56

__Campo Bairro referente ao logradouro do prestador__

Preencher com o conteúdo do campo BAIRRO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN57

__Campo Estado\(UF\) referente ao logradouro do prestador__

Preencher com o conteúdo do campo UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN58

__Campo Cidade referente ao logradouro do prestador__

Preencher com o conteúdo do campo CIDADE da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN59

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN60

__Campo Prestador Optante pelo Simples Nacional__

Preencher com:

S\-Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N\-Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Texto

Tamanho: 1

MFS4263

RN61

__Campo Aliquota do Simples Nacional__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 00\.00

Tipo: Numérico

Tamanho: 5

MFS4263

__Serviço Tomado de Prestador Residente Fora do País Sem Nota Fiscal__

RN62

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 8 ou 9 ou Tipo de Documento = RPA
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF igual “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal diferente de “1”

MFS4263

RN63

__Campo Indicador de Registro__

Preencher valor fixo “P”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN64

__Campo Número do Documento__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN65

__Campo Data da emissão do documento__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN66

__Campo Tipo do Documento__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN67

__Campo Valor do Documento__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN68

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN69

__Campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN70

__Campo Sigla do país__

Preencher com o conteúdo do campo SIGLA\_PAIS da tabela PAIS referente ao país da Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN71

__Campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN72

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN73

__Campo Informações gerais sobre a empresa__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

__Serviço Tomado de Prestador Residente Fora do País Com Nota Fiscal__

RN74

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF igual “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal diferente de “1”

MFS4263

RN75

__Campo Indicador de Registro__

Preencher valor fixo “F”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN76

__Campo Número da Nota Fiscal inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN77

__Campo Série da Nota Fiscal__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN78

__Campo Data da emissão da Nota Fiscal__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN79

__Campo Tipo da Nota Fiscal__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN80

__Campo Valor da Nota Fiscal__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN81

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN82

__Campo Sigla do país__

Preencher com o conteúdo do campo SIGLA\_PAIS da tabela PAIS referente ao país da Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN83

__Campo Nome da Empresa__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN84

__Campo Informações gerais sobre a empresa__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN85

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

__Serviço Tomado de Prestador Residente no País Com Nota Fiscal – Sem Obras__

RN86

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Canal de Distribuição/ Código Obra não preenchido
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF diferente de “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal igual a “1”

MFS4263

RN87

__Campo Indicador de Registro__

Preencher valor fixo “I”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN88

__Campo Número da Nota Fiscal inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN89

__Campo Série da Nota Fiscal__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN90

__Campo Data da emissão da Nota Fiscal__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN91

__Campo Tipo da Nota Fiscal__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN92

__Campo Valor da Nota Fiscal__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN93

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN94

__Campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN95

__Campo Prestador estabelecido no Município__

Preencher com:

S\-Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for igual ao município do estabelecimento selecionado na tela de geração;

N\-Não Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for diferente do município do estabelecimento selecionado na tela de geração\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela SAFX04 não estiver preenchido, gravar branco e emitir a mensagem de log: “O campo Prestador estabelecido no Município do Registro T não foi preenchido, falta cadastrar o código do município no Cadastro de Pessoas Físicas/ Jurídicas\. <<Nº NF>>, <<Data de Emissão>>, <<Código FIS/JUR>>\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN96

__Campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN97

__Campo Inscrição municipal do prestador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo estiver preenchido com ISENT%, gravar zeros\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN98

__Campo Dígito da inscrição Municipal__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar das posições 11 a 12;
- Se não houver posições 11 a 12, gravar branco;
- Se a posição 11 estiver preenchida e a 12 não, completar com brancos a esquerda\.

 

Tipo: Numérico

Tamanho: 2

MFS4263

RN99

__Campo CNPJ ou CPF do prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS4263

RN100

__Campo Prestador isento de inscrição estadual__

Preencher com S\-Isento quando o campo INSC\_ESTADUAL da tabela SAFX04 estiver preenchido com ISENT%, caso contrário preencher com N\-Não Isento\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN101

__Campo Inscrição estadual do prestador__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__*Observação:*__

- Será gerado esse campo apenas quando o campo “Prestador isento de inscrição estadual” for igual a N\.

Tipo: Numérico

Tamanho: 15

Campo obrigatório\.

MFS4263

RN102

__Campo CEP referente ao logradouro do prestador__

Preencher com o conteúdo do campo CEP da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 8

Campo obrigatório\.

MFS4263

RN103

__Campo Tipo de logradouro do prestador__

Preencher com o conteúdo do campo TP\_LOGRADOURO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 5 primeiras posições\.

Tipo: Texto

Tamanho: 5

Campo obrigatório\.

MFS4263

RN104

__Campo Título do logradouro do prestador__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 5

MFS4263

RN105

__Campo Logradouro do prestador__

Preencher com o conteúdo do campo ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN106

__Campo Complemento do logradouro do prestador__

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se ultrapassar 40 posições, truncar à direita\.

Tipo: Texto

Tamanho: 40

MFS4263

RN107

__Campo Número do logradouro do prestador__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN108

__Campo Bairro referente ao logradouro do prestador__

Preencher com o conteúdo do campo BAIRRO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN109

__Campo Estado\(UF\) referente ao logradouro do prestador__

Preencher com o conteúdo do campo UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN110

__Campo Cidade referente ao logradouro do prestador__

Preencher com o conteúdo do campo CIDADE da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN111

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN112

__Campo Base de Cálculo__

Preencher com o conteúdo do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN113

__Campo Prestador Optante pelo Simples Nacional__

Preencher com:

S\-Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N\-Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Texto

Tamanho: 1

MFS4263

__Serviço Tomado de Prestador Residente no País Com Nota Fiscal – Com Obras__

RN114

__Regra p/ Recuperar Registro__

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Canal de Distribuição/ Código Obra preenchido
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Pessoa Física/ Jurídica cadastrada na nota fiscal que possua o campo UF diferente de “EX”
- Indicador de Tipo de Serviço do serviço cadastrado no item da nota fiscal igual a “1”

MFS4263

RN115

__Campo Indicador de Registro__

Preencher valor fixo “H”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN116

__Campo Número da Nota Fiscal inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.

Tipo: numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN117

__Campo Série da Nota Fiscal__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN118

__Campo Data da emissão da Nota Fiscal__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS4263

RN119

__Campo Tipo da Nota Fiscal__

Preencher com:

2 \(Cancelada\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL for igual a “S”;

4 \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Retida\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município do módulo selecionado;

6 \(Pagto pelo Prestador\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “455” na tela Classificação de Serviços de Parâmetros para Município;

7 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

8 \(S\. Judicial\), se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “09” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “427” na tela Classificação de Serviços de Parâmetros para Município;

Se nenhuma das condições acima for atendida, preencher com 1 \(Tributada\)\.

*Observação:* A opção 3 \(Anulada\) não será tratada nessa Issue\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN120

__Campo Valor da Nota Fiscal__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN121

__Campo Atividade ou serviço prestado__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN122

__Campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS4263

RN123

__Campo Prestador estabelecido no Município__

Preencher com:

S\-Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for igual ao município do estabelecimento selecionado na tela de geração;

N\-Não Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for diferente do município do estabelecimento selecionado na tela de geração\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela SAFX04 não estiver preenchido, gravar branco e emitir a mensagem de log: “O campo Prestador estabelecido no Município do Registro T não foi preenchido, falta cadastrar o código do município no Cadastro de Pessoas Físicas/ Jurídicas\. <<Nº NF>>, <<Data de Emissão>>, <<Código FIS/JUR>>\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN124

__Campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS4263

RN125

__Campo Inscrição municipal do prestador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo estiver preenchido com ISENT%, gravar zeros\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN126

__Campo Dígito da inscrição Municipal__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar das posições 11 a 12;
- Se não houver posições 11 a 12, gravar branco;
- Se a posição 11 estiver preenchida e a 12 não, completar com brancos a esquerda\.

 

Tipo: Numérico

Tamanho: 2

MFS4263

RN127

__Campo CNPJ ou CPF do prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS4263

RN128

__Campo Prestador isento de inscrição estadual__

Preencher com S\-Isento quando o campo INSC\_ESTADUAL da tabela SAFX04 estiver preenchido com ISENT%, caso contrário preencher com N\-Não Isento\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN129

__Campo Inscrição estadual do prestador__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__*Observação:*__

- Será gerado esse campo apenas quando o campo “Prestador isento de inscrição estadual” for igual a N\.

Tipo: Numérico

Tamanho: 15

Campo obrigatório\.

MFS4263

RN130

__Campo CEP referente ao logradouro do prestador__

Preencher com o conteúdo do campo CEP da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 8

Campo obrigatório\.

MFS4263

RN131

__Campo Tipo de logradouro do prestador__

Preencher com o conteúdo do campo TP\_LOGRADOURO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 5 primeiras posições\.

Tipo: Texto

Tamanho: 5

Campo obrigatório\.

MFS4263

RN132

__Campo Título do logradouro do prestador__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 5

MFS4263

RN133

__Campo Logradouro do prestador__

Preencher com o conteúdo do campo ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN134

__Campo Complemento do logradouro do prestador__

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se ultrapassar 40 posições, truncar à direita\.

Tipo: Texto

Tamanho: 40

MFS4263

RN135

__Campo Número do logradouro do prestador__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS4263

RN136

__Campo Bairro referente ao logradouro do prestador__

Preencher com o conteúdo do campo BAIRRO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN137

__Campo Estado\(UF\) referente ao logradouro do prestador__

Preencher com o conteúdo do campo UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS4263

RN138

__Campo Cidade referente ao logradouro do prestador__

Preencher com o conteúdo do campo CIDADE da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS4263

RN139

__Campo Local de prestação do serviço__

Preencher com:

D\-Dentro do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual ao município do estabelecimento selecionado na tela de geração;

F\-Fora do Município, quando o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for diferente do município do estabelecimento selecionado na tela de geração;

__Tratamento:__

- Se o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “Município com local de prestação de serviço não localizado na capa do documento fiscal\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS4263

RN140

__Campo Base de Cálculo__

Preencher com o conteúdo do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS4263

RN141

__Campo Código da Obra__

Preencher com o conteúdo do campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Apesar de numérico esse campo deve ser alinhado à esquerda e preenchido com espaços à esquerda\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS4263

RN142

__Campo Prestador Optante pelo Simples Nacional__

Preencher com:

S\-Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N\-Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Texto

Tamanho: 1

MFS4263

RN143

__Campo Aliquota do Simples Nacional__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 00\.00

Tipo: Texto

Tamanho: 5

MFS4263

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

