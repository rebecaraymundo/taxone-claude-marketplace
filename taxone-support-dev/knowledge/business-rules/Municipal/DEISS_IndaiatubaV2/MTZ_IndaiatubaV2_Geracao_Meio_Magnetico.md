# MTZ_IndaiatubaV2_Geracao_Meio_Magnetico

- **Fonte:** MTZ_IndaiatubaV2_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 113 KB

---

THOMSON REUTERS

Municipal 

 Serviços Prestados e Tomados 

	Geração do Meio Magnético – IndaiatubaV2 \- SP 	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-18414 

João Henrique

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços prestados e tomados em atendimento ao novo validador IndaiatubaV2\.

MFS\-19714

João Henrique

Esse documento tem como finalidade alterar a estrutura de geração do arquivo magnético de serviços prestados e tomados em atendimento ao validador Indaiatuba\-SP\.

MFS26231

Andréa Rocha

Esse documento tem como finalidade alterar a estrutura de geração do arquivo magnético de serviços prestados e tomados em atendimento ao validador Indaiatuba\-SP para a versão 2\.0\.0\.4\.

MFS30645

Alessandra Cristina Navatta

A alteração desta demanda, consiste em atender a versão 2\.0\.0\.3\.2 do leiaute \(do arquivo de __Importação__\)\. 

__Vale ressaltar que a prefeitura desconsiderou a versão liberada anteriormente \(2\.0\.0\.4\) atendida através da MFS26231 e criou esta nova versão \(2\.0\.0\.3\.2\)\.__

MFS34141

Liliane Assaf

Ajuste nas regras dos campos 02, 03, 24, 25 e 26: regras RN09, RN10\_2, RN32, RN33

MFS44961

Andréa Rocha

Alteração da regra do campo Código do País Serviço Realizado e retirar a complementação dos campos com brancos ou zeros\.  Conforme informado pela prefeitura, não deve ser feita esta complementação\.

 MFS534573

Rogério Ohashi

Alteração da regra do campo Código do País Serviço Realizado, quando o código do País é Brasil, o campo não deve ser preenchido, de acordo com o Manual de Layout\.

MFS\-599796

Rosemeire Santos

Este documento tem como objetivo, ajustar as regras __RN25__ e __RN26__, Código do município de incidência e Código do município prestação do serviço\.

MFS608655

Rogério Ohashi

Este documento tem como objetivo, ajustar a regra __RN26__, Código do município prestação do serviço\.\(Voltar a regra anterior\)

MFS616950

Rogério Ohashi

Este documento tem como objetivo, ajustar a regra __RN25__, Código do município de Incidência\. \(Incluir a mesma regra para Serviços Tomados\)

MFS829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Indaiatuba” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“__<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>__O validador de Indaiatuba 2\.0 DEISS é utilizado por empresas que emitem Nota Fiscal Eletrônica de Serviços \(NFS\-e\), a escrituração é realizada automaticamente tanto para o prestador quanto para o tomador do serviço”\.__

