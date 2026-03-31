# MTZ-CIAP-Calculo_Credito_Extemporaneo

- **Fonte:** MTZ-CIAP-Calculo_Credito_Extemporaneo.docx
- **Modificado:** 2025-12-26
- **Tamanho:** 39 KB

---

# Módulo – Ativo Permanente – Cálculo dos Créditos Extemporâneos 

Localização: Menu Estadual, Módulo CIAP, item Movimento 🡪 Créditos Extemporâneos 🡪 Cálculo dos Créditos Extemporâneos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS2931\-B10

Tratamento dos Créditos Extemporâneos

O objetivo desta OS é implementar o tratamento dos créditos extemporâneos do CIAP para a geração do registro G126 do Sped Fiscal – Bloco G\. 

27/09/2010

\(criação\)

OS2388\-E23

Aumento da quantidade de casas decimais do IND\_PER\_SAI de 4 para 8\.

OS3708\-B

Atendimento ao Decreto 49\.382/12 – RS

Alteração no cálculo do CIAP para utilizar a parametrização das regras específicas do tempo de apropriação \(vide __RN01__, Passo 3\)\.

03/08/2012

OS4459

Alteração Modelo C \(frações diferenciadas\)

Alterações no Modelo C para mostrar os resultados separados por fração \(IN50 e Ajuste SINIEF\)  \(__RN01, Passo 2__\)

10/04/2014

MFS2713

Nova parametrização de regras específicas no formato “Por Estabelecimento”\.

Criação de nova opção “Por Estabelecimento” p/a parametrização de regras específicas p/o prazo de apropriação dos créditos \(a parametrização original do módulo é por UF\)\. \(vide __RN01, Passo 3__\)\.

12/01/2016

MFS22919

Alteração no cálculo dos créditos extemporâneos 

Incluída nova coluna na tabela do cálculo para armazenar a numeração das parcelas de forma sequencial \(vide __RN03__\)\.\.\.

13/12/2018

## REGRAS DE NEGÓCIO

__Cód__

__Descrição__

__DR__

# RN00

O cálculo dos créditos extemporâneos foi implementado no Módulo CIAP para atender à geração do registro G126 do Sped Fiscal na __OS2931\-B10__\.

Antes de habilitar os parâmetros para seleção do usuário, deverá ser exibida a seguinte mensagem:

O Cálculo dos Créditos  Extemporâneos é opcional, e quando utilizado, deve ser executado obrigatoriamente antes do cálculo dos créditos do CIAP\. A alteração na seqüência destes processos pode acarretar erro no cálculo das parcelas, dependendo dos parâmetros utilizados para o cálculo \(consultar detalhes no help\)\.

                                                                               <OK>

Parâmetros de Tela:

Campo __Período__ 🡪 Data inicial e final do período a ser apurado\. Como o CIAP não trabalha com calendário, as telas permitem que o usuário informe qualquer intervalo de datas\. Mas as datas devem pertencer ao mesmo mês, por isso, são efetuadas as mesmas críticas do cálculo “normal” \(item “Movimento 🡪 Cálculo do Crédito – ICMS”\), que são:

Verifica se o ano é o mesmo\. Senão, exibe a mensagem 🡪  “*O ano inicial e final deve ser o mesmo*”

Verifica se o mês é o mesmo\. Senão, exibe a mensagem 🡪  “*O mês inicial e final deve ser o mesmo*”

Verifica se a data final é >= inicial\.  Senão, exibe a mensagem 🡪  “A data inicial não pode ser maior que a final”

Campo __Estabelecimentos__ 🡪 Exibe todos os estabelecimentos da Empresa parametrizados no CIAP \(menu “Cadastros 🡪 Parâmetros de Estabelecimento”\)\.

    

OS2931\-B10

# RN01

__PROCESSAMENTO__:

O processo consiste em calcular as parcelas dos períodos anteriores, desde a data fiscal da nota, até o período imediatamente anterior ao período da data de operação\. 

__Etapas do cálculo__:

- Antes de iniciar o processo, os valores já calculados para o período solicitado são excluídos, para que o cálculo possa ser reprocessado; 
- Recupera do cadastro do CIAP todas as aquisições com data de operação \(DAT\_OPER\) dentro do período informado em tela\. Além disso, a data de operação também deve ser de um período posterior ao período da data fiscal da aquisição \(DAT\_FISCAL\)\.  O entendimento do que seja “período” depende da periodicidade:

🡪 Se *mensal* \(fração = 1/48\) 🡪 significa que as datas terão que ser de *meses* diferentes;

 

                   🡪 Se *quinzenal* \(fração = 1/96\) 🡪 significa que as datas terão que ser de *quinzenas* diferentes;

 

                   🡪 Se *decendial* \(fração = 1/144\) 🡪 significa que as datas terão que ser de *decêndios* diferentes;

                   Além dos critérios de data, verifica\-se também o status do Bem\. Na prática os critérios para recuperação 

                   das aquisições são os seguintes:

                   Empresa              – código da Empresa

                   Estabelecimento – código do Estabelecimento selecionado para o cálculo

                   Data de Operação \- deve ser uma data compreendida no período informado p/o cálculo

                   Data Fiscal – deve ser uma data de um período *anterior* ao período da data de operação

                   Status do Bem – deve ser <> “I” 

 

 __Obs__: Bens com status “E” serão recuperados normalmente, sem a necessidade de verificar quando foi efetuada a baixa, como é feito no cálculo “normal”\. Isso porque um Bem só pode ser alienado em uma data >= a Data de Operação do cadastro do CIAP, que é a data em que o Bem entrou no CIAP\.  Assim, nunca haverá a possibilidade de existir uma baixa para um período "extemporâneo"\.  A preocupação com o status “E” no momento de efetuar o cálculo do CIAP é por causa do reprocessamento\) 

- Para cada aquisição recuperada, será efetuado o cálculo das parcelas extemporâneas\. Dependendo da diferença entre as datas, poderão ser calculadas uma ou várias parcelas extemporâneas\. O cálculo é feito desde o período da data fiscal da aquisição, até o período imediatamente *anterior* ao período informado em tela;

Exemplo:

Data Operação = 20/09/2010

Data Fiscal        = 15/07/2010

\(significa que a nota entrou na Empresa em 15/07, mas só foi incluída no CIAP em 20/09\)

__Periodicidade Mensal__:

Período informado em tela: __01/09/2010 a 30/09/2010__

A parcela referente a este período será calculada normalmente no cálculo do CIAP deste período

Parcelas extemporâneas a serem calculadas:

Parcela 1, período de referência 🡪 01/07/2010 a 31/07/2010   \(mês de Julho\)

Parcela 2, período de referência 🡪 01/08/2010 a 31/08/2010   \(mês de Agosto\)

__Periodicidade Quinzenal__:

Período informado em tela: __16/09/2010 a 30/09/2010__

A parcela referente a este período \(segunda quinzena de Setembro\) será calculada normalmente no cálculo do CIAP deste período

Parcelas extemporâneas a serem calculadas:

Parcela 1, período de referência 🡪 01/07/2010 a 15/07/2010   \(primeira quinzena de Julho\)

Parcela 2, período de referência 🡪 16/07/2010 a 31/07/2010   \(segunda quinzena de Julho\)

Parcela 3, período de referência 🡪 01/08/2010 a 15/08/2010   \(primeira quinzena de Agosto\)

Parcela 4, período de referência 🡪 16/08/2010 a 31/08/2010   \(segunda quinzena de Agosto\)

Parcela 5, período de referência 🡪 01/09/2010 a 15/09/2010   \(primeira quinzena de Setembro\)

__Periodicidade Decendial__:

Período informado em tela: __11/09/2010 a 20/09/2010__

A parcela referente a este período \(segundo decêndio de Setembro\) será calculada normalmente no cálculo do CIAP deste período

Parcelas extemporâneas a serem calculadas:

Parcela 1, período de referência 🡪 01/07/2010 a 10/07/2010   \(primeiro decêndio de Julho\)

Parcela 2, período de referência 🡪 11/07/2010 a 20/07/2010   \(segundo decêndio de Julho\)

