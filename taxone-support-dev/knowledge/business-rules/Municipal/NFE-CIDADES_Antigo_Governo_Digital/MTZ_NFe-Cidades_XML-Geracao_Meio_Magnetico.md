# MTZ_NFe-Cidades_XML-Geracao_Meio_Magnetico

- **Fonte:** MTZ_NFe-Cidades_XML-Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-03-09
- **Tamanho:** 120 KB

---

### NFe\-Cidades – Geração do Meio Magnético – V01

### Controle das Alterações

__MFS__

__Nome__

__Descrição__

__OS3470\-F__

Geração do Meio Magnético NFe\-Cidades 

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo NFe\-Cidades\. Dessa forma usaremos o módulo de Parâmetros por Município que servirá para o usuário realizar a parametrização de todos os municípios atendidos pelo NFe\-Cidades em um único lugar\. Além disso, também realizaremos a geração dos municípios através de uma única geração, ou seja, quando o cliente clicar em um município do NFe\-Cidades será exibido a mesma tela de geração do Meio Magnético\. 

Com essa OS também estaremos criando as obrigações para os municípios de Louveira, Itajubá, Guaxupé, entre outros\. 

__OS3786__

Ajustar o formato do arquivo de Retenções \(Tomador\) para XML

Este documento tem como objetivo permitir que os municípios do validador NFe\-Cidades passem a gerar os arquivos XML de acordo com o novo layout\.

__CH21455\_2013__

Correção dos campos Valor e ValorISS\.

Este documento tem como objetivo corrigir o campo “Valor” da tag Item e incluir o campo “ValorIss” da tag Item\.

__CH4832\_2014__

GUAXUPÉ \- Não está gerando o campo tributacao na tag <nf>\.

Este documento tem como objetivo ajustar a geração do arquivo, incluindo a tag <tributação>\.

__OS4552__

Não está gerando corretamente o campo tributacao na tag <nf>\.

Este documento tem como objetivo corrigir a geração do arquivo, ajustando os dados da tag <tributacao>\.

__CH13734\_2014__

Alteração do campo atividade da tag <item> 

Este documento tem como objetivo alterar o campo atividade da tag <item> para Serviços Prestados e Serviços Tomados\.

__CH10072\_2014__

Divinópolis – Alteração do campo tributacao na tag <nf>

Este documento tem como objetivo alterar o campo tributacao da tag <nf> para Serviços Prestados e Serviços Tomados especificamente do município Divinópolis\.

__CH24741\_2014__

Pouso Alegre e Amparo – Alteração do campo tributacao na tag <nf>

Este documento tem como objetivo alterar o campo tributacao da tag <nf> para Serviços Tomados especificamente do município Pouso Alegre e Amparo\.

__CH20606\_2014__

Itajubá – Alteração do campo tributacao na tag <nf>

Este documento tem como objetivo alterar o campo tributacao da tag <nf> para Serviços Tomados especificamente ao município Itajuba\.

__CH24741\-A\_2014__

Pouso Alegre e Amparo – Alteração do campo tributacao na tag <nf>

Este documento tem como objetivo alterar o campo tributacao da tag <nf> para Serviços Tomados especificamente ao município Pouso Alegre e Amparo

__MFS\-1522__

Teixeira de Freitas – Inclusão de Município

Este documento tem como objetivo atribuir as funcionalidades do Validador NFe\-Cidades ao município aderente de Teixeira de Freitas do estado da Bahia\.

__MFS\_2071__

Santa Bárbara D’ Oeste – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

__MFS\-16477__

São Roque – Inclusão de Município

Este documento tem como objetivo incluir o município de São Roque/SP no validador NFe\-Cidades conforme layout disponibilizado pela prefeitura\.

__MFS\-25461__

SAO ROQUE \- Alteração regra tag <tributacao>

Este documento tem como objetivo ajustar a regra do campo <tributacao> de serviços tomados\. 

__MFS\-26695__

SAO ROQUE \- Alteração regra tag <atividade>