__MFS\-18414__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “20509” \(Indaiatuba\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Indaiatuba, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-18414__

__RN03__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menu e sub\-menus no módulo IndaiatubaV2:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda 

__MFS\-18414__

__RN04__

__Regra de criação do nome do arquivo:__

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” __estiver desmarcado__ será gerado o arquivo com a nomenclatura do arquivo normal indicado abaixo\. Devem ser gerados dois arquivos distintos, __no formato TXT __e a cada__ 50 registros atingidos dentro do arquivo o mesmo deverá ser quebrado em vários\.__

Devem ser nomeados da seguinte forma:

__SERVIÇOS TOMADOS:__

__T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA__\___SEQ\.TXT__, onde:

       __T__: Apenas registros de serviços tomados\.

__       SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_1\.TXT

      T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_2\.TXT

__T\_INDAIATUBA\_DDMMAAAA__\___SEQ\.TXT,__ onde:

__T\_ INDAIATUBA__: Representa a obrigação que está sendo gerada, no caso IndaiatubaV2, arquivo de notas de serviços tomados\.

__DDMMAAAA:__ Representa o dia, mês e ano da geração\.

<a id="_Hlk210594326"></a>__SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__\.TXT:__ Representa a extensão do arquivo\.

Exemplo: __T\_INDAIATUBA\_DDMMAAAA\_1\.txt__ 

                __T\_INDAIATUBA\_DDMMAAAA\_2\.txt__

__SERVIÇOS PRESTADOS:__

__P\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA__\___SEQ\.TXT__, onde:

       __P__: Apenas registros de serviços prestados

__       SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: P\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_1\.TXT

      P\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_2\.TXT

__P\_INDAIATUBA\_DDMMAAAA__\___SEQ\.TXT,__ onde:

__P\_ INDAIATUBA__: Representa a obrigação que está sendo gerada, no caso IndaiatubaV2, arquivo de notas de serviços prestados\.

__DDMMAAAA:__ Representa o dia, mês e ano da geração\.

__SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__\.TXT:__ Representa a extensão do arquivo\.

Exemplo: __P\_INDAIATUBA\_DDMMAAAA\_1\.txt__ 

                __P\_INDAIATUBA\_DDMMAAAA\_2\.txt__

Caso o parâmetro “Gerar Arquivos por Data de Emissão” estiver marcado, não será possível marcar o parâmetro “Quebrar Arquivos por Data de Emissão” e deverá ser realizada a seguinte verificação: 

Este arquivo deverá conter todas as notas fiscais com data de emissão dentro do período de referência\.

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, __não será possível marcar__ o parâmetro “Gerar Arquivos por Data de Emissão” e deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser:

__SERVIÇOS TOMADOS:__

__T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA__\___SEQ\_ MMAAAA\.TXT__, onde:

       __T__: Apenas registros de serviços tomados\.

__       SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__DDMMAAAA__: representa a data inicial da geração\.   

__MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_1\_012010\.TXT

      T\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_2\_012010\.TXT

__T\_INDAIATUBA\_DDMMAAAA__\___SEQ\_MMAAAA\.TXT,__ onde:

__T\_ INDAIATUBA__: Representa a obrigação que está sendo gerada, no caso <a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK33"></a>I<a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK30"></a>ndaiatubaV2, arquivo de notas de serviços tomados\.

__DDMMAAAA:__ Representa o dia, mês e ano da geração\.

__SEQ:__ Deverá gerar uma sequencial para cada arquivo com __50 registros__\. 

__MMAAAA: __Representa o mês da competência referente à nota gerada\.

__\.TXT:__ Representa a extensão do arquivo\.

Exemplo: __T\_INDAIATUBA\_DDMMAAAA\_1\_MMAAAA\.txt__ 

                __T\_INDAIATUBA\_DDMMAAAA\_2\_MMAAAA\.txt__

__*Observação:*__ Neste caso o arquivo normal também deverá ser gerado tanto para serviços prestados quanto tomados, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS\-18414__

__MFS\-829438     __

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido Desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido Desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)

__Gerar Arquivos por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>__Regime de Lucro Presumido ou Real:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-18414__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

1. O leiaute deverá ser apresentado em dois arquivos no formato __texto \- TXT__, padrão de codificação UTF\-8 \(sem BOM\), contendo apenas caracteres da tabela ASCII, __com no máximo 50 \(cinquenta\) registros por arquivo__\. Um arquivo deverá conter as informações sobre os __serviços prestados__, e o outro arquivo sobre os __serviços tomados__\. 
2. Todos os registros devem conter no final de cada linha do arquivo digital, os caracteres “CR” \(Carriage Return\) e “LF” \(Line Feed\) correspondentes a “retorno do carro” e “salto de linha”\.
3. Não deveremos considerar as Notas Fiscais Eletrônicas emitidas por prestadores do Município de Indaiatuba\.
4. A linha do arquivo digital deve conter os campos na exata ordem em que estão listados no leiaute\. Entre os campos deve ser inserido o delimitador “|” \(pipe\)\. O caractere delimitador “|” não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos ou alfanuméricos\. O caractere “|” não deve ser usado como delimitador de início e de fim da linha\. Todos os caracteres de formatação \(máscaras\) devem ser removidos\. 

Exemplo \(campos da linha\): 

11111111111111|2222222|3|20180319|201803|802|1500,00|0,00|1||3520509|3520509 

Exemplo \(conteúdo do campo\): 

