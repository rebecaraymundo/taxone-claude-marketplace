# MTZ_DMSe_Geracao_do_Meio_Magnetico_Campo_Bom

- **Fonte:** MTZ_DMSe_Geracao_do_Meio_Magnetico_Campo_Bom.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Municipal – DMSe Campo Bom

##### DOCUMENTO DE REQUISITO

__Data__

__OS/CH__

__Nome__

__Descrição__

15/08/2014

OS4564

Marcos G\. de Paula

Criação do Documento

11/05/2016

__MFS\_2071__

João Henrique

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

05/10/2025

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Campo Bom deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Campo Bom: “Consiste na entrega das informações sobre os serviços tomados do município de Campo Bom”\.

OS4564

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “03905” \(Campo Bom\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Campo Bom, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

OS4564

RN03

__Estrutura de menus do módulo DMS\-e:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DMS\-e:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__

OS4564

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.XML__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.XML

__ST\_DMSE\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

__DDMMAAAA__: representa a data inicial da geração

__MUNICIPIO__: representa o município que está sendo gerado\.

__ST\_DMSE__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__\.XML__: extensão do arquivo\.

Ex: ST\_DMSE\_CAMPOBOM\_01012010\.XML

OS4564

MFS829438

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Número do Lote: __O campo deve ser um text Box\.__ __O campo deve permitir que o usuário digite o sequencial desejado, com no máximo 4 posições\. Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

__Responsável pela Entrega:__ deve ser um dropdownlist\. O campo deve exibir a relação de Responsáveis cadastrados na tela de Responsável por Informações \(Módulo Parâmetros / Menu Requisitos Legais >> Responsável por Informações\)\. Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Campo Bom, que estejam licenciados e que o usuário possua acesso no PowerLock\.

OS4564__ MFS\_2071__

RN06

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos\.

O arquivo a ser gerado para importação dever ser no formato __‘XML’;__

Não incluir comentários no arquivo XML;

Não incluir anotação e documentação no arquivo XML \(TAG annotation e TAG documentation\);

Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as TAGs\);

Acentos e caracteres especiais devem ser suprimidos do arquivo, conforme exigência do validador\.

__Campo tipo Data \(date\)__

Campos tipo Data devem ser preenchidos no seguinte formato: AAAA\-MM\-DD ;

__Campo de Valores Decimais__

Os valores decimais devem ser no formato: “__0\.00”__\.

Não deve ser utilizado separador de milhar\. O ponto \(__\.__\) deve ser utilizado para separar a parte inteira da fracionária:

Exemplo: 48\.562,25 = 48562\.25 / 1,00 = 1\.00 ou 1 / 0,50 = 0\.50 ou 0\.5

__Campo de Valores Percentuais__

Os valores percentuais devem ser preenchidos no formato: “0\.0000”\.

O formato em percentual presume o valor percentual em sua forma fracionária, contendo 5 dígitos\. O ponto \(\.\) separa a parte inteira da fracionária\.

Exemplo: 62% = 62 / 150% = 150 / 25,32% = 25\.32

__Campo tipo Numérico__

Não incluir “zeros não significativos” para campos numéricos;

Não incluir “espaços” no início ou no final de campos numéricos

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

__Campo tipo Texto__

Não deve ser inseridos espaços em branco após o preenchimento

Não inserir espaços no inicio ou fim dos campos;

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

As tags que permitirem valores nulos devem ser omitidas da estrutura XML a ser enviada quando seus valores forem nulos\.

OS4564

RN07

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)__

Considerar todas as notas com as seguintes características:

- Documentos de entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.

Quando a nota não tiver itens não deve ser recuperada\.

OS4564

RN08

__<?xml version="1\.0" encoding="utf\-8"?>__

Tag relacionada à formatação do arquivo deve conter o texto fixo: __‘<?xml version="1\.0" encoding="utf\-8"?>’\.__

Campo obrigatório\.

OS4564

RN09

__Regra para TAG <declaracoes></declaracoes>__

TAG que indica abertura da declaração, sendo aberta no início do XML e encerrada no final\.

TAG obrigatória\.

OS4564

RN10

__Regra p/ tag <lote versao="1\.0">__

TAG onde deve conter os dados da estrutura do lote de Notas Fiscais para fila de processamento\.

Deve ser gerada somente 1 vez no arquivo e encerrada com o formato __</lote>__

Campo obrigatório\.

OS4564

RN11

__Regra p/ tag <numeroLote></numeroLote>__

Preencher com o campo “Número do Lote” da tela de geração do meio magnético\.

Sequencial numérico por arquivo gerado\.

Tipo: N / Tam: 4

Campo obrigatório\.

OS4564

RN12

__Regra p/ tag <dhTrans></dhTrans>__