Este documento tem como objetivo ajustar a regra do campo <atividade> 

__MFS\-35279__

Araguari – Inclusão de Município

Este documento tem como objetivo incluir o município de Araguari/MG no validador NFe\-Cidades conforme layout disponibilizado pela prefeitura\.

__MFS\-48814__

Jaguariúna – Inclusão de Município

Esse documento tem como objetivo incluir o município de Jaguariúna/SP no validador NFe\-Cidades conforme layout disponibilizado pela prefeitura\.

Obs\. Conforme alinhamento com a equipe do Sonner \(empresa desenvolvedora do validador\), devemos considerar o mesmo layout do município de São Roque\.

__MFS\-74653__

DW \- MUNICIPAL – Lagoa Santa \- Inclusão de Município

Alterar a descrição do validador GOV DIGITAL para NFE\-CIDADES, pois o layout servirá para outros municípios \.\(Alterar a TFIX105 e tela de validadores\)

Esse documento tem como objetivo incluir o município de Lagoa Santa/MG\.

__MFS\-80214__

DW \- MUNICIPAL – Poços de Caldas

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de Poços de Caldas, que passa a considerar apenas as Notas Fiscais de prestadores de outros municípios\.

__MFS\-80305__

DW \- MUNICIPAL – Divinópolis

Este documento tem como objetivo alterar a regra de preenchimento do campo <atividade> para o município de Divinópolis\.

__MFS\-81352__

DW \- MUNICIPAL – Poços de Caldas

Este documento tem como objetivo alterar de preenchimento do campo <atividade> para o município de Poços de Caldas

__MFS\-89469__

Elisabete Costa

Este documento tem como objetivo incluir o município de “Limeira do Oeste/MG”\.

__MFS\-97195__

Elisabete Costa

Este documento tem como objetivo incluir o município de “Frutal/MG”\.

__MFS\-570046__

Rosemeire Santos

Este documento tem como objetivo implementar um novo parâmetro para que seja possível a geração do arquivo por Data de Emissão” na tela de geração\.

__MFS\-570328__

Rosemeire Santos

Este documento tem o objetivo é de readequar a regra de geração para o validador NFE CIDADES gerar ou não, conforme parametrização da tela de “Definição de Layout”\.

__MFS\-570805__

Rosemeire Santos

Este documento tem como objetivo ajustar campo <serie>, para o município de Jaguariúna/SP\.

__MFS__\-__575093__

Rogério Ohashi

Este documento tem como objetivo incluir o parâmetro “Quebrar Arquivos por Data de Emissão” na tela de Geração do Meio Magnético, quando houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Funcionalidade válido apenas para Geração de Serviços Tomados\.

__MFS\-600391__

Rosemeire Santos

Este documento tem como objetivo incluir o município de “Louveira/SP” no validador NFe\-Cidades\.

__MFS\-614477__

Rogério Ohashi

Este documento tem como objetivo alterar a regra de preenchimento do campo <atividade> para o município de Louveira\.

__MFS\-685523__

Bruna Ribeiro

Este documento tem como objetivo alterar a regra da tag tributação específica para o município de Louveira\. 

__MFS\-839837__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-909148__

Andréa Rocha

Este documento tem como objetivo alterar a regra de preenchimento do campo <atividade> para o município de Lagoa Santa\.

__MFS\-954705__

Rafael Fabiano

Este documento tem como objetivo de retornar o município de “Amparo/SP” no validador NFe\-Cidades\.

__MFS\-1050929__

Rosemeire Santos

Este documento tem como objetivo incluir os municípios de Socorro\-SP, Várzea Paulista\-SP, Ouro Preto\-MG e Paracatu\-MG, no validador NFe\-Cidades\.

__MFS\-1051533__

Rosemeire Santos

Este documento tem como objetivo, alterar o preenchimento da regra __RN12\.c__ da tag tributação para a geração Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\) para o município de Jaguariúna\.

### REGRAS DE NEGÓCIO 

