# MTZ_NFSE_ABACO_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_NFSE_ABACO_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-24
- **Tamanho:** 120 KB

---

THOMSON REUTERS

Serviços Tomados 

Geração do Meio Magnético – NFSEABACO 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-5630

Liliane Assaf

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados para atendimento ao município de Rondonópolis através do novo validador “NFSE ABACO”\.

OBS: Bastante semelhante ao validador Declarar DIR, criado pela MFS\-4913\.

MFS1\-0484

João Henrique 

Este documento tem como objetivo incluir o novo município Rio Branco/AC no validador “NFSE ABACO”, conforme layout disponibilizado pela prefeitura e informações obtidas pelo cliente\. 

MFS\-13170

Daniel Oliveira

Este documento tem como objetivo ajustar a geração de meio magnético para o município de Rio Branco para conforme informado pelo setor tributário notas fiscais eletrônicas emitidas por prestadores estabelecidos em Rio Branco/AC não devem ser declaradas na obrigação municipal\.

CH16990\_2017

MFS\-13410

João Henrique

Este documento tem como objetivo alterar a TFIX83 para considerar as séries válidas conforme layout disponibilizado pela Prefeitura de Rio Branco\-AC\.

CH17933\_2017

MFS\-13720

João Henrique

Este documento tem como objetivo incluir a geração de meio magnético para o município de Várzea Grande\-MT para o validador NFSE Ábaco\.

MFS\-15208

João Henrique

Este documento tem como objetivo incluir a geração de meio magnético para o município de Manaus\-AM no validador NFSE Ábaco\.

CH2520\_2018 \(MFS\-16433\)

Julyana Perrucini

Este documento tem como objetivo alterar a geração da declaração para desconsiderar as notas fiscais de prestadores de dentro do município\.

CH16023\_2018 \(MFS\-19400\)

Julyana Perrucini

Este documento tem como objetivo retirar a regra de omissão das TAGs em caso de valor nulo\.

CH24201\_2018

\(MFS\-21515\)

João Henrique

Essa alteração tem como finalidade não apresentar as TAGS <InscricaoMunicipal> e <Email> quando não existir informação e/ou valores para o município de Manaus\-AM\.

MFS\-24091

Andréa Rocha

Alterar a forma de gerar o campo Natureza de Operação\.

MFS\-26163

Andréa Rocha

Incluir limite de quantidades de notas para o município de Manuaus\.

MFS\-27368

Andréa Rocha

Alterar a forma de controlar o número do lote para o município de Manuaus\.

MFS\-35280

Alessandra Cristina Navatta

Este documento tem como objetivo incluir a geração de meio magnético para o município de Primavera do Leste \- MT no validador NFSE Ábaco\.

MFS\-48867

Alessandra Cristina Navatta

Este documento tem como objetivo incluir a geração de meio magnético para o município de Arapiraca \- AL no validador NFSE Ábaco\.

MFS\-80623

Alessandra Cristina Navatta

Este documento tem como objetivo incluir a geração de meio magnético para o município de Canoas RS no validador NFSE Ábaco, seguindo as regras do município de Arapiraca – AL

\(RN06\.a, RN18\.a, RN19\.a, IM09\)

MFS\-509666

Elisabete Costa

Este documento tem como objetivo incluir a geração de meio magnético para o município de Nova Lima\- MG no validador NFSE Ábaco \(RN04, RN07, RN09, RN10, RN18\.a, RN19\.a, IM10\)

MFS\-508025

Rogério Ohashi

Este documento tem como objetivo incluir a regra específica para o Município de Manaus para recuperar o Campo de NUM\_DOCFIS\_SERV caso estiver preenchido, senão será recuperado o campo de NUM\_DOCFIS\. \(RN17\.a\)

MFS\-700134

Bruna Ribeiro

Este documento tem como objetivo a inclusão de uma nova UF 'AL' na mesma regra de AM para a TAG <IdentificacaoPrestador>\.

MFS\-872524

Rogério Ohashi

Este documento tem como objetivo alterar o formato do arquivo específico para o município de Manaus, conforme orientação da Prefeitura de Manaus\.

MFS\-884276

Andréa Rocha

Inclusão de um parâmetro para definir se vai gerar todas as Notas Fiscais de Serviço Tomados, ou somente Notas com Retenção de ISS ou somente Notas sem Retenção de ISS\.

__MFS\-839887__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-901113__

Alessandra Navatta

Excluir os parâmetros na tela de geração para gerar Todas as Notas Fiscais de Serviço Tomados, ou somente Notas com Retenção ou Notas sem Retenção de ISS \(Somente Notas Fiscais de Serviço Tomados\) \(RN27\)\.Criada uma tela de parâmetro para contemplar esse filtro por validador\.

MFS\-996351

Rosemeire Santos

Este documento tem como objetivo, a inclusão da regra __RN21\.a__ para tratar o preenchimento do campo       <NaturezaOperacao>, com opção do __“16” \- Simples Federal __da lista de naturezas, para o município de Várzea Grande\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Estrutura de menus do módulo “NFSE ABACO”:__

- Arquivo
- Obrigações
	- __Meio Magnético __
	- __Geração – Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS\-5630__

__RN02__

__Regra para Tela Obrigações – Meio Magnético:__

__\[EXCLUSÃO MFS\-901113\]\[MFS884276\] __Inclusão de um parâmetro para definir se serão geradas as notas com retenção de ISS, ou sem retenção ou todas as notas

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Número do Lote: __O campo deve permitir que o usuário digite o número do lote desejado, com no máximo 15 posições\. Este campo é de preenchimento __obrigatório__\. Caso o usuário não informe valor para este campo, o sistema deverá exibir a mensagem de preenchimento obrigatório\.

__Quebrar Arquivos por Data de Emissão:__ O campo deve ser um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Forma de Geração do Arquivo__: Campo do tipo Radiobutton, com as seguintes opções:

   \-Todas as Notas;

   \- Somente Notas com Retenção de ISS;

   \- Somente Notas sem Retenção de ISS\. 

    Por default, a opção __“Todas as Notas”__ deve vir marcada\. 

__    Se__ a opção selecionada for igual a __“Todas as Notas”__

         Devem ser geradas todas as notas fiscais no arquivo

__    Senão Se__ a opção selecionada for igual a __“Somente Notas com Retenção de ISS”__

         Devem ser geradas somente as notas fiscais em que o campo “ISS Retido“  for igual a “1 \(ISS Retido\)” no arquivo

