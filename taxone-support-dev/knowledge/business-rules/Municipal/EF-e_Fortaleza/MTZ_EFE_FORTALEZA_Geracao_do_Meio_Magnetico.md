# MTZ_EFE_FORTALEZA_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_EFE_FORTALEZA_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Municipal – Fortaleza

EF\-e Fortaleza

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1928

Julyana Perrucini

Este documento tem como objetivo tratar a geração do meio magnético para atendimento ao município de Fortaleza através do validador EF\-e\.

CH6990\_2016

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento do campo 30\-Código da Natureza da Operação\.

MFS\_2071

João Henrique 

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH13043\_2017

\(MFS\-12391\)

João Henrique

Este documento tem como objetivo não considerar as notas fiscais eletrônicas de fornecedores de dentro do município\.

CH14064\_2017

\(MFS\-12436\)

João Henrique

Este documento tem como objetivo incluir a parametrização de Classificação de Serviços por PFJ\.

MFS24480

Andréa Rocha

Este documento tem como objetivo aumentar o tamanho do campo razão social\.

MFS26332

Andréa Rocha

Este documento tem como objetivo passar a gerar as notas de prestadores de dentro do município\.

MFS27422

Andréa Rocha

Este documento tem como objetivo passar a utilizar o campo Número do Documento Fiscal de Serviço com até 60 posições\.

MFS61471

Andréa Rocha

Inclusão de um parâmetro para definir o conteúdo do campo “Descrição do Serviço”, conforme solicitação feita pelo cliente e avaliada com o setor de informação\. Incluir o tratamento para gerar somente um serviço por nota, conforme regra do validador\.

MFS898313

Andréa Rocha

Alteração da regra de preenchimento do campo 24\-CNAE \(Código da Classificação Nacional de Atividades Econômicas versão 2\.1\) da Atividade, para utilizar o código de atividade relacionado ao serviço\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O módulo “Fortaleza \-  EF\-e” deve manter localizado no grupo “Municipal”\. 

Descrição no Manager: “*Consiste na entrega das informações sobre os serviços tomados na EF\-e \(Escrituração Fiscal Eletrônica\) do município de Fortaleza\.*”\.

