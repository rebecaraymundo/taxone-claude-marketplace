# MTZ-EISS_JABOTICABAL-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-EISS_JABOTICABAL-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 103 KB

---

THOMSON REUTERS

Municipal

EISS Jaboticabal \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4405

DW – Municipal \- Geração do Meio Magnético EISS Jaboticabal

Deverá ser atualizado o módulo de Jaboticabal para que permita a geração do meio magnético EISS Jaboticabal, onde serão informados os documentos fiscais de serviço prestados \(emitidos\) e tomados \(recebidos\)\.

MFS\_2071

DW \- MUNICIPAL – EISS Jaboticabal – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

MFS\-829438     

DW \- MUNICIPAL – EISS Jaboticabal – Ajuste na Nomenclatura do Documento

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

 

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Jaboticabal” deve ficar localizado no grupo “Municipal”\.

Descrição do Módulo: <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>“Consiste na entrega das informalções sobre os serviços tomados ou prestados do município de Jaboticabal\.”

OS4405

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “24303” \(Jaboticabal\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Jaboticabal, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS4405

RN03

__Estrutura de menus do módulo Jaboticabal:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Jaboticabal:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

OS4405

RN04

__Regra de criação do nome do arquivo__

Deverá respeitar o seguinte formato: 

__Serviços Prestados:__

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

<a id="OLE_LINK4"></a>__SP\_JABOTICABAL\_DDMMAAAA\.txt__, onde:

__               __<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a>__SP__: representa a obrigação que está sendo gerada, apenas registros de serviços prestados\.__       __

__               JABOTICABAL__: representa o município que está sendo gerado\.

               __DDMMAAAA__: representa a data inicial da geração\.           

               __\.txt__: extensão do arquivo\.

Ex: SP\_JABOTICABAL\_25012014\.txt

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_JABOTICABAL\_DDMMAAAA\.txt__, onde:

               __ST__: representa a obrigação que está sendo gerada, apenas registros de serviços tomados\.__       __

__               JABOTICABAL__: representa o município que está sendo gerado\.

               __DDMMAAAA__: representa a data inicial da geração\.           

               __\.txt__: extensão do arquivo\.

Ex: ST\_JABOTICABAL\_01012010\.txt

OS4405

MFS829438

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

Gerar Serviços Tomados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

Obs: Devem ser gerados arquivos separados para serviços prestados e serviços tomados\.

OS4405__ __MFS\_2071

RN06

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Regras referentes à formatação dos registros gerados no meio magnético:__

- \.Os campos do tipo numérico devem ser alinhados à direita, completados com zeros à esquerda até atingir o tamanho exato do campo, sem vírgula e sem ponto e os não utilizados deverão ser preenchidos com zeros;
- Para o campo de valor de alíquota, deverão considerar duas casas decimais\. 
- Os campos do tipo Alfanuméricos devem ser alinhados à esquerda com brancos a direita e os não utilizados deverão conter brancos;
- Informe as datas no formato AAAAMMDD \(sem barras\);

OS4405

__Os arquivos deverão ser gerados no seguinte formato: __

__ \- Colunado __

Respeitando os tamanhos dos campos\. Cada linha deve conter a informação de uma nota\. Exemplo: 

0

0

0

0

0

0

0

0

0

0

2

2

0

1

2

1

5

2

1

7

__\.__

__\.__

    

                                                                

                                                          __\(1\)                                                                      \(2\)   \(3\)                           \(4\)__

__\(1\)__ IM/CNPJ/CPF\(14 posições\) 

__\(2\)__ Tipo identificador 

__\(3\)__ Tipo da nota 

__\(4\)__ Número da nota \(14 posições\) 

Obs\.: Poderá haver mais de uma linha para a mesma nota, quando conter produtos ou alíquotas diferentes\.

\- Nesse tipo de arquivo, é __obrigatório __que o campo tenha o tamanho máximo permitido\. Os campos numéricos terão que ser completados com zeros a esquerda e os alfanuméricos terão que ser completados com brancos no final, até atingir o tamanho máximo do campo\. Exemplo: 

Supondo que o status da nota não seja “Cancelada”\. Sendo assim, não temos data de cancelamento\. Mas o campo deverá ser preenchido com 8 zeros \(00000000\)\.

RN07

__Regra geral p/ Registro de Serviços Prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas 

com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);     
- Classificação do Documento fiscal = 2 ou 3;    
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.
- Quando a nota não tiver itens não deve ser recuperada\.

