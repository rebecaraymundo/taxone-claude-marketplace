# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_RS

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_RS.docx
- **Modificado:** 2025-02-06
- **Tamanho:** 127 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- RS

__Localização__: 

##### DOCUMENTO DE REQUISITO

__*Data*__

__*Demanda*__

__Descrição__

__Responsável__

16/12/2016

MFS8625

Alteração na geração do registro 1400 para o estado do RS: geração automática dos códigos 01, 02, 03 e 05\.

Vânia Mattos

29/09/2023

MFS436036

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

Liliane Assaf

03/02/2025

MFS710626

Inclusão do modelo 66 na regra do código 02 – Energia Elétrica \(Distribuição\);

Graciela Soares

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração – Específico por UF<a id="_Toc75782998"></a> – RS

__RN1400\-RS__

__*MFS7944*__*: Alterou a geração do 1400 para tratar o RS conforme regras específicas\. A princípio, todos os códigos serão gerados somente a partir da manutenção\.*

__*MFS8625*__*: Alterou a geração do 1400 p/gerar de forma automática os códigos 01, 02, 03 e 05\.*

A geração do 1400 para a modalidade “RS” é feita de acordo com os códigos específicos da tabela do RS \(*Tabela de Itens UF Índice de Participação dos Municípios *\)\. 

*\(Obs: Até a MFS7944 não existe ato legal específico com orientações a respeito\)*

Os tipos de operação solicitados são os seguintes, conforme os códigos da tabela específica do RS:

01\-Transporte: serviço de transporte por município de origem deste Estado;

02\-Energia Elétrica: distribuição de energia elétrica em cada município;

03\-Comunicação:  prestação de serviços de comunicação em cada município;

05\-Vendas fora do Estabelecimento;

06\-Energia Elétrica \- geração de energia elétrica produzida em município distinto;

09\-Regime Especial;

As regras estão organizadas da seguinte forma:

__RN1400\-RS\-01__ – geração para o código 01;

__RN1400\-RS\-02__ – geração para o código 02;

__RN1400\-RS\-03__ – geração para o código 03;

__RN1400\-RS\-05__ – geração para o código 05;

__RN1400\-RS\-06__ – geração para o código 06;

__RN1400\-RS\-09__ – geração para o código 09;

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-RS\-01__

__Código 01 \- Transportes  __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Alteração __MFS8625__: desenvolveu a geração automática p/o código 01\.

Alteração __CH13531\_2017 \- MFS12315__:  tratamento das deduções, que conforme o setor de Informação \(item 7 do chamado\) precisamos prever a dedução das aquisições de serviço\.

__OBS__: A geração deste código é feita de forma semelhante ao código 23 de SP \(__SPDIPAM23__\), onde para os conhecimentos \(classificação 4, 5 ou 6\) é utilizado o município de origem da SAFX07, __ou__, o município de coleta da SAFX51, caso o município de origem da capa não esteja preenchido\. A diferença é que o código SPDIPAM23 utiliza uma parametrização de produtos \(parametrização especifica da GIA de SP\) que __não__ é utilizada para este código do RS\.

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem do transporte\.

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no __D100__ que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S = ‘9’ \(somente saídas\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  __7, 8, 8B, 9, 10, 11, 26, 27 ou 57 __\(modelos gravados no D100\)

\- Situação = somente as não canceladas

\- Notas com ou sem itens 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no

   Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__01__”

\- Classificação = __1, 3, 4, 5 ou 6__ 

 \(a nf de modelo 07 usa classificação 1/3 e os conhecimentos classificação 4, 5 ou 6\)

\- No caso das notas de __classificação 1 ou 3__ à serão consideradas apenas as notas

  em que o município de origem \(município onde ocorreu o início da prestação do

  serviço\) seja do RS \(campos 117\-UF Origem e 182\-Município Origem da SAFX07\);

\- No caso das notas de __classificação 4, 5 ou 6__ à serão consideradas apenas as

   notas em que em que o município de origem da SAFX07 seja do RS __ou__, quando

   este não for informado,  o município da coleta na SAFX51 seja do RS \(campos 

   62\-UF Coleta e 42\-Município Coleta da SAFX51\);   

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\-Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\. 

O município utilizado no agrupamento será o município de origem da NF __ou__ o município de coleta dos itens de frete \(X51\), quando se tratar de notas de frete \(classificação 4/5/6\), conforme descrito acima na regra da recuperação dos dados\.

Valor a ser totalizado:

\- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64, SAFX08\) ou valor

   total da nota \(SAFX07\), no caso das notas sem itens;

