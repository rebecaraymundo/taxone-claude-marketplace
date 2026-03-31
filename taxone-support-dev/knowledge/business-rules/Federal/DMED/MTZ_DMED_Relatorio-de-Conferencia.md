# MTZ_DMED_Relatorio-de-Conferencia

- **Fonte:** MTZ_DMED_Relatorio-de-Conferencia.docx
- **Modificado:** 2022-02-15
- **Tamanho:** 77 KB

---

THOMSON REUTERS

__Módulo DMED – Relatório de Conferência__

__Localização__: Menu Federal,  Módulo: DMED, item de menu Relatórios 🡪 Relatório de Conferência

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS3814

Criação do Módulo da DMED 

Criação do Módulo da DMED

24/11/2014

\(criação do docto\)

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Este relatório foi criado na OS3814, que criou o Módulo da DMED \(Declaração de Serviços Médicos e de Saúde\), e seu objetivo é demonstrar cada um dos movimentos do contas a pagar \(SAFX05\) que compõem os totais a serem gerados no arquivo magnético da DMED\.

__OBS__: Assim como a geração do meio magnético, na versão original do relatório foi desenvolvida apenas a parte da DMED referente aos prestadores de serviço de saúde\. Os dados específicos das operadoras *não* foram gerados \(registros OPPAS, TOP, RTOP, DTOP e RDTOP\)\.

__RN01__

__                                                          Parâmetros de Tela__

Como este relatório trabalha com seleção de pessoas fis/jur \(SAFX04\), é necessário trabalhar comum Grupo de Relacionamento\. Para isso, na abertura da tela será exibida a janela de seleção do grupo de relacionamento \(da mesma forma que é feita nas telas de parametrização de operações e contas contábeis\)\.

O usuário irá selecionar um grupo de relacionamento, e o grupo escolhido será demonstrado ao lado do campo “Pessoa Física/Jurídica”\.

__Ano de Referência__ 🡪 Neste campo o usuário informará um ano de referência para a recuperação dos dados\. 

__Pessoa Física/Jurídica__ 🡪 Ao lado deste campo será exibido o grupo de relacionamento escolhido pelo usuário na abertura da tela\. Como padrão neste tipo de tela, esta informação *não* fica habilitada para alteração do usuário\. A mudança do grupo só poderá ser feita através do botão “Grupo” da barra de menu\.

Este campo trabalha com janela de seleção da SAFX04\. Serão exibidas para seleção apenas as pessoas fis/jur do grupo de relacionamento escolhido pelo usuário na abertura da tela\. 

Após selecionar a pessoa fis/jur, serão exibidas em tela as seguintes informações da pessoa:

      \- Indicador e código \(na primeira linha\)

      \- Razão Social \(na segunda linha\)

O usuário não poderá digitar o indicador ou código da pessoa, pois os campos *não* serão habilitados para digitação\. Assim, para selecionar uma pessoa, o usuário deverá obrigatoriamente abrir a janela de seleção \(pastinha amarela\) e selecionar a pessoa desejada\.

__Estabelecimentos__ 🡪 Neste campo será exibida a lista dos estabelecimentos para seleção do usuário\. Para isso será utilizada a parametrização da centralização dos estabelecimentos para escrituração das obrigações federais do Módulo Parâmetros \(menu “Preliminares 🡪 Centralização da Escrituração de Obrigações Federias”\)\.

Serão disponibilizados os estabelecimentos que atendam aos seguintes critérios:

     \- Estabelecimentos da empresa do login;

 

    \- Estabelecimentos parametrizados nos dados inicias \(menu “Parâmetros 🡪 Dados Iniciais”\);

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

*\(é o mesmo conceito utilizado na geração do Sped Contribuições, no menu “Obrigações 🡪 Geração dos Registros”\) *

__RN02__

__                                          Recuperação e Processamento dos Dados __

O processo deste relatório é o mesmo da geração do arquivo, com a diferença que no relatório os valores das parcelas *não* são totalizados\. Ao invés de demonstrar os totais de cada pessoa fis/jur, em benefício próprio, e/ou de cada beneficiário, quando for o caso, o relatório detalha os movimentos envolvidos em cada totalização\. Mas a lógica é a mesma para os dois processos\.

