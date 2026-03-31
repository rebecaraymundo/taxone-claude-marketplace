# MTZ-CIAP-Rel_Conferencia_ModC_por_Fracao

- **Fonte:** MTZ-CIAP-Rel_Conferencia_ModC_por_Fracao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

                                           __Módulo CIAP – Relatório de Conferência do Modelo C por Fração__

__                                       __

__Localização: __Menu Estadual, Módulo CIAP, menu Relatórios 🡪 Conferência Modelo C por Fração \(IN50/Aj\.SINIEF\) 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4459\-B

Alteração Modelo C \(frações diferenciadas\)

Alterações no Modelo C para mostrar os resultados separados por fração \(IN50 e Ajuste SINIEF\)

14/04/2014

REGRAS DE NEGÓCIO

__RN00 \- Regras gerais__

Relatório criado na OS4459\-B com objetivo de possibilitar a conferência dos totais do Modelo C por fração \(ver detalhes no help\)\. 

O relatório é específico para os livros Modelo C dos formatos IN50 e Ajuste SINIEF, cujos totais são calculados por fração, quando for o caso\.

Para gerar o relatório é pré\-requisito que o cálculo do CIAP tenha sido executado para o período em questão, pois as informações serão recuperadas das tabelas que contém o resultado dos cálculos\.

__RN01 – Parâmetros da Geração__

__Data da Apuração de Referência__ 🡪 Esta data \(DDMMAAAA\) será utilizada para a recuperação dos dados nas tabelas do cálculo do CIAP

__Geração por Inscrição Estadual Única__ 🡪 Parâmetro S/N para indicar quando o cálculo do CIAP for feito por inscrição estadual única\. Default = desmarcado\. Este parâmetro será utilizado apenas para filtrar os estabelecimentos centralizadores na seleção dos estabelecimentos, e também para exibir o estabelecimento de origem do Bem no relatório \(ver na RN04 as regras de preenchimento da coluna “N\. ou Código”\)\. 

__UF__ 🡪 Este campo é a lista das UF’s da tabela ESTADOS \+ opção “Todas as UF’s”\. 

__Estabelecimentos__ 🡪 Neste quadro serão demonstrados os estabelecimentos para seleção do usuário\. Serão exibidos apenas os estabelecimentos que atendam aos seguintes critérios:

\- estabelecimentos parametrizados no CIAP \(item “Cadastros 🡪 Parâmetros por Estabelecimento”\);

\- estabelecimentos da UF informada no campo “UF”;

\- estabelecimentos que utilizem o livro Modelo C, do formato da IN50 ou do Ajuste SINIEF \(item “Cadastros 🡪 Parâmetros por Estabelecimento”\);

\- se parâmetro “Geração por Inscrição Estadual Única” marcado, serão exibidos apenas os estabelecimentos centralizadores, de acordo com a 

   parametrização dos estabelecimentos centralizadores de inscrição única do Módulo de Controle das Obrigações Estaduais\.

 

Para cada estabelecimento selecionado será gerado um relatório, de acordo com as regras descritas a seguir\.

Os estabelecimentos selecionados, mas sem movimento no período solicitado *não* serão considerados\. 

__RN02 – Origem dos Dados e Processamento__

__Origem dos Dados__: Tabela das Aquisições e tabelas dos cálculos do Modelo C do CIAP: 

\- Tabela das Aquisições do CIAP 🡪 APT\_AQUISICAO

\- Tabela dos Bens envolvidos no cálculo do período 🡪 APT\_DEM\_BASE\_CR

\- Tabela dos totais do período 🡪 APT\_DEM\_CR\_MENSAL

__Processamento__:

Serão recuperados todos os registros da tabela de cálculo dos Bens \(APT\_DEM\_BASE\_CR\), considerando o estabelecimento e o período solicitados:

      COD\_EMPRESA    =  código da empresa

      COD\_ESTAB          =  código do estabelecimento

      DAT\_APURACAO  =  data da apuração solicitada

