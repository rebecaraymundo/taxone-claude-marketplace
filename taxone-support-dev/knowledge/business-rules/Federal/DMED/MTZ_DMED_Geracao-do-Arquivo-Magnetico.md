# MTZ_DMED_Geracao-do-Arquivo-Magnetico

- **Fonte:** MTZ_DMED_Geracao-do-Arquivo-Magnetico.docx
- **Modificado:** 2024-08-30
- **Tamanho:** 86 KB

---

THOMSON REUTERS

__Módulo DMED – Geração do Arquivo Magnético__

__Localização__: Menu Federal,  Módulo: DMED, item de menu Obrigações à Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS3814

Criação do Módulo da DMED 

Criação do Módulo da DMED

18/11/2014

__\(criação do docto\)__

MFS\-47274

Alessandra Cristina Navatta

Inclusão de validação para aceitar ano referência a partir de 2015\.

Inclusão do Campo “10 \- Indicador declarante possui registro ANS”, no registro DECPJ, a partir do ano referência 2021\.

Ajustar na tela o label Ano de Referência para Ano Calendário

26/11/2020

MFS\-75996

Alessandra Cristina Navatta

Inclusão de validação para aceitar no campo ano calendário, ano a partir de 2016\. A regra foi ajustada para ficar genérica \(evitando ajuste anual\)\. 

25/11/2021

MFS\-558025

Rogério Ohashi

Tratamento da regra do Campo “10 \- Indicador declarante possui registro ANS”, para gravar “Nulo”, se o Campo de Tipo de Declarante for igual à 1\.

21/08/2023

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta geração foi criada na OS3814, que criou o Módulo da DMED \(Declaração de Serviços Médicos e de Saúde\), e faz a geração do arquivo magnético de acordo com as especificações do layout descritas na Instrução Normativa 1\.504, de 29/10/2014  \(layout no Anexo Único\)\.

__OBS__: Na versão original da geração foi desenvolvida apenas a geração dos registros referentes aos prestadores de serviço de saúde\. Assim, os registros específicos das operadoras *não* foram gerados \(registros OPPAS, TOP, RTOP, DTOP e RDTOP\)\.

Nome do arquivo a ser gerado: “__DMED\_9999__”, sendo “9999” o ano de referência informado na tela da geração\. 

\(o Anexo Único que divulgou o layout, *não* traz nenhuma informação sobre o nome do arquivo a ser gerado\)

__RN01__

__                                                          Parâmetros de Tela__

__Ano Calendário__ à Neste campo o usuário informará um ano para a recuperação dos dados\. 

__\[Alteração MFS\-47274\]__ – 

Deve ser indicado na tela ano maior ou igual a 2015\. Se ano for menor que 2015, exibir a mensagem: “Informar ano calendário a partir de 2015”

__\[Alteração MFS\-75996\] – __

__Preencher o ano, com a informação menor ou igual ao ano atual\. O menor ano permitido deve ser no máximo, seis anos anterior ao ano atual\. Ex\. Para Ano 2021: permitir ano de 2015 até 2021, Para Ano 2022: permitir ano a partir de 2016 até 2022, etc\.\.\. Se a regra não for atendida, exibir a mensagem: “Informar ano calendário a partir de <menor ano permitido>”__

__Declaração retificadora__ à Este campo é uma lista com as seguintes opções:

    Não

    Sim 

Valor default: opção “Não” 

__Número recibo da última declaração__ à Campo numérico de 12 posições  Este campo ficará habilitado apenas quando o campo “Declaração retificadora” for = “Sim”\. Caso contrário, ficará desabilitado\. 

 	

__Situação da declaração__ à Este campo é uma lista com as seguintes opções:

Normal

Declaração de situação especial 

Valor default: opção “Normal” 

__Data do evento__ à Campo data \(dia, mês e ano\)\.  Este campo ficará habilitado apenas quando o campo “Situação da declaração” for = “Declaração de situação especial”\. Caso contrário, ficará desabilitado\.