__Origem dos dados__: 

     \- Parametrização dos dados iniciais da DMED     \(menu “Parâmetros 🡪 Dados Iniciais”\)

     \- Parametrização das Operações                         \(menu “Parâmetros 🡪 Operações”\)

     \- Parametrização das Contas Contábeis              \(menu “Parâmetros 🡪 Contas Contábeis”\)

     \- Tabelas do Contas a Receber                            \(SAFX05 e SAFX501\)

Será gerado um relatório para cada estabelecimento selecionado em tela, da seguinte forma:

__No caso dos estabelecimentos centralizadores__:

 

Neste caso, ao utilizar qualquer uma das parametrizações \(dados iniciais, operações e contas\) o acesso aos dados será feito sempre em nome do estabelecimento centralizador\. Desta forma, o usuário só precisa parametrizar os dados em nome do centralizador\.

Ao recuperar os dados do contas a receber \(SAFX05\), serão considerados os dados de todos os estabelecimentos envolvidos, o centralizador e *todos os seus centralizados*\.

Como o relatório mostra movimento a movimento, a origem do movimento é mostrada na coluna “Estab\.”\.

__No caso dos estabelecimentos “independentes”__:

Neste caso, ao utilizar qualquer uma das parametrizações \(dados iniciais, operações e contas\) o acesso aos dados será feito sempre em nome do próprio estabelecimento “independente”\. Assim, o usuário precisará cadastrar as parametrizações em nome de cada um dos estabelecimentos “independentes”, quando for necessário gerar desta forma\.

Ao recuperar os dados do contas a receber \(SAFX05\), serão considerados *apenas* os dados do estabelecimento “independente”\.

__Utilização da parametrização das operações e contas contábeis:__

A utilização da parametrização das operações e das contas contábeis dependerá da opção do usuário nos dados iniciais \(menu “Parâmetros 🡪 Dados Iniciais”\), da seguinte forma:

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

Se centralizador 🡪 deve ser = código do estabelecimento centralizador ou qualquer um dos seus centralizados;

Se descentralizado 🡪 deve ser = código do estabelecimento;

Data do Movimento

Deve ser uma data enquadrada no ano de referência informado em tela; 

Pessoa Fis/Jur

Depende se o usuário escolheu ou não uma pessoa fis/jur específica na tela da geração:

Quando for informada uma pessoa fis/jur 🡪 neste caso, a pessoa fis/jur do movimento deve ser = a pessoa fis/jur selecionada em tela \(indicador e código\);

Caso contrário 🡪 a informação da pessoa fis/jur não será utilizada nos critérios da recuperação dos dados;

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

Atenção 🡪 Os movimentos da SAFX05 que atendam as regras descritas, mas *não* tenham nenhuma parcela \(SAFX501\) paga no ano, *não serão considerados*\. Isso porque só interessa à DMED os valores recebidos no ano, que corresponde aos pagamentos recebidos das pessoas físicas\.

Os dados recuperados serão agrupados por pessoa fis/jur \(campos 04 e 05\) e beneficiário \(campo 29 e 30\)\.

Com base nos dados recuperados, o relatório será gerado estabelecimento a estabelecimento selecionado em tela\.

__Ordenação dos dados__:

Para o relatório de cada estabelecimento, os dados serão ordenados da seguinte forma:

          \- Pessoa Fis/Jur \(ordenar pela razão social da pessoa fis/jur\) 

          \- Beneficiário \(ordenar pela razão social da pessoa fis/jur beneficiária\)

Para cada pessoa / beneficiário, os movimentos serão ordenados por:

          \- Data do Movimento

          \- Número do Documento

Para cada movimento, as parcelas serão ordenadas por:   \(caso exista mais de uma parcela para o movimento\) 

          \- Número da parcela

Sobre o beneficiário:

O beneficiário é uma pessoa fis/jur indicada nos campos 29 e 30 da SAFX05\. 

Quando o beneficiário do pagamento é a própria pessoa fis/jur, o campo “Beneficiário” da SAFX05 estará nulo\. Caso contrário o campo “Beneficiário” estará preenchido\. 

