# MTZ_SIAP_NET_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_SIAP_NET_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-02-26
- **Tamanho:** 126 KB

---

THOMSON REUTERS

	

Municipal 

 Serviços Tomados e Prestados 

Geração do Meio Magnético \- SIAP\. NET	

#####                                               DOCUMENTO DE REQUISITO	

__MFS/CH__

__Nome__

__Descrição__

MFS9232

João Henrique de Araujo\.

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados e prestados em atendimento ao novo validador SIAP\. NET\. 

CH10136\_2017 \(MFS11411\)

Julyana Perrucini

Este documento tem como objetivo alterar a extensão do arquivo de\.TXT para\.CSV\.

CH10136\_2017

\(MFS11926\)

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento dos dados de cadastro do prestador para Serviços Tomados, pois atualmente está gerando incorreto com os dados do tomador\.

MFS\-15537

João Henrique de Araujo\.

Este documento tem como objetivo incluir o município de Guaratinguetá\-SP no validador SIAP\.NET\.

MFS\-20832

João Henrique de Araujo\.

Este documento tem como objetivo incluir o município de Lorena\-SP no validador SIAP\.NET\.

CH23992\_2018

\(MFS\-21537\)

João Henrique de Araujo\.

Esse documento tem como finalidade alterar o tratamento do campo “Código de Atividade” para o Município de Lorena\-SP, possibilitando que o cliente parametrize a informação na geração do arquivo magnético para as notas fiscais\.

MFS29900

Alessandra Cristina Navatta

Este documento tem como objetivo incluir o município de Santarém\-PA no validador SIAP\.NET

MFS48836

Andréa Rocha

Este documento tem como objetivo incluir o município de Jacareí\-SP no validador SIAP\.NET

MFS\-67609

Alessandra Cristina Navatta

Incluir na geração do arquivo um header \(1ª linha do arquivo magnético\) e ajustar o formato dos campos de tipo alfanuméricos para o município de Jacareí\-SP\.

MFS\-67609

Alessandra Cristina Navatta

Para o município de Jacareí\-SP, foi necessário alterar a regra de formatação do arquivo \(RN07\)\. Nesta demanda, para o município de Jacareí, a formatação do arquivo deve ser conforme regras da RN07\.A, que indica que a separação dos campos é por vírgula \(‘,’\) e os campos não possuem posições fixas \(não deve ser incluído espaços para completar o total das posições\) 

MFS\-71570

Andréa Rocha

Alterar a regra de geração do campo Data da Prestação do Serviço, para tratar para a situação em que a data fiscal é maior que a data de emissão da nota fiscal, causando erro no validador para notas fiscais de entrada\.

MFS80582

Andréa Rocha

Alterar a recuperação das informações de Serviços Tomados para o município de Jacareí, que passa considerar apenas Notas Fiscais de Serviços prestados de outros municípios\.

MFS88576

Rogério Ohashi

Tratamento na regra de geração do campo Série NF, para recuperar a informação do parâmetro “Série MSAF x Série” da Tela de Parâmetros por Município, para só depois recuperar da Nota Fiscal, alteração padrão para todos os Municípios\.

MFS99542

Andréa Rocha

Incluir na geração do arquivo um header \(1ª linha do arquivo magnético\) e ajustar o formato dos campos de tipo alfanuméricos para o município de Pindamonhangaba\-SP\.  A formatação do arquivo deve ser conforme as regras da RN07\.A, que indica que a separação dos campos é por vírgula \(‘,’\) e os campos não possuem posições fixas \(não deve ser incluído espaços para completar o total das posições\)\.  Vai ser utilizada a mesma regra do município de Jacareí, conforme os testes feitos para o validor de Pindamonhangaba\.

MFS535351

Rogério Ohashi

Tratamento na regra de geração do campo Código de Município, para complementar com zeros, a informação do Campo de Município, até complementar 5 posições, conforme tabela IBGE\.

MFS538782

Rogério Ohashi

Este documento tem como objetivo incluir o Município de Pindamonhangaba na Regra específica do Município de Lorena para o de campo Código da Atividade\. \(RN30\)\.

MFS567586

Rosemeire Santos

Tratamento na regra de geração do campo "Código do Município onde o Serviço foi Prestado", para complementar com zeros, até complementar 5 posições, conforme tabela IBGE e exigência do validador do município de Pindamonhangaba\.

MFS\-778546

Rosemeire Santos 

Este documento tem como objetivo incluir o município de IBIRITÉ/MG no validador SIAP\.NET

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

MFS929421