OS4405

RN08

__Regras para o campo Identificação do Prestador :__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO; 

Senão, 

Preencher com o campo CGC da tabela ESTABELECIMENTO quando o campo  INSC\_MUNICIPAL da tabela ESTABELECIMENTO estiver vazio;

Tipo: Numérico 

Tamanho: 14 caracteres

OS4405

RN09

__Regras para o campo Tipo Identificação: __

__Preencher com:__

__“2”__ – IM, quando o campo “Identificação do Prestador” \(RN08\)  estiver preenchido com uma Inscrição Municipal, ou seja, quando o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO estiver preenchido\. 

__“0”__ – CNPJ, quando o campo “Identificação do Prestador”  estiver preenchido com um CNPJ, ou seja, quando o valor inserido no campo CGC da tabela ESTABELECIMENTO possuir 14 posições\.

__“1”__ –  Não será tratado\.

 

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN10

__Regras para o campo Tipo: __

Preencher com:

__“1”__ – __Nota Emitida __

Tipo: Alfanumérico       

Tamanho: 01 caracteres

OS4405

RN11

__Regras para o campo Número da Nota: __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN12

__Regras para o campo Série: __

Preencher com o campo Série da tela Parâmetros por Município / Parâmetros / Modelo Msaf x Série, referente ao modelo cadastrado na nota fiscal\.

Obs\.: Caso a série não for parametrizada em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: "Série não parametrizada em Parâmetros por Município\. Favor verificar\!”

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN13

__Regras para o campo Data de Emissão da Nota __

 Preencher com a data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Data no formato AAAAMMDD \(sem barras\) 

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN14

__Regras para o campo  Mês de Referência __

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

OS4405

RN15

__Regras para o campo  Ano de Referência __

Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

OS4405

RN16

__Regras para o campo  Status __

Preencher com:

__“1”__ – Normal,  se campo SITUACAO = “N” da SAFX07\.

__“2” __– Cancelada, se campo SITUACAO = “S” da SAFX07\.

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN17

__Regras para o campo  Data do Cancelamento__

Se caso o campo “Status”\(RN16\) esteja preenchido com o valor “__2__”, preencher com o campo DAT\_CANCELAMENTO da tabela DWT\_DOCTO\_FISCAL, referente a data de cancelamento da nota\. Preencher  no formato AAAAMMDD \(sem barras\)\.

Senão, preencher com zeros\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN18

__Regras para o campo Natureza da Operação :__

Preencher com:

__“1”__ – Serviço, quando Classificação do Documento fiscal = 2\.

__“2”__ – Mista, quando Classificação do Documento fiscal = 3

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN19

__Regras para o campo Valor Total:__

Preencher com:

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres

OS4405

RN20

__Regras para o campo Valor dos Serviços:__

Preencher com:

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\.

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres

OS4405

RN21

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>__Regras para o campo Valor dos Impostos:__

Preencher com:

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres

OS4405

RN22

__Regras para o campo Recolhimento do Imposto:__

Preencher com:

__“0” – Isento__\. Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\. 