Este campo é de preenchimento obrigatório quando a opção do campo “Situação da declaração” for = “Declaração de situação especial”\. Neste caso, se não preenchido, será exibida a seguinte mensagem em tela e a geração não será iniciada:

__*                                                                                    “Informe Data do Evento”*__

__Estabelecimentos__ à Neste campo será exibida a lista dos estabelecimentos para seleção do usuário\. Para isso será utilizada a parametrização da centralização dos estabelecimentos para escrituração das obrigações federais do Módulo Parâmetros \(menu “Preliminares à Centralização da Escrituração de Obrigações Federias”\)\.

Serão disponibilizados os estabelecimentos que atendam aos seguintes critérios:

     \- Estabelecimentos da empresa do login;

 

    \- Estabelecimentos parametrizados nos dados iniciais \(menu “Parâmetros à Dados Iniciais”\);

     \- Estabelecimentos centralizadores \(conforme a parametrização da centralização dos estabelecimentos descrita acima\);

       __ou__

     \- Estabelecimentos “independentes”, ou seja, estabelecimentos que, de acordo com esta parametrização, não sejam centralizadores, e também

       não constem como estabelecimento centralizado de nenhuma das centralização existentes; 

Os estabelecimentos centralizadores aparecerão no seguinte formato:  “*Estab\. Centralizador: XXXXXX – XXXXXXXXXXXXXXXXXX*”

Os estabelecimentos “independentes” aparecerão no seguinte formato: “*Estab\. Descentralizado: XXXXXX – XXXXXXXXXXXXXXXXXX*”

Primeiro serão listados todos os centralizadores, e depois os “independentes”\. Para realçar a diferença entre os tipos de estabelecimento, os “independentes” serão mostrados sempre algumas colunas a frente dos centralizadores\.

Exemplo:

 \[  \]  Estab\. Centralizador: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 \[  \]  Estab\. Centralizador: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 \[  \]  Estab\. Centralizador: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 \[  \]  Estab\. Centralizador: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 \[  \]     Estab\. Descentralizado: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 \[  \]     Estab\. Descentralizado: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

*\(é o mesmo conceito utilizado na geração do Sped Contribuições, no menu “Obrigações à Geração dos Registros”\) *

__RN02__

__                                          Recuperação e Processamento dos Dados __

__Origem dos dados__: 

     \- Parametrização dos dados iniciais da DMED     \(menu “Parâmetros à Dados Iniciais”\)

     \- Parametrização das Operações                         \(menu “Parâmetros à Operações”\)

     \- Parametrização das Contas Contábeis              \(menu “Parâmetros à Contas Contábeis”\)

     \- Tabelas do Contas a Receber                            \(SAFX05 e SAFX501\)

Será gerado um arquivo para cada estabelecimento selecionado em tela, da seguinte forma:

__No caso dos estabelecimentos centralizadores__:

 

Neste caso, ao utilizar qualquer uma das parametrizações \(dados iniciais, operações e contas\) o acesso aos dados será feito sempre em nome do estabelecimento centralizador\. Desta forma, o usuário só precisa parametrizar os dados em nome do centralizador\.

Ao recuperar os dados do contas a receber \(SAFX05\), serão considerados os dados de todos os estabelecimentos envolvidos, o centralizador e *todos os seus centralizados*\.

__No caso dos estabelecimentos “independentes”__:

Neste caso, ao utilizar qualquer uma das parametrizações \(dados iniciais, operações e contas\) o acesso aos dados será feito sempre em nome do próprio estabelecimento “independente”\. Assim, o usuário precisará cadastrar as parametrizações em nome de cada um dos estabelecimentos “independentes”, quando for necessário gerar desta forma\.

Ao recuperar os dados do contas a receber \(SAFX05\), serão considerados *apenas* os dados do estabelecimento “independente”\.

