# MTZ_DS_Imperatriz_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DS_Imperatriz_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-07
- **Tamanho:** 99 KB

---

THOMSON REUTERS 

Municipal

DS Imperatriz \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1532

Geração do Meio Magnético DS Imperatriz

Deverá ser criado um novo módulo que permita a geração do meio magnético DS Imperatriz em que serão informados apenas os documentos fiscais de serviços tomados e prestados\. 

MFS\-829438    

Geração do Meio Magnético DS Imperatriz

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Imperatriz” deve ficar localizado no grupo “Municipal”\.

MFS1532

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MA” e ao código de município do IBGE igual a “5302” \(Imperatriz\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Imperatriz, Maranhão\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS1532

RN03

__Estrutura de menus do módulo Imperatriz:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Imperatriz:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

MFS1532

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

__ST\_DS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração

__MUNICIPIO__: representa o município que está sendo gerado\.

__ST\_DS__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_DS\_IMPERATRIZ\_01012010\.TXT

MFS1532

MFS829438    

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final: __deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Serviço do Declarante:__ deve ser uma lista do tipo Combobox\. Deverá exibir as seguintes opções:

\- Serviços em Geral \- Tributados pelo ISS

\- Serviços com Dedução na Base de Cálculo do ISS ou com Exclusão de Material

\- Serviços de Saúde

\- Comércio, Indústria, Substituição Tributária

\- Serviços de Construção Civil

\- Serviços de Pessoa Jurídica \- Sem Notas Fiscais Emitidas

\- Serviços de Caráter Pessoal

\-  Serviços de Educação e Treinamento

\- Instituições Financeiras

\- Transportes Coletivos

Deve exibir a opção “ Serviços em Geral \- Tributados pelo ISS” selecionada como Default\. 

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Imperatriz, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS1532

RN06

__Regras Gerais de formatação do arquivo__

O arquivo a ser gerado para importação dever  ser no  formato  texto\.

Observações :

\- Todos os registros deverão ser finalizados com a quebra de linha\.

\- Campos numericos, devem ser preenchidos com zeros à esquerda até atingir o tamanho  exato  do campo\. Quando o campo for opcional, ou seja, o conteúdo do campo não for fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\. 

\- Serão utilizados 02 posições para a parte decimal\. Exemplo:

O campo com tamanho 12 significa: 10 posições para a parte inteira e 02 posições para a parte decimal\.

Para um valor de R$ 2\.500,__00__ no arquivo deverá estar gravado assim: 0000002500__00__

\- Os valores numéricos serão truncados, quando a informação preenchida no banco de dados, for maior do que o tamanho máximo exigido pelo layout\. 

\- Todos os campos tipo Texto,  deverão ser preenchidos alinhados pela esquerda, Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo\.

MFS1532

__Segmento A \- Identificação do Declarante__

RN07

__Campo Segmento:__

Preencher com o valor fixo __“A”__\.

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS1532

RN08

__Campo Número Identificação do registro no segmento:__

Preencher com o valor fixo __“0000”__\.

Tipo: Numérico

Tamanho: 04 caracter

MFS1532

RN09

__Campo  Mês de Competência:__

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>Preencher com o Mês e Ano informado no campo “Data Inicial” na tela de Geração do Meio Magnético\.

Tipo: Numérico 

Tamanho: 06 caracteres __\(AAAAMM\)__

MFS1532

RN10

__Campo  CNPJ/CPF do Declarante:__

Preencher com campo CGC da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tam\.: 14 caracteres 

MFS1532

RN11

__Campo Razão Social do Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tam\.: 100 caracteres

MFS1532

RN12

__Campo Endereço do Declarante:__

Preencher com o conteúdo do campo ENDERECO da tabela ESTABELECIMENTO\.

Se o conteúdo do campo ENDERECO possuir mais de 40 posições significativas, deverá gerar a informação  truncado, mas retornar no log a seguinte mensagem: 

“O campo Endereço do Declarante \(ENDERECO\) ultrapassou o tamanho máximo permitido \(40 posições\)\.”

Tipo: Alfanumérico 

Tamanho máximo: 40

MFS1532

RN13

__Campo Número do Endereço do Declarante__

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Se o conteúdo do campo NUM\_ENDERECO possuir mais de 05 posições significativas, deverá gerar a informação  truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Endereço do Declarante \(NUM\_ENDERECO\) ultrapassou o tamanho máximo permitido \(05 posições\)\.”

Tipo: Alfanumérico 

Tamanho máximo: 05

MFS1532

RN14

__Campo Bairro do Declarante:__

Será gerado com o conteúdo do campo BAIRRO da tabela estabelecimento\.

Tipo: Alfanumérico 

Tamanho máximo: 20

MFS1532

RN15

__Campo CEP do Declarante:__

Será gerado com o conteúdo do campo CEP da tabela ESTABELECIMENTO\.

Tipo: numérico 

Tamanho máximo: 20

MFS1532

RN16

__Campo Município do Declarante:__

Será gerado com o conteúdo do campo CIDADE da tabela ESTABELECIMENTO\.

Se o conteúdo do campo CIDADE possuir mais de 20 posições significativas, deverá gerar a informação  truncado, mas retornar no log a seguinte mensagem: 

“O campo Município do Declarante \(CIDADE\)  ultrapassou o tamanho máximo permitido \(20 posições\)\.”

Tipo: Alfanumérico 

Tamanho máximo: 20

MFS1532

RN17

__Campo Telefone do Declarante:__

Será gerado com o conteúdo do campo TELEFONE da tabela ESTABELECIMENTO\.

Tipo: numérico 

Tamanho máximo: 10

MFS1532

RN18

__Campo Nome Fantasia:__

Será gerado com o conteúdo do campo NOME\_FANTASIA da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico 

Tamanho máximo: 50

MFS1532

RN19

__Campo Qualificação do Declarante:__

Preencher com texto fixo __“1”__:

Tipo: Numérico 

Tamanho máximo: 01

MFS1532

RN20

__Campo  Tipo de Serviço:__

Verificar na tela de Geração do Meio Magnético no campo Serviço do Declarante, as seguintes situações:

Se a opção “Serviços em Geral \- Tributados pelo ISS” estiver selecionada, preencher com __“01”__;

Se a opção “Serviços com Dedução na Base de Cálculo do ISS ou com Exclusão de Material” estiver selecionada, preencher com __“02”__;

Se a opção “Serviços de Saúde” estiver selecionada, preencher com __“03”__;

Se a opção “Comércio, Indústria, Substituição Tributária” estiver selecionada, preencher com __“04”__;

Se a opção “Serviços de Construção Civil” estiver selecionada, preencher com __“05”__;

Se a opção “Serviços de Pessoa Jurídica \- Sem Notas Fiscais Emitidas” estiver selecionada, preencher com __“08”__;

Se a opção “Serviços de Caráter Pessoal” estiver selecionada, preencher com __“09”__;

Se a opção “Serviços de Educação e Treinamento” estiver selecionada, preencher com __“10”__;

Se a opção “Instituições Financeiras” estiver selecionada, preencher com __“11”__;

Se a opção “Transportes Coletivos” estiver selecionada, preencher com __“12”__;

Tipo: numérico 

Tamanho: 02 caracteres

MFS1532

RN21

__Campo UF do Declarante:__

Preencher com o campo UF da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tam: 2

MFS1532

RN22

__Campo Inscrição Municipal__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

Se o conteúdo do campo INSC\_MUNICIPAL  possuir mais de 06 posições significativas, deverá gerar a informação  truncando, mas retornar no log a seguinte mensagem: 

“O campo Inscrição Municipal \(INSC\_MUNICIPAL \) ultrapassou o tamanho máximo permitido \(06 posições\)\.”

Tipo: Numérico

Tam\.: 06 caracteres

MFS1532

RN23

__Campo E\-Mail do Declarante__

Preencher com o campo EMAIL da tabela ESTABELECIMENTO\.

Se o conteúdo do campo EMAIL possuir mais de 30 posições significativas, deverá gerar a informação  truncando, mas retornar no log a seguinte mensagem: 

“O campo E\-Mail do Declarante \(EMAIL\) ultrapassou o tamanho máximo permitido \(30 posições\)\.”

Tipo: Alfanumérico

Tam\.: 30 caracteres

MFS1532

RN24

__Campo Complemento do Endereço do Declarante__

Preencher com o campo COMPL\_ENDERECO da tabela estabelecimento\.

Tipo: Alfanumérico

Tam\.: 20 caracteres

MFS1532

RN25

__Campo Serviços sem nota__

Preencher com o Texto Fixo __“0”\.__

Tipo: Alfanumérico

Tam\.: 01 caracter

MFS1532

RN26

__Campo Seqüencial do Registro__

Numeração seqüencial dos registros para todo o arquivo\.

Preencher com __000001__\.

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

__Segmento D \- Identificação das Notas Recebidas __

RN27

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.

MFS1532

RN28

__Campo Segmento:__

Preencher com o valor fixo __“D”__\.

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS1532

RN29

__Campo Número Identificação do registro no segmento:__

Preencher com sequêncial alinhado com zeros à esquerda\. Ex\.: 0001 até 9999 \(máximo\)\. Um segmento para nota recebida\.

Tipo: Numérico

Tamanho: 04 caracter

MFS1532

RN30

__Campo  Mês de Competência:__

Preencher com o Mês e Ano informado no campo “Data Inicial” na tela de Geração do Meio Magnético no formato AAAAMM\. Ex:201510\.

Tipo: Numérico

Tamanho: 04 caracter

MFS1532

RN31

__Campo Número da Nota:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

Na geração deste campo, deve ser consideradas 10 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 10 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(10 posições\)\.”

\(Ex para esta situação: Nº de NF 123456789012 será gerado 3456789012\)\.

Tipo: Numérico

Tamanho: 10 caracter

MFS1532

RN32

__Campo CNPJ/CPF do Prestador do Serviço:__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 06 da SAFX04\)\.