__“1” – Retido__\. Para que esse campo seja preenchido com __“1”,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(deve ser o campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\. 

__“3” – Simples Nacional__\. Quando o campo IND\_ISS da tabela ESTABELECIMENTO = “07” \.

  

__“2” – A recolher\. __Não será tratado nesta OS\.     

Caso nenhuma das opões seja verdadeira, Não preencher__\.__

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN23

__Regras para o campo Atividade:__

Preencher com:

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN24

__Regras para o campo Alíquota:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Campo tipo numérico com quatro casas, sendo que duas representam os decimais\. Valor sem separador de decimais \(__,__ ou __\.__\)\. 

Tipo: Numérico

Tamanho: 04 caracteres

OS4405

RN25

__Regras para o campo Razão Social do Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 100 caracteres

OS4405

RN26

__Regras para o campo Cidade do Prestador:__

Preencher com o campo CIDADE da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 40 caracteres

OS4405

RN27

__Regras para o campo UF do Prestador:__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO preenchido na tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4405

RN28

__Regras para o campo Local do Prestador:__

Identifica o local da Prestação, devendo preencher com:

__“0”__ \- Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL  for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__“1”__ \- Se o campo COD\_MUNICIPIO da tabela  DWT\_DOCTO\_FISCAL  for um valor válido e diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Senão, preencher com:

__“2”__ – Não cadastrado\. Quando não estiver preenchido o município da nota\.

Tipo: Alfanumério

Tamanho: 01 caracteres

OS4405

RN29

__Regras para o campo Identificação do Tomador:__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR; 

Senão, 

Preencher com o campo  CGC\_CPF  da tabela X04\_PESSOA\_FIS\_JUR quando o campo  INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR estiver vazio;

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN30

__Regras para o campo Tipo Identificação Tomador:  __

Preencher com:

 __“2”__ – IM, quando o campo “Identificação do Prestador” \(RN29\)  estiver preenchido com uma Inscrição Municipal, ou seja, quando o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR estiver preenchido\.

__“0”__ – CNPJ, quando o campo “Identificação do Tomador”  estiver preenchido com um CNPJ, ou seja, quando o valor inserido no campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 14 posições\.

__“1”__ – CPF, quando o campo “Identificação do Tomador”  estiver preenchido com um CPF, ou seja, quando o valor inserido no campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 11 posições\.

 

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN31

__Regras para o campo Razão Social do Tomador:  __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 100 caracteres

OS4405

RN32

__Regras para o campo Cidade do Tomador:  __

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 40 caracteres

OS4405

RN33

__Regras para o campo UF do Tomador:  __

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4405

RN34

__Regras para o campo Local do Tomador:  __

Preencher com:

__“0”__ \- Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__“1”__ \- Se o campo COD\_MUNICIPIO da tabela  X04\_PESSOA\_FIS\_JUR for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO__\.__

__“2”__ – Não será tratado nesta OS\.

__“3” – __Não será tratado nesta OS\.

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN35

__Regras para o campo Número do RPS:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN36

__Regras para o campo Tipo do RPS:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Numérico

Tamanho: 01 caracteres

OS4405

RN37

__Regras para o campo Série RPS:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Alfanumérico

Tamanho: 05 caracteres

OS4405

RN38

__Regras para o campo Hora da Emissão da NFe:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Numérico

Tamanho: 06 caracteres

OS4405

RN39

__Regras para o campo Data da Geração do RPS:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN40

__Regras para o campo Hashcode:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Alfanumérico

Tamanho: 20 caracteres

OS4405

RN41

__Regras para o campo Valor Tributos Federais PIS :  __

Preencher com o campo VLR\_PIS da DWT\_ITENS\_SERV\.

Valor do PIS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN42

__Regras para o campo Valor Tributos Federais CONFINS :  __

Preencher com o campo VLR\_COFINS da DWT\_ITENS\_SERV\.

Valor do CONFINS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais         \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN43

__Regras para o campo Valor Tributos Federais I\.R :  __

Preencher com o campo VLR\_TRIBUTO\_IR da DWT\_ITENS\_SERV\.

Valor do I\.R é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN44

__Regras para o campo Valor Tributos Federais INSS :  __

Preencher com o campo VLR\_INSS\_RETIDO da DWT\_ITENS\_SERV\.

Valor do I\.R é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN45

__Regras para o campo Valor Tributos Federais CSLL :  __

Preencher com o valor do campo VLR\_CSLL da DWT\_ITENS\_SERV\.

Valor do INSS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN46

__Regra para o campo Motivo do Cancelamento:__

Preencher com as informações do campo DESCRIÇÃO da tabela OBS\_MOTIVO\_NOTA, que é referente ao código do campo      138 –“COD\_MOTIVO” da tabela SAFX07\. 

OBS\.: Os códigos e suas descrições, são cadastrados manualmente pelo usuário na tela “DW / Manutenção / Cadastros /  Motivo de Cancelamento e Extravio de NF\. É Preenchido de acordo com a tabela de Motivos de Cancelamento estipulada por cada Município\.

\- Caso não seja  informado nenhuma informação de Motivo de cancelamento, deverá  deixar em branco\.

Tipo: Alfanumérico

Tamanho: 150 caracteres

OS4405

RN47

__Regras para o campo Descriminação Serviços:__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referêntea descrição do serviço\.

Preencher com Brancos\.

Tipo: Alfanumérico

Tamanho: 1260 caracteres

OS4405

RN48

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Documentos de Entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.
- Quando a nota não tiver itens não deve ser recuperada\. 

OS4405

RN49

__Regras para o campo Identificação do Prestador :__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR; 

Senão, 

Preencher com o campo  CGC\_CPF  da tabela X04\_PESSOA\_FIS\_JUR quando o campo  INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR estiver vazio;

Tipo: Numérico 

Tamanho: 14 caracteres

OS4405

RN50

__Regras para o campo Tipo Identificação: __

__Preencher com:__

__“2”__ – IM, quando o campo “Identificação do Prestador” \(RN49\)  estiver preenchido com uma Inscrição Municipal, ou seja, quando o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR estiver preenchido\.

 

__“0”__ – CNPJ, quando o campo “Identificação do Prestador”  estiver preenchido com um CNPJ, ou seja, quando o valor inserido no campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 14 posições\.

__“1”__ – CPF, quando o campo “Identificação do Prestador”  estiver preenchido com um CPF, ou seja, quando o valor inserido no campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 11 posições\.

 

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN51

__Regras para o campo Tipo: __

Preencher com:

__“2”__ – __Nota Recebida__ 

Tipo: Alfanumérico 

Tamanho: 01 caracteres

OS4405

RN52

__Regras para o campo Número da Nota: __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN53

__Regras para o campo Documento Fiscal: __

Preencher com o campo Modelo da tela Parâmetros por Município / Parâmetros / Tipo Docto Msaf x Tipo Docto, referente ao Documento cadastrado na nota fiscal\.  Caso não seja parametrizado, deverá informar com brancos\.

Obs\.: Caso o Tipo de Documento não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: "Tipo de Documento não parametrizado em Parâmetros por Município\. Favor verificar\!”

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN54

__Regras para o campo Data de Emissão da Nota __

 Preencher com a data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Data no formato AAAAMMDD \(sem barras\) 

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN55

__Regras para o campo  Mês de Referência __

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

OS4405

RN56

__Regras para o campo  Ano de Referência __

Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

OS4405

RN57

__Regras para o campo  Status __

Preencher com o texto fixo __“0”__\.

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN58

__Regras para o campo  Data do Cancelamento__

Como não será recuperada as notas canceladas para Serviços Tomados, deverá preencher com zeros\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN59

__Regras para o campo Natureza da Operação :__

Preencher com:

__“1”__ – Serviço, quando Classificação do Documento fiscal = 2\.

__“2”__ – Mista, quando Classificação do Documento fiscal = 3

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN60

__Regras para o campo Valor Total:__

Preencher com:

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres      

OS4405

RN61

__Regras para o campo Valor dos Serviços:__

Preencher com:

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\.

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres

OS4405

RN62

__Regras para o campo Valor dos Impostos:__

Preencher com:

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Campo numérico com onze casas, sendo que duas representam os decimais\.  

Tipo: Numérico

Tamanho: 11 caracteres

OS4405

RN63

__Regras para o campo Recolhimento do Imposto:__

Preencher com:

__“1” – Isento__\. Verificar se__ __o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__“2” – Retido__\. Para que esse campo seja preenchido com __“2”\- __SIM__,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(deve ser sempre o campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.  

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \. 

__“4” \-  __Não será tratado nesta OS\.

Caso nenhuma das opões seja verdadeira, Não preencher__\.__

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN64

__Regras para o campo Atividade:__

Preencher com:

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\.\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN65

__Regras para o campo Alíquota:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Campo tipo numérico com quatro casas, sendo que duas representam os decimais\. Valor sem separador de decimais \(__,__ ou __\.__\)\. 

Tipo: Numérico

Tamanho: 04 caracteres

OS4405

RN66

__Regras para o campo Razão Social do Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 100 caracteres

OS4405

RN67

__Regras para o campo Cidade do Prestador:__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 40 caracteres

OS4405

RN68

__Regras para o campo UF do Prestador:__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO preenchido na tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4405

RN69

__Regras para o campo Local do Prestador:__

Identifica o local da Prestação, devendo preencher com:

Preencher com:

 

__“0”__ \- Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__“1”__ \- Se o campo COD\_MUNICIPIO da tabela  X04\_PESSOA\_FIS\_JUR  for um valor válido e diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO__\.__

__ “2”__ – Não será tratado\.

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN70

__Regras para o campo Identificação do Tomador:__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO; 

Senão, 

Preencher com o campo CGC da tabela ESTABELECIMENTO quando o campo  INSC\_MUNICIPAL da tabela ESTABELECIMENTO estiver vazio;

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN71

__Regras para o campo Tipo Identificação Tomador:  __

Preencher com:

__“2”__ – IM, quando o campo “Identificação do Prestador” \(RN70\)  estiver preenchido com uma Inscrição Municipal, ou seja, quando o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO estiver preenchido\. 

 

__“0”__ – CNPJ, quando o campo “Identificação do Tomador”  estiver preenchido com um CNPJ, ou seja, quando o valor inserido no campo CGC da tabela ESTABELECIMENTO possuir 14 posições\.

__“1”__ – Não será tratado\.

 

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4405

RN72

__Regras para o campo Razão Social do Tomador:  __

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\. 

Tipo: Alfanumérico

Tamanho: 100 caracteres

OS4405

RN73

__Regras para o campo Cidade do Tomador:  __

Preencher com o campo CIDADE da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 40 caracteres

OS4405

RN74

__Regras para o campo UF do Tomador:  __

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4405

RN75

__Regras para o campo Local do Tomador:  __

Preencher com:

__“0”__ \- Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL  for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__“1”__ \- Se o campo COD\_MUNICIPIO da tabela  DWT\_DOCTO\_FISCAL  for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO__\.__

Senão, preencher com:

__“2”__ – Não cadastrado\. Quando não estiver preenchido o município da nota\.

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4405

RN76

__Regras para o campo Número do RPS:  __

Não será tratado nesta OS\.  Preencher com Zeros\.

Tipo: Numérico

Tamanho: 14 caracteres

OS4405

RN77

__Regras para o campo Tipo do RPS:  __

Não será tratado nesta OS\. Preencher com Zeros\.

Tipo: Numérico

Tamanho: 01 caracteres

OS4405

RN78

__Regras para o campo Série RPS:  __

Não será tratado nesta OS\. Preencher com Zeros\.

Tipo: Alfanumérico

Tamanho: 05 caracteres

OS4405

RN79

__Regras para o campo Hora da Emissão da NFe:  __

Não será tratado nesta OS\. Preencher com Zeros\.

Tipo: Numérico

Tamanho: 06 caracteres

OS4405

RN80

__Regras para o campo Data da Geração do RPS:  __

Não será tratado nesta OS\. Preencher com Zeros\.

Tipo: Numérico

Tamanho: 08 caracteres

OS4405

RN81

__Regras para o campo Hashcode:  __

Não será tratado nesta OS\. Deixar em branco\.

Tipo: Alfanumérico

Tamanho: 20 caracteres

OS4405

RN82

__Regras para o campo Valor Tributos Federais PIS :  __

Preencher com o campo VLR\_PIS da DWT\_ITENS\_SERV\.

Valor do PIS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN83

__Regras para o campo Valor Tributos Federais CONFINS :  __

Preencher com o campo VLR\_COFINS da DWT\_ITENS\_SERV\.

Valor do CONFINS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais         \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN84

__Regras para o campo Valor Tributos Federais I\.R :  __

Preencher com o campo VLR\_TRIBUTO\_IR da DWT\_ITENS\_SERV\.

Valor do I\.R é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN85

__Regras para o campo Valor Tributos Federais INSS :  __

Preencher com o campo VLR\_INSS\_RETIDO da DWT\_ITENS\_SERV\.

Valor do I\.R é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN86

__Regras para o campo Valor Tributos Federais CSLL :  __

Preencher com o valor do campo VLR\_CSLL da DWT\_ITENS\_SERV\.

Valor do INSS é numérico com doze casas, sendo que quatro representam os decimais\. Valor sem separador de decimais \(__, __ou __\.__\)\. 

Tipo: Numérico

Tamanho: 12 caracteres

OS4405

RN87

__Regra para o campo Motivo do Cancelamento:__

Deverá informar em branco\.

Tipo: Alfanumérico

Tamanho: 150 caracteres

OS4405

RN88

__Regras para o campo Descriminação Serviços:__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referêntea descrição do serviço\.

Preencher com Brancos\.

Tipo: Alfanumérico

Tamanho: 1260 caracteres

OS4405

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

