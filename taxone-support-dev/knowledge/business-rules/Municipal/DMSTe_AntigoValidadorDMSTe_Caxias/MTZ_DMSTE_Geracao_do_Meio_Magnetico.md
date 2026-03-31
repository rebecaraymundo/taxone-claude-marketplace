# MTZ_DMSTE_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DMSTE_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-12
- **Tamanho:** 125 KB

---

77

                                                                            THOMSON REUTERS

	

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – DMST\-e Caxias do Sul

##### 	DOCUMENTO DE REQUISITO	

__MFS/CH__

__Nome__

__Descrição__

MFS11982

João Henrique de Araujo\.

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético em XML de serviços tomados para atender o novo validador DMST\-e Caxias do Sul\.

CH14720\_2017

\(MFS\-12565\)

João Henrique de Araujo\.

Essa alteração consiste em gerar zeros para a TAG <alíquota> quando o item da NF estiver sem preenchimento\.

MFS\-71302

Alessandra Cristina Navatta

Alterar a descrição do validador de DMSTE Caxias para DMSTE \(TFIX105 e tela de validadores\)

Incluir o município de Campo Bom/RS no validador DMST\-e\. \(RN59 e RN60\)

Ajustada a RN38\(espécie\) e RN39 \(série\), retirando a lista aceita por município, para deixar a regra genérica considerando as informações existentes na tfix correspondente \(TIFX83 e TFIX84\)\.

MFS\-618623

Rosemeire Santos

Este documento tem como objetivo incluir o município de Canoas/RS na geração do meio magnético em XML de serviços tomados do validador DMST\-e\.

MFS\-646002

Denilson André Santos

Este documento, tem como objetivo, fazer a readequação das seguintes regras:

RN37 \- <documento>: Gerar somente documentos que, possuam valor de retenção de ISS

RN47 \- <totais>: Gerar somente totais que, possuam valor de retenção de ISS

RN50 \- <baseCalculo>: Adaptação de regras para geração da base de cálculo

RN51 \- <aliquota>: Adaptação de regras para geração da alíquota

RN52 \- <valorISS>: Adaptação de regras para geração do valor do ISS

MFS\-703003

Rosemeire Santos

Este documento tem como objetivo, incluir o município de Carlos Barbosa/RS na geração do meio magnético em XML de serviços tomados do validador DMST\-e\.

MFS\-754955

Alessandra Cristina Navatta

Criação de regras para o município de Carlos Barbosa:

- Atualização da tfix83, para atender as séries exigidas pelo município\. Tag: <serie>S</serie> \(RN39\)
- Inclusão do campo <codigoLei116Principal></codigoLei116Principal>, na tag <documento> \(RN09 e RN42\.1\)

MFS\-767622

Andréa Rocha

Alteração da regra de preenchimento da tag <competencia>, para preencher de acordo com a data de emissão da nota\.

MFS\-826035

Andréa Rocha

Alteração da regra de preenchimento da tag <imRemetente> e da tag <imTomador> para o município de Canoas\. A alteração é necessária porque existe uma regra geral de limitação do tamanho do campo inscrição municipal, que não pode ser maior que 6 posições, e para Canoas não existe a limitação\.

MFS\-834548

Andréa Rocha

Inclusão dos campos <codigoLei116Principal> e <codigoServico> na tag <documento> para o município de Canoas\.

MFS\-[890983](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/890983)

Rafael Donisete

Este documento tem como objetivo, incluir o município de São Borja/RS na geração do meio magnético em XML de serviços tomados do validador DMST\-e\.

MFS\-908810

Andréa Rocha

Alteração de regra de preenchimento da tag <imTomador> para a geração do arquivo de construção civil, para o município de Canoas\.

MFS\-915209

Andréa Rocha

Alteração da regra de preenchimento do campo <codigoServico> para o município de Canoas\.  Esse campo foi criado na MFS834548, seguindo as informações passadas pelo cliente, que iria utilizar o código de atividade\. No entanto, após essa implementação, o cliente enviou uma nova lista de códigos de serviços disponíveis para Canoas, o que exige a atualização da regra de preenchimento do campo para refletir essa mudança\.

MFS\-921327

Andréa Rocha

Alteração de regra de preenchimento da tag <imRemetente> para a geração do arquivo de construção civil, para o município de Canoas\.

MFS\-903857

Andréa Rocha

Alteração de regra de geração do arquivo para não considerar as notas fiscais de prestadores do mesmo município de estabelecimento\.

MFS\-961809

Rosemeire Santos

Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão” para Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)

__MFS\-1024956__

Rosemeire Santos

Alteração da regra RN08, para sumarizar os itens da nota fiscal, quando possuem os mesmos códigos de serviços, para o município de Caxias do Sul/RS\.

__MFS\-1024956__

Rosemeire Santos

Alteração na regra RN45, para o correto preenchimento do campo “tipo ISS”

__MFS\-1048839__

Rosemeire Santos

Este documento tem como objetivo incluir o novo campo Numero Nacional, no validador do DMSTe, para todos os municípios\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Caxias do Sul” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “Consiste em registrar todas as informações sobre as notas fiscais de serviços tomados, emitidas em papel ou por meio eletrônico \(NFS\-e\), por um contribuinte ao longo de um determinado mês”\.__

