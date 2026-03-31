# MTZ-DMS_Santo_Angelo-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-DMS_Santo_Angelo-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-09-22
- **Tamanho:** 138 KB

---

  

THOMSON REUTERS

Municipal

 Santo Ângelo \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3792

DW – Municipal \- Geração do Meio Magnético Santo Ângelo

Deverá ser criado o módulo de Santo Ângelo para a geração do meio magnético Santo Ângelo, onde serão informados os documentos fiscais de serviço prestados \(emitidos\) e tomados \(recebidos\)\.

__OS3341\-A3__

Geração do Meio Magnético para nota fiscais com número de documento com mais de 12 posições\.  

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

__MFS\_2071__

DW \- MUNICIPAL – Santo Ângelo – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

__MFS\-893850__

Rosemeire Santos

Este documento tem como objetivo ajustar as regras de geração do arquivo meio magnético do município de Santo Ângelo/RS

 

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Santo Ângelo” deve ficar localizado no grupo “Municipal”\.

Descrição do Módulo: <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>“Consiste na entrega das informalções sobre os serviços tomados ou prestados do município de Santo Ângelo\.”

OS3792

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “17509” \(Santo Ângelo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Santo Ângelo, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3792

RN03

__Estrutura de menus do módulo Santo Ângelo:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Santo Ângelo:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

OS3792

RN04

__Regra de criação do nome do arquivo__

Deverá respeitar o seguinte formato: 

__Serviços Prestados:__

<a id="OLE_LINK4"></a>__SP\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

__               __<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a>__SP__: representa a obrigação que está sendo gerada, apenas registros de serviços prestados\.__       __

__               MUNICIPIO__: representa o município que está sendo gerado\.

               __DDMMAAAA__: representa a data inicial da geração\.           

               __\.txt__: extensão do arquivo\.

Ex: SP\_SANTOANGELO\_25012014\.txt

__Serviços Tomados:__

__ST\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

               __ST__: representa a obrigação que está sendo gerada, apenas registros de serviços tomados\.__       __

__               MUNICIPIO__: representa o município que está sendo gerado\.

               __DDMMAAAA__: representa a data inicial da geração\.           

               __\.txt__: extensão do arquivo\.

Ex: ST\_SANTOANGELO\_01012010\.txt

OS3792

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

Gerar Serviços Tomados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

Obs: Devem ser gerados arquivos separados para serviços prestados e serviços tomados\.

OS3792

MFS\_2071

RN06

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Regras referentes à formatação dos registros gerados no meio magnético:__

- Somente é permitido gerar arquivos de extensão __\.txt \. __
- Todos os campos serão separados por “__ ;__ ”\.
- Os campos do tipo numérico devem ser alinhados à direita, completados com zeros à esquerda até atingir o tamanho exato do campo, sem vírgula e sem ponto e os não utilizados deverão ser preenchidos com zeros;
- Os campos do tipo numérico, campo de valores deve ser preenchidos sem complemento dos zeros a esquerda e com ponto\.
- Para o campo de valor de alíquota, deverão considerar duas casas decimais\. 
- Os campos do tipo Alfanuméricos devem ser alinhados à esquerda com brancos a direita e os não utilizados deverão conter brancos;
- Os campos do tipo Alfanumerico devem ser preenchidos conforme a obrigatoriedade, quando não tiver deve apenas conter o campo vazio\.
- Informe a data no formato AAAA\-MM\-DD HH:MM:SS\. Caso não tenha hora, colocar ela no formato 00:00:00\.

__Modelo do Arquivo esperado:__

NFS;2025;0001;0001;18672652000138;2025\-03\-07 12:03:00;467;3412\.20;03;1;92665611054501;1;;0;0\.00;0\.00;0\.00;0\.00;12;

SER;18672652000138;467;98807240;10;2;0\.00;3412\.20;03;2025

NFS;2025;0001;0001;05017262000182;2025\-03\-07 12:03:00;61001;13139\.67;03;1;92665611054501;1;;0;394\.19;0\.00;0\.00;0\.00;02;

SER;05017262000182;61001;94920170;10;2;5\.00;13139\.67;03;2025

OS3792

__MFS\-893850__

RN07

__Regra geral p/ Registro de Serviços Prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas 

com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);  
- Classificação do Documento fiscal = 2 ou 3;    
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.
- Quando a nota não tiver itens não deve ser recuperada\.

OS3792

RN08

__Regras para o campo Identificação do Registro \- Linha 1 do tipo NFS \(Identificação do Documento Fiscal\)__

Preencher com o texto fixo Declaração Dos Dados Importados \(NFS\) “__NFS”__

OS3792

__MFS\-893850__

RN09

__Regras para o campo Ano de Exercício:__

Indica o ano de competência da declaração\.  Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Formato __AAAA\.__

Tipo: Numérico

