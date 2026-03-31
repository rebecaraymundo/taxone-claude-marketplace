# MTZ-eSocial-Geracao-Evento-S1200-Remuneracao

> Fonte: MTZ-eSocial-Geracao-Evento-S1200-Remuneracao.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1200

(Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social)


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Movimentos



DOCUMENTO DE REQUISITO

























Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	4
4.	Gravação dos Dados	6




Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.

















## Parâmetros da Tela


Este documento é específico das regras de geração do evento S-1200.

A geração dos dados do S-1200 é feita apenas para os trabalhadores autônomos, cujas informações são carregadas para as tabelas SAFX247/248/249/250.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Movimentos”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento


Origem dos dados: - Parametrização “Dados Iniciais” do Módulo eSocial;
- SAFX247 - Demonstrativo de Pagamento dos Autônomos;
- SAFX248 - Demonstrativo de Pagamento dos Autônomos (Rubricas);
- SAFX250 - Demonstrativo de Pagamento dos Autônomos (Outros Vínculos do Trabalhador);
- SAFX04/2037/2058/2059 (Cadastro de Pessoas Fis/Jur, Setor e Processos Administrativo/Judicial);

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos demonstrativos de pagamento na SAFX247:

- Empresa – empresa do estabelecimento centralizador selecionado;
- Estabelecimento – Serão recuperados os demonstrativos de todos os estabelecimentos envolvidos na centralização (o estabelecimento
centralizador, que é o selecionado em tela, e os centralizados), de acordo com a parametrização das obrigações federais do módulo
Parâmetros (menu Preliminares > Centralização da Escrituração de Obrigações Federais);
- Ano Competência – ano do período informado na tela da geração (campo “Período”);
- Mês Competência – mês do período informado na tela da geração (campo “Período”);


Critérios para a recuperação das rubricas do demonstrativo(SAFX248) e dos outros vínculos do trabalhador (SAFX250):

Para cada demonstrativo recuperado da SAFX247, serão recuperadas as informações das rubricas do demonstrativo, e dos outros vínculos do
trabalhador no período de competência do demonstrativo.

Estas informações serão recuperadas das tabelas SAFX248 e SAFX250 (tabelas “filhas” da SAFX247), a partir dos seguintes critérios:




Conceito do evento S-1200 x Tabela dos Demonstrativos (SAFX247):


Para cada trabalhador será gerado um único evento S-1200 no período de competência, contemplando todos os demonstrativos que possam existir no período.

Normalmente, no caso de autônomos teremos um único demonstrativo para cada período de competência (ou seja, a cada período, existirá uma única linha na SAFX247 para cada trabalhador).

No entanto, pode acontecer de existir mais de um demonstrativo do mesmo trabalhador para um mesmo período de competência (tanto as tabelas envolvidas, como a geração do evento S-1200 estão preparados para este cenário).

Exemplo: No caso de um trabalhador com dois demonstrativos para um determinado mês, teríamos dois registros na SAFX247 de mesmo período e trabalhador, mas diferenciados pelo campo 07-Identificador do Demonstrativo de Pagamento (ou seja, mesmos campos chave, exceto pelo campo 07 que seria diferente).

Observar que a chave da Tabela dos Demonstrativos (SAFX247) é:

[ Empresa + Estabelecimento + Ano Competência + Mês Competência + Trabalhador (Indicador e Código da Pessoa Fis/Jur) + Identificador do Demonstrativo de Pagamento ]

Assim, o campo da SAFX247 que identifica o demonstrativo é o 07-Identificador do Demonstrativo de Pagamento. No caso de um trabalhador com mais de um demonstrativo para um mesmo período de competência, os demonstrativos serão diferenciados por  este campo.

O registro do evento S-1200 que contém os dados de cada demonstrativo separadamente é o registro dmDev e seus registros “filhos”. Assim, no dmDev serão geradas as informações de cada demonstrativo existente para o trabalhador no período.


## Verificação do Status de Eventos já Gerados


MFS16750: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1200_OC, coluna IND_STATUS).

Para cada trabalhador a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este trabalhador no mesmo período de competência.

Caso não:

O evento do trabalhador será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:

A geração de um novo evento para o trabalhador dependerá do status do evento já existente, da seguinte forma:



Se o status do evento já existente não permitir regeração:

Nesse caso, o trabalhador em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:
Aviso: Já existe evento anterior gerado para o trabalhador. O status do evento não permite uma nova geração.
Dados do Registro:  Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX, Período: XX/XXXX