\- Notas de classificação 4, 5 ou 6 \(a nota não terá itens\)  à valor total da nota 

  \(SAFX07\);

*Obs: Os CTRC’s têm a classificação 4, 5 ou 6, e não têm itens na SAFX08\. Os seus itens ficam na SAFX51, e se referem aos dados das notas fiscais das mercadorias carregadas\. Desta forma, o valor do serviço de transporte é sempre o valor da capa \(SAFX07\), pois os valores da SAFX51 são os valores das notas do carregamento\.*

Sobre o município de coleta dos itens de frete \(SAFX51\): 

Ao utilizar o município de coleta da SAFX51, caso exista mais de um item de frete para o mesmo documento, e eles tiverem municípios de coleta *diferentes*, será gravada a seguinte mensagem no log, e o documento *não* será considerado:* “Existem na base de dados itens de frete para o documento com mais de um município de coleta\. O documento não será considerado p/o registro 1400, código 01”\. *Caso o município da SAFX51 também não esteja preenchido, será gravada a seguinte mensagem no log, e o documento *não* será considerado: *“Para gerar o registro 1400, cód 01, é necessário que o município de origem esteja preenchido \(UF/munic origem da SAFX07 ou munic Coleta da SAFX51\)\. O documento não será considerado”\.*

Exemplo:

Nota fiscal: 25107

Classificação: 4 \(CTRC\)

CFOP: 5106

Município origem: Buri

Valor da Nota: 1\.000,00

Itens da X51: 1\-Município coleta: Pederneiras, Valor = 800,00; 

                      2\-Município coleta: Pederneiras, Valor = 200,00;

Neste cenário seria usado o município de origem da capa \(= Buri\)\.

Mas, se na capa o município de origem não estivesse preenchido, seria usado o município de Pederneiras;

__Apuração dos valores a serem deduzidos:     \(CH13531\_2017 \- MFS12315\)__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP\) 

\- Somente as notas em que a “*UF Origem*” da nota = “RS”;

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__01 \(Transportes\)__”

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município *de origem da nota* \(SAFX07\), utilizando os seguintes valores:

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__01__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__01__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\-\) 

                                 \[Valor resultante das deduções\]

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-RS\-02__

__Código 02 – Energia Elétrica \(Distribuição\)  __

Alteração __MFS8625__: desenvolveu a geração automática p/o código 02\.

Alteração__ MFS20147__: altera critério de recuperação das notas fiscais utilizando o filtro de CFOP ou CFOP/Natureza e inclui tratativa para exclusão dos itens sem receita por Operação, CST e Produto ou Operação e CST, assim como, regra especificada na geração padrão para EE/Telecom/Água que é feita por CST ou Produto\.

__\[MFS710626\] __Inclusão do modelo de nota “66”

<a id="_Hlk72402275"></a>Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 	

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do RS\. 

*\(A geração deste código não trabalha com deduções automáticas, pois não existe ainda nenhum ato legal com esclarecimentos sobre os códigos do RS\. Assim, para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\)*

<a id="_Hlk72402313"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos  C500, C600 ou C700 para o segmeno de energia elétrica\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “06 ou 66”

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “__RS__”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__02__”;

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

<a id="_Hlk72402354"></a>__Totalização das Notas recuperadas da SAFX42/SAFX43:__

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

Valor a ser totalizado à valor do serviço do item \(campo “19\-Valor do Serviço” da SAFX43\)

__MFS35568__: A totalização das notas recuperadas passou a ser feita da seguinte forma: deve somar o Valor do Serviço dos itens de adição, e subtrair o Valor do Desconto dos itens de dedução, da seguinte forma:

	

Valor a ser totalizado = 

       Se item de adição, soma o __valor do serviço__ \(campo 19 SAFX43\);

       Se item de dedução, subtrai o __valor do desconto__ \(campo 18 da SAFX43\); 

        *\(ao subtrair o valor do desconto, considerar sempre o valor absoluto\)*