__Utilização da parametrização das operações e contas contábeis:__

A utilização da parametrização das operações e das contas contábeis dependerá da opção do usuário nos dados iniciais \(menu “Parâmetros à Dados Iniciais”\), da seguinte forma:

     Se campo “Parâmetros para geração da DMED” =  __1__ \(*Operações\)*

           Neste caso será utilizada apenas a parametrização por operação; 

     Se campo “Parâmetros para geração da DMED” = __2__ \(*Contas Contábeis\)*

           Neste caso será utilizada apenas a parametrização por conta contábil; 

     Se campo “Parâmetros para geração da DMED” = __3__ \(*Operações \+ Contas Contábeis\)* 

           Neste caso serão utilizadas as duas parametrização \(operação e conta contábil\); 

__Critérios para a recuperação dos dados na SAFX05 e SAFX501:__

       __SAFX05__:

Empresa

= código da empresa do login;

Estabelecimento

Depende do tipo do estabelecimento selecionado em tela \(conforme descrito acima\):

Se centralizador à deve ser = código do estabelecimento centralizador ou qualquer um dos seus centralizados;

Se descentralizado à deve ser = código do estabelecimento;

Data do Movimento

Deve ser uma data enquadrada no ano de referência informado em tela; 

Operação

Se “Parâmetros para geração da DMED” = __1__ \(*Operações*\) ou __3__ \(*Operações \+ Contas Contábeis\):*

     O movimento deve ter a operação \(campo “10\-Código de Operação”\) parametrizada;

Senão

     A operação do movimento poderá ser qualquer \(não será verificada\);

Conta

Se “Parâmetros para geração da DMED” = __2__ \(*Contas Contábeis*\) ou __3__ \(*Operações \+ Contas Contábeis\):*

     O movimento deve ter a conta \(campo “16\-Conta Contábil”\) parametrizada;

Senão

     A conta do movimento poderá ser qualquer \(não será verificada\);

      __SAFX501 \(Parcelas\)__:

Para cada registro do contas a receber recuperado \(SAFX05\), de acordo com os critérios acima, serão recuperadas todas as suas parcelas cuja data de pagamento __\(\*\)__ seja do ano de referência informado em tela\.

 

__\(\*\)__ campo “18\-Data do Pagamento”

Atenção à Os movimentos da SAFX05 que atendam as regras descritas, mas *não* tenham nenhuma parcela \(SAFX501\) paga no ano, *não serão considerados*\. Isso porque só interessa à DMED os valores recebidos no ano, que corresponde aos pagamentos recebidos das pessoas físicas\.

__ __ 

__Totalização dos dados recuperados:__

Os valores das parcelas recuperadas \(campo “14\-Valor da Parcela”\) serão totalizados por:

     \- Pessoa Fis/Jur do movimento     \(campos 04 e 05 da SAFX05\)

     \- Beneficiário do movimento          \(campos 29 e 30 da SAFX05\)

O beneficiário é uma pessoa fis/jur indicada nos campos 29 e 30 da SAFX05\. 

Quando o beneficiário do pagamento é a própria pessoa fis/jur, o campo “Beneficiário” da SAFX05 estará nulo\. 

Caso contrário o campo “Beneficiário” estará preenchido\. 

Assim, a totalização dos valores poderá resultar: 

Apenas um valor total referente ao valor pago no ano cujo beneficiário é o próprio pagador:

Valor total das parcelas pagas cujo campo “Beneficiário” \(campo 29 da SAFX05\) esteja vazio\.

‘n’ valores totais pagos cujo beneficiário sejam outras pessoas:

Valor total das parcelas pagas cujo campo “Beneficiário” \(campo 29 da SAFX05\) esteja preenchido com uma pessoa fis/jur diferente da pessoa do campo 04/05\.

A seguir serão descritas as regras especificas da geração de cada registro:

 

__RN03__