__    Senão__ __Se__ a opção selecionada for igual a __“Somente Notas sem Retenção de ISS”__

            Devem ser geradas somente as notas fiscais em que o campo  “ISS Retido“ for igual a “2 – \(sem ISS Retido\)” no arquivo\.

     __Obs\.:__ As notas fiscais que serão geradas no arquivo serão recuperadas conforme as regras de recuperação já existentes\.  Este   parâmetro serve para gerar as notas separadamente, conforme a opção escolhida\.

__Estabelecimento:__ Os estabelecimentos exibidos devem obedecer as seguintes premissas:

- Que esteja licenciado\.
- Que o usuário possua direito de acesso no PowerLock;
- Que pertença ao município em questão pertencente a UF/ Município selecionado no Manager\.

__MFS\-5630__

__MFS884276__

__MFS\-901113__

__RN03__

__Regra para abas existentes na Tela Obrigações – Meio Magnético:__

Após processar o meio magnético devem ser exibidas as abas “__Log__”, “__Arquivo__”, “__Processos__” e “__Relatório__”\. 

A aba “__Arquivo__” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “__Log__” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “__Processo concluído com erros__”\.

__MFS\-5630__

__RN04__

__Regra p/ nomenclatura do arquivo magnético:__

__O Arquivo deverá conter as seguintes nomenclaturas:__

1. __AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNNNNNNNnfseabaco\_SEQ\.xml: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_N\_MMAAAA\.xml__

Quando o parâmetro __Quebrar Arquivos por Data de Emissão__ estiver desmarcado será gerado apenas um arquivo por Estabelecimento, com a nomenclatura do arquivo normal, indicado abaixo:

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNNNNNNNnfseabaco\_SEQ\.xml__

__Onde: AAAAMMDD:__ data inicial informada para geração, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\) 

__NNNNNNNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 15 \(quinze\) posições, e finalizado pelo sufixo “nfseabaco”\.

__nfseabaco__: indica que o arquivo é do validador “NFSE ABACO”\.

__\_SEQ__: representa a sequência de quebra do arquivo\.

__\.XML__: Extensão do arquivo\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ N\_MMAAAA\.XML__, onde:

       __MMAAAA__: representa a mês inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__ N:__ Indica o número do lote \(controlado pelo tomador\) com 15 \(quinze\) posições\.

__\.XML__: Extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_N\_012010\.xml

__Exemplo:__ Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_N\_012010\.xml\.

1. __AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNNNNNNN\_MMAAAAnfseabaco\_SEQ\.xml: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ N\_MMAAAA\_MMAAAA\.XML__

Quando o parâmetro __Quebrar Arquivos por Data de Emissão__ __estiver marcado__, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos por Estabelecimento de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__AAAAMMDDXXXXXXXXXXXXXXNNNNNNNNNNNNNNN\_MMAAAAnfseabaco\_SEQ\.xml__

__Onde:AAAAMMDD:__ data inicial informada para geração, AAAA __\(Ano\)__, MM __\(Mês\)__ e dia __\(DD\)\.__

__XXXXXXXXXXXXXX__: Indica o CNPJ do Tomador\. \(Recuperar a informação do ESTABELECIMENTO em questão\)  

__NNNNNNNNNNNNNNN:__ Indica o número do lote \(controlado pelo tomador\) com 15 \(quinze\) posições, e finalizado pelo sufixo ”nfseabaco”\. Quando houver quebra de arquivo, o número do lote deve ser incrementado, igual será feito com a sequência do arquivo\.

__\_MMAAAA: __mês e ano da competência referente à nota gerada\.

__nfseabaco__: indica que o arquivo é do validador “NFSE ABACO”\.

__\_SEQ__: representa a sequência de quebra do arquivo\.

__\.XML__: Extensão do arquivo\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ N\_MMAAAA\_MMAAAA\.XML__, onde:

__       MMAAAA:__ representa a data inicial da geração

       __MMAAAA__: representa a mês inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__ N:__ Indica o número do lote \(controlado pelo tomador\) com 15 \(quinze\) posições\.

__\.XML__: Extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_N\_012000\_012010\.xml

__Exemplo:__ 

Lote número 13, gerado no dia 24/12/2011 pelo Tomador de CNPJ 95\.836\.771/0001\-20, deverá ser transformado no arquivo XML com o nome EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_N\_01012000\_012010\.xml\.

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__Observação:__

__Regra p/ nomenclatura do arquivo magnético para o município de Manaus/AM:__

Em cada arquivo magnético é permitido até 150 notas fiscais, então a cada 150 notas atingidas dentro do arquivo o mesmo deverá ser quebrado em vários e gerar uma sequencial assim como, tratamos para o município de Indaiatuba, entre outros\.

__\_SEQ__: representa a sequência de quebra do arquivo quando atingida a quantidade de mais de 150 notas fiscais\.

__MFS\-5630__

__MFS\-26163__

__MFS\-27368__

__MFS\-509666__

__MFS\-839887__

__RN05__

__Regra p/ Definição do Leiaute do arquivo magnético:__

__Arquivo exemplo:__ __modelo\_declaracao\_nfs\_lote\.xml__