__MFS11982__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “5108” \(Caxias do Sul\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Caxias do Sul, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS11982__

__RN03__

__Estrutura de menus do módulo:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS11982__

__RN04__

__Regra de nomenclatura do arquivo:__

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.XML__, onde:

        __MMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

        __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_CAXIASDOSUL\_01012014\_122013\.XML

__\[ALTERAÇÃO \- MFS961809\] \- __Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão” para Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.XML__, onde:

        __MMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

        __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_CAXIASDOSUL\_01012014\_122013\.XML

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS11982__

__MFS\-961809__

__RN05__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Menu:__  Obrigações >> Geração do Meio Magnético:

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.      

__Número do Lote:__ O campo deve permitir que o usuário digite o número do lote desejado, com no máximo 6 posições\. Este campo não é obrigatório\.                            

__Quebrar arquivo por Data de Emissão:__ Deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Gaspar, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS11982__

__RN06__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS11982__

__RN07__

__Regras para geração do Meio Magnético:__

__Regras referentes à formatação dos registros gerados no meio magnético:__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

1. __O arquivo a ser gerado para importação dever ser no formato__ __‘XML’__\.
2. __Não deve ser inserido caractere não significativo para preencher o tamanho completo do campo, ou seja, zeros antes de número ou espaço em branco após a cadeia de caracteres\. A posição do campo é definida na estrutura do documento XML através de tags \(<tag>conteúdo</tag>\)\.__
3. __A regra constante do parágrafo anterior deverá estender\-se aos campos para os quais não há indicação de obrigatoriedade e que, no entanto, seu preenchimento torna\-se obrigatório, seja condicionado à legislação específica ou ao negócio do contribuinte\. Nesse caso, deverá constar a tag com o valor correspondente e, para os demais campos não obrigatórios, deverão ser eliminadas as tags\.__
4. __Para reduzir o tamanho final do arquivo XML da DMST\-e, alguns cuidados de programação deverão ser assumidos:__

\- Não incluir "zeros não significativos" para campos numéricos;

\- Não incluir "espaços" no início ou no final de campos numéricos e alfanuméricos;

\- Não incluir comentários no arquivo XML;

\- Não incluir anotação e documentação no arquivo XML \(tag annotation e tag documentation\);

\- Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as tags\)\.

1. __As tags que permitirem valores nulos devem ser omitidas da estrutura XML a ser enviada quando seus valores forem nulos\.__
2. __A seguir encontra\-se a tabela com a lista dos tipos simples que serão utilizados como tipos de dados\. A tabela consiste das seguintes colunas:__

\- Campo: nome do tipo simples;

\- Tipo: tipo primitivo de dados utilizados pelo campo: __C \- Caractere, N \- Número, D \- Data ou Data/Hora e T \- Token__;

\- Descrição: descreve informações sobre o campo;

\- Tam\.: tamanho do campo;

1.  __Quando forem caracteres, o tamanho define a quantidade máxima de caracteres que o texto poderá ter;__
2.  __Quando for numérico o tamanho pode ser representado das seguintes formas:__

__\- __Número inteiro, que define o total de dígitos existente no número\. Exemplo: “15” significa que o número poderá ter, no máximo, 15 dígitos;

\- Número fracionário, que define o total de dígitos e quantos deles serão designados para a parte fracionária\. Exemplo: “15,2” significa que o número poderá ter, no máximo, 15 dígitos sendo 2 deles a da parte fracionária\. A parte fracionária não é obrigatória quando assim definido;

\- No número decimal não deve ser utilizado separador de milhar\. O ponto \(\.\) deve ser utilizado para separar a parte inteira da fracionária\. Exemplo: 48\.562,25 = 48562\.25 1,00 = 1\.00 ou 0,50 = 0\.50 ou 0\.5

             O arredondamento de valores/cálculos na validação da nota admite uma margem de divergência de R$ 0,03\.

\- Valores Percentuais \(decimal\) Tem o formato 000\.00\. O formato em percentual presume o valor percentual em sua forma fracionária\. O ponto \(\.\) separa a parte inteira da fracionária\. Exemplo: 62% = 62, 150% = 150, 25,32% = 25\.32, 2,75% = 2\.75

__MFS11982__

__RN08__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados \(só geraremos serviços tomados no arquivo\)\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2 ou 3 
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;

__\[ALTERAÇÃO\-MFS1024956\]__ __Tratamento p/ agrupar os Itens com o mesmo Código de Serviço, para o município de Caxias do Sul\.__

\- Deverá ser gerado uma “linha” para cada Código de Serviço, e deve\-se agrupar todos os itens de serviço das notas fiscais que possuírem o mesmo código de serviço\.

\- Dos itens agrupados, os campos “valorTotal, valorDeduca, baseCalculo e valorISS” deverão ser sumarizados por Número de Nota Fiscal e Código de Serviço\.

__Por exemplo: __

Se a Nota Fiscal possuir 3 itens, 2 deles com o mesmo código de Serviço, nesse caso serão gravados apenas 2 itens no arquivo meio magnético, sendo um referente ao item 1 e 2, \(que serão agrupados\) e o segundo referente ao item 3\. No primeiro contendo as informações dos itens com o mesmo código de serviço e o segundo com o outro código de serviço\.

- Não será considerado documento sem item;

__\[INCLUSÃO – MFS903857\] __A regra abaixo deve ser aplicada para o validador DMSTE, abrangendo todos os municípios que utiliza esse validador\.

__Notas Fiscais eletrônicas de Serviços Tomados: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

