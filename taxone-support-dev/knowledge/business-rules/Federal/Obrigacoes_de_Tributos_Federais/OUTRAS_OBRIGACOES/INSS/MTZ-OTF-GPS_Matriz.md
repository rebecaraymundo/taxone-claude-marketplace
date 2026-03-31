# MTZ-OTF-GPS_Matriz

- **Fonte:** MTZ-OTF-GPS_Matriz.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 76 KB

---

# Obrigações de Tributos Federais – GPS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2494

# GPS – Cooperativa de Trabalho de Transporte 

Durante a geração das retenções do INSS os dados deverão ser gravados considerando o campo 26 da SAFX04, onde o sistema deverá verificar se a informação é referente à Cooperativa de transporte, caso seja, a nota gerada referente a essa Pessoa Fis/Jur deve ser levada para a tela de manutenção com a data do fato gerador preenchida conforme a data fiscal\.

Durante a geração da Guia a data de competência apresentada na GPS deve ser a mesma da data fiscal\.

OS2613

# GPS – Retenção 2º Base INSS

Conforme especificado no documento de requisitos o sistema realmente não gera a informações completas para apuração da GPS, por isso o objetivo desse documento é de alterar a sistemática atual fazendo com que a guia dessas operações sejam gravadas considerando os valores informados nos campos referentes à 2ºBase de INSS\.

CH50401

# Demonstrativo de INSS – OTF

Atualmente os demonstrativos das retenções de INSS são tirados sem um separador de totais identificando os meses e as pessoas fis/jur\. Esse chamado trata da inclusão desses totais nos demonstrativos\.

CH81520

# Rotinas de Geração da GPS

Considerar notas fiscais classificação fiscal = 8 e 9 na geração

OS3232

# Rotinas de Geração da GPS

Permitir consolidação da GPS por CNPJ

OS3128

# Recuperação da Tela de Manutenção das Consolidações das Retenções de INSS

Conforme especificado no documento de requisitos o sistema realmente não traz todas as retenções para manutenção das consolidações, portanto, o objetivo desse documento é de alterar a regra de recuperação atual fazendo com que todas as operações sejam recuperadas comparando somente o mês/ano do cadastro da PFJ com o mês/ano da data fiscal da tela de consolidação das retenções\.

OS 3359

# Rotina de Geração da GPS

A rotina de geração das retenções de INSS deve considerar os RPAs pela Data da Emissão, se o prestador de serviço for PJ e pela Data do pagamento caso o prestador for PF, com base no período de lançamento informado pelo usuário\.

OS2839\-A

# Recuperação da Tela de Geração da GPS

Alterar a rotina de geração das retenções de INSS \(tanto pela consolidação, quanto pelas notas\), para gerar as guias dos RPAs que não tenham valores de INSS, mas que possuem o valor de Outras Entidades\. 

Esta alteração deve contemplar as consolidações Por Estabelecimento \(Avulso\) e Por Cedente \(Fonte\)\.

Demonstrar no log da geração das retenções os códigos de pagamentos que não estão devidamente parametrizados, quando o documento não possuir valores de INSS, mas tiver valor de Outras Entidades\.

OS3216

# Gerar GPS com CEI do Cedente no campo 05 – CNPJ ou CEI

Este documento de requisito tem por objetivo permitir que os GPS’s sejam segregadas por CEI – o que o sistema já faz hoje – e que o CEI do Cedente \(Prestador do serviço\) deve ser gerado no campo 05 da GPS\.

CH112249\_V2

# Considerar no Cálculo de Juros e Multa da GPS o Valor de Outras Entidades

Este documento de requisito tem por objetivo permitir que o Valor de Outras Entidades seja considerado para o cálculo de Juros e Multa na emissão da GPS\.

CH1069\_2012

# Alterar o Valor Mínimo de Recolhimento do INSS\.

Alterar na geração da GPS o valor mínimo de recolhimento do INSS para R$10,00\.

OS3668

# Gerar GPS por Empresa

O cliente WEG reportou através do chamado 4387\_2012 que a geração da GPS – Guia da Previdência Social está sendo gerada por Estabelecimento ao invés da mesma ser gerada por Empresa\. Segundo o próprio cliente, esse problema não ocorria no passado\. O mesmo informou que demorou um bom tempo \(entre 6 meses e 1 ano\) para atualizar o produto e ao fazê\-lo esse problema passou a ocorrer\.

Foi realizado um call entre o cliente e o Sr\. Carlos Nascimento \(Informação\) onde foi explicado para o cliente como o produto se comportava\. Segundo informações do próprio Sr\. Carlos Nascimento, a legislação não é clara se a geração da GPS deve ser feita por Empresa ou Estabelecimento\. Foi informado ao cliente também que essa opção de geração seria liberada no produto como uma “faculdade gerencial”, ou seja, sem efeito legal\.

Vale salientar que hoje já existe um parâmetro para essa geração, mas o mesmo – marcado ou desmarcado – possui o mesmo efeito, ou seja, gera a GPS por Estabelecimento\.

Em virtude desse cenário, será desenvolvida uma funcionalidade a partir desse parâmetro para que o cliente possa gerar a GPS por Empresa, desde que as premissas da funcionalidade de multi\-empresa que foram desenvolvidas para o cliente Sicredi na OS3096\-E não sejam alteradas ou impactadas\.