Andréa Rocha

Alteração de regra de preenchimento do campo “Inscrição Cadastral Municipal Própria” para a geração do arquivo de construção civil\.

MFS937915

Andréa Rocha

Alteração de regra de preenchimento dos campos “Valor ISS” e “Alíquota”, para recuperar o valor e alíquota do ISS retido, quando o valor e alíquota de ISS não estiverem preenchidos\.

MFS1003747

Klemer de Monteiro

Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão”, para Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)

__MFS\-1046420__

Rosemeire Santos

Este documento tem como objetivo incluir os municípios de Arapei/SP, Bananal/SP, Biritiba Mirim/SP, Cachoeira Paulista/SP, Canas/SP, Pedro De Toledo/SP, Queluz/SP, Redencao Da Serra/SP, Roseira/SP, Salesopolis/SP, Santa Branca/SP, Silveiras/SP no validador SIAP\.NET

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__          MSF/CH__

__RN01__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo “Pindamonhangaba” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “Consiste na entrega das informações sobre os serviços tomados e prestados do município de Pindamonhangaba”\.__

__MFS9232__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “38006” \(Pindamonhangaba\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Pindamonhangaba, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS9232__

__RN03__

__Estrutura de menus do módulo:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS9232__

__MFS29900__

__RN04__

__Regra de nomenclatura do arquivo:__

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__\[ALTERADA \- CH10136\_2017 \(MFS11411\) / MFS1003747\] \- __Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão”, para Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.CSV__, onde:

__MMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.CSV__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.CSV

__       SIAPNET\_MUNICIPIO\_DDMMAAAA\.CSV TXT__, onde:

       __SIAPNET__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.CSV TXT__: extensão do arquivo\.

*Exemplo:* SIAPNET\_PINDAMONHANGABA\_01012010\.CSV TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.CSV__, onde:

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.CSV__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.CSV

__       SIAPNET\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.CSV TXT__, onde:

__        SIAPNET__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.CSV TXT__: extensão do arquivo\.

Ex: SIAPNET\_PINDAMONHANGABA\_01012014\_122013\.CSV TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS9232__

__CH10136\_2017 \(MFS11411\)__

__MFS29900__

__MFS829438  
MFS1003747__

__RN05__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Menu:__  Obrigações >> Geração do Meio Magnético:

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Gerar Serviços Tomados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. Quando a opção “Gerar Serviços Tomados” não estiver selecionada, deve ser desabilitado\. \(Opções S = Marcado e N = Desmarcado\)\.

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Gaspar, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS9232__

__MFS29900__

__RN06__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS9232__

MFS29900

__RN07__

__Regras para geração do Meio Magnético:__

__\[ALTERADA \- CH10136\_2017 \(MFS11411\)\]__

__Regras referentes à formatação dos registros gerados no meio magnético:__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

O arquivo gerado para importação deve ser no formato __‘CSV’__ __‘TXT’\.__

- Deve ser usado o separador ponto e vírgula \(;\) para separar as informações de cada campo\.
- Campo Caractere: Devem ser alinhados a esquerda\. Preencher com espaços em branco à direita, caso seja necessário ou não possua informação\.
- Campo Numérico: Devem ser alinhados a direita\. Preencher com zeros à esquerda caso seja necessário ou não possua valor

__MFS9232__

__CH10136\_2017 \(MFS11411\)__

__MFS29900__

__RN07\.A__

__Regras para geração do Meio Magnético para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei/SP, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

O arquivo gerado para importação deve ser no formato __‘CSV’\.__

- Deve ser usado o separador vírgula \(,\) para separar as informações de cada campo\.
- Os campos não possuem tamanho fixo \(não deve ser incluído espaços para completar as posições\)

__Observações Importantes:__ Para o município de Jacareí, o arquivo CSV deve gerar sem as aspas\.

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN08__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = S\);
- Não será considerado documento sem item;

__MFS9232__

__MFS15537__

__MFS29900__

__RN08\.A__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados para os municípios de Guaratinguetá, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = S\);
- Não será considerado documento sem item;
- Não considerar NFS\-e de Prestadores de dentro do município de Guaratinguetá, ou seja, quando a Pessoa Fis/Jur cadastrada na NFS\-e estiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR __Igual__ de Guaratinguetá\.

__MFS15537__

__MFS\-1046420__

__RN08\.B__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados para o município de Jacareí__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = S\);
- Não será considerado documento sem item;
- Não considerar NFS\-e de Prestadores de dentro do município de Jacareí, ou seja, quando a Pessoa Fis/Jur cadastrada na NFS\-e estiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR __Igual__ de Jacareí\.