__CÓD__

__DESCRIÇÃO__

__MFS__

__RN01__

__Estrutura de menus do módulo NFe\-Cidades:__

Deverão ser criados os seguintes menus e sub\-menus no módulo NFe\-Cidades:

- Arquivo
- Obrigações
	- Meio Magnético
	- Geração Meio Magnético – RPS
	- Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3470\-F__

__RN02__

__Regra de criação do nome do arquivo__

__Serviços Prestados:__

__SP\_ EMPRESA \_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.xml__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

__       ESTABELECIMENTO: __Representa o prestador de serviço

__       EMPRESA: __Representa o prestador de serviço

       __SP__: Apenas registros de serviços prestados\.

       __\.xml__: extensão do arquivo\.

__Ex:__ SP\_EMPRESA\_ESTABELECIMENTO\_UNAI\_012010\.xml

__Serviços Tomados:__

__ST\_ EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.xml__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

       __ST__: Apenas registros de serviços tomados\.

       __\.xml__: extensão do arquivo\.

__Ex:__ ST\_ EMPRESA\_ESTABELECIMENTO\_UNAI\_012010\.xml

__\[ALTERAÇÃO\-MFS\-570046\] – Regra Inclusão do parâmetro na tela geração “Gerar arquivo por Data de Emissão” por validador\.  __

Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

O parâmetro Gerar Arquivo por Data de Emissão estiver marcado\.

Este arquivo deverá conter todas as notas fiscais com data de emissão dentro do período de referência\.

__ALTERAÇÃO\-MFS575093\] Tratamento da regra de geração para considerar o parâmetro “Quebrar Arquivos por Data de Emissão”__

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado deve ser realizado a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__ST\_ EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA \_MMAAAA\.xml__, onde:

__       ST:__ Apenas registros de serviços tomados\.

__       MUNICIPIO: __município que está sendo gerado\.

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       MMAAAA__: representa a data inicial da geração\.

__       MMAAAA: __representa a data de período de geração, mês e ano\.

__      \.xml__: extensão do arquivo\.

Ex: ST\_ EMPRESA\_ESTABELECIMENTO\_UNAI\_012010\_122009\.xml 

Obs: Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

__OS3470\-F__

__MFS\-570046__

__MFS575093__

__MFS\-839837__

__MFS\-954705__

__RN03__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__\[ALTERAÇÃO\-MFS\-570046\] – Regra Inclusão do parâmetro na tela geração “Gerar arquivo por Data de Emissão” por validador__

Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

Gerar Arquivo por Data de Emissão: deve ser exibido através de um checkbox\. \(Opções S = Marcado e N = Desmarcado\)

__ALTERAÇÃO\- MFS575093\] Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão”__

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. 

A opção S = “Marcado” e N = “Desmarcado"\. 

__Obs:__ Devem ser gerados arquivos separados para serviços prestados e serviços tomados, ou seja, um arquivo para os registros prestados e outro para os registros tomados\.

__OS3470\-F__

__MFS\_2071__

__MFS\-570046__

__MFS575093__

__MFS\-954705__

__RN04__

__Regra p/ Estrutura do XML:__

<?xml version="1\.0" encoding="ISO\-8859\-1" standalone="true"?>

<GovDigital xsi:noNamespaceSchemaLocation="govdigital\.xsd"  xmlns:xsi="http://www\.w3\.org/2001/XMLSchema\-instance"> 

<escrituracao mes="MM” ano="AAAA" > 

<nf>                \.\.\.

<contraparte> 

          \.\.\.

</contraparte>

<itens> 

<item>

				    \.\.\.

                                                         </item> 

<item>

				    \.\.\.

                                                         </item>

 			</itens> 

		</nf> 

</escrituracao> 

</GovDigital>

__OS3786__

__RN05__

__Regra p/ recuperar notas fiscais emitidas__:

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

__Obs:__ Se a nota tiver mais de um item, os mesmos devem ser informados em cada tag de item\. Os itens de mesmo código de atividade devem ser consolidados e demonstrados em uma única tag item\.