• Campo alfanumérico: Eloá da Silva Ltda\. → |Eloá da Silva Ltda\.| 

• Campo numérico: 1234,56 → |1234,56|

1. Os __campos numéricos__ deverão ser preenchidos sem os separadores de milhar, sinais ou quaisquer outros caracteres como: “\.”, “\-”, “%”, devendo a vírgula ser utilizada como separador decimal\.
2. Os __campos decimais__ deverão ser preenchidos conforme instrução da quantidade de casas decimais precedidos por vírgula\.
3. Os __campos percentuais__ deverão ser preenchidos desprezando\-se o símbolo \(%\), sem nenhuma convenção matemática\.

      __\[MFS44961\]__ retirar a complementação dos campos com zeros ou espaços em branco

__Observações:__ 

Os campos numéricos obrigatórios que não estiverem com informação serão preenchidos com zeros ou à esquerda até completar seu tamanho máximo\. 

Os campos do tipo texto \(alfanumérico\) serão preenchidos com espaço em branco, se não houver informação de preenchimento\. 

__Exemplos dos campos numéricos de valores monetários:__

Exemplo \(valores monetários, quantidades, percentuais, etc\.\): 

• $ 1\.129\.998,99 → |1129998,99| 

• 1\.255,42 → |1255,42| 

• 234,567 → |234,567| 

• 10\.000,00 → |10000,00| 

• 17,00 % → |17,00| 

• 30 → |30|

__MFS\-18414__

__RN07__

__Regras para a Geração do Arquivo de Serviços Prestados:__

Esses registros apenas devem ser gerados no arquivo quando o campo __“Gerar serviços prestados”__ estiver marcado e deve conter todas as notas com as seguintes características:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal dentro do período de referência __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência
- Não deve recuperar notas fiscais sem itens\.
- O agrupamento das notas fiscais deverá ser realizado pelos campos: Código de Serviço, Alíquota e ISS retido;
- Para considerar notas fiscais eletrônicas verificar: 
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__MFS\-18414__

__RN08__

__Regras para a Geração do Arquivo de Serviços Tomados:__

Esses registros apenas devem ser gerados no arquivo quando o campo __“Gerar serviços tomados”__ estiver marcado e deve conter todas as notas com as seguintes características:

- Notas fiscais de Entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal dentro do período de referência __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência
- Não deve recuperar notas fiscais sem itens\.
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- O agrupamento das notas fiscais deverá ser realizado pelos campos: Código de Serviço, Alíquota e ISS retido;
- Para considerar notas fiscais eletrônicas verificar: 
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__RN08\_2__

__Regra para o campo Número da Linha\.__

Nesse campo será informado um contador de linhas geradas no arquivo\.

Exemplos: “01”, “20”, “50”\.

Obrigatório

Formato: 99 

Tamanho: 2 posições

Tipo: Numérico

__MFS\-19714__

__RN09__

__Regra para o campo CPF ou CNPJ do Prestador/Tomador__

Nesse campo será informado o CPF ou CNPJ do Prestador do Serviço\. 

__\[MFS34141\]: Esta MFS veio corrigir a regra que estava invertida\.__

__Serviços Tomados:__ Preencher com a informação do campo __CGC__ da tabela __ESTABELECIMENTO\.__

__Serviços Prestados: __Preencher com a informação do campo __CPF\_CGC__ da tabela __X04\_PESSOA\_FIS\_JUR __\(campo 06 da SAFX04\)\.

__Serviços Tomados:__ Preencher com a informação do campo __CPF\_CGC__ da tabela __X04\_PESSOA\_FIS\_JUR __\(campo 06 da SAFX04\)\.

__Serviços Prestados: __Preencher com a informação do campo __CGC__ da tabela __ESTABELECIMENTO\.__\.\.

__Tratamentos:__

- Se o Prestador/Tomador do exterior, UF = EX, preencher esse campo com “99999999999999”\.

Obrigatório\. 

Formato: 99999999999999 

Tamanho: 14 posições

Tipo: Numérico

__MFS\-18414__

__MFS\-19714__

__MFS26231__

__MFS30645__

__MFS34141__

__RN10__

__\[EXCLUÍDO \- MFS30645\] Regra para o campo CCM \(Inscrição Municipal\) do Tomador__