Parcela 3, período de referência 🡪 21/07/2010 a 31/07/2010   \(terceiro decêndio de Julho\)

Parcela 4, período de referência 🡪 01/08/2010 a 10/08/2010   \(primeiro decêndio de Agosto\)

Parcela 5, período de referência 🡪 11/08/2010 a 20/08/2010   \(segundo decêndio de Agosto\)

Parcela 6, período de referência 🡪 21/08/2010 a 31/08/2010   \(terceiro decêndio de Agosto\)

Parcela 7, período de referência 🡪 01/09/2010 a 10/09/2010   \(primeiro decêndio de Setembro\)

__Para cada parcela a ser calculada o procedimento é o seguinte__:

__Passo 1__🡺 Totaliza os valores de ICMS do Bem:

 

Soma os valores de ICMS da aquisição \(valor ICMS \+ Valor Difal \+ Valor Frete \+ Difal Frete \+  Valor ICMS\-ST\);

Importante 🡪 A utilização ou não dos valores de diferencial de alíquota neste total depende do parâmetro

 “*Apropriação do Dif de Alíquota*” \(menu “Cadastros 🡪 Parâmetros por Estabelecimento”\), seguindo o

mesmo procedimento feito nas rotinas do cálculo “normal” do CIAP\.

Segue condição para utilizar ou não os valores do difal no total do ICMS:

A condição para utilização do diferencial de alíquota se baseia nos seguintes parâmetros:

- Parâmetro de apropriação do Diferencial de Alíquota;
- Número da parcela extemporânea;
- Data do Internamento da NF \(somente p/a opção “4” do parâmetro\); 

__Se  parâmetro Difal =  “1” ou  nulo__

       Somar os valores do diferencial de alíquota \(independente da parcela\);

__Se parâmetro Difal = “2”__

      Se número da parcela = 1

            *Não* somar os valores do diferencial de alíquota;

      Senão

            Somar os valores do diferencial de alíquota;

__Se parâmetro Difal = “3”__

        *Não* somar os valores do diferencial de alíquota \(independente da parcela\);

__Se parâmetro Difal = “4”__

      Verificar se a data de internamento do cadastro das aquisições esta preenchida \(campo “*49\-Data de*

*      Notificação de Internamento da NF*” da SAFX82\): 

       Caso não: 

           \-Considerar o valor total do ICMS do Bem = 0 \(fará com que o valor da parcela seja = 0\)

           \-Grava a seguinte mensagem de aviso no log de processo: 

           “*Existem Documento\(s\) Fiscal\(is\) sem a Data de Notificacao do Internamento\- AM*”

            \(é a mensagem de código 50904 da TFIX22\)

       Caso sim:

           \-Verificar a diferença de meses existente entre a data de internamento e a data final

            do periodo a que se refere a parcela extemporânea \(ou seja, é a data do campo “Data

            final do período da parcela” que será gravada na tabela dos créditos extemp\.\):

             Se diferença < 2

                   *Não* somar os valores do diferencial de alíquota;

             Senão

                   Somar os valores do diferencial de alíquota;

Obs: Este tratamento é o mesmo feito no cálculo “normal” do CIAP\.

__Passo 2__ 🡺 Calcula o coeficiente das saídas

O cálculo de cada parcela considera o coeficiente das saídas que foi utilizado no período\.  Esta informação é obtida na tabela do cálculo que tem o resultado final do período da parcela a ser calculada\. Na tabela existe um único registro de resultado para cada período:    *\(vide OBS abaixo sobre a *__*OS4459*__*\)*

 

     \- Se Modelo C 🡪 Utiliza a tabela APT\_DEM\_CR\_MENSAL

     \- Se Modelo D 🡪 Utiliza a tabela APT\_EST\_MENS\_ANO

Nos dois casos os critérios para recuperação são:

COD\_EMPRESA   = empresa do login

COD\_ESTAB         = estabelecimento para o qual estão sendo calculadas as parcelas extemporâneas

DAT\_APURACAO = data final do período \(seja mês, quinzena ou período\)