Este arquivo está disponível no site da prefeitura de Rondonópolis \(https://www\.e\-nfs\.com\.br/e\-nfs\_roo/index\.jsp\)

<?xml version="1\.0" encoding="utf\-8"?>

<EnviarLoteNFSenvio>

  <LoteNfse id="40">

    <NumeroLote>40</NumeroLote>

    <Cnpj>92751653000120</Cnpj>

    <InscricaoMunicipal>12345</InscricaoMunicipal>

    <QuantidadeNfs>2</QuantidadeNfs>

    __<ListaNfse>__

      <Nfse>

        <InfNfse id="45">

          <Numero>45</Numero>

		  <Serie>3</Serie>

		  <Tipo>3</Tipo>

          <DataEmissao>2011\-03\-08T11:23:06</DataEmissao>

          <NaturezaOperacao>13</NaturezaOperacao>

          <Competencia>2011\-03\-08</Competencia>

          <Servico>

            <Valores>

              <ValorServicos>200\.00</ValorServicos>

              <ValorDeducoes>00\.00</ValorDeducoes>

              <IssRetido>1</IssRetido>

              <ValorIss>4\.00</ValorIss>

              <ValorIssRetido>4\.00</ValorIssRetido>

              <BaseCalculo>200\.00</BaseCalculo>

              <Aliquota>0\.02</Aliquota>

              <ValorLiquidoNfse>196\.00</ValorLiquidoNfse>

            </Valores>

            <ItemListaServico>101</ItemListaServico>

            <Discriminacao>Parcela Extra R$200,00</Discriminacao>

          </Servico>

          <PrestadorServico>

            <IdentificacaoPrestador>

              <Cnpj>51912237000180</Cnpj>

            </IdentificacaoPrestador>

            <RazaoSocial>REAL ASSESSORIA EMPRESARIAL LTDA</RazaoSocial>

            <Endereco>

              <CodigoMunicipio>4304606</CodigoMunicipio>

            </Endereco>

            <Contato>

              <Email>REAL@REALASSESSORIA\.COM</Email>

            </Contato>

          </PrestadorServico>

		  <TomadorServico>

		     <IdentificacaoTomador>

              <CpfCnpj>

                <Cnpj>92751653000120</Cnpj>

              </CpfCnpj>

              <InscricaoMunicipal>12345</InscricaoMunicipal>

            </IdentificacaoTomador>

          </TomadorServico>

        </InfNfse>

      </Nfse>

      <Nfse>

        <InfNfse id="46">

          <Numero>46</Numero>

		  <Serie>3</Serie>

		  <Tipo>3</Tipo>

          <DataEmissao>2011\-03\-08T11:23:06</DataEmissao>

          <NaturezaOperacao>13</NaturezaOperacao>

          <Competencia>2011\-03\-08</Competencia>

          <Servico>

            <Valores>

              <ValorServicos>200\.00</ValorServicos>

              <ValorDeducoes>00\.00</ValorDeducoes>

              <IssRetido>1</IssRetido>

              <ValorIss>4\.00</ValorIss>

              <ValorIssRetido>4\.00</ValorIssRetido>

              <BaseCalculo>200\.00</BaseCalculo>

              <Aliquota>0\.02</Aliquota>

              <ValorLiquidoNfse>196\.00</ValorLiquidoNfse>

            </Valores>

            <ItemListaServico>101</ItemListaServico>

            <Discriminacao>Parcela Extra R$200,00</Discriminacao>

          </Servico>

          <PrestadorServico>

            <IdentificacaoPrestador>

              <Cnpj>51912237000180</Cnpj>

            </IdentificacaoPrestador>

            <RazaoSocial>REAL ASSESSORIA EMPRESARIAL LTDA</RazaoSocial>

            <Endereco>

              <CodigoMunicipio>4304606</CodigoMunicipio>

            </Endereco>

            <Contato>

              <Email>REAL@REALASSESSORIA\.COM</Email>

            </Contato>

          </PrestadorServico>

		  <TomadorServico>

		     <IdentificacaoTomador>

              <CpfCnpj>

                <Cnpj>92751653000120</Cnpj>

              </CpfCnpj>

              <InscricaoMunicipal>12345</InscricaoMunicipal>

            </IdentificacaoTomador>

          </TomadorServico>

        </InfNfse>

      </Nfse>

    __</ListaNfse>__

  </LoteNfse>

</EnviarLoteNFSenvio>

__MFS\-5630__

__RN06__

__Regra p/ Formatação de campos Utilizados no arquivo magnético:__

Seguir a definição de formatação e tipos existente no “Manual\_Validador\.pdf”, tópico “Anexo 1”, páginas 5, 6, 7, 8, 9\.

Existem dois tipos que estão sem definição de domínio no  “Manual\_Validador\.pdf”, TsSerie e TsTipo\.

Em consulta a prefeitura de Rondonópolis conseguimos a definição dos domínios desses tipos:

__TsSerie:__

- 8 – T1,  
- 9 – NF, 
- 10 – OUTROS, 
- 11 – UNICA, 
- 12 – SERI 1, 
- 13 – SERIE A 
- 14 – RPA  

__TsTipo:__

- 1 – NFS, 
- 2 – RPA, 
- 3 – OUTROS

__\[ALTERADA \- CH16023\_2018 \(MFS\-19400\)\]__

__Destaque para a orientação:__

“TAGs que permitem valores nulos devem ser omitidas da estrutura XML a ser enviada”

Ou seja, se o campo não é obrigatório no layout e não houver informação na tabela do DW, então não apresentar a tag no arquivo\.

__MFS\-5630__

__CH16023\_2018 \(MFS\-19400\)__

__RN06\.a__

__Regra p/ Formatação de campos Utilizados no arquivo magnético \(Para o município de Arapiraca e Canoas\):__

Existem dois tipos que estão sem definição de domínio no “Arapiraca JADE\.pdf”, TsSerie e TsTipo\.

__TsSerie:__

- 3 – T,
- 5 – T1
- 6 – M1, 
- 7 – NF, 
- 8 – RPA, 
- 9 – OUT  

__TsTipo:__

- 3 – NFS, 
- 8 – RPA, 
- 9 – OUTROS

__MFS\-48867__

__MFS\-80623__

__RN07__

__Regra p/ Recuperação das notas fiscais de serviços tomados \(a geração será somente de serviços tomados no arquivo\)\.__

__\[ALTERADA \- CH2520\_2018 \(MFS\-16433\)\]__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3;

ou

Classificação da nota fiscal = 9 e código do documento \(cód\_docto = ‘RPA’\);

- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Nota não cancelada \(SITUACAO <> ‘S’\)
- Não será considerado documento sem item\.
- Para considerar notas fiscais eletrônicas verificar: 
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__
	- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__MFS\-5630__

__CH2520\_2018 MFS\-16433__

__MFS\-509666__

__RN07\.a__

__Regra para geração de serviços tomados para o município de Rio Branco/AC__

Conforme informado pelo setor tributário notas fiscais eletrônicas emitidas por prestadores estabelecidos em Rio Branco/AC não devem ser declaradas na obrigação municipal\. Para tanto as notas fiscais para serem ignoradas na obrigação municipal deverão possuir as seguintes particularidades:

    \- Código do município do estabelecimento deve ser de __Rio Branco/ Acre __assim como o município e UF da__ Pessoa Fis/Jur__\.

    \- Código do modelo de documento igual a __‘55’ ou__ Indicador de nota fiscal eletrônica __‘ind\_nf\_eletronica’ __for igual a__ ‘S’\.__

__  __

__MFS\-13170__

__Regras de preenchimento das tags do arquivo magnético validador “NFSE ABACO”__

Geração do meio magnético

__RN08__

__Formato do arquivo__

O arquivo que será enviado deverá seguir o seguinte formato:

<?xml version="1\.0" encoding="utf\-8"?>

 

<EnviarLoteNFSenvio>

  <LoteNfse id="__iddd__">

__\.__

__\.__

__\.__

  </LoteNfse>

</EnviarLoteNFSenvio>

   __ __

__MFS\-5630__

__RN08\.a__

__Formato do arquivo – Específico para o município de Manauas__

O arquivo que será enviado deverá seguir o seguinte formato:

<?xml version="1\.0" encoding="utf\-8"?>

<?xml version="1\.0"?>\.

  

<EnviarLoteNFSenvio>

  <LoteNfse id="__iddd__">

__\.__

__\.__

__\.__

  </LoteNfse>

</EnviarLoteNFSenvio>

__MFS\-872524__

__RN09__

__Regra para o campo <LoteNfse id="iddd"> da Tag <EnviarLoteNFSenvio>__

Tag principal do arquivo, todas as outras tags deverão estar dentro do __<LoteNfse id="iddd">__

Dentro desta tag virá o identificador do Lote \( “iddd”\) que deve ser preenchido com campo __Número do Lote __informado da tela de  geração do Meio Magnético\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__Obs:__ 

O número do lote é o mesmo para todos os arquivos gerados pelo processamento\. O cliente pode selecionar mais de um estabelecimento\. O número do lote é o mesmo para todos os arquivos de todos os estabelecimentos gerados\.

Quando__ __parâmetro __Quebrar Arquivos por Data de Emissão__ estiver marcado__ __e mais de um arquivo for gerado, o número do lote é o mesmo em todos os arquivos\.

__MFS\-5630__

__MFS\-509666__

__RN09\.a__

__Regra para o campo <LoteNfse id="iddd"> da Tag <EnviarLoteNFSenvio> para o município de Manaus/AM:__

Tag principal do arquivo, todas as outras tags deverão estar dentro do __<LoteNfse id="iddd">__

Se houver quebra de arquivo \(quantidade > 150\)

     Dentro desta tag virá o identificador do Lote \( “iddd”\) que deve ser preenchido com campo __Número do Lote __gerado no arquivo \(ver RN04\)

Senão

     Dentro desta tag virá o identificador do Lote \( “iddd”\) que deve ser preenchido com campo __Número do Lote __informado da tela de geração do Meio Magnético

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__Obs:__ 

O número do lote é o mesmo para todos os arquivos gerados pelo processamento\. O cliente pode selecionar mais de um estabelecimento\. O número do lote é o mesmo para todos os arquivos de todos os estabelecimentos gerados\.

Quando__ __parâmetro __Quebrar Arquivos por Data de Emissão__ estiver marcado__ __e mais de um arquivo for gerado, o número do lote é o mesmo em todos os arquivos\.

__MFS\-27368__

__RN10__

__Regra para o campo <NumeroLote> da TAG <LoteNfse id="iddd">__

Recuperar a informação preenchida pelo usuário no campo __Número do Lote __informado da tela de geração do Meio Magnético\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__MFS\-5630__

__MFS\-509666__

__RN10\.a__

__Regra para o campo <NumeroLote> da TAG <LoteNfse id="iddd"> para o município de Manaus/AM:__

Se houver quebra de arquivo \(quantidade > 150\)

      Recuperar a informação do __Número do Lote __ gerado no arquivo \(ver RN04\)

Senão

      Recuperar a informação preenchida pelo usuário no campo __Número do Lote __informado da tela de geração do Meio Magnético\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__MFS\-27368__

__RN11__

__Regra para o campo <Cnpj> da TAG <LoteNfse id="iddd">__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 14

Campo Obrigatório

__MFS\-5630__

__RN12__

__Regra para o campo <InscricaoMunicipal> da TAG <LoteNfse id="iddd">__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 15

Campo Obrigatório

__MFS\-5630__

__RN13__

__Regra para o campo <QuantidadeNfs> da TAG <LoteNfse id="iddd">__

Preencher com a quantidade de notas fiscais <Nfse> geradas dentro da TAG \- < ListaNfse> \.

Tipo: Numérico

Tamanho: 4

Campo Obrigatório

__MFS\-5630__

__RN14__

__Regra para o campo <ListaNfse> da TAG <LoteNfse id="iddd">__

Tag para listar todas as notas fiscais\.

Campo Obrigatório

__MFS\-5630__

__RN15__

__Regra para o campo <Nfse> da TAG < ListaNfse >__

Tag para representar cada nota fiscal\.

Campo Obrigatório

__MFS\-5630__

__RN16__

__Regra para o campo <InfNfse id="iddd"> da TAG <Nfse>__

Tag para as informações da nota fiscal\.

Dentro desta tag virá o identificador da Nota Fiscal\( “iddd”\) que deve ser preenchido com campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Campo Obrigatório

__MFS\-5630__

__RN16\.a__

__Regra para o campo <InfNfse id="iddd"> da TAG <Nfse> \- __Regra específica para o Município de Manaus

Tag para as informações da nota fiscal\.

Dentro desta tag virá o identificador da Nota Fiscal\( “iddd”\) que deve ser preenchido:

__Se__ o NUM\_DOCFIS\_SERV estiver vazio

  __Preencher__ com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Senão__ 

__    Preencher __com o campo NUM\_DOCFIS\_SERV da tabela DWT\_DOCTO\_FISCAL\.

Campo Obrigatório

__MFS\-508025__

__RN17__

__Regra para o campo <Numero> da TAG <InfNfse id="iddd">__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__MFS\-5630__

__RN17\.a__

__Regra para o campo <Numero> da TAG <InfNfse id="iddd"> \- __Regra específica para o Município de Manaus

 __Se__ o NUM\_DOCFIS\_SERV estiver vazio

  __Preencher__ com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Senão__ 

__    Preencher __com o campo NUM\_DOCFIS\_SERV da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 15

Campo Obrigatório

__MFS\-508025__

__RN18__

__Regra para o campo <Serie> da TAG <InfNfse id="iddd"> __

A lista de séries \(segundo o tipo TsSerie\) que este campo pode assumir, carregada na __TFIX83__ \(Cadastro das Séries/Modelos das Obrigações \- PRT\_SERIE\_OBRIG\) é:

- 8 \- T1,  
- 9 \- NF, 
- 10 \- OUTROS, 
- 11 \- UNICA, 
- 12 \- SERI 1, 
- 13 \- SERIE A 
- 14 \- RPA  

__Regra de Preenchimento:__

__Parametrização de Modelo Msaf x Série__

Preencher com o campo Série da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao Modelo cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o modelo da nota, sistema deve exibir no log a seguinte mensagem: 

“Para o Modelo XX do Documento  "NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Modelo Msaf x Série\. Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Modelo Msaf x Série\.”

Tipo: Alfanumérico

Tamanho: 5

Campo Obrigatório\.

__MFS\-5630__

__RN18\.a__

__Para o município de Arapiraca, Canoas e Nova Lima:__

__Regra para o campo <Serie> da TAG <InfNfse id="iddd"> __

A lista de séries \(segundo o tipo TsSerie\) que este campo pode assumir, carregada na __TFIX83__ \(Cadastro das Séries/Modelos das Obrigações \- PRT\_SERIE\_OBRIG\) é:

- 3 – T,  
- 5 – T1, 
- 6 – M1, 
- 7 – NF, 
- 8 – RPA, 
- 9 –  OUT  

__Regra de Preenchimento:__

__Parametrização de Modelo Msaf x Série__

Preencher com o campo Série da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao Modelo cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o modelo da nota, sistema deve exibir no log a seguinte mensagem: 

“Para o Modelo XX do Documento  "NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Modelo Msaf x Série\. Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Modelo Msaf x Série\.”

Tipo: Alfanumérico

Tamanho: 5

Campo Obrigatório\.

__CH16990\_2017__

__MFS\-13410__

__MFS\-35861__

__MFS\-48867__

__MFS\-80623__

__MFS\-509666__

__RN19__

__Regra para o campo <Tipo> da TAG <InfNfse id="iddd">__

A lista de Tipos \(segundo o tipo TsTipo\) que este campo pode assumir, carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG\) é:__ __