__OS3786__

__MFS\-954705__

__RN06__

__Regra p/ recuperar notas fiscais recebidas__:

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Nota não cancelada \(SITUACAO <> ‘S’\)

Quando a nota não tiver itens não deve ser recuperada\.

__Obs: __Se a nota tiver mais de um item, os mesmos devem ser informados em cada tag de item\. Os itens de mesmo código de atividade devem ser consolidados e demonstrados em uma única tag item\.

__\[ALTERAÇÃO\-MFS\-570046\] – Regra Inclusão do parâmetro na tela geração “Gerar arquivo por Data de Emissão” por validador__

Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

O parâmetro Gerar Arquivo por Data de Emissão estiver marcado\.

Este arquivo deverá conter todas as notas fiscais com data de emissão dentro do período de referência\.

__\[ALTERAÇÃO\-MFS\-570328/ MFS\-600391\] __A regra abaixo deve ser aplicada para o validador __NFe\-Cidades__, abrangendo todos os municípios que utiliza esse validador\.

__Desconsiderar as NFS\-e emitidas no próprio município__ __– Específico para Jaguariuna/SP\.__

     

\- Recuperar as Notas Fiscais Eletrônico de Serviço, considerando a parametrização da Tela de __“Notas Fiscais Eletrônicas”, __no Menu Parâmetros por Município com as chaves de __UF__ e __Município__, conforme regras abaixo:

__Notas Fiscais eletrônicas de Serviço Prestado: __

__\- Para Tomadores Dentro do município:__

__Se __parâmetro “__*Tomador Dentro do Município*__” estiver “__*marcado*__” desconsiderar notas fiscais com campo movto\_e\_s = 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do tomador for __*igual*__ ao código de município do Estabelecimento;

__Se __parâmetro “__*Tomador Dentro do Município*__” estiver “__*desmarcado*__” considera as notas fiscais com campo movto\_e\_s = 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do tomador for __*igual*__ ao código de município do Estabelecimento;

__\- Para Tomadores Fora do município:__

__\- Se __parâmetro “__*Tomador Fora do Município*__” estiver “__*marcado*__” gerar notas fiscais com campo movto\_e\_s = 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do tomador for __*diferente*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Tomador Fora do Município*__” estiver “__des*marcado*__” desconsiderar as notas fiscais com campo movto\_e\_s = 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do tomador for __*diferente*__ ao código de município do Estabelecimento;

Default: Desmarcado

__Notas Fiscais eletrônicas de Serviço Tomado: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Para Prestadores Fora do município:__

__Se __parâmetro “__*Prestador Fora do Município*__” estiver “__marcado__” gerar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*diferente*__ ao código de município do Estabelecimento\.

__Se __parâmetro “__*Prestador Fora do Município*__” estiver “__desmarcado__” desconsiderar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente

ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*diferente*__ ao código de município do Estabelecimento\.

 Default: Desmarcado

__ \-  Se__ a __UF__ e o __Município __do estabelecimento não estiver parametrizados no Módulo > Parâmetro por Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

\- Para as notas eletrônicas, __recuperar somente__ se:

\- Se o Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __E__ município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\) 

__OU__

\- Se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente

ao tipo de documento da nota fiscal __E__ município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

\- Estabelecimentos escolhidos na tela de geração

\- Data fiscal dentro do período de referência

\- Notas canceladas devem ser consideradas

__OS3786__

__MFS\-570046__

__MFS\-570328__

__MFS\-600391__

__MFS\-954705__

__MFS\-1050929__

__RN06\.a__

__Regra p/ recuperar notas fiscais recebidas__ __\(Regra Específica \- Poços de Caldas__\):

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Nota não cancelada \(SITUACAO <> ‘S’\)
- Prestadores fora do município de Poços de Caldas, ou seja, quando a Pessoa Fis/Jur cadastrada na NFS tiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR diferente de Poços de Caldas

Quando a nota não tiver itens não deve ser recuperada\.