CH2806\-A\_2012

# Digitação da GPS não está gravando o número do processo

Deverá ser tratado o Número do Processo a partir da Geração da GPS na tela de Digitação da GPS

CH19809\_2012

# Cálculo de Juros indevido na geração da GPS

O módulo esta calculando juros de forma indevida

OS3904

# Geração de Retenções de INSS

Ao usar o módulo FUNRURAL, desprezar as notas da SAFX07, que estão  na SAFX63 com a Situação Especial: 03\- Depósito Judicial, na geração da GPS\.

CH13919/2013

# Geração de Retenções de INSS

Ajuste na regra do parâmetro “Considerar apenas retenções NÃO processadas” para que o seu tratamento se mantenha no processamento por empresa ou por estabelecimento\.

CH843\_2015

# Alteração no cálculo de multa diária da GPS

Este documento tem como objetivo ajustar a rotina de cálculo da multa diária na Geração das Retenções e Consolidação das Retenções de INSS para a Emissão da GPS\.

CH16317\_2015

# Alteração no cálculo de multa diária da GPS

Este documento tem como objetivo ajustar a rotina de cálculo da multa diária na Geração das Retenções e Consolidação das Retenções de INSS para a Emissão da GPS\.

CH6745\_2016

# Alteração na recuperação das notas de PJ na geração das retenções de INSS

Este documento tem como objetivo ajustar a recuperação das notas fiscais de pessoa jurídica na geração das retenções do INSS para a GPS\.

MFS\-6168

# Inclusão de parâmetro na tela de Emissão da GPS

Este documento tem como objetivo alterar a tela e a rotina da Emissão da GPS para que o usuário possa selecionar qual Guia deseja emitir: Pagas, Abertas ou Ambas\.

CH4837\_2017

\(MFS\-11391\) 

# Ajuste na geração na GPS quando for para Associação Desportiva\.

Este documento tem como objetivo alterar a saída da GPS quando o Código de Pagamento INSS for igual a 2500 e for ‘para Associações Esportivas’\.

CH9607\_2017

\(MFS\- 11862\)

# Alteração na recuperação das notas de PF na geração das retenções de INSS

Este documento tem como objetivo ajustar a recuperação das notas fiscais de pessoa física na geração das retenções do INSS para a GPS\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No campo 26 da SAFX04 “Classe de Pessoa Fís/Jur” deverá ser incluída a opção “05\-Cooperativa de transporte”\.

OS2494

__RN01__

O nome desse campo será somente “Data do Fato gerador”

OS2494

__RN02__

Quando da geração da retenção de INSS, se identificado que no campo 26 da SAFX 04 a informação colocada é “Cooperativa de transporte”, o campo “Data do fato gerador” dessa tela \(Manutenção de Dados de Retenção\) será igual a informação colocada no campo “Data Fiscal”\.

OS2494

__RN03__

Quando da geração das retenções de INSS o sistema deverá quando estiver lendo as informações da tabela SAFX07 deverá considerar também durante a gravação das informações, os dados colocados nos campos 151 – Segunda Base de Cálculo para INSS, 152 – Segunda Alíquota de INSS, 153 – Segundo Valor de Tributo INSS e 154 – Segundo Código de Pagamento INSS\. Da mesma forma que era feito na release 27\.

OS2613

__RN04__

Quando da geração da consolidação das retenções de INSS o sistema deverá quando estiver lendo as informações da tabela SAFX07 deverá considerar também durante a gravação das informações, os dados colocados nos campos 151 – Segunda Base de Cálculo para INSS, 152 – Segunda Alíquota de INSS, 153 – Segundo Valor de Tributo INSS e 154 – Segundo Código de Pagamento INSS\. Da mesma forma que era feito na release 27\.

OS2613

__RN05__

Verificar se para a alteração conforme RN00 e RN01 deve – se somente retirar o comentário feito na procedure__* saf\_inss\_df\.*__

OS2613

__RN06__

Após a alteração conforme RN00 e RN01, o sistema terá de gerar guias separadas para os dados colocados nos campos 151, 152, 153 e 154 da SAFX07\.

OS2613

__RN07__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN08__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência \+ Extemporâneo = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o relatório traz as notas cujo período de emissão seja diferente do período de lançamento e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN09__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão, trazendo inclusive as notas que passaram da data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN10__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal \+ Extemporâneo = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN11__

Ao final do relatório, independente do critério utilizado para geração do mesmo, terá um totalizador geral\. Que deverá se igual a soma dos meses apresentados no relatório\.

Obs: Essa regra será aplicada para os demonstrativos que apresentarem os totalizadores “geral e por estabelecimento”, caso exista demonstrativos que não apresentem esses totais, este não deverá ser inserido, permanecendo assim como esta\.

CH50401

__RN12__

__\[EXCLUÍDA – CH59907\-A – OS NÃO IMPLEMENTADA\]__ Quando o prestador do serviço for uma pessoa física, na GPS as informações devem ser do contratante, e não do prestador\.

Nos campos NOME/RAZAO SOCIAL/FONE ENDEREÇO e no campo IDENTIFICADOR devem ser demonstradas as informações não do prestador do serviço e sim do contratante do serviço, pois neste tipo de operação é ele quem efetua o pagamento dos 20% do INSS\. 

Neste caso, o sistema deverá:

1. Identificar a PF/PJ do documento fiscal de serviço\.
2. Caso a PF/PJ seja uma Pessoa Física gerar os dados do estabelecimento na GPS\.

CH59907\-A

__RN13__

__\[EXCLUÍDA – CH59907\-A – OS NÃO IMPLEMENTADA\] __A regra RN12 só se aplica quando a pessoa da nota fiscal for __física__ \(para pessoa jurídica a regra não deve ser alterada\!\)\.

Para poder distinguir isso, o sistema deve se valer de um dos critérios abaixo\. Os dois critérios deverão ser incorporados, porém não deverá ser obrigatório o preenchimento dos dois, apenas um deles preenchido é suficiente:

1. Caso o campo CPF/CNPJ \(06 da safx04\) possua 11 posições;

*    ou*

1. O campo “Classe de Pessoa Fis\./Jur\.” \(26 da safx04\) esteja preenchido com a opção “01 – Pessoa Física”\.

CH59907\-A

__RN14__

Nas parametrizações do cliente, as notas de pessoa física têm uma parametrização própria por cedente ou por estabelecimento\.

Esta parametrização já determina que as guias de pessoa física ou de pessoa jurídica sejam geradas separadamente, por isso não será necessário nenhum tratamento para este ponto\.

CH59907\-A

__RN15__

__Geração da GPS__

Alterar a geração da GPS para considerar também as notas fiscais cuja classificação sejam 8 ou 9 \(cod\_clas\_doc\_fis = 8, 9\), quando a parametrização do INSS for qualquer uma das relacionadas abaixo:

→ Por Pessoa Física Jurídica x Alíquota

→ Código de Pagamento

→ Código de Pagamento x Alíquota

Esta alteração deverá impactar todas as rotinas da GPS:

- Geração das Retenções de INSS
- Geração da Consolidação das Retenções
- Relatório de Conferência para as Retenções
- GPS → Digitação/Emissão

CH81520

__RN16__

__Emissão do Demonstrativo de INSS__

Considerar também as notas fiscais cuja classificação sejam 8 ou 9 \(cod\_clas\_doc\_fis = 8, 9\) nos seguintes Demonstrativos:

OTF → Outras Obrigações → Retenção de INSS – Serviços Prestados → Emissão do Demonstrativo de INSS →

- INSS por Cedente \(Fonte\) → Analítico
- INSS por Cedente \(Fonte\) → Sintético
- INSS por Estabelecimento \(Avulso\) → Analítico
- INSS por Estabelecimento \(Avulso\) → Sintético
- Geral → Analítico
- Geral → Sintético

CH81520

__RN17__

__Geração das Retenções de INSS__

__Parâmetro “Processar”:__

__Opções:__

\(  \) Retenções do INSS a partir das notas fiscais

\(  \) Consolidação das retenções para emissão da GPS

\(  \) Ambas

Quando for escolhida a segunda ou a terceira opção, habilitar o parâmetro abaixo\.

Se for escolhida a primeira opção, o parâmetro abaixo deverá ficar desabilitado:

*Consolidar GPS por:*

*         \(  \) Código da Pessoa Fis/Jur*

*         \(  \) CNPJ/CPF*

SE ao clicar em “Execução”, não for escolhida nenhuma das duas opções, exibir a seguinte mensagem:

__MasterSAF – IR__

__X__

 

 

 

 

 

 

 

 

__Informe “Consolidar GPS por:”__

 

 

 

 

 

 

 

 

OS3232

__RN18__

__Parâmetro “Consolidar GPS por:”__

Este parâmetro será habilitado na tela somente quando as opções do parâmetro “Processar”, forem:

2 – Consolidação das retenções para emissão da GPS

3 – Ambas

__→ Quando a opção de consolidação for “*Código da Pessoa Fis/Jur*”:__

Deverá ser mantida a forma de consolidação atual, ou seja:

__Estabelecimento Avulso__

__Cedente/Fonte__

Código da Empresa

Código do Estabelecimento

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

Código Pessoa Fis/Jur

CNPJ/CPF

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

__→ Quando a opção de consolidação for “*CNPJ/CPF*”:__

Consolidar conforme indicação abaixo:

__Estabelecimento Avulso__

__Cedente/Fonte__

Código da Empresa

Código do Estabelecimento

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

CNPJ/CPF

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

Neste caso, acumular o código/razão social de uma das quaisquer pessoas fis/jur para a emissão da GPS\.

 

OS3232

__RN19__

__Regra para recuperação da tela de manutenção das consolidações das retenções de INSS__

Deverá ser mantida a recuperação atual, somente alterando a seguinte regra:

Recuperar os dados referente ao período informado da tabela IRT\_RET\_INSS\_CED 

__SE__

O campo VALID\_FIS\_JUR da tabela X04 \(Validade\) deve ter mês/ano <= ao mês/ano do campo DAT\_FISCAL da tabela IRT\_RET\_INSS\_CED 

OBS: Não onsolidaç o dia informado nos dois campos\.

OS3128

__RN20__

A recuperação das notas para a geração das retenções de INSS__ deve permanecer__ __da mesma forma__ conforme a regra abaixo:

A data do lançamento deve estar compreendida dentro do mês da emissão __E__

A data fiscal deve estar dentro do primeiro dia do mês da data da emissão até o dia\_limite\_pagamento do mês posterior 

 