Preencher com a Data e Hora de geração do arquivo, no formato “AAAA\-MM\-DD HH:MM:SS”

OS4564

RN13

__Regra p/ tag <docRemetente></docRemetente>__

Preencher com a informação do campo CPF/CNPJ do “Responsável pela Entrega” parametrizado na tela de geração do meio magnético\.

OS4564

RN14

__Regra p/ tag <docContribuinte></docContribuinte>__

Preencher com o campo CGC da tabela ESTABELECIMENTO do estabelecimento de geração do arquivo\.

Campo obrigatório\.

OS4564

RN15

__Regra para tag <servicosTomados></servicosTomados>__

TAG que indica início da demonstração das informações de serviços tomados, sendo demonstrada como filha da tag <lote> e encerrada no final da demonstração das informações\.

TAG obrigatória\.

OS4564

RN16

__Regra para tag <servicoTomado></servicoTomado>__

Esta tag será demonstrada sempre que a regra de seleção dos serviços tomados \(RN07\) __FOR__ atendida\. Para cada NF de Serviço Tomado encontrada na base será gerada uma tag <servicoTomado> e na sequência as suas tags filhas detalhando as notas\.

OS4564

RN17

__Regra para tag <emitente></emitente>__

TAG filha da tag <servicoTomado>\. Será gerada com base na SAFX04 para demonstrar as informações dos prestadores dos serviços tomados associados às NFs considerados na seleção inicial\.

OS4564

RN18

__Regra para tag <CPF></CPF> ou <CNPJ></CNPJ>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo CPF\_CGC da SAFX04\.

Se o conteúdo do campo tiver 11 posições, será gerado como tag <CPF></CPF>\. Se o conteúdo tiver 14 posições, será gerado <CNPJ></CNPJ>\.

OS4564

RN19

__Regra para tag <IE></IE>__

Campo pertencente à tag <emitente>\. Será gerado o conteúdo do campo INSC\_ESTADUAL da SAFX04\.

Tamanho máximo: 20

OS4564

RN20

__Regra para tag <IM></IM>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo INSC\_MUNICIPAL da SAFX04\.

Tamanho máximo: 20

OS4564

RN21

__Regra para tag <xNome></xNome>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo RAZAO\_SOCIAL da SAFX04\.

Tamanho máximo: 70

OS4564

RN22

__Regra para tag <xLgr></xLgr>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo ENDERECO da SAFX04\.

Tamanho máximo: 100

OS4564

RN23

__Regra para tag <nro></nro>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo NUM\_ENDERECO da SAFX04, considerando as 5 últimas posições do campo \(por se tratar de um campo alfanumérico na SAFX04 consideramos as 5 últimas\)\.

Se o tamanho do campo tiver mais de 5 posições e for aplicada a regra de seleção dos 5 últimos, retornar a mensagem no log: “A tag “__<nro>__” foi gerada com as 5 últimas posições do campo Número na SAFX04 para o emitente <__<CPF></CPF> ou <CNPJ></CNPJ>__>\*\. Avaliar necessidade de ajuste”\.

*\* Demonstrar o CPF/CNPJ gerado no arquivo para que o usuário possa identificar onde está o erro\.*

Tamanho máximo: 5

OS4564

RN24

__Regra para tag <xCpl></xCpl>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo COMPL\_ENDERECO da SAFX04\.

Tamanho máximo: 100

OS4564

RN25

__Regra para tag <xBairro></xBairro>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo BAIRRO da SAFX04\.

Tamanho máximo: 100

OS4564

RN26

__Regra para tag <cMun></cMun>__

Campo pertencente à tag <emitente>\. Será gerado com a concatenação do campo COD\_UF\+ COD\_MUNICIPIO da TACES06, considerando o COD\_MUNICIPIO da SAFX04 para seleção\.

OS4564

RN27

__Regra para tag <xMun></xMun>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo CIDADE da SAFX04\.

Tamanho máximo: 60

OS4564

RN28

__Regra para tag <UF></UF>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo UF da SAFX04\.

OS4564

RN29

__Regra para tag <Pais></Pais>__

Campo pertencente à tag <emitente>\. Será gerado com a descrição do país disponível na TACES05, considerando como critério de seleção o COD\_PAIS da SAFX04\.

Tamanho máximo: 60

TAG consta no layout, mas é criticada pelo validador, por este motivo não vamos gerar\.

OS4564

RN30

__Regra para tag <CEP></CEP>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo CEP da SAFX04\.

OS4564

RN31

__Regra para tag <ddd></ddd>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo significativo \(desconsiderando zeros à esquerda\) do campo DDD da SAFX04\.

OS4564

RN32

__Regra para tag <Fone></Fone>__