Nesse campo será informado a Inscrição Municipal do Tomador\.

__Serviços Tomados:__ Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __ESTABELECIMENTO\.__

__Serviços Prestados: __Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

__Tratamento:__

Se o contribuinte for estabelecido no município de Indaiatuba, o preenchimento do campo será obrigatório\. Caso não seja informado valor, o sistema deverá exibir uma mensagem de erro no log*: “Tomador estabelecido em Indaiatuba, favor verificar o preenchimento do campo”\.*

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-18414__

__MFS\-19714__

__MFS26231__

__MFS30645__

__RN10\_2__

__Regra para o campo Nome ou Razão Social do Prestador__

Nesse campo será informado a Razão Social do Prestador de Serviços\. 

__\[MFS34141\]: Esta MFS veio corrigir a regra que estava invertida\.__

__Serviços Tomados:__ Preencher com o campo __RAZAO\_SOCIAL __da tabela__ ESTABELECIMENTO__

__Serviços Prestados:__ Preencher com o campo __RAZAO\_SOCIAL __da tabela__ X04\_PESSOA\_FIS\_JUR __\(campo 05 da SAFX04\)

__Serviços Tomados:__  Preencher com o campo __RAZAO\_SOCIAL __da tabela__ X04\_PESSOA\_FIS\_JUR __\(campo 05 da SAFX04\)\. 

__Serviços Prestados:__ Preencher com o campo __RAZAO\_SOCIAL __da tabela__ ESTABELECIMENTO\.__

Obrigatório

Formato: XXXXXXXXXXXXX…/ 

Tamanho: 100 posições

Tipo: Caractere

__MFS\-19714__

__MFS26231__

__MFS30645__

__MFS34141__

__RN11__

__Regra para o campo Tipo de Escrituração __

Nesse campo será informado o tipo da escrituração\. Preencher com:

__‘P’__ \- NF de serviço de Serviço Prestado quando o campo __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __= ‘9’__

__‘T’__ \- NF de serviço de Serviço Tomado quando o campo __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __<> ‘9’__

Obrigatório

Formato: X 

Tamanho: 1 posição

Tipo: Caractere 

__MFS\-18414__

__RN12__

__Regra para o campo Competência __

Nesse campo será informado o mês e ano de competência do arquivo gerado\. Preencher com o mês e o ano informado na data inicial da tela de geração do arquivo meio magnético\.

Obrigatório

Formato: AAAAMM \(ano/ mês\)

Tamanho: 6 posições

Tipo: Numérico

__MFS\-18414__

__MFS\-19714__

__RN13__

__Regra para o campo Dia Data da Emissão da Nota__

Nesse campo será informado o Dia a Data de Emissão da Nota\. Preencher com o __DIA__ \(anoMêsDia\) informado no campo __DATA\_EMISSAO__ da tabela __DWT\_DOCTO\_FISCAL\.__

Obrigatório\.

Formato: DD aaaaMMdd

Tamanho: 2 8 posições

Tipo: Numérico

__MFS\-18414__

__MFS\-19714__

__RN14__

__Regra para o campo Código do Serviço Tomado__

Nesse campo será informado o <a id="OLE_LINK39"></a><a id="OLE_LINK40"></a>Código de Serviço Tomado conforme lista de serviços sujeitos ao ISSQN\. Preencher com o conteúdo do campo __COD\_SERV\_LEI\_116__ da tabela __DWT\_SERVICO\_LEI\_116__ referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0000 \(zeros\) e emitida a mensagem de log: “*O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar”\.*

Obrigatório\.

Formato: 9999

Tamanho: 4 posições

Tipo: Numérico

__MFS\-18414__

__RN15__

__Regra para o campo Alíquota\.__

Nesse campo será informado a Alíquota de Imposto do documento fiscal\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Se o campo Alíquota estiver sem preenchimento, exibir uma mensagem de log: *“O campo Alíquota não está preenchido, favor verificar”\.*

Exemplos: 

2,5000% → 2,5000; 

2,0341% → 2,0341; 

10,4564% → 10,4564;

2,5000000000% → 2,5000000000; 

2,0341000002% → 2,0341000002; 

4,0000000000% → 4,0000000000\. 

  

Obrigatório\.

Formato: 9999,9999999999

