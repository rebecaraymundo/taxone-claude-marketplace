# MTZ_NFTS-WEB SERVICE_Geracao_Meio_Magnetico_Situacao_Especial

- **Fonte:** MTZ_NFTS-WEB SERVICE_Geracao_Meio_Magnetico_Situacao_Especial.docx
- **Modificado:** 2025-12-06
- **Tamanho:** 79 KB

---

### NFTS WEB SERVICE

Geração do meio magnético p/ estabelecimentos fora do município em questão\.

__                                                  DOCUMENTO DE REQUISITO__

__Data__

__MFS__

__Nome__

__Descrição__

05/12/2025

MFS\-895592

Rosemeire Santos

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador NFTS SALVADOR, via Web Service\.

 

### REGRAS DE NEGÓCIOS

###### __Regras__

###### __DESCRIÇÃO__

__MFS__

RN01

__Estrutura de menus do módulo NFTS SALVADOR:__

Deverão ser criado o seguinte menu e sub\-menus no módulo NFTS SALVADOR:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS\-895592__

RN02

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

Quando o parâmetro ‘__Quebrar Arquivos por Data de Emissão__’ estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.XML__, onde:

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_122025\.XML

Quando o parâmetro ‘Quebrar Arquivos por Data de Emissão’ estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.XML__, onde:

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012025\_012025\.XML

Obs\.: Neste caso o arquivo normal__ também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS\-895592__

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados\.

__MFS\-895592__

RN04

__Regras de formatação dos registros gerados no meio magnético:__

Campos que representam CPF e CNPJ \(respectivamente 11 e 14 caracteres\) devem ser informados com o tamanho fixo previsto, sem formatação e com o preenchimento dos zeros não significativos; 

Campos numéricos que representam valores e quantidades são de tamanho variável, respeitando o tamanho máximo previsto para o campo e a quantidade de casas decimais \(quando houver\)\. 

O preenchimento de zeros não significativos causa erro de validação do Schema XML\. 

Os campos numéricos devem ser informados sem o separador de milhar, com uso do ponto decimal para indicar a parte fracionária \(quando houver\) respeitando\-se a quantidade de dígitos prevista no layout; 

 As datas devem ser informadas no formato “AAAA\-MM\-DD”\. 

Para reduzir o tamanho final das mensagens XML alguns cuidados de programação deverão ser assumidos: 

 Na geração das mensagens XML, excetuados os campos identificados como obrigatórios no respectivo Schema XML, não incluir as TAGs de campos zerados \(para campos tipo numérico\) ou vazios \(para campos tipo caractere\); 

Não incluir "espaços" no início e/ou no final de campos alfanuméricos; 

Não incluir comentários na mensagem XML; 

Não incluir anotação e documentação na mensagem XML \(TAG annotation e TAG documentation\); 

Não incluir caracteres de formatação na mensagem XML: “LF” \(Line Feed ou salto de linha, caractere ASCII 10\), "CR" \(Carriage Return ou retorno do carro, caractere ASCII 13\), "tab", \(caractere de "espaço" entre as TAGs\)\.

__MFS\-895592__

RN05

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)__

Considerar todas as notas com as seguintes características:

- Documentos de entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2, 3 e 9 \(RPA\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência informado na tela de geração
- Considerar notas canceladas\.

 Recuperar as Notas Fiscais Eletrônico de Serviço, considerando a parametrização da Tela de __“Notas Fiscais Eletrônicas”,__ no Menu Parâmetros por Município com as chaves de __UF__ e __Município__, conforme regras abaixo:

__Notas Fiscais eletrônicas de Serviço Tomado: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

Default: Desmarcado

__ \-  Se__ a __UF__ e o __Município __do estabelecimento não estiver parametrizados no Módulo > Parâmetro por Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

__MFS\-895592__

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