\(Itens de __adição__ são os itens com o campo “20\-Adição/Desconto” __nulo__ ou = “__A__”\);

\(Itens de __dedução__ são os itens com o campo “20\-Adição/Desconto” = “__D__”\);

Exemplo: supondo as notas abaixo para um mesmo município do ponto de Consumo:

   Nota 101: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 1\.000,00

                    Item 2, Adição/ Desc\. = “__A__”, Valor do Serviço = 500,00

   Nota 102: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 2\.000,00

                    Item 2, Adição/ Desc\. = “__D__”, Valor do Desconto = 300,00

   Valor totalizado = __3\.200,00__ \(1\.000,00 \+ 500,00 \+ 2\.000,00 – 300,00\)

__MFS20147:__ Essa alteração se faz necessária por conta de alguns critérios adotados pela CPFL, segue:

- Utilização de CST 090 para operações que não possuem fato gerador do ICMS \(CIP, Seguros, Juros, Multa, Atualização Monetária, etc\) e que precisam ser desconsiderados da composição do valor adicionado das operações que ocorrem fato gerador, pois não há legislação que determina uma situação tributária específica para esse cenário fiscal e pode acontecer com qualquer contribuinte que possui atividades ativas com energia elétrica, água e telecomunicaçãoes, porque são segmentos que não possuem cobranças, em Nota Fiscal, ausentes à sua operação, ou seja, não existem documentos de entrada escriturados para deduzir as saídas\.

__Exclusão__

__Alterada \[MFS30891\]__

Para cada combinação de produto e município ou somente município conforme totalização a seguir, se houver parametrização de operação e CST na tela de “Exclusão de Itens sem Receita – Por CST x Operação”, do módulo SPED à EFD\-Escrituração Fiscal Digital, item de menu: Parâmetros >> Registro 1400 >> Específico por UF >> Exclusão Itens S/ Receita >> Por CST x Operação, então:

- Nesse cenário em específico desconsiderar os itens de serviço na composição do valor da totalização\.

*Exemplo:*

NF 100

Município do Ponto de Consumo = RS 14902 \(PORTO ALEGRE\)

Item 1

Produto A

__CST 90__

Adição/ Desc\. = Adição

Valor do Serviço = 300,00

Item 2

Produto B

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 50,00

NF 101

Município do Ponto de Consumo = RS 14902 \(PORTO ALEGRE\)

Item 1

Produto A

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 200,00

Paramêtro de Exclusão = __Operação 02\-Energia Elétrica \(Distribuição\) __e __CST 90 __

*Totalização = *

*|1400|02|4314902|250,00| \(se for valor negativo ou 0 desconsiderar do arquivo, para valor negativo será emitida a mensagem de log descrita nessa RN\)*

__MFS35568: __Desfaz o procedimento abaixo, implementado pela __MFS30891__, onde o valor do campo Desconto dos itens de dedução era subtraído do total das notas, com base na parametrização por CST e Produto \(menu “Dedução à Por CST x Produto”\)\. Esta parametrização *foi retirada do módulo*, e a dedução do Desconto dos itens de dedução passou a ser feita no junto com a totalização das notas, ou seja, a partir das próprias notas processadas \(vide regra acima, item “Totalização das Notas Recuperadas”\)\. 

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__02__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__02__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                     \[Valor resultante da totalização\] 

                                                       \(\+\)

                        \[Campo “Outros Valores” informado manualmente\]

                                                        \(\-\) 

                       \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\) e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-RS\-03__

__Código 03 \- Comunicação  __

Alteração __MFS8625__: desenvolveu a geração automática p/o código 03\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 	

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do RS\. 

*\(A geração deste código não trabalha com deduções automáticas, pois não existe ainda nenhum ato legal com esclarecimentos sobre os códigos do RS\. Assim, para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\)*

__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos de Telecom \(D500/D600/D700\)\)

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “21” ou “22” ou ‘62’

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__03__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__03__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                     \[Valor resultante da totalização\] 

                                                       \(\+\)

                        \[Campo “Outros Valores” informado manualmente\]

                                                        \(\-\) 

                       \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\) e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-RS\-05__