MFS1928

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “4400” \(Fortaleza\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Fortaleza, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS1928

__RN03__

__Estrutura de menus do módulo Fortaleza \- EF\-e para validador EF\-e:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Fortaleza \- EF\-e para validador EF\-e:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
- Janela

Ajuda

MFS1928

__RN04__

__Geração do Meio Magnético __

__Menu:__  Obrigações >> Geração do Meio Magnético

A geração do meio magnético deve ser feita no padrão Framework\.

Essa tela será composta pelas seguintes abas:

Parâmetros: o sistema deve exibir os parâmetros de entrada da geração\.

Processos: o sistema deve exibir os processos já executados para essa geração\.

Log de Processo: o sistema deve exibir o log gerado durante a geração\.

Arquivo: o sistema deve exibir o arquivo que será gravado\. 

Conferência do Meio Magnético: o sistema deve exibir um relatório de conferência das informações geradas no meio magnético\.

MFS1928

__RN05__

__Regra de criação do nome do arquivo__

Esse módulo gera apenas as notas fiscais de serviços tomados, pois a Importação de documentos de serviços prestados não está mais disponível na versão 2\.4 do validador\.

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_EFE\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

       __ST\_EFE:__ representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

       __MUNICIPIO:__ representa o município que está sendo gerado\.

       __DDMMAAAA:__ representa a data inicial da geração

       __\.txt:__ extensão do arquivo\.

Caso o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado deverá ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal;
- Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas e a nomenclatura desses arquivos deverão ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__ST\_EFE\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.txt__, onde:

     __ST\_EFE:__ representa a obrigação que está sendo gerada\.

__     MUNICIPIO: __representa o município para o qual está sendo gerado\.

     __DDMMAAAA:__ representa a data inicial da geração\.

__     MMAAAA:__ representa o mês da competência referente à nota gerada\.

    \.__txt:__ extensão do arquivo\.

Ex: ST\_EFE\_FORTALEZA\_01012010\_122009\.txt

MFS1928

MFS829438     

__RN06__

__Regra p/ tela da Geração do Meio Magnético__

__Menu:__  Obrigações >> Geração do Meio Magnético

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\. 

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar Arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__\[MFS61471\] __Inclusão de um parâmetro para definir o conteúdo do campo “Descrição do Serviço”

__Considerar a Descrição do Serviço da Lei 116/03:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Estabelecimento:__ neste campo devem ser listados todos os estabelecimentos que deverão ser considerados na geração do arquivo\.

MFS1928

MFS61471

__RN07__

__Regra do campo Estabelecimento da tela Obrigações – Meio Magnético:__

O sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS1928

__RN08__

__Regras referentes à formatação dos registros gerados no meio magnético__

- O arquivo deve ser gerado em formato texto \(txt\);
- Os campos devem vir separados por ponto e vírgula \(;\);
- Os campos que não tiverem definição de tamanho no layout serão considerados com o tamanho do conteúdo informado no campo em questão do MasterSAF\.

MFS1928

__RN09__

__Regra geral p/ recuperar serviços tomados __

O arquivo deve conter todas as notas com as seguintes características:

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento de Serviço e Mista \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou classificação do documento de Recebibos \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

*Observação:* 

- Arquivo conterá apenas informações de serviços tomados;
- Recuperar apenas notas fiscais com itens de serviços;

      __\[MFS61471\] __Inclusão de um parâmetro para definir o conteúdo do campo “Descrição do Serviço” e o tratamento pra gerar somente 

       um serviço por nota, conforme regra do validador\.

- Somente pode ser gerado um serviço por número de documento fiscal, mas pode\-se ter códigos de serviços diferentes cadastrados para um mesmo documento fiscal, desde que a descrição destes serviços seja a mesma, porque as informações serão agrupadas pela descrição do serviço\. Além da descrição do serviço, os registros serão agrupados por código da obra,  código ART, Código da Natureza da Operação, Alíquota e Indicador de ISS Retido\. Então quando houver mais de um serviço com a mesma descrição e os outros campos do agrupamento também estiverem iguais, os valores devem ser somados para se preencher os campos de valor \(ex\.: Valor do Serviço Prestado, Valor das Deduções\.\.\.\)\.  Entretanto, quando existir mais de um serviço a ser gerado por documento fiscal, ou seja, duas linhas a serem geradas para o mesmo número de documento fiscal, deve ser gerada somente uma linha e deve ser dada uma mensagem no log para o documento vinculado, mostrando as principais informações: “Existe mais de serviço cadastrado para o mesmo número de documento fiscal\.”\.

\[MFS26332\]

- Não considerar NFS\-e de Prestadores de dentro do município de Fortaleza, ou seja, quando a Pessoa Fis/Jur cadastrada na NFS\-e estiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR __Igual__ de Fortaleza\.
- Considerar NFS\-e de Prestadores de dentro do município de Fortaleza, ou seja, quando a Pessoa Fis/Jur cadastrada na NFS\-e estiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR __Igual__ de Fortaleza __E__ o campo Tipo de Documento \(campo 17\) for igual a 12 \- NFS\-e do município de Fortaleza, utilizando a parametrização para recuperar o tipo de documento \(menu Parâmetros >> Tipo Docto Msaf x Tipo Docto\), vide RN26\.

MFS1928

CH13043\_2017

MFS26332

MFS61471

__RN10__

__Regra p/ o campo 1\-Indicador da Versão do Layout__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 3\.

Gravar fixo: __2\.0__\.

MFS1928

__RN11__

__Regra p/ o campo 2\-Tipo da Prestação de Serviço__

Campo numérico de preenchimento obrigatório de tamanho máximo 1\.

Gravar fixo: __2__\. Referente a serviço tomado\.

MFS1928

__RN12__

__Regra p/ o campo 3\-Tipo de Pessoa Referente ao Prestador__

Campo numérico de preenchimento obrigatório sem definição de tamanho\.

Preencher com:

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 11 posições, indicando Pessoa Física;

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 14 posições, indicando Pessoa Jurídica;

3, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota estiver branco/nulo e o campo IND\_CONTEM\_COD da tabela X04\_PESSOA\_FIS\_JUR for igual a “4”, indicando Estrangeiro\.

MFS1928

__RN13__

__Regra p/ o campo 4\-CPF ou CNPJ do Prestador__

Campo numérico de preenchimento obrigatório de tamanho máximo 14\.

Preencher com o conteúdo do campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se estrangeiro deixar vazio\.

MFS1928

<a id="_Hlk433297870"></a>__RN14__

__Regra p/ o campo 5\-Nome ou Razão Social do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 115 150\.

Preencher com o conteúdo campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente <a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>a pessoa fis/jur cadastrada na nota\.

MFS1928

MFS24480

__RN15__

__Regra p/ o campo 6\-Inscrição Municipal do Prestador de Fortaleza__

Campo numérico de preenchimento não obrigatório de tamanho máximo 7\.

Preencher com o conteúdo do campo INSC\_MUNICIPAL da <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual ao município de “Fortaleza”\.

__Tratamento:__

- Se a IM for maior que 7 posições, deixar vazio, pois não é obrigatório\.

MFS1928

__RN16__

__Regra p/ o campo 7\-Código do País do Prestador__

Campo numérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo do campo PAIS\_COD\_BCB da tabela PAISES, referente ao código do país da pessoa fis/jur cadastrada na nota\. 

__Tratamento:__

- Desconsiderar os zeros da esquerda dos códigos cadastrados no campo PAIS\_COD\_BCB\.

MFS1928

__RN17__

__Regra p/ o campo 8\-Código da Unidade de Federação do Prestador__

Campo alfanumérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo do campo UF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

MFS1928

__RN18__

__Regra p/ o campo 9\-Código da Cidade do Prestador__

Campo numérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo dos campos \(concatenando\) “COD\_UF” \+ COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o código do município não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O código do município não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN19__

__Regra p/ o campo 10\-CEP do Prestador__

Campo numérico de preenchimento obrigatório de tamanho máximo 8\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o CEP não estiver preenchido no cadastro, será preenchido com zeros conforme a tabela origem e deve emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O CEP não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN20__

__Regra p/ o campo 11\-Nome do Logradouro do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 125\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o endereço não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN21__

__Regra p/ o campo 12\-Número do Endereço do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 10\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o número do endereço não estiver preenchido no cadastro, deixar vazio em branco e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Número do Endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

 

MFS1928

__RN22__

__Regra p/ o campo 13\-Complemento do Endereço do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 60\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o complemento do endereço não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Complemento do Endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN23__

__Regra p/ o campo 14\-Bairro do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 60\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o bairro do endereço não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Bairro do Endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN24__

__Regra p/ o campo 15\-Telefone do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 12\.

Preencher com o conteúdo dos campos \(concatenando\) DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Considerar para preenchimento os 2 dígitos da direita do DDD \(se tiver preenchido\) \+ espaço \+ 9 dígitos do telefone;
- Se o telefone do prestador não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Telefone do Prestador não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN25__

__Regra p/ o campo 16\-E\-mail do Prestador__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 80\.

Preencher com o conteúdo do campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__Tratamento:__

- Se o e\-mail do prestador não estiver preenchido no cadastro, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O e\-Mail do Prestador não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN26__

__Regra p/ o campo 17\-Tipo do Documento Digitado__

Campo numérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo do campo Tipo Documento da parametrização no módulo Municipal – Parâmetros para Município, item de menu Parâmetros >> Tipo Docto Msaf x Tipo Docto, referente ao tipo do documento cadastrado na nota\. 

__Tratamento:__

- Se o tipo do documento não estiver parametrizado, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Tipo do Documento não está cadastrado para NF do prestador em questão\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN27__

__Regra p/ o campo 18\-Número do Documento__

Verificar a parametrização \(Modulo: Básicos >> Parâmetros, Menu: Preliminares >> Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)\)