Valores a serem recuperados: Valor das Saídas Tributadas e Valor Total das Saídas do período\.

Calcula o coeficiente das saídas da seguinte forma, considerando 4 casas decimais na operação:

           Coeficiente =  Valor das Saídas Tributadas  / Valor Total das Saídas do período

Alteração __OS2388\-E23__ 🡪 Este cálculo passou a ser feito, considerando 8 casas decimais, ao invés de 4 como feito na versão original \(alteração do Ato Cotepe ICMS N\. 2, de 16/03/2011, que aumentou a quantidade de decimais par 8\)\.

Alteração __OS4459__ 🡪 No caso do Modelo C, a tabela dos resultados do período foi alterada para inclusão da fração na chave primária\. Assim, poderão existir ‘n’ linhas de resultado para o mesmo período, diferenciadas apenas pela fração\. Neste caso, as informações a serem obtidas p/o cálculo do crédito extemporâneo são únicas no período, ou seja, as colunas que interessam no caso, terão o mesmo conteúdo em todas as linhas referentes a um mesmo período\. Por isso, basta recuperar qualquer uma das linhas de resultado referentes ao período desejado\.

OBS: Nesta etapa do cálculo, quando ocorrer de não encontrar na base de dados as informações do cálculo referentes ao período em questão \(período da parcela extemporânea a ser calculada\), o procedimento será o seguinte: 

🡪 A parcela de crédito referente a este período não será calculada;

🡪 Será gravada a seguinte mensagem de aviso no log de processo:

      “*Os valores referentes ao cálculo do CIAP do período não foram identificados na base de dados\. A parcela  de crédito *

*      extemporânea deste período não será calculada, pela impossibilidade de calcular o coeficiente das saídas*”

      \(o log também informará o período e o registro do CIAP em questão, para que o usuário possa resolver o problema\)

__Passo 3__ 🡺 Divide o ICMS pelo número de parcelas

Divide o valor total do ICMS calculado no passo \(1\), pelo número de parcelas, considerando 2 casas decimais na operação\.

O número de parcelas depende da periodicidade:

Total ICMS / 48    🡪 se periodicidade mensal \(Fração = 1/48\)  

Total ICMS / 96      🡪 se periodicidade quinzenal \(Fração = 1/96\)

Total ICMS / 144     🡪 se periodicidade decendial \(Fração = 1/144\)

__Alteração da OS3708\-B \(Ago/12\)__:     Criação da parametrização das regras específicas por UF

__Alteração da MFS2713 \(Jan/16\)__:        Criação da parametrização das regras específicas por Estabelecimento

O número de parcelas depende dos seguintes critérios:

\- O campo “Fração” da parametrização por estabelecimento;

\- A parametrização das regras específicas por UF; 

     \(menu “Cadastros 🡪 Regras Específicas p/o Prazo de Apropriação dos Créditos p/ UF”\) 

\- A parametrização das regras específicas por Estabelecimento; 

     \(menu “Cadastros 🡪 Regras Específicas p/o Prazo de Apropriação dos Créditos p/ Estabelecimento”\), 

A partir destes critérios, a obtenção da fração a ser utilizada é feita da seguinte forma:

__Se__ o CFOP ou CFOP/Nat da aquisição constar na parametrização das regras específicas __por  Estabelecimento__, com uma data

        de validade que englobe a data fiscal da aquisição: 

         Neste caso o total do ICMS será dividido pelo número de parcelas da parametrização \(Total ICMS / N\. Parcelas\)

__Senão__

     Se o CFOP ou CFOP/Nat  da aquisição constar na parametrização das regras específicas __por UF__ com um período de validade

           que englobe a data fiscal da aquisição: 

            Neste caso o total do ICMS será dividido pelo número de parcelas da parametrização \(Total ICMS / N\. Parcelas\)

     Senão    *\(neste caso será utilizado o procedimento original\)*

            Total ICMS / 48    🡪 se periodicidade mensal \(Fração = 1/48\)  

            Total ICMS / 96      🡪 se periodicidade quinzenal \(Fração = 1/96\)

            Total ICMS / 144     🡪 se periodicidade decendial \(Fração = 1/144\)