__MFS80582__

__RN09__

__Regra p/ Recuperação das notas fiscais de Serviços Prestados__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\);
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = S\);
- Não será considerado documento sem item;

__MFS9232__

__MFS29900__

__HEADER__

__\[MFS48836__/__ MFS99542\] __Inclusão do Header para os municípios de __Jacareí e Pindamonhangaba\.__

A primeira linha do arquivo deve ser o header \(contendo os labels entre aspas e caracteres de separação conforme indicado abaixo\):

"Indicador de Tipo de Serviço","Número NF","Série NF","Data Prestação de Serviço","Data Emissão da NF","Status NF","Documento CPF/CNPJ","Inscrição Mobiliária","Razão Social","Endereço","Número","Complemento","Bairro","Código do Município","Código do País","Cep","Telefone","Email","Tributada","Código do Município onde o Serviço foi Prestado","Código da Atividade","Código da Lista de Serviços",Discriminação,"Valor NF","Valor Deduções","Valor Desconto Condicionado","Valor Desconto Incondicionado","Valor INSS","Valor Csll","Valor Outras Retenções","Valor Pis","Valor Cofins","Valor Ir","Valor Iss","Prestador Optante Simples Nacional",Alíquota,"Código da Obra","Código ART","Inscrição Própria","Código do Benefício"\.

__\[MFS\-778546/ MFS\-1046420\]__ Inclusão do Header para os municípios de __Ibirité__, __Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras__

A primeira linha do arquivo deve ser o header \(contendo os labels entre aspas e caracteres de separação conforme indicado abaixo\):

"Indicador de Tipo de Serviço","Número NF","Série NF","Data Prestação de Serviço","Data Emissão da NF","Status NF","Documento CPF/CNPJ","Inscrição Mobiliária","Razão Social","Endereço","Número","Complemento","Bairro","Código do Município","Código do País","Cep","Telefone","Email","ISS Retido no Tomador","Código do Município onde o Serviço foi Prestado","Código da Atividade","Código da Lista de Serviços",”Discriminação”,"Valor NF","Valor Deduções","Valor Desconto Condicionado","Valor Desconto Incondicionado","Valor INSS","Valor Csll","Valor Outras Retenções","Valor Pis","Valor Cofins","Valor Ir","Valor Iss","Prestador Optante Simples Nacional",”Alíquota”,"Código da Obra","Código ART","Inscrição Própria", " Código do Benefício "\.

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN10__

__Regra para o campo Indicador de Tipo de Serviço:__

Preencher com:

__ ‘P’__ \- NF de serviço de Serviço Prestado quando o campo __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __= ‘9’__

__ ‘T’__ \- NF de serviço de Serviço Tomado quando o campo __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __<> ‘9’__

Campo obrigatório\.

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS9232__

__RN11__

__Regra para o campo Número NF:__

Preencher com a informação do campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__ __\(campo 08 da SAFX07\)__

__Tratamento:__ Somente números, sem pontos\.

Campo obrigatório\.

Formato: 9999999999 

Tamanho: 10 posições

Tipo: Numérico

__MFS9232__

__RN12__

__Regra para o campo Série NF:__

 __Preencher__ com o campo Série da tela de Parâmetros por Município – Série Msaf x Série, associado à série informada na nota fiscal \(campo __SERIE\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__\)\.

__    Se __o campo não for preenchido, devido não existir o parâmetro\. \(“Série Msaf x Série”\)

__Preencher__ com a informação do campo __SERIE\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)__

__  Se__ o campo __*ainda não for preenchido*__, informar no log a seguinte mensagem: “O campo de Série NF é obrigatório, efetue a parametrização da Série na tela de “Série Msaf x Série”\. Localização: Módulo: Municipal à Parâmetro por Município à Menu: Parâmetros à Série Msaf x Série\.  Dados do Registro: NF de Saída – Número NF: 0000 – Série NF: 000 – Data fiscal: dd/mm/aaaa\. 

      

__Tratamento:__ Letras, números, sem pontos, sem traços e sem espaços\.

__Campo obrigatório\.__

Formato: XXXXX 

Tamanho: 5 posições

Tipo: Alfanumérico

__MFS9232__

__MFS88576__

__RN13__

__Regra para o campo Data Prestação de Serviço:__

__\[MFS71570\] Tratamento para a situação em que a data fiscal é maior que a data de emissão da nota fiscal__

      Preencher com a informação do campo __DATA\_FISCAL__ da tabela __DWT\_DOCTO\_FISCAL__

      Preencher com a informação do campo __DATA\_EMISSAO__ da tabela __DWT\_DOCTO\_FISCAL__

