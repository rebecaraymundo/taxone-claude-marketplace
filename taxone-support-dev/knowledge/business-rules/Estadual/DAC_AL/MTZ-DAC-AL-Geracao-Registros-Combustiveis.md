# MTZ-DAC-AL-Geracao-Registros-Combustiveis

- **Fonte:** MTZ-DAC-AL-Geracao-Registros-Combustiveis.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 88 KB

---

THOMSON REUTERS

Módulo DAC Alagoas 

Geração dos Registros de Combustíveis \(Varejo\) 

__Localização__: Menu Estadual, Módulo DAC\-AL, item <a id="OLE_LINK88"></a><a id="OLE_LINK89"></a><a id="OLE_LINK90"></a>Obrigações 🡪 Geração dos Registros

DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS30414__

Geração dos Registros de Combustíveis

A geração da DAC\-AL foi alterada para passar a gerar os registros de combustíveis da DAC\-AL\.

15/10/2019 

\(criação do documento\)

Sumário

[1\.	Regras Gerais	2](#_Toc22219023)

[2\.	Registro Tipo 70 \- Informações Mensais das Bombas de Combustível	3](#_Toc22219024)

[3\.	Registro Tipo 71\- Informações Mensais dos Bicos das Bombas de Combustível	4](#_Toc22219025)

[4\.	Registro Tipo 72 \- Informações Mensais dos Lacres das Bombas de Combustível	6](#_Toc22219026)

[5\.	Registro Tipo 73 \- Informações Mensais dos Encerrantes das Bombas de Combustível	7](#_Toc22219027)

[6\.	Registro Tipo 74 \- Informações Mensais de Estoque de Combustível	11](#_Toc22219028)

[7\.	Relatório de Conferência – Layout dos Registros de Combustíveis	13](#_Toc22219029)

# <a id="_Toc22219023"></a>Regras Gerais 

Este documento é específico da geração dos seguintes registros:

- Registro Tipo 70: Informações mensais das bombas de combustível;
- Registro Tipo 71: Informações mensais dos bicos das bombas de combustível;
- Registro Tipo 72: Informações mensais dos lacres das bombas de combustível;
- Registro Tipo 73: Informações mensais dos encerrantes das bombas dos revendedores varejistas de combustíveis;
- Registro Tipo 74: Informações mensais de estoque de combustível;

A geração destes registros foi desenvolvida na __MFS30414__, por solicitação do cliente __MAKRO__, chamado 18053/2019\.

Usuária: Brígida Carvalho, Contato: \(11\) 37452997

A geração destes registros é feita a partir das tabelas utilizadas no Sped Fiscal para gerar os registros de controle dos postos de combustível \(registros 1300 ao 1370\)\. Para a DAC\-AL, são utilizadas apenas as tabelas destacadas a seguir: 

\-SAFX2060\-Cadastro dos Tanques

\-SAFX2061\-Cadastro das Bombas \(\*\)

\-SAFX2062\-Cadastro dos Bicos

\-SAFX121\-Lacres das Bombas

\-SAFX122\-Tanques x Bicos \(\*\)

\-SAFX123\-Movimentação Diária por Tanque

\-SAFX124\-Vendas Diárias

\-SAFX125\-NF’s Entrada x Armazenamento

# <a id="_Toc350763252"></a><a id="_Toc22219024"></a>Registro Tipo 70 \- Informações Mensais das Bombas de Combustível

Origem dos dados: __SAFX2061__ \- Tabela de Cadastro das Bombas;

Neste registro serão informadas todas as Bombas de combustíveis com movimentação no período \(mês e ano informado na tela da geração\)\.

Critérios da recuperação dos dados da __SAFX2061__: 

- Empresa = código da empresa do login;
- Estabelecimento = código do estabelecimento selecionado para geração;
- Validade = para cada Bomba, será considerado sempre o registro de validade mais atual para o período \(maior data que seja <= data do primeiro dia do período da geração\);
- Somente Bombas com movimento no período \(serão consideradas *apenas* as Bombas que tenham movimento na __SAFX124__ \(Vendas Diárias\) para o período em questão\);

Para cada Bomba será gerado *um único registro 70* com as seguintes informações:

01

Tipo

= “__70__”

02

Número de Série da Bomba 

Campo “05\-Série” da SAFX2061

03

Nome do fabricante

Campo “06\-Fabricante” da SAFX2061 

Como na tabela o tamanho do campo \(80\) é superior ao do layout da DAC \(40\), a informação será truncada caso exceda o limite de 40 posições\. E nesse caso, será gerada a seguinte mensagem de aviso no log:

*“Registro 70: O tamanho do campo “Nome do Fabricante” excedeu o limite máximo de 40 posições no layout da DAC\. O registro foi gerado com a informação truncada\. Número da Bomba: 9999999999, Série: XXXXXXXXXXXX”\. *

04

Modelo da Bomba

Campo “07\-Modelo” da SAFX2061

05

Medição

Este campo é gerado a partir do campo “08\-Tipo de Medição” da SAFX2061, da seguinte forma:

Se campo *08\-Tipo de Medição* = “0” \(Analógico\)

      O campo será preenchido com “A”;

Se campo *08\-Tipo de Medição* = “1” \(Digital\)

      O campo será preenchido com “D”;

__Obs__\.: Este campo __não__ consta no layout do documento “LayoutNovaDacAbril2007” \(layout mais recente disponível no site da Sefaz\-AL\)\. Mas conforme testes realizados no programa da DAC\-AL, onde foi testada a importação de arquivos TXT de acordo com o layout, foi verificada a inclusão deste campo no TXT\.

  

# <a id="_Toc22219025"></a>Registro Tipo 71\- Informações Mensais dos Bicos das Bombas de Combustível

Origem dos dados: __SAFX122__ \- Tabela de Relacionamento Tanque x Bicos;

Neste registro serão informados todos os Bicos das Bombas, com a informação do Tanque de onde vem o combustível\. Serão considerados apenas os Bicos com movimentação no período \(mês e ano informado na tela da geração\)\.

Critérios da recuperação dos dados da __SAFX122__: 

- Empresa = código da empresa do login;
- Estabelecimento = código do estabelecimento selecionado para geração;
- Validade = para cada Bomba/Bico, será considerado sempre o registro de validade mais atual para o período \(maior data que seja <= data do primeiro dia do período da geração\);
- Somente Bombas/Bicos com movimento no período \(serão consideradas *apenas* as Bombas/Bicos que tenham movimento na __SAFX124__ \(Vendas Diárias\) para o período em questão\);

Para cada Bomba/Bico será gerado *um único registro 71* com as seguintes informações:

01

Tipo

= “__71__”

02

Número de Série da Bomba 

Este campo é gerado com a informação da Série da Bomba \(campo “05\-Série” da SAFX2061\), obtido na SAFX2061 através do número da Bomba \(campo “04\-Número da Bomba” da SAFX122\)\.

Para obter o registro do cadastro da Bomba na SAFX2061, será considerado o registro de validade mais atual para o período\. 

03

Número do Bico

Campo “05\-Número do Bico” da SAFX122 

Como na tabela o tamanho do campo \(10\) é superior ao do layout da DAC \(02\), caso o número do Bico na SAFX122 exceda dois dígitos, o registro *não* será gerado, e no log será gerada a seguinte mensagem de erro:

*“Registro 71: O tamanho do campo “Número do Bico” excedeu o limite máximo de 02 dígitos no layout da DAC\. O registro não foi gerado\. Número da Bomba: 999999999, Série: XXXXXXXXXXXX, Número do Bico: 999999999”\.  *

04

Código do Combustível

Campo “09\-Código do Combustível \(DAC\-AL\)” do cadastro do Tanque informado no campo 05\.

Para obter o registro do cadastro do Tanque na SAFX2060, será considerado o registro de *maior* data de validade, desde que não ultrapasse a data do primeiro dia do período\.

05

Número do Tanque

Campo “03\-Número do Tanque” da SAFX122\.

Como na tabela o tamanho do campo \(10\) é superior ao do layout da DAC \(02\), caso o número do Tanque na SAFX122 exceda dois dígitos, o registro *não* será gerado, e no log será gerada a seguinte mensagem de erro:

*“Registro 71: O tamanho do campo “Número do Tanque” excedeu o limite máximo de 02 dígitos no layout da DAC\. O registro não foi gerado\. Número do Tanque: 9999999999”\.*

# <a id="_Toc22219026"></a>Registro Tipo 72 \- Informações Mensais dos Lacres das Bombas de Combustível

Origem dos dados: __SAFX121__ \- Tabela dos Lacres das Bombas;

Neste registro serão informados todos os lacres das Bombas com movimentação no período \(mês e ano informado na tela da geração\)\.

Para cada Bomba, serão recuperados todos os lacres válidos para o período em questão\. Assim, poderá existir mais de um lacre por Bomba\.

\(Supondo por exemplo, que a Bomba inicie o mês com um determinado lacre, e no meio do período ocorra a troca do lacre\)

 

Critérios da recuperação dos dados da __SAFX121__: 

- Empresa = código da empresa do login;
- Estabelecimento = código do estabelecimento selecionado para geração;
- Validade = para cada Bomba, serão considerados todos os lacres utilizados no período, podendo retornar mais de um resultado, conforme descrito acima\. 

                A lógica no caso, é informar todos os lacres utilizados na Bomba no decorrer do mês em questão\. Ou seja, deve\-se considerar o lacre usado na 

                Bomba no primeiro dia do período, e também todos os lacres que possam ter sido trocados no decorrer no período\.

                Exemplo:

Bomba

Data do Lacre

Número do Lacre

1

20/11/2018

111

1

10/01/2019

112

1

30/01/2019

113

1

10/03/2019

114

- Para geração do mês 12/2018, seria gerado apenas o lacre __111 __\(de 20/11/2018\);
- Para geração do mês 01/2019, seriam gerados três lacres: __111__ \(de 20/11/2018\), o __112 __\(de 10/01/2019\), e o __113 __\(de 30/01/2019\);
- Para geração do mês 02/2019, seria gerado apenas o lacre __113 __\(de 30/01/2019\);
- Para geração do mês 03/2019, seriam gerados dois lacres: __113__ \(de 30/01/2019\) e o __114__ \(de 10/03/2019\);

 

- Somente Bombas com movimento no período \(serão consideradas *apenas* as Bombas que tenham movimento na __SAFX124__ \(Vendas Diárias\) para o período em questão\);

Para cada Bomba serão gerados um ou vários registros 72, conforme os lacres recuperados para a Bomba pela regra descrita acima, com as seguintes informações:

01

Tipo

= “__72__”

02

Número de Série da Bomba 

Este campo é gerado com a informação da Série da Bomba \(campo “05\-Série” da SAFX2061\), obtido na SAFX2061 através do número da Bomba \(campo “03\-Número da Bomba” da SAFX121\)\.

Para obter o registro do cadastro da Bomba na SAFX2061, será considerado o registro de validade mais atual para o período\. 

03

Número do Lacre

Campo “05\-Número do Lacre” da SAFX121 

Como na tabela o tamanho do campo \(20\) é superior ao do layout da DAC \(10\), caso o número do lacre na SAFX121 exceda 10 dígitos, o registro *não* será gerado, e no log será gerada a seguinte mensagem de erro:

*“Registro 72: O tamanho do campo “Número do Lacre” excedeu o limite máximo de 10 dígitos no layout da DAC\. O registro não foi gerado\. Número da Bomba: 999999999, Número do Lacre: XXXXXXXXXXXXXXXXX”\.  *

*\(Observar que na SAFX121 este campo é alfanumérico \(assim como no Sped\), mas na DAC o campo é numérico\)\.*

*   *

# <a id="_Toc22219027"></a>Registro Tipo 73 \- Informações Mensais dos Encerrantes das Bombas de Combustível

Origem dos dados: __SAFX124__ \- Tabela das Vendas Diárias;

Neste registro será informado o resumo mensal sobre a movimentação de cada Bomba/Bico\.

Para cada Bomba/Bico será gerado um registro 73 com os valores totalizados na movimentação do período\.

Critérios da recuperação dos dados da __SAFX124__: 

- Empresa = código da empresa do login;
- Estabelecimento = código do estabelecimento selecionado para geração;
- Data do Movimento = data enquadrada no período da geração;

Para cada Bomba/Bico será gerado *um único registro 73*, com as seguintes informações:

__Observação sobre os campos Volume com Intervenção” e “Volume sem Intervenção”:__

Durante testes de importação de arquivo realizados no programa da DAC\-AL, foi verificado que somente um dos campos de volume deve ser preenchido\. E o programa só aceita um registro 73 por Bomba/Bico\. Desta forma, foi alinhado com o cliente Makro que o volume do mês seria apurado normalmente, e o resultado lançado em “Volume sem Intervenção”, se no mês não houver nenhuma intervenção, ou em “Volume com Intervenção” se no mês tiver alguma intervenção\. 

01

Tipo

= “__73__”

02

Número de Série da Bomba 

Este campo é gerado com a informação da Série da Bomba \(campo “05\-Série” da SAFX2061\), obtido na SAFX2061 através do número da Bomba \(campo “04\-Número da Bomba” da SAFX124\)\.

Para obter o registro do cadastro da Bomba na SAFX2061, será considerado o registro de validade mais atual para o período\. 

03

Número do Bico

Campo “05\-Número do Bico” 

Como na tabela o tamanho do campo \(10\) é superior ao do layout da DAC \(02\), caso o número do Bico na SAFX124 exceda dois dígitos, o registro *não* será gerado, e no log será gerada a seguinte mensagem de erro:

*“Registro 73: O tamanho do campo “Número do Bico” excedeu o limite máximo de 02 dígitos no layout da DAC\. O registro não foi gerado\. Número da Bomba: 999999999, Série: XXXXXXXXXXXX, Número do Bico: 999999999”\.  *

04

Leitura inicial do bico

Este campo é gerado com a quantidade da primeira leitura efetuada na Bomba/Bico no período\.

Campo: “12\-Contador Inicial”

Será considerado o contador inicial do registro de *menor* data do período \(normalmente, será o dia 01\)\.

Quando existir mais de um registro na menor data, será considerado o de *menor sequencial* \(campo 06\-Sequencial\)\.

Obs\.: Observar que a SAFX124 tem o campo Sequencial justamente para permitir ‘n’ registros num mesmo dia para a mesma Bomba/Bico\. Isso pode ocorrer por exemplo, quando há uma intervenção na Bomba\.

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

05

Leitura final do bico

Este campo é gerado com a quantidade da última leitura efetuada na Bomba/Bico no período\.

Campo: “13\-Contador Final”

Será considerado o contador final do registro de *maior* data do período \(normalmente, será o dia 30 ou 31\)\.

Quando existir mais de um registro na maior data, será considerado o de *maior sequencial* \(campo 06\-Sequencial\)\.

Obs\.: Observar que a SAFX124 tem o campo Sequencial justamente para permitir ‘n’ registros num mesmo dia para a mesma Bomba/Bico\. Isso pode ocorrer por exemplo, quando há uma intervenção na Bomba\.

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

06

Volume sem Intervenção

Este campo é gerado através da totalização do volume de saídas da Bomba/Bico, de todos os dias do período:

Para cada movimento da SAFX124, será calculado o volume:

                                   \(*“13\-Contador Final”* – *“12\-Contador Inicial”* – *“14\-Aferição”\)*

O total do volume do período será a soma do resultado de todos os dias\.

O resultado obtido será gravado no campo “*06\-Volume sem Intervenção*” __ou__ no campo “*07\-Volume com Intervenção*”, dependendo se no período houve alguma intervenção na Bomba/Bico ou não\.

__Se__ existir algum movimento no período com o campo “*07\-Número da Intervenção*” *preenchido*:

      Neste caso, houve intervenção, então os campos serão gerados da seguinte forma:

      Campo “*06\-Volume sem Intervenção*” = zeros;

      Campo “*07\-Volume com Intervenção*” = Total do volume apurado;

__Senão__

      Neste caso, *não* houve intervenção, então os campos serão gerados da seguinte forma:

      Campo “*06\-Volume sem Intervenção*” = Total do volume apurado;

      Campo “*07\-Volume com Intervenção*” = zeros;

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

07

Volume com Intervenção

Ver regra do campo “*06\-Volume sem Intervenção*”\.

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

08

Número do novo lacre

Neste campo é informado o número do lacre mais recente da bomba\.

O campo é gerado com a informação do número do lacre \(campo “05\-Número do Lacre” da SAFX121\), obtido na SAFX121 através do número da Bomba em questão\.

Para obter o registro do lacre na SAFX121 \(Tabelas dos Lacres das Bombas\), será considerado o lacre de maior data, desde que não ultrapasse o período em questão\.

09

Total de aferições

Total da quantidade do campo “14\-Aferições” de todas as vendas do mês

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

10

Total de perda/ganho de

combustível

Total da perda ou ganho no período\. 

Este valor é apurado através da totalização dos campos “*16\-Perdas*” e “*17\-Ganhos*” das vendas do período\.

O resultado final será = Total Ganhos – Total Perdas 

   \- Se resultado positivo 🡪 trata\-se de um ganho, assim o campo será gerado com o valor positivo;

   \- Se resultado negativo 🡪> trata\-se de uma perda, assim, o campo será gerado com o valor negativo;

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

# <a id="_Toc22219028"></a>Registro Tipo 74 \- Informações Mensais de Estoque de Combustível

Origem dos dados: __SAFX123__ – Movimentação Diária por Tanque;

Neste registro será informado o resumo mensal sobre a movimentação de Tanque\. Para cada Tanque será gerado um registro 74 com os valores totalizados na movimentação do período\.

Critérios da recuperação dos dados da __SAFX123__: 

- Empresa = código da empresa do login;
- Estabelecimento = código do estabelecimento selecionado para geração;
- Data do Movimento = data enquadrada no período da geração;

Para cada Tanque será gerado *um único registro 74*, com as seguintes informações:

__Obs__\.: No layout do documento “LayoutNovaDacAbril2007” \(layout mais recente disponível no site da Sefaz\-AL\), o campo “*03\-Código do Combustível*” ocuparia das posições 05 a 07 \(vide coluna ”Posição”\)\. No entanto, este campo é numérico de 2 posições, e portanto, ocupa apenas da posição 05 a 06\. Desta forma, o registro 74 tem em seu layout 36 posições, e não 37 conforme consta no layout\. Durante testes de importação de arquivo realizados no programa da DAC\-AL,  o registro 74 foi importado normalmente desta forma \(com apenas 36 posições na linha\)\.

01

Tipo

= “__74__”

02

Número do Tanque 

 Campo “04\-Número do Tanque” da SAFX123\.

Como na tabela o tamanho do campo \(10\) é superior ao do layout da DAC \(02\), caso o número do Tanque na SAFX123 exceda dois dígitos, o registro *não* será gerado, e no log será gerada a seguinte mensagem de erro:

*“Registro 74: O tamanho do campo “Número do Tanque” excedeu o limite máximo de 02 dígitos no layout da DAC\. O registro não foi gerado\. Número do Tanque: 999999999”\.  *

03

Código do Combustível

Campo “09\-Código do Combustível \(DAC\-AL\)” do cadastro do Tanque \(SAFX2060\)\.

Para obter o registro do cadastro do Tanque na SAFX2060, será considerado o registro de *maior* data de validade, desde que não ultrapasse a data do primeiro dia do período\.

04

Estoque de Abertura

Este campo é gerado com a quantidade do estoque de combustível no Tanque *no início do período*\.

Será o conteúdo do campo “05\-Estoque Inicial” do registro de *menor* data do período \(normalmente, será o dia 01\)\.

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

05

Estoque de Fechamento

Este campo é gerado com a quantidade do estoque de combustível no Tanque *no final do período*\.

Esta quantidade é apurada com base no registro de *maior data do período *\(normalmente, será o dia 30 ou 31\), da seguinte forma:

Campo “*05\-Estoque Inicial*”

__\+__

\(Campo “*06\-Entradas*” __\+__ campo “*09\-Ganhos*”\)

__\-__

\(Campo “*07\-Saídas*” __\+ __campo “*08\-Perdas*”\)

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

06

Volume Recebido

Este campo é gerado com o resultado da totalização do campo “*06\-Entradas*”, de todos os dias do período\.

__Obs__\.: Este campo deve ser gerado com apenas 2 casas decimais \(esta é a quantidade de casas decimais tratadas no programa da DAC\-AL, para as quantidades dos registros 73 e 74\)\. 

# <a id="_Toc22219029"></a>Relatório de Conferência – Layout dos Registros de Combustíveis 

Layout das linhas do relatório de conferência \(aba “Relatório”\) referentes aos registros 70, 71, 72, 73, 74 e 75:

__Tipo    Série Bomba                                    Fabricante                                                          Modelo            \. __

  70      XXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXX

__Tipo    Série Bomba       Bico     Código do Combustível      Número do Tanque__

  71      XXXXXXXXXXXX      99                          99                                             99

__Tipo    Série Bomba       Número do Lacre__

  72      XXXXXXXXXXXX         XXXXXXXXXX

__Tipo    Série Bomba    Bico     Leitura Ini     Leitura Fim    Volume S/Interv\.   Volume C/Interv\.   Número doLacre     Aferições      Perda/Ganho__

  73      XXXXXXXXXXXX   99     99\.999\.999,99    99\.999\.999,99        99\.999\.999,99           99\.999\.999,99              XXXXXXXXXX      99\.999\.999,99    99\.999\.999,99

__Tipo    Número do Tanque   Código do Combustível    Estoque de Abertura    Estoque de Fechamento    Volume Recebido__

  74                      99                                        99                                  99\.999\.999,99                         99\.999\.999,99                     99\.999\.999,99     

= = = = = =

 

