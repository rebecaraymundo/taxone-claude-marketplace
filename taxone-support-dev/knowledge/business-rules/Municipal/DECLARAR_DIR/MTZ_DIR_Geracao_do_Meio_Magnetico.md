# MTZ_DIR_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DIR_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-19
- **Tamanho:** 133 KB

---

THOMSON REUTERS

Serviços Tomados 

Geração do Meio Magnético – Declarar DIR 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS4913

João Henrique de Araujo\.

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento ao município de Caçador através do novo validador Declarar DIR\.

MFS7309

João Henrique de Araujo

Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento do município de Itajaí\. Além da inclusão da TAG <NaturezadeOperacao> e Modelo Msaf x Modelo específicos para o município\.

CH23363\_2018 \(MFS\-21821\)

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento da TAG <CpfCnpj> da TAG <IdentificacaoPrestador> para considerar a TAG <Cpf> e a TAG <Cnpj> de acordo com a informação prestada, e tem como objetivo também de alterar o preenchimento da TAG <CodigoPais> da TAG <Servico> para considerar o código e não a sua descrição do país\.

MFS23198

Liliane V\. Assaf

Alterações:

>> Inclusão de críticas de campos obrigatórios e não preenchidos durante a geração\.

>> Inclusão do campo Código País do Prestador\.

>> Alteração na ordem dos campos Telefone e Email do Contato do Prestador\.

MFS24286

Andréa Rocha

Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento do município de Chapecó\. E inclusão das regras para a TAG <NaturezadeOperacao>\.

MFS32921

Andréa Rocha

Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento do município de Itajaí\. E inclusão das regras para a TAG <NaturezadeOperacao>\.

MFS36210

Andréa Rocha

Este documento tem como objetivo incluir a TAG <Competencia> e alterar a TAG <EnviarLoteDirEnvio> para o município de Itajaí\.

MFS37062

Andréa Rocha

Este documento tem como objetivo incluir a TAG <__ NaturezaOperacao__ > para o município de Itajaí\.

MFS29901

Andréa Rocha

Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento do município de Canoinhas\. E inclusão das regras para a TAG <NaturezadeOperacao> e <Competencia >\.

MFS61114

Rogério Ohashi

Alteração na regra de recuperação das notas fiscais para o município de __Itajaí/SC__\. \(__RN10\.a\)__

MFS81624

Alessandra Cristina Navatta

Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento do município de Balneário Camboriú\.

\(RN10, RN10a, RN11a, RN12a, RN22, RN24c, RN24e, RN35b, RN71, RN72\)

__Atenção: A RN10 foi excluída pois, de acordo com alinhamento interno envolvendo time e PO, ficou decidido que as regras de exclusão de notas eletrônicas serão tratadas de forma genérica e não específicas por município, diante disso, a RN10a passa a ser a regra atual \(para todos os municípios\)__

MFS86229

Rogério Ohashi

Este documento tem como objetivo alterar a regra de preenchimento da TAG <__ NaturezaOperacao__ > para o município de Balneário de Camboriú\.

MFS80513

Andréa Rocha

Alteração da regra de preenchimento da TAG <Discriminacao> para o município de Itajaí, seguindo as informações do layout de Itajaí\.

__MFS557532__

Rogério Ohashi

Este documento tem como objetivo de __retirar__ a regra de preenchimento da TAG <__CodigoPais__> específico para o município de Balneário de Camboriú\. \(Conforme arquivo modelo disponibilizado pela Prefeitura de Balneário Camboriú\)\.

__MFS557632__

Rogério Ohashi

Alteração da regra de preenchimento da TAG <Discriminacao> para o município de __Balneário Camboriú__, incluir na regra \(__RN46\.a__\), mesma regra de Itajaí\.

__MFS579474__

Rosemeire Santos

Este documento tem como objetivo ajustar as regras __\(RN37\)__ Valor ISS Retido, __\(RN39\)__ Base Cálculo e __\(RN40\)__ Alíquota de ISS para o município de Itajaí\.

__MFS621197__

Rosemeire Santos

Este documento tem como objetivo incluir o município de __Mafra/SC__, na geração do meio magnético de serviços tomados do validador Declarar DIR\.

__MFS\-735965__

Bruna Ribeiro 

Este documento tem como objetivo para o município de __Itajaí/SC__, definir o nome do arquivo para geração no Declarar DIR\.

__MFS\-884684__

Rosemeire Santos

Este documento tem como objetivo incluir o município de __Joinville/SC__, na geração do meio magnético de serviços tomados do validador Declarar DIR\.

__MFS\-829438      __

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1041458__

Alessandra Cristina Navatta

Ajuste na regra de preenchimento do campo __<ItemListaServico>__ dentro da TAG __<Servico>__, passando a considerar a parametrização definida na __TFIX85__ especificamente para o município de __Itajaí__\.

Caso não exista parametrização cadastrada na TFIX85, o sistema manterá o comportamento anterior, utilizando a informação do campo __COD\_SERV\_LEI\_116__\. \(RN46\)

__MFS\-1048308__

Alessandra Cristina Navatta

Este documento tem como objetivo incluir o município de __Iraní/SC__, na geração do meio magnético de serviços tomados do validador Declarar DIR\.

Retomar a nomenclatura do arquivo utilizada antes da alteração da MFS‑829438 para todos os municípios, exceto Itajaí‑SC\.      

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Regra para inclusão do novo módulo no Manager:__

__joinville__

O novo módulo Caçador deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Caçador: “Consiste na entrega das informações sobre os serviços tomados do município de Caçador”\.

__MFS4913__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “3006” \(Caçador\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Caçador, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS4913__

__RN03__

__Regra para geração do Meio Magnético:__

A geração do meio magnético deve ser feita no Framework\. Caso o usuário selecione mais de um estabelecimento na geração, o sistema irá gerar um arquivo para cada estabelecimento\. 

__MFS4913__

__RN04__

__Deverão ser criados os seguintes itens de menu e no módulo Declarar DIR:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
	- __Arquivo de Entradas de Serviços__
- Janela
- Ajuda

__MFS4913__

__RN05__

__Regras referentes ao padrão de codificação, declaração de namespace e encerramento do arquivo\.__

Adotou\-se a recomendação W3C para XML 1\.0 \(disponível em www\.w3\.org/TR/REC\-xml\) para a especificação dos documentos XML\. Com a codificação dos caracteres UTF\-8, todos os documentos deverão ser iniciados com a declaração:

<?xml version="1\.0" encoding="UTF\-8"?>

__Observação:__ Cada arquivo XML somente deverá conter uma declaração <?xml version="1\.0" encoding="UTF\-8"?>\.

__MFS4913__

__RN06__

__Regras referentes à otimização na montagem do arquivo__

Os documentos XML não deverão incluir:

• "zeros não significativos" para campos numéricos;

• "espaços" no início ou no final de campos numéricos e alfanuméricos;

• comentários no arquivo XML;

• anotação e documentação no arquivo XML \(TAG annotation e TAG documentation\);

• caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de

"espaço" entre as TAG’s\)\.

