# MTZ_DMISS_Geracao_do_Meio_Magnetico_Caucaia

- **Fonte:** MTZ_DMISS_Geracao_do_Meio_Magnetico_Caucaia.docx
- **Modificado:** 2025-12-04
- **Tamanho:** 94 KB

---

THOMSON REUTERS

Municipal

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4626

Geração do Meio Magnético DMISS \- Caucaia

Deverá ser criado um novo módulo que permita a geração do meio magnético DMISS Caucaia em que serão informados os documentos fiscais de serviços tomados e prestados\. 

OS4770

Geração do Meio Magnético DMISS \- Caucaia

A Prefeitura Municipal de Caucaia/CE disponibilizou uma nova versão do Layout DMISS\.  Por causa desse novo documento, algumas regras foram alteradas e outras regras incluídas para atender as exigências do município\.

MFS2071

DW \- MUNICIPAL \- DMISS – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH20426\_2016

Geração do Meio Magnético DMISS \- Caucaia

Este documento tem como objetivo alterar o formato de preenchimento do campo Competência do Registro Tipo H\.

CH20424\_2016

Geração do Meio Magnético DMISS \- Caucaia

Este documento tem como objetivo alterar o preenchimento do Campo Código do Serviço dos Registros Tipo E e Tipo R\.

MFS7153

Geração do Meio Magnético DMISS – 

Caucaia 

Este documento tem como objetivo alterar o preenchimento do Campo Código do Serviço dos Registros Tipo E e Tipo R\.

__MFS\-923053__

Rafael Fabiano

Este documento tem como objetivo a inclusão do município de Caucaia/CE no validador __DMISS CAUCAIA__\.

	

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Caucaia” deve ficar localizado no grupo “Municipal”\.

