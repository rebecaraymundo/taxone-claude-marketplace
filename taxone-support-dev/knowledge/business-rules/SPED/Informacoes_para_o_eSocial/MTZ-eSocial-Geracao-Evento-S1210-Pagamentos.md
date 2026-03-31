# MTZ-eSocial-Geracao-Evento-S1210-Pagamentos

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1210-Pagamentos.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 96 KB

---

THOMSON REUTERS

Módulo eSocial

Geração Evento S\-1210

\(Pagamentos de Rendimentos do Trabalho\) 

__Localização__: Menu SPED, módulo Informações para o eSocial, menu Geração 🡪 Geração dos Movimentos 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS15870__

Luciano Ribeiro

Geração dos dados do evento S\-1210 \(Pagamentos de Rendimentos do Trabalho\)

26/12/2017 

\(criação do documento\)

__MFS18065__

Eduardo Cruz

\-Inclusão do campo matricula no registro infoPgtoParc; 

07/06/2018

__MFS16751__

Luciano Ribeiro

Críticas em relação a regeração dos eventos\. 

27/03/2018

<a id="_Hlk523235881"></a>__MFS16762__

Lara Aline

Inclusão rotina de Reprocessar Evento

28/08/2018

MFS\-60476

Rogério Ohashi

Ajuste na regra de geração do Campo__ “__cpfTrab” para considerar o Campo CPF\_SP__ __da tabela X04\_PESSOA\_FIS\_JUR __preenchido__, __E__ __quando__ o Campo 27 \- Classe de Empresa” __for Igual__ a "05 – MEI \(Micro Empreendedor Individual\)\. Tratamento para atender os eventos S\-1200 e S\-1210 para fornecedores autônomos MEI\. \(Estavam sendo desconsiderados por estarem cadastrados pelo CNPJ\)\.

25/03/2021

__MFS\-87306__

__Elisabete Costa__

__Alterações Versão S\-1\.0__

__03/06/2022__

__MFS\-96008__

__Elisabete Costa__

Retirada do Módulo: __Informações para o E\-Social__ do __T1__

__04/11/2022__

Sumário