Tipo: Numérico

Tamanho: 14 caracter

MFS1532

RN33

__Campo Nome do Prestador do Serviço:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tam\.: 100 caracteres

MFS1532

RN34

__Campo Inscrição Municipal do Prestador do Serviço:__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

Se o conteúdo do campo INSC\_MUNICIPAL  possuir mais de 06 posições significativas, deverá gerar a informação  truncando, mas retornar no log a seguinte mensagem: 

“O campo Inscrição Municipal \(INSC\_MUNICIPAL \) ultrapassou o tamanho máximo permitido \(06 posições\)\.”

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

RN35

__Campo Série da Nota:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)

Tipo: Alfanumérico

Tam\.: 03 caracteres

MFS1532

RN36

__Campo Tipo do Documento:__

Preencher com a informação do campo “Tipo Documento” da tela Tipo Docto Msaf x Tipo Documento, em Parâmetros para Município, referente ao tipo de documento cadastrado na nota fiscal\.

Obs\.: Caso o tipo de documento não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para o Tipo de Documento "XX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização do Tipo Docto Msaf x Tipo Documento\. Efetuar a parametrização no menu Parâmetros > Tipo Docto Msaf x Tipo Documento no módulo "Parâmetros para Município"\.

Tipo: numérico

Tam\.: 01 caracteres