Tamanho: 6,4 posições \[MFS30645 Alteração\] Tamanho: 14,10

Tipo: Numérico

__MFS\-18414__

__MFS\-30645__

__RN16__

__Regra para o campo Número da Nota Fiscal Inicial__

Nesse campo será informado o número Inicial da Nota Fiscal\. Preencher com a informação do campo __NUM\_DOC\_FIS__ da __DWT\_DOCTO\_FISCAL\.__

Obrigatório\.

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-18414__

__RN17__

__Regra para o campo Número da Nota Fiscal Final__

Nesse campo será informado o número Final da Nota Fiscal\. Preencher com a informação do campo __NUM\_DOC\_FIS__ da __DWT\_DOCTO\_FISCAL\.__

Obrigatório\.

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-18414__

__RN18__

__Regra para o campo Número da Nota Fiscal Substituída __

Esse campo não será tratado por enquanto, preencher com zeros\. No site da prefeitura e/ou manual não possui informações sobre o número da Nota Fiscal Substituída\.

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-18414__

__RN19__

__Regra para o campo Série da Nota Fiscal__

Nesse campo será informado o número Final da Nota Fiscal\. Preencher com a informação do campo __SERIE\_DOCFIS __da __DWT\_DOCTO\_FISCAL\.__

Obrigatório\.

Formato: XXXXX

Tamanho: 5 posições

Tipo: Caractere 

__MFS\-18414__

__RN20__

__Regra para o campo Valor da Nota Fiscal__

Nesse campo será informado o Valor da Nota Fiscal\. Preencher com a informação do campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\. __

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as três primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘456789123456,45’\.

- <a id="OLE_LINK36"></a><a id="OLE_LINK37"></a><a id="OLE_LINK38"></a>Se o campo Valor da Nota Fiscal estiver com o tamanho acima do máximo permitido \(14,2 posições\) ou sem preenchimento, exibir uma mensagem no log: *“O campo Valor da Nota Fiscal está com o tamanho acima do permitido ou não está preenchido, favor verificar”\.*

Obrigatório\.

Formato: 999999999999,99

Tamanho: 14,2 posições

Tipo: Numérico

__MFS\-18414__

__RN21__

__Regra para o campo Valor do Desconto de Materiais __

Nesse campo será informado o Valor do desconto de materiais, conforme a Instrução Normativa Nº\. 01/2013 e Decreto Municipal Nº\. 13\.185/2017\. Preencher com a informação do campo__ VLR\_DESCONTO __da __DWT\_ITENS\_SERV\.__

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as três primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘456789123456,45’\.

- Se o campo Valor do Desconto de Materiais estiver com o tamanho acima do máximo permitido \(14,2 posições\) exibir uma mensagem no log: *“O campo Valor do Desconto de Materiais está com o tamanho acima do permitido, favor verificar”\.*

Formato: 999999999999,99

Tamanho: 14,2 posições

Tipo: Numérico

__MFS\-18414__

__RN22__

__Regra para o campo Valor do Imposto__

Esse campo será apresentado com o Valor do ISS dos documentos fiscais\. Preencher com o somatório do campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as três primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘456789123456,45’\.

- Se o campo Valor do Imposto estiver com o tamanho acima do máximo permitido \(14,2 posições\) ou sem preenchimento, exibir uma mensagem no log: *“O campo Valor do Imposto está com o tamanho acima do permitido ou não está preenchido, favor verificar”\.*

Obrigatório\.

Formato: 999999999999,99

Tamanho: 14,2 posições

Tipo: Numérico

__MFS\-18414__

__RN23__

__Regra para o campo Exigibilidade do ISS__

Nesse campo será informado a opção de exigibilidade do ISS\. 

__Serviços Prestados:__

Preencher com:

__“3” \- Isenção\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“5” \- Imunidade\.__

- Se o IND\_ISS da tabela ESTABELECIMENTO = “01”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__“6” \- Exigibilidade Suspensa por Decisão Judicial\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427” no módulo: Parâmetros para Município\.

__“7” \- Exigibilidade Suspensa por Processo Administrativo\.__

- Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485” no módulo: Parâmetros para Município\.

__“2” \- Não Incidência\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “06”; __OU__
- Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432” no módulo: Parâmetros para Município\.