Se o campo __COD\_ESTAB__ selecionado na geração for __igual__ ao campo __COD\_ESTAB__ da parametrização __E__

     Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da parametrização __E__

     Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __

     Então preencher com o campo NUM\_DOCFIS\_SERV da tabela DWT\_DOCTO\_FISCAL \(campo 282 da SAFX07\)\.__ __

__Senão__

     Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

Campo numérico de preenchimento obrigatório de tamanho máximo 18\.

__Obs\.:__ Se for utilizado o campo NUM\_DOCFIS\_SERV e o tamanho for maior que 18 caracteres, o campo Número do Documento deve ser preenchido com as 18 primeiras posições e deve ser emitida a mensagem no log para o documento, mostrando as principais informações: “O Número do Documento ultrapassou o tamanho máximo permitido de 18 caracteres\. Campo de preenchimento obrigatório, favor verificar\.”\. 

MFS1928

MFS27422

__RN28__

__Regra p/ o campo 19\-Série do Documento__

Campo alfanumérico de preenchimento não obrigatório de tamanho máximo 10\.

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)\.

 

MFS1928

__RN29__

__Regra p/ o campo 20\-Data da Emissão do Documento__

Campo data de preenchimento obrigatório de tamanho máximo 10\.

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

__Tratamento:__

- Formato DD/MM/AAAA\.

