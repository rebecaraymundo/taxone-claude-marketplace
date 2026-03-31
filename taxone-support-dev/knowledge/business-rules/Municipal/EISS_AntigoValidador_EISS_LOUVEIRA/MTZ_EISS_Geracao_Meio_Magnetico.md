# MTZ_EISS_Geracao_Meio_Magnetico

- **Fonte:** MTZ_EISS_Geracao_Meio_Magnetico.docx
- **Modificado:** 2024-02-20
- **Tamanho:** 75 KB

---

THOMSON REUTERS

__e\-ISS__

__Louveira__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS5143

Julyana Perrucini

Criação de validador para município\.

CH7445\-A\_2016

Julyana Perrucini

Este documento tem como objetivo alterar a formatação do campo Serviço\.

MFS\-73049

Alessandra Cristina Navatta

Alterar a descrição do validador EISS Louveira para EISS, pois agora o layout servirá para outros municípios\. \(AlterarTFIX105 e tela de validadores\)

Incluir a geração de meio magnético para o município de Descalvado/SP para o validador EISS\. \(RN35 e RN36\)

Alteração da regra de recuperação dos serviços tomados, para desconsiderar as notas fiscais emitidas no município de Descalvado \(RN07\.a\)

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager__

O novo módulo Louveira deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Louveira: *“Consiste na entrega das informações sobre os serviços tomados do município de Louveira”\.*

MFS5143

RN02

__Regra p/ abertura do novo módulo no Manager__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “27306” \(Louveira\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Louveira, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS5143

RN03

__Estrutura de menus do módulo DMS__

Deverão ser criados os seguintes itens de menu e no módulo EISS LOUVEIRA:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS5143

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EISS\_LOUVEIRA\_DDMMAAAA\.TXT__, onde:

__ST\_EISS\_LOUVEIRA__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_EISS\_LOUVEIRA\_01012013\.TXT

MFS5143

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Louveira, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS5143

RN06

__Regras referentes à formatação dos registros gerados no meio magnético__

Os tipos de dados utilizados nesta especificação deverão seguir os seguintes critérios:

- __Texto \-__ Podem ser qualquer caractere, inclusive números e símbolos;
- __Número \-__ Somente os caracteres entre 0 e 9 serão aceitos\. Nos casos onde valores decimais precisarem ser informados, estes não poderão conter separador de milhar ou decimal\. Nestes casos, as casas decimais deverão ser informadas\. Ex: R$ 1\.234,56 deverá ser informado como: 123456 \(Exceção: Campo 27 \- Alíquota do Simples Nacional\);
- __Data \-__ Deve ser informada no formato DD/MM/YYYY, ex: 25/08/2015\.

MFS5143

RN07

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

Desconsiderar todas as notas fiscais de serviço com as seguintes características:

- Se a pessoa física/jurídica vinculada na nota fiscal for do exterior \(campo UF da tabela SAFX04 = “EX”\)
- Se a nota fiscal não possuir itens

MFS5143

RN07\.a

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\), para o município de Descalvado__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

Desconsiderar todas as notas fiscais de serviço com as seguintes características:

- Se a pessoa física/jurídica vinculada na nota fiscal for do exterior \(campo UF da tabela SAFX04 = “EX”\)
- Se a nota fiscal não possuir itens
- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

MFS\-73049

RN08

__Regra p/ campo Indicador de Registro__

Não utilizado no momento, preencher com branco\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS5143

RN09

__Regra p/ campo Número__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 10 primeiras posições\.
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)\.”\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS5143

RN10

__Regra p/ campo Série__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS5143

RN11

__Regra p/ campo Emissão__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL no formato DD/MM/AAAA\.

Tipo: Data

Tamanho: 10

Campo obrigatório\.

MFS5143

RN12

__Regra p/ campo Tipo__

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

MFS5143

RN13

__Regra p/ campo Valor__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

Tipo: Numérico

Tamanho: 12

Campo obrigatório\.

MFS5143

RN14

__Regra p/ campo Serviço__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__\[ALTERADA \- CH7445\-A\_2016\]__

__Tratamento:__

- Deve ser considerados brancos à direita para completar o tamanho do campo;
- Caso o serviço contido na nota não tenha Código Serviço Lei 116/03 relacionado a ele, deve apresentar mensagem no log: “Código Serviço Lei 116/03 obrigatório\. Ver cadastro de Serviço em Mastersaf DW >> Manutenção >> Códigos >> Serviços ”\.