__“4” \- Exportação\.__

- Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520” no módulo: Parâmetros para Município\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“1” \- Exigível\.__

__Serviços Tomados:__

Preencher com:

__“3” \- Isenção\.__

- Se o campo <a id="OLE_LINK34"></a><a id="OLE_LINK35"></a>IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“5” \- Imunidade\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “07”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__“6” \- Exigibilidade Suspensa por Decisão Judicial\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “09”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427” no módulo: Parâmetros para Município\.

__“7” \- Exigibilidade Suspensa por Processo Administrativo\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “11”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485” no módulo: Parâmetros para Município\.

__“2” \- Não Incidência\.__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432” no módulo: Parâmetros para Município\.

__“4” \- Exportação\.__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520” no módulo: Parâmetros para Município\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“1” \- Exigível\.__

Obrigatório\.

Formato: X

Tamanho: 1 posição

Tipo: Caractere 

__MFS\-18414__

__RN24__

__Regra para o campo Número do Processo __

Nesse campo será informado o Número do Processo quando a exigibilidade do Prestador/Tomador é Suspensa por __Decisão Judicial__ ou Suspensa por__ Processo Administrativo\.__ Preencher com o campo __NUM\_PROC\_JUR__ da tabela __DWT\_DOCTO\_FISCAL__ quando o __IND\_TIPO\_PROC__ da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido e se o campo__ Exigibilidade do ISS__ for igual a ‘6‘ ou ‘7’ \(RN23\)\.

__Tratamento: __

- Se o campo__ Exigibilidade do ISS__ for igual a 6 ou 7 e o campo NUM\_PROC\_JUR da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, emitir a mensagem de log: *“A exigibilidade da nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>> é por Suspensão e necessita do preenchimento do Número do Processo”\.*

Formato: 999999999999\.\.\./

Tamanho: 30 posições

Tipo: Caractere

__MFS\-18414__

__RN25__

__Regra para o campo Código do Município Incidência  __

Nesse campo será informado o código do município de incidência do imposto conforme a tabela do IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

__\[ALTERAÇÃO\-MFS599796\-MFS616950\] Serviços Prestados e Serviços Tomados__

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\), referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__ 

- Se o campo Código do Município Indecência não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Obrigatório

Formato: 9999999

Tipo: Numérico

Tamanho: 7

__MFS\-18414__

__MFS\-599796__

__MFS616950__

__RN26__

__Regra para o campo Código do Município Serviço Realizado__

__\[ALTERAÇÃO\-MFS608655\] __

Nesse campo será informado o código do município onde o serviço foi realizado conforme a tabela do IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\), referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

__\[ALTERAÇÃO\-MFS599796\] Serviços Prestados__

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

<a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>__Tratamento:__

- *Se o município de local de prestação de serviço não estiver preenchido, deverá ser gravado com 0000000 \(zeros\) e emitida a mensagem de log: “O Código do município não será considerado porque o local de prestação não foi preenchido na NF\. Campo de preenchimento obrigatório, favor verificar”;*
- Se UF = EX, no caso de exterior, no sistema deverá ser informado fixo “9999999”\. 

Obrigatório\.

Formato: 9999999

Tipo: Numérico

Tamanho: 7

__MFS\-18414__

__MFS\-599796__

__MFS608655__

__RN27__

__Regra para o campo __<a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>__Código do País Serviço Realizado__

Identifica o Código do País \(BACEN\) de onde o serviço foi realizado\. Preencher com a concatenação do campo COD\_PAIS \+ DIG\_VERIFICADOR da tabela PAIS, referente ao campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR \(campo 21 da SAFX04\)\.

__\[MFS44961/MFS534573\] __conforme a definição do layout, este campo só deve ser preenchido se o código do município de realização do serviço for igual a 9999999\.

__Tratamento__:

- O campo Código do País__ __somente deve ser preenchido se o Código do Município Serviço Realizado estiver preenchido com “9999999” \(RN26\)\. Caso seja um município do Brasil, país de Código BACEN = ‘1058’, o campo __não__ deve ser preenchido, conforme orientação do Manual Layout\.  o campo deve ser preenchido com 0000 \(zeros\)\. 

Formato: 9999

Tipo: Numérico