OS4626

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “03709” \(Caucaia\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Caucaia, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS4626

RN03

__Estrutura de menus do módulo Caucaia:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Caucaia:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

OS4626

__RN04__

__Regra de criação do nome do arquivo__

O arquivo tem o formato texto \(Text Encoding = ISO\-8859\-1\), devendo ser gerado com o nome composto das seguintes informações: 

__Serviços Prestados:__

__      SP\_DMISS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SP\_DMISS__: <a id="OLE_LINK24"></a><a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="OLE_LINK27"></a>representa a obrigação que está sendo gerada\. Apenas registros de serviços prestados\.

       __\.TXT__: extensão do arquivo\.

Ex: SP\_DMISS\_CAUCAIA\_01012010\.TXT

__Serviços Tomados:__

__ST\_DMISS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __ST\_DMISS__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

       __\.TXT__: extensão do arquivo\.

Ex: ST\_DMISS\_CAUCAIA\_01012010\.TXT

__\[ALTERADA OS4770\]__

Para a criação do arquivo, será levado em conta, Inscrição Municipal do contribuinte e a competência da qual se quer importar os dados\. O nome do arquivo deve ser composto das seguintes Informações, Inscrição Municipal \+ Competência e extensão “ISS__”\.__

<a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Serviços Prestados:__

<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>__0000000\_SP0000019__<a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>__012010\.ISS __

__Onde:__

__0000000: __Representa o número do processo da geração\.

<a id="OLE_LINK28"></a><a id="OLE_LINK29"></a><a id="OLE_LINK30"></a>__SP: __Representa a obrigação que está sendo gerada\. Apenas registros de serviços prestados\.

__0000019:__ Inscrição municipal do Contribuinte \(numérico sem ponto e sem hífen\)\. Recuperar o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\. 

__012010:__ Data da competência da DMISS\. Preencher com mês e ano ano do campo Data Inicial da tela de geração do meio magnético\.

__ISS: __Extensão do arquivo\.

__Serviços Tomados:__

__0000000\_ST0000019012010\.ISS __

__Onde:__

__0000000: __Representa o número do processo da geração\.

__ST: __Representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__0000019:__ Inscrição municipal do Contribuinte \(numérico sem ponto e sem hífen\)\. Recuperar o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\. 

__012010:__ Data da competência da DMISS\. Preencher com mês e ano ano do campo Data Inicial da tela de geração do meio magnético\.

__ISS: __Extensão do arquivo\.

OS4626

OS4770

__MFS\-923053__

__RN05__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final: __deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Gerar Serviços Prestados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Caucaia, que estejam licenciados e que o usuário possua acesso no PowerLock\.

<a id="OLE_LINK35"></a><a id="OLE_LINK36"></a><a id="OLE_LINK37"></a>OS4626

MFS\_2071

__MFS\-923053__

RN06

__Regras Gerais de formatação do arquivo__

O arquivo a ser gerado para importação dever ser no formato texto, e conter os seguintes tipos de registros:

      \* Registro tipo "H" \- Identificação \(Header\)

      \* Registro tipo "E" \- Notas Emitidas

      \* Registro tipo "R" \- Notas Recebidas

Observações:

1. O primeiro registro dever ser, obrigatoriamente, um registro do tipo "H"\.
2. Todos os registros deverão ser finalizados com a quebra de linha\.
3. Os registros tipo E e R devem ser agrupados pelos campos Natureza da Operação e Alíquota de ISSQN\.
4. Campos numéricos como Inscrição Municipal, CNPJ, valor da nota fiscal, devem ser preenchidos com zeros à esquerda até atingir o tamanho exato do campo\. Quando o campo for opcional, ou seja, o conteúdo do campo não for fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\. 
5. Serão utilizadas 02 posições para a parte decimal\. Exemplo:

O campo com tamanho 15 significa: 13 posições para a parte inteira e 02 posições para a parte decimal\.

Para um valor de R$ 2\.500,__00__ no arquivo deverá estar gravado assim: 0000000002500__00__

1. Os valores numéricos serão truncados, quando a informação preenchida no banco de dados, for maior do que o tamanho máximo exigido pelo layout\. 
2. O campo Alíquota será do tipo numérico, com 4 posições, sendo que duas casas representam as decimais\. Valor sem separador de decimais, sem ponto ou virgula \(, ou\.\) no formato “0000”\. O valor da alíquota será truncado, caso o valor informado no banco possuir mais do que 4 posições\.
3. Todos os campos alfanuméricos deverão ser preenchidos alinhados pela esquerda, se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo\.
4. Para adequação da DMISS ao sistema NFS\-e foram feitas as seguintes mudanças:

__           __ \* O registro do tipo "T" não será mais utilizado a partir de 01/01/2013;

             \* As informações que compõe o registro "T" serão incluídas no final do registro "E" e "R";

OS4626

OS4770

RN07

__Regra do Registro Tipo H – Identificação__

Primeiro registro do arquivo\. Deve existir apenas um registro tipo "H" por arquivo\.

Esse registro deve conter informações referentes ao estabelecimento do contribuinte escolhido na tela de geração do meio magnético\. 

OS4626

<a id="_Hlk417299356"></a>RN08

__Regra do Registro Tipo H \- Campo Tipo do Registro:__

Preencher com o texto fixo __“H”, __indicando a linha do registo\.

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4626

RN09

__Regra do Registro Tipo H \- Campo Versão do Arquivo:__

Indica a versão do layout a ser utilizada\. Deve ser preenchido com o número da versão atual\. 

Preencher com o texto fixo __“001”, __indicando a versão atual do registro\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4770

RN10

__Regra do Registro Tipo H – Campo CNPJ:__

Preencher com campo CGC da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tam\.: 14 caracteres

OS4626

<a id="_Hlk417299600"></a>RN11

__Regra do Registro Tipo H \- Inscrição do Contribuinte:__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Numérico 

Tamanho: 07 caracteres

OS4626

RN12

__Regra do Registro Tipo H \- Competência:__

__\[ALTERADA – CH20426\_2016\]__

<a id="OLE_LINK42"></a><a id="OLE_LINK43"></a>Preencher com o mês e o ano informados no campo Data Inicial da tela de geração do Meio Magnético\. 

Preencher no formato __MMAAAA__ __AAAAMM__\.

Tipo: Alfanumérico 

Tamanho: 06 caracteres

OS4770

CH20426\_2016

RN13

__Regra do Registro Tipo E – Notas Fiscais Emitidas__

Registro de detalhes para notas fiscais emitidas\. Sem limites de ocorrências\.

OS4626

RN14

__Regra geral p/ Registro de Serviços Prestados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.

OS4626

RN15

__Regra do Registro Tipo E \- Campo Tipo do Registro:__

Preencher com o texto fixo __“E”, __indicando a linha do registro\.

Tipo: Alfanumérico

Tamanho: 01 caractere

OS4626

RN16

__Regra do Registro Tipo E \- Campo Data de Emissão:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data no formato __99/99/9999__

Tamanho: 10 caracteres

OS4626

RN17

__Regra do Registro Tipo E \- Campo Modelo:__

Preencher com a informação do campo “Modelo DMISS” da tela Modelo Msaf x modulo, em Parâmetros para Município, referente ao modelo cadastrado na nota fiscal\.

Obs\.: Caso o modelo não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para o Modelo de Documento "XX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização de Modelo Msaf x Modelo\. Efetuar a parametrização no menu Parâmetros > Modelo Msaf x Modelo no módulo "Parâmetros para Município"\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4626

RN18

__Regra do Registro Tipo E \- Campo Natureza da Operação:__

__\[__<a id="OLE_LINK67"></a><a id="OLE_LINK68"></a><a id="OLE_LINK69"></a>__ALTERADA OS4770\]__

Preencher com: 

<a id="OLE_LINK56"></a><a id="OLE_LINK57"></a><a id="OLE_LINK58"></a>__      11 – Isento:__ verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido,

      verificar se o serviço cadastrado na nota e o município cadastrado no Estabelecimento estão parametrizados na tela Parâmetros

      Classificação de Serviços com o COD\_PARAM = “433”;

__      12 – ISS Devido pelo prestador:__ Verificar se__ __o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. __ __

      __02 – Com Dedução: __<a id="OLE_LINK59"></a><a id="OLE_LINK60"></a><a id="OLE_LINK61"></a><a id="OLE_LINK62"></a>Verificar se__ __o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. __ __

      __03 – Não Incidência:__ Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem

      parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”;

      __04 – Imune:__ Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”\. Se não estiver preenchido, verificar se

      o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros \- 

      Classificação de Serviços com o COD\_PARAM = “420”__;__

      __05 – Construção Civil:__ Quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço

      cadastrado na nota\.

      __06 – Regime de Estimativa: __verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido

      verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por

      Município – Classificação de Serviços – Município com o COD\_PARAM = “421”\.

__      07 – Sociedade Profissional: __Quando campo IND\_ISS da tabela ESTABELECIMENTO = ‘08’\.

__      08 – Iss Devido em Outro município: __Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento

      estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

      __09 – Optante do Simples:__ Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”\.

      <a id="OLE_LINK47"></a><a id="OLE_LINK48"></a>__10 – Optante do MEI__: Não será tratada\.

      __01 \- Normal: __<a id="OLE_LINK63"></a>Se nenhuma das opções acima for verdadeira, preencher com__ “01”\.__

Tipo: Numérico

Tamanho: 02 caracteres

OS4626

OS4770

<a id="_Hlk417308165"></a>RN19

__Regra do Registro Tipo E \- Campo Código do Serviço:__

__\[ALTERADA – CH20424\_2016\]__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”*\.

Preencher com brancos à direita e ignorar os zeros à esquerda\. *Exemplos:* “0101”, deve gravar “1\.01”\.       

                                                                                                                         “40\.01” deve gravar “40\.01”

Formato: 99\.99 ou 9\.99 \(este quando iniciado com zeros\)

Tipo: Alfanumérico

Tamanho: 05 caracteres

OS4770

CH20424\_2016

MFS7153

<a id="_Hlk417303628"></a>RN20

__Regra do Registro Tipo E \- Campo Código da Atividade CNAE:__

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Preencher com o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO referente ao código da atividade econômica\.  O campo deve ser preenchido sem formatação\. Ex: “114700”\.

Quando o campo COD\_ATIVIDADE estiver vazio, deverá preencher com espaço e exibir a seguinte mensagem no Log: “Favor preencher o Código de Atividade Econômica – CNAE, no cadastro do Estabelecimento\.”

__Tipo: Alfanumérico__

__Tamanho: 10 caracteres__

OS4626

OS4770

RN21

__Regra do Registro Tipo E \- Campo Tipo de recolhimento do ISSQN:__

Preencher com:

"__A__" – Para preencher com “A”, é necessário que pelo menos umas das seguintes opções sejam verdadeiras:

               Verificar o local da prestação do serviço \(deve ser o campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não    estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2” e se o local da prestação do serviço = município do módulo selecionado
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido e se o local da prestação do serviço = município do módulo selecionado e se o local da prestação do serviço = município 

Se não, 

Preencher com __"R"\.__

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4626

RN22

__Regra do Registro Tipo E \- Campo Número do documento fiscal:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Na geração deste campo, deve ser consideradas 10 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 10 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(10 posições\)\.”

\(Ex para esta situação: Nº de NF 123456789012 será gerado 3456789012\)\.

Tipo: Numérico

Tamanho: 10 caracteres

OS4626

RN23

__Regra do Registro Tipo E \- Campo Valor Bruto do documento fiscal:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. 

Exemplo: R$10,25 = 000000000001025

OS4626

RN24

__Regra do Registro Tipo E \- Campo Valor do serviço:__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. 

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. Exemplo: R$10,25 = 000000000001025

OS4626

RN25

__Regra do Registro Tipo E \- Campo Aliquota de ISSQN:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

<a id="OLE_LINK139"></a><a id="OLE_LINK140"></a><a id="OLE_LINK141"></a>Tipo: Numérico

Tamanho: Valor com __04 __posições com zeros a esquerda, sem vírgula e sem ponto\. 

Exemplo: 5,00% = 0500 ou 2,75% = 0275

OS4626

OS4770

RN26

__Regra do Registro Tipo E \- Campo Valor do Imposto:__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. Exemplo: R$10,25 = 000000000001025

OS4626

<a id="_Hlk417308858"></a>

RN27

__Regra do Registro Tipo E \- Indicador de CPF/CNPJ do Tomador__

Este campo indica o tipo de dados que será fornecido no campo CPF/CNPJ do Tomador de serviços

Preencher com:

__1 __para CPF, <a id="OLE_LINK86"></a><a id="OLE_LINK87"></a><a id="OLE_LINK88"></a><a id="OLE_LINK89"></a><a id="OLE_LINK90"></a>quando a informação do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 11 posições\.

__2 __para CNPJ, quando a informação do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 14 posições\.

__3__ para Não\-informado, quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR estiver vazio\.

Tipo: Alfanumérico 

Tamanho: 01 caracteres

OS4770

<a id="_Hlk417304966"></a>RN28

__Regra do Registro Tipo E \- Campo CPF/CNPJ do tomador de serviços:__

Preencher com o campo <a id="OLE_LINK82"></a><a id="OLE_LINK83"></a><a id="OLE_LINK84"></a><a id="OLE_LINK85"></a>CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico 

Tamanho: 14 caracteres

OS4626

OS4770

RN29

__\[EXCLUÍDA OS4770\]__

__Regra do Registro Tipo E \- Campo Identificador Documento \(CPF/CNPJ/Documento não\-informado\) do tomador de serviços\.__

Preencher com “N“ caso o campo anterior “CPF/CNPJ do tomador de serviços” não estiver preenchido\. Caso contrário, deixar em branco este campo\.

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4626

OS4770

RN30

__Regra do Registro Tipo E \- Campo Inscrição Municipal do tomador de serviços:__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 07 caracteres

OS4626

RN31

__Regra do Registro Tipo E \- Campo Nome/Razão Social do tomador de serviços__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK94"></a><a id="OLE_LINK95"></a>Tipo: Alfanumérico

Tamanho: 80 caracteres

OS4626

<a id="OLE_LINK91"></a><a id="OLE_LINK92"></a><a id="OLE_LINK93"></a>OS4770

RN32

__\[EXCLUÍDA OS4770\]__

__Regra do Registro Tipo E \- Campo Nome Fantasia do tomador de serviços__

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 50 caracteres

OS4626

OS4770

RN33

__Regra do Registro Tipo E \- Campo Logradouro do tomador de serviços__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 50 caracteres

OS4626

OS4770

RN34

__Regra do Registro Tipo E \- Campo Número do tomador de serviços__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK96"></a><a id="OLE_LINK97"></a><a id="OLE_LINK98"></a><a id="OLE_LINK99"></a>__\[ALTERADO OS4770\]__

Tipo: Alfanumérico

Tamanho: 10 caracteres

OS4626

OS4770__ __

RN35

__Regra do Registro Tipo E \- Campo Complemento do tomador de serviços__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK100"></a><a id="OLE_LINK101"></a><a id="OLE_LINK102"></a>__\[ALTERADO OS4770\]__

Tipo: Alfanumérico

Tamanho: 30 caracteres

OS4626

<a id="OLE_LINK103"></a><a id="OLE_LINK104"></a><a id="OLE_LINK105"></a>OS4770

RN36

__Regra do Registro Tipo E \- Campo Bairro do tomador de serviços__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK106"></a><a id="OLE_LINK107"></a><a id="OLE_LINK108"></a><a id="OLE_LINK109"></a>__\[ALTERADO OS4770\]__

Tipo: Alfanumérico

Tamanho: 50 caracteres

<a id="OLE_LINK110"></a><a id="OLE_LINK111"></a>OS4626

OS4770

RN37

__Regra do Registro Tipo E \- Campo Cidade do tomador de serviços__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK112"></a><a id="OLE_LINK113"></a><a id="OLE_LINK114"></a><a id="OLE_LINK115"></a>__\[ALTERADO OS4770\]__

Tipo: Alfanumérico

Tamanho: 40 caracteres

<a id="OLE_LINK116"></a><a id="OLE_LINK117"></a><a id="OLE_LINK118"></a><a id="OLE_LINK119"></a>OS4626

OS4770

RN38

__Regra do Registro Tipo E \- Campo Estado do tomador de serviços__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4626

RN39

__Regra do Registro Tipo E \- Campo CEP do tomador de serviços__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADO OS4770\]__

Tipo: Alfanumérico

Tamanho:08 caracteres

OS4626

OS4770

__RN40__

__Regra do Registro Tipo R – Notas Fiscais Recebidas__

Registro de detalhes para notas fiscais recebidas, sem limites de ocorrências\.

OS4626

__MFS\-923053__

__RN41__

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

OS4626

__MFS\-923053__

RN42

__Regra do Registro Tipo R \- Campo Tipo do Registro:__

Preencher com o texto fixo __“R”, __indicando a linha do registro\.

Tipo: Alfanumérico

Tamanho: 01 caracter

OS4626

RN43

__Regra do Registro Tipo R \- Campo Data de Emissão:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data no formato __99/99/9999__

Tamanho: 10 caracteres

OS4626

RN44

__Regra do Registro Tipo R \- Campo Modelo:__

Preencher com a informação do campo “Modelo DMISS” da tela Modelo Msaf x modulo, em Parâmetros para Município, referente ao modelo cadastrado na nota fiscal\.

Obs\.: Caso o modelo não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para o Modelo de Documento "XX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização de Modelo Msaf x Modelo\. Efetuar a parametrização no menu Parâmetros > Modelo Msaf x Modelo no módulo "Parâmetros para Município"\.

Tipo: Alfanumérico 

Tamanho: 02 caracteres

OS4626

RN45

__Regra do Registro Tipo R \- Campo Natureza da Operação:__

Preencher com: 

__ALTERADA OS4770\]__