Tamanho: 4 Caracteres

OS3792

RN10

__Regras para o campo Código do Modelo: __

Preencher com o campo Modelo da tela Parâmetros por Município / Parâmetros / Modelo Msaf x Modelo, referente ao modelo cadastrado na nota fiscal\.

 \- No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

__Obs\.:__ Caso o Modelo da Nota não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: 

Para o modelo "XXX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização do “Modelo Msaf x Modelo”\. Efetuar a parametrização no menu Parâmetros > Modelo Msaf x Modelo no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tamanho: 04  caracteres

OS3792

RN11

__Regras para o campo Série: __

Preencher com o campo Série da tela Parâmetros por Município / Parâmetros / Série Msaf x Série, referente a Série cadastrada na nota fiscal\.

\- No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

__Obs\.:__ Caso a Série não for parametrizada em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: 

Para a série "XX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização da “Série Msaf x Série”\. Efetuar a parametrização no menu Parâmetros > Série Msaf x Série no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tamanho: 04  caracteres

OS3792

RN12

__Regras para o campo CPF/CNPJ do Prestador do Serviço: __

 Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

RN13

__Regras para o campo Data de Emissão do Doc\. Fiscal __

 Preencher com a data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Data no formato “AAAA\-MM\-DD HH:MM:SS”

Caso não tenha hora, colocar ela no formato “00:00:00”\.

Tipo: Data

Tamanho: 19 caracteres

OS3792

RN14

__Regras para o campo Número da Documento: __

Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL, __somente o número do documento, sem os zeros a esquerda\.

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__OBS\.: Devido restrições de Santo ângelo, será exibido apenas as 15 primeiras posições, conforme exigência do layout do validador\.__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15 caracteres

OS3792

OS3341\-A3

__MFS\-893850__

RN15

__Regras para o campo Valor do Documento:__

Preencher com:

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Formado: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\)\.

OS3792

__MFS\-893850__

RN16

__Regras para o campo  Mês de Competência__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Alfanumérico 

Tamanho: 02 caracteres

OS3792

RN17

__Regras para o campo  Tipo__

Preencher com o texto fixo “__0__” para prestados

Tipo: Numérico 

Tamanho: 01 caracteres

OS3792

__MFS\-893850__

RN18

__Regras para o campo CPF/CNPJ do tomador do serviço__

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \. 

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

RN19

__Regras para o campo  Situação do Documento __

Preencher com:

__“1”__ \- Se campo SITUACAO = “N” da SAFX07\.

__“3” \- __Se campo SITUACAO = “S” da SAFX07\.

 

“__2__” – Não será tratado\.

“__4__” – Não será tratado\. 

Tipo: Numérico

Tamanho: 01 caracter

OS3792

RN20

__Regra para o campo  Observações do Documento__

Preencher com brancos

Tipo: Alfanumérico

Tamanho: 300 caracteres

OS3792

__MFS\-893850__

RN21

__Regra para o campo Optante do Simples:__

Preencher com:

__“1” \- __Quando o campo IND\_ISS da tabela ESTABELECIMENTO = “07” \.

Senão preencher com “__0__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS3792

RN22

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>__Regras para o campo Valor dos Impostos:__

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com zeros, sem ponto e sem vírgula\.

Formado: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN23

__Regra para o campo BaseCalculo__

Preencher com o campo BASE\_ISS da tabela DWT\_ITENS\_SERV\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), __  __deverá preencher com zeros, sem ponto e sem virgula\.

Formado: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN24

__Regra para o campo Dedução__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com zeros, sem ponto e sem virgula\.

Formado: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN25

__Regra para o campo Desconto__

Preencher com o somatório do campo VLR\_DESCONTO da tabela DWT\_ITENS\_SERV\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com zeros, sem ponto e sem virgula\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN26

__Regra para o campo Código da Situação Tributária__

Deverá preencher com:

“__6__” – Isento\. Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

“__7__” – Imune\. Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\. 

“__8__” – Serviços Sujeitos a Tributação Fixa\. Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

“__9__” \- ISS regime Estimativa\. Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\. 

“__3__” – Tributada com redução da base de cálculo\. Quando o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município em questão e caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, o COD\_MUNICIPIO da tabela ESTABELECIMENTO deverá ser igual ao município em questão e o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referente ao serviço cadastrado na nota deverá ser __igual__ à 17\.05\. 

“__4__” – Tributada Integralmente\. Quando o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município em questão e caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, o COD\_MUNICIPIO da tabela ESTABELECIMENTO deverá ser igual ao município em questão e o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referente ao serviço cadastrado na nota deverá ser __diferente__ de 1705\.

“__2__” – Quando o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL <> município em questão\. 

__Obs\.:__ No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher cojm “__20__”\.

Tipo: Numérico

Tamanho: 02 caracteres

OS3792

RN27