Formato: 99\.99

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS5143

CH7445\-A\_2016

RN15

__Regra p/ campo Prestador__

Preencher com:

1\-Física, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 11 posições\.

2\-Jurídica, quando o campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal esteja preenchido com 14 posições\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5143

RN16

__Regra p/ campo Prestador estabelecido no Município__

Preencher com:

S\-Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for igual ao município do estabelecimento selecionado na tela de geração;

N\-Não Estabelecido, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal for diferente do município do estabelecimento selecionado na tela de geração\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela SAFX04 não estiver preenchido, gravar branco e emitir a mensagem de log: “O campo Prestador estabelecido no Município não foi preenchido, falta cadastrar o código do município no Cadastro de Pessoas Físicas/ Jurídicas\. <<Nº NF>>, <<Data de Emissão>>, <<Código FIS/JUR>>\.”\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS5143

RN17

__Regra p/ campo Razão Social do prestador__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 100

Campo obrigatório\.

MFS5143

RN18

__Regra p/ campo Inscrição municipal do prestador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo estiver preenchido com ISENT%, gravar zeros\.

Tipo: Numérico

Tamanho: 10

Campo obrigatório\.

MFS5143

RN19

__Regra p/ campo Dígito da inscrição Municipal__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar das posições 09 a 10;
- Se o campo IE não estiver preenchido das posições 09 a 10, completar com zeros a esquerda\.

 

Tipo: Numérico

Tamanho: 2

MFS5143

RN20

__Regra p/ campo CNPJ ou CPF do prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS5143

RN21

__Regra p/ campo Prestador isento de inscrição estadual__

Preencher com S\-Isento quando o campo INSC\_ESTADUAL da tabela SAFX04 estiver preenchido com ISENT%, caso contrário preencher com N\-Não Isento\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS5143

RN22

__Regra p/ campo Inscrição estadual do prestador__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__*Observação:*__

- Será gerado esse campo apenas quando o campo “Prestador isento de inscrição estadual” for igual a N\.

Tipo: Numérico

Tamanho: 15

Campo obrigatório\.

MFS5143

RN23

__Regra p/ campo CEP referente ao logradouro do prestador__

Preencher com o conteúdo do campo CEP da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 8

Campo obrigatório\.

MFS5143

RN24

__Regra p/ campo Tipo de logradouro do prestador__

Preencher com o conteúdo do campo TP\_LOGRADOURO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 5 primeiras posições\.

Tipo: Texto

Tamanho: 5

Campo obrigatório\.

MFS5143

RN25

__Regra p/ campo Título do logradouro do prestador__

Preencher com espaços em branco\.

Tipo: Texto

Tamanho: 5

MFS5143

RN26

__Regra p/ campo Logradouro do prestador__

Preencher com o conteúdo do campo ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS5143

RN27

__Regra p/ campo Complemento do logradouro do prestador__

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Se ultrapassar 40 posições, truncar à direita\.

Tipo: Texto

Tamanho: 40

MFS5143

RN28

__Regra p/ campo Número do logradouro do prestador__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 10

Campo obrigatório\.

MFS5143

RN29

__Regra p/ campo referente ao logradouro do prestador__

Preencher com o conteúdo do campo BAIRRO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS5143

RN30

__Regra p/ campo Estado\(UF\) referente ao logradouro do prestador__

Preencher com o conteúdo do campo UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 2

Campo obrigatório\.

MFS5143

RN31

__Regra p/ campo Cidade referente ao logradouro do prestador__

Preencher com o conteúdo do campo CIDADE da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Texto

Tamanho: 50

Campo obrigatório\.

MFS5143

RN32

__Regra p/ campo Local de prestação do serviço__

Não utilizado no momento, preencher com branco\.

Tipo: Texto

Tamanho: 1

Campo obrigatório\.

MFS5143

RN33

__Regra p/ campo Prestador Optante pelo Simples Nacional__

Preencher com:

S\-Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N\-Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Texto

Tamanho: 1

MFS5143

RN34

__Campo Aliquota do Simples Nacional__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 00\.00

Tipo: Numérico

Tamanho: 5

MFS4263

RN35

__Regra p/ inclusão do novo módulo no Manager__

O novo módulo descalvado deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Descalvado: *“Consiste na entrega das informações sobre os serviços tomados do município de Descalvado”\.*

MFS\-73049

RN36

__Regra p/ abertura do novo módulo no Manager__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “13702” \(Descalvado\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Descalvado, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS\-73049

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