- 1 \- NFS, 
- 2 \- RPA, 
- 3 \- OUTROS

__Regra de Preenchimento:__

__Parametrização de Tipo Docto Msaf x Tipo Documento__

Preencher com o campo Tipo Documento da tela Municipal – Parâmetros por Município – Tipo Docto Msaf x Tipo Documento referente ao Código do Tipo do Documento cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o Tipo do Documento informado na nota, o sistema deve exibir no log a seguinte mensagem: 

“Para o Tipo Documento XXXXX do Documento  "NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Tipo Docto Msaf x Tipo Documento\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Tipo Docto Msaf x Tipo Documento\.”

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS\-5630__

__RN19\.a__

__Regra para o campo <Tipo> da TAG <InfNfse id="iddd"> \(Para o município de Arapiraca e Canoas\)__

A lista de Tipos \(segundo o tipo TsTipo\) que este campo pode assumir, carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG\) é:__ __

- 3 – NFS, 
- 8 – RPA, 
- 9 – OUTROS

__Regra de Preenchimento:__

__Parametrização de Tipo Docto Msaf x Tipo Documento__

Preencher com o campo Tipo Documento da tela Municipal – Parâmetros por Município – Tipo Docto Msaf x Tipo Documento referente ao Código do Tipo do Documento cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o Tipo do Documento informado na nota, o sistema deve exibir no log a seguinte mensagem: 

