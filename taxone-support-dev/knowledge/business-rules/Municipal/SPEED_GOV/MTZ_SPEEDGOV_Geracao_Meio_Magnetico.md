# MTZ_SPEEDGOV_Geracao_Meio_Magnetico

- **Fonte:** MTZ_SPEEDGOV_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-02-19
- **Tamanho:** 102 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – SPEED GOV 	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-9371

João Henrique

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador SPEED GOV\.

<a id="_Hlk513816556"></a>MFS\-<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>14868

João Henrique

Inclusão do município de Eusébio\-CE no validador SPEED GOV\.

<a id="_Hlk513817606"></a>MFS\-17874

João Henrique

Inclusão do município de Aracati\-CE no validador SPEED GOV\.

CH22706  
\(MFS\-21724\)

João Henrique

Alteração no tratamento do formato e log do campo __</Aliquota>\.__

MFS25184

Andréa Rocha

Inclusão do município de Juazeiro do Norte\-CE no validador SPEED GOV\.

MFS28438

Andréa Rocha

Alteração no tratamento do formato do campo __</LocalPrestacao >\.__

MFS26916

Aline Melo

Inclusão do município de Sobral\-CE no validador SPEED GOV\.

MFS30219

Andréa Rocha

Inclusão do município de Caucaia\-CE no validador SPEED GOV\.

MFS59907

Andréa Rocha

Alteração da regra de recuperação das notas fiscais para o município de Maracanaú\.

MFS59858

Rogério Ohashi

Alteração da regra de recuperação das notas fiscais para o município de Eusébio\. \(__RN07\.b\)__

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1048305__

Rosemeire Santos

Este documento tem como objetivo, incluir o município de Açailândia/MA no validador SPEED GOV\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Maracanaú” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Maracanaú”\.__

__MFS\-9371__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “7650” \(Maracanaú\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Maracanaú, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-9371__

__RN03__

__Estrutura de menus do módulo SPEED GOV__

Deverão ser criados os seguintes menu e sub\-menus no módulo SPEED GOV:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)
- Janela
- Ajuda 

__MFS\-9371__

__RN04__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.XML__, onde:

__MMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.XML

__       SPEEDGOV\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SPEEDGOV__: representa a obrigação que está sendo gerada\. 

       __\.XML__: extensão do arquivo\.

*Exemplo:* SPEEDGOV\_MARACANAU\_01012010\.xml

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_MMAAAA\.XML__, onde:

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.XML

__   SPEEDGOV\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__               SPEEDGOV__: representa a obrigação que está sendo gerada\.    

__               MUNICIPIO__: representa o município que está sendo gerado\.   

               __DDMMAAAA__: representa a data inicial da geração\.   

__               MMAAAA:__ mês da competência referente à nota gerada

               __\.XML__: extensão do arquivo\.

Ex: SPEEDGOV\_MARACANAU\_01012014\_122013\.xml

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

__MFS\-9371__

__MFS\-829438      __

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-9371__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

- Campos de valor que não houver preenchimento, gravar “0”;
- Campos que não possuírem informação deixar TAGS vazias;

__MFS\-9371__

__RN07__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2, 3 ou 9 e COD\_DOCTO = ‘RPA’
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.

__MFS\-9371__

__RN07\.a__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\) para o município de Maracanaú, Eusébio e Açailândia:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2, 3 ou 9 e COD\_DOCTO = ‘RPA’
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.

__\[MFS59907\] Inclusão da regra para não recuperar as notas fiscais dos prestadores do mesmo município da geração __

- Não recuperar os documentos fiscais desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.

__MFS\-59907__

__MFS\-59858__

__MFS\-1048305__

__RN07\.b__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\) para o município de Eusébio:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2, 3 ou 9 e COD\_DOCTO = ‘RPA’
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.

__\[MFS59858\] Inclusão da regra para não recuperar as notas fiscais dos prestadores do mesmo município da geração __