__Obs:__ Se a nota tiver mais de um item, os mesmos devem ser informados em cada tag de item\. Os itens de mesmo código de atividade devem ser consolidados e demonstrados em uma única tag item\.

__MFS\-80214__

__RN07__

__Regra p/ tag <escrituracao ano="AAAA" mes="MM">__:

Preencher o campo:

- escrituração ano com o ano informado no campo Data Inicial da tela de geração do meio magnético\.
- escrituração mês com o mês informado no campo Data Inicial da tela de geração do meio magnético\.

__OS3786__

__RN08__

__Regra p/ o campo correlação da tag <nf>__

Preencher com um sequencial único para cada nota gerada no arquivo\. Deve\-se conter um sequencial para cada arquivo gerado \(Notas Emitidas e Notas Recebidas\)\.

__OS3786__

__RN09__

__Regra p/ o campo papel da tag <nf>__

Preencher com:

prestador, quando o campo movto\_e\_s da tabela DWT\_DOCTO\_FISCAL = ‘9’

tomador, quando o campo movto\_e\_s da tabela DWT\_DOCTO\_FISCAL <> ‘9’

__OS3786__

__RN10__

__Regra p/ o campo número da tag <nf>__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3786__

__RN11__

__Regra p/ o campo serie da tag <nf>__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[ALTERAÇÃO\-MFS\-570805\] – Regra específica para Notas de Serviço Tomados no município de Jaguariúna/SP\.__

Quando o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL, estiver vazio, preencher com valor “__NFS__”, conforme orientação da prefeitura\.

__OS3786__

__MFS\-570805__

__RN12__

__Regra p/ o campo tributacao da tag <nf> \- REGRA GERAL__

A tag “__tributacao”, __deverá ser gerada__ __para todos os casos, independente se o prestador for ou não do mesmo município de geração\.

__Notas fiscais emitidas__

Deve preencher com:

__‘5’ – Retida __

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 

OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__‘6’ – Não retida __

Caso nenhuma das opções acima seja verdadeira\.

__Notas fiscais recebidas__

Deve preencher com:

__ __

__‘5’ – Retida __

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 

OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__ ‘6’ – Não retida __

Caso nenhuma das opções acima seja verdadeira\.

__CH4832\_2014__

__OS4552__

__MFS\-954705__

__MFS\-1050929__

__RN12\.a__

__Regra p/ o campo tributacao da tag <nf> \- ESPECÍFICA__

__Para o município: Bragança Paulista, Socorro, Várzea Paulista, Ouro Preto e Paracatu\.__

__Deverá tratar os tipos de tributação abaixo:__

__Notas Fiscais Recebidas__

__“5” – Isenção:__

\- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”

\- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”; __preencher com “5”\.__

__“6” – Imune:__

\- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”

\- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”;__ preencher com “6”\.__

__“7” \- Exigibilidade Suspensa por Processo Administrativo: __

__\- __Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”, __preencher com “7”;__

__“8” \- Exigibilidade suspensa por decisão Judicial: __

__\- __Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”

\- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”; __preencher com “8”\.__

__“10” – Exportação:__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”, __preencher com “10’;__

__“1” – Tributação no Município:__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”, __preencher com “1’;__

__“2” – Tributação fora do Município:__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”, __preencher com “2’;__

__“3” \- Retido no Município: __Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado __OU __

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado, __OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“4” \- __Caso nenhuma das opções acima seja verdadeira, __preencher com “4”__

__Notas Fiscais Emitidas__

__“9” – Cancelado: __Se campo SITUACAO = “S” da SAFX07\.

__“5” – Isenção:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”;

__Preencher com “5”\.__

__“6” – Imune:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”;__ preencher com “6”\.__

__“7” \- Exigibilidade Suspensa por Processo Administrativo: __

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”, __preencher com “7”;__ 

__“8” \- Exigibilidade suspensa por decisão Judicial: __

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”; __preencher com “8”\.__