“Para o Tipo Documento XXXXX do Documento "NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Tipo Docto Msaf x Tipo Documento\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Tipo Docto Msaf x Tipo Documento\.”

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS\-48867__

__MFS\-80623__

__RN19\.b__

__Regra para o campo <Tipo> da TAG <InfNfse id="iddd"> \(Para o município de Nova Lima\)__

A lista de Tipos \(segundo o tipo TsTipo\) que este campo pode assumir, carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG\) é:__ __

- 1 – RPS, 
- 2 – Nota Fiscal conjugada \(Mista\), 
- 3 – Cupom

__Regra de Preenchimento:__

__Parametrização de Tipo Docto Msaf x Tipo Documento__

Preencher com o campo Tipo Documento da tela Municipal – Parâmetros por Município – Tipo Docto Msaf x Tipo Documento referente ao Código do Tipo do Documento cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o Tipo do Documento informado na nota, o sistema deve exibir no log a seguinte mensagem: 

“Para o Tipo Documento XXXXX do Documento "NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Tipo Docto Msaf x Tipo Documento\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Tipo Docto Msaf x Tipo Documento\.”

Tipo: Numérico

Tamanho: 1

Campo Obrigatório\.

__MFS\-509666__

__RN20__

__Regra para o campo <DataEmissao> da TAG <InfNfse id="iddd">__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data/Hora \(datetime\)

Campo Obrigatório\.

__MFS\-5630__

__RN21__

__Regra para o campo <NaturezaOperacao> da TAG <InfNfse id="iddd">     __

A lista de naturezas \(segundo o tipo TsNaturezaOperacao\) que este campo pode assumir é:

- 11 – ISS a Recolher
- 12 – Imune Isento
- 13 – Retenção ISSQN
- 14 – Não Incidência
- 15 – Estimado Fixo
- 16 – Simples Federal
- 19 – Retenção Simples
- 111 – Suspenso
- 28 – Recolhimento Fora
- 212 – Serviço no Exterior

__Regra de Preenchimento:__

__“12” \- Imune Isento__

-  Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10”\.
-  Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

Se uma das condições acima for verdadeira, preencher com __12\.__

__ “14” \- Não Incidência__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

Se a condição acima for verdadeira, preencher com __14\.__

__ “15” \- Estimado Fixo__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

Se a condição acima for verdadeira, preencher com __15\.__

__ “28” \- Recolhimento Fora \(\*\*\*\*\)__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472” 

E 

__\[MFS24091\]__

Se o campo Código do Município do ISS \(COD\_MUNICIPIO da tabela SAFX07\) referente ao local de prestação de serviço cadastrado na nota fiscal for __diferente__ do município do módulo selecionado\.

Se o campo Código do Município do ISS \(COD\_MUNICIPIO da tabela SAFX07\) referente ao local de prestação de serviço cadastrado na nota fiscal for DIFERENTE do município do prestador do serviço campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal\.

Se a condição acima for verdadeira, preencher com __28\.__

__ “111” \- Suspenso__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”, preencher com __111__\.

__“212” \- Serviço no Exterior__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota, estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”,