Default: Desmarcado

__ \-  Se__ a __UF__ e o __Município __do estabelecimento não estiverem parametrizados no Módulo > Parâmetro por Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

__ MFS11982__

__ MFS903857__

__MFS\-1024956__

__RN09__

__Estrutura do Arquivo:__

__*Exemplo de XML de Serviços Tomados:*__

<?xml version="1\.0" encoding="utf\-8"?>

 <declaracoes>

  <lote versao="1\.0">

    <numeroLote>1</numeroLote>

    <dhTrans>2015\-05\-05 09:01:00</dhTrans>   

    <imRemetente>123456</imRemetente>       

    <imTomador>123456</imTomador>              

    <competencia>201505</competencia> 

    <servicosTomados>

      <servicoTomado>

        <prestador>

          <nome>Infisc</nome>

          <cpfCnpj>08967207000141</cpfCnpj>

          <codigoMunicipio>4305108</codigoMunicipio>

          <nomeMunicipio>Caxias do Sul</nomeMunicipio>

          <uf>RS</uf>

          <pais>Brasil</pais>

          <inscricaoEstadual>ISENTO</inscricaoEstadual>

          <inscricaoMunicipal>18195</inscricaoMunicipal>

          <logradouro>Julio de Castilhos</logradouro>

          <numeroLogradouro>100</numeroLogradouro>

          <complementoLogradouro>Sala 508</complementoLogradouro>

          <bairro>Centro</bairro>

          <cep>95600000</cep>

          <ddd>51</ddd>

          <fone>81881032</fone>

        </prestador> 

        <documento>

          <especie>NFSE</especie>   

          <serie>S</serie> 

          <numero>16</numero>

          <numeroNacional>16</numeroNacional>  

          <dataEmissao>2015\-04\-28</dataEmissao>

          <status>N</status> 

          <codigoLei116Principal>0801</codigoLei116Principal> __\[ALTERAÇÃO MFS\-754955/MFS\-834548\]__ Esta tag só deve estar disponível para os municípios de Carlos Barbosa e Canoas  
          <codigoMunicipioTributacao>4305108</codigoMunicipioTributacao>

          <tipoISS>M</tipoISS> 

          <codigoServico>010101</ codigoServico > __\[MFS\-834548\]__ Esta tag só deve estar disponível para o município de Canoas  
       </documento>

       <totais>

         <valorTotal>1000\.00</valorTotal>

         <valorDeducao>20\.00</valorDeducao>

         <baseCalculo>980\.00</baseCalculo>

         <aliquota>4\.00</aliquota>

         <valorISS>39\.20</valorISS>

       </totais>

      </servicoTomado>

    </servicosTomados>

   </lote>

  <Signature> … </Signature>

</declaracoes>

__MFS11982__

__MFS\-754955__

__MFS\-834548__

__MFS\-1048839__

__RN10__

__Regra para tag <?xml version="1\.0" encoding="utf\-8"?> __

Tag relacionada à formatação do arquivo deve conter o texto fixo: __<?xml version="1\.0" encoding="utf\-8"?>__

TAG obrigatória\.

__MFS11982__

__RN11__

__Regra para tag <declaracoes> __

Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __<declaracoes>\.__

TAG obrigatória\.

__MFS11982__

__RN12__

__Regra para o campo <lote versao= “1\.0” > __

Tag que identifica o layout do arquivo\. Preencher com o conteúdo fixo: __“1\.0”\.__

TAG obrigatória\.

__MFS11982__

__RN13__

__Regra para o campo <numeroLote> da TAG </numeroLote>__

Tag que identifica o número do lote\. Preencher com a informação digitada pelo usuário na tela de geração do meio magnético\.

Formato: 999999

Tamanho: 6 posições

Tipo: Numérico

__MFS11982__

__RN14__

__Regra para o campo <dhTrans> da TAG </dhTrans>__

Identifica a data e hora da transmissão da geração do meio magnético\. Preencher com a data e hora em que o arquivo foi gerado\. \(Utilizar sysdate\)\.

Tem o formato __AAAA\-MM\-DDTHH:MM:SS__ onde:

- __AAAA__ representa o ano com quatro caracteres, 
- __MM__ representa o mês com dois caracteres, 
- __DD__ representa o dia com dois caracteres, 
- __T__ representa o caractere de formatação __\(devendo ser usado um espaço em branco\)__ que deve existir separando a data da hora, 
- __HH__ representa a hora com dois caracteres, 
- __MM__ representa os minutos com dois caracteres; 
- __SS__ representa os segundos com dois caracteres __\(não sendo obrigatório incluir os segundos__\)\.

TAG Obrigatória\.

Formato: AAAA\-MM\-DDTHH:MM:SS

Tamanho: 19 posições

Tipo: Data

__MFS11982__

__RN15__

__Regra para o campo <imRemetente> da TAG </imRemetente >__

Tag que identifica a Inscrição Municipal do Remetente do lote\. Será gerado com o conteúdo do campo __INSC\_MUNICIPAL__ da tabela de __ESTABELECIMENTO__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 14 posições, então para atender a obrigação deverão ser desconsideradas as últimas posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de ‘12345678912345’ deverá ser informado ‘123456’\.