Tamanho: 4

__MFS\-18414__

__MFS\-44961__

__MFS\-534573__

__RN28__

__Regra para o campo Prestador Optante pelo Simples Nacional __

Identifica se o Prestador é optante do Simples Nacional\. 

__Serviços Prestados__

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”\.

Senão, preencher com:

__“2” \- Não\.__

__Serviços Tomados__

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) = “S” referente ao prestador cadastrado na nota fiscal\.

Senão, preencher com:

__“2” \- Não\.__

Obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS\-18414__

__RN29__

__Regra para o campo ISS Retido__

Nesse campo será registrado se o ISS será retido ou não pelo município\.

__Serviços Prestados__

__Preencher com “1”__ \(retido\), quando pelo menos uma das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. 

Caso nenhuma das opões seja verdadeira, __preencher com__ __“2” __\(não retido\)__\. __

__Serviços Tomados__

__Preencher com “1”__ \(retido\), quando pelo menos uma das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. 

Caso nenhuma das opões seja verdadeira, __preencher com__ __“2”__ \(não retido\)__\. __

Obrigatório\.

Formato: X

Tamanho: 1 posição

Tipo: Caractere

__MFS\-18414__

__RN30__

__Regra para o campo Situação da Nota Fiscal__

Nesse campo será preenchido a situação da Nota Fiscal\.

Preencher com:

__“C” – Cancelada\. __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = S

__“S” – Substituída\. __

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>Se o código do serviço da nota fiscal estiver parametrizado em: \(Básicos > Mastersaf DW > Manutenção > Códigos > Alíquota de Serviço\) e o campo “Serviço p/Substituído” estiver marcado\.

__“U” – Substituta\.__

Se o código do serviço da nota fiscal estiver parametrizado em: \(Básicos > Mastersaf DW > Manutenção > Códigos > Alíquota de Serviço\) e o <a id="OLE_LINK13"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a>campo “Serviços p/ Substituto Tributário” estiver marcado\.

__“N”__ __– Normal\.__ 

Se nenhuma das opções acima forem verdadeiras\.

Obrigatório

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS\-18414__

__RN31__

__Regra para o campo Regime Especial de Tributação__

Nesse campo será informado o indicador do regime especial de tributação\.

__Serviços Prestados__

Preencher com:

__“1” \- Microempresa municipal\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “11”\.

__“2” \- Estimativa\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “02” referente o prestador cadastrado na nota fiscal; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421” no módulo: Parâmetros para Município\.

__“3” \- Sociedade de Profissionais\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “08”\.

__“4” \- Cooperativa\.__

- Se o campo NAT\_PESSOA\_JUR da tabela ESTABELECIMENTO = “01”\.

__“5” \- Microempresário Individual \(MEI\)\.__

- Não será tratado\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

- Não será tratado\.

__Tratamentos:__

- O campo é de preenchimento obrigatório somente para contribuintes não optantes pelo regime de lucro presumido ou lucro real, então se o usuário marcar a opção Regime de Lucro Presumido ou Real na tela de geração do arquivo magnético e não houver essa informação para o prestador/tomador relacionado não haverá mensagem de log, caso contrário, se o usuário NÃO marcar essa opção e a informação não for preenchida para o prestador/tomador, deverá ser gerado com 0 \(zero\) e emitida a mensagem de log: *“Contribuinte não optante pelo regime de lucro presumido ou lucro real precisa informar Regime Especial de Tributação, favor verificar ISS /Natureza da PJ cadastrada no Estabelecimento”\.*

__Serviços Tomados__

Preencher com:

__“1” \- Microempresa municipal\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “04 – Microempresa \(ME\) ” referente o prestador cadastrado na nota fiscal\.

__“2” \- Estimativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “08 \- Regime de Estimativa” referente o prestador cadastrado na nota fiscal\.

__“3” \- Sociedade de Profissionais\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “06 \- Sociedade Profissional” referente o prestador cadastrado na nota fiscal\.

__“4” \- Cooperativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “02 \- Cooperativa” __OU__ “05 \- Cooperativa de Transporte” referente o prestador cadastrado na nota fiscal\.