__                                                  Estrutura do Arquivo da DMED __

__Registro__

__Ocorrência__

__Conteúdo__

__DMED__

\(1 p/arquivo\)

Informações sobre a declaração

__RESPO__

\(1 p/arquivo\)

Dados do responsável pela declaração

__DECPJ__

\(1 p/arquivo\)

Dados do declarante

__OPPAS__

\(1 p/arquivo\)

__\(se o declarante for = OPERADORA\)__

__     TOP__

\(vários\)

Titular do plano \- Valores recebidos no ano

__          RTOP__

\(vários p/cada TOP\)

Titular do plano \- Valores reembolsados \(por prestador do serviço\)

__     DTOP__

\(vários p/cada TOP\)

Dependente \- Valores recebidos no ano

__          RDTOP__

\(vários p/cada DTOP\)

Dependente \- Valores reembolsados \(por prestador do serviço\)

__PSS__

\(1 p/arquivo\)

__\(se o declarante for = PRESTADOR DE SERVIÇO\)__

__     RPPSS__

\(vários\)

Responsável pelo pagamento \- Valores recebidos no ano \(em seu benefício\)

__          BRPPSS__

\(vários p/cada RPPSS\)

Responsável pelo pagamento \- Valores recebidos no ano \(em benefício de terceiros\)

__FIMDMED__

\(1 p/arquivo\)

Registro de encerramento do arquivo

__OBS__: Como descrito nas regras gerais \(RN00\), a versão original da geração \(OS3814\) desenvolveu apenas os registros específicos dos prestadores de serviço\. Assim, os registros OPPAS, TOP, RTOP, DTOP e RDTOP não foram gerados\.

__RN\-DMED__

__                                                           Registro DMED __

Registro de abertura do arquivo\.

Este registro é gerado a partir dos parâmetros informados na tela da geração\.

Ver preenchimento dos campos na planilha “DMED\_De\-Para”\.

__RN\-RESPO__

__                                                   Registro RESPO __

Registro que contém os dados do responsável pela declaração DMED\.

Este responsável é parametrizado no menu “Parâmetros à Dados Iniciais”, campo “Responsável pela declaração”\. Suas informações de cadastro são recuperadas na tabela dos responsáveis legais \(módulo Parâmetros, item “Requisitos Legais à Responsável por Informações”\)\. 

Ver preenchimento dos campos na planilha “DMED\_De\-Para”\.

Obs: Para o campo “02\-CPF” não é necessário verificar se o conteúdo do campo na tabela é mesmo um CPF, pois na parametrização dos dados iniciais só é aceito o cadastro de responsável que seja uma pessoa física\.

__RN\-DECPJ__

__                                                     Registro DECPJ __

Registro que contém os dados da empresa declarante das informações da DMED\.

Os dados para geração deste registro serão as informações cadastrais do estabelecimento da geração \(tabela ESTABELECIMENTO\), e alguns dados parametrizados no menu “Parâmetros à Dados Iniciais”\.

*\(quando se tratar de geração centralizada serão recuperados os dados do estabelecimento centralizador\)  *

Ver preenchimento dos campos na planilha “DMED\_De\-Para” e regras específicas descritas a seguir:

Campo “__07\-CPF Responsável perante o CNPJ__”:

O conteúdo deste campo é o CPF do cadastro dos responsáveis legais \(módulo Parâmetros\) do responsável parametrizado nos dados iniciais, no campo “Responsável pela empresa”\.

Obs: Para este campo não é necessário verificar se o conteúdo do campo na tabela é mesmo um CPF, pois na parametrização dos dados iniciais só é aceito o cadastro de responsável que seja uma pessoa física\.

__\[Alteração MFS\-47274\]__ Inclusão do Campo “__10 \- Indicador declarante possui registro ANS__”, a partir do ano referência 2021 \(ano da data que está sendo gerada a obrigação\) \. 