__Tratamento:__ Letras, números, sem pontos, sem traços e sem espaços\. Esse campo sempre deverá ser preenchido com 10 posições\.

Campo obrigatório\.

Formato: dd/mm/aaaa 

Tamanho: 10 posições

Tipo: Data

__MFS9232__

__MFS71570__

__RN14__

__Regra para o campo Data da Emissão da NF:__

Preencher com a informação do campo __DATA\_EMISSAO__ da tabela __DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)__

__Tratamento: __exemplo 02/05/2012

Campo obrigatório\.

Formato: dd/mm/aaaa 

Tamanho: 10 posições

Tipo: Data

__MFS9232__

__RN15__

__Regra para o campo Status da NF:__

Preencher com a informação do campo __SITUACAO__ da tabela __DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\):__

Se__ “N”__ – Nota Fiscal NÃO cancelada, preencher com __“1” \(Normal\)__

Se__ “S”__ – Nota Fiscal regularmente cancelada, preencher com __“2” \(Cancelada\)__

*Observação:* De acordo com o layout da prefeitura as Notas Extraviadas não devem ser importadas através do arquivo\. Serão informadas em um menu específico no site da prefeitura\. 

Campo obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS9232__

__RN16__

__Regra para o campo Documento CPF/CNPJ:__