Segue regras do preenchimento dos dados no relatório: 

__RN03__

__                                                             Cabeçalho __

Ver layout na planilha anexa “*Relatorio\_de\_Conferencia\_da\_DMED*”\.

No cabeçalho serão demonstrados os seguinte dados:

\- Razão social do estabelecimento \(do centralizador, quando for o caso\);

\- Data da emissão do relatório;

\- Página;

\- Ano de referência informado em tela;

\- CNPJ do estabelecimento \(do centralizador, quando for o caso\);

__RN04__

__                           Linha de identificação da pessoa fis/jur e o beneficiário __

Esta linha será impressa sempre que for iniciar a demonstração dos movimentos de uma determinada pessoa fis/jur e o beneficiário, ou, ao iniciar uma nova página\.

Pessoa Física/Jurídica

Indicador, código e razão social da pessoa fis/jur dos movimentos 

\(referente a pessoa fis/jur dos campos 04 e 05 da SAFX05\) 

Beneficiário

Indicador, código e razão social da pessoa fis/jur beneficiária

 \(referente a pessoa fis/jur dos campos 29 e 30 da SAFX05\)

Quando não existir beneficiário, este campo será preenchido com a seguinte informação:  “*\(o próprio\)*”

\(conforme o exemplo que aparece na planilha de layout\)

 

__RN05__

__                                                 Linha de detalhe dos movimentos__

Esta linha demonstra os movimentos e suas parcelas pagas, referentes a pessoa fis/jur e beneficiário\.

c\(como descrito na RN02, os movimentos serão ordenados por Data do Movimento, Número do Documento e Número da parcela\)

No caso dos movimentos com mais de uma parcela, a informação das colunas referentes à SAFX05 *não se repetem*\. Ou seja, os dados que identificam o movimento serão mostrados apenas na linha referente *a primeira parcela*\. 

Dt\. Movto\. 

Data do movimento \(campo 03 da SAFX05\)

N\. Documento 

Número e série do documento \(campos 07 e 08 da SAFX05\)

Dt\. Emissão

Data de emissão do movimento \(campo 11 da SAFX05\)

Valor

Valor do movimento \(campo 14 da SAFX05\)

Operação

Código da operação do movimento \(campo 10 da SAFX05\)

Conta Contábil

Código da conta do movimento \(campo 16 da SAFX05\)

Parcela

Estas informações são referentes às parcelas pagas do movimento:

Campo 12 \- Número da Parcela \(SAFX501\)

Campo 13 – Data do Vencimento \(SAFX501\)

Campo 18 – Data do Pagamento \(SAFX501\)

Campo 14 \- Valor da Parcela \(SAFX501\)

Vencimento

Pagamento

Valor Pago

Estab\.

Código do estabelecimento de origem do movimento\.

\(o objetivo desta coluna é identificar a origem do movimento, já que as obrigações federais são centralizadas\)

__RN06__

__                               Linha de total da pessoa fis/jur e beneficiário__

Esta linha será impressa após o último movimento de cada pessoa fis/jur e beneficiário, demonstrando o valor total dos pagamentos\.

Total da Pessoa Fis/Jur e Beneficiário

Totalização da coluna “Valor Pago” dos movimentos de cada pessoa fis/jur e beneficiário

__RN07__

__                                          Linha do total geral da pessoa fis/jur __

Esta linha será impressa após a demonstração de todos os movimentos de uma determinada pessoa fis/jur e todos os seus beneficiários, demonstrando o total geral dos pagamentos da pessoa fis/jur\.

Total Geral da Pessoa Fis/Jur

Totalização da coluna “Valor Pago” de todos os movimentos de uma pessoa fis/jur 

\(totalizando todos os beneficiários\)

__RN08__

__                                       Linha do total geral do estabelecimento __

Esta linha será impressa após a demonstração de todos os movimentos de uma determinada pessoa fis/jur e todos os seus beneficiários, demonstrando o total geral dos pagamentos da pessoa fis/jur\.

Total Geral

Totalização da coluna “Valor Pago” de todos os movimentos do estabelecimento 

\(considerando que será impresso um relatório para cada estabelecimento selecionado em tela\)

= = = = = 