MFS1532

RN37

__Campo Indicador de Retenção:__

Indicador de Retenção de ISS\. Preencher com : 

__S__ = Sim\. Para preencher com “S”, deve verificar se o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado __OU __

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo 

COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

Se não, preencher com :

__“N__” = Não houve retenção de ISS\.

Tipo: numérico

Tam\.: 01 caracteres

MFS1532

RN38

__Campo Valor do Serviço:__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. 

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN39

__Campo Valor do ISS Retido:__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN40

__Campo Data de Emissão da Nota:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Data no formato DDMMAAAA\. Ex\.: __04072003__ \(04 de Julho de 2003\)\.

Tipo: Alfanumérico

Tam\.: 8 caracteres

MFS1532

RN41

__Campo Valor da Dedução:__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: Alfanumérico

Tam\.: 18 caracteres

MFS1532

RN42

__Campo Tipo da Atividade:__

Preencher com a informação do campo “Atividade” da tela Serviço Msaf x Atividade, em Parâmetros para Município, referente ao Código da Atividade cadastrada na nota fiscal\.

Obs\.: Caso o Código da Atividade não seja parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para a Atividade "XXX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização do Serviço Msaf x Atividade\. Efetuar a parametrização no menu Parâmetros > Serviço Msaf x Atividade no módulo "Parâmetros para Município"\.

Tipo: numérico

Tam\.: 03 caracteres

MFS1532

RN43

__Campo Fornecimento de Material:__

Preencher com:

‘__S__’ = Sim, quando o campo VLR\_MAT\_PROP da tabela SAFX09 estiver preenchida\.

 Se não Preencher com:

 ‘__N__’ = Não\.

Tipo: Alfanumérico

Tam\.: 01 caracteres

MFS1532

RN44

__Campo Suspenso por decisão Judicial:__

Preencher com:

__“S” \-  __Quando pelo menos umas das seguintes opções seja verdadeira:

- Campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”\.
- Se campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

__Se não, preencher com:__

