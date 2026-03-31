# MTZ_ARISS_Geracao_Meio_Magnetico

- **Fonte:** MTZ_ARISS_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Municipal

ARISS \- Sistema de Arrecadação do ISSQN

DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-8312

Julyana Perrucini

Criação de validador para município\.

MFS\-9256

Jean Meyohas

Alterando o tamanho do campo do numero da Nota\.

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__REGRAS DE NEGÓCIO__

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

RN01

__Estrutura de menus do módulo DMS:__

Deverão ser criados os seguintes menu e sub\-menus no módulo ARISS:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
- Janela
- Ajuda 

MFS\-8312

RN02

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

__       ST\_ARISS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __ST\_ARISS__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_ARISS\_RIODASPEDRAS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__ST\_ARISS\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__        ST\_ARISS__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.TXT__: extensão do arquivo\.

Ex: ST\_ARISS\_RIODASPEDRAS\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-8312

MFS829438     

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS\-8312

RN04

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos:

O arquivo a ser gerado para importação dever ser no formato __‘TXT’\.__

- Caracter: Alinhados a esquerda\. Preencher com espaços em branco à direita, quando necessário\. 
- Numérico: Alinhados a direita\. Preencher com zeros à esquerda quando necessário\. 
- O único campo que deve conter ponto \(\.\) é o “Código da Atividade” \(posição 43 a 48\)\. 
- O campo “Valor da Nota” não deve conter ponto \(\.\) e nem vírgula \(,\)\. *Exemplo:* Se tivermos uma nota de R$ 1\.000,00 no registro ficaria 000000100000\.__ __

MFS\-8312

RN05

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-8312

RN06

__Regra p/ campo CNPJ/CPF Prestador__

Identifica o CNPJ ou o CPF do Prestador do serviço\.

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório\.

Formato: 99999999999999

Tamanho: 11 a 14 posições

Tipo: Alfanumérico

MFS\-8312

RN07

__Regra p/ campo Data da Nota__

Identifica a data de emissão da nota fiscal de serviço\.

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Campo obrigatório\.

Formato: DDMMAAAA

Tamanho: 08

Tipo: Data

MFS\-8312

RN08

__Regra p/ campo Número da Nota__

Identifica o número da nota fiscal de serviço\.

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

Campo obrigatório\.

Formato: 9999999999

Tamanho: 10

Tamanho: 08

Tipo: Numérico

MFS\-8312

RN09

__Regra p/ campo Valor da Nota__

Identifica o valor total da nota fiscal de serviço\.

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123456789123456,45, gravar 678912345645\.

Campo obrigatório\.

Formato: 999999999999

Tamanho: 10,2

Tipo: Numérico 

MFS\-8312

RN10

__Regra p/ campo Código da Atividade__

Identifica o código tributário de serviços do município\. 

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e este vinculado ao item da nota fiscal\.

__Tratamento:__

- Será necessário completar com zeros a esquerda\. *Exemplo:* Código Lei 116 “0101” na tabela, gravar “001\.01”; Código Lei 116 “1720” na tabela, gravar “017\.20”; e assim por diante;
- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Data Fiscal>>”*\.

Campo obrigatório\.

Formato: 999\.99

Tamanho: 06

Tipo: Numérico 

MFS\-8312

RN11

__Regra p/ campo Situação da Nota__

Identifica qual a situação da nota fiscal de serviço\.

Preencher com:

__“C” \- Cancelada\.__

- Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) for igual a “S”\.

__“S” \- Simples Nacional\.__

- Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”\.

__“I” \- Isentas\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“M” \- Microempresário Individual \(MEI\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “05 – MEI \(Micro Empreendedor Individual\)” referente o prestador cadastrado na nota fiscal\.

__“R” \- Retido\.__

- Se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município __OU__ se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual ao município do estabelecimento selecionado\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“N” \- Normal\.__

Campo obrigatório\.

Formato: X

Tamanho: 01

Tipo: Alfanumérico

MFS\-8312

RN12

__Regra p/ campo Código do Município__

Identifica o Código do Município do Prestador\.

Preencher com o campo Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, emitir uma mensagem padrão de log\.

Campo obrigatório\.

Formato: 99999

Tamanho: 05

Tipo: Numérico 

MFS\-8312

RN13

__Regra p/ campo CNPJ Tomador__

Identifica o CNPJ do Tomador do serviço\.

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

Campo obrigatório\.

Formato: 99999999999999

Tamanho: 14 posições

Tipo: Alfanumérico

MFS\-8312

RN14

__Regra p/ campo Alíquota Simples Nacional__

Identifica a alíquota do Prestador quando for optante pelo Simples Nacional\.

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV \(campo 34 da SAFX09\) se o campo IND\_SIMPLES\_NAC da tabela SAFX04 referente à Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas posições do número decimal\. *Exemplo:* 123,4567, gravar 2345\.

Campo não obrigatório\.

Formato: 9999

Tamanho: 2,2 posições

Tipo: Numérico

MFS\-8312

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

__MFS\-8312__

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-8312__

__IM03__

Código IBGE: __44004 – __Município/UF:__ RIO DAS PEDRAS / SP__

A descrição funcional do módulo será: “Consiste na emissão de Notas Fiscais de Serviço Eletrônicas de forma integrada com os sistemas de gestão utilizados para faturamento dos serviços prestados pelos contribuintes do município”\.

__MFS\-8312__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

