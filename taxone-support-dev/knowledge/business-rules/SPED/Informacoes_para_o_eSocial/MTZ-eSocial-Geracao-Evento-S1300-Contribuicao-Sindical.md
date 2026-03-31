# MTZ-eSocial-Geracao-Evento-S1300-Contribuicao-Sindical

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1300-Contribuicao-Sindical.docx
- **Modificado:** 2022-06-07
- **Tamanho:** 83 KB

---

THOMSON REUTERS

Módulo eSocial

Geração Evento S\-1300

\(Contribuição Sindical Patronal\) 

__Localização__: Menu SPED, módulo Informações para o eSocial, menu Geração 🡪 Geração Prévia dos Movimentos 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS15871__

Geração do evento S\-1300

Geração dos dados do evento S\-1300 \(Contribuição Sindical Patronal\)

28/12/2017 

\(criação do documento\)

__MFS16751__

Controle Status x Regeração

Críticas em relação a regeração dos eventos\. 

28/03/2018

<a id="_Hlk523235881"></a>__MFS16762__

Lara Aline

Inclusão rotina de Reprocessar Evento

28/08/2018

__MFS\-87543__

__Elisabete Costa__

__Exclusão do Evento S\-1300 \- Para versão S\-1\.0__

__06/06/2022__

Sumário