__Regras para o campo Identificação do Registro \- Linha 2 do tipo SER \(Identificação do Serviço relacionado ao Documento Fiscal\)__

Preencher com o texto fixo Descrição Dos Dados Importados \(SER\) “__SER”__

__Obs\.: __A linha 2 do tipo SER, deve ficar embaixo da linha 1 Tipo NFS

OS3792

__MFS\-893850__

RN28

__Regras para o campo CPF/CNPJ do Prestador do Serviço: __

 Preencher com o campo CGC da tabela ESTABELECIMENTO

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

__MFS\-893850__

RN29

__Regras para o campo Número do Documento: __

Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL, __somente o número do documento, sem os zeros a esquerda\.

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL\.__

__OBS\.: Devido restrições de Santo ângelo, será exibido apenas as 15 primeiras posições, conforme exigência do layout do validador\.__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15 caracteres\. 

OS3792

OS3341\-A3

__MFS\-893850__

RN30

__Regras para o campo Local da Prestação do Serviço \(CEP\): __

 Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR; 

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

Tipo: Alfanumérico

Tamanho: 08 caracteres

OS3792

__MFS\-893850__

RN31

__Regras para o campo Código do Serviço:__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\. Porém deverá inserir no campo, apenas os dois primeiros dígitos da esquerda para a direita\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

Tipo: Numérico

Tamanho: 11 caracteres

OS3792

__MFS\-893850__

RN32

__Regras para o campo Atividade:__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\. Porém deverá inserir no campo, apenas os dois últimos dígitos da direita\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com “__0__”\.

Tipo: Numérico

Tamanho: 11 caracteres

OS3792

__MFS\-893850__

RN33

__Regras para o campo Alíquota:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com zeros, sem ponto e sem virgula\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN34

__Regras para o campo Valor do Serviço:__

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\.

Obs\.: No caso de notas canceladas \(campo SITUACAO = “S” da SAFX07\), deverá preencher com zeros, sem ponto e sem virgula\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN35

__Regras para o campo Mês de Competência:__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico

Tamanho: 2 Caracteres

OS3792

RN36

__Regras para o campo Ano de Exercício:__

Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico

Tamanho: 4 Caracteres

OS3792

RN37

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Documentos de Entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.
- Quando a nota não tiver itens não deve ser recuperada\. 

OS3792

RN38

__Regras para o campo Identificação do Registro \- Linha 1 do tipo NFS \(Identificação do Documento Fiscal\)__

Preencher com o texto fixo Declaração Dos Dados Importados \(NFS\) “__NFS”__

OS3792

__MFS\-893850__

RN39

__Regras para o campo Ano de Exercício:__

Indica o ano de competência da declaração\.  Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Formato __AAAA\.__

Tipo: Numérico

Tamanho: 4 Caracteres

OS3792

RN40

__Regras para o campo Código do Modelo: __

Preencher com o campo Modelo da tela Parâmetros por Município / Parâmetros / Modelo Msaf x Modelo, referente ao modelo cadastrado na nota fiscal\.

__Obs\.:__ Caso o Modelo da Nota não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: 

Para o modelo "XXX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização do “Modelo Msaf x Modelo”\. Efetuar a parametrização no menu Parâmetros > Modelo Msaf x Modelo no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tamanho: 04  caracteres

OS3792

RN41

__Regras para o campo Série: __

Preencher com o campo Série da tela Parâmetros por Município / Parâmetros / Série Msaf x Série, referente a Série cadastrada na nota fiscal\.

__Obs\.:__ Caso a Série não for parametrizada em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: 

Para a série "XX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização da “Série Msaf x Série”\. Efetuar a parametrização no menu Parâmetros > Série Msaf x Série no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tamanho: 04  caracteres

OS3792

RN42

__Regras para o campo CPF/CNPJ do Prestador do Serviço: __

 Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \. 

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

RN43

__Regras para o campo Data de Emissão do Doc\. Fiscal __

 Preencher com a data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Data no formato “AAAA\-MM\-DD HH:MM:SS”

Caso não tenha hora, colocar ela no formato “00:00:00”\.

Tipo: Data

Tamanho: 19 caracteres

OS3792

RN44

__Regras para o campo Número da Documento: __

Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL, __somente o número do documento, sem os zeros a esquerda\.

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL\.__

__OBS\.: Devido restrições de Santo Ângelo, será exibido apenas as 15 primeiras posições, conforme exigência do layout do validador\.__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15 caracteres

OS3792

OS3341\-A3

__MFS\-893850__

RN45

__Regras para o campo Valor do Documento:__

Preencher com:

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Campo numérico com dez casas, sendo que duas representam os decimais\. 

 

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres

OS3792

__MFS\-893850__

RN46

__Regras para o campo  Mês de Competência__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Alfanumérico 

Tamanho: 02 caracteres

OS3792

RN47