__Código 05 – Vendas Fora do Estabelecimento  __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Alteração __MFS8625__: desenvolveu a geração automática p/o código 05\.

*Obs: Neste tipo de operação a empresa emite uma nota fiscal para a remessa da mercadoria a ser vendida \(para acobertar a saída da mercadoria do estabelecimento\), e depois, ao efetuar cada venda, emite uma nota fiscal de venda fora do estabelecimento \(CFOP 5103/5104\)\. No retorno ao estabelecimento, caso tenha mercadorias não vendidas, emite uma nova nota para acobertar o retorno destas mercadorias\. A ideia é que o usuário parametrize as notas das vendas realizadas, que deve ter a indicação do município onde foi efetuada a venda\.*

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no __C100__ que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente saídas \(MOVTO\_E\_S= “__9__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no  

   menu “Parâmetros à  Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat” 

   para a operação do tipo “__05__” 

\- O município de destino da nota \(campos 122\-UF Destino e 183\-Município Destino da 

   SAFX07\) deve ser um município da UF do Estabelecimento

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município de destino__ \(campo 183 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__05__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__05__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                       \(\-\) 

               \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\)\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-RS\-06__

<a id="OLE_LINK185"></a><a id="OLE_LINK186"></a><a id="OLE_LINK187"></a>__Código 06 – Energia Elétrica \(Geração\)  __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__06__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__06__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-RS\-09__

__Código 09 – Regime Especial  __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__09__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__09__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-RS__

__*MFS7944*__*: Alterou a geração do 1400 para tratar o RS conforme regras específicas\. A princípio, todos os códigos serão gerados somente a partir da manutenção\.*

__*MFS8625*__*: Alterou a geração do 1400 p/gerar de forma automática os códigos 01, 02, 03 e 05\.*

A geração do 1400 para a modalidade “RS” é feita de acordo com os códigos específicos da tabela do RS \(*Tabela de Itens UF Índice de Participação dos Municípios *\)\. 

*\(Obs: Até a MFS7944 não existe ato legal específico com orientações a respeito\)*

Os tipos de operação solicitados são os seguintes, conforme os códigos da tabela específica do RS:

01\-Transporte: serviço de transporte por município de origem deste Estado;

02\-Energia Elétrica: distribuição de energia elétrica em cada município;

03\-Comunicação:  prestação de serviços de comunicação em cada município;

05\-Vendas fora do Estabelecimento;

06\-Energia Elétrica \- geração de energia elétrica produzida em município distinto;

09\-Regime Especial;

As regras estão organizadas da seguinte forma:

__RN1400\-RS\-01__ – geração para o código 01;

__RN1400\-RS\-02__ – geração para o código 02;

__RN1400\-RS\-03__ – geração para o código 03;

__RN1400\-RS\-05__ – geração para o código 05;

__RN1400\-RS\-06__ – geração para o código 06;

__RN1400\-RS\-09__ – geração para o código 09;

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-RS\-01__

__Código 01 \- Transportes  __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Alteração __MFS8625__: desenvolveu a geração automática p/o código 01\.

Alteração __CH13531\_2017 \- MFS12315__:  tratamento das deduções, que conforme o setor de Informação \(item 7 do chamado\) precisamos prever a dedução das aquisições de serviço\.

__OBS__: A geração deste código é feita de forma semelhante ao código 23 de SP \(__SPDIPAM23__\), onde para os conhecimentos \(classificação 4, 5 ou 6\) é utilizado o município de origem da SAFX07, __ou__, o município de coleta da SAFX51, caso o município de origem da capa não esteja preenchido\. A diferença é que o código SPDIPAM23 utiliza uma parametrização de produtos \(parametrização especifica da GIA de SP\) que __não__ é utilizada para este código do RS\.

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem do transporte\.

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no __D100__ que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S = ‘9’ \(somente saídas\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  __7, 8, 8B, 9, 10, 11, 26, 27 ou 57 __\(modelos gravados no D100\)

\- Situação = somente as não canceladas

\- Notas com ou sem itens 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no

   Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__01__”

\- Classificação = __1, 3, 4, 5 ou 6__ 

 \(a nf de modelo 07 usa classificação 1/3 e os conhecimentos classificação 4, 5 ou 6\)

\- No caso das notas de __classificação 1 ou 3__ à serão consideradas apenas as notas

  em que o município de origem \(município onde ocorreu o início da prestação do

  serviço\) seja do RS \(campos 117\-UF Origem e 182\-Município Origem da SAFX07\);

\- No caso das notas de __classificação 4, 5 ou 6__ à serão consideradas apenas as

   notas em que em que o município de origem da SAFX07 seja do RS __ou__, quando

   este não for informado,  o município da coleta na SAFX51 seja do RS \(campos 

   62\-UF Coleta e 42\-Município Coleta da SAFX51\);   

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\-Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\. 

O município utilizado no agrupamento será o município de origem da NF __ou__ o município de coleta dos itens de frete \(X51\), quando se tratar de notas de frete \(classificação 4/5/6\), conforme descrito acima na regra da recuperação dos dados\.

Valor a ser totalizado:

\- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64, SAFX08\) ou valor

   total da nota \(SAFX07\), no caso das notas sem itens;

\- Notas de classificação 4, 5 ou 6 \(a nota não terá itens\)  à valor total da nota 

  \(SAFX07\);

*Obs: Os CTRC’s têm a classificação 4, 5 ou 6, e não têm itens na SAFX08\. Os seus itens ficam na SAFX51, e se referem aos dados das notas fiscais das mercadorias carregadas\. Desta forma, o valor do serviço de transporte é sempre o valor da capa \(SAFX07\), pois os valores da SAFX51 são os valores das notas do carregamento\.*

Sobre o município de coleta dos itens de frete \(SAFX51\): 

Ao utilizar o município de coleta da SAFX51, caso exista mais de um item de frete para o mesmo documento, e eles tiverem municípios de coleta *diferentes*, será gravada a seguinte mensagem no log, e o documento *não* será considerado:* “Existem na base de dados itens de frete para o documento com mais de um município de coleta\. O documento não será considerado p/o registro 1400, código 01”\. *Caso o município da SAFX51 também não esteja preenchido, será gravada a seguinte mensagem no log, e o documento *não* será considerado: *“Para gerar o registro 1400, cód 01, é necessário que o município de origem esteja preenchido \(UF/munic origem da SAFX07 ou munic Coleta da SAFX51\)\. O documento não será considerado”\.*

Exemplo:

Nota fiscal: 25107

Classificação: 4 \(CTRC\)

CFOP: 5106

Município origem: Buri

Valor da Nota: 1\.000,00

Itens da X51: 1\-Município coleta: Pederneiras, Valor = 800,00; 

                      2\-Município coleta: Pederneiras, Valor = 200,00;

Neste cenário seria usado o município de origem da capa \(= Buri\)\.

Mas, se na capa o município de origem não estivesse preenchido, seria usado o município de Pederneiras;

__Apuração dos valores a serem deduzidos:     \(CH13531\_2017 \- MFS12315\)__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP\) 