__      11 – Isento:__ <a id="OLE_LINK72"></a>Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver

      preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados

      na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__      12 – ISS Devido pelo prestador:__ Verificar se__ __o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. __ __

      __02 – Com Dedução: __Verificar se__ __o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. __ __

      __03 – Não Incidência:__ Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem

      parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”;

      __04 – Imune:__ Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\. Se não estiver preenchido,

      verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros \- 

      Classificação de Serviços com o COD\_PARAM = “420”__;__

      __05 – Construção Civil:__ Quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço

      cadastrado na nota\.

      __06 – Regime de Estimativa: __verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido

      verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por

      Município – Classificação de Serviços – Município com o COD\_PARAM = “421”\.

__      07 – Sociedade Profissional: __Quando campo IND\_ISS da tabela ESTABELECIMENTO = ‘08’\.

__      08 – Iss Devido em Outro município: __Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento

      estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

      __09 – Optante do Simples:__ Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR estiver selecionado\.

      __10 – Optante do MEI__: Não será tratada\.

      __01 \- Normal: __Se nenhuma das opções acima for verdadeira, preencher com__ “01”\.__

Tipo: Numérico

Tamanho: 02 caracteres

OS4626

OS4770

RN46

__Regra do Registro Tipo R \- Campo Código do Serviço:__