Se o status do evento já existente permitir regeração:

Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação ORIGINAL ou uma
RETIFICAÇÃO, dependendo do status do evento original, como descrito a seguir:

- Se status do evento original = 8 ou = 9  Nesse caso, o novo evento será gerado como RETIFICAÇÃO;
- Se status do evento original <> 8 e <> 9  Nesse caso, o novo evento será gerado como ORIGINAL;




[MFS16762]
Importante: Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação (Critérios estão no documento de tela do Painel de Controle de Eventos) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.



## Gravação dos Dados


Conforme descrito acima (“Conceito do evento S-1200 x Tabela dos Demonstrativos (SAFX247)”), será gerado um evento S-1200 para cada trabalhador, com as seguintes informações:

(os registros não citados não serão gerados)



Registro evtRemun – Evento Remuneração do Trabalhador



Registro ideEvento - Informações de Identificação do evento.





Registro ideEmpregador - Informações de identificação do empregador.



Registro ideTrabalhador - Informações de identificação do trabalhador.

As informações do trabalhador serão recuperadas no seu cadastro na SAFX04, através dos campos “05-Indicador da Pessoa Fis/Jur” e “06-Código da Pessoa Fis/Jur” da SAFX247.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.



Registro infoMV - Informações referentes à outros vínculos do trabalhador

Este registro, e também o registro remunOutrEmpr, serão gerados apenas quando o trabalhador tiver outros vínculos / atividades para definição do limite do salário de contribuição. Para isso será verificado o preenchimento do campo “08-Indicador de Desconto da Contribuição Previdenciária” da SAFX247, da seguinte forma:

Se campo “08-Indicador de Desconto da Contribuição Previdenciária” não preenchido, os registros infoMV e remunOutrEmpr não serão gerados.

Caso contrário, o registro infoMV será gerado com a seguinte informação:



Obs: Quando existir mais de um demonstrativo para o trabalhador, basta que o campo esteja preenchido em qualquer um dos demonstrativos. E nesse caso, pode-se considerar o conteúdo do campo 08 de qualquer um dos demonstrativos (conceitualmente basta que os outros vínculos sejam cadastrados para um dos demonstrativos).




Registro remunOutrEmpr – Informações referentes à outros vínculos do trabalhador

Como descrito acima para o registro infoMV, este registro será gerado apenas quando o campo “08-Indicador de Desconto da Contribuição Previdenciária” estiver preenchido.

Para sua geração, serão recuperadas as informações dos outros vínculos cadastrados para o trabalhador no período de competência (SAFX250), de acordo com as regras da recuperação dos dados descrita no item “2-Recuperação dos Dados e Processamento”.

Poderão existir vários registros de outros vínculos, e para cada registro recuperado, será gerado um registro remunOutrEmpr, com as informações descritas abaixo:


Obs: Quando existir mais de um demonstrativo para o trabalhador, a pesquisa dos outros vínculos será feita para todos os demonstrativos do trabalhador, e para cada registro de outros vínculos será gerado um registro remunOutrEmpr, mas, desconsiderando os vínculos duplicados que o usuário possa ter incluído. Ou seja, se de todos os outros vínculos recuperados, existirem vínculos de mesmo CNPJ/CPF, será gerado apenas um registro remunOutrEmpr.






Registro infoComplem – Informações de identificação do trabalhador

Assim como as informações do registro ideTrabalhador, as informações deste registro também são originadas do registro do trabalhador autônomo na SAFX04, através dos campos “05-Indicador da Pessoa Fis/Jur” e “06-Código da Pessoa Fis/Jur” da SAFX247.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.

Registro procJudTrab - Informações sobre a existência de processos do trabalhador

As informações de processos do trabalhador serão recuperadas da tabela das rubricas do demonstrativo (SAFX248).

Para isso, será verificada a existência de processo em cada uma das rubricas do demonstrativo em questão.

(ver critérios sobre a recuperação das rubricas do demonstrativo no item “2-Recuperação dos Dados e Processamento”)

O processo é informado nos seguintes campos da tabela das rubricas (SAFX248):

14-Indicador do Tipo de Processo
15-Número do Processo
16-Código do Indicativo da Suspensão

Poderão existir vários processos (de várias rubricas), e para cada um deles será gerado um registro procJudTrab, com as seguintes informações:



Registro dmDev - Informações de cada demonstrativo de pagamento do trabalhador