- Não recuperar os documentos fiscais desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.

__MFS\-59858__

__RN08__

__Estrutura do Arquivo:__

<?xml version=”1\.0” encoding=”UTF\-8”?>

   <Declaracao>

       <Notas>

          <Nota>

            <DataEmissao>2015\-11\-09</DataEmissao>

            <NumeroNota>100</NumeroNota>

            <Serie>A</Serie>

            <TipoPrestador>1</TipoPrestador>

            <Prestador>

                <Documento>12345678900</Documento>

                <RazaoSocial>EMPRESA TESTE LTDA</RazaoSocial>

                <Email>[teste@gmail\.com</Email](mailto:teste@gmail.com%3c/Email)>

                <Telefone>85993741874</Telefone>

                <InscricaoMunicipal>1234</InscricaoMunicipal>

                <Cep>60140170</Cep>

                <TipoLogradouro>RUA</TipoLogradouro>

                <Logradouro>TESTE</Logradouro>

                <Numero>SN</Numero>

                <Complemento>AP 103</Complemento>

                <Bairro>Centro</Bairro> 

                <Cidade>2305233</Cidade>

                <InscricaoEstadual></InscricaoEstadual>

                <Pais>Brasil</Pais>

           </Prestador>

           <LocalPrestacao>2305233</LocalPrestacao>

           <Servico>101</Servico>

           <Valor>1000\.00</Valor>

           <Aliquota>0\.0</Aliquota>

           <ValorDeducao>0\.00</ValorDeducao>

           <ValorDescontoIncondicionado>0\.00</ValorDescontoIncondicionado>

           <CodigoDaObra></CodigoDaObra>

       </Nota> 

    </Notas> 

</Declaracao> 

__MFS\-9371__

__RN09__

__Regra p/ o cabeçalho do arquivo:__

Preencher com o tag <?xml version=”1\.0” encoding=”UTF\-8”?>

TAG obrigatória\. – Cada arquivo possui uma única declaração\.

__MFS\-9371__

__RN10__

__Regra para tag <Declaracao> __Tag relacionada à abertura da formatação do arquivo que deve receber as informações das notas tomadas declaradas com o texto fixo: __<Declaracao>\.__

TAG obrigatória\.

__MFS\-9371__

__RN11__

__Regra para tag <Notas> __Tag relacionada à abertura da lista de notas de serviços tomados com o texto fixo: __<Notas>\.__

TAG obrigatória\.

__MFS\-9371__

__RN12__

__Regra p/ tag <Nota> __Tag relacionada à nota fiscal com o texto fixo: __<Nota>\.__

TAG obrigatória\.

__MFS\-9371__

__RN13__

__Regra p/ tag <DataEmissao> </DataEmissao>__

Identifica a Data da emissão da nota\. 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL __\(campo 11 da SAX07\)__

__Tratamento:__

- Se o campo Data Emissão não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: YYYY\-MM\-DD 

Tipo: Data

Tamanho: 10 posições 

__MFS\-9371__

__RN14__

__Regra p/ tag <Numero> </Numero>__

Identifica o Número da Nota fiscal\. 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL __\(campo 08 da SAFX07\)__

__Tratamento:__

- Se o campo Número da Nota não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 999999999999999

Tipo: Numérico

Tamanho: 15 posições

__MFS\-9371__

__RN15__

__Regra p/ tag <Serie> </Serie>__

Identifica a Série da Nota fiscal conforme cadastrado\.

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL __\(campo 09 da SAFX07\)__

Formato: XXX

Tipo: Alfanumérico

Tamanho: 3 posições

__MFS\-9371__

__RN16__

__Regra p/ tag <TipoPrestador> </TipoPrestador>__

Preencher com__ ‘2’ – Simples: __Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR estiver selecionado;

Preencher com__ ‘3‘ – MEI: __Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = ‘05’;

