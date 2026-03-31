# MTZ-DS_Maraba-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-DS_Maraba-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-30
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Municipal

DS Marabá \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1528

Geração do Meio Magnético DS Marabá

Deverá ser criado um novo módulo que permita a geração do meio magnético DS Marabá em que serão informados apenas os documentos fiscais de serviços tomados\. 

MFS829438

Ajuste da Nomenclatura do Arquivo

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Marabá” deve ficar localizado no grupo “Municipal”\.

MFS1528

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PA” e ao código de município do IBGE igual a “4208” \(Marabá\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Marabá, Pará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS1528

RN03

__Estrutura de menus do módulo Marabá:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Marabá:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

MFS1528

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

__ST\_DS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração

__MUNICIPIO__: representa o município que está sendo gerado\.

__ST\_DS__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_DS\_MARABA\_01012010\.TXT

MFS1528

MFS829438

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final: __deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Marabá, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS1528

RN06

__Regras Gerais de formatação do arquivo__

O arquivo a ser gerado para importação dever  ser no  formato  texto\.

Observações :

\- Todos os registros deverão ser finalizados com a quebra de linha\.

\- Campos numericos, devem ser preenchidos com zeros à esquerda até atingir o tamanho  exato  do campo\. Quando o campo for opcional, ou seja, o conteúdo do campo não for fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\. 

\- Serão utilizados 02 posições para a parte decimal\. Exemplo:

O campo com tamanho 12 significa: 10 posições para a parte inteira e 02 posições para a parte decimal\.

Para um valor de R$ 2\.500,__00__ no arquivo deverá estar gravado assim: 0000002500__00__

\- Os valores numéricos serão truncados, quando a informação preenchida no banco de dados, for maior do que o tamanho máximo exigido pelo layout\. 

\- Todos os campos tipo Texto,  deverão ser preenchidos alinhados pela esquerda, Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo\.

MFS1528

RN07

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.

MFS1528

RN08

__Campo Registro:__

Preencher com o valor fixo __“2”__\.

Tipo: Numérico

Tamanho: 01 caracter

MFS1528

RN09

__Campo Documento do Tomador:__

Preencher com campo CGC da tabela ESTABELECIMENTO\.

Tipo: Texto

Tam\.: 18 caracteres \(Com Pontos/Barras/Hifens\)

MFS1528

RN10

__Campo  Exercício / Mês de Referência:__

Preencher com o Mês e Ano informado na tela de geração do meio magnético\.

Tipo: Numérico 

Tamanho: 06 caracteres \(AAAAMM\)

MFS1528

RN11

__Campo  Código do Serviço:__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

Tipo: Numérico 

Tamanho: 09 caracteres

MFS1528

RN12

__Campo  Inscrição Municipal:__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 15 caracteres

MFS1528

RN13

__Campo Documento do Prestador:__

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\. 

Obs\.: Quando não existir informação no campo CGC\_CPF, deve respeitar a regra de campo texto, completando com espaços\. A questão da barra, pontos e hífens, apenas quando existir CNPJ\.  

Tipo: Texto

Tam\.: 18 caracteres \(Com Pontos/Barras/Hifens\)

MFS1528

RN14

__Campo Razão Social do Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR

Tipo: Texto

Tam\.: 100 caracteres

MFS1528

RN15

__Campo Situação do Prestador__

Deve preencher com__ “0” \- __Do Município:

Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Deve preencher com__ “1”__ \-  Fora do Município:

Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Deverá preencher com __“2” __– Extrangerio:

Se a UF da tabela X04\_PESSOA\_FIS\_JUR relacionado à pessoa FIS/JUR cadastrada na nota fiscal for do Exterior, ou se o campo COD\_MUNICIPIO da X04\_PESSOA\_FIS\_JUR for nulo\.

Tipo: Numérico

Tam\.: 01 caracter

MFS1528

RN16

__Campo Forma de Tributação__

Preencher com:  

      __0 – Retido: __Verificar se__ __o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV <> 0\. __ __

     __ 3 – Isento :__ Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido

      verificar se o serviço cadastrado na nota está parametrizado na tela Parâmetros por Município/Parâmetros

      Classificação de Serviços com o COD\_PARAM = “433”\.

      __4 – Imune:__ Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\. Se não estiver preenchido, verificar se

      o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros \- 

      Classificação de Serviços com o COD\_PARAM = “420”__;__

__      5 – Outro Município: __Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento

      estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

__      7 – Não Incidencia:__ Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem

      parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”;

      __8 – Estimado: __Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver

      preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela

      Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

     __11 – Simples Nacional:__ Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR estiver selecionado\.

     __13 \- M\.E\.I__: Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela

      Parâmetros – Classificação de Serviços com o COD\_PARAM = “452”\.

Caso nenhuma das alternativas anteriores forem verdadeiras, deve preencher com “__1” __normal\.

Tipo: Numérico

Tamanho: 02 caracteres

MFS1528

RN17

__Campo Tipo de Documento:__

Preencher com a informação do campo “Modelo DS Maraba” da tela Modelo Msaf x modulo, em Parâmetros para Município, referente ao modelo cadastrado na nota fiscal\.

Obs\.: Caso o modelo não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para o Modelo de Documento "X" do Documento "NNNNNN\-SSS", não foi localizada a parametrização de Modelo Msaf x Modelo\. Efetuar a parametrização no menu Parâmetros > Modelo Msaf x Modelo no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tamanho: 02 caracteres

MFS1528

RN18

__Campo Número da Nota Fiscal:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Na geração deste campo, deve ser consideradas 09 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 09 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(09 posições\)\.”

\(Ex: para esta situação: Nº de NF 123456789012 será gerado 456789012\)\.

Tipo: Numérico

Tamanho: 09 caracteres

MFS1528

RN19

__Campo Data de Emissão da Nota:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. 

Tipo: Data no formato __AAAAMMDD __

Tamanho: 08 caracteres

MFS1528

RN20

__Campo Valor Contábil:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Na geração deste campo, deve ser considerada __12__ posições da direita para a esquerda, incluíndo os centavos\. Se o conteúdo do campo VLR\_TOT tiver mais de 12 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O “Valor informado para o campo Valor Contábil ultrapassou o tamanho máximo permitido \(12 posições\) e será truncado\.”

Tipo: Numérico

Tamanho: Valor com 12 posições com zeros a esquerda, sem vírgula e sem ponto\. Exemplo: R$10,25 = 000000001025

MFS1528

RN21

__Campo Valor Tributário:__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Na geração deste campo, deve ser considerada __12__ posições da direita para a esquerda, incluíndo os centavos\. Se o conteúdo do campo VLR\_TRIBUTO\_ISS tiver mais de 12 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O “Valor informado para o campo Valor Tributário, ultrapassou o tamanho máximo permitido \(12 posições\) e será truncado\.”

Tipo: Numérico

Tamanho: Valor com 12 posições com zeros a esquerda, sem vírgula e sem ponto\. Exemplo: R$10,25 = 000000001025

MFS1528

RN22

__Campo Observações:__

Preencher com brancos\.

Tipo: Alfanumérico

Tamanho: 255 caracteres

MFS1528

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