[1\.	Parâmetros da Tela	2](#_Toc517780597)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc517780598)

[3\.	Verificação do Status de Eventos já Gerados	4](#_Toc517780599)

[4\.	Gravação dos Dados	6](#_Toc517780600)

__O Evento S\-1300 não deve ser gerado a partir da versão S\-1\.0__

__\[MFS\-87543\]__

# <a id="_Toc517780597"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1300\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\-eSocial\-Geracao\-Movimentos*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc517780598"></a>Recuperação dos Dados e Processamento

__Origem dos dados__: \- Parametrização “Dados Iniciais” do Módulo eSocial;

                               \- SAFX251 \- Tabela das Contribuições Sindicais do Período;

A partir da versão S1\.0 esse evento não será mais gerado\.

__Critérios para a recuperação dos dados da parametrização “Dados Iniciais”__:

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

     \- Estabelecimento – estabelecimento selecionado na tela da geração;

__Critérios para a recuperação das contribuições sindicais do período na SAFX251__:

     \- __Empresa__ – empresa do estabelecimento centralizador selecionado;

     \- __Estabelecimento__ – Serão recuperadas as contribuições de todos os estabelecimentos envolvidos na centralização \(o estabelecimento

       centralizador, que é o selecionado em tela, e os centralizados\), de acordo com a parametrização das obrigações federais do módulo

       Parâmetros \(menu Preliminares > Centralização da Escrituração de Obrigações Federais\);

     \- __Ano Referência__ – ano do período informado na tela da geração \(campo “Período”\);

     \- __Mês Referência__ – mês do período informado na tela da geração \(campo “Período”\);

__Agrupamento dos dados:__

Para cada estabelecimento centralizador será gerado um único evento S\-1300, com as informações descritas no item “Gravação dos Dados”\. 

As contribuições recuperadas para cada estabelecimento centralizador, serão agrupadas e totalizadas pelas seguintes informações:

     \- Sindicato \(campo 05\-Código do Sindicato\);

     \- Tipo da Contribuição \(campo 06\-Tipo da Contribuição\);

     \- Campo a ser totalizado: 07\-Valor da Contribuição

O resultado de cada totalização irá gerar um registro __contribSind__\. Desta forma, se dois estabelecimentos envolvidos na centralização tiverem contribuições na SAFX251 para um mesmo Sindicato, e que sejam do mesmo tipo, será gerado um único registo __contribSind__ no evento\. 

Exemplo: Supondo que os estabelecimentos ESOC1 e ESOC2 estejam centralizados, sendo o ESOC1 o centralizador, e que existam na SAFX251 as seguintes contribuições:

__Estabelecimento__

__Sindicato__

__Tipo__

__Valor__

ESOC1

__SD\-1__

__1__

4\.500,00

ESOC1

__SD\-1__

__2__

1\.200,00

ESOC1

__SD\-2__

__1__

850,00

ESOC2

__SD\-1__

__1__

6\.000,00

ESOC2

__SD\-2__

__1__

2\.400,00

ESOC2

__SD\-3__

__1__

700,00

O resultado do agrupamento seria o seguinte, e seriam gravados quatro registros __contribSind__:

__Sindicato__

__Tipo__

__Valor__

__SD\-1__

__1__

10\.500,00

__SD\-1__

__2__

1\.200,00

__SD\-2__

__1__

3\.250,00

__SD\-3__

__1__

700,00

# <a id="_Toc509582647"></a><a id="_Toc509925718"></a><a id="_Toc509929675"></a><a id="_Toc509937503"></a><a id="_Toc517780599"></a>Verificação do Status de Eventos já Gerados

__MFS16751__: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente\. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1300\_OC, coluna IND\_STATUS\)\.

Para cada estabelecimento a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este estabelecimento no mesmo período de referência\.

__Caso não:__ 

      O evento do estabelecimento será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

      A geração de um novo evento para o estabelecimento dependerá do status do evento já existente, da seguinte forma:

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

        Se o status do evento já existente __não__ permitir regeração:

            Nesse caso, o estabelecimento em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:

*                  Aviso: Já existe evento anterior gerado para o estabelecimento\. O status do evento não permite uma nova geração\.*

*                  Dados do Registro:  Estabelecimento: XXXXXX  /  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX, *__*Período*__*: XX/XXXX *

        Se o status do evento já existente permitir regeração:

             Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação __ORIGINAL__ ou uma

             __RETIFICAÇÃO__, dependendo do status do evento original, como descrito a seguir:

              \- Se status do evento original = 8 ou = 9 🡪 Nesse caso, o novo evento será gerado como __RETIFICAÇÃO__;

 

              \- Se status do evento original <> 8 e <> 9 🡪 Nesse caso, o novo evento será gerado como __ORIGINAL__;

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

<a id="_Hlk523235760"></a>__\[MFS16762\]__

<a id="_Hlk523155984"></a>__Importante:__ Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação \(Critérios estão no documento de tela do Painel de Controle de Eventos\) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\. 

# <a id="_Toc517780600"></a>Gravação dos Dados

As contribuições recuperadas, agrupadas e totalizadas conforme a regra acima, serão geradas num único evento S\-1300, com as seguintes informações: 

*\(os registros não citados não serão gerados\)*

__Registro evtContrSindPatr__ – Evento Contribuição Sindical Patronal

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

__Se__ for a primeira geração do evento do estabelecimento no período:

      O campo será gerado com “__1__” \(__Arquivo Original__\);

__Senão__

      Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:

      Se status do evento original = 8 ou = 9 🡪 O campo será gerado com “__2__” \(__Retificação__\);

      Se status do evento original <> 8 e <> 9 🡪 O campo será gerado com “__1__” \(__Arquivo Original__\);

nrRecibo

Este campo não será preenchido

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

__Registro contribSind__ \- Informações da contribuição sindical patronal\.

Este registro é gerado a partir das contribuições agrupadas e totalizadas conforme descrito no item “*2\-Recuperação dos Dados e Processamento*”\.

Para cada combinação de Sindicato e Tipo da Contribuição, será gerado um registro __contribSind__ com o valor total das contribuições\.

cnpjSindic

Este campo será gerado com a informação do CNPJ do sindicato, recuperado da SAFX2048 \(Tabela dos Sindicatos, campo CNPJ do Sindicato\), através do campo 05\-Código do Sindicato da SAFX251\.

Caso o CNPJ do Sindicato não esteja preenchido na SAFX2048, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo CNPJ da entidade Sindical Beneficiária \(cnpjSindic\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “05\-CNPJ do Sindicato” da Tabela de Sindicatos \(SAFX2048\)*

*Dados do Registro: Sindicato: XXXXX*

tpContribSind

Campo 06\-Tipo da Contribuição

vlrContribSind

Campo 07\-Valor da Contribuição \(total agrupado por Sindicato e Tipo da Contribuição\)

= = = = = =

 