Campo pertencente à tag <emitente>\. Será gerado com o conteúdo do campo TELEFONE da SAFX04\.

OS4564

RN33

__Regra para tag <documento></documento>__

TAG filha da tag <servicoTomado>\. Será gerada com base na SAFX07 para demonstrar as informações das NFs considerados na seleção inicial\.

OS4564

RN34

__Regra para tag <serie></serie>__

Campo pertencente à tag <documento>\. Será gerado com o conteúdo do campo SERIE\_DOCFIS da SAFX07\.

OS4564

RN35

__Regra para tag <nNFS></nNFS>__

Campo pertencente à tag <documento>\. Será gerado com o conteúdo do campo NUM\_DOCFIS da SAFX07, desconsiderando zeros à esquerda\.

OS4564

RN36

__Regra para tag <dEmi></dEmi>__

Campo pertencente à tag <documento>\. Será gerado com o conteúdo do campo DATA\_EMISSAO da SAFX07\.

OS4564

RN37

__Regra para tag <xNatOper></xNatOper>__

Campo pertencente à tag <documento>\. Será gerado com o conteúdo da Descrição da Natureza da Operação da SAFX2006, considerando como critério de seleção o COD\_NATUREZA\_OP da SAFX07\.

OS4564

RN38

__Regra para tag <totais></totais>__

TAG filha da tag <servicoTomado>\. Será gerada com base na SAFX09 para demonstrar as informações dos valores dos Itens das NFs considerados na seleção inicial\.

OS4564

RN39

__Regra para tag <vTotalServico></vTotalServico>__

Campo pertencente à tag <totais>\. Será resultado da somatória do campo VLR\_TOT da SAFX09 de todos os itens vinculados à NF\.

OS4564

RN40

__Regra para tag <vRedBCProp></vRedBCProp>__

Campo pertencente à tag <totais>\. Neste momento não geraremos esta tag\.

*Obs\. Marcos de Paula: entrei em contato com a Prefeitura buscando a informação de como poderíamos obter o conteúdo desta tag, mas eles informaram que só passam orientações para contribuintes e se eu conseguisse um CNPJ e IM de contribuinte, ajudariam\. Liguei para o cliente Arezzo, que solicitou esta geração, e o mesmo informou que a redução é um benefício que a prefeitura concede e que eles não têm\. Para gerarmos esta tag precisamos de um case que nos apoie\.*

OS4564

RN41

__Regra para tag <vBCProp></vBCProp>__

Campo pertencente à tag <totais>\. Será resultado da somatória do campo BASE\_ISS da SAFX09 de todos os itens vinculados à NF\.

OS4564

RN42

__Regra para tag <vISSProp></vISSProp>__

Campo pertencente à tag <totais>\. Será resultado da somatória do campo VLR\_ISS da SAFX09 de todos os itens vinculados à NF\.

OS4564

RN43

__Regra para tag <vRedBCRet></vRedBCRet>__

Campo pertencente à tag <totais>\. Neste momento não geraremos esta tag\.

*Obs\. Marcos de Paula: entrei em contato com a Prefeitura buscando a informação de como poderíamos obter o conteúdo desta tag, mas eles informaram que só passam orientações para contribuintes e se eu conseguisse um CNPJ e IM de contribuinte, ajudariam\. Liguei para o cliente Arezzo, que solicitou esta geração, e o mesmo informou que a redução é um benefício que a prefeitura concede e que eles não têm\. Para gerarmos esta tag precisamos de um case que nos apoie\.*

OS4564

RN44

__Regra para tag <vBCRet></vBCRet>__

Campo pertencente à tag <totais>\. Será resultado da somatória do campo VLR\_BASE\_ISS\_RETIDO da SAFX09 de todos os itens vinculados à NF

OS4564

RN45

__Regra para tag <vISSRet></vISSRet>__

Campo pertencente à tag <totais>\. Será resultado da somatória do campo VLR\_ISS\_RETIDO da SAFX09 de todos os itens vinculados à NF

OS4564

RN46

__Regra para tag <semServicoTomado></semServicoTomado>__

Esta tag será demonstrada sempre que a regra de seleção dos serviços tomados \(RN07\) __NÃO FOR__ atendida\. Indica que não houve movimentação de serviços tomados no período\.

OS4564

RN47

__Regra para tag <anoApuracao></anoApuracao>__

Campo pertencente à tag <semServicoTomado>\. Será gerado com o Ano de geração parametrizado na Data Final de geração\.

OS4564

RN48

__Regra para tag <mesApuracao></anoApuracao>__

Campo pertencente à tag <semServicoTomado>\. Será gerado com o Mês de geração parametrizado na Data Final de geração\.

OS4564

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