A ideia é pesquisar as parametrizações exatamente nessa ordem de __prioridade__, ou seja, primeiro verificar se a operação esta parametrizada nas regras específicas *por estabelecimento*\. Caso não, pesquisar a parametrização das regras específicas *por UF*, e quando não existir nenhuma das duas, será utilizado o procedimento original do módulo, que é utilizar a fração informada na parametrização geral do CIAP\. 

Na pesquisa da parametrização das regras específicas serão observados os seguintes detalhes:

- Ao pesquisar a parametrização __por UF__, deve\-se considerar apenas os dados referentes à UF do Estabelecimento em questão, ou seja, estabelecimento para o qual a aquisição esta cadastrada;
- Ao pesquisar a parametrização __por Estabelecimento__, considerar apenas os dados referentes ao estabelecimento da aquisição em questão, ou seja, estabelecimento para o qual a aquisição esta cadastrada\. Quando se tratar de geração por Inscrição Estadual Única, a parametrização a ser utilizada também deve ser sempre a do estabelecimento da aquisição, independente de quem seja o centralizador;
- Se a aquisição tiver CFOP e NAT \(campos 12 e 13 da SAFX82\) 🡪 usar a parametrização por CFOP/NAT
- Se a aquisição tiver apenas o CFOP 🡪 usar a parametrização do CFOP
- Se a aquisição não tiver o CFOP 🡪 neste caso, considerar que não existe nenhuma parametrização de regras específicas, e aplicar o procedimento original do módulo;
- Considerar apenas os registros da parametrização cujo período de validade englobe a data fiscal da nota fiscal da aquisição \(campo 09\-Data Fiscal da SAFX82\)
- Ao verificar as datas, observar que somente a data inicial da validade da parametrização é obrigatória\. A data final poderá ou não estar preenchida\. Caso não esteja, significa que o término da validade ainda não foi definido, ou seja, a regra é válida desde a data inicial até “sempre”\.  

__Passo 4__ 🡺 Aplica o coeficiente das saídas 

Sobre o valor obtido no Passo \(3\), multiplica o coeficiente das saídas calculado no Passo \(2\), considerando 2 casas decimais na operação:

Valor da Parcela = Valor Passo \(3\) \* Coeficiente Passo \(2\)

Obs: O cálculo é feito em etapas, conforme descreve os passos \(3\) e \(4\), ao invés de fazer um único cálculo dividindo o total do ICMS por 48, 96 ou 144, e na mesma conta multiplicando pelo coeficiente\.  

Os valores das parcelas extemporâneas calculadas para cada Bem são armazenados numa tabela, conforme descrito na __RN02__\.

# RN02

__Gravação dos Dados Calculados__:

Para cada parcela de crédito calculada, são armazenadas as seguintes informações:

Empresa 

Empresa do login

Estabelecimento

Estabelecimento em questão 

\(no caso do cálculo por I\.E\.U\. o estabelecimento a ser gravado será sempre o centralizador\)

Data da Apuração

\(data final do período informado em tela\)

Todos os dados calculados nesta rotina ficarão armazenados *para uma única data de apuração*, que é a data final do período informado em tela\.

As parcelas extemporâneas referentes a Bens incluídos no CIAP num determinado período, serão apropriadas *neste mesmo período*, junto à parcela “oficial” deste período, que é a que aparecerá no Livro do CIAP\.

Obs: Da mesma forma que nas tabelas da apuração do CIAP, basta armazenar a data final do período \(esta informação corresponde à coluna DAT\_APURACAO das tabelas de cálculo do CIAP\)\.

Identificador do CIAP \(NUM\_CIAP\)

Assim como todas as tabelas internas do CIAP, a identificação do registro da aquisição é feita através do NUM\_CIAP\. 

Data inicial do período da parcela 

Data final do período da parcela

Data inicial e final do período a que se refere à parcela extemporânea\.  

Número da parcela calculada

As parcelas extemporâneas calculadas são numeradas do 1 em diante, começando da mais antiga \(do período mais antigo\)\.