Ex\. Nota de 06/2011, 

Data do lançamento dentro do mês da geração \(01/06 à 30/06\) __E__

Data Fiscal entre 01/06 à 20/07 \(considerando que a data\_limite\_pagamento esteja configurado para o dia 20\)\.

A Alteração será feita para a __Manutenção de dados da Retenção__ e na __Emissão da GPS__, quando o prestador de Serviço for  PF\. 

Deverá ser considerado para as notas cujo o prestador do serviço seja  PF a data fiscal do documento para o documento se enquadrar no Mês/Ano Competência, conforme critérios abaixo:

\- Se o campo CPF/CNPJ\(SAFX04\.CPF\_CGC\) conter 11 posições, deverá ser considerado dentro do período de lançamento da GPS se a Data Fiscal \(DWT\_DOCTO\_FISCAL\.DATA\_FISCAL\) do RPA, estiver dentro do mês/ano informado no campo ‘Período de lançamento’ da tela de Geração de Retenções de INSS \.

\- Se o campo CPF/CNPJ \(SAFX04\.CPF\_CGC\) conter 14 posições, deverá ser considerado dentro do período de lançamento da GPS se a Data da Emissão \(DWT\_DOCTO\_FISCAL\.DATA\_EMISSAO\) do RPA, estiver dentro do mês/ano informado no campo  ‘Período de lançamento’ da tela de Geração de Retenções de INSS\.

Exemplo:

Considerando o seguinte cenário: 4 documentos, sendo dois deles com Data da Emissão e Data Fiscal dentro do mês de Junho \(um Prestado por PF e outro por PJ\), os outros dois com Datas Fiscais, posterior ao mês da emissão \(um Prestado por PF e outro por PJ\)\.

Na tela da manutenção de dados da Retenção:

__Deve ser considerado Mês/Ano Competencia: 06/2011 as seguintes notas:__

NF 01 – Prestador de Serviço PF: Data da Emissao e Data Fiscal dentro do mês de junho/2011\. 

NF 02 – Prestador de Serviço PJ: Data da Emissao e Data Fiscal dentro do de junho/2011\.

NF 03 – Prestador de Serviço PF: Emissão \(junho/2011\) e Data Fiscal mês \(julho/2011\)\.

NF 04 – Prestador de Serviço PJ: Data da Emissao \(junho/2011\) e Data Fiscal \(julho/2011\)\. 

__Deve ser considerado Mês/Ano Competencia: 07/2011 a seguinte nota:__

NF 03 – Prestador de Serviço PF: Emissão \(junho/2011\) e Data Fiscal mês \(julho/2011\)\.

OS3359

MFS\- 11862

__RN20\.a__

Para Pessoa Jurídica \(PJ\), de acordo com a regra de recuperação, por ser considerada a sua data de emissão, deve ser limitada a sua recuperação até 60 dias, considerando que a data do lançamento será compreendida dentro do mês da emissão e a data fiscal será dentro do primeiro dia do mês da data da emissão até o dia limite de pagamento do mês posterior\.

*Observação: C*onforme prevê a legislação o limite será de 60 meses \(5 anos\), mas faremos 60 dias inicialmente para atendimento ao cliente Bradesco e posteriormente será tratado via OS com a necessidade de criação de parâmetro, no intuito de tratar performance\.

CH6745\_2016

__RN20\.b__

Não deverá ser alterado o processo para o calculo de Juros e Multa\. Atualmente o sistema considera os seguintes critérios para o cálculo: Com base na data do fato gerador \(da nota\), para considerar o período do lançamento na tela da geração de INSS, usando o dia  \(do mês posterior\) informado no campo ‘Dia  Limite do Recolhimento’ \(parametrizado na tela Parametros DARF/GPS\) e a data do recolhimento \(considerada a data do efetivo pagamento\), informada na tela da Geração de retenção de INSS\.

Exemplificando:

Data do fato gerador : 01/01/2011, dia Limite do Recolhimento: 20, neste caso o sistema considerará juros e multa se a data de recolhimento for superior à data 20/02/2011\.

OS3359

__RN21__

Na rotina da geração das retenções de INSS \(alterar a consolidação e a geração através das notas\), para recuperar os dados da SAFx07 \(populando as tabelas irt\_ret\_inss\_df e irt\_ret\_inss\_ced\), quando os registros não possuírem valor de INSS \(Base, Valor de imposto e Alíquota\) e possuir o valor de Outras Entidades\. 

Esta alteração deve contemplar as consolidações Por Estabelecimento \(Avulso\) e Por Cedente \(Fonte\)\.

Há três formas de gerar as retenções: Por Pessoa FISJUR x Alíquota, Por Código de Retenção ou Código de Retenção x Alíquota, porém, para estes casos \(que só exista o valor de Outras Entidades\), a alíquota deverá ser recuperada na tela de parametrização do INSS, considerando o código de pagamento  informado na nota fiscal\.

Não deve ser alterado a package saf\_inss\_consolidacao, com relação ao valor mínimo de retenções de INSS, pois o campo Outras entidades não influencia neste valor\. 

Se existir no documento, valores no campo Outras Entidades, e  valor de INSS \(que não tenha atingido o valor mínimo de retenção\), a GPS não deve ser gerada, para o mês em questão\. Os valores deverão ser armazenados para a geração do mês ubsequente, quando o valor mínimo for atingido\.