A informação da categoria do trabalhador (campo codCateg) será recuperada do cadastro da SAFX04, através dos campos “05-Indicador da Pessoa Fis/Jur” e “06-Código da Pessoa Fis/Jur” da SAFX247 (da mesma forma que algumas informações dos registros ideTrabalhador, infoComplem e  ideEstabLot).

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.



Registro ideEstabLot – Identificação da lotação

A informação da lotação do trabalhador (campo codLotacao) será recuperada do cadastro da SAFX04, através dos campos “05-Indicador da Pessoa Fis/Jur” e “06-Código da Pessoa Fis/Jur” da SAFX247 (da mesma forma que algumas informações dos registros ideTrabalhador, infoComplem e dmDev).

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.

Os campos tpInsc e nrInsc são gerados a partir da Tabelas de Setores (SAFX2037), ou, a partir do próprio CNPJ do estabelecimento, conforme regra descrito abaixo.



Registro remunPerApur – Remuneração do Trabalhador no Período da Apuração

As informações deste registro não serão geradas, mas sua tag será gerada porque existem os registros “filhos” a serem gerados.
(conforme o mapeamento original, as informações do remunPerApur não se aplicam a autônomos)


Registro itensRemun – Detalhamento das Rubricas do Demonstrativo de Pagamento

Este registro é gerado a partir das rubricas do demonstrativo (SAFX247) em questão, recuperadas da Tabela das Rubricas do Demonstrativo (SAFX248).

[MFS-28553]
Não pode ser utilizada rubrica:
O campo “11-Código Incidência IRRF” da SAFX2114 deve ser diferente [31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83]

Para cada rubrica, será gerado um registro itensRemun, com as seguintes informações:


Registro infoComplCont – Informações complementares contratuais do trabalhador                  (criado na versão 2.4.02, MFS18065)


Assim como as informações do registro ideTrabalhador e infoComplem, as informações deste registro também são originadas do registro do trabalhador autônomo na SAFX04, através dos campos “05-Indicador da Pessoa Fis/Jur” e “06-Código da Pessoa Fis/Jur” da SAFX247.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.
= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15870 | Geração do evento S-1200 | Geração dos dados do evento S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social) | 20/12/2017  (criação do documento) |
| MFS18065 | Atualizações da versão 2.4.02 | -Excluídos os campos codCBO, natAtividade e qtdDiasTrab do “infoComplem”; -Geração do novo registro “infoComplCont” (filho do dmDev); | 07/06/2018 |
| MFS16751 | Controle Status x Regeração | Críticas em relação a regeração dos eventos. | 27/03/2018 |
| MFS19608 | Lara Aline | Ajuste na geração do campo codCBO a origem passa a ser pela SAFX247. | 11/07/2018 |
| MFS16762 | Lara Aline | Inclusão rotina de Reprocessar Evento | 28/08/2018 |
| MFS22087 | Lara Aline | Ajuste na geração do campo codLotacao a origem passa a ser pela SAFX247, caso não preenchido recuperamos da SAFX04 como padrão. | 07/11/2018 |
| MFS28553 | EDUARDO CRUZ | Informações para o eSocial - Evento S-1200 não deve gerar rubricas (tag itensremun) onde no evento S-1010 a mesma seja codIncIRRF a [31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83] | 10/07/2019 |
| MFS60476 | Rogério Ohashi | Ajuste na regra de geração do Campo “cpfTrab” para considerar o Campo CPF_SP da tabela X04_PESSOA_FIS_JUR preenchido, E quando o Campo 27 - Classe de Empresa” for Igual a "05 – MEI (Micro Empreendedor Individual). Tratamento para atender os eventos S-1200 e S-1210 para fornecedores autônomos MEI. (Estavam sendo desconsiderados por estarem cadastrados pelo CNPJ). | 25/03/2021 |
| MFS-87292 | Elisabete Costa | Alterações Versão S-1.0 | 03/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Empresa = | Campo “Empresa” do demonstrativo |
| --- | --- |
| Estabelecimento = | Campo “Estabelecimento” do demonstrativo |
| Ano Competência = | Campo “Ano Competência” do demonstrativo |
| Mês Competência = | Campo “Mês Competência” do demonstrativo |
| Indicador Pessoa Fis/Jur = | Campo “Indicador Pessoa Fis/Jur” do demonstrativo |
| Código Pessoa Fis/Jur = | Campo “Código Pessoa Fis/Jur” do demonstrativo |
| Identificador do Demonstrativo de Pagamento = | Campo “Identificador do Demonstrativo de Pagamento” do demonstrativo |