__“13” \- Retenção ISSQN__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\.
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se uma das condições acima for verdadeira  E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for diferente de__ “S”, preencher com __13\.__

__“19” \- Retenção Simples__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\. 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se uma das condições acima for verdadeira  E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for igual a__ “S”, preencher com __19\.__

__ “16” \- Simples Federal__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\.
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\. 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se nenhuma das condições acima for verdadeira E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for igual a “S”,__ preencher com __16__\.

__“11” – ISS a Recolher__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\. 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\. 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se nenhuma das condições acima for verdadeira E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for diferente de__ “S”, preencher com __11\.__

__Mensagem no Log:__

Se a nota não atender aos critérios para preenchimento do campo NaturezaOperacao, sistema deve exibir no log a seguinte mensagem: 

“Documento  "NNNNNNNNNNNN \-SSS" gerado sem preenchimento do campo Natureza Operação\. Favor rever informações relacionadas a retenção e valores de ISS no próprio documento fiscal e parametrização de Classificação Serviço por Município\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Classificação Serviço\-\-> Município”

Tipo: Numérico

Tamanho: 2

Campo Obrigatório\.

__Obs: Cada item de serviço deve ter a Natureza de Operação determinada pelas regras acima\. __

__A Natureza de Operação determinada para o 1º item de serviço é gravada na tag <NaturezaOperação>\. As Naturezas de Operação dos demais itens são gravadas na tag <Discriminacao>\.__

__O mesmo acontece para <Aliquota> <ItemListaServico>  <NaturezaOperacao > e <IssRetido>\.__

__MFS\-5630__

__MFS\-24091__

__RN21\.a__

__Regra para o campo <NaturezaOperacao> da TAG <InfNfse id="iddd"> \- Específica para o município de Várzea Grande__

A lista de naturezas \(segundo o tipo TsNaturezaOperacao\) que este campo pode assumir é:

- 11 – ISS a Recolher
- 12 – Imune Isento
- 13 – Retenção ISSQN
- 14 – Não Incidência
- 15 – Estimado Fixo
- 16 – Simples Federal
- 19 – Retenção Simples
- 28 – Recolhimento Fora
- 111 – Suspenso
- 212 – Serviço no Exterior

__Regra de Preenchimento:__

__“12” \- Imune Isento__

-  Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10”\.
-  Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

Se uma das condições acima for verdadeira, preencher com __12\.__

__ “14” \- Não Incidência__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

Se a condição acima for verdadeira, preencher com __14\.__

__ “15” \- Estimado Fixo__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

Se a condição acima for verdadeira, preencher com __15\.__

__ “28” \- Recolhimento Fora \(\*\*\*\*\)__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472” 

E 

__\[MFS24091\]__

Se o campo Código do Município do ISS \(COD\_MUNICIPIO da tabela SAFX07\) referente ao local de prestação de serviço cadastrado na nota fiscal for __diferente__ do município do módulo selecionado\.

Se o campo Código do Município do ISS \(COD\_MUNICIPIO da tabela SAFX07\) referente ao local de prestação de serviço cadastrado na nota fiscal for DIFERENTE do município do prestador do serviço campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal\.

Se a condição acima for verdadeira, preencher com __28\.__

__ “111” \- Suspenso__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”, preencher com __111__\.

__“212” \- Serviço no Exterior__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota, estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”,

__“13” \- Retenção ISSQN__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\.
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se uma das condições acima for verdadeira  E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for diferente de__ “S”, preencher com __13\.__

__“19” \- Retenção Simples__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\. 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se uma das condições acima for verdadeira  E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for igual a__ “S”, preencher com __19\.__

__ “16” \- Simples Federal__

Verificar se todas as condições abaixo são verdadeiras:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\.
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\. 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se todas as condições acima forem verdadeiras E se o campo IND\_SIMPLES\_NAC, referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for igual a__ “S”, e o campo IND\_CLASSE\_EMP __for igual a 03__ \(Empresa Normal\) da tabela SAFX04, então preencher com __16\.__

__“11” – ISS a Recolher__

Verificar se uma das condições abaixo é verdadeira\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"\. 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\. 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Se nenhuma das condições acima for verdadeira E se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal __for diferente de__ “S”, preencher com __11\.__

__Mensagem no Log:__

Se a nota não atender aos critérios para preenchimento do campo NaturezaOperacao, sistema deve exibir no log a seguinte mensagem: 

“Documento  "NNNNNNNNNNNN \-SSS" gerado sem preenchimento do campo Natureza Operação\. Favor rever informações relacionadas a retenção e valores de ISS no próprio documento fiscal e parametrização de Classificação Serviço por Município\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Classificação Serviço\-\-> Município”

Tipo: Numérico

Tamanho: 2

Campo Obrigatório\.

__Obs: Cada item de serviço deve ter a Natureza de Operação determinada pelas regras acima\. __

__A Natureza de Operação determinada para o 1º item de serviço é gravada na tag <NaturezaOperação>\. As Naturezas de Operação dos demais itens são gravadas na tag <Discriminacao>\.__

__O mesmo acontece para <Aliquota> <ItemListaServico>  <NaturezaOperacao > e <IssRetido>\.__

__MFS\-996351__

__RN22__

__Regra para o campo <Competencia> da TAG <InfNfse id="iddd">__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Data \(date\)

Campo Obrigatório\.

__MFS\-5630__

__RN23__

__Regra para o campo <Servico> da TAG <InfNfse id="iddd">__

Tag para identificar item da nota fiscal\.

__Obs: __No caso da nota possuir mais de um item de serviço, estes são agrupados por __<Aliquota> <ItemListaServico>  <NaturezaOperacao > e <IssRetido>__ e os valores totalizados para estes grupamentos, __<ValorServicos>  <ValorDeducoes> <ValorIss> <BaseCalculo> <ValorLiquidoNfse> <ValorIssRetido>\.__

Como só pode existir uma ocorrência de <Servico> por nota fiscal no arquivo XML, somente um agrupamento é gravado nas tags <Aliquota> <ItemListaServico> <NaturezaOperacao >, <IssRetido>, <ValorServicos>  <ValorDeducoes> <ValorIss> <BaseCalculo> <ValorLiquidoNfse> <ValorIssRetido>\.  Os demais agrupamentos não são gravados distintamente nessas tags\. Daí a tag <Discriminacao> é utilizada, onde essas informações de todos os itens de serviço são apresentadas\.