__\[Alteração MFS\-558025\]__ Readequação da Regra de geração do Campo de Ordem “__10 \- Indicador declarante possui registro ANS”\.__

      

__Se__ o campo de tipo do declarante for igual à 1 o Campo 10 não deve ser preenchido – Gravar o campo em branco ||

__Ou__

__        Se__ o campo de tipo do declarante seja igual à 2 ou 3;

__ Preencher__ com "S", se campo "Registro ANS" estiver preenchido, caso contrário preencher com "N"\.  

            __Se__ o campo de tipo do declarante for igual à 2 ou 3, e o campo não tenha sido preenchido, será exibida a mensagem abaixo e a operação não será salva:

*                                                         “O registro ANS deve ser informado quando o tipo de declarante for 2 ou 3”*

__Obs\.: __Campo de preenchimento obrigatório se o campo de tipo do declarante seja igual à 2 ou 3\]

__RN\-PSS__

__                                                 Registro PSS__

Este registro será gerado apenas quando o declarante for um prestador de serviços de saúde\. Para isso, será verificado o conteúdo do campo “Tipo do Declarante”, da parametrização dos dados iniciais\.

Se “Tipo do Declarante” = 1 \(Prestador de Serviço\) __ou__ 3 \(Prestador de Serviço e Operadora\) àneste caso, será gravado o registro PSS;	 

__RN\-RPPSS__

__                                                 Registro RPPSS__

Este registro demonstra os valores recebidos no ano, *detalhados pelos responsáveis dos pagamentos*, mas apenas no caso dos pagamentos feitos em benefício próprio\.

\(valores recebidos em benefício de terceiros são demonstrados no registro BRPPSS\)

Os pagamentos feitos em benefício próprio são os registros da SAFX05 em que o campo “Beneficiário” esteja sem preenchimento\.

  

De acordo com as regras de totalização dos valores descritas na __RN02__, será gravado um registro RPPSS para cada resultado obtido de pagamentos realizados em benefício próprio \(quando existe a pessoa fis/jur e *não* existe um beneficiário\)\.

Os registros RPPSS serão ordenados por CPF \(campo 02\)\.

Ver preenchimento dos campos na planilha “DMED\_De\-Para” e regras específicas descritas a seguir\.

Campo “__02\-CPF do responsável pelo pagamento__”:

Pelas regras da DMED os pagamentos a serem demonstrados são apenas de pessoas físicas\. Sendo assim, o correto é que sejam parametrizados \(por operação e/ou conta contábil\), apenas os lançamentos da SAFX05 referentes a pessoas fis/jur com CPF\. Caso a informação do campo \(conforme as regras da totalização descrita na __RN02__\), seja um CNPJ \(conteúdo de 14 caracteres\), o registro RPPSS *não será gravado* no arquivo, e será gravada a seguinte mensagem de erro no log do processo:

__*“Registro de pagamentos de pessoas jurídicas não são considerados na DMED\. Favor rever a parametrização das operações e/ou contas contábeis”*__

O log exibirá os dados de identificação da pessoa fis/jur em questão \(Indicador e Código\), para que o usuário possa conferir os dados\.

Importante à Neste caso, além de não gravar o registro RPPSS, *também não serão gravados os registros “filhos” BRPPSS* caso existam \(registros dos pagamentos feitos em benefício de terceiros\)\.

Campo “__03\-Nome__”:

A razão social da pessoa fis/jur será truncada quando necessário, caso o conteúdo do campo na SAFX04 ultrapasse as 60 posições do layout\.

Campo “__04\-Valor pago no ano pelo responsável em benefício próprio__”:

O valor gravado neste campo é o resultado da totalização das parcelas pagas pela pessoa fis/jur da SAFX05 em benefício próprio, ou seja, quando não existe a informação de um beneficiário \(vide regras da totalização na __RN02__\)\.