Os registros recuperados serão exatamente as linhas que compõe o Quadro 2 dos livros Modelo C \(IN50 e Aj\.SINIEF\)\.

Esses dados serão agrupados pela fração \(incluída na tabela pela OS4459\), e gerados no relatório por quebra de fração\.

Ao finalizar os movimentos de uma determinada fração, será impresso um quadro de total, mostrando o valor total do crédito do período referente a fração em questão\.

A seguir serão descritas as regras do preenchimento dos dados no relatório\.

__RN03 – Cabeçalho__

Primeira linha 🡪 nesta linha será impresso a razão social da Empresa, a data da geração do relatório e a página;

Segunda linha 🡪 nesta linha será impresso o código, a razão social, o CNPJ e a inscrição estadual do estabelecimento;

Terceira linha 🡪 nesta linha será impresso o título do relatório e a data da apuração em questão \(informada em tela\); 

__RN04 \- Demonstrativo dos Bens com Fração Mensal de “nn” Parcelas:__

\(“nn” – fração referente aos Bens que serão demonstrados\)

Sob este título serão demonstrados todos os Bens recuperados da tabela do cálculo \(conforme processamento descrito na __RN02__\), agrupados por fração\.

Ordenação das linhas:

Para cada fração, a ordenação das linhas será a partir dos seguintes dados:

      \- Ano da aquisição do Bem, que aparece concatenado ao número do Bem na coluna “N\. ou Código” \(ver abaixo regra de preenchimento do

        campo “N\. ou Código”\);

      \- Para cada ano, conforme item anterior, a ordenação será pelo número ou código do Bem \(NUM\_OFICIAL\_CIAP\);

      \- Por último, para cada ano e número, a ordenação será pela data da operação \(DAT\_OPER\)\. No caso, o Bem poderá ter mais de uma linha

        quando existir uma ou mais baixas \(saídas\) no período;

O preenchimento das colunas será feito no mesmo formato em que os movimentos são demonstrados no livro, e correspondem as seguintes colunas da tabela do cálculo \(APT\_DEM\_BASE\_CR\):

 

__N\. ou Código__ – O preenchimento desta coluna depende do parâmetro “*Geração por Inscrição Estadual Única*”, da seguinte forma:

Se parâmetro __*desmarcado*__:

Neste caso o conteúdo do campo será a concatenação do número oficial do Bem \(coluna NUM\_OFICIAL\_CIAP\) com o ano da aquisição do Bem\.

*\(mesmo que seja um movimento de saída, o ano a ser concatenado é sempre o ano da aquisição do Bem \(ao invés do ano da saída\), da mesma forma que é feito na emissão do livro\) *

Exemplo:

__N\. ou Código__

__Data__

__Nota Fiscal__

__Descrição__

__Entrada__

__Saída__

__Total Crédito a Apropriar__

0000551/2012

10/04/2012

110

Maquina de Cortar 

100,00

100,00

__0000551/2012__

__20/01/2014__

556

Maquina de Cortar

100,00

0,00

00000552/2012

01/07/2012

222

Furadeira Modelo 123

250,00

250,00

00000553/2012

10/12/2012

980

Furadeira Modelo 456

50,00

300,00

00000024/2013

05/04/2013

444

Trator 

200,00

500,00

__00000024/2013__

__31/01/2014__

557

Trator

200,00

300,00

00000025/2013

20/04/2013

440

Pallets Modelo 888 Pequeno

100,00

400,00

00000026/2013

01/05/2013

680

Pallets Modelo 888 Médio

120,00

520,00

00000027/2013

30/11/2013

420

Pallets Modelo 888 Grande

80,00

600,00

0000001/2014

10/01/2014

560

Esteira 

300,00

900,00

0000002/2014

15/01/2014

561

Empilhadeira

400,00

1\.300,00

__0000002/2014__

__31/01/2014__

558

Empilhadeira

400,00

900,00

Se parâmetro __*marcado*__:

Neste caso o conteúdo do campo será a concatenação do número oficial do Bem \(coluna NUM\_OFICIAL\_CIAP\) com o código do estabelecimento de origem do Bem \(coluna COD\_ESTAB\_ORIGEM\) e o ano da aquisição do Bem, no formato: 

                 \[ Número \+ ‘\-‘ \+ código estabelecimento \+ ‘/’ \+ ano da aquisição \], exemplo: 0000551\-EST01/2012\.  

Este mesmo procedimento é feito na emissão do livro para geração por inscrição estadual única\.

__Data__ – DAT\_OPER

__Nota Fiscal__ – concatenação das colunas: NUM\_DOCFIS, SERIE\_DOCFIS e SUB\_SERIE\_DOCFIS

__Descrição__ \- DSC\_BEM

__Entrada__ – Esta coluna será preenchida com o conteúdo de VLR\_CRED\_ICMS, mas apenas quando IND\_E\_S = “E”\. Quando se tratar de saídas \(IND\_E\_S = “S”\), a coluna não será preenchida\.

__Saída__ \- Esta coluna será preenchida com o conteúdo de VLR\_CRED\_ICMS, mas apenas quando IND\_E\_S = “S”\. Quando se tratar de entradas \(IND\_E\_S = “E”\), a coluna não será preenchida\.

__Total Crédito a Apropriar__ – esta coluna é a totalização do valor lançado nas colunas “Entrada” e “Saída” \(as entradas são somadas e as saídas subtraídas\)\.

__RN05 – Linhas de Total da Fração:__

Ao finalizar a impressão dos movimentos de uma determinada fração, serão demonstradas as linhas de resultado, conforme descrito a seguir:

No label “__Resultado do período referente aos Bens com apropriação em “nn” parcelas__”, o “nn” é a fração referente aos Bens que foram demonstrados\.

__Coeficiente das Saídas__ – O conteúdo deste campo será exatamente o coeficiente demonstrado no Quadro 3 do livro, na\(s\) linha\(s\) referente\(s\) ao período em questão\. A informação será recuperada da tabela dos totais do período \(APT\_DEM\_CR\_MENSAL\), na\(s\) linha\(s\) correspondente\(s\) ao Estabelecimento e período da geração\. Se existirem várias linhas \(de frações diferenciadas\), a informação poderá ser recuperada de qualquer uma das linhas, pois terá exatamente o mesmo conteúdo em todas elas \(trata\-se da coluna __COEFICIENTE__\)\.

__Total Crédito a Apropriar__ \- O conteúdo deste campo será exatamente o total do crédito a apropriar demonstrado no Quadro 3 do livro, na linha referente ao período __e fração em questão__\. Aqui, a recuperação da informação da tabela \(APT\_DEM\_CR\_MENSAL\) é feita da linha referente ao Estabelecimento, período __e fração__, pois cada fração terá o seu valor diferenciado dos demais \(trata\-se da coluna __VLR\_TOT\_APROPRIAR__\)\. 

OBS: Este valor recuperado da tabela será exatamente igual ao valor totalizado na última linha da coluna “__Total Crédito a Apropriar”__, da parte do relatório que demonstra o detalhamento das movimentações dos Bens da fração em questão\. Caso essa igualdade não aconteça, significa algum problema/erro na geração do relatório, que não estará demonstrando os Bens corretamente, da mesma forma feita no livro, ou ainda, algum problema na totalização das entradas e saídas\.

__Fração__ – Neste campo será demonstrada a fração em questão, no formato “1/nn” \(Ex: 1/24, 1/36, 1/48\)

__Crédito a Apropriar no Período__ – O conteúdo deste campo será exatamente o valor do crédito a apropriar no período demonstrado no Quadro 3 do livro, na linha referente ao período __e fração em questão__\. Aqui, a recuperação da informação da tabela \(APT\_DEM\_CR\_MENSAL\) é feita da linha referente ao Estabelecimento, período __e fração__, pois cada fração terá o seu valor diferenciado dos demais \(trata\-se da coluna __VLR\_TOT\_CREDITO__\)\.

= = = = = =