Valor default__ = ‘N’__

Tipo: Alfanumérico

Tam\.: 01 caracteres

MFS1532

RN45

__Campo Inscrição de autônomo:__

Este campo deverá ser preenchido com __espaços__\. Não será tratado neste segmento\.

Tipo: Alfanumérico

Tam\.: 10 caracteres

MFS1532

RN46

__Campo Seqüencial do Registro:__

Numeração seqüencial dos registros para todo o arquivo\.

Numeração seqüencial dos registros para todo o arquivo\. Ex\.: Linha 1 = 000001; Linha 2 = 000002; e assim

sucessivamente\.

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

RN47

__Regra geral p/ Registro de Serviços Prestados__

Esses registros referente aos serviços prestados, apenas devem ser gerados no arquivo, quando o campo “Gerar serviços prestados” estiver marcado na tela de Geração e deve conter todas as notas com as seguintes características:

Recuperar as notas fiscais com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 e 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

       \-     Quando a nota não tiver itens não deve ser  recuperada\.

MFS1532

__Segmento  C \- Identificação das Notas Emitidas __

RN48

__Campo Segmento:__

Preencher com o valor fixo __“C”__\.

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS1532

RN49

__Campo Número Identificação do registro no segmento:__

Preencher com sequêncial alinhado com zeros à esquerda\. Ex\.: 0001 até 9999 \(máximo\)\. Um segmento para nota recebida\.

Tipo: Numérico

Tamanho: 04 caracter

MFS1532

RN50

__Campo  Mês de Competência:__

Preencher com o Mês e Ano informado no campo “Data Inicial” na tela de Geração do Meio Magnético no formato AAAAMM\. Ex:201510\.

Tipo: Numérico

Tamanho: 06 caracter

MFS1532

RN51

__Campo Número da Nota:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

Na geração deste campo, deve ser consideradas 10 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 10 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(10 posições\)\.”

\(Ex para esta situação: Nº de NF 123456789012 será gerado 3456789012\)\.

Tipo: Numérico

Tamanho: 10 caracter

MFS1532

RN52

__Campo CNPJ/CPF do Tomador do Serviço:__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 06 da SAFX04\)\.

Tipo: Numérico

Tamanho: 14 caracter

MFS1532

RN53

__Campo Nome do Tomador do Serviço:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tam\.: 100 caracteres

MFS1532

RN54

__Campo Inscrição Municipal do Tomador do Serviço:__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

Se o conteúdo do campo INSC\_MUNICIPAL  possuir mais de 06 posições significativas, deverá gerar a informação  truncando, mas retornar no log a seguinte mensagem: 

“O campo Inscrição Municipal \(INSC\_MUNICIPAL \) ultrapassou o tamanho máximo permitido \(06 posições\)\.”

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

RN55

__Campo Série da Nota:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)

Tipo: Alfanumérico

Tam\.: 03 caracteres

MFS1532

RN56

__Campo Tipo do Recolhimento:__

__3__ = Nota Fiscal Cancelada\. Se campo SITUACAO = “S” da SAFX07;