__MFS\-5630__

__RN24__

__Regra para o campo <Valores> da TAG <Servico>__

Tag para relacionar valores do item da nota fiscal\.

__MFS\-5630__

__RN25__

__Regra para o campo <ValorServicos> da TAG <Valores>__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento  "NNNNNNNNNNNN \-SSS" com Valor do Serviço excedendo o tamanho máximo permitido \(15 posições\)”\.
- Se o campo o valor do serviço não estiver preenchido ou for igual a zero, então emitir a mensagem de log: “Documento  "NNNNNNNNNNNN \-SSS" com Valor do Serviço não preenchido, sendo que este campo é obrigatório\.

Tipo: Numérico

Tamanho: 15,2

Campo Obrigatório\.

__MFS\-5630__

__RN26__

__Regra para o campo <ValorDeducoes> da TAG <Valores>__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento “NNNNNNNNNNNN \-SSS" com Valor de Dedução excedendo o tamanho máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

Campo Não obrigatório\.

__MFS\-5630__

__RN27__

__Regra para o campo <IssRetido> da TAG <Valores>__

__Se o campo <NaturezaOperacao> relacionada ao item da nota fiscal estiver preenchido com ‘13’ ou ‘19’, então:__

    Preencher com o valor ‘1’ \- \(Sim\)\. 

__Caso contrário:__

    Preencher com ‘2’ – \(Não\)\.

Tipo: Numérico

Tamanho: 1

Domínio: 1 – Sim

                2 – Não

Campo Obrigatório\.

__Obs: Cada item de serviço deve ter o Indicador de ISS Retido determinado pela regra acima\. __

__O Indicador de ISS Retido determinado para o 1º item de serviço é gravado na tag < IssRetido>\.  Os Indicadores de ISS Retido dos demais itens são gravados na tag <Discriminacao>\.__

__O mesmo acontece para <Aliquota> <ItemListaServico> <NaturezaOperacao > e <IssRetido>\.__

__MFS\-5630__

__RN28__

__Regra para o campo <ValorIss> da TAG <Valores>__

 

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento “NNNNNNNNNNNN \-SSS" com Valor do ISS excedendo o tamanho máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

Campo Não obrigatório\.

__MFS\-5630__

__RN29__

__Regra para o campo <ValorIssRetido> da TAG <Valores>  __

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, considerando a regra abaixo:

__Se o campo <NaturezaOperacao> relacionado ao item de serviço estiver preenchido com ‘13’ ou ‘19’, então:__

      Considerar o VLR\_TRIBUTO\_ISS deste item na consolidação dos valores para gravar a tag __<ValorIssRetido>\.__

__Caso contrário:__

      Não considerar o VLR\_TRIBUTO\_ISS deste item\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Valor com tamanho acima do máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

Campo Não obrigatório\.

__MFS\-5630__

__RN30__

__Regra para o campo <BaseCalculo> da TAG <Valores>__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento “NNNNNNNNNNNN \-SSS" com Valor da Base de Cálculo excedendo o tamanho máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

Campo Não obrigatório\.

__MFS\-5630__

__RN31__

__Regra para o campo <Aliquota> da TAG <Valores>__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

*Observação:* Será preenchido com o tamanho máximo da tabela Mastersaf\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento “NNNNNNNNNNNN \-SSS" com Alíquota excedendo o tamanho máximo permitido \(5 posições\)”\.

Tipo: Numérico

Tamanho: 5,4

Campo Não obrigatório\.

__Obs: A alíquota do 1º item de serviço é gravada na tag <Aliquota> e as alíquotas dos demais itens são gravadas na tag <Discriminacao>\.__

__O mesmo acontece para <Aliquota> <ItemListaServico>  <NaturezaOperacao > e <IssRetido>\.__

__MFS\-5630__

__RN32__

__Regra para o campo <ValorLiquidoNfse> da TAG <Valores>__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Mensagem no Log:__

- Se o campo exceder o número de caractere permitido, emitir a mensagem de log: “Documento “NNNNNNNNNNNN \-SSS" com Valor Líquido excedendo o tamanho máximo permitido \(15 posições\)”\.

Tipo: Numérico

Tamanho: 15,2

Campo Não obrigatório\.

__MFS\-5630__

__RN33__

__Regra para o campo <ItemListaServico> da TAG <Servico>__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018\. Desprezar o zero à esquerda dos Códigos de Serviço da Lei 116\. Exemplos:

0001, deverá ficar igual a 1

0704, deverá ficar 704

__Mensagem no Log:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, sistema deve exibir no log a seguinte mensagem:

“Documento “NNNNNNNNNNNN \-SSS" gerado sem preenchimento do campo Item Lista Serviço\. Favor informar o Código da Lei 116 no Cadastro do Serviço para o Código do Servido relacionado ao documento fiscal\.”

Tipo: Alfanumérico

Tamanho: 4

Campo Obrigatório

__Obs: O Código de Serviço da Lei 116 do 1º item de serviço é gravado na tag < ItemListaServico > e os Códigos de Serviços da Lei 116 dos demais itens são gravados na tag <Discriminacao>\.__

__O mesmo acontece para <Aliquota> <ItemListaServico> <NaturezaOperacao > e <IssRetido>\.__

__MFS\-5630__

__RN34__

__Regra para o campo <Discriminacao> da TAG <Servico> __

A discriminação será utilizada para descrever cada item de serviço do documento fiscal da seguinte forma\. 

\[“Num\. Item:  “                    NUM\_ITEM da tabela DWT\_ITENS\_SERV                                    “\- “

 “Item da Lista Serviço: “    COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116           “\- “

 “Natureza da Operação: “ RN24                                                                                                “\- “

 “Valor do Serviço: “            VLR\_SERVICO da tabela DWT\_ITENS\_SERV                              “\- “

 “Valor de Dedução: “         VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV                     “\- “

 “Valor do ISS: “                VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.                      “\- “

  “Base de Cálculo:            VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV                        “\- “

  “Alíquota: “                       ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV                      “\- “

  “Valor Líquido: “              RN33                                                                                          “\- “

  “Valor do ISS Retido:      RN34                                                                                           “\- “

  “Indicador ISS Retido:     RN35   \]

Tipo: Alfanumérico

Tamanho: 2000

Campo Obrigatório

__MFS\-5630__

__RN35__

__Regra para a Tag <PrestadorServico> da TAG <InfNfse id="iddd">__