Preencher com__ ‘4’ – Estrangeiro: __Se o campo UF for = ‘EX’ da tabela X04\_PESSOA\_FIS\_JUR\.

Preencher com__ ‘5’ – Pessoa Física com Nota: __Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possui 11 posições = ‘CPF’ E o campo COD\_CLASS\_DOC\_FIS for igual = ‘2’ e ‘3’ da SAFX07\.

Preencher com__ ‘6’ – Pessoa Física sem Nota:__ Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possui 11 posições = ‘CPF’ E o campo COD\_CLASS\_DOC\_FIS ‘9’ e COD\_DOCTO = ‘RPA’ da SAFX07\.

Preencher com__ ‘1’ – Normal:__ Quando nenhuma das opções acima for verdadeira\.

__Tratamento:__

- Se o campo Tipo Prestador não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1 posição

__MFS\-9371__

__RN17__

__Regra p/ tag <Prestador> __Tag relacionada à abertura das informações do prestador do serviço com o texto fixo: __<Prestador>\.__

__MFS\-9371__

__RN18__

__Regra p/ tag <Documento> </Documento>__

Identifica: 

 CNPJ \(se empresa\); 

 CPF \(se pessoa física\) do prestador;

 Documento Estrangeiro;

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR __\(campo 06 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for igual a 11 posições\.
- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for maior que 11 posições\.
- Se o campo UF for =__ ‘EX’ __da tabela X04\_PESSOA\_FIS\_JUR preencher com o valor fixo ‘1’\. – Não deverá emitir mensagem para documento estrangeiro\.
- Se o campo Documento for igual ou maior que 11 posições e não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 99999999999, 99999999999999 ou 9999999999

Tipo: Alfanumérico\. 

Tamanho: 14 posições

__MFS\-9371__

__RN19__

__Regra p/ tag <RazaoSocial> </RazaoSocial>__

Identifica o Nome ou a Razão Social do prestador\.

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR __\(campo 05 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Razão Social não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: XXXXXXXXXXXXXXX\.\.\./ 

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW\.

__MFS\-9371__

__RN20__

__Regra p/ tag <Email> </Email>__

Identifica o E\-mail do Prestador\. 

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR __\(campo 40 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

Formato: XXXXXXXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW\.

__MFS\-9371__

__RN21__

__Regra p/ tag <Telefone> </Telefone>__

Identifica o Telefone do Prestador\. 

Preencher com o campo DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR __\(campos 22 e 23 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

Formato: XXXXXXXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 11 posições

__MFS\-9371__

__RN23__

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Identifica a Inscrição Municipal do prestador\. 

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR __\(campo 09 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Inscrição Municipal não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Formato: XXXXXXXXXXXXXXX

Tipo: Numérico

Tamanho: 8 posições

__MFS\-9371__

__RN24__

__Regra p/ tag <Cep> </Cep>__

Identifica o CEP do Prestador\. 

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR __\(campo 20 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Cep não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8 posições

__MFS\-9371__

__RN25__

__Regra p/ tag <TipoLogradouro> </TipoLogradouro>__

Identifica o tipo de Logradouro do prestador\. 

Preencher com o campo LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR __\(campo 42 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Tipo Logradouro não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.
- Todas as letras deveram ser preenchidas em ‘Maiúsculo’\.

Campo Obrigatório

Formato: XXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 3 posições

__MFS\-9371__

__RN26__

__Regra p/ tag <Lougradouro> </Logradouro>__

Identifica o endereço do prestador\. 

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR __\(campo 12 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Logradouro não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.
- Todas as letras deveram ser preenchidas em ‘Maiúsculo’\.

Campo Obrigatório

Formato: XXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 125 posições

__MFS\-9371__

__RN27__

__Regra p/ tag <Numero> </Numero>__

Identifica o número do endereço do prestador\. 

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR __\(campo 13 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 10 posições, então para atender a obrigação deverão ser consideradas as 3 primeiras posições do campo para atender o tamanho exigido pela Prefeitura\. Exemplo: 1234567891, gravar 123
- Se o campo Número não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: XXXXXXXXXX

Tipo: Alfanumérico – __Exemplo: ‘100’ ou ‘SN’\.__

Tamanho: 3 posições

__MFS\-9371__

__RN28__

__Regra p/ tag <Complemento> </Complemento>__

Identifica o complemento do endereço do prestador\. 

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR __\(campo 14 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Todas as letras deveram ser preenchidas em ‘Maiúsculo’\.

*Exemplo: “*AP 201”

Formato: XXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 60 posições

__MFS\-9371__

__RN29__

__Regra p/ tag <Bairro> </Bairro>__

Identifica o bairro do endereço do prestador\. 

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR __\(campo 15 da SAFX04\)__ referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo Bairro não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: XXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 60 posições

__MFS\-9371__

__RN30__

__Regra p/ tag <Cidade> </Cidade>__

Identifica o código do município \(IBGE\) do Prestador\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

__Tratamento:__ 

- Se o campo Cidade não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 9999999

Tipo: Numérico

Tamanho: 7 posições

__MFS\-9371__

__RN31__

__Regra p/ tag <InscricaoEstadual> </ InscricaoEstadual >__

Inscrição Estadual do prestador de serviço\.

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR __\(campo 08 da SAFX04\)__\.

Formato: 9999999

Tipo: Numérico

Tamanho: 7 posições

__MFS\-9371__

__RN32__

__Regra p/ tag <Pais> </Pais>__

Preencher o campo DESCRICAO da tabela PAIS correspondente ao campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Formato: XXXXXXXXXXXXXX\.\.\./

Tipo: Alfanumérico

Tamanho: 30 posições

__MFS\-9371__

__RN33__

__Regra p/ tag </Prestador>__ Tag relacionada ao encerramento das informações do prestador do serviço com o texto fixo: __</Prestador>\.__

__MFS\-9371__

__RN34__

__Regra p/ tag <LocalPrestacao> </LocalPrestacao>__

Identifica o Código IBGE do munícipio onde o serviço foi prestado\.

Se o tamanho do campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL for igual a 7

       Preencher o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL

Senão

       Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ o campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL\.  

__Tratamento:__

- Se o campo Local Prestação não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo Obrigatório

Formato: 9999999

Tipo: Numérico

Tamanho: 7 posições

__MFS\-9371__

__MFS28438__

__RN35__

__Regra p/ tag <Servico> </Servico>__

Código de serviço baseado na “LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003\.

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

__Tratamento:__

- Se o campo Serviço não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

*Exemplos: *0704 deverá ficar ‘0704’

                1415 deverá ficar ’1415’

Campo Obrigatório

Formato: 9999

Tipo: Numérico

Tamanho: 4 posições

__MFS\-9371__

__RN36__

__Regra p/ tag <Aliquota> </Aliquota>__

Identifica a Alíquota ISS da Nota Fiscal\. Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV __\(campo 32 da SAFX09\)\.__

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro e as últimas da parte decimal para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123,4567, gravar 3\.4
- Se o documento fiscal possuir Base ISS e/ou valor de ISS e a Tag de <Aliquota> estiver sem preenchimento ou zerada, o sistema deve apresentar uma mensagem no log padrão para o usuário: *“A Aliquota ISS do item de serviço é obrigatória e não foi informado”\.*

Caso o documento seja isento do imposto, preencher a alíquota com zeros, sem apresentar log\.

Formato: 0\.0 

__Observação:__ No manual da escrituração não temos a informação da Tag <Aliquota>, apenas o formato de exemplo nas notas fiscais do manual, Exemplos: 5\.0/ 0\.0\.

Tipo: Alfanumérico

Tamanho: 3 posições

__MFS\-9371__

CH22706  
\(MFS\-21724\)

__RN37__

__Regra p/ tag <Valor> </Valor>__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV__ \(Campo 15 da SAFX09\)__\. Esse campo deverá exibir o valor da Nota Fiscal\. 

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123456789123456,45, gravar 9123456\.45
- Se o campo Valor não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Formato: 9999999\.99 

*Exemplo:* “1290\.00”, utilizar ponto como separador decimal\.

Tamanho: 10 posições 

Tipo: Numérico

__MFS\-9371__

__RN38__

__Regra p/ tag <ValorDeducao> </ValorDeducao>__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123456789123456,45, gravar 9123456\.45\.

Formato: 9999999\.99

Exemplo: 290\.00, utilizar ponto como separador decimal\.

Tamanho: 10 posições\. 

Tipo: Numérico

__MFS\-9371__

__RN39__

__Regra p/ tag <ValorDescontoIncondicionado> </ ValorDescontoIncondicionado>__

Preencher com o somatório do campo VLR\_DESCONTO__ __da tabela DWT\_ITENS\_SERV\.

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123456789123456,45, gravar 9123456\.45

 Formato: 9999999\.99 

*Exemplo:* 120\.00, utilizar ponto como separador decimal\.

Tamanho: 10 posições 

Tipo: Numérico

__MFS\-9371__

__RN40__

__Regra p/ tag <CodigoDaObra> </CodigoDaObra>__

Se o campo IND\_TP\_SERVICO da X2018\_SERVICOS referente o serviço cadastrado na nota for igual a “1”, preencher com o conteúdo do campo COD\_CANAL\_DISTRIB da DWT\_DOCTO\_FISCAL \(campo 81 da SAFX07\)\. A obra será recuperada da nota fiscal devendo ser cadastrada no Canal de Distribuição/Obra, localizado em Básicos >> MasterSAF DW >> Manutenção >> Cadastros referente a obra cadastrada na nota\.

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 10 posições, então para atender a obrigação deverão ser consideradas as 8 primeiras posições do número para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 1234567891 gravar 12345678

Formato: 99999999

Tamanho: 8 posições\.

Tipo: Numérico

__MFS\-9371__

__RN41__

__Regra p/ tag </Nota> __Tag relacionada ao encerramento da nota fiscal com o texto fixo: __</Nota>\.__

TAG obrigatória\.

__MFS\-9371__

__RN42__

__Regra para tag </Notas> __Tag relacionada ao encerramento da lista de notas de serviços tomados com o texto fixo: __</Notas>\.__

TAG obrigatória\.

__MFS\-9371__

__RN43__

__Regra para tag </Declaracao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __</Declaracao>\.__

TAG obrigatória\.

__MFS\-9371__

<a id="_Hlk513816937"></a>__RN44__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Eusébio” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Eusébio”\.__

__MFS\-14868__

__RN45__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “4285” \(Eusébio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Eusébio Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-14868__

__RN46__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Aracati” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Aracati”\.__

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>__MFS\-17874__

__RN47__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “1109” \(Aracati\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Aracati, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-17874__

__RN47__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Juazeiro do Norte” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Juazeiro do Norte”\.__

__MFS\-25184__

__RN48__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “7304” \(Juazeiro do Norte\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Juazeiro do Norte, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-25184__

__RN49__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Sobral” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“__<a id="_Hlk14869426"></a>__Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Sobral CE”\.__

__MFS\-26916__

__RN50__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “12908” \(Sobral\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Sobral, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-26916__

__RN51__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Caucaia” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Caucaia”__\.

__MFS\-26916__

__RN52__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “CE” e ao código de município do IBGE igual a “3709” \(Caucaia\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Caucaia, Ceará\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-26916__

__RN53__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Açailândia” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Açailândia”__\.

__MFS\-1048305__

__RN54__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MA” e ao código de município do IBGE igual a “55” \(Açailândia\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Açailândia, Maranhão\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-1048305__

	

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