__2__ = ISS Retido\. Para preencher com “2”, é necessário que pelo menos umas das seguintes opções sejam verdadeira:

                            Verificar o local da prestação do serviço \(deve ser o campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o

                         mesmo não    estiver

                         preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

                        \- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se 

                        estiver preenchido,

            verificar se está preenchido com “2”  e se o local da prestação do serviço = município do módulo selecionado

           \- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na

           nota e utilizando o

          campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo

           selecionado

            \- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido e se o local da prestação do

           serviço = município do módulo selecionado e se o local da prestação do serviço = município\.

__4 __= Imune/Isento \. Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido, verificar se o serviço

                              cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros

                              Classificação de Serviços com o COD\_PARAM = “433”;

__5 __= Suspenso por Decisão Judicial\. Preencher com 5 se pelo menos umas das seguintes opções seja verdadeira:

                    \- se o <a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>campo IND\_ISS da tabela ESTABELECIMENTO = “03”\.

                    \- se o serviço cadastrado na nota está parametrizado na tela Parâmetros – Classificação de Serviços – Município com o

                      cód\_param = 427\.

__6 __= Não Tributável\. Verificar se __o__ campo IND\_ISS da tabela ESTABELECIMENTO = “09”, e se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “444”\.

__7__ = Fator Gerador em Outro Município\. Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento

      estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

__8__ = Simples Nacional\. Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”;

Se caso nenhuma das condições for verdadeira, deverá preencher com __“1”\.__

Tipo: numérico

Tam\.: 01 caracteres

MFS1532

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>RN57

__Campo Valor do Serviço:__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. 

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN58

__Campo Valor do ISS a Recolher:__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN59

__Campo Valor do ISS Retido:__

Preencher com o somatório do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN60

__Campo Data de Emissão da Nota:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Data no formato DDMMAAAA\. Ex\.: __04072003__ \(04 de Julho de 2003\)\.

Tipo: Alfanumérico

Tam\.: 8 caracteres

MFS1532

RN61

__Campo Identificação do Serviço:__

Este campo deverá ser preenchido com __zeros__\. Não será tratado neste segmento\.

Tipo: numérico

Tam\.: 04 caracteres

MFS1532

RN62

__Campo Identificação da Atividade:__

Preencher com a informação do campo “Atividade” da tela Serviço Msaf x Atividade, em Parâmetros para Município, referente ao Código da Atividade cadastrada na nota fiscal\.

Obs\.: Caso o Código da Atividade não seja parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para a Atividade "XXX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização do Serviço Msaf x Atividade\. Efetuar a parametrização no menu Parâmetros > Serviço Msaf x Atividade no módulo "Parâmetros para Município"\.

Tipo: numérico

Tam\.: 03 caracteres

MFS1532

RN63

__Campo Valor da Dedução:__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV

Todos os campos de valores devem ser cadastrados sem formatação, com duas casas decimais\. Ex: 1562,00 = 156200\.

Tipo: Alfanumérico

Tam\.: 18 caracteres

MFS1532

RN64

__Campo Valor da Paga__

Este campo deverá ser preenchido com __zeros__\. Não será tratado neste segmento\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN65

__Campo Número do Processo Judiciário__

Este campo deverá ser preenchido com __espaços__\. Não será tratado neste segmento\.

Tipo: Alfanumérico

Tam\.: 15 caracteres

MFS1532

RN66

__Campo Número do Documento do aluno__

Este campo deverá ser preenchido com __espaços__\. Não será tratado neste segmento\.

Tipo: Alfanumérico

Tam\.: 11 caracteres

MFS1532

RN67

__Campo Nome do aluno__

Este campo deverá ser preenchido com __espaços__\. Não será tratado neste segmento\.

Tipo: Alfanumérico

Tam\.: 11 caracteres

MFS1532

RN68

__Campo Fornecimento de Material:__

Preencher com:

‘__S__’ = Sim, quando o campo VLR\_MAT\_PROP da tabela SAFX07 estiver preenchida\.

 Se não Preencher com:

 ‘__N__’ = Não\.

Tipo: Alfanumérico

Tam\.: 01 caracteres

MFS1532

RN69

__Campo Retenção Efetiva__

Este campo deverá ser preenchido com zeros\. Não será tratado neste segmento\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN70

__Campo ISS Complementar__

Este campo deverá ser preenchido com zeros\. Não será tratado neste segmento\.

Tipo: numérico

Tam\.: 18 caracteres

MFS1532

RN71

__Campo Seqüencial do Registro:__

Numeração seqüencial dos registros para todo o arquivo\.

Numeração seqüencial dos registros para todo o arquivo\. Ex\.: Linha 1 = 000001; Linha 2 = 000002; e assim

sucessivamente\.

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

__Segmento H \- Trailer__

RN72

__Campo Segmento:__

Preencher com o valor fixo __“H”__\.

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS1532

RN73

__Campo Número Identificação do registro no segmento:__

Preencher com o valor fixo “0000”\.

Tipo: Numérico

Tamanho: 04 caracteres

MFS1532

RN74

__Campo  Mês de Competência:__

Preencher com o Mês e Ano informado no campo “Data Inicial” na tela de Geração do Meio Magnético\.

Tipo: Numérico 

Tamanho: 06 caracteres __\(AAAAMM\)__

MFS1532

RN75

__Campo  Quantidade de Registros:__

Preencher com a quantidade de registros\. Contar todas as linhas do arquivo, inclusive a linha do segmento H\.

Tipo: Numérico 

Tamanho: 06 caracteres

MFS1532

RN76

__Campo Seqüencial do Registro__

Numeração seqüencial dos registros para todo o arquivo\. Exemplo: Linha 1 = __000001__; Linha 2 = __000002__; e assim sucessivamente\.

Tipo: numérico

Tam\.: 06 caracteres

MFS1532

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