OBS: Este valor poderá ter conteúdo = zero quando existirem apenas pagamentos feitos pela pessoa fis/jur em benefício de terceiros \(vide regra descrita na __RN\-BRPPSS__ sobre “__quando a pessoa fis/jur tiver apenas pagamentos realizados em benefício de terceiros__”\)\.

__RN\-BRPPSS__

__                                          Registro BRPPSS__

Este registro demonstra os valores recebidos no ano, *detalhados pelos responsáveis dos pagamentos e por beneficiário*, ou seja, apenas no caso dos pagamentos feitos em benefício de terceiros\.

Os registros BRPPSS são “filhos” do RPPSS, e assim, devem ser gravados sempre abaixo do “pai” RPPSS\.

Os pagamentos feitos em benefício de terceiros são os registros da SAFX05 em que o campo “Beneficiário” esteja preenchimento\.

De acordo com as regras de totalização dos valores descritas na __RN02__, será gravado um registro BRPPSS para cada resultado obtido de pagamentos realizados em benefício de terceiros \(quando existe a pessoa fis/jur e o beneficiário\)\.

Os registros BRPPSS de cada “pai” RPPSS, serão ordenados por CPF \(campo 02\) e data do nascimento \(campo 03\)\.

__Importante__: __\(quando a pessoa fis/jur tiver apenas pagamentos realizados em benefício de terceiros\)__

Caso nos resultados da totalização feita conforme __RN02__, existam dados para um registro “filho” BRPPSS, e não exista valores para o registro “pai” RPPSS, o procedimento será o seguinte:

\- Será gravado um registro RPPSS com o campo “04\-Valor pago no ano” = zero;

\- Associado ao “pai” RPPSS será gravado normalmente o registro “filho”;

Este procedimento é necessário para que os valores pagos pela pessoa fis/jur em benefício de terceiros possa ser demonstrado no arquivo, mesmo quando não exista nenhum pagamento feito por esta pessoa em benefício próprio \(já que o registro filho não pode ser gravado sem o pai correspondente\)\.

Ver preenchimento dos campos na planilha “DMED\_De\-Para” e regras específicas descritas a seguir\.

Campo “__02\-CPF do Beneficiário__”:

O beneficiário pode não ter CPF, e nesse caso este campo ficará sem preenchimento \(“||”\)\. Por isso o campo não é obrigatório no layout\. É o caso por exemplo, de um beneficiário menor de idade sem CPF, e neste caso, o cadastro da SAFX04 será feito como uma pessoa “Especial”, utilizado para as pessoas sem CNPJ/CPF \(campo “04\-Indicador de Conteúdo do código” = 4\)\.

Obs: No caso do beneficiário ter um CPF, não é necessário verificar se o conteúdo do campo na tabela \(SAFX04\) é mesmo um CPF, pois na importação / manutenção da SAFX05 só é aceito o cadastro de beneficiário que seja uma pessoa física\.

Campo “__03\-Data de Nascimento__”:

Este campo é obrigatório quando não existir o CPF \(o que ocorrerá na situação descrita acima\)\. Sendo assim, será feita a seguinte crítica:

Se não existir informação nem para o CPF, nem para a data de nascimento do beneficiário: 

      O registro será gerado normalmente sem informação nos dois campos, mas será gravada a seguinte mensagem de erro no log de processo: 

__*  “Beneficiários sem CPF cadastrado, devem ter a informação da data do nascimento\. Verificar o cadastro da pessoa na SAFX04”*__

O log exibirá os dados de identificação da pessoa fis/jur do beneficiário \(Indicador e Código\), para que o usuário possa conferir os dados\.

Campo “__04\-Nome__”:

A razão social da pessoa fis/jur será truncada quando necessário, caso o conteúdo do campo na SAFX04 ultrapasse as 60 posições do layout\.

__RN\-FIMDMED__

__                                             Registro FIMDMED__

Registro de finalização do arquivo\.

= = = = = 

