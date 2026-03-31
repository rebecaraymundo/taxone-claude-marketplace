# MTZ_E_RECEITA_Geracao_Meio_Magnetico

- **Fonte:** MTZ_E_RECEITA_Geracao_Meio_Magnetico.docx
- **Modificado:** 2024-07-29
- **Tamanho:** 77 KB

---

THOMSON REUTERS

e\-Receita

Ribeirão das Neves

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS5039

Julyana Perrucini

Criação do município Ribeirão das Neves atendido pela e\-Receita\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager__

O novo módulo Ribeirão das Neves deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Ribeirão das Neves: *“Consiste na entrega das informações sobre os serviços tomados no e\-Receita do município de Ribeirão das Neves”\.*

MFS5039

RN02

__Regra p/ abertura do novo módulo no Manager__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “54606” \(Ribeirão das Neves\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Ribeirão das Neves, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS5039

RN03

__Estrutura de menus do módulo DMS__

Deverão ser criados os seguintes itens de menu e no módulo e\-Receita:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS5039

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_ERECEITA\_DDMMAAAA\.TXT__, onde:

__ST\_ERECEITA__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_ERECEITA\_01012013\.TXT

Caso o parâmetro “Quebrar Arquivo por Data de Emissão” estiver marcado deverá ser realizada a seguinte verificação:

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivo de acordo com as competências geradas, e nesse caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas\. 

A nomenclatura desses arquivos deverá ser:

__ST\_ERECEITA\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__ST\_ERECEITA__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__MMAAAA:__ representa o mês da competência referente à nota fiscal gerada\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_ERECEITA\_01012013\_122012\.TXT

MFS5039

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Quebrar Arquivos por Data de Emissão:__ O campo deve ser um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Ribeirão das Neves, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS5039

RN06

__Regras referentes à formatação dos registros gerados no meio magnético__

- O arquivo deve ser gerado utilizando a codificação ISO\-8859\-1;
- Respeitar o início e fim de cada campo conforme leiaute, completando com espaços em branco até atingir o tamanho do campo;
- Devem ser enviadas somente notas fiscais válidas \(registro 2, campo situação da nota fiscal igual á N, I ou R\);
- Todo o conteúdo da nota fiscal deve estar em único arquivo;
- Ao calcular o valor do ISSQN \(base cálculo x alíquota\) utilizar a regra de arrendondamento universal para terceira casa decimal, onde menor que 5 arredonda para baixo e maior ou igual a 5 arredonda para cima\. *Exemplo:* R$10,30 X 2% = R$0,206 arredondando R$0,21\.

__Legenda tipos de campos:__

Numérico \- Campo deve ser preenchido somente com números;

Caracter \- Campo pode ser preenchido com qualquer caracter \(letras, números, etc\.\);

Data formatada \- Campo preenchido com dia \(2 dígitos\), mês \(2 dígitos\) e ano \(4 dígitos\)\. *Formato:* DDMMAAAA;

Moeda \- Campo preenchido com número com 2 casas decimais utilizando o ponto como separador de casas decimais\. *Exemplo: *1234\.56 \(sem separador para milhar\)\.

MFS5039

RN07

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS5039

RN08

__Regra do Registro Tipo 0 – Campo Identificação do registro \(0\)__

Preencher valor fixo “0”\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5039

RN09

__Regra do Registro Tipo 0 – Campo CNPJ da Prefeitura__

Preencher valor fixo “18314609000109”\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS5039

RN10

__Regra do Registro Tipo 0 – Campo Versão do Leiaute__

Preencher valor fixo “1\.1”\.

Tipo: Caracter

Tamanho: 3

Campo obrigatório\.

MFS5039

RN11

__Regra do Registro Tipo 1 – Campo Identificação do registro \(1\)__

Preencher valor fixo “1”\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5039

RN12

__Regra do Registro Tipo 1 – Campo Identificação do Serviço__

Preencher valor fixo “T”\.

Tipo: Caracter

Tamanho: 1

Campo obrigatório\.

MFS5039

RN13

__Regra do Registro Tipo 1 – Campo Tipo identificador do município__

Preencher valor fixo “1”\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5039

RN14

__Regra do Registro Tipo 1 – Campo CPF ou CNPJ do tomador de serviços__

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na geração do meio magnético\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS5039

RN15

__Regra do Registro Tipo 1 – Campo Nome do tomador de serviços__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na geração do meio magnético\.

__Tratamento:__

- Considerar as 50 primeiras posições\.

Tipo: Caracter

Tamanho: 50

Campo obrigatório\.

MFS5039

RN16

__Regra do Registro Tipo 1 – Campo Data inicial da competência declarada__

Preencher com o conteúdo do campo “Data Inicial” da tela de geração do meio magnético\.

Tipo: Data formatada

Tamanho: 8

Campo obrigatório\.

MFS5039

RN17

__Regra do Registro Tipo 1 – Campo Data final da competência declarada__

Preencher com o conteúdo do campo “Data Final” da tela de geração do meio magnético\.

Tipo: Data formatada

Tamanho: 8

Campo obrigatório\.

MFS5039

RN18

__Regra do Registro Tipo 2 – Campo Identificação do registro \(2\)__

Preencher valor fixo “2”\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5039

RN19

__Regra do Registro Tipo 2 – Campo CPF ou CNPJ do prestador de serviços__

Preencher com o conteúdo do campo CPF\_CGC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

Tipo: Numérico

Tamanho: 14

Campo obrigatório\.

MFS5039

RN20

__Regra do Registro Tipo 2 – Campo Nome do prestador de serviços__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 50 primeiras posições\.

Tipo: Caracter

Tamanho: 50

Campo obrigatório\.

MFS5039

RN21

__Regra do Registro Tipo 2 – Campo Série da nota fiscal__

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Caracter

Tamanho: 6

Campo obrigatório\.

MFS5039

RN22

__Regra do Registro Tipo 2 – Campo Número da nota fiscal__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 18

Campo obrigatório\.

MFS5039

RN23

__Regra do Registro Tipo 2 – Campo Data de emissão da nota fiscal__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data formatada

Tamanho: 8

Campo obrigatório\.

MFS5039

RN24

__Regra do Registro Tipo 2 – Campo Espécie nota fiscal__

Preencher valor fixo “N”\.

Tipo: Caracter

Tamanho: 1

Campo obrigatório\.

MFS5039

RN25

__Regra do Registro Tipo 2 – Campo Situação da nota fiscal__

Preencher com:

I \(Isenta\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

R \(Retida\), se o campo IND\_TP\_RET for igual a “1” e o campo COD\_MUNICIPIO for igual ao município do módulo selecionado da tabela DWT\_DOCTO\_FISCAL OU se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota OU se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido;

Se nenhuma das condições acima for atendida, preencher com N \(Tributada Normal\)\.

Tipo: Caracter

Tamanho: 1

Campo obrigatório\.

MFS5039

RN26

__Regra do Registro Tipo 2 – Campo Valor da nota fiscal__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 000000000000\.00

Tipo: Moeda

Tamanho: 15

Campo obrigatório\.

MFS5039

RN27

__Regra do Registro Tipo 2 – Campo Define onde esta estabelecido o prestador__

Preencher com:

D \- Dentro do Município, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual ao município do módulo selecionado;

F \- Fora do Município, quando o campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for diferente do município do módulo selecionado;

*Observação:* O município precisa ser devidamente cadastrado na Tabela de Município \(SAFX2097\)\.

__Tratamento:__

- Se o campo “Código do Município” estiver vazio, considerar o município da tabela ESTABELECIMENTO e emitir a mensagem de log: “O município do Prestador do serviço não foi localizado, será considerado Prestador dentro do município de Ribeirão das Neves”\.

Tipo: Caracter

Tamanho: 1

Campo obrigatório\.

MFS5039

RN28

__Regra do Registro Tipo 2 – Campo Codigo IBGE do munícipio de localização do prestador__

Preencher com o conteúdo do campo COD\_UF da tabela MUNICIPIO de acordo com UF da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal \+ o conteúdo do campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal\.

*Observação:* O município precisa ser devidamente cadastrado na Tabela de Município \(SAFX2097\)\.

__Tratamento:__

- O campo COD\_UF corresponde a 2 posições, enquanto o campo COD\_MUNICIPIO corresponde a 5 posições, se na tabela SAFX2097 o COD\_MUNICIPIO for menor que 5 posições, completar com zeros à esquerda\. *Exemplo:* Município Rio de Janeiro = 4557 deverá ficar 04557, a UF corresponde a 33, então o campo será preenchido com 3304557;
- Se o campo “Código do Município” estiver vazio, preencher branco e emitir a mensagem de log: “O município do Prestador do serviço não foi localizado, não será preenchido o Código IBGE do município de localização do Prestador”\.

Tipo: Numérico

Tamanho: 7

Campo obrigatório\.

MFS5039

RN29

__Regra do Registro Tipo 2 – Campo Optante Simples Nacional__

Preencher com:

S \- Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

N \- Não Optante, quando o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “N”\.

Tipo: Caracter

Tamanho: 1

Campo obrigatório\.

MFS5039

RN30

__Regra do Registro Tipo 3 – Campo Identificação do registro \(3\)__

Preencher valor fixo “3”\.

Tipo: Numérico

Tamanho: 1

Campo obrigatório\.

MFS5039

RN31

__Regra do Registro Tipo 3 – Campo Item lista de serviços__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

Tipo: Numérico

Tamanho: 7

Campo obrigatório\.

MFS5039

RN32

__Regra do Registro Tipo 3 – Campo Código IBGE do município da prestação do serviço__

Preencher com o conteúdo do campo COD\_UF da tabela MUNICIPIO relacionando\-o com UF da tabela SAFX2097 referente ao local de prestação de serviço preenchido na nota fiscal \+ o conteúdo do campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

*Observação:* O município precisa ser devidamente cadastrado na Tabela de Município \(SAFX2097\)\.

__Tratamento:__

- O campo COD\_UF corresponde a 2 posições, enquanto o campo COD\_MUNICIPIO corresponde a 5 posições, se na tabela SAFX2097 o COD\_MUNICIPIO for menor que 5 posições, completar com zeros à esquerda\. *Exemplo:* Município Rio de Janeiro = 4557 deverá ficar 04557, a UF corresponde a 33, então o campo será preenchido com 3304557;
- Se o campo “Código do Município do ISS” estiver vazio, preencher branco e emitir a mensagem de log: “O município do local de prestação do serviço não foi localizado, não será preenchido o Código IBGE do município da prestação do serviço”\.

Tipo: Numérico

Tamanho: 7

Campo obrigatório\.

MFS5039

RN33

__Regra do Registro Tipo 3 – Campo Base de Cálculo__

Preencher com o conteúdo do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 000000000000\.00

Tipo: Moeda

Tamanho: 15

Campo obrigatório\.

MFS5039

RN33

__Regra do Registro Tipo 3 – Campo Alíquota da prestação do serviço__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 7 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 0\.00

Tipo: Moeda

Tamanho: 4

Campo obrigatório\.

MFS5039

RN34

__Regra do Registro Tipo 3 – Campo Valor ISSQN__

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 000000000000\.00

Tipo: Moeda

Tamanho: 15

Campo obrigatório\.

MFS5039

RN35

__Regra do Registro Tipo 3 – Campo Valor ISSQN Retido__

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, quando pelo menos umas das seguintes opções forem verdadeiras:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com “0\.00”\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;

Formato: 000000000000\.00

Tipo: Moeda

Tamanho: 15

Campo obrigatório\.

MFS5039

RN36

__Regra do Registro Tipo 3 – Campo Descrição do Serviço__

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

Tipo: Caracter

Tamanho: 2000

Campo obrigatório\.

MFS5039

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