OS2839\-A

__RN22__

Criar uma nova msg no log da geração das retenções de INSS, apenas para os documentos que possuem valor de Outras Entidades e que não possuem valores de INSS\. 

Na mensagem deverá ser listado o código de pagamento que não possuir a seguinte parametrização:

\- Não foi utilizada a regra de Código de Pagamento  em __Parâmetros DARF/GPS __e 

\- Os códigos não estejam parametrizados na opção__ Parâmetro de INSS__\. 

__Obs\. Para estes casos \(que só existe valor de Outras Entidades, sem valor de INSS\), deve\-ser usado obrigatoriamente a regra de Códigos de Pagamento \(Parâmetros DARF/GPS\)\.__

As informações serão recuperadas da SAFX07, mostrando a seguinte msg: 

__Não há parametrização para o cód\. De pagto exclusivo para Outras Entidades\. Parametrize em Parâmetros DARF/GPS, usando a regra por Cód\. De Pagto e depois informe o código em Parâmetro de INSS\.__

OS2839\-A

__RN23__

Ao gerar a GPS por Cedente \(*ver campo Tipo de Consolidação = Por Cedente \(Fonte\) no menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Parâmetro de INSS*\) e quando o campo 172 da SAFX07 estiver preenchido, o sistema deverá considerar como CEI, o CEI do Cedente, ou seja, do Prestador do Serviço\.

Por exemplo, caso no critério de consolidação, existam 2 NF’s de serviço com mesmo Código de Pagamento INSS \(campo 127 da SAFX07\), Pessoa Física/Jurídica \(campos 06 e 07 da SAFX07\) e Alíquota INSS \(campo 86 da SAFX07\) possuam CEI’s diferentes \(campo 172 da SAFX07\), deverão ser gerados duas GPS’s e o CEI a ser gerado será recuperado conforme regra abaixo:

Tela: Manutenção de Dados de Retenção

Menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção de Dados de Retenção 

Campo: Código CEI – recuperar a informação do campo 30 da SAFX04

Tela: Nova Consolidação das Retenções

Menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção da Consolidação das Retenções 

Campo: Código CEI – recuperar a informação do campo 30 da SAFX04

Tela: Nova Digitação GPS

Menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação 

Campo: Código CEI – recuperar a informação do campo 30 da SAFX04

Caso o campo 30 da SAFX04 não esteja preenchido, recuperar o CPF/CNPJ do Cedente através do campo 06 da SAFX04\.

OS3216

__RN24__

Na GPS a ser gerada deverá ser gerada no campo 05 o CEI do Cedente\. Essa informação deverá ser recuperada conforme a RN23, ou seja, do campo 30 da SAFX04\.

OS3216

__RN25__

Na coluna de Observações da GPS, deverá ser informado o CEI da Obra\. Essa informação deve ser recuperada do campo 172 da SAFX07, conforme texto abaixo:

__CÓDIGO CEI OBRA: <<CAMPO 172 – SAFX07>>__

__RN26__

__\[ALTERADA – CH19809\_2012\]__

Na rotina de geração das retenções de INSS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS\) do módulo Obrigações de Tributos Federais, o cálculo de Juros e Multa deverá considerar o Valor de Outras Entidades, além do Valor do INSS Retido\. A regra para o cálculo de Juros e Multa é a seguinte:

- __JUROS__

Deverá ser aplicado 1% de Juros – caso o pagamento exceda a data limite de pagamento do tributo – sobre o Valor Total, que é formado sobre o Valor do INSS Retido \(campo 87 da SAFX07\) \+ Valor de Outras Entidades \(campo 214 da SAFX07\)\. *OBS:* A regra de 1% é definida em lei e não serão utilizados os Juros da SELIC, pois os mesmos só são aplicáveis nos casos de parcelamentos de Tributos Federais, como por exemplo, Imposto de Renda Retido na Fonte e PIS/COFINS\. No caso do INSS como o pagamento é a vista o Juros não utiliza  a SELIC como parâmetro

- 
	- Deverá ser aplicado Taxa Selic \(campo “Valor” da tela Índice de Conversão do módulo DW\) a partir do primeiro dia do mês subsequente ao vencimento do prazo até o mês anterior ao do pagamento e de 1% \(um por cento\) no mês do pagamento\.

__*Exemplo 1*:__

__Competência__

__Vencimento__

__ Pagamento__

__Valor INSS__

__Valor Juros__

__Valor Total__

06/2012

07/2012

13/09/2012

430,78

7,28

\(4,30 = 1% no mês do pagamento

\+ 2,98 = 0,69% da SELIC de Agosto/2012\)

513,40

__*Exemplo 2*:__

__Competência__

__Vencimento__

__Data Pagamento__

__Valor INSS__

__Valor Juros__

__Valor Total__

05/2012

06/2012

13/09/2012

430,78