[1\.	Parâmetros da Tela	2](#_Toc517780654)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc517780655)

[3\.	Verificação do Status de Eventos já Gerados	5](#_Toc517780656)

[4\.	Gravação dos Dados	7](#_Toc517780657)

__Devido ao end\-of\-support da mensageria OS E\-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E\-Social será retirado do TAX ONE e deverá permanecer no DW\.__

# <a id="_Toc517780654"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1210\.

A geração dos dados do S\-1210 é feita apenas para os trabalhadores autônomos, cujas informações são carregadas para as tabelas SAFX247/248/249/250\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\-eSocial\-Geracao\-Movimentos*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc517780655"></a>Recuperação dos Dados e Processamento

__Origem dos dados__: \- Parametrização “Dados Iniciais” do Módulo eSocial;

                                \- SAFX247 \- Demonstrativo de Pagamento dos Autônomos;

                                \- SAFX248 \- Demonstrativo de Pagamento dos Autônomos \(Rubricas\);

                                \- SAFX249 \- Demonstrativo de Pagamento dos Autônomos \(Pagamentos Parciais\);

                                \- SAFX04 \- \(Cadastro de Pessoas Fis/Jur\);

__Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:__

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

     \- Estabelecimento – estabelecimento selecionado na tela da geração;

__Sobre a recuperação dos pagamentos efetuados no período:__

O objetivo do evento S\-1210 é demonstrar todos os pagamentos de trabalhadores, efetuados no período informado para a geração\.

Os pagamentos podem ser totais ou parciais\. 

Um pagamento total é quando o valor pago corresponde ao valor integral que aparece no demonstrativo de pagamento\.

Um pagamento parcial é quando o valor pago NÃO corresponde ao valor integral que aparece no demonstrativo de pagamento, sendo apenas parte deste\. 

A identificação se o pagamento referente a um Demonstrativo de Pagamento \(SAFX247\) é total ou parcial, é feita pelo campo “*09\-Indicador de Pagamento Total*”\. Quando é um pagamento parcial, os valores parciais pagos são carregados para a Tabela dos Pagamentos Parciais \(SAFX249\)\.  

Desta forma, para gerar o evento S\-1210, é necessário recuperar os pagamentos totais da SAFX247 e os pagamentos parciais da SAFX249, sendo pré\-requisito que o pagamento seja efetuado no período informado para a geração\. 

     \- Recuperação dos pagamentos totais na SAFX247:

   

     \- __Empresa__ – empresa do estabelecimento centralizador selecionado;

     \- __Estabelecimento__ – Serão recuperados os pagamentos de todos os estabelecimentos envolvidos na centralização \(o estabelecimento

       centralizador, que é o selecionado em tela, e os centralizados\), de acordo com a parametrização das obrigações federais do módulo

       Parâmetros \(menu Preliminares > Centralização da Escrituração de Obrigações Federais\);

     \- __Indicador de Pagamento Total \(campo 09\) __– “S”;

     \- __Data do Pagamento \(campo 10\) __– Mês/Ano informados na tela da geração \(campo “*Período \(MM/AAAA\)*”\);

     \- Recuperação dos pagamentos parciais na SAFX249:

     \- __Empresa__ – empresa do estabelecimento centralizador selecionado;

     \- __Estabelecimento__ – Serão recuperados os pagamentos de todos os estabelecimentos envolvidos na centralização \(o estabelecimento

       centralizador, que é o selecionado em tela, e os centralizados\), de acordo com a parametrização das obrigações federais do módulo

       Parâmetros \(menu Preliminares > Centralização da Escrituração de Obrigações Federais\);

     \- __Data do Pagamento \(campo 08\) __– Mês/Ano informados na tela da geração \(campo “*Período \(MM/AAAA\)*”\);

__Agrupamento dos dados:__

No evento S\-1210, as informações específicas sobre os pagamentos ficam no registro “__infoPgto__”, e seus registros filhos “__detPgtoFl__” __\(O registro detPgtoFl deixa de existir a partir da versão S\-1\.0, os campos passarão a fazer parte do registro infoPgto\.\)__

\.

Devido à hierarquia dos registros do evento S\-1210, os pagamentos recuperados serão agrupados pelas seguintes informações:

*\(observar a hierarquia dos dados no layout do S\-1210\)*

Data do Pagamento

Campo 10\-Data de Pagamento, no caso da SAFX247

Campo 08\-Data de Pagamento, no caso da SAFX249

Tipo do Pagamento

Campo 11\-Tipo do Pagamento, no caso da SAFX247

Campo 11\-Tipo do Pagamento, no caso da SAFX249

Período de Competência

Campos 02\-Ano Competência e 03\-Mês Competência, no caso da SAFX247 

Campos 02\-Ano Competência e 03\-Mês Competência, no caso da SAFX249

Identificador do Demonstrativo de Pagamento

Campo 07\-Identificador do Demonstrativo de Pagamento, no caso da SAFX247

Campo 07\-Identificador do Demonstrativo de Pagamento, no caso da SAFX249

__Até a versão 2\.5: __

	Para cada combinação de Data do Pagamento \+ Tipo do Pagamento, será gerado um registro __infoPgto__\. 

	Para cada combinação de Período de Competência \+ Identificador do Demonstrativo de Pagamento, será gerado um registro “filho” __detPgtoFl__\. 

	A partir do registro “filho” __detPgtoFl__, os dados do pagamento serão gerados no registro __retPgtoTot__ ou no  __infoPgtoParc__, dependendo tratar\-se de pagamento total ou parcial\.

*	\(esses registros “retPgtoTot” e “infoPgtoParc” são registros “filhos do “detPgtoFl”, ambos do mesmo nível\)*

Desta forma, teremos:

__infoPgto__ \- Agrupamento dos pagamentos efetuados na mesma DATA e que sejam do mesmo Tipo de Pagamento;

       __detPgtoFl__ \- Identificação do Período de Competência  e do Identificador do Demonstrativo a que se refere o pagamento;

              __retPgtoTot__ – Registro a ser preenchido quando se tratar de pagamento integral;

              __infoPgtoParc__ \- Registro a ser preenchido quando se tratar de pagamento parcial;

__A partir da versão S\-1\.0: __

	Para cada combinação de Data do Pagamento \+ Tipo do Pagamento \+ Período de Competência \+ Identificador do Demonstrativo de Pagamento, será gerado um registro __infoPgto__\. 

Obs: Este agrupamento dos pagamentos é necessário apenas para o caso em que existir mais de um pagamento efetuado no período para o mesmo trabalhador\. Sejam pagamentos referentes a mais de um demonstrativo, ou pagamentos referentes a diferentes parcelas de um mesmo demonstrativo\.

# <a id="_Toc509582647"></a><a id="_Toc509925718"></a><a id="_Toc509929675"></a><a id="_Toc509937127"></a><a id="_Toc517780656"></a>Verificação do Status de Eventos já Gerados

__MFS16751__: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente\. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1210\_OC, coluna IND\_STATUS\)\.

Para cada beneficiário a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este beneficiário no mesmo período de competência\.

__Caso não:__ 

      O evento do beneficiário será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

      A geração de um novo evento para o beneficiário dependerá do status do evento já existente, da seguinte forma:

__Status__

__Permite regeração dos dados__

1\-Aguardando geração XML

Sim

3\-Enviando para mensageria

Não

4\-Erro geração XML

Sim

5\-Evento recebido pela mensageria

Não

6\-Evento rejeitado pela mensageria

Sim 

7\-Em Processamento \(mensageria\)

Não

8\-Recebido pelo Fisco com sucesso

Sim \(Retificação\)

9\-Recebido pelo Fisco com advertência

Sim \(Retificação\)

10\-Rejeitado pelo Fisco

Sim

12\-Evento Excluído

Sim

14\-Evento excluído na mensageria

Sim

15\-Erro técnico na mensageria

Sim__ __

       Se o status do evento já existente __não__ __permitir regeração__:

            Nesse caso, o beneficiário em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:

*                  Aviso: Já existe evento anterior gerado para o beneficiário\. O status do evento não permite uma nova geração\.*

*                  Dados do Registro:  Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX, *__*Período*__*: XX/XXXX *

       Se o status do evento já existente __permitir regeração__:

            Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação __ORIGINAL__ ou uma

            __RETIFICAÇÃO__, dependendo do status do evento original, como descrito a seguir:

            \- Se status do evento original = 8 ou = 9 🡪 Nesse caso, o novo evento será gerado como __RETIFICAÇÃO__;

            \- Se status do evento original <> 8 e <> 9 🡪 Nesse caso, o novo evento será gerado como __ORIGINAL__;

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

<a id="_Hlk523235760"></a>__\[MFS16762\]__

<a id="_Hlk523155984"></a>__Importante:__ Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação \(Critérios estão no documento de tela do Painel de Controle de Eventos\) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\. 

# <a id="_Toc517780657"></a>Gravação dos Dados

A partir dos dados recuperados das tabelas SAFX247 e SAFX249 \(conforme os critérios descritos acima\), será gerado um evento S\-1210 __para cada trabalhador__\.

*\(os registros não citados não serão gerados\)*

__Registro evtPgtos__ – Evento Pagamentos de Rendimentos do Trabalhado

id

Identificação do evento, conforme REGRA\_VALIDA\_ID\_EVENTO:

“ID” \+ “1” \+ CNPJ do estabelecimento \+ data da geração \(AAAAMMDD\) \+ hora da geração \(HHMMSS\) \+ sequencial

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita;

Sequencial \(99999\) \- Número sequencial da chave\. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora\. 

__Registro ideEvento__ \- Informações de Identificação do evento\.

indRetif

Conteúdo fixo = “1” \(Arquivo original\)

OBS: A princípio, este campo será gerado sempre como “1” \(Arquivo original\)\. Somente após a criação do painel é que teremos o controle automático, para verificar se é uma retificação ou não\.

__MFS16751__: Alteração para gerar também os eventos de retificação\.

Este campo será gerado de acordo com a verificação de status descrita no item “*3\-Verificação do Status de Eventos já Gerados*”:

__Se__ for a primeira geração do evento do beneficiário no período:

      O campo será gerado com “__1__” \(__Arquivo Original__\);

__Senão__

      Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:

      Se status do evento original = 8 ou = 9 🡪 O campo será gerado com “__2__” \(__Retificação__\);

      Se status do evento original <> 8 e <> 9 🡪 O campo será gerado com “__1__” \(__Arquivo Original__\);

nrRecibo

Este campo não será gerado

OBS: Este campo será gerado somente após a criação do painel, quando teremos o controle automático para verificar se é uma retificação ou não\.

__MFS16751__: Alteração para gerar também os eventos de retificação\.

Este campo será gerado de acordo com o conteúdo do campo anterior \(__indRetif__\), da seguinte forma:

Se indRetif = “1” \(Arquivo Original\)

     Nesse caso este campo *não* será gerado;

Se indRetif = “2” \(Retificação\)

     Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado\. Ou seja, com o conteúdo

     do campo nrRecibo que consta no *evento original*;

__indApuracao__

__MFS\-87306: Vrs\.S\-1\.0__

Conteúdo fixo = “1” \(= Mensal\)

*\(como os autônomos não têm décimo terceiro salário, este campo será gerado sempre como “1”\)*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

perApur

Mês e ano do período informado na tela da geração, no formato AAAA\-MM \(conforme orientação do layout\)

__indGuia__

__MFS\-87306: Vrs\.S\-1\.0__

A partir da versão S\-1\.0 foi criado o campo indGuia\. __O mesmo não deve ser gerado__, pois é destinado a ser informado apenas por empregadores pessoas físicas e usado apenas para o recolhimento unificado dos tributos e do FGTS pelos empregadores __domésticos__\.

tpAmb

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

procEmi

Conteúdo fixo = “1” \(= Aplicativo do empregador\)

verProc 

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\. 

*Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideEmpregador__ \- Informações de identificação do empregador\.

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita;

__Registro ideBenef__ \- Informações do beneficiário do pagamento\.

As informações do trabalhador serão recuperadas no seu cadastro na __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da SAFX247\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

cpfBenef

\[__ALTERAÇÃO\- MFS60476__\] Tratamento para fornecedores autônomos MEI\.

Caso existir informação no campo CPF\_SP da tabela X04\_PESSOA\_FIS\_JUR, __E se__ o Campo IND\_CLASSE\_EMP, \(Campo 27 \- Classe de Empresa\), da tabela X04\_PESSOA\_FIS\_JUR __for__ __igual__ a "05 – MEI \(Micro Empreendedor Individual\)", gerar o campo com a informação do campo CPF\_SP, caso contrário seguir com a regra original:

Campo 06\-CPF\-CGC da SAFX04

Como se trata de autônomos, a pessoa fis/jur deve ser uma pessoa física\. Por isso, será verificado o conteúdo do campo “06\-CPF\-CGC” da pessoa fis/jur recuperada da SAFX04\. Se o conteúdo deste campo for um CNPJ, será gravada a mensagem abaixo no log, e o campo cpfBenef não será gerado\.

*Erro: O campo CPF do Beneficiário \(cpfBenef\) deve ser um CPF\. A informação não será gerada no evento\.*

*Origem: Campo “06\-CPF\-CGC” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Registro deps__ \- Informações de dependentes do beneficiário

	

Este registro será gerado apenas quando o beneficiário tiver a informação de dependentes na __SAFX04__, ou seja, quando o campo “46\-Quantidade de Dependentes Imposto de Renda” estiver preenchido, e seu conteúdo for <> zeros\.

Caso contrário, o registro “deps” não será gerado\.

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 o registro e todos os seus campos não serão gerados\.__

*Obs: As regras p/ recuperação dos dados cadastrais do trabalhador na SAFX04 estão descritas acima \(registro ideBenef\)\.*

vrDedDep

Este valor será calculado da seguinte forma:

                          \[ Número de dependentes do trabalhador x Valor de dedução por dependente \]

Sendo:

Número de dependentes do trabalhador = número de dependentes do cadastro do trabalhador \(SAFX04, campo 46\-Quantidade de Dependentes Imposto de Renda\);

Valor de dedução por dependente = valor parametrizado nos dados iniciais \(menu Parâmetros > Dados Iniciais\);

__Registro infoPgto__ – Informações dos pagamentos efetuados

dtPgto

Data do pagamento, conforme regra de agrupamento descrita no item “*2\-Recuperação dos Dados e Processamento*”

__tpPgto__

__MFS\-87306: Vrs\.S\-1\.0__

Tipo do pagamento, conforme regra de agrupamento descrita no item “*2\-Recuperação dos Dados e Processamento*”

Até a versão 2\.5\.0\. os valores válidos são:

1, 2, 3, 5, 6, 7, 9

__A partir da versão S\-1\.0, os valores válidos são:__

__1, 2, 3, 4, 5\. __

__indResBr__

__MFS\-87306: Vrs\.S\-1\.0__

Este campo é gerado a partir da informação do país cadastrado para o trabalhador na SAFX04, da seguinte forma:

Se País informado = Brasil, o campo será gravado com “S”;

Senão, o campo será gravado com “N”;

*Obs: As regras p/ recuperação dos dados cadastrais do trabalhador na SAFX04 estão descritas acima \(registro ideBenef\)\.*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

  

Caso o campo País não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Residente Fiscal no Brasil \(indResBr\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “21\-País” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Registro detPgtoFl__ – Detalhamento dos pagamentos efetuados

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\. __

__Os campos que serão mantidos passarão a fazer parte do registro infoPgto\.__

__Registro infoPgto__ – Informações dos pagamentos efetuados

perRef

Período de competência, conforme regra de agrupamento descrita no item “*2\-Recuperação dos Dados e Processamento*”\.

ideDmDev

Identificador do demonstrativo de pagamento, conforme regra de agrupamento descrita no item “*2\-Recuperação dos Dados e Processamento*”\.

__indPgtoTt__

__MFS\-87306: Vrs\.S\-1\.0__

Indicador de pagamento do demonstrativo de pagamento \(campo “09\-Indicador de Pagamento Total” da SAFX247\)

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

vrLiq

Este campo é gerado dependendo se o pagamento indicado no demonstrativo é total ou parcial \(campo “09\-Indicador de Pagamento Total” da SAFX247\), da seguinte forma:

__Se campo “09\-Indicador de Pagamento Total” = “S”__

      Nesse caso trata\-se de um pagamento total, então, este valor será gerado com o resultado da soma de todas as

      rubricas do demonstrativo \(__SAFX248__\), dependendo do tipo da rubrica:

      \[ Valor Total \(campo 13\) das rubricas do tipo “1” –  Valor Total \(campo 13\) das rubricas do tipo 2 \]

     

__Se campo “09\-Indicador de Pagamento Total” = “N”__

      Nesse caso trata\-se de um pagamento parcial, então, este valor será gerado com o resultado da soma de todas as

      rubricas indicadas na tabela dos pagamentos parciais \(__SAFX249__\), dependendo do tipo da rubrica:

      \[ Valor Total \(campo 15\) das rubricas do tipo “1” –  Valor Total \(campo 15\) das rubricas do tipo 2 \]

Rubricas do tipo “1” são os vencimentos, e do tipo “2” são os descontos *\(rubricas do tipo informativo \(3 e 4\) não       entram no cálculo\)\. *Para verificar o tipo da rubrica, acessar o cadastro de rubricas \(SAFX2114\) através dos campos       “08\-Código da Tabela da Rubrica” e “09\-Código da Rubrica”\.

Havendo mais de um registro da rubrica na SAFX2114, será considerado o registro de > data de validade inicial       cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. E a validade final deve estar nula ou       ser de um mês/ano que seja >= ao mês/ano do período informado na tela da geração\.

O tipo da rubrica é o campo 07\-Tipo de Rubrica da SAFX2114\.

__*OBS*__*: Para a recuperação dos dados das rubricas, seja na SAFX248, ou na SAFX249, lembrar que estas duas tabelas são tabelas “filhas” do demonstrativo \(SAFX247\)\. Assim, basta partir dos dados que compõe a chave da tabela mãe\.*

__nrRecArq__

__MFS\-87306: Vrs\.S\-1\.0__

Este campo não será gerado \(conforme mapeamento original, não se aplica a autônomos\)

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

__Registro retPgtoTot__ \- Retenções efetuadas no ato do pagamento pelo valor total do demonstrativo 

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 o registro e todos os seus campos não serão gerados\.__

Este registro será gerado a partir das rubricas da __SAFX248__, quando se tratar de pagamento total\.

Trata\-se exatamente das rubricas que foram consideradas para gerar o campo “__vrLiq__” do registro “pai” \(registro __detPgtoFl__\), para os casos de pagamento total\.

A diferença é que neste registro serão consideradas *apenas* as rubricas referentes a descontos do IRRF e pensão alimentícia, conforme as orientações do manual de layout\. 

Ou seja, serão consideradas apenas as rubricas que atendam a seguinte condição: 

            O campo “11\-Código Incidência IRRF” da SAFX2114 deve ser = 31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82 ou 83 

codRubr

Campo 09\-Código da Rubrica da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

ideTabRubr

Campo 08\-Código da Tabela da Rubrica da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

qtdRubr

Campo 10\-Quantidade de Referência da Rubrica da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

fatorRubr

Campo 11\-Fator de Cálculo da Rubrica da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

vrUnit

Campo 12\-Valor Unitário da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

vrRubr

Campo 13\-Valor Total da __SAFX248__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

__Registro infoPgtoParc__ – Informações dos pagamentos efetuados em valor menor que o apurado no demonstrativo 

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 o registro e todos os seus campos não serão gerados\.__

Este registro será gerado a partir das rubricas da __SAFX249__, quando se tratar de pagamento parcial\.

Trata\-se exatamente das rubricas que foram consideradas para gerar o campo “__vrLiq__” do registro “pai” \(registro __detPgtoFl__\), para os casos de pagamento parcial\.

A diferença é que neste registro serão consideradas *apenas* as rubricas referentes a descontos do IRRF e pensão alimentícia, conforme as orientações do manual de layout \(*mesmo procedimento feito para o registro retPgtoTot*\)\. 

Ou seja, serão consideradas apenas as rubricas que atendam a seguinte condição: 

            O campo “11\-Código Incidência IRRF” da SAFX2114 deve ser = 31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82 ou 83 

matricula

Este campo não será gerado

*\(*__*MFS18065*__*: Campo incluído na vrs 2\.4\.02\)*

*\(conforme mapeamento original, esta informação não se aplica aos autônomos\)*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

codRubr

Campo 10\-Código da Rubrica da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

ideTabRubr

Campo 09\-Código da Tabela da Rubrica da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

qtdRubr

Campo 12\-Quantidade de Referência da Rubrica da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

fatorRubr

Campo 13\-Fator de Cálculo da Rubrica da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

vrUnit

Campo 14\-Valor Unitário da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

vrRubr

Campo 15\-Valor Total da __SAFX249__

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

__Registro idePgtoExt__ – Informações de pagamentos efetuados a beneficiários do exterior 

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro e seus registros filhos só devem ser gerados até a versão 2\.5, a partir da versão S\-1\.0 o registro e todos os seus campos não serão gerados\.__

Este registro e seus registros “filhos” \(idePais e endExt\) serão gerados *apenas* quando o trabalhador for de outro país, ou seja, quando o campo __indResBr__ do registro __infoPgto__ = “N”\.

__Registro idePais__ – Identificação do país onde foi realizado o pagamento 

\(ver condição para a geração deste registro na especificação do registro __idePgtoExt__\)

As informações deste registro são informações de cadastro do trabalhador \(SAFX04\)\. A regra para recuperação dos dados da SAFX04 é a mesma já descrita para registros anteriores\.

 

CodPais

__MFS\-87306: Vrs\.S\-1\.0__

Código do país: campo “21\-Pais” da SAFX04 

Caso o campo País não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código do País \(CodPais\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “21\-País” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

indNIF

Campo “59\-Indicador do Nº de Identificação Fiscal” da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Indicativo do Número de Identificação Fiscal \(indNIF\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “59\-Indicador do Nº de Identificação Fiscal” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

nifBenef

Campo “53\-Número de Identificação Fiscal” da SAFX04

Caso este campo não esteja preenchido na SAFX04 e o conteúdo gerado para o campo indNIF seja = “1”, será gerada a seguinte mensagem de aviso no log de erros:

\(a geração deste campo é obrigatória apenas quando o indNIF for = 1\) 

*Erro: O campo Número de Identificação Fiscal – NIF \(nifBenef\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “53\-Número de Identificação Fiscal” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

__Registro endExt__ – Informações complementares do endereço do beneficiário 

\(ver condição para a geração deste registro na especificação do registro __idePgtoExt__\)

__MFS\-87306: Vrs\.S\-1\.0__

__Este registro e seus registros filhos só devem ser gerados até a versão 2\.5, a partir da versão S\-1\.0 o registro e todos os seus campos não serão gerados\.__

As informações deste registro são informações de cadastro do trabalhador \(SAFX04\)\. A regra para recuperação dos dados da SAFX04 é a mesma já descrita para registros anteriores\.

dscLograd

__MFS\-87306: Vrs\.S\-1\.0__

Campo “12\-Endereço” da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Descrição do Logradouro \(dscLograd\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “12\-Endereço” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

nrLograd

__MFS\-87306: Vrs\.S\-1\.0__

Campo “13\-Número do Endereço” da SAFX04

Caso este campo não esteja preenchido na SAFX04, o campo “nrLograd” não será gerado\.

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

Complem

__MFS\-87306: Vrs\.S\-1\.0__

Campo “14\-Complemento do Endereço” da SAFX04

Caso este campo não esteja preenchido na SAFX04, o campo “complem” não será gerado\.

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

Bairro

__MFS\-87306: Vrs\.S\-1\.0__

Campo “15\-Bairro” da SAFX04

Caso este campo não esteja preenchido na SAFX04, o campo “bairro” não será gerado\.

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

nmCid

__MFS\-87306: Vrs\.S\-1\.0__

Campo “16\-Município” da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Nome da Cidade \(nmCid\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “16\-Município” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

codPostal

__MFS\-87306: Vrs\.S\-1\.0__

Campo “20\-CEP” da SAFX04 

Caso este campo não esteja preenchido na SAFX04, o campo “codPostal” não será gerado\.

__Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.__

= = = = = = 

