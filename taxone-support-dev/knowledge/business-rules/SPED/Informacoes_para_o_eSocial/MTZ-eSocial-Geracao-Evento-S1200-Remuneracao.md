# MTZ-eSocial-Geracao-Evento-S1200-Remuneracao

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1200-Remuneracao.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 99 KB

---

THOMSON REUTERS

Módulo eSocial

Geração Evento S\-1200

\(Remuneração de trabalhador vinculado ao Regime Geral de Previd\. Social\) 

__Localização__: Menu SPED, módulo Informações para o eSocial, menu Geração 🡪 Geração dos Movimentos 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS15870__

Geração do evento S\-1200

Geração dos dados do evento S\-1200 \(Remuneração de trabalhador vinculado ao Regime Geral de Previd\. Social\)

20/12/2017 

\(criação do documento\)

__MFS18065__

Atualizações da versão 2\.4\.02

\-Excluídos os campos codCBO, natAtividade e qtdDiasTrab do “infoComplem”;

\-Geração do novo registro “infoComplCont” \(filho do dmDev\); 

07/06/2018

__MFS16751__

Controle Status x Regeração

Críticas em relação a regeração dos eventos\. 

27/03/2018

__MFS19608__

Lara Aline

Ajuste na geração do campo codCBO a origem passa a ser pela SAFX247\.

11/07/2018

<a id="_Hlk523235881"></a>__MFS16762__

Lara Aline

Inclusão rotina de Reprocessar Evento

28/08/2018

__MFS22087__

Lara Aline

Ajuste na geração do campo codLotacao a origem passa a ser pela SAFX247, caso não preenchido recuperamos da SAFX04 como padrão\.

07/11/2018

__MFS28553__

EDUARDO CRUZ

__Informações para o eSocial \- Evento S\-1200 não deve gerar rubricas \(tag itensremun\) onde no evento S\-1010 a mesma seja codIncIRRF a \[31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83\]__

__10/07/2019__

__MFS60476__

Rogério Ohashi

Ajuste na regra de geração do Campo__ “__cpfTrab” para considerar o Campo CPF\_SP__ __da tabela X04\_PESSOA\_FIS\_JUR __preenchido__, __E__ __quando__ o Campo 27 \- Classe de Empresa” __for Igual__ a "05 – MEI \(Micro Empreendedor Individual\)\. Tratamento para atender os eventos S\-1200 e S\-1210 para fornecedores autônomos MEI\. \(Estavam sendo desconsiderados por estarem cadastrados pelo CNPJ\)\.

__25/03/2021__

__MFS\-87292__

Elisabete Costa

Alterações Versão S\-1\.0

03/06/2022

__MFS\-96008__

Elisabete Costa

Retirada do Módulo: Informações para o E\-Social do T1

04/11/2022

Sumário