10,20 \(4,30 = 1% no mês do pagamento 

\+ 2,98 = 0,69% da SELIC de Agosto/2012 

\+ 2,93 = 0,68% da SELIC de Julho/2012

527,13

- 
	- Quando a data de vencimento \(campo “Dia Limite para Recebimento” na tela Parâmetros DARF/GPS \) e a data de recolhimento \(campo “Data para recolhimento” na tela Geração das Retenções do INSS estiverem dentro do mesmo mês, não deverá ter calculo de juros\.

__*Exemplo 3*:__

__Competência__

__Vencimento__

__Data Pagamento__

__Valor INSS__

__Valor Juros__

__Valor Total__

08/2012

09/2012

28/09/2012

430,78

0,00

442,15

__*Exemplo 4:*__

__Competência__

__Vencimento__

__Data Pagamento__

__Valor INSS__

__Valor Juros__

__Valor Total__

08/2012

09/2012

13/09/2012

430,78

0,00

430,78

- 
	- Quando o pagamento ocorrer no mês posterior ao do vencimento, deverá ser aplicado somente 1% de Juros sobre o valor, sem a incidência da Taxa Selic\.

__*Exemplo 5*:__

__Competência__

__Vencimento__

__Data Pagamento__

__Valor INSS__

__Valor Juros__

__Valor Total__

07/2012

08/2012

13/09/2012

430,78

4,30 = 1% no mês do pagamento sem SELIC

442,15

Para os exemplos acima, deve ser considerado como Valor Total, o Valor do INSS Retido \(campo 87 da SAFX07\) \+ Valor de Outras Entidades \(campo 214 da SAFX07\)\. 

__\[ALTERADA – CH843\_2015\]/\[ALTERADA – CH16317\_2015\]__

- __MULTA__
	- Deverá ser aplicado 0,33% de Multa diária por dia de atraso – caso o pagamento exceda a data limite de pagamento do tributo – limitado a no máximo 20% de acordo com os parâmetros de DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) do módulo Obrigações de Tributos Federais sobre o Valor Total, que é formado sobre o Valor do INSS Retido \(campo 87 da SAFX07\) \+ Valor de Outras Entidades \(campo 214 da SAFX07\)\. 
	- Quando a data de recolhimento informada na consolidação das retenções for superior à data de vencimento fixa no código \(dia 20 do mês subsequente ao da competência\) e for selecionada opção de calcular juros e multa, o sistema deverá identificar quantos dias __corridos__ de atraso ocorreram entre o vencimento e o pagamento, a partir do primeiro dia  útil ao do vencimento do prazo previsto para o pagamento do tributo ou contribuição até o dia em que ocorrer o seu pagamento e multiplicar esse nº de dias pelo valor informado no campo “Multa Diária”\. 
	- Aplicar o percentual encontrado sobre o valor da contribuição para chegar ao valor da multa\. Quando o resultado da mutiplicação da Multa diária pelo número de dias de atraso for maior que o valor informado no campo “Limite de Multa”, considerar o percentual informado no campo “Limite de Multa”\.

__*Exemplo 1:*__

__Quando o atraso inicia/vence em dia útil__

Número de dias: 8                                      cálculo: 8 x 0,33 = 2,64                  

Multa Diária: 0,33                                        450 x 2,64% = 11,88            

Valor da Contribuição: 450

*Observação: *o número de dias se iniciou ou venceu em dia de expediente normal \(dia útil\), conforme o parágrafo único do artigo 210 do CTN\.

__*Exemplo 2:*__

__Quando o atraso não inicia/vence em dia útil__

Número de dias: 8                                      cálculo: 6 x 0,33 = 1,98                  

Multa Diária: 0,33                                        450 x 1,98% = 8,91            

Valor da Contribuição: 450

*Observação: *o número de dias não se iniciou ou venceu em dia de expediente normal \(dia útil\), conforme o parágrafo único do artigo 210 do CTN, ou seja, supondo que o vencimento tenha iniciado no sábado, deve ser contado a partir da segunda\-feira do vencimento \(dia útil\), contando então \-2 dias\.

CH112249\_V2

CH19809\_2012

__CH843\_2015__

__RN27__

Durante o processo de Consolidação das Retenções de INSS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS\) do módulo Obrigações de Tributos Federais, o campo “Total Recolhimento” da tela de Digitação da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\) deverá ser calculado da seguinte maneira:

Total Recolhimento = Valor INSS \+ ATM \+ Juros \+ Multa \+ Outros Valores \(campo 7\) \+ Outros Valores \(campo 8\) \+ __*Valor de Outras Entidades*__

Atualmente esse campo não considera o Valor de Outras Entidades, e o mesmo deve ser considerado\.

CH112249\_V2 

__RN28__

Os campos “Juros” e “Multa” da tela de Digitação da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\) do módulo Obrigações de Tributos Federais, deverão ser populados com as regras de Juros e Multa considerando o Valor de Outras Entidades – ver RN26\.

CH112249\_V2

__RN29__

A rotina de Emissão da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Emissão\) do módulo Obrigações de Tributos Federais, não será alterada, visto que o campo 11 – TOTAL já está considerando os campos Valor INSS \+ ATM \+ Juros \+ Multa \+ Outros Valores \(campo 7\) \+ Outros Valores \(campo 8\) \+ Valor de Outras Entidades\.

CH112249\_V2

__RN30__

Alterar para R$ 10,00 o valor mínimo de recolhimento de contribuição do Instituto Nacional do Seguro Social \(INSS\), via Guia da Previdência Social \(GPS\)\.

CH1069\_2012

__RN31__

A geração das retenções do INSS por Empresa irá ser realizada da seguinte forma:

- Processamento dos Dados das Retenções de INSS __por Empresa__:
	- Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela Parâmetros DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) esteja marcado, a geração irá ocorrer de forma centralizada, ou seja, as retenções serão consolidadas no Estabelecimento Matriz, ou seja, o Estabelecimento que está definido como Matriz no cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.
	- Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela Parâmetros DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) esteja desmarcado, a geração irá ocorrer de forma descentralizada, ou seja, as informações geradas serão por Estabelecimento – independente se o Estabelecimento selecionado for o Matriz\. Nesse caso é importante salientar que o conceito Multi\-Empresa \(criado na OS3096\-E\) deverá ser mantido\.
- Processamento dos Dados das Retenções de INSS __por Estabelecimento__:
	- Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela Parâmetros DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) esteja desmarcado, a geração irá ocorrer de forma descentralizada, ou seja, as informações geradas serão por Estabelecimento – independente se o Estabelecimento selecionado for o Matriz\.
	- Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela Parâmetros DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) esteja marcado, o cliente não conseguirá gerar a GPS por Estabelecimento, obrigando o mesmo a desmarcar o parâmetro\.

OS3668

__RN32__

Durante a rotina de geração das retenções do INSS, caso a pessoa física/jurídica seja uma Pessoa Física \(campo CPF/CNPJ da SAFX04 com 11 posições\), deverá ser gerado no campo 5 – Identificador da Guia da Previdência Social, a informação contida no campo “Número PIS/PASEP/NIT” dessa Pessoa Física\.

CH7862\_2012

__RN33__

Caso durante a geração, o prestador Pessoa Física não possua o campo “Número PIS/PASEP/NIT” preenchido, a informação gerada no campo 5 – Identificador deverá ser o CPF da mesma\.

CH7862\_2012

__RN34__

Caso durante a geração o prestador seja uma Pessoa Jurídica \(campo CPF/CNPJ da SAFX04 com 14 posições\), a informação a ser gerada no campo 5 – Identificador continuará sendo o “CNPJ” dessa Pessoa Jurídica\.

CH7862\_2012

__RN35__

Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela de Parâmetros por DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) do módulo Obrigações de Tributos Federais esteja selecionado, a opção de Processar Dados por Estabelecimento da tela de Geração das Retenções do INSS deverá ficar desabilitada, para que o usuário gere a GPS consolidada pelo Estabelecimento Matriz somente por empresa\.

Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela de Parâmetros por DARF/GPS \(menu: Parâmetros >> Parâmetros DARF/GPS\) do módulo Obrigações de Tributos Federais esteja desmarcado, o comportamento continua como atualmente, ou seja, o sistema permite a seleção do parâmetro\.

OS3668

__RN36__

Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” esteja selecionado, deverá ser exibida a seguinte mensagem abaixo do parâmetro “Processar por – Empresa OU Estabelecimento”:

“O parâmetro “Consolida GPS por Estabelecimento Matriz” está selecionado e a geração deverá ser feita por Empresa\.”

Essa mensagem se faz necessária para facilitar o entendimento do usuário acerca da funcionalidade\.

Caso o parâmetro “Consolida GPS por Estabelecimento Matriz” esteja desmarcado, essa mensagem não será exibida\.

OS3668

__RN37__

O parâmetro “Consolida GPS por Estabelecimento Matriz” deverá ter seu nome alterado para “Consolida GPS por Estabelecimento Matriz”\. Essa mudança se faz necessária para facilitar o entendimento do usuário sobre a funcionalidade desse parâmetro\.

OS3668

__RN38__

A geração da GPS Centralizada irá ocorrer desde que os estabelecimentos centralizados pertençam ao mesmo grupo ligado à Pessoa Física/Jurídica\. Isso ocorre devido à toda a estrutura da GPS possuir como campo\-chave o Grupo de Validade\.

Caso um estabelecimento centralizado não pertença ao mesmo grupo e o cliente gere a GPS centralizada, o sistema não irá gerar as informações do estabelecimento centralizado nem no Estabelecimento Matriz e nem no Estabelecimento Filial\.

Além da não geração, será exibida uma mensagem de erro no log por empresa, citando o código da empresa informando do fato:

“Há Estabelecimento\(s\) centralizado\(s\) que não pertence\(m\) ao mesmo Grupo de Validade de Pessoa Física/Jurídica e por isso suas informações não foram geradas\. Para a correta geração desse\(s\) Estabelecimento\(s\), o mesmo deve pertencer ao mesmo grupo do Estabelecimento Matriz ou o mesmo deve ser gerado isoladamente, através da geração por Estabelecimento\.

OS3668

__RN39__

Caso o cliente gere a GPS, o sistema deverá gravar no campo “Número do Processo” o Número do Processo pertinente de acordo com as regras abaixo e critério de geração da GPS selecionado:

- Caso na tela de Geração da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS a opção selecionada no campo “Processar” seja “Retenções do INSS a partir das Notas Fiscais”:
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_RET\_INSS\_DF \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção de Dados da Retenção\)

__OBS: nesse caso, o Número do Processo não será informado para a Consolidação ou Digitação\.__

- Caso na tela de Geração da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS a opção selecionada no campo “Processar” seja “Consolidação das retenções para emissão da GPS”:
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_RET\_INSS\_CED \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção da Consolidação das Retenções\)
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\)

__OBS: nesse caso, o mesmo Número do Processo da Consolidação será o da Digitação\.__