__  MFS4913__

__RN07__

__\[Alteração MFS\-1048308\] Regra p/ nomenclatura do arquivo magnético:__

O Arquivo deverá conter a seguinte nomenclatura:

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal, indicado abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAA__ onde:

__MMAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.XML

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNNdir\.xml__

__Onde:__

__AAAAMMDD:__ Indica a data padrão, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\) 

__NNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 10 \(dez\) posições, e finalizado pelo sufixo ”dir”\.

__DIR__: indica que o arquivo é de DIR \(Declaração Imposto Retido\)\.

__\.XML__: Extensão do arquivo\.

__Exemplo:__ Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome 20111224958367710001200000000013dir\.xml\.

__Observação\.: O número do lote não deverá ultrapassar o valor limite de 2\.147\.483\.000, devido a conversão de tipos numéricos\.__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ AAAAMMDD__ onde:

__AAAAMMDD__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_20100101\.XML

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNN\_MMAAAAdir\.xml__

__Onde:__

__AAAAMMDD:__ Indica a data padrão, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\)  

__NNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 10 \(dez\) posições, e finalizado pelo sufixo ”dir”\.

__\_MMAAAA: __mês e ano da competência referente à nota gerada\.

__DIR__: indica que o arquivo é de DIR \(Declaração Imposto Retido\)\.

__\.XML__: Extensão do arquivo\.

__Exemplo:__ Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome 20111224958367710001200000000013__\_072016__dir\.xml\.

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__Observações:__

O número do lote não deverá ultrapassar o valor limite de 2\.147\.483\.000, devido a conversão de tipos numéricos\.

__ __

__  __

__ __

__ MFS4913__

__MFS\-884684__

__MFS\-1048308__

__RN07\.a__

__Regra p/ nomenclatura do arquivo magnético para o município de Itajaí/SC:__

O Arquivo deverá conter a seguinte nomenclatura:

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNN\_MMAAAAdir\.xml__

__Onde:__

__AAAAMMDD:__ Indica a data padrão, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\)  

__NNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 10 \(dez\) posições, e finalizado pelo sufixo ”dir”\.

__\_MMAAAA: __Mês e ano do período de geração selecionado em tela\. 

__DIR__: indica que o arquivo é de DIR \(Declaração Imposto Retido\)\.

__\.XML__: Extensão do arquivo\.

__Exemplo:__ Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome 20111224958367710001200000000013__\_072016__dir\.xml\.

__Observação\.: O número do lote não deverá ultrapassar o valor limite de 2\.147\.483\.000, devido a conversão de tipos numéricos\.__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNN\_MMAAAAdir\.xml__

__Onde:__

__AAAAMMDD:__ Indica a data padrão, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\)  

__NNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 10 \(dez\) posições, e finalizado pelo sufixo ”dir”\.

__\_MMAAAA: __mês e ano da competência referente à nota gerada\.

__DIR__: indica que o arquivo é de DIR \(Declaração Imposto Retido\)\.

__\.XML__: Extensão do arquivo\.

__Exemplo:__ Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome 20111224958367710001200000000013__\_072016__dir\.xml\.

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__Observações:__

O número do lote não deverá ultrapassar o valor limite de 2\.147\.483\.000, devido a conversão de tipos numéricos\.

__MFS\-735965__

__RN08__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Número do Lote: __O campo deve permitir que o usuário digite o número do lote desejado, com no máximo 10 posições\. Este campo é de preenchimento __obrigatório__\. Caso o usuário não informe valor para este campo, o sistema deverá exibir a mensagem de preenchimento obrigatório\.

__Quebrar Arquivos por Data de Emissão:__ O campo deve ser um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Caçador, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS4913__

__RN09__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS4913__

__RG01__

__Regras Gerais para geração do Meio Magnético:__

A seguir serão descritas as formatações necessárias que serão seguidas para a geração correta da estrutura dos arquivos\. Este arquivo deve ser no formato __‘XML’__\.

__Data \(Date\)__

__Formato: AAAA\-MM\-DD onde:__

AAAA = ano com 4 caracteres

MM = mês com 2 caracteres

DD = dia com 2 caracteres

__Data/Hora \(datetime\)__

__Formato:__ __AAAA\-MM\-DDTHH:mm:ss onde:__

AAAA = ano com 4 caracteres

MM = mês com 2 caracteres

DD = dia com 2 caracteres

T = caractere de formatação que deve existir separando a data da hora

HH = hora com 2 caracteres

mm: minuto com 2 caracteres

ss: segundo com 2 caracteres

Exemplo:2011\-04\-30T08:22:56

__Valores Decimais \(Decimais\) __

__Formato: 0\.00__

Não deve ser utilizado separador de milhar\. O ponto \(\.\) deve ser utilizado para separar a parte inteira da fracionária\.

Exemplo:

48\.562,25 = 48562\.25

1,00 = 1\.00 ou 1

0,50 = 0\.50 ou 0\.5

__Valores Percentuais \(Decimais\) __

__Formato 0\.0000__

O formato em percentual presume o valor percentual em sua forma fracionária, contendo 5 dígitos\. O ponto \(\.\) separa a parte inteira da fracionária\.

Exemplo:

62% = 0\.62

150% = 1\.5

25,32 = 0\.2532

No layout os campos são identificados através do Tipo primitivo de dados utilizados pelo campo:

- __C__: Caracteres;
- __N:__ Número;
- __D:__ Data ou Data/Hora;

__Definição dos campos:__

__Campo Tipo Caracteres:__ Quando o campo for do tipo __“C”__, no layout a coluna __“Tamanho”__ define a quantidade máxima de caracteres que o texto poderá ter\.

__Campo tipo Numérico: __Quando o campo for do tipo__ “N”__, pode ser representado das seguintes formas:

- Número inteiro, que define o total de dígitos existentes no número\. Exemplo: “15” significa que o número poderá ter, no máximo, 15 dígitos;
- Número fracionário, que define o total de dígitos e quantos deles serão designados para a parte fracionária\. Exemplo: “15,2” significa que o número poderá ter, no máximo, 15 dígitos sendo 2 deles a identificação da parte fracionária\. A parte fracionária não é obrigatória quando assim definido;

__Campo tipo Data:__

Quando for data não haverá definição de tamanho;

__Observação:__ Todos os campos deverão obedecer ao tamanho e a formatação definidos pelo layout\.

__                      Os campos não obrigatórios devem desconsiderar as TAGS na geração, exceto a TAG <ValorIssRetido>\.__

__MFS4913__

__RN10__

__\[Excluída MFS81624\] Regra p/ Recuperação das notas fiscais de serviços tomados \(a geração será somente de serviços tomados no arquivo\)\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Não será considerado documento sem item\.

__MFS4913__