__\[ALTERADA – CH20424\_2016\]__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”*\.

Preencher com brancos à direita e ignorar os zeros à esquerda\. *Exemplos:* “0101”, deve gravar “1\.01”\.       

                                                                                                                         “40\.01” deve gravar “40\.01”

Formato: 99\.99 ou 9\.99 \(este quando iniciado com zeros\)

Tipo: Alfanumérico

Tamanho: 05 caracteres

OS4770

CH20424\_2016

MFS7153

RN47

__Regra do Registro Tipo R \- Campo Codigo da Atividade CNAE:__

 Preencher com o campo COD\_ATIVIDADE da tabela X04\_PESSOA\_FIS\_JUR referente ao Código da Atividade Econômica\. O campo deve ser preenchido sem formatação\. Ex: “114700”\.

Quando o campo COD\_ATIVIDADE estiver vazio, deverá preencher com espaço e exibir a seguinte mensagem no Log: “Favor preencher o Código de Atividade Econômica – CNAE, no cadastro de Pessoa Física/Jurídica\.”

__Tipo: Alfanumérico__

__Tamanho: 10 caracteres__

<a id="OLE_LINK124"></a><a id="OLE_LINK125"></a><a id="OLE_LINK126"></a><a id="OLE_LINK127"></a>OS4770

