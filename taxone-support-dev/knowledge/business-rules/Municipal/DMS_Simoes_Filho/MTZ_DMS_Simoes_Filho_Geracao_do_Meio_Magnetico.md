# MTZ_DMS_Simoes_Filho_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DMS_Simoes_Filho_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-07
- **Tamanho:** 72 KB

---

	

THOMSON REUTERS

Municipal – DMS Simões Filho

##### DOCUMENTO DE REQUISITO

__Data__

__OS/CH__

__Nome__

__Descrição__

12/09/2014

OS4596

Jefferson Mota

Criação do Documento

11/05/2016

MFS\_2071

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

O novo módulo Simões Filho deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Simões Filho: “Consiste na entrega das informações sobre os serviços tomados do município de Simões Filho”\.

OS4596

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a “30709” \(Simões Filho\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Simões Filho, Bahia\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

OS4596

RN03

__Estrutura de menus do módulo DMS:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DMS:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__

OS4596

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_DMS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração

__MUNICIPIO__: representa o município que está sendo gerado\.

__ST\_DMS__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_DMS\_SIMOESFILHO\_01012013\.TXT

OS4596

MFS829438    

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Simões Filho, que estejam licenciados e que o usuário possua acesso no PowerLock\.

OS4596

__MFS\_2071__

RN06

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos\.

O arquivo a ser gerado para importação dever ser no formato __‘TXT’;__

__Campo tipo Data__

Campos tipo Data devem ser preenchidos no seguinte formato: “AAAA\-MM\-DD”\. Deverá ter um tamanho fixo de 10 caracteres, incluindo separador;

__Campo de Valores Decimais__

Os valores decimais devem ser no formato: “__0\.0000”__\. O campo deverá ter quatro casas decimais, separadas por ponto \(“\.”\), sem agrupamento de milhares\. Exemplo: 1\.500,00 = 1500\.0000

__Campo tipo Numérico__

Campo formado somente por caracteres numéricos\. Todos os campos do tipo numérico serão preenchidos alinhados pela direita\. Se necessário, serão preenchidos com zeros à esquerda até completar seu tamanho máximo\.

__Campo tipo Texto__

Todos os campos do tipo texto  serão preenchidos alinhados pela esquerda\. Se necessário, serão preenchidos com espaços em branco à direita até completar seu tamanho máximo\.

Os campos deverão ser separados por ponto e vírgula \(__;__\) e as linhas separadas por quebras de linhas\. 

OS4596

RN07

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas com as seguintes características:

- Documentos de entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.

Quando a nota não tiver itens não deve ser recuperada\.

OS4596

RN08

__Regra p/ campo Situação Fiscal__

Deverá preencher com um das situações abaixo:

__“2”__ \- Simples Nacional\. Verificar se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”,

__“3__ “\- ISS Construção Civil\. Verificar se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘__1__’, referente ao serviço cadastrado na nota\.

__“5”__ \- Não Incidência\. Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

__“4”__ – Microempreendedor\. Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = ‘04’;

__“1”__ \- ISS Normal\. Preencher com 1, quando nenhuma das opções anteriores forem verdadeiras\.

Campo obrigatório\.

Tamanho: 1

Tipo: Numérico

OS4596

RN09

__Regra p/ campo Número da Nota__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Campo obrigatório\.

Tamanho: 10

Tipo: Numérico

OS4596

RN10

__Regra p/ campo Data de Emissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \.

Campo obrigatório\.

Tamanho: 10

Tipo: Data

OS4596

RN11

__Regra p/ campo Data de Pagamento__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo 175 da SAFX07\)\. 

__Obs\.:__ Se caso o campo estiver em branco, ou a data for menor que a data de emissão, deverá preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Campo obrigatório\.

Tamanho: 10

Tipo: Data

OS4596

RN12

__Regra p/ campo Alíquota da Nota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Valor decimal __com duas casas decimais e sem símbolo de percentual__\. Conforme Situação Fiscal e serviço prestado deve ser informado alíquota entre 2,00% e 5,00%\. Exemplos: 2,00% = 2\.00   /    2,75% = 2\.75    /    5,00% \- 5\.00

Campo obrigatório\.

Tipo: Decimal

Tamanho máximo\.: 5 caracteres

OS4596

RN13

__Regra p/ campo Base de Cálculo__

Preencher com o campo BASE\_ISS da tabela DWT\_ITENS\_SERV\.

Campo obrigatório\.

Tipo: Decimal

Tamanho máximo: 16 caracters\. Os valores decimais devem ser no formato: “__0\.0000”__\. 

OS4596

RN14

__Regra p/ campo Valor da Nota__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Campo obrigatório\.

Tipo: Decimal 

Tamanho máximo: 16 caracters\. Os valores decimais devem ser no formato: “__0\.0000”__\.

OS4596

RN15

__Regra p/ campo CPF / CNPJ Prestador__

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\.

Campo obrigatório\.

Tipo: Numérico

Tam\.: 14 posições

OS4596

RN16

__Regra p/ campo Nome / Razão Social Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Campo obrigatório\.

Tipo: Texto

Tam\.: 50 posições

OS4596

RN17

__Regra p/ campo Valor do Material__

Não será tratado\. Não Preencher\.

OS4596

RN18

__Regra p/ campo CPF / CNPJ Tomador__

Preencher com o campo CGC da tabela ESTABELECIMENTO 

Campo obrigatório\.

Tipo: Numérico

Tam\.: 14 posições

OS4596

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