MFS1928

__RN30__

__Regra p/ o campo 21\-Situação do Documento__

Campo numérico de preenchimento não obrigatório de tamanho máximo 1\.

Preencher com:

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) = ‘S’

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) <> ‘S’

MFS1928

__RN31__

__Regra p/ o campo 22\-Mês de Competência do Documento__

Campo numérico de preenchimento obrigatório de tamanho máximo 2\.

Preencher com o mês informado na data inicial da tela de geração do meio magnético\.

__Tratamento:__

- Formato “MM”\.
- Se o parâmetro “Quebrar Arquivo por Data de Emissão” estiver marcado deve ser considerado o mês da competência referente à nota gerada\.

MFS1928

__RN32__

__Regra p/ o campo 23\-Ano de Competência do Documento__

Campo numérico de preenchimento obrigatório de tamanho máximo 4\.

Preencher com o ano informado na data inicial da tela de geração do meio magnético\. 

__Tratamento:__

- Formato “AAAA”\.
- Se o parâmetro “Quebrar Arquivo por Data de Emissão” estiver marcado deve ser considerado o ano da competência referente à nota gerada\.

MFS1928

__RN33__

__Regra p/ o campo 24\-CNAE \(Código da Classificação Nacional de Atividades Econômicas versão 2\.1\) da Atividade__

__\[MFS898313\] __Utilização da atividade econômica referente ao código de serviço da nota

 

Campo numérico de preenchimento obrigatório de tamanho máximo 9\.

Preencher com o conteúdo do campo Atividade da parametrização no módulo Municipal – Parâmetros para Município, item de menu Parâmetros >> Atividade Msaf x Atividade, referente a atividade do serviço cadastrado na nota\. 

Preencher com o conteúdo do campo Atividade da parametrização no módulo Municipal – Parâmetros para Município, item de menu Parâmetros >> Atividade Msaf x Atividade, referente a atividade da pessoa fis/jur cadastrada na nota\. 

__Tratamento:__

- Se a atividade não estiver parametrizada, gerar com zero e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: 

“A Atividade Econômica do serviço em questão não está cadastrada\. Campo de preenchimento obrigatório, favor verificar\.”\.

“A Atividade Econômica do prestador em questão não está cadastrada\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

MFS898313

__RN34__

__Regra p/ o campo 25\-Alíquota__

Campo numérico de preenchimento não obrigatório de tamanho máximo 3\.

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula e formatar o valor da tabela DWT\_ITENS\_SERV de 000,0000 para 0,00, ou seja, se o contribuinte ultrapassar valor permitido que seja estabelecido por código de atividade, será de responsabilidade do mesmo tal informação\. Exemplos: o valor 4,31 ficaria 431, o valor 5,00 ficaria 500\. Então na tabela, se o valor 265,2222, entrar com 5,22 que ficaria 522 no arquivo\.

MFS1928

__RN35__

__Regra p/ o campo 26\-Descrição do Serviço__

Campo alfanumérico de preenchimento obrigatório de tamanho máximo 2000\.

__\[MFS61471\] __Inclusão de um parâmetro para definir o conteúdo do campo “Descrição do Serviço”

Se o parâmetro “Considerar a Descrição do Serviço da Lei 116/03” estiver marcado

     Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no 

     item da nota

Senão

     Preencher com o conteúdo do campo DESCRICAO da tabela X2018\_SERVICOS referente ao serviço cadastrado no item da nota\.

__Tratamento:__