RN48

__Regra do Registro Tipo R \- Campo Tipo de recolhimento do ISSQN:__

Preencher com:

"__A__" – Para preencher com “A”, é necessário que pelo menos umas das seguintes opções sejam verdadeiras:

               Verificar o local da prestação do serviço \(deve ser o campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não    estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado; 
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado;
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido e se o local da prestação do serviço = município do módulo selecionado e se o local da prestação do serviço = município 

<a id="OLE_LINK128"></a>

Se não, 

Preencher com __"R"\.__

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4770

__RN49__

__Regra do Registro Tipo R \- Campo Número do documento fiscal:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Na geração deste campo, deve ser consideradas 10 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 10 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(10 posições\)\.”

\(Ex para esta situação: Nº de NF 123456789012 será gerado 3456789012\)\.

Tipo: Numérico

Tamanho: 10 caracteres

OS4626

__MFS\-923053__

RN50

__Regra do Registro Tipo R \- Campo Valor Bruto do documento fiscal:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. 

Exemplo: R$10,25 = 000000000001025

OS4626

RN51

__Regra do Registro Tipo R \- Campo Valor do serviço:__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. 

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. 

Exemplo: R$10,25 = 000000000001025

OS4626

RN52

__Regra do Registro Tipo R \- Campo Aliquota de ISSQN:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: Valor com __04 __posições com zeros a esquerda, sem vírgula e sem ponto\. 

Exemplo: 5,00% = 0500 ou 2,75% = 0275

OS4626

OS4770

RN53

__Regra do Registro Tipo R \- Campo Valor do Imposto:__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Tipo: Numérico

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\. Exemplo: R$10,25 = 000000000001025

OS4626

__RN54__

__Regra do Registro Tipo R \- Indicador de CPF/CNPJ do Prestador__

Este campo indica o tipo de dados que será fornecido no campo CPF/CNPJ do prestador de serviços\.

Preencher com:

__1 __para CPF, quando a informação do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 11 posições\.

__2 __para CNPJ, quando a informação do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR possuir 14 posições\.

__3__ para Não\-informado, quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR estiver vazio\.

Tipo: Alfanumérico 

Tamanho: 01 caracteres

<a id="OLE_LINK145"></a><a id="OLE_LINK146"></a><a id="OLE_LINK147"></a><a id="OLE_LINK148"></a>OS4770

__MFS\-923053__

RN55

__Regra do Registro Tipo R \- Campo CPF/CNPJ do prestador de serviços:__

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\. 

__\[ALTERADA OS4770\]__

Tipo: Numérico 

Tamanho: 14 caracteres

OS4626

<a id="OLE_LINK149"></a><a id="OLE_LINK150"></a><a id="OLE_LINK151"></a><a id="OLE_LINK152"></a>OS4770

RN56

__\[EXCLUÍDA OS4770\]__

__Regra do Registro Tipo R \- Campo Identificador Documento \(CPF/CNPJ/Documento não\-informado\) do prestador de serviços__

Não será tratado\.

Tipo: Alfanumérico

Tamanho: 01 caracteres

OS4626

<a id="OLE_LINK153"></a><a id="OLE_LINK154"></a><a id="OLE_LINK155"></a><a id="OLE_LINK156"></a>OS4770

RN57

__Regra do Registro Tipo R \- Campo Inscrição Municipal do prestador de serviços:__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 07 caracteres

OS4626

RN58

__Regra do Registro Tipo R \- Campo Nome/Razão Social do prestador de serviços__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK157"></a><a id="OLE_LINK158"></a><a id="OLE_LINK159"></a>__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 80 caracteres

OS4626

OS4770

RN59

__\[EXCLUÍDA OS4770\]__

__Regra do Registro Tipo R \- Campo Nome Fantasia do prestador de serviços__

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 60 caracteres

OS4626

OS4770

RN60

__Regra do Registro Tipo R \- Campo Endereço do prestador de serviços__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 50 caracteres

OS4626

OS4770

RN61

__Regra do Registro Tipo R \- Campo Número do prestador de serviços__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 10 caracteres

OS4626

OS4770

RN62

__Regra do Registro Tipo R \- Campo Complemento do prestador de serviços__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 30 caracteres

OS4626

OS4770

RN63

__Regra do Registro Tipo R \- Campo Bairro do prestador de serviços__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 50 caracteres

OS4626

OS4770

RN64

__Regra do Registro Tipo R \- Campo Cidade do prestador de serviços__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

<a id="OLE_LINK160"></a><a id="OLE_LINK161"></a><a id="OLE_LINK162"></a>__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 40 caracteres

OS4626

OS4770

RN65

__Regra do Registro Tipo R \- Campo Estado do prestador de serviços__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Alfanumérico

Tamanho: 02 caracteres

OS4626

RN66

__Regra do Registro Tipo R \- Campo CEP do prestador de serviços__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__\[ALTERADA OS477O\]__

Tipo: Alfanumérico

Tamanho: 08 caracteres

OS4626

OS4770

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