\- Somente as notas em que a “*UF Origem*” da nota = “RS”;

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__01 \(Transportes\)__”

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município *de origem da nota* \(SAFX07\), utilizando os seguintes valores:

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__01__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__01__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\-\) 

                                 \[Valor resultante das deduções\]

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-RS\-02__

__Código 02 – Energia Elétrica \(Distribuição\)  __

Alteração __MFS8625__: desenvolveu a geração automática p/o código 02\.

Alteração__ MFS20147__: altera critério de recuperação das notas fiscais utilizando o filtro de CFOP ou CFOP/Natureza e inclui tratativa para exclusão dos itens sem receita por Operação, CST e Produto ou Operação e CST, assim como, regra especificada na geração padrão para EE/Telecom/Água que é feita por CST ou Produto\.

__\[MFS710626\] __Inclusão do modelo de nota “66”

Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 	

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do RS\. 

*\(A geração deste código não trabalha com deduções automáticas, pois não existe ainda nenhum ato legal com esclarecimentos sobre os códigos do RS\. Assim, para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\)*

__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos  C500, C600 ou C700 para o segmeno de energia elétrica\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “06 ou 66”

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “__RS__”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__02__”;

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Totalização das Notas recuperadas da SAFX42/SAFX43:__

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

Valor a ser totalizado à valor do serviço do item \(campo “19\-Valor do Serviço” da SAFX43\)