- Se o campo <imRemetente> estiver com o tamanho acima do máximo permitido \(6 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <imRemetente> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

TAG Obrigatória

Formato: 999999 

Tamanho: 6 posições

Tipo: Numérico

__MFS11982__

__RN15\.a__

__Regra para o campo <imRemetente> da TAG </imRemetente > para o município de Canoas__

__\[MFS921327\] __Alteração do preenchimento do campo para a geração da Construção Civil

Tag que identifica a Inscrição Municipal do Remetente do lote\. 

__Se __a geração do arquivo selecionada for igual a “Arquivos de Entrada de Serviços \(Const\.Civil / Utilities/ Telecom\)”

      Será gerado com o conteúdo do campo inscrição municipal eventual da tabela X156\_CAD\_INSC\_MUN, cadastrada para o 

      estabelecimento em que está sendo gerado o arquivo magnético

__Senão__

      Será gerado com o conteúdo do campo __INSC\_MUNICIPAL__ da tabela de __ESTABELECIMENTO__\.

TAG Obrigatória

Formato: 999999999999999 

Tamanho: 15 posições

Tipo: Numérico

__MFS826035__

__MFS921327__

__RN16__

__Regra para o campo <imTomador > da TAG </imTomador >__

Tag que identifica a Inscrição Municipal do Tomador\. Será gerado com o conteúdo do campo __INSC\_MUNICIPAL__ da tabela de __ESTABELECIMENTO\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 14 posições, então para atender a obrigação deverão ser desconsideradas as últimas posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de ‘12345678912345’ deverá ser informado ‘123456’\.

- Se o campo <imTomador> estiver com o tamanho acima do máximo permitido \(6 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <imTomador> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

TAG Obrigatória

Formato: 999999 

Tamanho: 6 posições

Tipo: Numérico

__MFS11982__

__RN16\.a__

__Regra para o campo <imTomador > da TAG </imTomador > para o município de Canoas__

__\[MFS908810\] __Alteração do preenchimento do campo para a geração da Construção Civil

Tag que identifica a Inscrição Municipal do Tomador\. 

__Se __a geração do arquivo selecionada for igual a “Arquivos de Entrada de Serviços \(Const\.Civil / Utilities/ Telecom\)”

      Será gerado com o conteúdo do campo inscrição municipal eventual da tabela X156\_CAD\_INSC\_MUN, cadastrada para o 

      estabelecimento em que está sendo gerado o arquivo magnético

__Senão__

      Será gerado com o conteúdo do campo __INSC\_MUNICIPAL__ da tabela de __ESTABELECIMENTO\.__

TAG Obrigatória

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico

__MFS826035__

__MFS908810__

__RN17__

__Regra para o campo <competencia> da TAG </competencia>__

__\[MFS767622\]__ Alteração da regra de preenchimento para tratar a data de emissão da nota

Identifica o ano e mês da competência\.

__Se__ o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado

      Preencher com o mês e o ano referente à data de emissão das notas fiscais geradas no arquivo 

__Senão __ 

       Preencher com o mês e o ano informados no campo __Data Inicial da tela Obrigações – Meio Magnético__\.

TAG Obrigatória\.

Formato: AAAAMM

Tamanho: 6 posições

Tipo: Data

__MFS11982__

__MFS767622__

__RN18__

__Regra para o campo <servicosTomados> __Tag relacionada à abertura dos Serviços Tomados com o texto fixo: __<servicosTomados>__

TAG obrigatória\.

__MFS11982__

__RN19__

__Regra para o campo <servicoTomado> __Tag relacionada à abertura das informações do Serviço Tomado com o texto fixo: __<servicoTomado>__

__MFS11982__

__RN20__

__Regra para o campo <prestador> __Tag relacionada à abertura dos dados do prestador do serviço com o texto fixo__ <prestador>__

TAG obrigatória\.

__MFS11982__

__RN21__

__Regra para o campo <nome> da TAG <prestador>__

Identifica o nome do Prestador\. Preencher com a informação do campo RAZAO\_SOCIAL __\(Campo 05\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ 

__Observação Importante: __Se for prestador __estrangeiro__ UF = EX, apenas os campos *<nome>* e *<pais>* serão obrigatórios para a TAG de <prestador> as demais são opcionais\.

TAG Obrigatória

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN22__

__Regra para o campo <cpfCnpj> da TAG <prestador>__

Identifica o documento do Prestador\. Preencher a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ 

Deve conter 11 \(para CPF\) ou 14 \(para CNPJ\)\. 

__Observação:__ Apenas números, sem pontos, traços, espaços ou qualquer outro caracter\.

TAG Obrigatória

Formato: 99999999999999

Tamanho: 11 / 14 posições

Tipo: Alfanumérico

__MFS11982__

__RN23__

__Regra para o campo <codigoMunicipio> da TAG <prestador>__

Identifica o código do município do prestador conforme IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela\.

__Observação: __Apenas números, sem pontos, traços, espaços ou qualquer outro Caracter\.

TAG Obrigatória

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11982__

__RN24__

__Regra para o campo <nomeMunicipio> da TAG <prestador>__

Identifica a cidade do prestador\. Preencher com a informação\. Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao COD\_MUNICIPIO preenchido na tabela X04\_PESSOA\_FIS\_JUR\.

TAG Obrigatória

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN25__

__Regra para o campo <uf> da TAG <prestador>__

Identifica a sigla do estado do prestador\. Preencher com a informação do campo UF __\(campo 19\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

TAG Obrigatória

Formato: XX 

Tamanho: 2 posições

Tipo: Alfanumérico

__MFS11982__

__RN26__

__Regra para o campo <pais> da TAG <prestador>__

Identifica o nome do país do prestador\. Preencher com a descrição do País\. Deverá utilizar o campo DESCRICAO da tabela PAIS, referente ao código do país cadastrado no campo COD\_PAIS da tabela SAFX04\.

__Observação Importante: __Se for prestador __estrangeiro__ UF = EX, apenas os campos *<nome>* e *<pais>* serão obrigatórios para a TAG de <prestador> as demais são opcionais\.

__Tratamento:__

__\- __Se o campo <pais> não estiver preenchido\. Exibir uma mensagem no log: “O campo <pais> do prestador não está preenchido, favor verificar”\.

TAG Obrigatória

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN27__

__Regra para o campo <inscricaoEstadual> da TAG <prestador>__

Identifica a inscrição estadual do Prestador\. Preencher com o campo __INSC\_ESTADUAL__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

__Tratamento:__

- Se o prestador não tiver valor para o campo <inscricaoEstadual> deverá ser preenchido com __“ISENTO “\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS11982__

__RN28__

__Regra para o campo <inscricaoMunicipal> da TAG <prestador>__

Identifica a inscrição municipal do prestador\. Preencher com o campo __INSC\_MUNICIPAL__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS11982__

__RN29__

__Regra para o campo <logradouro> da TAG <prestador>__

Identifica o endereço do prestador\. Preencher com a informação do campo ENDERECO __\(campo 12\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN30__

__Regra para o campo <numeroLogradouro> da TAG <prestador>__

Identifica o número do endereço do prestador\. Preencher com a informação do campo NUM\_ENDERECO __\(campo 13\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: 999999 

Tamanho: 6 posições

Tipo: Numérico

__MFS11982__

__RN31__

__Regra para o campo <complementoLogradouro> da TAG <prestador>__

Identifica o complemento do endereço do prestador\. Preencher com a informação do campo COMPL\_ENDERECO __\(campo 14\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN32__

__Regra para o campo <bairro> da TAG <prestador>__

Identifica o Bairro do prestador\. Preencher com a informação do campo BAIRRO __\(campo 15\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 100 posições

Tipo: Alfanumérico

__MFS11982__

__RN33__

__Regra para o campo <cep> da TAG <prestador>__

Identifica o CEP da cidade do prestador\. Preencher com a informação do campo CEP __\(campo 20\)__ da tabela __X04\_PESSOA\_FIS\_JUR__

__Observação: __Código postal da EBCT, informando apenas números, sem pontos, traços ou qualquer outro Caracter\.

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__MFS11982__

__RN34__

__Regra para o campo <ddd> da TAG <prestador>__

Identifica o código para telefone\. Preencher com o campo DDD __\(campo 22\) __da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: 999

Tamanho: 3 posições

Tipo: Numérico

__MFS11982__

__RN35__

__Regra para o campo <fone> da TAG <prestador>__

Identifica o número do telefone do prestador\.

Preencher com a informação do campo Telefone __\(campo 23\)__ considerando as 8 primeiras posições \(ignorar hífen\) da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: 99999999999999

Tamanho: 14 posições

Tipo: Numérico

__MFS11982__

__RN36__

__Regra para o campo <prestador> __Tag relacionada ao encerramento dos dados do prestador do serviço com o texto fixo:__ </prestador>__

__MFS11982__

__RN37__

__Regra para o campo <documento> __Tag relacionada à abertura dos dados da nota fiscal com o texto fixo:__ <documento>__

TAG obrigatória\.

Se DWT\_DOCTO\_FISCAL \- MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL \- COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e WT\_DOCTO\_FISCAL \- SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL \- IND\_TP\_RET = 1 e \(\(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS > 0,00 e DWT\_ITENS\_SERV \- VLR\_ISS > 0,00\) ou \(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS\_RETIDO > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO > 0,00\)\) e 

DWT\_DOCTO\_FISCAL \- COD\_MUNICIPIO = Município do módulo selecionado então gerar <documento>

Senão

    NÃO gerar <documento>, ir para o próximo documento\.

__MFS11982__

__MFS\-646002__

__RN38__

__Regra para o campo <especie> da TAG <documento>__

A lista de Documentos \(segundo o tipo TEspecie\) que este campo pode assumir, está carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG\) é:__ __

- BL – Boleto, 
- CF – Cupom Fiscal, 
- CTRC – Conhecimento de Transporte Rodoviário de Cargas,
- CUPOM – Cupom,
- ING – Ingresso,
- ND – Não Disponível,
- NF – Nota Fiscal,
- NFE – Nota Fiscal Eletrônica \(Outros municípios\),
- NFSE – Nota Fiscal de Serviços eletrônica \(Caxias do Sul\),
- NFF – Nota Fiscal Fatura,
- NFFSE – Nota Fiscal Fatura de Serviço eletrônica \(Caxias do Sul\),
- REC – Recibo
- RPS – Recibo Provisório de Serviços
- SPE – Serviço Proveniente do Exterior

__Regra de Preenchimento:__

__Parametrização de Tipo Docto Msaf x Espécie__

Preencher com o campo Tipo Documento da tela Municipal – Parâmetros para Município – Tipo Docto Msaf x Espécie referente ao Código do Tipo do Documento cadastrado na nota\.

__Tratamento:__

- Se não existir parametrização para a espécie do documento fiscal, o sistema deve exibir no log uma mensagem padrão de alerta para o usuário\. 

TAG obrigatória

Formato: XXXXX

Tamanho: 5

Tipo: Alfanumérico

__MFS11982__

__MFS71302__

__RN39__

__Regra para o campo <serie> da TAG <documento>__

A lista de séries \(segundo o tipo TSerie\), conforme o manual layout que este campo pode assumir está carregada na __TFIX83__ \(Cadastro das Séries/Modelos das Obrigações \- PRT\_SERIE\_OBRIG\) é:

- ND – Serie ND, 
- S/S – Serie S/S, 
- UNI – Serie UNI, 
- B – Serie B, 
- M\-8 – Serie M\-8, 
- A – Serie A, 
- A\-1 – Serie A\-1,
- A\-2 – Serie A\-2,
- B – Serie B,
- B\-1 – Serie B\-1,
- B\-2 – Serie B\-2,
- M\-1 – Serie M\-1,
- M\-7 – Serie M\-7,
- S – Serie S,
- A1 – Serie A1

__Regra de Preenchimento:__

__Parametrização de Série Msaf x Série__

Preencher com o campo Série da tela Municipal – Parâmetros para Município – Série Msaf x Série referente à série cadastrada na Nota Fiscal\.

__Tratamento:__

- Se não existir parametrização para a série da nota, o sistema deve exibir no log uma mensagem padrão de alerta para o usuário\. 

TAG obrigatória

Formato: XXXXX

Tamanho: 5

Tipo: Alfanumérico

__MFS11982__

__MFS71302__

__RN40__

__Regra para o campo <numero> da TAG <documento>__

Identifica o número do documento fiscal, número da Nota Fiscal de Serviços eletrônica, formado por um número crescente e sequencial\. Preencher com a informação do campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__ __\(campo 08 da SAFX07\)__

TAG Obrigatória\.

Formato: 999999999 

Tamanho: 9 posições

Tipo: Alfanumérico

__MFS11982__

__RN41__

__Regra para o campo <numeroNacional> da TAG <documento> __

Municípios a serem acrescentados nessa regra __Campo Bom, Canoas, Carlos Barbosa, Caxias Do Sul e São Borja\.__

Identifica o número do documento fiscal, número da Nota Fiscal de Serviços eletrônica, formado por um número crescente e sequencial\. Preencher com a informação do campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__ __\(campo 08 da SAFX07\)__

Número Nacional da NFSe, enviar para notas com data superior a 01/01/2026\.

TAG Não Obrigatória\.

Formato: 999999999 

Tamanho: 9 posições

Tipo: Alfanumérico

__MFS\-1048839__

__RN42__

__Regra para o campo <dataEmissao> da TAG <documento>__

Identifica à data de emissão do documento fiscal\. Preencher com a informação do campo __DATA\_EMISSAO__ da tabela __DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)__

TAG Obrigatória

Formato: AAAA\-MM\-DD *Exemplo: *2017\-07\-11

Tamanho: 10 posições

Tipo: Data\.

__MFS11982__

__RN43__

__Regra para o campo <status> da TAG <documento>__

Identifica o status da nota fiscal\. 

Se na nota fiscal o campo SITUACAO for = “S” da SAFX07, preencher com “__C__” para Nota Cancelada\.

Senão preencher com “__N__” para nota Não cancelada\. 

__Tratamento:__

- Caso o documento fiscal esteja cancelado, o sistema deverá emitir a seguinte mensagem de alerta para o usuário: “A Nota Fiscal encontra\-se cancelada, favor preencher o campo Dt\.Autentic/Cancel com a Data de Cancelamento da Nota”\.

Formato: X 

Tamanho: 1 posição

Tipo: Caracter\.

__MFS11982__

__RN42\.a__

__RN44__

__Para os municípios de Carlos Barbosa e Canoas:__

__Regra para o Campo <codigoLei116Principal> da TAG <documento>__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

Deve ser informado apenas números, sem pontos, traços, espaços ou qualquer outro caractere\.

Tratamento:

- Se o campo COD\_SERV\_LEI\_116 não estiver preenchido, Exibir uma mensagem no log: “O campo <COD\_SERV\_LEI\_116> não está preenchido, favor verificar”\.

TAG Obrigatória

Formato: NNNN 

Tamanho: 4 posições

__MFS\-754955__

__MFS\-834548__

__RN45__

__Regra para o campo <dataCancelamento> da TAG <documento>__

Identifica a data de cancelamento da Nota Fiscal\. Preencher com a informação do campo __DAT\_AUTENTIC__ __\(campo 80 da SAFX07\)__ quando na nota fiscal o campo SITUACAO for = “S” da SAFX07\. 

Formato: AAAA\-MM\-DD *Exemplo: *2017\-07\-11

Tamanho: 10 posições

Tipo: Data\.

__MFS11982__

__RN46__

__Regra para o campo <codigoMunicipioTributacao> da TAG <documento>__

Identifica o código do município conforme a tabela do IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao __COD\_MUNICIPIO \(Campo 73\)__ da tabela __X07\_DOCTO\_FISCAL__\. 

__Observação:__ Os zeros à esquerda precisam ser indicados no código do município\. Por exemplo, o código do IBGE para Caxias do Sul – RS é 4305108 e tem que ser indicado nas tags como 4305108, não desprezando qualquer zero que exista entre a indicação da UF \(__43 para a UF Rio Grande do Sul__\) e do Município \(__05108 para o município Caxias do Sul__\)\.

Formato: 9999999 – Somente números sem formatação\.

Tamanho: 7 posições

Tipo: Numérico\. 

__MFS11982__

__RN47__

__Regra para o campo <tipoISS> da TAG <documento>__

Identifica o tipo de ISSQN conforme a sessão 2\.2 do layout\.

__Preencher com ‘F’__ __– ISSQN Fora do Município: __Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472” E Se o campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL\) referente ao local de prestação de serviço cadastrado na nota fiscal for DIFERENTE do município do prestador do serviço campo COD\_MUNICIPIO da tabela SAFX04 referente à Pessoa Física / Jurídica cadastrada na nota fiscal\.

__Preencher com ‘M’ – ISSQN Retido:__ Verificar se uma das condições abaixo é verdadeira:

Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" __OU__

Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO __OU__

Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

Caso nenhuma das opções acima seja verdadeira

Preencher com __‘N’ – ISSQN Não Retido:__

TAG obrigatória\.

Formato: X 

Tamanho: 1 posição

Tipo: Caracter\.

__MFS11982__

__MFS\-1024956__

__RN45\.a__

__RN48__

__Para o município de Canoas:__

__Regra para o campo <codigoServico> da TAG <documento>__

Identifica o código da atividade do serviço prestado\. Preencher com o campo Serviço da tela Municipal – Parametros por Município – Parâmetros – Serviço Msaf x Serviço, referente ao serviço cadastrado na nota fiscal\. 

__Tratamento:__

- Se não houver parametrização para o serviço cadastrado na nota fiscal, deve ser exibida a seguinte mensagem de log: “O serviço não foi parametrizado na tela Parâmetros para Município – Parâmetros – Serviço Msaf x Serviço\. Favor verificar\.”\.
- Se não houver parametrização para o serviço cadastrado na nota fiscal deixar o campo em branco\.

Identifica o código da atividade do serviço prestado\. Preencher com a informação do campo COD\_ATIVIDADE__ \(campo 22 da SAFX2018\)__ referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. 

Formato: X

Tipo: Caracter\.

__MFS834548__

__MFS915209__

__RN49__

__Regra para o campo </documento> __Tag relacionada ao encerramento dos dados da nota fiscal com o texto fixo:__ </documento>__

TAG obrigatória\.

__MFS11982__

__RN50__

__Regra para o campo <totais> __Tag relacionada à abertura da totalização da nota fiscal com o texto fixo:__ <totais>__

TAG obrigatória\.

Se DWT\_DOCTO\_FISCAL \- MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL \- COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e WT\_DOCTO\_FISCAL \- SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL \- IND\_TP\_RET = 1 e \(\(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS > 0,00 e DWT\_ITENS\_SERV \- VLR\_ISS > 0,00\) ou \(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS\_RETIDO > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO > 0,00\)\) e 

DWT\_DOCTO\_FISCAL \- COD\_MUNICIPIO = Município do módulo selecionado então gerar <totais>

Senão

    NÃO gerar <totais>, ir para o próximo documento\.

__MFS11982__

__MFS\-646002__

__RN51__

__Regra para o campo <valorTotal> da TAG <totais>__

Identifica o valor total dos serviços constantes no documento fiscal\. Preencher com o campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\.__ 

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <valorTotal> estiver com o tamanho acima do máximo permitido \(13,2 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <valorTotal> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

TAG obrigatória\.

Formato: 9999999999999\.99 

Tamanho: 13,2 posições

Tipo: Numérico

__MFS11982__

__RN52__

__Regra para o campo <valorDeducao > da TAG <totais>__

Identifica o valor de Dedução da Nota Fiscal\. Preencher com o campo __VLR\_DEDUCAO\_ISS__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

Formato: 9999999999999\.99 

Tamanho: 13,2 posições

Tipo: Numérico

__MFS11982__

__RN53__

__Regra para o campo <baseCalculo> da TAG <totais>__

Esse campo identifica a base de cálculo do Serviço tomado\. Preencher com o campo __VLR\_BASE\_ISS\_1__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <baseCalculo> estiver com o tamanho acima do máximo permitido \(13,2 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <baseCalculo> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

Se DWT\_DOCTO\_FISCAL\- MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL \- COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e WT\_DOCTO\_FISCAL \- SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL \- IND\_TP\_RET = 1 e \(\(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS > 0,00 e DWT\_ITENS\_SERV \- VLR\_ISS > 0,00\) ou \(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS\_RETIDO > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO > 0,00\)\) e 

\(DWT\_ITENS\_SERV \- ALIQ\_TRIBUTO\_ISS > 0 ou DWT\_ITENS\_SERV \- VLR\_ALIQ\_ISS\_RETIDO > 0\) e DWT\_DOCTO\_FISCAL\-COD\_MUNICIPIO = Município do módulo selecionado então

    Preencher tag <baseCalculo>, com o somatório do campo DWT\_ITENS\_SERV\-VLR\_BASE\_ISS ou DWT\_ITENS\_SERV\-VLR\_BASE\_ISS\_RETIDO

Fim Se

TAG obrigatória\.

Formato: 9999999999999\.99 

Tamanho: 13,2 posições

Tipo: Numérico

__MFS11982__

__MFS\-646002__

__RN54__

__Regra para o campo <aliquota> da TAG <totais>__

Esse campo identifica a Alíquota do Serviço tomado\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV __

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverão ser desconsideradas as duas últimas posições da parte fracionaria para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123,4567, gravar 123\.45
- Se o campo <aliquota> não estiver preenchido no item do documento fiscal, preencher com zeros de acordo com o tamanho exigido pela prefeitura\. Exibir uma mensagem de alerta para o usuário no log: “O campo <aliquota> não está preenchido, favor verificar”\.

Se DWT\_DOCTO\_FISCAL \- MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL \- COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e WT\_DOCTO\_FISCAL \- SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL \- IND\_TP\_RET = 1 e \(\(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS > 0,00 e DWT\_ITENS\_SERV \- VLR\_ISS > 0,00\) ou \(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS\_RETIDO > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO > 0,00\)\) e 

\(DWT\_ITENS\_SERV \- ALIQ\_TRIBUTO\_ISS > 0 ou DWT\_ITENS\_SERV \- VLR\_ALIQ\_ISS\_RETIDO > 0\) e DWT\_DOCTO\_FISCAL\-COD\_MUNICIPIO = Município do módulo selecionado então

    Preencher tag <aliquota>, com os dados do campo DWT\_ITENS\_SERV\- ALIQ\_TRIBUTO\_ISS ou DWT\_ITENS\_SERV\- VLR\_ALIQ\_ISS\_RETIDO

TAG obrigatória\.

Formato: 999\.99 

Tamanho: 3,2 posições

Tipo: Numérico

__MFS11982__

__MFS\-646002__

__RN55__

__Regra para o campo__ __<valorISS>__ da TAG __<totais>__

Esse campo identifica o valor do ISSQN\. Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

             Exemplo: Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <valorISS> estiver com o tamanho acima do máximo permitido \(13,2 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <valorISS> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

Se DWT\_DOCTO\_FISCAL \- MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL \- COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e DWT\_DOCTO\_FISCAL \- SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL \- IND\_TP\_RET = 1 e \(\(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS > 0,00\) ou \(DWT\_ITENS\_SERV \- VLR\_BASE\_ISS\_RETIDO > 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO > 0,00\)\) e \(DWT\_ITENS\_SERV \- ALIQ\_TRIBUTO\_ISS > 0 ou DWT\_ITENS\_SERV \- VLR\_ALIQ\_ISS\_RETIDO > 0\) e DWT\_DOCTO\_FISCAL \- COD\_MUNICIPIO = Município do módulo selecionado então

    Preencher tag <valorISS>, com o somatório do campo DWT\_ITENS\_SERV\- VLR\_ISS ou DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO

TAG obrigatória\.

Formato: 9999999999999\.99 

Tamanho: 13,2 posições

Tipo: Numérico

__MFS11982__

__MFS\-646002__

__RN56__

__Regra para o campo </totais> __Tag relacionada ao encerramento da totalização da nota fiscal com o texto fixo:__ </totais>__

TAG obrigatória\.

__MFS11982__

__RN57__

__Regra para o campo </servicoTomado> __Tag relacionada ao encerramento das informações das notas de serviços tomados com o texto fixo:__ </servicoTomado>__

TAG obrigatória\.

__MFS11982__

__RN58__

__Regra para o campo </servicosTomados> __Tag relacionada ao encerramento das informações dos serviços tomados com o texto fixo:__ </servicosTomados>__

TAG obrigatória\.

__MFS11982__

__RN59__

__Regra para o campo </lote> __Tag relacionada ao encerramento do lote do arquivo que receberá as informações das notas tomadas com o texto fixo:__ </lote>\.__

__MFS11982__

__RN60__

__Regra para o campo <Signature> da TAG </Signature>__

Essa TAG não será gerada na estrutura do XML\.

__MFS11982__

__RN61__

__Regra para o campo </declaracoes> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo:__ </declaracoes>__

TAG obrigatória\.

__MFS11982__

__RN62__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Campo Bom” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste em registrar todas as informações sobre as notas fiscais de serviços tomados, emitidas em papel ou por meio eletrônico \(NFS\-e\), por um contribuinte ao longo de um determinado mês”\.

__MFS71302__

__RN63__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “3905” \(Campo Bom\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Campo Bom, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS71302__

__RN64__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Canoas” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste em registrar todas as informações sobre as notas fiscais de serviços tomados, emitidas em papel ou por meio eletrônico \(NFS\-e\), por um contribuinte ao longo de um determinado mês”\.

__MFS618623__

__RN65__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “4606” \(Canoas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Canoas, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS618623__

__RN66__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Calos Barbosa” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste em registrar todas as informações sobre as notas fiscais de serviços tomados, emitidas em papel ou por meio eletrônico \(NFS\-e\), por um contribuinte ao longo de um determinado mês”\.

__MFS\-703003__

__RN67__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “4804” \(Carlos Barbosa\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Carlos Barbosa, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-703003__

__RN68__

__Regra para inclusão do novo módulo no Manager:__

O módulo “São Borja” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste em registrar todas as informações sobre as notas fiscais de serviços tomados, emitidas em papel ou por meio eletrônico \(NFS\-e\), por um contribuinte ao longo de um determinado mês”\.

MFS\-[890983](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/890983)

__RN69__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “8002” \(São Borja\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Carlos São Borja, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-[890983](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/890983)