- Caso o parâmetro esteja marcado e a descrição do serviço da Lei 116 não estiver preenchida, preencher com o conteúdo do campo DESCRICAO da tabela X2018\_SERVICOS\.
- Se a descrição do serviço da tabela X2018\_SERVICOS não estiver preenchida, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “A Descrição do Serviço não está cadastrada para o Serviço do prestador em questão\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

MFS61471

__RN36__

__Regra p/ o campo 27\-Código do País Onde Ocorreu a Prestação do Serviço__

Campo numérico de preenchimento obrigatório sem tamanho definido\.

Gravar fixo: __1058__\.

*Considerações:*

Será sempre fixo como Brasil porque o código do país, UF e de município do local de prestação são relacionados na validação da obrigação e não existe UF e municípios de outros países\.

MFS1928

__RN37__

__Regra p/ o campo 28\-Código da Unidade de Federação Onde Ocorreu a Prestação do Serviço__

Campo alfanumérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO referente o cadastro do município na X2097\_MUNIC\_ISS relacionado ao local de prestação do serviço da nota\.

__Tratamento:__

- Se o local de prestação não estiver preenchido, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “A UF não será considerada porque o local de prestação não foi preenchido na NF\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN38__

__Regra p/ o campo 29\-Código da Cidade Onde Ocorreu a Prestação do Serviço __

Campo numérico de preenchimento obrigatório sem tamanho definido\.

Preencher com o conteúdo dos campos \(concatenando\) “COD\_UF” \+ COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) referente o cadastro do município na X2097\_MUNIC\_ISS e estado relacionado ao local de prestação do serviço da nota\.

__Tratamento:__

- Se o local de prestação não estiver preenchido, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O município não será considerado porque o local de prestação não foi preenchido na NF\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1928

__RN39__

__Regra p/ o campo 30\-Código da Natureza da Operação__

Campo numérico de preenchimento obrigatório sem tamanho definido\.

__\[ALTERADA – CH6990\_2016\]__

Preencher com:

3, se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual  a “10”, caso não esteja preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”;

4, se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual  a “07”, caso não esteja preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”;

5, se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual  a “09”, caso não esteja preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”;

6, se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual  a “11”;

7, se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”;

1, se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços por Pessoa Fis/Jur ou por Município \(módulo Parâmetros para Município\) referente ao serviço e ao município do prestador \(Pessoa Fis/Jur\) cadastrado na nota fiscal, mais o código do prestador \(em casos de parametrização por Pessoa Fis/Jur\) com o COD\_PARAM = “471”, caso não esteja cadastrado verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão\. Se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento;

2, se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços por Pessoa Fis/Jur ou por Município \(módulo Parâmetros para Município\) referente ao serviço e ao município do prestador \(Pessoa Fis/Jur\) cadastrado na nota fiscal, mais o código do prestador \(em casos de parametrização por Pessoa Fis/Jur\) com o COD\_PARAM = “472”, caso não esteja cadastrado verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão\.

MFS1928

CH6990\_2016

CH14064\_2017

__RN40__

__Regra p/ o campo 31\-Código ART__

Campo alfanumérico de preenchimento não obrigatório de tamanho máximo 15\.

Se campo IND\_TP\_SERVICO da X2018\_SERVICOS referente o serviço cadastrado na nota for igual a “1”, preencher com o conteúdo do campo Código ART da tela de cadastro de Canal de Distribuição/Obra, localizado em Básicos >> MasterSAF DW >> Manutenção >> Cadastros referente a obra cadastrada na nota\.

MFS1928

__RN41__

__Regra p/ o campo 32\-Código da Obra__

Campo alfanumérico de preenchimento não obrigatório de tamanho máximo 15\.

Se campo IND\_TP\_SERVICO da X2018\_SERVICOS referente o serviço cadastrado na nota for igual a “1”, preencher com o conteúdo do campo COD\_CANAL\_DISTRIB da DWT\_DOCTO\_FISCAL \(campo 81 da SAFX07\)\. A obra será recuperada da nota fiscal devendo ser cadastrada no Canal de Distribuição/Obra, localizado em Básicos >> MasterSAF DW >> Manutenção >> Cadastros referente a obra cadastrada na nota\.