- Caso na tela de Geração da GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS a opção selecionada no campo “Processar” seja “Ambas”:
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_RET\_INSS\_DF \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção de Dados da Retenção\)
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_RET\_INSS\_CED \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Manutenção da Consolidação das Retenções\)
	- Gravar o Número do Processo no campo NUM\_PROCESSO da tabela IRT\_GPS \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\)

__OBS: nessas três manutenções, o Número do Processo será o mesmo\.__

Vale salientar que caso o cliente gere a GPS sem ser pela opção “Ambas”, o Número de Processo da tela de Retenções de INSS será diferente em relação às telas de Consolidação e Digitação que nesse caso serão iguais\.

Caso o cliente inclua algum registro manualmente – Retenção, Consolidação ou Digitação – o campo de Número do Processo assumirá o valor “0”\. Caso o cliente realize alguma manutenção em um registro gerado de forma automática nessas telas – Retenção, Consolidação ou Digitação, o Número do Processo permanecerá\.

CH2806\-A\_2012

__RN40__

Ao informar que utiliza o módulo FUNRURAL \(parâmetro __‘Processar contribuições de INSS para o FUNRURAL’, __preenchido com ‘SIM’\), na tela ‘Geração de Retenções de INSS’ \(localizada em Federal/ Obrigações de Tributos Federais / Outras Obrigações/ Retenções de INSS – Serviços Prestados\) desconsiderar dos registros pré\-selecionados, as notas da SAFX07, que estão na SAFX63 com a Situação Especial: 03\- Depósito Judicial, no processo de Consolidação das retenções para a emissão da GPS\.

Também não devem ser gerados na tela de digitação da GPS \(GPS/Digitação\), os registros que estão na SAFX63 com a Situação Especial: 03\- Depósito Judicial\.

Referente ao processo das Retenções do INSS a partir das notas fiscais, nada será alterado, pois o processo atualmente já não considera os dados da SAFX63\.

OS3904

__RN41__

Se o parâmetro __‘Processar contribuições de INSS para o FUNRURAL’ __

estiver preenchido com ‘Não’, nada será alterado\.

OS3904

__RN42__

Parâmetro “__Considerar apenas retenções NÃO processadas__”

Na geração das Retenções do INSS, se o parâmetro "Considerar apenas retenções NÃO processadas" __estiver__ marcado somente as notas que não foram consideradas em processamentos anteriores e que atendem aos critérios de seleção serão consideradas na geração\. Neste caso, as informações já processadas serão mantidas e as e novas retenções e consolidações devem ser geradas\.

Se o parâmetro "Considerar apenas retenções NÃO processadas" __não estiver__ marcado todas as notas serão consideradas e as retenções do período devem ser regeradas e consolidadas\.

As regras deste parâmetro se aplicam tanto para processamento por empresa, quanto por estabelecimento\. E se aplica também para as situações em que o parâmetro “Consolida GPS por Estabelecimento Matriz” da tela Parâmetros DARF/GPS está selecionado, a diferença neste caso é que as informações serão gravadas para o estabelecimento centralizador\.

CH13919/2013

__RN43__

Parâmetro __“Emitir Guias”__ na Emissão da GPS:

__*Localização:*__

Módulo Federal – OTF

Item de Menu Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Emissão

Criação do parâmetro “Emitir Guias” em combo box deverá conter as seguintes opções: Pagas, Abertas ou Ambas\. A opção Ambas será Default\.

__*Emissão da GPS*__

Se no processamento da emissão das Guias, o parâmetro da tela Relatório de Guia de Previdência Social “Emitir Guias” estiver selecionada com a opção *Pagas*, então emitir as Guias quando o campo Status Guia for igual a Pago e as datas de Envio Bancário e Data Pagamento estiverem preenchidas na tela de Digitação GPS de acordo com o mês/ competência ou período fiscal selecionado no item Lançamentos\.

  Senão

     Se no processamento da emissão das Guias, o parâmetro da tela Relatório de Guia de Previdência Social “Emitir Guias” estiver selecionada com a opção *Abertas*, então emitir as Guias quando o campo Status Guia for igual a Aberto de acordo com o mês/ competência ou período fiscal selecionado no item Lançamentos\.

     Senão

         Se no processamento da emissão das Guias, o parâmetro da tela Relatório de Guia de Previdência Social “Emitir Guias” estiver selecionada com a opção *Ambas*, então emitir as Guias quando o campo Status Guia for igual a Pago e Aberto independente das datas de Envio Bancário e Data Pagamento estiverem preenchidas ou não na tela de Digitação GPS \(podendo ocorrer de só um campo estar preenchido dessas datas\) de acordo com o mês/ competência ou período fiscal selecionado no item Lançamentos\.

MFS\-6168

__RN44__

__Geração da GPS:__

__*Localização:*__

Módulo Federal – OTF

Item de Menu Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Emissão

__Tratamento:__

Se na grid “Seleção de Pagamentos” o valor ‘2500’ estiver marcado E a opção ‘GPS para Associações Desportiva’ for selecionada, na emissão da GPS deverá gerar com o título de ‘Contratado no campo 01 da GPS junto as informações da Pessoa Física Jurídica "Nome e CNPJ" \(Cedente\) que o sistema atualmente gera corretamente\.

 

__CH4837\_2017__

	