[1\.	Parâmetros da Tela	2](#_Toc517780633)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc517780634)

[3\.	Verificação do Status de Eventos já Gerados	4](#_Toc517780635)

[4\.	Gravação dos Dados	6](#_Toc517780636)

__Devido ao end\-of\-support da mensageria OS E\-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E\-Social será retirado do TAX ONE e deverá permanecer no DW\.__

# <a id="_Toc517780633"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1200\.

A geração dos dados do S\-1200 é feita apenas para os trabalhadores autônomos, cujas informações são carregadas para as tabelas SAFX247/248/249/250\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\-eSocial\-Geracao\-Movimentos*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc517780634"></a>Recuperação dos Dados e Processamento

Origem dos dados: \- Parametrização “Dados Iniciais” do Módulo eSocial;

                               \- SAFX247 \- Demonstrativo de Pagamento dos Autônomos;

                               \- SAFX248 \- Demonstrativo de Pagamento dos Autônomos \(Rubricas\);

                               \- SAFX250 \- Demonstrativo de Pagamento dos Autônomos \(Outros Vínculos do Trabalhador\);

                               \- SAFX04/2037/2058/2059 \(Cadastro de Pessoas Fis/Jur, Setor e Processos Administrativo/Judicial\);

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

     \- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos demonstrativos de pagamento na __SAFX247__:

     \- __Empresa__ – empresa do estabelecimento centralizador selecionado;

     \- __Estabelecimento__ – Serão recuperados os demonstrativos de todos os estabelecimentos envolvidos na centralização \(o estabelecimento

       centralizador, que é o selecionado em tela, e os centralizados\), de acordo com a parametrização das obrigações federais do módulo

       Parâmetros \(menu Preliminares > Centralização da Escrituração de Obrigações Federais\);

     \- __Ano Competência__ – ano do período informado na tela da geração \(campo “Período”\);

     \- __Mês Competência__ – mês do período informado na tela da geração \(campo “Período”\);

Critérios para a recuperação das rubricas do demonstrativo\(__SAFX248__\) e dos outros vínculos do trabalhador \(__SAFX250__\):

     Para cada demonstrativo recuperado da __SAFX247__, serão recuperadas as informações das rubricas do demonstrativo, e dos outros vínculos do 

     trabalhador no período de competência do demonstrativo\. 

     Estas informações serão recuperadas das tabelas SAFX248 e SAFX250 \(tabelas “filhas” da SAFX247\), a partir dos seguintes critérios: 

Empresa =

Campo “Empresa” do demonstrativo

Estabelecimento =

Campo “Estabelecimento” do demonstrativo

Ano Competência =

Campo “Ano Competência” do demonstrativo

Mês Competência =

Campo “Mês Competência” do demonstrativo

Indicador Pessoa Fis/Jur =

Campo “Indicador Pessoa Fis/Jur” do demonstrativo

Código Pessoa Fis/Jur =

Campo “Código Pessoa Fis/Jur” do demonstrativo

Identificador do Demonstrativo de Pagamento =

Campo “Identificador do Demonstrativo de Pagamento” do demonstrativo

__Conceito do evento S\-1200 x Tabela dos Demonstrativos \(SAFX247\)__:

 __Para cada trabalhador será gerado um único evento S\-1200 no período de competência__, contemplando todos os demonstrativos que possam existir no período\.

Normalmente, no caso de autônomos teremos um único demonstrativo para cada período de competência \(ou seja, a cada período, existirá uma única linha na SAFX247 para cada trabalhador\)\.

No entanto, pode acontecer de existir mais de um demonstrativo do mesmo trabalhador para um mesmo período de competência \(tanto as tabelas envolvidas, como a geração do evento S\-1200 estão preparados para este cenário\)\.

*Exemplo: No caso de um trabalhador com dois demonstrativos para um determinado mês, teríamos dois registros na SAFX247 de mesmo período e trabalhador, mas diferenciados pelo campo 07\-Identificador do Demonstrativo de Pagamento \(ou seja, mesmos campos chave, exceto pelo campo 07 que seria diferente\)\.*

Observar que a chave da Tabela dos Demonstrativos \(SAFX247\) é:

__       \[ Empresa \+ Estabelecimento \+ Ano Competência \+ Mês Competência \+ Trabalhador \(Indicador e Código da Pessoa Fis/Jur\) \+ Identificador do Demonstrativo de Pagamento \]__

Assim, o campo da SAFX247 que identifica o demonstrativo é o 07\-Identificador do Demonstrativo de Pagamento\. No caso de um trabalhador com mais de um demonstrativo para um mesmo período de competência, os demonstrativos serão diferenciados por  este campo\.

O registro do evento S\-1200 que contém os dados de cada demonstrativo separadamente é o registro __dmDev__ e seus registros “filhos”\. Assim, no __dmDev__ serão geradas as informações de cada demonstrativo existente para o trabalhador no período\. 

# <a id="_Toc509582647"></a><a id="_Toc509925718"></a><a id="_Toc509929675"></a><a id="_Toc517780635"></a>Verificação do Status de Eventos já Gerados

__MFS16750__: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente\. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1200\_OC, coluna IND\_STATUS\)\.

Para cada trabalhador a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este trabalhador no mesmo período de competência\.

__Caso não:__ 

      O evento do trabalhador será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

      A geração de um novo evento para o trabalhador dependerá do status do evento já existente, da seguinte forma:

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

             Nesse caso, o trabalhador em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:

*                  Aviso: Já existe evento anterior gerado para o trabalhador\. O status do evento não permite uma nova geração\.*

*                  Dados do Registro:  Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX, *__*Período*__*: XX/XXXX *

         Se o status do evento já existente __permitir regeração__:

             Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação __ORIGINAL__ ou uma

             __RETIFICAÇÃO__, dependendo do status do evento original, como descrito a seguir:

              \- Se status do evento original = 8 ou = 9 🡪 Nesse caso, o novo evento será gerado como __RETIFICAÇÃO__;

              \- Se status do evento original <> 8 e <> 9 🡪 Nesse caso, o novo evento será gerado como __ORIGINAL__;

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

<a id="_Hlk523235760"></a>__\[MFS16762\]__

<a id="_Hlk523155984"></a>__Importante:__ Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação \(Critérios estão no documento de tela do Painel de Controle de Eventos\) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\. 

# <a id="_Toc517780636"></a>Gravação dos Dados

Conforme descrito acima \(“*Conceito do evento S\-1200 x Tabela dos Demonstrativos \(SAFX247\)*”\), será gerado um evento S\-1200 __para cada trabalhador__, com as seguintes informações: 

*\(os registros não citados não serão gerados\)*

__Registro evtRemun__ – Evento Remuneração do Trabalhador

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

__Se__ for a primeira geração do evento do trabalhador no período:

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

 

indApuracao

Conteúdo fixo = “1” \(= Mensal\)

*\(como os autônomos não têm décimo terceiro salário, este campo será gerado sempre como “1”\)*

perApur

Mês e ano do período informado na tela da geração, no formato AAAA\-MM \(conforme orientação do layout\)

indGuia

__MFS\-87292__:__Vrs S\-1\.0__

A partir da versão S\-1\.0 foi criado o campo indGuia\. __O mesmo não deve ser gerado,__ pois é destinado a ser informado apenas por empregadores pessoas físicas e usado apenas para o recolhimento unificado dos tributos e do FGTS pelos empregadores __domésticos__\.

tpAmb

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

procEmi

Conteúdo fixo = “1” \(= Aplicativo do empregador\)

verProc 

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\.\. 

*Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideEmpregador__ \- Informações de identificação do empregador\.

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita;

__Registro ideTrabalhador__ \- Informações de identificação do trabalhador\.

As informações do trabalhador serão recuperadas no seu cadastro na __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da SAFX247\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

cpfTrab

\[__ALTERAÇÃO\- MFS60476__\] Tratamento para fornecedores autônomos MEI\.

Caso existir informação no campo CPF\_SP da tabela X04\_PESSOA\_FIS\_JUR, __E se__ o Campo IND\_CLASSE\_EMP \(Campo 27 \- Classe de Empresa\) da tabela X04\_PESSOA\_FIS\_JUR __for__ __igual__ a "05 – MEI \(Micro Empreendedor Individual\)", gerar o campo com a informação do campo CPF\_SP, caso contrário seguir com a regra original:

Campo 06\-CPF\-CGC da SAFX04

Como se trata de autônomos, a pessoa fis/jur deve ser uma pessoa física\. Por isso, será verificado o conteúdo do campo “06\-CPF\-CGC” da pessoa fis/jur recuperada da SAFX04\. Se o conteúdo deste campo for um CNPJ, será gravada a mensagem abaixo no log, e o campo cpfTrab não será gerado\.

*Erro: O campo Número do CPF do Trabalhador \(cpfTrab\) deve ser um CPF\. A informação não será gerada no evento\.*

*Origem: Campo “06\-CPF\-CGC” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

nisTrab

__MFS\-87292__:vrs S\-1\.0

Campo 35\-Número do PIS/PASEP da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Número de Identificação Social – NIS \(nisTrab\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “35\-Número do PIS/PASEP” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.

__Registro infoMV__ \- Informações referentes à outros vínculos do trabalhador

	

Este registro, e também o registro __remunOutrEmpr__, serão gerados apenas quando o trabalhador tiver outros vínculos / atividades para definição do limite do salário de contribuição\. Para isso será verificado o preenchimento do campo “*08\-Indicador de Desconto da Contribuição Previdenciária*” da SAFX247, da seguinte forma:

Se campo “*08\-Indicador de Desconto da Contribuição Previdenciária*” não preenchido, os registros __infoMV__ e __remunOutrEmpr__ não serão gerados\.

Caso contrário, o registro infoMV será gerado com a seguinte informação: 

indMV

Campo 08\-Indicador de Desconto da Contribuição Previdenciária \(SAFX247\)

__*Obs*__*: Quando existir mais de um demonstrativo para o trabalhador, basta que o campo esteja preenchido em qualquer um dos demonstrativos\. E nesse caso, pode\-se considerar o conteúdo do campo 08 de qualquer um dos demonstrativos \(conceitualmente basta que os outros vínculos sejam cadastrados para um dos demonstrativos\)\.*

__Registro remunOutrEmpr__ – Informações referentes à outros vínculos do trabalhador

Como descrito acima para o registro __infoMV__, este registro será gerado apenas quando o campo “*08\-Indicador de Desconto da Contribuição Previdenciária*” estiver preenchido\.

<a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>Para sua geração, serão recuperadas as informações dos outros vínculos cadastrados para o trabalhador no período de competência \(SAFX250\), de acordo com as regras da recuperação dos dados descrita no item “2\-Recuperação dos Dados e Processamento”\.

Poderão existir vários registros de outros vínculos, e para cada registro recuperado, será gerado um registro __remunOutrEmpr__, com as informações descritas abaixo:

__*Obs*__*: Quando existir mais de um demonstrativo para o trabalhador, a pesquisa dos outros vínculos será feita para todos os demonstrativos do trabalhador, e para cada registro de outros vínculos será gerado um registro *__*remunOutrEmpr*__*, mas, desconsiderando os vínculos duplicados que o usuário possa ter incluído\. Ou seja, se de todos os outros vínculos recuperados, existirem vínculos de mesmo CNPJ/CPF, será gerado apenas um registro *__*remunOutrEmpr*__*\.*

tpInsc

Se conteúdo do campo “08\-CNPJ/CPF do Empregador” \(SAFX250\) for um CNPJ \(14 dígitos\),

      Gravar “1”;

Se conteúdo do campo “08\-CNPJ/CPF do Empregador” \(SAFX250\) for um CPF \(11 dígitos\),

      Gravar “2”;

nrInsc

Campo 08\-CNPJ/CPF do Empregador \(SAFX250\)

codCateg

Campo 09\-Código da Categoria do Trabalhador \(SAFX250\)

vlrRemunOE

Campo 10\-Valor Remuneração \(SAFX250\)

<a id="_Hlk516146668"></a>__Registro infoComplem__ – Informações de identificação do trabalhador

Assim como as informações do registro __ideTrabalhador__, as informações deste registro também são originadas do registro do trabalhador autônomo na __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da SAFX247\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

nmTrab

Campo 05\-Razão Social da SAFX04 

dtNascto

Campo 45\-Data de Nascimento da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Data de Nascimento \(dtNascto\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “45\-Data de Nascimento” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

codCBO

__MFS\-18065__: Campo excluído na vrs 2\.4\.02;

Campo 34\-CBO da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Classificação Brasileira de Ocupação \- CBO \(codCBO\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “34\-CBO” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

NatAtividade

__MFS\-18065__: Campo excluído na vrs 2\.4\.02;

Campo 67\-Natureza da Atividade da SAFX04

Caso este campo não esteja preenchido na SAFX04, este campo não será gerado\.

qtdDiasTrab

__MFS\-18065__: Campo excluído na vrs 2\.4\.02;

Este campo não será gerado

*\(conforme mapeamento original, esta informação não se aplica aos autônomos\) *

__Registro procJudTrab__ \- Informações sobre a existência de processos do trabalhador

As informações de processos do trabalhador serão recuperadas da tabela das rubricas do demonstrativo \(__SAFX248\)\. __

Para isso, será verificada a existência de processo em cada uma das rubricas do demonstrativo em questão\.

*\(ver critérios sobre a recuperação das rubricas do demonstrativo no item “2\-Recuperação dos Dados e Processamento”\)*

O processo é informado nos seguintes campos da tabela das rubricas \(SAFX248\):

   14\-Indicador do Tipo de Processo

   15\-Número do Processo

   16\-Código do Indicativo da Suspensão

__  __

Poderão existir vários processos \(de várias rubricas\), e para cada um deles será gerado um registro __procJudTrab__, com as seguintes informações:

tpTrib

__MFS\-87292__:Vrs S\-1\.0

Campo 12\-Abrangência do Processo da SAFX2058 \(Tabela de Cadastro dos Processos\)

Este campo é gerado com a informação da abrangência da decisão referente ao processo\. Para obter esta informação, será feita a recuperação dos dados cadastrais do processo na Tabela de Processos \(SAFX2058\), a partir dos campos “14\-Indicador do Tipo de Processo” e “15\-Número do Processo” da rubrica \(SAFX248\)\.

Até a versão 2\.5\.0\. os valores válidos são:

1, 2, 3, 4

A partir da versão S\-1\.0, os valores válidos são:

1, 2\.

Caso este campo não esteja preenchido na SAFX2058 para o processo em questão, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Abrangência da Decisão \(tpTrib\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “12\-Abrangência do Processo” da Tabela de Processo Administrativo/Judicial \(SAFX2058\)*

*Dados do Registro: Tipo do Processo: X, Número do Processo: XXXXXXXXXXXXXXXXXXX*

nrProcJud

Campo 15\-Número do Processo da SAFX248

codSusp

Campo 16\-Código do Indicativo da Suspensão da SAFX248

__Registro dmDev__ \- Informações de cada demonstrativo de pagamento do trabalhador

A informação da categoria do trabalhador \(campo codCateg\) será recuperada do cadastro da __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da SAFX247 \(da mesma forma que algumas informações dos registros __ideTrabalhador, infoComplem __e__  ideEstabLot__\)\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

ideDmDev

Campo 07\-Identificador do Demonstrativo de Pagamento da SAFX247

codCateg

Campo 66\-Código da Categoria do Trabalhador da SAFX04

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código da Categoria do Trabalhador \(codCateg\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “66\-Código da Categoria do Trabalhador” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

<a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK28"></a>__Registro ideEstabLot__ – Identificação da lotação

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>A informação da lotação do trabalhador \(campo __codLotacao__\) será recuperada do cadastro da __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da SAFX247 \(da mesma forma que algumas informações dos registros __ideTrabalhador, infoComplem __e__ dmDev__\)\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será <a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

Os campos __tpInsc__ e __nrInsc__ são gerados a partir da Tabelas de Setores \(SAFX2037\), __ou__, a partir do próprio CNPJ do estabelecimento, conforme regra descrito abaixo\. 

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>

tpInsc

__MFS\-87292__:Vrs S\-1\.0

<a id="OLE_LINK5"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>A geração deste campo depende do conteúdo do campo “<a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>*07\-Tipo de Inscrição da Lotação*” da SAFX2037 \(Tabela de Cadastro dos Setores\)\.

Para obter a informação na Tabela de Setores \(SAFX2037\), será feita a recuperação dos dados a partir do campo “__68\-Setor__” do cadastro do trabalhador \(SAFX04\)\. Havendo mais de um registro do Setor na SAFX2037, será considerado o de > data de validade cujo mês/ano seja <= <a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>ao mês/ano do período informado na tela da geração\. Além disso, a validade final do Setor, quando preenchida, deve ser de um mês/ano >= ao mês/ano do período\.

Até a versão 2\.5\.0\. os valores válidos são:

1, 2, 3, 4

A partir da versão S\-1\.0, os valores válidos são:

1, 3, 4,

Recuperada a informação do Setor \(SAFX2037\), a regra da geração do campo é a seguinte:

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>Se o campo <a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>“*07\-Tipo de Inscrição da Lotação*” da SAFX2037 estiver preenchido,

      O campo será gravado com o conteúdo do campo “*07\-Tipo de Inscrição da Lotação*” da SAFX2037;

Senão,

       O campo será gravado com “1”;

nrInsc

Para a geração deste campo, vale a mesma regra descrita para o campo anterior, mas considerando o campo “*08\-Número de Inscrição da Lotação*” da SAFX2037 \(Tabela de Cadastro dos Setores\):

Se o campo “*08\-Número de Inscrição da Lotação*” da SAFX2037 estiver preenchido,

      O campo será gravado com o conteúdo do campo “*08\-Número de Inscrição da Lotação*” da SAFX2037;

Senão,

       O campo será gravado com o CNPJ do estabelecimento do demonstrativo \(ou seja, da SAFX247\)\. Neste caso

       será gravado o CNPJ completo, com os 14 dígitos;

codLotacao

__\[MFS22087\]__

Campo 13\-Setor da __SAFX247__

Caso este campo não esteja preenchido na SAFX247, será verificada se a informação está preenchida no Campo 68\-Setor da __SAFX04__

Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código da Lotação Tributária \(codLotacao\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “13\-Setor” do Demonstrativo de Pagamento dos Autônomos \(SAFX247\) ou Campo “68\-Setor” da Tabela de Cadastro de Pessoas Fis/Jur \(SAFX04\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX*

qtdDiasAv

Este campo não será gerado

*\(conforme mapeamento original, esta informação não se aplica aos autônomos\)*

<a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a>__Registro remunPerApur__ – Remuneração do Trabalhador no Período da Apuração

As informações deste registro não serão geradas, mas sua tag será gerada porque existem os registros “filhos” a serem gerados\. 

*\(conforme o mapeamento original, as informações do remunPerApur não se aplicam a autônomos\)  *

<a id="OLE_LINK37"></a><a id="OLE_LINK38"></a><a id="OLE_LINK39"></a>__Registro itensRemun__ – Detalhamento das Rubricas do Demonstrativo de Pagamento

Este registro é gerado a partir das rubricas do demonstrativo \(SAFX247\) em questão, recuperadas da Tabela das Rubricas do Demonstrativo \(SAFX248\)\.

__\[MFS\-28553\]__

Não pode ser utilizada rubrica: 

O campo “11\-Código Incidência IRRF” da SAFX2114 deve ser diferente \[31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83\] 

Para cada rubrica, será gerado um registro itensRemun, com as seguintes informações:

codRubr

Campo 09\-Código da Rubrica da SAFX248

ideTabRubr

Campo 08\-Código da Tabela da Rubrica da SAFX248

qtdRubr

Campo 10\-Quantidade de Referência da Rubrica da SAFX248

fatorRubr

Campo 11\-Fator de Cálculo da Rubrica da SAFX248

vrUnit

__MFS\-87292__:Vrs S\-1\.0

Campo 12\-Valor Unitário da SAFX248

Este campo só deve ser gerado até a versão 2\.5, a partir da versão S\-1\.0 ele não deve ser gerado\.

vrRubr

Campo 13\-Valor Total da SAFX248

indApurIR

__MFS\-87292__:Vrs S\-1\.0

Campo 14\-Tipo de apuração de IR

A partir da versão S\-1\.0, os valores válidos são:

0, 1\.

Este campo só deve ser gerado a partir da versão S\-1\.0\. 

Como regra, o campo \{indApurIR\} deve ser preenchido com __\[0\]:__ com esse indicativo a rubrica é considerada para apuração do IR a partir dos dados informados no eSocial \(S\-1200, S\-1202, S\-1207, S\-2299 ou S\-2399\), cabendo o envio do R\-4004 na EFD\-Reinf para iniciar a apuração e enviar as informações complementares solicitadas pela DIRF\.

Excepcionalmente, podem haver situações \(por exemplo, RRA\) em que para ocorrer a correta apuração do IR com base nas informações do eSocial o declarante precisa elaborar uma estrutura complexa neste evento\. Para evitar isso, ele pode optar por enviar os valores no grupo \[itensRemun\] 93 indicando \{indApurIR\}=__\[1\] __e, nesse caso o IR não é apurado com base no eSocial e esses valores devem ser informados no R\-4010 da EFD\-Reinf direto no formato tradicional da DIRF\.

__Registro infoComplCont__ – Informações complementares contratuais do trabalhador                  \(criado na versão 2\.4\.02, __MFS18065__\)

*Observação sobre a alteração da versão 2\.4\.02:*

*Os campos deste registro eram originalmente gerados no registro “infoComplem” \(filho do “ideTrabalhador”\)\. Na versão 2\.4\.02 eles foram “transferidos“ para este novo registro “infoComplCont”\. Como o novo registro é filho do “dmDev”, pressupõe\-se que possam existir trabalhadores que tenham mais de um demonstrativo no período, sendo cada um deles de uma atividade diferente\. Desta forma, o mais lógico seria que estas informações fossem criadas na tabela do demonstrativo \(SAFX247\), no entanto, como a geração do eSocial é restrita aos autônomos, continuaremos a utilizar os dados da SAFX04\. Futuramente, se for necessário, podemos incluir estes dados junto ao demonstrativo \(SAFX247\)\.*

Assim como as informações do registro __ideTrabalhador__ e __infoComplem__, as informações deste registro também são originadas do registro do trabalhador autônomo na __SAFX04__, através dos campos “05\-Indicador da Pessoa Fis/Jur” e “06\-Código da Pessoa Fis/Jur” da __SAFX247__\.

Havendo mais de um registro da pessoa fis/jur na __SAFX04__, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

codCBO

__\[MFS19608\]__

Campo 12\-CBO da SAFX247

Caso este campo não esteja preenchido na SAFX247, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Classificação Brasileira de Ocupação \- CBO \(codCBO\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “12\-CBO” da Tabela Demonstrativo de Pagamento dos Autônomos \(SAFX247\)*

*Dados do Registro: Pessoa Fis/Jur \(Ind/Cód\): X / XXXXXXXXXXXXXXXXX    Estab: XXXXXXXX*

natAtividade

Campo 67\-Natureza da Atividade da SAFX04

Caso este campo não esteja preenchido na SAFX04, este campo não será gerado\.

qtdDiasTrab

Este campo não será gerado

*\(conforme mapeamento original, esta informação não se aplica aos autônomos\)*

= = = = = = 