__“10” – Exportação:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”, __preencher com “10’;__

__“1” – Tributação no Município:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”, __preencher com “1’;__

__“2” – Tributação fora do Município:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”, __preencher com “2’;__

__“3” \- Retido no Município: __Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“4” \- __Caso nenhuma das opções acima seja verdadeira, __preencher com “4”\.__

__OS4552__

__MFS\-1050929__

__RN12\.b__

__Regra p/ o campo tributacao da tag <nf> \- ESPECÍFICA__

__Para o município: Divinópolis / MG__

__Deverá tratar os tipos de tributação abaixo:__

__Notas Fiscais Recebidas__

Deve preencher com:

__“4” – Retida__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado; OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado; OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“8” – Não retida__

Caso nenhuma das opções acima seja verdadeira\.

__Notas Fiscais Emitidas__

__“2” – Cancelado: __

\- Se campo SITUACAO = “S” da SAFX07\.

__“9” \- Exigibilidade suspensa por decisão Judicial: __

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “08”\.

__“1” – Tributada:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”; OU

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”\.

__“3” – Isenção/Imune:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”; OU

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”; OU

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”; OU

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

__“6” – Não Tributada:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “09”; OU

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

__“5” – Retida Fora do Município:__

\- Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\):

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado; OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado; OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado;

\- Verificar se o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\) das notas fiscais é diferente do município do Estabelecimento\.

__CH10072\_2014__

__RN12\.c__

__Regra p/ o campo tributacao da tag <nf>   \-   ESPECÍFICA__

__Para os municípios: Pouso Alegre, Amparo, Itajubá, Teixeira de Freitas, São Roque, Jaguariúna, Lagoa Santa, Limeira do Oeste\.__

__Deverão tratar os tipos de tributação abaixo:__

__Notas fiscais recebidas__

Deve preencher com:

__‘1’ – Retida__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

‘__2’ – Não retida__

Caso nenhuma das opções acima seja verdadeira\.

__\[ALTERAÇÃO \- MFS\-1051533\] – __Específica para o município de __Jaguariúna__ Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)

__Notas fiscais recebidas__

Deve preencher com:

__‘2’ – Retida__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

‘__1’ – Não retida__

Caso nenhuma das opções acima seja verdadeira\.

__Notas fiscais emitidas__

__“9” – Cancelado: __Se campo SITUACAO = “S” da SAFX07\.

__“5” – Isenção:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”;

__Preencher com “5”\.__

__“6” – Imune:__

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”;__ preencher com “6”\.__

__“7” \- Exigibilidade Suspensa por Processo Administrativo: __

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”, __preencher com “7”;__ 

__“8” \- Exigibilidade suspensa por decisão Judicial: __

\- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”\.

\- Se não estiver preenchido, verificar se o serviço e o município do estabelecimento cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”; __preencher com “8”\.__

__“10” – Exportação:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”, __preencher com “10’;__

__“1” – Tributação no Município:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”, __preencher com “1’;__

__“2” – Tributação fora do Município:__

Se o serviço e o município do estabelecimento cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”, __preencher com “2’;__

__“3” \- Retido no Município: __

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“4” \- __Caso nenhuma das opções acima seja verdadeira, __preencher com “4”\.__

__CH24741\_2014__

__CH24741\_2014__

__CH20606\_2014__

__MFS\-1522__

__MFS\-25461__

__MFS\-48814__

__MFS\-74653__

__MFS\-89469__

__MFS\-1051533__

__RN12\.d__

__Regra p/ o campo tributacao da tag <tributação>   \-   ESPECÍFICA __para o município de Louveira\. 

Não gerar a tag tributação\. 

OBS: Conforme orientação da Prefeitura de Louveira o campo de tributação deixará de ser obrigatório e em breve será retirado\. 

__MFS\-685523__

__RN13__

__Regra p/ o campo diaPrestacao da tag <nf>__

Preencher com o dia do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: DD\.

__OS3786__

__RN14__

__Regra p/ o campo documento da tag <contraparte>__