Valor da parcela passível de apropriação 

Valor calculado no Passo \(3\)\.

Valor total das saídas do período a que se refere o crédito calculado

Valor calculado no Passo \(2\)\.

Valor das saídas tributadas do período a que se refere o crédito calculado

Valor calculado no Passo \(2\)\.

Valor da parcela 

Valor calculado no Passo \(4\)\.

Estabelecimento de Origem

Código do estabelecimento de origem da aquisição

\(este campo é utilizado apenas no caso do cálculo por I\.E\.U\.\)

CFOP

CFOP do cadastro das aquisições

Obs: Esta informação é armazenada para auxiliar o processo de geração de NF com os créditos do CIAP, no caso da nota ser gerada com CFOP’s distintos\.

Número da Parcela Sequencial

Número da parcela calculada de forma sequencial, conforme descrito na __RN03__\. 

Validação do CFOP🡪 Assim como no cálculo “normal” do CIAP, este cálculo verifica se o CFOP da aquisição esta preenchido, e *caso não esteja* o processo será finalizado com , e no log serão geradas as seguintes mensagens:

🡪  “*Aquisição com CFOP nulo\. Não irá gerar lançamento do crédito por CFOP*” \(msg código 50453 já usada no cálculo normal\)

🡪 “*Processo de geração do cálculo dos créditos extemporâneos interrompido por erro*”   

# RN03

__Número da parcela sequencial:__

Esta coluna será preenchida *apenas* quando o parâmetro *“Gerar a numeração das parcelas de forma sequencial nos casos de transferência de Bens entre estabelecimentos” \(menu Cadastros > Parâmetros de Estabelecimento\)* estiver marcado\.

Caso contrário, a coluna ficará sem preenchimento\. 

Obs\.: Este procedimento poderia ser feito sempre, sem nenhum parâmetro\. No entanto, isso poderia impactar a performance, e por isso, optamos pela criação do parâmetro\.  

__Regra de preenchimento:__

Esta coluna foi criada na tabela do cálculo pela __MFS22137/MFS22919__, com objetivo de armazenar o número da parcela “sequencial” calculada no período\. 

Obs\.: O campo “Número da Parcela” que compõe a chave da tabela \(coluna NUM\_PARCELA\) continua a ser gerado normalmente, sem alterações\. 

O diferencial do “__Número da parcela sequencial”__ é que esta coluna armazena a numeração da parcela em sequência única por Código de Bem, considerando todos os estabelecimentos da empresa\.

Desta forma, quando um Bem for transferido entre estabelecimentos, a primeira parcela calculada no estabelecimento de destino *não* será a parcela 1, e sim a parcela sequencial, considerando todas as parcelas já calculadas para o Bem nos estabelecimentos de origem da\(s\) transferência\(s\)\.

Forma de calcular a parcela sequencial:

     \[ Conteúdo gravado no campo “Número da Parcela” \+ Quantidade parcelas calculadas nos outros estab’s \]

A parcela sequencial é obtida somando\-se ao conteúdo gravado no campo “Número da Parcela”, a quantidade de parcelas já calculadas nos estabelecimentos anteriores \(outros estabelecimentos da mesma empresa\) por onde o Bem tenha passado antes da transferência, considerando também os créditos extemporâneos que possam existir nestes estabelecimentos anteriores\.

Obs: Para verificar a quantidade de parcelas dos outros estabelecimentos, uma alternativa é comparar o campo “N\. Parcela” da aquisição *no primeiro estabelecimento* com a aquisição no estabelecimento atual, e apurar a diferença entre os dois\. O resultado será o número de parcelas calculadas nos estabelecimentos anteriores\.

Ver exemplo sobre a numeração das parcelas na planilha anexa “*Exemplo\_Numeracao\_Parcelas*”\.

Obs\.: A informação da parcela sequencial será utilizada na geração do Bloco G do Sped Fiscal, especificamente na opção desenvolvida para o cliente Nextel \(parâmetro “*Gerar os registros a partir de valores calculados pelo CIAP no mês anterior*” do menu “Dados Iniciais” = “S”\)\. 

MFS22919