__MFS35568__: A totalização das notas recuperadas passou a ser feita da seguinte forma: deve somar o Valor do Serviço dos itens de adição, e subtrair o Valor do Desconto dos itens de dedução, da seguinte forma:

	

Valor a ser totalizado = 

       Se item de adição, soma o __valor do serviço__ \(campo 19 SAFX43\);

       Se item de dedução, subtrai o __valor do desconto__ \(campo 18 da SAFX43\); 

        *\(ao subtrair o valor do desconto, considerar sempre o valor absoluto\)*

\(Itens de __adição__ são os itens com o campo “20\-Adição/Desconto” __nulo__ ou = “__A__”\);

\(Itens de __dedução__ são os itens com o campo “20\-Adição/Desconto” = “__D__”\);

Exemplo: supondo as notas abaixo para um mesmo município do ponto de Consumo:

   Nota 101: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 1\.000,00

                    Item 2, Adição/ Desc\. = “__A__”, Valor do Serviço = 500,00

   Nota 102: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 2\.000,00

                    Item 2, Adição/ Desc\. = “__D__”, Valor do Desconto = 300,00

   Valor totalizado = __3\.200,00__ \(1\.000,00 \+ 500,00 \+ 2\.000,00 – 300,00\)

__MFS20147:__ Essa alteração se faz necessária por conta de alguns critérios adotados pela CPFL, segue:

- Utilização de CST 090 para operações que não possuem fato gerador do ICMS \(CIP, Seguros, Juros, Multa, Atualização Monetária, etc\) e que precisam ser desconsiderados da composição do valor adicionado das operações que ocorrem fato gerador, pois não há legislação que determina uma situação tributária específica para esse cenário fiscal e pode acontecer com qualquer contribuinte que possui atividades ativas com energia elétrica, água e telecomunicaçãoes, porque são segmentos que não possuem cobranças, em Nota Fiscal, ausentes à sua operação, ou seja, não existem documentos de entrada escriturados para deduzir as saídas\.

__Exclusão__

__Alterada \[MFS30891\]__

Para cada combinação de produto e município ou somente município conforme totalização a seguir, se houver parametrização de operação e CST na tela de “Exclusão de Itens sem Receita – Por CST x Operação”, do módulo SPED à EFD\-Escrituração Fiscal Digital, item de menu: Parâmetros >> Registro 1400 >> Específico por UF >> Exclusão Itens S/ Receita >> Por CST x Operação, então:

- Nesse cenário em específico desconsiderar os itens de serviço na composição do valor da totalização\.

*Exemplo:*

NF 100

Município do Ponto de Consumo = RS 14902 \(PORTO ALEGRE\)

Item 1

Produto A

__CST 90__

Adição/ Desc\. = Adição

Valor do Serviço = 300,00

Item 2

Produto B

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 50,00

NF 101

Município do Ponto de Consumo = RS 14902 \(PORTO ALEGRE\)

Item 1

Produto A

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 200,00

Paramêtro de Exclusão = __Operação 02\-Energia Elétrica \(Distribuição\) __e __CST 90 __

*Totalização = *

*|1400|02|4314902|250,00| \(se for valor negativo ou 0 desconsiderar do arquivo, para valor negativo será emitida a mensagem de log descrita nessa RN\)*

__MFS35568: __Desfaz o procedimento abaixo, implementado pela __MFS30891__, onde o valor do campo Desconto dos itens de dedução era subtraído do total das notas, com base na parametrização por CST e Produto \(menu “Dedução à Por CST x Produto”\)\. Esta parametrização *foi retirada do módulo*, e a dedução do Desconto dos itens de dedução passou a ser feita no junto com a totalização das notas, ou seja, a partir das próprias notas processadas \(vide regra acima, item “Totalização das Notas Recuperadas”\)\. 

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__02__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__02__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                     \[Valor resultante da totalização\] 

                                                       \(\+\)

                        \[Campo “Outros Valores” informado manualmente\]

                                                        \(\-\) 

                       \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\) e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