__Regras para o campo Tipo__

Preencher com o texto fixo __“1”__

Preencher com o texto fixo “__0__”\.

Tipo: Numérico 

Tamanho: 01 caracteres

OS3792

__MFS\-893850__

RN48

__Regras para o campo CPF/CNPJ do tomador do serviço__

Preencher com o campo CGC da tabela ESTABELECIMENTO \. 

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

RN49

__Regras para o campo  Situação do Documento __

Preencher com:

__Preencher com texto fixo “1”__

__“3” \- __Não será tratado\.

 

“__2__” – Não será tratado\.

“__4__” – Não será tratado\. 

Tipo: Numérico

Tamanho: 01 caracter

OS3792

RN50

__Regra para o campo  Observações do Documento__

Apresentar o campo sem espaços em branco

Tipo: Alfanumérico

Tamanho: 300 caracteres

OS3792

__MFS\-893850__

RN51

__Regra para o campo Optante do Simples:__

Preencher com:

__“1” \- __Quando o campo IND\_ISS da tabela ESTABELECIMENTO = “07” \.

Senão preencher com “__0__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS3792

RN52

__Regras para o campo Valor dos Impostos:__

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN53

__Regra para o campo BaseCalculo__

Preencher com o campo BASE\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN54

__Regra para o campo Dedução__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN55

__Regra para o campo Desconto__

Preencher com o somatório do campo VLR\_DESCONTO da tabela DWT\_ITENS\_SERV\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792__ __

__MFS\-893850__

RN56

__Regra para o campo Código da Situação Tributária__

Deverá preencher com:

“__6__” – Isento\. Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

“__7__” – Imune\. Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.__ __ 

“__9__” \- Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

“__5__” – Quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur da nota <> do município em questão E o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota = 1705\.

“__2__” – Quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur da nota <> do município em questão e o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota diferente de 1705\.

“__12__” \- Quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur da nota = do município em questão\.

Tipo: Numérico

Tamanho: 02caracteres

OS3792

RN57

__Regras para o campo Identificação do Registro \- Linha 2 do tipo SER \(Identificação do Serviço relacionado ao Documento Fiscal\)__

Preencher com o texto fixo Descrição Dos Dados Importados \(SER\) “__SER”__

__Obs\.: __A linha 2 do tipo SER, deve ficar embaixo da linha 1 Tipo NFS

OS3792

__MFS\-893850__

RN58

__Regras para o campo CPF/CNPJ do Tomador do Serviço: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\.

 Preencher com o campo CGC da tabela ESTABELECIMENTO; 

Tipo: Alfanumérico

Tamanho: 14 caracteres

OS3792

__MFS\-893850__

RN59

__Regras para o campo Número do Documento: __

Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL, __somente o número do documento, sem os zeros a esquerda\.

Tela\-A ç  Modulo: Básicos >> Parâmetros Menu: Preliminares >> Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)

Se o campo COD\_ESTAB selecionado na geração for = o campo COD\_ESTAB da Tela\-A

  E

Campo Data\_fiscal for maior ou igual o campo Data Inicio da Tela\-A    

  E

Campo NUM\_DOCFIS\_SERV da tabela DWT\_DOCTO\_FISCAL estiver preenchido

  

Então, preencher com o campo NUM\_DOCFIS\_SERV da tabela DWT\_DOCTO\_FISCAL\.

OBS\.: Devido restrições de Santo ângelo, será exibido apenas as 15 primeiras posições, conforme exigência do layout do validador\.

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15 caracteres

OS3792

OS3341\-A3

__MFS\-893850__

RN60

__Regras para o campo Local da Prestação do Serviço \(CEP\): __

 Preencher com o campo CEP da tabela ESTABELECIMENTO; 

Tipo: Alfanumérico

Tamanho: 08 caracteres

OS3792

RN61

__Regras para o campo Código do Serviço:__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\. Porém deverá inserir no campo, apenas os dois primeiros dígitos da esquerda para a direita\.

Tipo: Numérico

Tamanho: 11 caracteres

OS3792

RN62

__Regras para o campo Atividade:__

Preencher com:

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116\. Porém deverá inserir no campo, apenas os dois últimos dígitos da direita\.

Tipo: Numérico

Tamanho: 11 caracteres

OS3792

RN63

__Regras para o campo Alíquota:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN64

__Regras para o campo Valor do Serviço:__

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\.

Formato: 0\.00

Tipo: Numérico

Tamanho: 10\.2 caracteres \(Campo numérico com dez casas, sendo que duas representam os decimais\.\)

OS3792

__MFS\-893850__

RN65

__Regras para o campo Mês de Competência:__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico

Tamanho: 2 Caracteres

OS3792

RN66

__Regras para o campo Ano de Exercício:__

Preencher com o ano informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico

Tamanho: 4 Caracteres

OS3792

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