| Status | Permite regeração dos dados |
| --- | --- |
| 1-Aguardando geração XML | Sim |
| 3-Enviando para mensageria | Não |
| 4-Erro geração XML | Sim |
| 5-Evento recebido pela mensageria | Não |
| 6-Evento rejeitado pela mensageria | Sim |
| 7-Em Processamento (mensageria) | Não |
| 8-Recebido pelo Fisco com sucesso | Sim (Retificação) |
| 9-Recebido pelo Fisco com advertência | Sim (Retificação) |
| 10-Rejeitado pelo Fisco | Sim |
| 12-Evento Excluído | Sim |
| 14-Evento excluído na mensageria | Sim |
| 15-Erro técnico na mensageria | Sim |


| Sobre a limpeza do evento já existente: Se o status do evento já existente for = 1 (Aguardando geração XML), 4 (Erro geração XML) ou 14 (Evento excluído na mensageria), este evento será apagado ao efetuar a regeração de um novo evento. Nos demais casos, a limpeza do evento já existente não será feita (para manter o histórico dos erros ocorridos), e será feita apenas a regeração de um novo evento. |
| --- |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO: “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita; Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| indRetif | Conteúdo fixo = “1” (Arquivo original) OBS: A princípio, este campo será gerado sempre como “1” (Arquivo original). Somente após a criação do painel é que teremos o controle automático, para verificar se é uma retificação ou não.  MFS16751: Alteração para gerar também os eventos de retificação. Este campo será gerado de acordo com a verificação de status descrita no item “3-Verificação do Status de Eventos já Gerados”:  Se for a primeira geração do evento do trabalhador no período:       O campo será gerado com “1” (Arquivo Original); Senão       Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:        Se status do evento original = 8 ou = 9  O campo será gerado com “2” (Retificação);       Se status do evento original <> 8 e <> 9  O campo será gerado com “1” (Arquivo Original); |
| --- | --- |
| nrRecibo | Este campo não será gerado OBS: Este campo será gerado somente após a criação do painel, quando teremos o controle automático para verificar se é uma retificação ou não.  MFS16751: Alteração para gerar também os eventos de retificação.  Este campo será gerado de acordo com o conteúdo do campo anterior (indRetif), da seguinte forma:  Se indRetif = “1” (Arquivo Original)       Nesse caso este campo não será gerado;  Se indRetif = “2” (Retificação)       Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado. Ou seja, com o conteúdo      do campo nrRecibo que consta no evento original; |
| indApuracao | Conteúdo fixo = “1” (= Mensal)  (como os autônomos não têm décimo terceiro salário, este campo será gerado sempre como “1”) |
| perApur | Mês e ano do período informado na tela da geração, no formato AAAA-MM (conforme orientação do layout) |
| indGuia  MFS-87292:Vrs S-1.0 | A partir da versão S-1.0 foi criado o campo indGuia. O mesmo não deve ser gerado, pois é destinado a ser informado apenas por empregadores pessoas físicas e usado apenas para o recolhimento unificado dos tributos e do FGTS pelos empregadores domésticos. |
| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do empregador) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”..  Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita; |


| cpfTrab | [ALTERAÇÃO- MFS60476] Tratamento para fornecedores autônomos MEI.  Caso existir informação no campo CPF_SP da tabela X04_PESSOA_FIS_JUR, E se o Campo IND_CLASSE_EMP (Campo 27 - Classe de Empresa) da tabela X04_PESSOA_FIS_JUR for igual a "05 – MEI (Micro Empreendedor Individual)", gerar o campo com a informação do campo CPF_SP, caso contrário seguir com a regra original:  Campo 06-CPF-CGC da SAFX04  Como se trata de autônomos, a pessoa fis/jur deve ser uma pessoa física. Por isso, será verificado o conteúdo do campo “06-CPF-CGC” da pessoa fis/jur recuperada da SAFX04. Se o conteúdo deste campo for um CNPJ, será gravada a mensagem abaixo no log, e o campo cpfTrab não será gerado.  Erro: O campo Número do CPF do Trabalhador (cpfTrab) deve ser um CPF. A informação não será gerada no evento. Origem: Campo “06-CPF-CGC” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX |
| --- | --- |
| nisTrab  MFS-87292:vrs S-1.0 | Campo 35-Número do PIS/PASEP da SAFX04  Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Número de Identificação Social – NIS (nisTrab) é de preenchimento obrigatório e não foi informado Origem: Campo “35-Número do PIS/PASEP” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX  Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |


| indMV | Campo 08-Indicador de Desconto da Contribuição Previdenciária (SAFX247) |
| --- | --- |


| tpInsc | Se conteúdo do campo “08-CNPJ/CPF do Empregador” (SAFX250) for um CNPJ (14 dígitos),       Gravar “1”; Se conteúdo do campo “08-CNPJ/CPF do Empregador” (SAFX250) for um CPF (11 dígitos),       Gravar “2”; |
| --- | --- |
| nrInsc | Campo 08-CNPJ/CPF do Empregador (SAFX250) |
| codCateg | Campo 09-Código da Categoria do Trabalhador (SAFX250) |
| vlrRemunOE | Campo 10-Valor Remuneração (SAFX250) |


| nmTrab | Campo 05-Razão Social da SAFX04 |
| --- | --- |
| dtNascto | Campo 45-Data de Nascimento da SAFX04 Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Data de Nascimento (dtNascto) é de preenchimento obrigatório e não foi informado Origem: Campo “45-Data de Nascimento” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX |
| codCBO  MFS-18065: Campo excluído na vrs 2.4.02; | Campo 34-CBO da SAFX04  Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros: Erro: O campo Classificação Brasileira de Ocupação - CBO (codCBO) é de preenchimento obrigatório e não foi informado Origem: Campo “34-CBO” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX |
| NatAtividade  MFS-18065: Campo excluído na vrs 2.4.02; | Campo 67-Natureza da Atividade da SAFX04  Caso este campo não esteja preenchido na SAFX04, este campo não será gerado. |
| qtdDiasTrab  MFS-18065: Campo excluído na vrs 2.4.02; | Este campo não será gerado  (conforme mapeamento original, esta informação não se aplica aos autônomos) |


| tpTrib  MFS-87292:Vrs S-1.0 | Campo 12-Abrangência do Processo da SAFX2058 (Tabela de Cadastro dos Processos)  Este campo é gerado com a informação da abrangência da decisão referente ao processo. Para obter esta informação, será feita a recuperação dos dados cadastrais do processo na Tabela de Processos (SAFX2058), a partir dos campos “14-Indicador do Tipo de Processo” e “15-Número do Processo” da rubrica (SAFX248).  Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4  A partir da versão S-1.0, os valores válidos são: 1, 2.  Caso este campo não esteja preenchido na SAFX2058 para o processo em questão, será gerada a seguinte mensagem de aviso no log de erros: Erro: O campo Abrangência da Decisão (tpTrib) é de preenchimento obrigatório e não foi informado Origem: Campo “12-Abrangência do Processo” da Tabela de Processo Administrativo/Judicial (SAFX2058) Dados do Registro: Tipo do Processo: X, Número do Processo: XXXXXXXXXXXXXXXXXXX |
| --- | --- |
| nrProcJud | Campo 15-Número do Processo da SAFX248 |
| codSusp | Campo 16-Código do Indicativo da Suspensão da SAFX248 |


| ideDmDev | Campo 07-Identificador do Demonstrativo de Pagamento da SAFX247 |
| --- | --- |
| codCateg | Campo 66-Código da Categoria do Trabalhador da SAFX04  Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código da Categoria do Trabalhador (codCateg) é de preenchimento obrigatório e não foi informado Origem: Campo “66-Código da Categoria do Trabalhador” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX |


| tpInsc   MFS-87292:Vrs S-1.0 | A geração deste campo depende do conteúdo do campo “07-Tipo de Inscrição da Lotação” da SAFX2037 (Tabela de Cadastro dos Setores).  Para obter a informação na Tabela de Setores (SAFX2037), será feita a recuperação dos dados a partir do campo “68-Setor” do cadastro do trabalhador (SAFX04). Havendo mais de um registro do Setor na SAFX2037, será considerado o de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração. Além disso, a validade final do Setor, quando preenchida, deve ser de um mês/ano >= ao mês/ano do período.  Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4  A partir da versão S-1.0, os valores válidos são: 1, 3, 4,  Recuperada a informação do Setor (SAFX2037), a regra da geração do campo é a seguinte:  Se o campo “07-Tipo de Inscrição da Lotação” da SAFX2037 estiver preenchido,       O campo será gravado com o conteúdo do campo “07-Tipo de Inscrição da Lotação” da SAFX2037; Senão,        O campo será gravado com “1”; |
| --- | --- |
| nrInsc | Para a geração deste campo, vale a mesma regra descrita para o campo anterior, mas considerando o campo “08-Número de Inscrição da Lotação” da SAFX2037 (Tabela de Cadastro dos Setores):  Se o campo “08-Número de Inscrição da Lotação” da SAFX2037 estiver preenchido,       O campo será gravado com o conteúdo do campo “08-Número de Inscrição da Lotação” da SAFX2037; Senão,        O campo será gravado com o CNPJ do estabelecimento do demonstrativo (ou seja, da SAFX247). Neste caso        será gravado o CNPJ completo, com os 14 dígitos; |
| codLotacao | [MFS22087] Campo 13-Setor da SAFX247  Caso este campo não esteja preenchido na SAFX247, será verificada se a informação está preenchida no Campo 68-Setor da SAFX04  Caso este campo não esteja preenchido na SAFX04, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código da Lotação Tributária (codLotacao) é de preenchimento obrigatório e não foi informado Origem: Campo “13-Setor” do Demonstrativo de Pagamento dos Autônomos (SAFX247) ou Campo “68-Setor” da Tabela de Cadastro de Pessoas Fis/Jur (SAFX04) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX |
| qtdDiasAv | Este campo não será gerado  (conforme mapeamento original, esta informação não se aplica aos autônomos) |


| codRubr | Campo 09-Código da Rubrica da SAFX248 |
| --- | --- |
| ideTabRubr | Campo 08-Código da Tabela da Rubrica da SAFX248 |
| qtdRubr | Campo 10-Quantidade de Referência da Rubrica da SAFX248 |
| fatorRubr | Campo 11-Fator de Cálculo da Rubrica da SAFX248 |
| vrUnit  MFS-87292:Vrs S-1.0 | Campo 12-Valor Unitário da SAFX248  Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |
| vrRubr | Campo 13-Valor Total da SAFX248 |
| indApurIR  MFS-87292:Vrs S-1.0 | Campo 14-Tipo de apuração de IR  A partir da versão S-1.0, os valores válidos são: 0, 1.  Este campo só deve ser gerado a partir da versão S-1.0.   Como regra, o campo {indApurIR} deve ser preenchido com [0]: com esse indicativo a rubrica é considerada para apuração do IR a partir dos dados informados no eSocial (S-1200, S-1202, S-1207, S-2299 ou S-2399), cabendo o envio do R-4004 na EFD-Reinf para iniciar a apuração e enviar as informações complementares solicitadas pela DIRF. Excepcionalmente, podem haver situações (por exemplo, RRA) em que para ocorrer a correta apuração do IR com base nas informações do eSocial o declarante precisa elaborar uma estrutura complexa neste evento. Para evitar isso, ele pode optar por enviar os valores no grupo [itensRemun] 93 indicando {indApurIR}=[1] e, nesse caso o IR não é apurado com base no eSocial e esses valores devem ser informados no R-4010 da EFD-Reinf direto no formato tradicional da DIRF. |


| Observação sobre a alteração da versão 2.4.02: Os campos deste registro eram originalmente gerados no registro “infoComplem” (filho do “ideTrabalhador”). Na versão 2.4.02 eles foram “transferidos“ para este novo registro “infoComplCont”. Como o novo registro é filho do “dmDev”, pressupõe-se que possam existir trabalhadores que tenham mais de um demonstrativo no período, sendo cada um deles de uma atividade diferente. Desta forma, o mais lógico seria que estas informações fossem criadas na tabela do demonstrativo (SAFX247), no entanto, como a geração do eSocial é restrita aos autônomos, continuaremos a utilizar os dados da SAFX04. Futuramente, se for necessário, podemos incluir estes dados junto ao demonstrativo (SAFX247). |
| --- |


| codCBO | [MFS19608] Campo 12-CBO da SAFX247  Caso este campo não esteja preenchido na SAFX247, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Classificação Brasileira de Ocupação - CBO (codCBO) é de preenchimento obrigatório e não foi informado Origem: Campo “12-CBO” da Tabela Demonstrativo de Pagamento dos Autônomos (SAFX247) Dados do Registro: Pessoa Fis/Jur (Ind/Cód): X / XXXXXXXXXXXXXXXXX    Estab: XXXXXXXX |
| --- | --- |
| natAtividade | Campo 67-Natureza da Atividade da SAFX04  Caso este campo não esteja preenchido na SAFX04, este campo não será gerado. |
| qtdDiasTrab | Este campo não será gerado (conforme mapeamento original, esta informação não se aplica aos autônomos) |