Tag para representar informações do Prestador \(Pessoa Física Jurídica da nota fiscal\)\.

__MFS\-5630__

__RN36__

__Regra para a Tag <IdentificacaoPrestador> da Tag <PrestadorServico> __

Tag para representar informações da Identificação do Prestador \(Pessoa Física Jurídica da nota fiscal\)\.

__MFS\-5630__

__RN37__

__Regra para o campo <Cnpj> da TAG <IdentificacaoPrestador> __

Preencher a informação do campo CPF\_CGC \(campo 06\) da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 14

Campo Obrigatório

__MFS\-5630__

__RN38__

__Regra para a Tag <InscricaoMunicipal> da TAG <IdentificacaoPrestador> __

Preencher a informação do campo INSC\_MUNICIPAL \(campo 09\) da tabela X04\_PESSOA\_FIS\_JUR\. 

__Para o Município de Manaus\-AM:__

Se não existir valor para essa TAG, o sistema não deverá exibir na estrutura do arquivo magnético\.

__Para o Município de Manaus\-AM e Arapiraca\-AL :__

Se não existir valor para essa TAG, o sistema não deverá exibir na estrutura do arquivo magnético\.

Tipo: AlfaNumérico

Tamanho: 15

Campo Não Obrigatório

__MFS\-5630__ CH24201\_2018

\(MFS\-21515\)

__MFS\- 700134__

__RN39__

__Regra para o campo <RazaoSocial> da TAG < PrestadorServico> __

Preencher com a informação dos campos: RAZAO\_SOCIAL \(Campo 05\) da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: AlfaNumérico

Tamanho: 115

Campo Obrigatório

__MFS\-5630__

__RN40__

__Regra para a Tag <Endereco> da TAG < PrestadorServico> __

Tag para representar informações do endereço do Prestador\.

__MFS\-5630__

__RN41__

__Regra para o campo <CodigoMunicipio> da TAG <Endereco>__

Preencher com o Código do Município conforme Tabela IBGE\.

Concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao COD\_MUNICIPIO \(Campo 25\) da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 7

Campo Não Obrigatório

__MFS\-5630__

__RN42__

__Regra para a Tag <Contato> da TAG < PrestadorServico> __

Tag para representar informações de contato do Prestador\.

__MFS\-5630__

__RN43__

__Regra para o campo <Email> da TAG <Contato> __

Preencher com a informação do campo E\_MAIL \(campo 40\) da tabela X04\_PESSOA\_FIS\_JUR\.

__Para o Município de Manaus\-AM__:

Se não existir valor para essa TAG, o sistema não deverá exibir na estrutura do arquivo magnético\.

Tipo: Alfanumérico

Tamanho: 80

Campo Não Obrigatório

__MFS\-5630__

CH24201\_2018

\(MFS\-21515\)

__RN44__

__Regra para a Tag <TomadorServico> da TAG <InfNfse id="iddd"> __

Tag para representar informações do Tomador \(Estabelecimento da geração\)\.

__MFS\-5630__

__RN45__

__Regra para a Tag <IdentificacaoTomador> da Tag <TomadorServico> __

Tag para representar informações da Identificação do Tomador \(Estabelecimento da geração\)\.

__MFS\-5630__

__RN46__

__Regra para a Tag <CpfCnpj> da Tag <IdentificacaoTomador> __

Tag para representar informações do CNPJ do Tomador \(Estabelecimento da geração\)\.

__MFS\-5630__

__RN47__

__Regra para o campo <Cnpj> da TAG <CpfCnpj> __

Recuperar a informação do campo: CGC da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho: 14

Campo Obrigatório

__MFS\-5630__

__RN48__

__Regra para a Campo <InscricaoMunicipal> da TAG < IdentificacaoTomador> __

Preencher a informação do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\. 

__Para o Município de Manaus\-AM:__

Se não existir valor para essa TAG, o sistema não deverá exibir na estrutura do arquivo magnético\.

Tipo: AlfaNumérico

Tamanho: 15

Campo Não Obrigatório

__MFS\-5630__

CH24201\_2018

\(MFS\-21515\)

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

# INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__OS/CH/MFS__

__IM00__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

__MFS\-5630__

__IM01__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-5630__

__IM02__

__Regra para Tela de Seleção dos Validadores pôr Município__

__Rondonópolis__

O município de Rondonópolis poderá ser gerado através de dois validadores \(ISS Intel para gerações até 12/06/2012 e “NFSE ABACO” para gerações a partir de 13/06/2012\)\. 

Dessa forma, após a abertura do módulo deve\-se exibir uma tela informando os validadores com suas respectivas Datas Inicial e Final do módulo que o município possui\.

Desta forma, o sistema saberá para qual validador o usuário pretende realizar a geração e ao clicar no nome do validador o sistema poderá chamar a geração correspondente ao validador selecionado\.

O validador mais antigo deve sempre vir em primeiro e deve ser informada a data da validade final informada na TFIX105\.

O validador mais atual deve vir logo em seguida e deve ser informada a data da validade inicial informada na TFIX105\.

__*Observação:*__ Essa tela apenas deve ser exibida para os municípios que possuam a troca de validadores e que tenham que manter os dois validadores para a geração dos períodos de vigência\. Para os demais municípios deve ser mantida a atual forma de geração\.

__MFS\-5630__

__IM03__

__Código IBGE: 7602 – Município/UF: Rondonópolis – MT__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Rondonópolis”

__MFS\-5630__

__IM04__

__Código IBGE: 401 – Município/UF: Rio Branco – AC__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Rio Branco”

__MFS\-10484__

__IM05__

__Código IBGE: 8402 – Município/UF: Vargem Grande – MT__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Vargem Grande”

__MFS\-13720__

__IM06__

__Código IBGE: 2603 – Município/UF: Manaus – AM__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Manaus”

__MFS\-15208__

__IM07__

__Código IBGE: 7040 – Município/UF: Primavera do Leste – MT__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Primavera do Leste”

__MFS\-35280__

__IM08__

__Código IBGE: 300 – Município/UF: Arapiraca – AL__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Arapiraca”

__MFS\-48867__

__IM09__

__Código IBGE: 4606 – Município/UF: Canoas – RS__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Canoas”

__MFS\-80623__

__IM10__

__Código IBGE: 44805 – Município/UF: Nova Lima – MG__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de “Nova Lima”

__MFS\-509666__