__MFS81624__

__RN10a__

__\[ALTERAÇÂO MFS81624\] A regra torna a ser genérica e não específica por município__

__Regra p/ Recuperação das notas fiscais de serviços tomados \(a geração será somente de serviços tomados no arquivo\) para o município de Itajaí/SC\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Não será considerado documento sem item\.

__\[ALTERAÇÃO\-MFS61114\]__ __Inclusão da regra para não recuperar as notas fiscais dos prestadores do mesmo município da geração __

- Não recuperar os documentos fiscais desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.

__MFS61114__

__MFS81624 MFS621197__

__MFS\-884684__

__MFS\-1048308__

__Layout de Conversão de DIR__

Geração do meio magnético

__RN11__

__Formato do arquivo__

O arquivo que será enviado deverá seguir o seguinte formato:

<?xml version="1\.0" encoding="UTF\-8" ?>

<EnviarLoteDirEnvio xmlns:ds= “[http://www\.w3\.org/2000/09/xmldsig\#](http://www.w3.org/2000/09/xmldsig) “xmlns:=" http://www\.publica\.inf\.br/dir">

<LoteDir versao="1\.00" id = “__iddd__”>

\.

\.

\.

\.

\.

</LoteDir>

</EnviarLoteDirEnvio>

   __ __

__MFS4913__

__RN11a__

__Formato do arquivo para o Município de Itajaí, Balneário Camboriú, Mafra, Joinville e Iraní__

O arquivo que será enviado deverá seguir o seguinte formato:

<?xml version="1\.0" encoding="UTF\-8" ?>

<EnviarLoteDirEnvio xmlns= "http://www\.publica\.inf\.br/dir">

<LoteDir versao="1\.00">

</LoteDir>

</EnviarLoteDirEnvio>

<EnviarLoteDirEnvio xmlns="http://www\.publica\.inf\.br/dir">

<LoteDir id="assinar" versao="1\.00">

<NumeroLote>5</NumeroLote>

<Cnpj>01362467000144</Cnpj>

<QuantidadeDir>1</QuantidadeDir>

<ListaDir>

<Dir>

<InfDir id="tcInfDir1">

<IdentificacaoDir>

<Numero>1</Numero>

<Serie>A1</Serie>

<Tipo>0</Tipo>

</IdentificacaoDir>

<DataEmissao>2014\-07\-28T00:00:01</DataEmissao>

<NaturezaOperacao>901</NaturezaOperacao>

<Competencia>2014\-04</Competencia>

<Status>1</Status>

<Servico>

<Valores>

<ValorServicos>1000\.00</ValorServicos>

<ValorDeducoes>5\.00</ValorDeducoes>

<ValorPis>1\.00</ValorPis>

<ValorCofins>2\.00</ValorCofins>

<ValorInss>3\.00</ValorInss>

<ValorIr>4\.00</ValorIr>

<ValorCsll>5\.00</ValorCsll>

<IssRetido>1</IssRetido>

<ValorIss>20\.00</ValorIss>

<ValorIssRetido>3\.00</ValorIssRetido>

<OutrasRetencoes>6\.00</OutrasRetencoes>

<BaseCalculo>980\.00</BaseCalculo>

<Aliquota>0\.02</Aliquota>

<ValorLiquido>995\.00</ValorLiquido>

<DescontoIncondicionado>7\.00</DescontoIncondicionado>

<DescontoCondicionado>8\.00</DescontoCondicionado>

<ValorProdutos>1000\.00</ValorProdutos>

</Valores>

<ItemListaServico>1\.01</ItemListaServico>

<Discriminacao>Analise de software</Discriminacao>

<CodigoMunicipio>4208203</CodigoMunicipio>

<CodigoPais>1058</CodigoPais>

</Servico>

<Tomador>

<IdentificacaoTomador>

<Cnpj>01362467000144</Cnpj>

</IdentificacaoTomador>

</Tomador>

<Prestador>

<IdentificacaoPrestador>

<CpfCnpj>

<Cnpj>03112402000176</Cnpj>

</CpfCnpj>

</IdentificacaoPrestador>

<RazaoSocial>EBA \- SISTEMAS E CONSULTORIA LTDA</RazaoSocial>

<Endereco>

<Endereco>Rua Icara</Endereco>

<Numero>151</Numero>

<Complemento>Novo complemento</Complemento>

<Bairro>Itoupava Seca</Bairro>

<CodigoMunicipio>4208203</CodigoMunicipio>

<Uf>SC</Uf>

<Cep>89035310</Cep>

</Endereco>

<Contato>

<Email>publica@publicainformatica\.com\.br</Email>

</Contato>

</Prestador>

</InfDir>

</Dir>

</ListaDir>

</LoteDir>

   __ __

__MFS36210__

__MFS81624 __

__MFS621197__

__MFS\-884684__

__MFS\-1048308__

__RN12__

__Regra para a Tag <LoteDir>__

Tag principal do arquivo, todas as outras tags deverão estar dentro do <LoteDir>

Dentro desta tag virá a versão “1\.00” id = “iddd”

__MFS4913__

__RN12a__

__Regra para a Tag <LoteDir> para o Município de Itajaí, Balneário Camboriú, Joinville e Iraní__

Tag principal do arquivo, todas as outras tags deverão estar dentro do <LoteDir>

Dentro desta tag virá a versão “1\.00”

__MFS36210__

__MFS81624__

__MFS\-884684__

__MFS\-1048308__

__RN13__

__Regra para o campo <NumeroLote> da TAG <LoteDir>__

Recuperar a informação preenchida pelo usuário no campo __Número do Lote __da tela de obrigações da geração do meio Magnético\.

__MFS4913__

__RN14__

__Regra para o campo <Cnpj> da TAG <LoteDir>__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 14

Campo Obrigatório

__MFS4913__

__RN15__

__Regra para o campo <QuantidadeDir> da TAG <LoteDir >__

Preencher com a quantidade de DIR geradas dentro da TAG \- <ListaDir> 

__MFS4913__

__RN16__

__Regra para o campo <ListaDir> da TAG <LoteDir>__

Tag para listar todas as notas fiscais\.

__MFS4913__

__RN17__

__Regra para o campo <Dir> da TAG <ListaDir>__

Tag para representar cada nota fiscal\.

__MFS4913__

__RN18__

__Regra para o campo <InfDir> da TAG <Dir>__

Tag para as informações da nota fiscal\.

__MFS4913__

__RN19__

__Regra para o campo <__<a id="_Hlk370509"></a>__IdentificacaoDir> da TAG <InfDir>__

Tag para identificação de cada nota fiscal\.

__MFS4913__

__RN20__

__Regra para o campo <Numero> da __<a id="_Hlk370542"></a>__TAG <IdentificacaoDir>__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__MFS4913__

__RN21__

__Regra para o campo <Serie> da TAG < IdentificacaoDir>__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 5

Campo Obrigatório\. 

__\[ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Caso a Série do Documento Fiscal \(SERIE\_DOCFIS da SAFX07\) não estiver preenchida, gerar a seguinte mensagem no log:

“Campo Série do Documento Fiscal deve ser preenchido”

As mensagens devem conter a identificação da chave do documento fiscal: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur\.

__MFS4913__

__RN22__

__Regra para o campo <Tipo> da TAG < IdentificacaoDir>__

__Modelo Msaf x Modelo \(Declarar DIR\):__

Nesse campo devem ser carregados os modelos, pertencentes ao município aderente ao validador DECLARAR DIR, que constam na TFIX83: 

0 – NFS\-e

1 – RPS

2 – Nota Fiscal Conjugada \(Mista\)

3 – Cupom

4 – NFS \(Convencional\)

__Modelo Msaf x Modelo \(Declarar DIR\) para o Município de Itajaí:__

Nesse campo devem ser carregados os modelos, pertencentes ao município aderente ao validador DECLARAR DIR, que constam na TFIX83: 

0 – NFS\-e

1 – RPS 

2 – Nota Fiscal Conjugada \(Mista\)

3 – Cupom Fiscal

4 – NF antiga \(em papel\)

5 – RPA Recibo de Pagamento a Autônomo

6 – Fatura

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__\[ ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Caso o Modelo do Documento Fiscal \(COD\_MODELO da SAFX07\) não esteja preenchido, gerar a seguinte mensagem no log:

“Campo Modelo do Documento Fiscal deve ser preenchido”

Caso o Modelo do Documento Fiscal  \(COD\_MODELO da SAFX07\) esteja preenchido, mas não haja parametrização de Modelo Msaf x Modelo da Declaração DIR, então gerar a seguinte mensagem no log:

“Para o Modelo ” || Código do Modelo da SAFX07|| “ do Documento, não foi localizada a parametrização de Modelo Msaf x Modelo\.'\);

“Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Modelo Msaf x Modelo\.”

As mensagens devem conter a identificação da chave do documento fiscal: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur\.

__MFS4913__

__MFS7309__

__MFS23198__

__MFS81624__

__RN23__

__Regra para o campo <DataEmissao> da TAG <InfDir>__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data \(Date\)

Campo Obrigatório\.

__\[ ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Caso a Data de Emissão do Documento Fiscal \(DATA\_EMISSAO da SAFX07\) não esteja preenchida, gerar a seguinte mensagem no log:

“Campo Data Emissão do Documento Fiscal deve ser preenchido”

As mensagens devem conter a identificação da chave do documento fiscal: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur\.

__MFS4913__

__MFS23198__

__RN24__

__Regra para o campo <NaturezaOperacao> da TAG <InfDir>__

Preencher com:

__‘904’ – \(Serviço imune, isento ou não tributado\):__

1. __Imune \- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.
2. __Isento ou não tributado \-__ Se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘901’ – \(ISS retido devido para Caçador\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘902’ – \(ISS retido para outro Município\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘903’ – \(ISS recolhido pelo prestador do serviço\)__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘905’__ __\- ISS retido devido para Caçador \(Simples Nacional\)__, se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘906’ – ISS retido devido para outro Município \(Simples Nacional\)__:__ __se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\. Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘907’ – ISS recolhido pelo prestador do Serviço \(optante Simples Nacional\):__ se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

Tipo: Numérico

Tamanho: 3

Campo Obrigatório\.

__\[ ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Se nenhuma das Naturezas da Operação for definida para o item de Serviço do Documento Fiscal, gerar a seguinte mensagem no log:

“Campo Natureza da Operação obrigatório e não gerado para o Documento Fiscal\. Rever parametrização de Classificação de Serviços no módulo Parâmetros para Município, assim como informações de retenção do ISS no Documento Fiscal”\.

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

__MFS4913__

__MFS23198__

__RN24a__

__Regra para o campo <NaturezaOperacao> da TAG <InfDir> para o Município de Itajaí__

Preencher com:

__‘901’ – ISS retido ou sujeito à substituição tributária, devido para Itajaí__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘902’ – ISS retido ou sujeito à substituição tributária, devido para outro município__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘921’ – ISS recolhido pelo prestador do serviço__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘931’ – Operação imune, isenta ou não tributada:__

__                                                                         __

1. __Imune \- __se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.
2. __Isento ou não tributado \-__ se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘951’__ __\- ISS retido ou sujeito à substituição tributária, devido para Itajaí \(Simples Nacional\)__, se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘952’ – ISS retido ou sujeito à substituição tributária, devido para outro município \(Simples Nacional\)__:__ __se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\. Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘971’ – ISS recolhido pelo prestador do serviço \(Simples Nacional\)__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

__‘981’ – Operação imune, isenta ou não tributada \(Simples Nacional\): __

1. __Imune \- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.
2. __Isento ou não tributado \-__ Se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘991’ – Nota Fiscal de Serviços Avulsa \(ISS pago antecipadamente pelo prestador: __não será tratado__\.__

Tipo: Numérico

Tamanho: 3

Campo Obrigatório\.

__Críticas:__

Se nenhuma das Naturezas da Operação for definida para o item de Serviço do Documento Fiscal, gerar a seguinte mensagem no log:

“Campo Natureza da Operação obrigatório e não gerado para o Documento Fiscal\. Rever parametrização de Classificação de Serviços no módulo Parâmetros para Município, assim como informações de retenção do ISS no Documento Fiscal”\.

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

Preencher com:

__‘101’ – \(ISS devido para Itajaí\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘111’ – \(ISS devido para outro Município\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘121’ – \(ISS Fixo \(Soc\. Profissionais\)\)__: se o campo IND\_CLASSE\_PFJ da tabela SAFX04 for = ‘06’\. 

__‘201’ – \(ISS Retido pelo tomador/intermediário\): __Não será tratado nessa MFS\.

__‘301’ – \(Operação imune, isenta ou não tributada\):__

__                                                                         __

1. __Imune \- __se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.
2. __Isento ou não tributado \-__ se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘501’__ __\- ISS devido para Itajaí \(Simples Nacional\)__, se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘511’ – ISS devido para outro Município \(Simples Nacional\): __Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__ __

__‘541’ – MEI \(Simples Nacional\)__: Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “452” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = ‘05\. E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘551’ – Escritório Contábil \(Simples Nacional\): __Não será tratado nessa MFS\.

__‘601’ – ISS Retido pelo tomador/intermediário \(Simples Nacional\):__ Não será tratado nessa MFS\.

__‘701’ – Operação imune, isenta ou não tributada \(Simples Nacional\): __

1. __Imune \- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.
2. __Isento ou não tributado \-__ Se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__MFS7309__

__MFS23198__

__MFS32921__

__MFS37062__

__RN24b__

__Regra para o campo <NaturezaOperacao> da TAG <InfDir> para o Município de Chapecó__

Preencher com:

__‘904’ – \(Serviço imune, isento ou não tributado\):__

1. __Imune \- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.
2. __Isento ou não tributado \-__ Se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘901’ – \(ISS retido devido para Chapecó\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘902’ – \(ISS retido devido para outro Município\)__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘903’ – \(ISS recolhido pelo prestador do serviço\)__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘905’__ __\- ISS retido devido para Chapecó \(Simples Nacional\)__, se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘906’ – ISS retido devido para outro Município \(Simples Nacional\)__:__ __se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\. Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘907’ – ISS recolhido pelo prestador do Serviço \(optante Simples Nacional\):__ se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

Tipo: Numérico

Tamanho: 2

Campo Obrigatório\.

__\[ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Se nenhuma das Naturezas da Operação for definida para o item de Serviço do Documento Fiscal, gerar a seguinte mensagem no log:

“Campo Natureza da Operação obrigatório e não gerado para o Documento Fiscal\. Rever parametrização de Classificação de Serviços no módulo Parâmetros para Município, assim como informações de retenção do ISS no Documento Fiscal”\.

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

__MFS24286__

__RN24c__

__Regra para o campo <NaturezaOperacao> da TAG <InfDir> para o Município de Canoinhas e Balneário Camboriú__

Preencher com:

__‘901’ – ISS retido devido no município__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘902’ – ISS retido devido para outro município__: se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\.

Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘921’ – ISS recolhido pelo prestador do serviço__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘931’ – Operação imune, isenta ou não tributada:__

__                                                                         __

1. __Imune \- __se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.
2. __Isento ou não tributado \-__ se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘951’__ __\- ISS retido ou sujeito à substituição tributária, devido para o município \(Simples Nacional\)__, se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado\.  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘952’ – ISS retido ou sujeito à substituição tributária, devido para outro município \(Simples Nacional\)__:__ __se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\. Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘971’ – ISS recolhido pelo prestador do serviço \(Simples Nacional\)__: se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

__‘991’ – Nota Fiscal de Serviços Avulsa \(ISS pago antecipadamente pelo prestador: __não será tratado__\.__

Tipo: Numérico

Tamanho: 3

Campo Obrigatório\.

__Críticas:__

Se nenhuma das Naturezas da Operação for definida para o item de Serviço do Documento Fiscal, gerar a seguinte mensagem no log:

“Campo Natureza da Operação obrigatório e não gerado para o Documento Fiscal\. Rever parametrização de Classificação de Serviços no módulo Parâmetros para Município, assim como informações de retenção do ISS no Documento Fiscal”\.

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

__MFS29901__

__   MFS81624__

__RN24d__

__Regra para o campo <NaturezaOperacao> da TAG <InfDir> Específico para o Município de Balneário Camboriú, Mafra, Joinville e Iraní__

Preencher com:

__‘901’ – ISS retido devido para__ __Balneário Camboriú:__ 

\- Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __E__ o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado __E __o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __igual__ ao campo COD\_MUNICIPIO da tabela de Estabelecimento\. __OU__ 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL __E__ o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __igual__ ao campo COD\_MUNICIPIO da tabela de Estabelecimento\.

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘902’ – ISS retido devido para outro município__: 

\- Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __OU__ 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\.

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘903’ – ISS recolhido pelo prestador do serviço:__ 

 \- Se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘904’ – Serviço imune, isento ou não tributado:__

1. __Imune: __

__\- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “07” __OU__ 

__\- __Se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município\.

1. __Isento ou não tributado:__

__ \-__  Se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV for maior que zero __OU__ 

__ \- __Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” __OU__

 

__ \-  __Se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros para Município\.

__‘905’__ __\- ISS retido devido para Balneário Camboriú \(Simples Nacional\)__: 

\- Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __E __o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __igual__ ao campo COD\_MUNICIPIO da tabela de Estabelecimento __OU__ 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ ao município do módulo selecionado __E __o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __igual__ ao campo COD\_MUNICIPIO da tabela de Estabelecimento\. 

 

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘906’ – ISS retido devido para outro Município \(Simples Nacional\)__:__ __

__\- __Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __OU__ 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __diferente__ do município do módulo selecionado\. 

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

__‘907’ – ISS recolhido pelo prestador optante Simples Nacional:__ 

\- Se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

__‘908’ – ISS retido devido para Balneário Camboriú – Prestado Fora: __

__\- __Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __E __o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ do município do módulo selecionado __E__ o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __diferente__ do campo COD\_MUNICIPIO da tabela de Estabelecimento\. __OU__ 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __diferente__ do campo COD\_MUNICIPIO da tabela de Estabelecimento\.

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “N”\.

__‘909’ – ISS recolhido pelo prestador do serviço – Prestado Fora:__ 

\- Se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “N”\.

__‘910’ – ISS recolhido pelo prestador optante – Prestado Fora \(Simples Nacional\):__

\- Se na capa do documento fiscal o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL e o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”\.

__‘911’ – ISS retido devido para__ __Balneário Camboriú – Prestado Fora \(Simples Nacional\):__

__\- __Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __E __o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for __igual__ do município do módulo selecionado __E__ o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __diferente__ do campo COD\_MUNICIPIO da tabela de Estabelecimento\. __OU__

 

\- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for __diferente__ do campo COD\_MUNICIPIO da tabela de Estabelecimento\.

  Verificar se o campo IND\_SIMPLES\_NAC da tabela SAFX04 é igual a “S”\.

Tipo: Numérico

Tamanho: 3

Campo Obrigatório\.

__Críticas:__

Se nenhuma das Naturezas da Operação for definida para o item de Serviço do Documento Fiscal, gerar a seguinte mensagem no log:

“Campo Natureza da Operação obrigatório e não gerado para o Documento Fiscal\. Rever parametrização de Classificação de Serviços no módulo Parâmetros para Município, assim como informações de retenção do ISS no Documento Fiscal”\.

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

__MFS86229__

__MFS621197__

__MFS\-884684__

__MFS\-1048308__

__RN25__

__Regra para o campo <Competencia> da TAG <InfDir> para o Município de Itajaí, Canoinhas, Balneário Camboriú, Mafra, Joinville e Iraní__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 7 \(formato AAAA\-MM\)

Campo Obrigatório\.

__MFS36210__

__MFS29901__

__MFS81624__

__MFS621197__

__MFS\-884684__

__MFS\-1048308__

__RN26__

__Regra para o campo <Status> da TAG <InfDir>__

Recuperar a informação do __\(campo 30\)__ SITUACAO da SAFX07:

Se__ “N”__ – Nota Fiscal não Cancelada, preencher com “1” \(Normal\)\.

Se__ “S”__ – Nota Fiscal regularmente cancelada, preencher com “2” \(Cancelado\)\.

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS4913__

__RN27__

__Regra para o campo <Servico> da TAG <InfDir>__

Tag para identificar item da nota fiscal\.

__MFS4913__

__RN28__

__Regra para o campo <Valores> da TAG <Servico>__

Tag para relacionar valores do item da nota fiscal\.

__MFS4913__

__RN29__

__Regra para o campo <ValorServicos> da TAG <Valores>__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.
- Se o campo VLR\_SERVICO estiver nulo, gravar o campo no arquivo com zero, pois o campo é obrigatório\.

Tipo: Numérico

Tamanho: 15,2

Campo Obrigatório\.

__MFS4913__

__RN30__

__Regra para o campo <ValorDeducoes> da TAG <Valores>__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN31__

__Regra para o campo <ValorPis> da TAG <Valores>__

Preencher com o somatório do campo VLR\_PIS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN32__

__Regra para o campo <ValorConfins> da TAG <Valores>__

Preencher com o somatório do campo VLR\_COFINS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN33__

__Regra para o campo <ValorInss> da TAG <Valores>__

Preencher com o somatório do campo VLR\_INSS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN34__

__Regra para o campo <ValorIr> da TAG <Valores>__

Preencher com o somatório do campo VLR\_TRIBUTO\_IR da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN35__

__Regra para o campo <ValorCsll> da TAG <Valores>__

Preencher com o somatório do campo VLR\_CSLL da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN36__

__Regra para o campo <IssRetido> da TAG <Valores> para os Municípios de Itajaí, Canoinhas, Balneário Camboriú, Mafra, Joinville e Iraní__

Se o campo <NaturezaOperacao> da TAG <InfDir> estiver preenchido com os códigos: ‘101’, ‘111’, ‘501’, e ‘511’, ‘901’, ‘902’, ‘905’, e ‘906’, ‘951’ e ‘952’, o campo <IssRetido> da TAG <Valores> deve ser preenchido com o valor ‘1’ \- \(Sim\)\. Caso o código seja diferente dos citados deve ser preenchido com o valor ‘2’ – \(Não\)\.

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS4913__

__MFS7309__

__MFS29901__

__MFS81624__

__MFS621197__

__MFS\-884684__

__MFS\-1048308__

__RN36a__

__Regra para o campo <IssRetido> da TAG <Valores> para os Municípios de Itajaí, Canoinhas e Balneário Camboriú__

Se o campo <NaturezaOperacao> da TAG <InfDir> estiver preenchido com os códigos: ‘101’, ‘111’, ‘501’, e ‘511’, o campo <IssRetido> da TAG <Valores> deve ser preenchido com o valor ‘1’ \- \(Sim\)\. Caso o código seja diferente dos citados deve ser preenchido com o valor ‘2’ – \(Não\)\.

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS7309__

__RN36b__

__Regra para o campo <IssRetido> da TAG <Valores> para os Municípios de Itajaí, Canoinhas, Balneário Camboriú e Mafra__

Se o campo <NaturezaOperacao> da TAG <InfDir> estiver preenchido com os códigos: ‘901’, ‘902’, ‘951’ e ‘952’, o campo <IssRetido> da TAG <Valores> deve ser preenchido com o valor ‘1’ \- \(Sim\)\. Caso o código seja diferente dos citados deve ser preenchido com o valor ‘2’ – \(Não\)\.

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS29901__

__MFS81624__

__MFS621197__

__RN37__

__Regra para o campo <ValorIss> da TAG <Valores>__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(12 posições\)”\.
- Se o campo VLR\_TRIBUTO\_ISS estiver nulo, gravar o campo no arquivo com zero, pois o campo é obrigatório\.

Tipo: Numérico

Tamanho: 12,2

__MFS4913__

__RN38__

__Regra para o campo <ValorIssRetido> da TAG <Valores>__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, caso o mesmo não esteja preenchido, preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV, quando o campo <IssRetido> for = ‘1’\. Caso contrário deverá preencher com ‘0’\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__MFS579474__

__RN39__

__Regra para o campo <OutrasRetencoes> da TAG <Valores>__

Preencher com o somatório dos campos VLR\_RET\_NF, VLR\_RET\_SERV da tabela FROM DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(12 posições\)”\.

Tipo: Numérico

Tamanho: 12,2

__MFS4913__

__RN40__

__Regra para o campo <BaseCalculo> da TAG <Valores>__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV, Se não estiver preenchido, preencher com o somatório do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Ou Se o campo VLR\_BASE\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros, preencher com o somatório dos campos VLR\_BASE\_ISS\_2, e ou VLR\_BASE\_ISS\_3 da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(12 posições\)”\.
- Se o campo VLR\_BASE\_ISS\_1, VLR\_BASE\_ISS\_RETIDO, VLR\_BASE\_ISS\_2, e ou VLR\_BASE\_ISS\_3, estiver nulo, gravar o campo no arquivo com zero, pois o campo é obrigatório\.

Tipo: Numérico

Tamanho: 12,2

Obrigatório

__MFS4913__

__MFS579474__

__RN41__

__Regra para o campo <Aliquota> da TAG <Valores>__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, \(campo 32 da SAFX09\) SE não tiver preenchido, preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

                                

__Tratamento:__

- Se o campo ALIQ\_TRIBUTO\_ISS estiver nulo, gravar o campo no arquivo com zero, pois o campo é obrigatório\.

*Observação:* Será preenchido com o tamanho máximo da tabela Mastersaf\.

Tipo: Numérico

Tamanho: 12,2

Obrigatório

__MFS4913__

__MFS579474__

__RN42__

__Regra para o campo <ValorLiquido> da TAG <Valores>__

Preencher com o somatório do campo VLR\_SERVICO menos o VLR\_PIS\_RETIDO, VLR\_COFINS\_RETIDO, VLR\_INSS\_RETIDO                VLR\_TRIBUTO\_IR, VLR\_CSLL da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(12 posições\)”\.

Tipo: Numérico

Tamanho: 12,2

Obrigatório

__MFS4913__

__RN43__

__Regra para o campo <DescontoIncondicionado> da TAG <Valores>__

Preencher com o campo VLR\_DESCONTO__ __da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN44__

__Regra para o campo <DescontoCondicionado> da TAG <Valores>__

Desconsiderar TAG\.

__MFS4913__

__RN45__

__Regra para o campo <ValorProdutos> da TAG <Valores>__

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

__MFS4913__

__RN46__

__Regra para o campo <ItemListaServico> da TAG <Servico>__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item ‘1’ da nota fiscal\.

Quando o código iniciar com zeros, desconsiderá\-los\.

*Exemplos:*

0001, deverá ficar igual a 1

0704, deverá ficar 704

Tipo: Alfanumérico

Tamanho: 4

Campo Obrigatório

__Observação:__ Quando a nota fiscal possuir mais de um item deverá ser listado na TAG <Discriminacao>

__\[ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Caso o campo COD\_SERVICO do Item de Serviço do Documento Fiscal não esteja relacionado ao Código da Lei 116 na SAFX2018, gerar a seguinte mensagem no log:

“Código do Serviço” || Código do Serviço do Documento Fiscal ||” sem informação do Código do Serviço da Lei 116 no Cadastro do Serviço \(SAFX2018\)\.”

As mensagens devem conter a identificação da chave do documento fiscal e do Item de Serviço: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur \+ Item de Serviço

__\[ALTERAÇÃO MFS\-1045814\]__ Específico para Município de Itajaí/SC:

Preencher com o campo Atividade da tela Parâmetros – Serviço Msaf x Atividade referente ao serviço cadastrado na nota fiscal\. De acordo com a TFIX85 \- Cadastro dos Códigos de Serviços Municipais \- PRT\_SERVICO\_OBRIG\. Caso não encontre a parametrização, considerar a regra geral \(informação do campo COD\_SERV\_LEI\_116\)\.

Tipo: Alfanumérico

Tamanho: 6

Campo Obrigatório

__MFS4913__

__MFS23198__

__MFS\-1045814__

__RN47__

__Regra para o campo <Discriminacao> da TAG <Servico>__

A discriminação será utilizada para descrever os demais itens do documento fiscal da seguinte forma:

Preencher com o conteúdo dos campos DSC\_SERV\_LEI\_116, COD\_SERV\_LEI\_116 da tabela \(DWT\_SERVICO\_LEI\_116\), ALIQ\_TRIBUTO\_ISS da tabela \(DWT\_ITENS\_SERV\), VLR\_SERVICO menos o VLR\_PIS\_RETIDO, VLR\_COFINS\_RETIDO, VLR\_INSS\_RETIDO, VLR\_TRIBUTO\_IR, VLR\_CSLL da tabela \(DWT\_ITENS\_SERV\), VLR\_DEDUCAO\_ISS da tabela \(DWT\_ITENS\_SERV\), VLR\_DESCONTO__ __da tabela \(DWT\_ITENS\_SERV\)\.

__Observação:__ Não serão considerados os seguintes itens: Quantidade e Desconto Condicionado;

*Exemplo: *

<Servico>

<Valores>\.\.\.</Valores>

<ItemListaServico></ItemListaServico>

<Discriminacao>\{\[\[Descricao=Descrição do item 1\]\[itemServico=102\]\[aliquota=0\.03\]\[Quantidade=2\]

\[ValorUnitario=2000\]\[Deducoes=0\]\[DescontoCondicionado=0\]\[DescontoIncondicionado=0\]\]

\[\[Descricao=Descrição do item 2\]\[itemServico=901\]\[aliquota=0\.04\]\[Quantidade=1\.6580\]\[ValorUnitario=150\.9880\]

\[Deducoes=5\.32\]\[DescontoCondicionado=8\.2\]\[DescontoIncondicionado=2\.99\]\]\}</Discriminacao>

<InformacoesComplementares></InformacoesComplementares>

<CodigoMunicipio></CodigoMunicipio>

<CodigoPais></CodigoPais>

</Servico>

Tipo: Alfanumérico

Tamanho: 2000

Campo Obrigatório

__MFS4913__

__RN47\.a__

__Regra para o campo <Discriminacao> da TAG <Servico> para o Município de Itajaí, Balneário Camboriú, Mafra, Joinville e Iraní__

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item ‘1’ da nota fiscal\.

Tipo: Alfanumérico

Tamanho: 2000

Campo Obrigatório

__Obs__\.: Quando a nota possuir mais de um item de serviço, devem ser mostradas as descrições de todos os serviços, desde que a descrição não seja igual, ou seja, forem de códigos de serviço da lei 116 diferentes\. As descrições devem ser separadas por um espaço em branco\.  Se o tamanho do total das descrições concatenadas ultrapassar 2000 caracteres, o conteúdo deve ser truncado\.

__MFS80513__

__MFS557632__

__MFS621197__

__MFS\-884684__

__MFS\-1048308__

__RN48__

__Regra para o campo <CodigoMunicipio> da TAG <Servico>__

Preencher com o Código do Município conforme Tabela IBGE\.

Concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

*Observação:* O município precisa ser devidamente cadastrado na Tabela de Município \(SAFX2097\)\.

__Tratamento:__

- O campo COD\_UF corresponde a 2 posições, enquanto o campo COD\_MUNICIPIO corresponde a 5 posições, se na tabela SAFX2097 o COD\_MUNICIPIO for menor que 5 posições, completar com zeros à esquerda\. *Exemplo:* Município Rio de Janeiro = 4557 deverá ficar 04557, a UF corresponde a 33, então o campo será preenchido com 3304557;
- Se o campo “Código do Município ISS” estiver vazio, deixar vazio e emitir a mensagem de log: “O município onde o serviço foi prestado não foi localizado, não será preenchido o Código IBGE do município de prestação do serviço”\.

Tipo: Numérico

Tamanho: 7

Campo Obrigatório\.

__MFS4913__

__RN49__

__Regra para o campo <CodigoPais> da TAG <Servico>__

__\[ALTERADA \- CH23363\_2018 \(MFS\-21821\)\]__

Preencher com o código do País de acordo com a tabela BACEN\. Deverá utilizar o campo COD\_PAIS \+ DIG\_VERIFICADOR da tabela PAIS, referente ao código do país cadastrado no campo COD\_PAIS da tabela SAFX04\.

Tipo: Numérico

Tamanho: 4

__MFS4913__

__CH23363\_2018 \(MFS\-21821\)__

__RN50__

__Regra para a Tag <Tomador>__

Tag para representar informações do Tomador\.

__MFS4913__

__RN51__

__Regra para a Tag <IdentificacaoTomador>__

Tag para representar informações da Identificação do Tomador\.

__MFS4913__

__RN52__

__Regra para o campo <Cnpj> da TAG <IdentificacaoTomador>__

Recuperar a informação do campo: CGC da tabela ESTABELECIMENTO\.

__MFS4913__

__RN53__

__Regra para a Tag <Prestador>__

Tag para representar informações do Prestador\.

__MFS4913__

__RN54__

__Regra para a Tag <IdentificacaoPrestador>__

Tag para representar informações da Identificação do Prestador\.

__MFS4913__

__RN55__

__Regra para a Tag <CpfCnpj> da TAG <IdentificacaoPrestador>__

Tag para representar informações do CPF/CNPJ do Prestador\.

__MFS4913__

__RN56__

__Regra para o campo <Cpf> ou <Cnpj> da TAG < CpfCnpj>__

Preencher a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ 

__\[ALTERADA \- CH23363\_2018 \(MFS\-21821\)\] __

Deve conter 11 \(para CPF\) e gerar uma TAG para identificação <Cpf> ou 14 \(para CNPJ\) e gerar uma TAG para identificação <Cnpj>\. 

Exemplo:

<CpfCnpj>

<Cpf>\.\.\.</Cpf>

</CpfCnpj>

ou

<CpfCnpj>

<Cnpj>\.\.\.</ Cnpj >

</CpfCnpj>

Tipo: Numérico

__\[ ALTERAÇÃO \- MFS23198\]__

__Tratamento:__

Para pessoas no Exterior \(situação especial na tabela\) será gravado a TAG como <Cpf>00000000000</Cpf>, pois o validador considera obrigatório\.

__Críticas:__

Caso o campo CFP\_CGC da X04\_PESSOA\_FIS\_JUR não estiver preenchido, gerar a seguinte mensagem no log:

“Campo CPF/CNPJ da Pessoa Fis/Jur deve ser preenchido”

As mensagens devem conter a identificação da chave do documento fiscal: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur\.

__MFS4913__

__CH23363\_2018 \(MFS\-21821\)__

__RN57__

__Regra para o campo <RazaoSocial> da TAG <Prestador>__

Preencher com a informação dos campos: RAZAO\_SOCIAL __\(Campo 05\)__ da tabela __X04\_PESSOA\_FIS\_JUR\. __

Tipo: Alfanumérico

Tamanho: 115

__MFS4913__

__RN58__

__Regra para a Tag <Endereco> da TAG <Prestador>__

Tag para representar informações do endereço do Prestador\.

__MFS4913__

__RN59__

__Regra para o campo <Endereco> da TAG <Endereco>__

Preencher com a informação do campo ENDERECO __\(campo 12\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Tipo: Alfanumérico

Tamanho: 125

__MFS4913__

__RN60__

__Regra para o campo <Numero> da TAG <Endereco>__

Preencher com a informação do campo NUM\_ENDERECO __\(campo 13\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Tipo: Alfanumérico

Tamanho: 10

__MFS4913__

__RN61__

__Regra para o campo <Complemento> da TAG <Endereco>__

Preencher com a informação do campo COMPL\_ENDERECO __\(campo 14\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Tipo: Alfanumérico

Tamanho: 60

__MFS4913__

__RN62__

__Regra para o campo <Bairro> da TAG <Endereco>__

Preencher com a informação do campo BAIRRO __\(campo 15\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Tipo: Alfanumérico

Tamanho: 60

__MFS4913__

__RN63__

__Regra para o campo <CodigoMunicipio> da TAG <Endereco>__

Preencher com o Código do Município conforme Tabela IBGE\.

Concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela __X04\_PESSOAL\_FIS\_JUR__\.

Tipo: Numérico

Tamanho: 7

__MFS4913__

__RN64__

__Regra para o campo <Uf > da TAG <Endereco>__

Preencher com a informação do campo UF __\(campo 19\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

__\[ ALTERAÇÃO \- MFS23198\]__

__Tratamento:__

Caso UF da tabela __X04\_PESSOAL\_FIS\_JUR __= EX, não gravar a tag <Uf>\.

Tipo: Alfanumérico

Tamanho: 2

__MFS4913__

__RN65__

__Regra para o campo <Cep> da TAG <Endereco>__

Preencher com a informação do campo CEP __\(campo 20\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Tipo: Numérico

Tamanho: 8

__\[ ALTERAÇÃO \- MFS23198\]__

__Críticas:__

Caso o CEP não tenha 8 posições, gerar a seguinte mensagem no log:

“O campo CEP deve conter oito posições”

As mensagens devem conter a identificação da chave do documento fiscal: Número, Série, Sub\-série, data fiscal, Pessoa Fis/Jur\.

__MFS4913__

__RN66__

__\[ALTERAÇÃO \- MFS23198\]__

__Regra para o campo <CodigoPais> da TAG <Endereco>__

Preencher com o código do País de acordo com a tabela BACEN\. Deverá utilizar o campo COD\_PAIS \+ DIG\_VERIFICADOR da tabela PAIS, referente ao código do país cadastrado no campo COD\_PAIS da tabela SAFX04\.

Tipo: Numérico

Tamanho: 4

__\[ALTERAÇÃO \- MFS557532/ MFS621197\] Retirar__ o município de Balneário Camboriú\.

__Obs\.:__ Conforme arquivo Modelo disponibilizado pela Prefeitura de Balneário Camboriú, não deve conter a TAG <CodigoPais> após a TAG <Cep>\. Foi efetuado alguns testes no validador junto com o cliente, e o arquivo apenas foi validado após a exclusão da TAG <CodigoPais> 

__MFS23198__

__MFS557532__

__MFS621197__

__RN67__

__Regra para o campo <Telefone> da TAG <Contato>__

Preencher com a informação do campo DDD __\(campo 22\)__ considerando as 3 primeiras posições \+ a informação do campo Telefone __\(campo 23\)__ considerando as 8 primeiras posições \(ignorar hífen\) da tabela __X04\_PESSOA\_FIS\_JUR__\.

*Observação: *O usuário deve cadastrar telefone comercial\.

Tipo: Alfanumérico

Tamanho: 11

__MFS4913__

__RN68__

__Regra para o campo <Email> da TAG <Contato>__

Preencher com a informação do campo E\_MAIL __\(campo 40\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Tipo: Alfanumérico

Tamanho: 80

__MFS4913__

__RN69__

__Regra para inclusão do novo módulo no Manager:__

__\[MFS32921\]__

__Itajaí__

O novo módulo Itajaí deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Itajaí: “Consiste na entrega das informações sobre os serviços tomados do município de Itajaí”\.

__Chapecó__

O novo módulo Chapecó deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Chapecó: “Consiste na entrega das informações sobre os serviços tomados do município de Chapecó”\.

__MFS7309__

__MFS24064__

__MFS32921__

__RN70__

__Regra para abertura do novo módulo no Manager:__

__\[MFS32921\]__

__Itajaí__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “8203” \(Itajaí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Itajaí, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__Chapecó__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “4202” \(Chapecó\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Chapecó, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS7309__

__MFS24064__

__MFS32921__

__RN71__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo Canoinhas deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Canoinhas: “Consiste na entrega das informações sobre os serviços tomados do município de Canoinhas”\.

__MFS29901__

__RN72__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “3808” \(Canoinhas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Canoinhas, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS29901__

__RN73__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo Balneário Camboriú deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Balneário Camboriú: “Consiste na entrega das informações sobre os serviços tomados do município de Balneário Camboriú”\.

__MFS81624__

__RN74__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “2008” \(Balneário Camboriú\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Balneário Camboriú, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS81624__

__RN75__

__Regra para inclusão do novo módulo no Manager:__

Módulo Mafra, já existente fica localizado no grupo “Municipal”\.

Descrição do módulo Mafra: “Consiste na entrega das informações sobre os serviços tomados do município de Mafra”\.

__MFS621197__

__RN76__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “10100” \(Mafra\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mafra, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS621197__

__RN77__

__Regra para abertura do módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “9102” \(Joinville\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Joinville, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS\-884684__

__RN78__

__Regra para abertura do módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “7809” \(Iraní\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Iraní, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS\-1048308__