Preencher o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN15__

__Regra p/ o campo nome da tag <contraparte>__

Preencher o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN16__

__Regra p/ o campo cep da tag <contraparte>__

Preencher o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN17__

__Regra p/ o campo logradouro da tag <contraparte>__

Preencher os campos TP\_LOGRADOURO e ENDERECO concatenados da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN18__

__Regra p/ o campo numero da tag <contraparte>__

Preencher o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN19__

__Regra p/ o campo complemento da tag <contraparte>__

Preencher o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN20__

__Regra p/ o campo bairro da tag <contraparte>__

Preencher o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN21__

__Regra p/ o campo estado da tag <contraparte>__

Preencher o campo COD\_ESTADO da tabela ESTADO correspondente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN22__

__Regra p/ o campo municipio da tag <contraparte>__

Preencher o campo DESCRICAO da tabela MUNICIPIO correspondente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN23__

__Regra p/ o campo pais da tag <contraparte>__

Preencher o campo DESCRICAO da tabela PAIS correspondente ao campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

__OS3786__

__RN24__

__Regra p/ o campo atividade da tag <item>   \- REGRA GERAL__

Preencher o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Tratamento:__

- Deverá vir com 6 posições separado por pontos – __Máscara: 00\.00\.00__
- Como na tabela DWT\_SERVICO\_LEI\_116 o código de serviço é cadastrado com 4 posições e o validador exige “gênero\.serviço”, recuperar o código de serviço e repetir as duas primeiras posições\. 

__Exemplo:__ 1001 deverá gerar 10\.10\.01\. 

- Quando o código de serviço for iniciado com zero será feito o mesmo tratamento anterior, mas devem ser ignorados os zeros nos dois primeiros separadores\. 

__Exemplo:__ 0702 deverá gerar 7\.7\.02\.

Se o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 não estiver preenchido para o serviço cadastrado na nota, deve\-se deixar o campo em branco e exibir uma mensagem no log informado a ausência da informação\.

__OS3786__

__CH13734\_2014__

__MFS\-954705__

__RN24\.a__

__Regra p/ o campo atividade da tag <item> Específica __

__Para os municípios: São Roque, Jaguariúna, Divinópolis, Poços de Caldas, Limeira do Oeste, Louveira, Lagoa Santa, Socorro, Várzea Paulista, Ouro Preto e Paracatu\.__

Preencher o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Tratamento:__

- Deverá vir com 4 posições separado por pontos – __Máscara: 00\.00__
- Como na tabela DWT\_SERVICO\_LEI\_116 o código de serviço é cadastrado com 4 posições\. 

__Exemplo:__ 1001 deverá gerar 10\.01\. 

Se o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 não estiver preenchido para o serviço cadastrado na nota, deve\-se deixar o campo em branco e exibir uma mensagem no log informado a ausência da informação\.

__MFS\-26695__

__MFS\-48814__

__MFS\-80305__

__MFS\-81352__

__MFS\-89469__

__MFS\-614477__

__MFS\-909148__

__MFS\-1050929__

__RN24\.b__

__Regra p/ o campo atividade da tag <item> Específica __

__Para o município: Araguari e Lagoa Santa__

Preencher o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Tratamento:__

- Deverá vir com 4 posições separado por pontos – __Máscara: 0\.000__
- Como na tabela DWT\_SERVICO\_LEI\_116 o código de serviço é cadastrado com 4 posições\. 

__Exemplo:__ 1001 deverá gerar 1\.001\. 

Se o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 não estiver preenchido para o serviço cadastrado na nota, deve\-se deixar o campo em branco e exibir uma mensagem no log informado a ausência da informação\.

__MFS\-35279__

__MFS\-74653__

__RN25__

__Regra p/ o campo descricao da tag <item>__

Preencher o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__OS3786__

__RN26__

__Regra p/ o campo valor da tag <item>__

Preencher com o valor do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. Utilizar ponto como separador de decimais\.

__OS3786__