__ATENÇÃO:__ Regra invertida nesse campo:

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo CPF\_CGC __\(campo 06 da tabela SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo CPF\_CGC __\(campo 06 da tabela SAFX04\) __CGC da tabela ESTABELECIMENTO

__Tratamento: __Somente números, sem pontos, sem traços\.

Formato: CPF: 99999999999 \(11 dígitos\) e CNPJ: 99999999999999 \(14 dígitos\) 

Tamanho: 14 posições

Tipo: Numérico

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__RN17__

__Regra para o campo Inscrição Mobiliária:__

__ATENÇÃO:__ Regra invertida nesse campo:

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo INSC\_MUNICIPAL __\(campo 09 da tabela SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo INSC\_MUNICIPAL __\(campo 09 da tabela SAFX04\) __INSC\_MUNICIPAL da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 20 posições

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se não existir, gerar nulo\. Caso exista, a informação deve ser sem formatação, porém entre aspas\. 

Formato: "XXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN18__

__Regra para o campo Razão Social:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo RAZAO\_SOCIAL __\(Campo 05 da tabela SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo RAZAO\_SOCIAL __\(Campo 05 da tabela SAFX04\) __RAZAO\_SOCIAL da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 150 posições

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546 / MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. 

Se não existir, gerar nulo\.

Formato: "XXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN19__

__Regra para o campo Endereço:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo ENDERECO __\(campo 12__ __da tabela__ __SAFX04\)\.__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo ENDERECO __\(campo 12__ __da tabela__ __SAFX04\) __ENDERECO da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 125 posições

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\.

Se não existir, gerar nulo\.

Formato: "XXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN20__

__Regra para o campo Número:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo NUM\_ENDERECO __\(campo 13__ __da tabela__ __SAFX04\)\.__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo NUM\_ENDERECO __\(campo 13__ __da tabela__ __SAFX04\) __NUM\_ENDERECO da tabela ESTABELECIMENTO

__Tratamento: __Sem pontos, sem traços, sem espaços\.

Formato: XXXXXXXXXX

Tamanho: 10 posições 

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546 / MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\. 

Formato: "XXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN21__

__Regra para o campo Complemento:__

__ATENÇÃO:__ Regra invertida nesse campo\.

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo COMPL\_ENDERECO __\(campo 14__ __da tabela__ __SAFX04\)\.__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo COMPL\_ENDERECO __\(campo 14__ __da tabela__ __SAFX04\) __COMPL\_ENDERECO da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 60 posições 

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se não existir informação, gerar nulo\. Se existir informação, ela deve estar entre aspas

__Formato: “__XXXXXX__”__

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN22__

__Regra para o campo Bairro:__

__ATENÇÃO:__ Regra invertida nesse campo\.

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo BAIRRO __\(campo 15__ __da tabela__ __SAFX04\)\.__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo BAIRRO __\(campo 15__ __da tabela__ __SAFX04\) __BAIRRO da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 60 posições 

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\.

Formato: "XXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN23__

__Regra para o campo Código do Município:__

__ATENÇÃO:__ Regra invertida nesse campo\.

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Concatenar o Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\) referente ao campo COD\_MUNICIPI __da tabela SAFX04__

__\[ALTERADA \- CH10136\_2017/MFS11926/MFS535351\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Concatenar o Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO __da tabela SAFX04__ __DWT\_DOCTO\_FISCAL\.__

__Atenção: Apesar de esse campo ter 10 posições não é necessário completar com zeros, então o município deverá ser gerado com a concatenação da UF \+ Município, exemplo: 35\+38006 = 3538006 \(Pindamonhangaba\)\.__

__Importante: Apesar de não ser necessário complementar com zeros, as 10 posições, o validador considera como válido o código de Município conforme Tabela de IBGE, dessa forma a informação do Município deverá conter 5 posições, Se necessário antes de concatenar, complementar o Campo de Município com zeros até compor 5 posições, conforme exemplo abaixo:__

__                                   Exemplo: 32\+5309 = 3205309 \(Vitória\)__

Formato: 9999999999

Tamanho: 10 posições 

Tipo: Numérico\.

__MFS9232__

__CH10136\_2017__

__MFS11926__

__MFS535351__

__RN24__

__Regra para o campo Código do País:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Se a UF __\(campo 21\)__ for = ‘EX’ preencher com a informação do campo COD\_PAIS da tabela SAFX04\. Caso contrário, preencha o campo com zeros ‘00000’\.

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Se a UF __\(campo 21\)__ for = ‘EX’ preencher com a informação do campo COD\_PAIS da tabela SAFX04\. Caso contrário, preencha o campo com zeros ‘00000’\.

Para prestador será sempre do Brasil, gravar fixo __‘00105’__\. 

*Observação:* Informar esse campo somente se for para estrangeiro, caso o campo não seja preenchido o sistema identifica como Brasil\.

Formato: 99999

Tamanho: 5 posições 

Tipo: Numérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Se a UF __\(campo 21\)__ for = ‘EX’ preencher com a informação do campo COD\_PAIS da tabela SAFX04\. Caso contrário, deixar nulo\.

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN25__

__Regra para o campo CEP:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo CEP __\(campo 20__ __da tabela__ __SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher coma informação do campo CEP __\(campo 20__ __da tabela__ __SAFX04\) __CEP da tabela ESTABELECIMENTO 

__Tratamento: __Sem pontos, sem traços, sem espaços\.

Formato: 99999999

Tamanho: 8 posições 

Tipo: Numérico\. 

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__RN26__

__Regra para o campo Telefone:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo DDD __\(campo 22\)__ considerando as 3 primeiras posições \+ a informação do campo Telefone __\(campo 23\)__ considerando as 9 primeiras posições \(sem hífen\) __\(da tabela__ __SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com a informação do campo DDD __\(campo 22\)__ considerando as 3 primeiras posições \+ a informação do campo Telefone __\(campo 23\)__ considerando as 9 primeiras posições \(sem hífen\) __\(da tabela__ __SAFX04\)__

Preencher com a informação do campo DDD considerando as 3 primeiras posições \+  as 9 primeiras posições \(sem hífen\) do campo TELEFONE da tabela ESTABELECIMENTO

__Tratamento: __Sem pontos, sem traços, parênteses, sem espaços\.

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 20 posições 

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\.

Formato: "XXXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN27__

__Regra para o campo E\-mail:__

__ATENÇÃO:__ Regra invertida nesse campo\. 

Quando o indicador de serviço for__ ‘P’ \- Prestador __preencha com os dados do__ Tomador:__

Preencher com a informação do campo do E\_MAIL __\(campo 40__ __da tabela__ __SAFX04\)__

__\[ALTERADA \- CH10136\_2017\(MFS11926\)\]__

Quando o indicador de serviço for__ ‘T’ \- Tomador __preencha com os dados do__ Prestador:__

Preencher com o campo E\_MAIL __\(campo 40__ __da tabela__ __SAFX04\) __EMAIL da tabela ESTABELECIMENTO

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 80 posições

Tipo: Alfanumérico\.

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para o município de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\.

Formato: "XXXXXXX"

__MFS9232__

__CH10136\_2017__

__\(MFS11926\)__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN28__

__Regra para o campo ISS Retido no Tomador:__

Este campo indica se o imposto foi retido pelo tomador\.

<a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a>Para serviços Prestados:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

<a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>Preencher com __‘S’__:

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com __“N”\.__

Para serviços Tomados:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

Preencher com __‘S’__:

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com __“N”\.__

Campo obrigatório\.

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS9232__

__RN29__

__Regra para o campo Código do Município onde foi prestado o serviço:__

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela SAFX07\.

__Tratamento:__

- Se o campo não estiver preenchido, no log do sistema deve ser exibida a mensagem: “O município não será considerado porque o local de prestação não foi preenchido na NF\. Campo de preenchimento obrigatório, favor verificar”\.

__Atenção: Apesar de esse campo ter 10 posições não é necessário completar com zeros, então o município deverá ser gerado com a concatenação da UF \+ Município, exemplo: 35\+38006 = 3538006 \(Pindamonhangaba\)\.__

__\[Alterada – MFS567586 \- Pindamonhangaba\]__

__mportante: Apesar de não ser necessário complementar com zeros, as 10 posições, o validador considera como válido o código de Município conforme Tabela de IBGE, dessa forma a informação do Município deverá conter 5 posições, Se necessário antes de concatenar, complementar o Campo de Município com zeros até compor 5 posições, conforme exemplo abaixo:__

__Exemplo: 32\+5309 = 3205309 \(Vitória\)__

Campo obrigatório\.

Formato: 9999999999

Tamanho: 10 posições

Tipo: Numérico

__MFS9232__

__CH10136\_2017\(MFS11926\)__

__MFS567586__

__RN30__

__Regra para o campo Código da Atividade:__

Preencher com a informação do campo COD\_ATIVIDADE __\(campo 22__ __da tabela__ __SAFX2018\)\.__

__Tratamento:__

- Quando o Indicador de Tipo de Serviço for = __‘T’ \- Tomador__ e o valor não for localizado, preencher esse campo com __‘1’ __completando com zeros a esquerda até chegar o tamanho do campo exigido pelo layout, “0000000001”\. 
- Quando o Indicador do Tipo de Serviço for = __‘P’ – Prestador__ e o valor não for localizado, preencher esse campo com ‘0000000000’\.
- Se o campo não estiver preenchido, no log do sistema deve ser exibida a mensagem: “O código da atividade não foi preenchido no cadastro do serviço para o serviço informado na nota fiscal\. Campo de preenchimento obrigatório, favor verificar”\.

__\[ALTERADO\-MFS538782/ MFS\-1046420\] __Inclusão dos Municípios de Lorena, Pindamonhangaba, __Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Preencher com o campo Atividade da tela Parâmetros – Serviço Msaf x Atividade referente ao serviço cadastrado na nota fiscal\. Se o sistema não encontrar atividade vinculada ao serviço do item da nota fiscal, exibir uma mensagem de campo obrigatório: *“O campo código da atividade é de preenchimento obrigatório, favor verificar a parametrização Serviço Msaf x Atividade em parâmetros por Município”\.*

Campo obrigatório\.

Formato: 9999999999

Tamanho: 10 posições

Tipo: Numérico

__MFS9232__

__CH23922\_2018__

__MFS\-21537__

__MFS538782__

__MFS\-1046420__

__RN31__

__Regra para o campo Código Lista de Serviços:__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

__Tratamento: __Se o campo não estiver preenchido, no log do sistema deve ser exibida a mensagem: “O código da Lei 116 não foi preenchido no cadastro do serviço para o serviço informado na nota fiscal\. Campo de preenchimento obrigatório, favor verificar”\.

*Exemplos: *0704 deverá ficar ‘07\.04’

                1415 deverá ficar ’14\.15’

Campo obrigatório\.

Formato: 99999

Tamanho: 5 posições

Tipo: Numérico

__MFS9232__

__RN32__

__Regra para o campo Discriminação:__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

\.

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 2000 posições \- É permitida a quebra de linha para este campo\.

Tipo: Alfanumérico

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\.

Formato: "XXXXXXX"

__MFS9232__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN33__

__Regra para o campo Valor dos Serviços/Valor da Nota Fiscal:__

Preencher com a informação do campo VLR\_TOT da tabela DWT\_ITENS\_SERV__ \(Campo 15 da SAFX09\)__\. Esse campo deverá exibir o valor da Nota Fiscal\. 

__Tratamento:__            

- Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “O campo valor da Nota Fiscal está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos, sem vírgula\. 
- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 15,00 deverá ser informado ‘1500’\.

                  Para o valor de 123456789123456,45 deverá ser informado ‘678912345645’\.

*Observação:* Os exemplos de tratamento acima se aplicam para os campos da __RN34 até RN43\.__

Campo obrigatório\.

Formato: 999999999999\. 

Tamanho: 12 posições

Tipo: Numérico

__MFS9232__

__RN34__

__Regra para o campo Valor Deduções__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor Deduções está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições\. 

Tipo: Numérico

__MFS9232__

__RN35__

__Regra para o campo Valor Desconto Condicionado__

Esse campo será gerado em ‘000000000000’

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN36__

__Regra para o campo Valor Desconto Incondicionado__

Preencher com o somatório do campo VLR\_DESCONTO__ __da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor Desconto Incondicionado está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN37__

__Regra para o campo Valor INSS__

Preencher com o somatório do campo VLR\_INSS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor INSS está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN38__

__Regra para o campo Valor CSLL__

Preencher com o somatório do campo VLR\_CSLL da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor CSLL está com tamanho acima do máximo permitido \(12 posições\)”\.       

   

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN39__

__Regra para o campo Outras Retenções__

Preencher com o somatório dos campos VLR\_RET\_NF, VLR\_RET\_SERV da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor Outras Retenções está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições

Tipo: Numérico

__MFS9232__

__RN40__

__Regra para o campo Valor Pis __

Preencher com o somatório do campo VLR\_PIS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor Pis está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN41__

__Regra para o campo Valor Cofins__

Preencher com o somatório do campo VLR\_COFINS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor Cofins está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN42__

__Regra para o campo Valor IR__

Preencher com o somatório do campo VLR\_TRIBUTO\_IR da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor IR está com tamanho acima do máximo permitido \(12 posições\)”\.          

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__RN43__

__Regra para o campo Valor ISS__

__\[MFS937915\] __Alteração para considerar o valor do ISS Retido

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Se o campo VLR\_TRIBUTO\_ISS for igual a zero ou não estiver preenchido

     Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __\(campo 58 da SAFX09\)__\.

__Tratamento:__             

- Esse campo será __obrigatório __se o tipo de Nota Fiscal for de Serviço Prestado, __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __= ‘9’\.  __Se o campo exceder o número de caracteres permitido, emitir a mensagem de log: “O campo valor ISS está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos, sem vírgula\. 
- Se o tipo de Nota Fiscal for de Serviço Tomado,__ MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ __<> ‘9’ __e o campo exceder o número de caracteres permitido, emitir a mensagem de log: “Valor ISS está com tamanho acima do máximo permitido \(12 posições\)”\.
- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 15,00 deverá ser informado ‘1500’\.

                  Para o valor de 123456789123456,45 deverá ser informado ‘678912345645’\.

Campo Obrigatório

Formato: 999999999999

Tamanho: 12 posições 

Tipo: Numérico

__MFS9232__

__MFS937915__

__RN44__

__Regra para o campo Prestador Optante Simples Nacional__

Este campo indica se o prestador é optante pelo programa Simples Nacional\.

Preencher com:

__“S” \- Sim\.__

Verificar se o campo IND\_SIMPLES\_NAC __\(campo 43 da tabela SAFX04\)__ é igual a “S”\.

Senão, preencher com:

__“N” \- Não__

Formato: X

Tamanho: 1 Posição

Tipo: Alfanumérico

__MFS9232__

__RN45__

__Regra para o campo Alíquota__

__\[MFS937915\] __Alteração para considerar a alíquota do ISS Retido

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV __\(campo 32 da SAFX09\)__\.

Se o campo ALIQ\_TRIBUTO\_ISS for igual a zero ou não estiver preenchido

     Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __\(campo 97 da SAFX09\)__\.

__Tratamento:__ 

- De acordo com o layout as alíquotas variam entre 2,00% e 5,00%, o preenchimento deverá ser realizado da seguinte forma, exemplo: para alíquota de 2,40% informe 240 e 5,00% informe 500\.
- Se o campo alíquota não estiver preenchido, o sistema deverá exibir uma mensagem padrão no log alertando o usuário: “O campo Alíquota não foi preenchido\. Campo de preenchimento obrigatório, favor verificar”\.

Campo Obrigatório

Formato: 999

Tamanho: 3 Posições

Tipo: Numérico

__MFS9232__

__MFS937915__

__RN46__

__Regra para o campo Código da Obra__

Se o campo IND\_TP\_SERVICO da X2018\_SERVICOS referente o serviço cadastrado na nota for igual a “1”, preencher com o conteúdo do campo COD\_CANAL\_DISTRIB da DWT\_DOCTO\_FISCAL \(campo 81 da SAFX07\)\. A obra será recuperada da nota fiscal devendo ser cadastrada no Canal de Distribuição/Obra, localizado em Básicos >> MasterSAF DW >> Manutenção >> Cadastros referente a obra cadastrada na nota\.

Formato: XXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 15 posições\.

Tipo: Alfanumérico

__\[ALTERADA MFS\-67609 / MFS99542/ MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se não existir informação, gerar nulo\. Se existir informação, ela deve estar entre aspas\.

Formato:”XXXXX”

__MFS9232__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN47__

__Regra para o campo Código ART__

Se o campo IND\_TP\_SERVICO da X2018\_SERVICOS referente o serviço cadastrado na nota for igual a “1”, preencher com o conteúdo do campo Código ART da tela de cadastro de Canal de Distribuição/Obra, localizado em Básicos >> MasterSAF DW >> Manutenção >> Cadastros referente a obra cadastrada na nota\.

Formato: XXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 15 posições\.

Tipo: Alfanumérico

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se não existir informação, gerar nulo\. Se existir informação, ela deve estar entre aspas

Formato:”XXXXX”

__MFS9232__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS\-1046420__

__RN48__

__Regra para o campo Inscrição Cadastral Municipal Própria__

__\[MFS929421\] __Alteração do preenchimento do campo para a geração da Construção Civil

__Se __a geração do arquivo selecionada for igual a “Arquivos de Entrada de Serviços \(Const\.Civil / Utilities/ Telecom\)” 

     Preencher com o conteúdo do campo inscrição municipal eventual da tabela X156\_CAD\_INSC\_MUN, cadastrada para 

     o estabelecimento em que está sendo gerado o arquivo magnético

__Senão__

     Preencher com a informação do campo INSC\_MUNICIPAL do ESTABELECIMENTO 

__Tratamento:__ 

- Se o campo Inscrição Municipal Própria não estiver preenchido, o sistema deverá exibir uma mensagem no log para o usuário: “O campo Inscrição Cadastral Municipal Própria não foi preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Deverá ser preenchido sem pontos, sem traços, sem espaços\.

Campo Obrigatório

Formato: XXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 20 posições\.

Tipo: Alfanumérico

__\[ALTERADA MFS\-67609 / MFS99542 / MFS\-778546/ MFS\-1046420\] \- Para os municípios de Jacareí, Pindamonhangaba, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Se existir informação, ela deve estar entre aspas\. Se não existir, gerar nulo\.

Formato:”XXXXX”

__MFS9232__

__MFS\-67609__

__MFS99542__

__MFS\-778546__

__MFS929421__

__MFS\-1046420__

__RN48\.a__

__Regra para o campo Código do Benefício – somente para os municípios de Jacareí, Ibirité, Arapei, Bananal, Biritiba Mirim, Cachoeira Paulista, Canas, Pedro De Toledo, Queluz, Redencao Da Serra, Roseira, Salesopolis, Santa Branca e Silveiras\.__

Preencher com branco\. 

Campo não obrigatório

Formato: XXXXX

Tamanho: 5 posições\.

Tipo: Alfanumérico

__MFS48836__

__MFS\-778546__

__MFS\-1046420__

__RN49__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo “Guaratinguetá” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados e prestados do município de Guaratinguetá”\.

__MFS15537__

__RN50__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “18404” \(Guaratinguetá\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Guaratinguetá, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS15537__

__RN51__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo “Santarém” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados e prestados do município de Santarém”\.

__MFS29900__

__RN52__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PA” e ao código de município do IBGE igual a “6807” \(Santarém\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Santarém, Pará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS29900__

__RN53__

__Regra para inclusão do novo módulo no Manager:__

O novo módulo “Jacareí” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados e prestados do município de Jacareí”\.

__MFS48836__

__RN54__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “24402” \(Jacareí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Jacareí, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS48836__

__RN55__

__Regra para abertura do módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “29806” \(Ibirité\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Ibirité, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-778546__

__RN56__

__Regra para abertura do novo módulo no Manager:__

__Para cada município dessa lista deverá ser criado um modulo\.__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__ARAPEI__

__SP__

3158

__BANANAL__

__SP__

4909

__BIRITIBA MIRIM__

__SP__

6607

__CACHOEIRA PAULISTA__

__SP__

8603

__CANAS__

__SP__

9957

__PEDRO DE TOLEDO__

__SP__

37206

__QUELUZ__

__SP__

41901

__REDENCAO DA SERRA__

__SP__

42305

__ROSEIRA__

__SP__

44301

__SALESOPOLIS__

__SP__

45001

__SANTA BRANCA__

__SP__

46009

__SILVEIRAS__

__SP__

52007

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “xxxx” \(Nome do município\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de \(Nome do Município\), São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-1046420__