MFS1928

__RN42__

__Regra p/ o campo 33\-Valor do Serviço Prestado__

Campo valor de preenchimento obrigatório de tamanho máximo 19\.

Preencher com o conteúdo campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV \(campo 14 da SAFX09\)\.

__Tratamento:__

- Se o valor do serviço não estiver preenchido, deixar vazio e emitir a mensagem no log para o documento vinculado, mostrando as principais informações: “O Valor do Serviço não foi preenchido na NF\. Campo de preenchimento obrigatório, favor verificar\.”;
- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN43__

__Regra p/ o campo 34\-Valor das Deduções__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN44__

__Regra p/ o campo 35\-Descontos Incondicionados__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Deixar vazio\. Não será tratado nessa MFS\.

MFS1928

__RN45__

__Regra p/ o campo 36\-Descontos Condicionados__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Deixar vazio\. Não será tratado nessa MFS\.

MFS1928

__RN46__

__Regra p/ o campo 37\-Outras Retenções__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com a soma do conteúdo dos campos VLR\_TOT\_RET, VLR\_RET\_NF e VLR\_RET\_SERV da tabela DWT\_ITENS\_SERV \(campos 93, 95 e 96 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN47__

__Regra p/ o campo 38\-Valor IR__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_IR da tabela DWT\_ITENS\_SERV \(campo 31 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN48__

__Regra p/ o campo 39\-Valor PIS__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_PIS da tabela DWT\_ITENS\_SERV \(campo 48 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN49__

__Regra p/ o campo 40\-Valor COFINS__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_COFINS da tabela DWT\_ITENS\_SERV \(campo 51 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN50__

__Regra p/ o campo 41\-Valor CSLL__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_CSLL da tabela DWT\_ITENS\_SERV \(campo 45 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN51__

__Regra p/ o campo 42\-Valor INSS__

Campo valor de preenchimento não obrigatório de tamanho máximo 19\.

Preencher com o conteúdo do campo VLR\_INSS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 78 da SAFX09\)\.

__Tratamento:__

- Desconsiderar pontos ou vírgula\. Exemplos: o valor 3,12 ficaria assim: 312\. O valor 5\.570,00 ficaria 557000\.

MFS1928

__RN52__

__Regra p/ o campo 43\-Número do Empenho__

Campo numérico de preenchimento não obrigatório sem tamanho definido\.

Deixar vazio\. Não será tratado nessa MFS\.

MFS1928

__RN53__

__Regra p/ o campo 44\-Indicador de ISS Retido__

Campo numérico de preenchimento não obrigatório sem tamanho definido\.

Preencher com:

1 \(SIM\), quando pelo menos uma das seguintes opções for verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “1”;
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS for igual “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO;
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido\.

Senão, preencher com 0 \(NÃO\)\.

MFS1928

__RN54__

__Regra p/ o campo 45\-Tipo de Tributação do Tomador__

Campo numérico de preenchimento não obrigatório sem tamanho definido\.

Deixar vazio\. \(Esse campo não é mais utilizado\. Não é necessário o preenchimento\)\.

MFS1928

__RN55__

__Regra p/ o campo 46\-Inscrição Municipal de Fortaleza do Contribuinte que está escriturando__

Campo numérico de preenchimento não obrigatório sem tamanho definido\.

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente o Estabelecimento selecionado na geração do arquivo magnético\.

MFS1928

__RN56__

__Regra p/ o campo 47\-Valor Bruto do Serviço\*__

INFOLEGIS 171/14 – H\.

Não será tratado porque esse campo deve ser preenchido somente por contribuinte que está escriturando e que seja do Regime de Caixa \(Exemplo Administração Pública Direta\)\. Orientação pela Prefeitura em deixá\-lo em branco ou não o informar e optamos por não informar\.

MFS1928

__RN57__

__Regra p/ o campo 48\-__ __Data do Pagamento\*__

INFOLEGIS 171/14 – H\.

Não será tratado porque esse campo deve ser preenchido somente por contribuinte que está escriturando e que seja do Regime de Caixa \(Exemplo Administração Pública Direta\)\. Orientação pela Prefeitura em deixá\-lo em branco ou não o informar e optamos por não informar\.

MFS1928

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