__CH21455__

__RN27__

__Regra p/ o campo valorIss da tag <item>__

Preencher com o valor do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Utilizar ponto como separador de decimais\.

Caso não possuir valores, informar abertura e fechamento da Tag\. 

__Exemplo:__ <valorIss></valorIss>\. 

__OBS\.:__ Quando o campo papel  da Tag <nf> for diferente de __“Tomador”__ o campo valorIss não deve ser gerado\.

__OS3786__

__CH21455__

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

MFS\-8205

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-8205

__IM03__

Código IBGE: __14550 – __Município/UF:__ CARNEIRINHO / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica\.

__OS3470\-F__

__IM04__

Código IBGE: __22306 – __Município/UF:__ DIVINÓPOLIS / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica\.

__OS3470\-F__ 

__IM05__

Código IBGE: __28709 – __Município/UF:__ GUAXUPÉ / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica\.

__OS3470\-F__

__IM06__

Código IBGE: __32404 – __Município/UF:__ ITAJUBÁ / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM07__

Código IBGE: __38203 – __Município/UF:__ LAVRAS / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM08__

Código IBGE: __49309 – __Município/UF:__ PEDRO LEOPOLDO / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM09__

Código IBGE: __51800 – __Município/UF:__ POÇOS DE CALDAS / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM10__

Código IBGE: __52501 – __Município/UF:__ POUSO ALEGRE / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM11__

Código IBGE: __52808 – __Município/UF:__ PRATA / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica\.

__OS3470\-F__

__IM12__

Código IBGE: __59803 – __Município/UF:__ SANTA VITÓRIA / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM13__

Código IBGE: __68606 – __Município/UF:__ TEÓFILO OTONI / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM14__

Código IBGE: __70404 – __Município/UF:__ UNAÍ / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM15__

Código IBGE: __70438 – __Município/UF:__ UNIÃO DE MINAS / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM16__

Código IBGE: __1905 – __Município/UF:__ AMPARO / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM17__

Código IBGE: __7605 – __Município/UF:__ BRAGANÇA PAULISTA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM18__

Código IBGE: __22307 – __Município/UF:__ ITAPETININGA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM19__

Código IBGE: __27306 – __Município/UF:__ LOUVEIRA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM20__

Código IBGE: __56453 – __Município/UF:__ VARGEM GRANDE PAULISTA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__OS3470\-F__

__IM21__

Código IBGE: __31350 – __Município/UF:__ TEIXEIRA DE FREITAS / BA__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-1522__

__IM22__

Código IBGE: __14407 – __Município/UF:__ PELOTAS / RS__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-10413__

__IM23__

Código IBGE: __50605 – __Município/UF:__ SÃO ROQUE / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-16477__

__IM24__

Código IBGE: __3504 – __Município/UF:__ ARAGUARI / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-35279__

__IM25__

Código IBGE: __24709 – __Município/UF:__ JAGUARIÚNA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-48814__

__IM26__

Código IBGE: __37601 – __Município/UF:__ LAGOA SANTA / MG__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__MFS\-74653__

__IM27__

Código IBGE: __38625 – __Município/UF:__ LIMEIRA DO OESTE / MG__

A descrição funcional do módulo será: “O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica”

__MFS\-89469__

__IM28__

Código IBGE: __27306 – __Município/UF:__ LOUVEIRA / SP__

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica

__   MFS\-600391__

__IM29__

Código IBGE: __XXXXX – __Município/UF:__ Nome do Município / UF__

__Para cada município dessa lista deverá ser criado um modulo\.__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__SOCORRO__

__SP__

52106

__VARZEA PAULISTA__

__SP__

56503

__OURO PRETO__

__MG__

46107

__PARACATU__

__MG__

47006

A descrição funcional do módulo será: O NFe\-Cidades consiste na entrega das informações sobre os serviços tomados de prestador residente no país com nota fiscal e/ou prestados para pessoa física e jurídica\.

__ MFS\-1050929__

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