__“5” \- Microempresário Individual \(MEI\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “05 – MEI \(Microempreendedor Individual\) ” referente o prestador cadastrado na nota fiscal\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “01 \- EPP \(Empresa de Pequeno Porte\) ” referente o prestador cadastrado na nota fiscal\.

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a>__Tratamentos:__

- O campo é de preenchimento obrigatório somente para contribuintes não optantes pelo regime de lucro presumido ou lucro real, então se o usuário marcar a opção Regime de Lucro Presumido ou Real na tela de geração do arquivo magnético e não houver essa informação para o prestador/tomador relacionado não haverá mensagem de log, caso contrário, se o usuário NÃO marcar essa opção e a informação não for preenchida para o prestador/tomador, deverá ser gerado com 0 \(zero\) e emitida a mensagem de log: *“Contribuinte não optante pelo regime de lucro presumido ou lucro real precisa informar Regime Especial de Tributação, favor verificar Classe da Pessoa Física/Jurídica <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS\-18414__

__RN32__

__Regra para o campo CPF ou CNPJ do Tomador/Prestador__

Nesse campo será informado o <a id="OLE_LINK25"></a>CPF ou CNPJ do Tomador do Serviço\. 

__\[MFS34141\]: Esta MFS veio corrigir a regra que estava invertida\.__

__Serviços Tomados:__ Preencher com a informação do campo __CPF\_CGC__ da tabela de __X04\_PESSOA\_FIS\_JUR__\.

__Serviços Prestados:__ Preencher com a informação do campo __CGC__ da tabela de __ESTABELECIMENTO\.__

__Serviços Tomados:__  Preencher com a informação do campo __CGC__ da tabela de __ESTABELECIMENTO\.__

__Serviços Prestados:__ Preencher com a informação do campo __CPF\_CGC__ da tabela de __X04\_PESSOA\_FIS\_JUR__\.

__Tratamentos:__

- Se o Prestador/Tomador do exterior, UF = EX, preencher esse campo com “99999999999999”\.
- <a id="OLE_LINK28"></a><a id="OLE_LINK29"></a>Se Prestador /Tomador for uma Pessoa Física, CPF\_CGC = 11 posições __E__ se encaixar a Regime Especial de Tributação \(verificar __RN31__\) esse campo deverá ser preenchido com “99999999999” \(nota de consumidor não será tratado no momento\)\.

Obrigatório\. 

Formato: 99999999999999 

Tamanho: 14 posições

Tipo: Numérico

__MFS\-18414__

__MFS\-19714__

__MFS26231__

__MFS30645__

__MFS34141__

__RN32\.a__

__Regra para o campo CCM \(Inscrição Municipal\) do Tomador__

Nesse campo será informado a Inscrição Municipal do Tomador\.

__Serviços Tomados:__ Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __ESTABELECIMENTO\.__

__Serviços Prestados: __Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

__Tratamento:__

Se o contribuinte for estabelecido no município de Indaiatuba, o preenchimento do campo será obrigatório\. Caso não seja informado valor, o sistema deverá exibir uma mensagem de erro no log*: “Tomador estabelecido em Indaiatuba, favor verificar o preenchimento do campo”\.*

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-19714__

__MFS26231__

__MFS30645__

__RN33__

__Regra para o campo Nome ou Razão Social do Tomador__

Nesse campo será informado a __Razão Social do Tomador__\. 

__\[MFS34141\]: Esta MFS veio corrigir a regra que estava invertida\.__

__Serviços Tomados__: Preencher com o campo __RAZAO\_SOCIAL __da tabela__ X04\_PESSOA\_FIS\_JUR __\(campo 05 da SAFX04\)\.

__Serviços Prestados:__ Preencher com o campo __RAZAO\_SOCIAL __da tabela__ ESTABELECIMENTO__

__Serviços Tomados__:   Preencher com o campo __RAZAO\_SOCIAL __da tabela__ ESTABELECIMENTO\. __

__Serviços Prestados:__ Preencher com o campo __RAZAO\_SOCIAL __da tabela__ X04\_PESSOA\_FIS\_JUR __\(campo 05 da SAFX04\)\.

Formato: XXXXXXXXXXXXX…/ 

Tamanho: 100 posições

Tipo: Caractere

__MFS\-18414__

__MFS\-19714__

__MFS26231__

__MFS30645__

__MFS34141__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

