# MTZ_EFD_Pre_Geracao_Registro_1400_ES

- **Fonte:** MTZ_EFD_Pre_Geracao_Registro_1400_ES.docx
- **Modificado:** 2026-01-28
- **Tamanho:** 92 KB

---

THOMSON REUTERS

                                                                                     __Módulo Sped Fiscal__

__  __

__		Pré\-Geração do Registro 1400 \(ES – Espírito Santo\)__

__Localização__: Menu Sped, Módulo EFD \- Escrituração Fiscal Digital, item Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF – __\(UF = Espírito Santo\)__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS__698113__

Ajuste dos códigos automáticos da UF ES para geração Anual

Processo de pré\-geração para o registro 1400 de ES para os códigos __ESIPM13005, ESIPM20009, ESIPM30011 e ESIPM43015 __que serão entregues anualmente\.

17/01/2025

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta geração foi criada na MFS698113, com objetivo de fazer a geração dos dados de registro 1400 para ES, em processo automático dos códigos __ESIPM13005, ESIPM20009, ESIPM30011 e ESIPM43015 __que a partir de 2025 passou a ser entregue anualmente\. 

A geração automática irá considerar apenas as operações referentes aos itens descritos abaixo\. Os demais itens constantes na relação de novos códigos não terão geração automática, e para informar seus valores, o usuário poderá utilizar a tela manutenção do registro 1400 \(campo “Valores Informados”\)\.   

- ESIPM13005 \(DISTRIBUIÇÃO DE ENERGIA ELÉTRICA\) antigo ESIPM05 \- Valor da energia elétrica distribuída a cada município, deduzidas as compras de energia elétrica, inclusive a transmissão, observando, no que couber, os valores de acordo com os critérios dos CFOPs dispostos em Manual específico\. Deve\-se utilizar o critério de rateio proporcional ao valor total de fornecimento por município\.
- ESIPM20009 \(PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO\) antigo ESIPM06 \- Valor das prestações de serviços de transporte intermunicipal e interestadual de passageiro, com ou sem emissão do BP\-e, detalhando o VAF para os municípios de início do transporte\. Deve\-se considerar, inclusive, os valores do subsídio do transporte público na proporção de cada município de inicio do transporte\.
- ESIPM30011 \(SERVIÇOS DE COMUNICAÇÃO E TELECOMUNICAÇÃO\) antigo ESIPM07 \- Valor das prestações dos serviços de comunicação e telecomunicação, detalhando o VAF para os municípios da realização dos serviços, inclusos no campo de incidência do ICMS, não considerando o faturamento referente à comercialização de equipamentos\.
- ESIPM43015 \(DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO\) antigo ESIPM10 \- Valor das operações com gás natural canalizado, observando, no que couber, os valores de acordo com os critérios dos CFOPs dispostos em Manual do IPM\. Deve\-se utilizar o critério de rateio proporcional ao valor total de fornecimento por município\.

Os dados apurados serão armazenados e utilizados posteriormente para gravação do registro 1400 na geração do Sped Fiscal\.

__RN01__

__                                                    Recuperação dos Dados__

A geração é feita separadamente para cada um dos itens a serem apurados \(conforme __RN00__\), da seguinte forma:

__DISTRIBUIÇÃO DE ENERGIA ELÉTRICA__

__PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO__

__SERVIÇOS DE COMUNICAÇÃO E TELECOMUNICAÇÃO__

__DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO__

Nestes casos, a apuração envolve outros segmentos: 

\- Energia Elétrica;

\- Transporte;

\- Comunicação / Telecomunicação;

\- Gás 

A apuração é feita a partir dos documentos de transporte da SAFX07, e para alguns casos, da SAFX42/SAFX43\. Em alguns casos também serão consideradas as operações de entrada \(deduções\) parametrizadas\. 

Os detalhes do processamento referente a cada um destes itens, e também sobre a gravação dos dados apurados, foram descritos separadamente, nas seguintes regras:

__RN02__

__DISTRIBUIÇÃO DE ENERGIA ELÉTRICA__

__RN03__

__PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO__

__RN04__

__SERVIÇOS DE COMUNICAÇÃO E TELECOMUNICAÇÃO__

__RN05__

__DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO__

__RN02__

__DISTRIBUIÇÃO DE ENERGIA ELÉTRICA__

__Código ESIPM13005  \(Código anterior: ESIPM05\)  – Operação de distribuição de energia elétrica __

__\[MFS698113\]__ Inclusão do código ESIPM13005 válido a partir de 01/03/2025\. O código  ESIPM05  foi descontinuado\.

__A partir de 2025 este código passa a ser entregue de forma anual para dados superiores ao ano anterior \(2024\)__

<a id="_Hlk72401896"></a>Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 

__\+__

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do ES, e considera também o valor a ser deduzido de cada municípo, referente às operações de compra de energia, conforme orienta a Portaria n\.34\-R, Ago/2015, Sefaz\-ES\. O total a ser deduzido é apurado com base nas notas fiscais parametrizadas \(no menu das deduções\), e rateado entre os municípios utilziando o critério de rateio\. 

<a id="_Hlk72401941"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos  C500, C600 ou C700 para o segmeno de energia elétrica\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “06” e “66”

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data compreendendo o Ano Base informado na Tela\. 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\(os documentos da X42/X43 sempre têm itens\)

<a id="_Hlk72402000"></a>__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

<a id="_Hlk72402090"></a>__Apuração do total das deduções a ser rateado entre os municípios:__

O valor total a ser rateado será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

*\(o tratamento das deduções é o mesmo descrito para o item ESIPM10 – Gás\)*

Critérios de recuperação das notas \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data compreendendo o Ano Base informado na Tela\. 

\- Somente as notas não canceladas

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo  “ESIPM13005__”__ \(cod\_param = 897\);

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

O total apurado será rateado entre os municípios processados com base na SAFX42/SAFX43, conforme descrito a seguir: 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\. Neste caso, não será realizado nenhum rateio, já que não tem nenhum valor a ser deduzido\. 

__Rateio do total das deduções entre os municípios:__

Para efetuar o rateio das deduções, será considerado o valor apurado na SAFX42/SAFX43 referente a cada município processado, e o total de todos os municípios\. Com base nestes critérios, será calculado o percentual de participação de cada município\. 

Exemplo:

                       Valor apurado \(X42/X43\)     Percentual de cada município

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Município A =             120\.000,00                          57,9598145 %

Município B =               85\.200,00                          41,1514683 %

Município C =                1\.840,00                             0,8887171 %

Total            =            207\.040,00                               \(100 %\)

No cálculo do percentual serão utilizadas 7 casas decimais, *sem* arredondar a sétima casa, para maior precisão\.

Supondo que o total a ser deduzido fosse de 95\.000,00\.

Neste caso, o valor de dedução correspondente a cada município seria:

Valor de dedução p/o município A =  55\.061,82   \(57,9598145% de 95\.000,00\)

Valor de dedução p/o município B =  39\.093,89   \(41,1514683% de 95\.000,00\)

Valor de dedução p/o município C =      844,28    \(0,8887171% de 95\.000,00\)

Ao calcular a dedução, *não* será feito o arredondamento dos decimais, para que o valor total *não* ultrapasse o total a ser deduzido \(que no exemplo é 95\.000,00\)

\. 

Como resultado apurado para cada município, teríamos:

                     Valor apurado \(X42/X43\)      Dedução         Resultado final

                      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Município A =         120\.000,00                  55\.061,82          64\.938,18

Município B =           85\.200,00                  39\.093,89          46\.106,11

Município C =            1\.840,00                       844,28                995,72

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM13005__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ ESIPM13005__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                  \[Valor resultante da totalização – valor da dedução apurada\] 

                                                       \(\+\)

                        \[Campo “Outros Valores” informado manualmente\]

                                                        \(\-\) 

                       \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\), o valor da dedução apurada, e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

\- O valor totalizado das notas \(X42/X43\) será gravado no campo “Valor Apurado”;

\- O valor da dedução calculado será gravado no campo “Deduções”; 

\- O valor final \(valor gravado no 1400\) será gravado no campo “Valor Total”;

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na __RN06__\.

__RN03__

__PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO__

__Código ESIPM20009   \(Código anterior: ESIPM06\) – Prestação de Serviço de Transporte Intermunicipal e Interestadual __

__*MFS1513*__*: Alterou a geração do código 06 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.*

__\[MFS698113\]__ Inclusão do código ESIPM20009 válido a partir de 01/03/2025\. O código  ESIPM06  foi descontinuado\.

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem do transporte\. Este item *não* usa parametrização de CFOP’s\. As operações são identificadas pelo modelo, tanto para transportes iniciados no ES, como em municípios de outros estados \(ver item 3\.6 da Portaria n\. 34\-R, Ago/2015\)\. No caso de outros estados, o valor será considerado na totalização do município do contribuinte \(emissor do documento\), conforme prevê a Portaria\. Este foi o conceito utilizado e alinhado junto à Informação para a geração deste item\. 

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Classificação = 1, 3 ou 4

   \(a classificação 4 é utilizada nos CTRC’s, e as classificações 1 /3 poderão constar

    na nota fiscal modelo 07 ou no caso dos bilhetes de passagem\)

\- Data Fiscal/ Data Extemporânea \- deve ser uma data compreendendo o Ano Base informado na Tela 

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve estar preenchido;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

*   \(neste caso, o município de origem pode ser <> "ES”, pois a Portaria cita que os*

*   transportes iniciados em outras UF’s serão registrados p/o munic\. do emitente\) *

\- Notas com *ou* sem itens na SAFX08; 

\- Modelo \(campo 13\) – todos os modelos de documentos de transporte:

07, 08, 8B, 09, 10, 11, 13, 14, 15, 16, 18, 30, 26, 27 e 57, 67

__\[MFS698113\]: __O Código passou a ser utilizado apenas para transporte de passageiros, portanto, sendo inativados na solução o uso dos modelos de documentos que referen\-se a transporte de cargas\. Em conjunto com o modelo de documento será utilizado também para identificação do transporte de passageiros o uso do CFOP, que deverá ser parametrizado na solução\.__ __

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros àRegistro 1400 à Específico por UF” para a operação  __“__<a id="_Hlk188351651"></a>__” \(__cod\_param = 900\); 

Serão considerandos os modelos de documento de transporte tanto de cargas como de pessoas, conforme prevê a Portaria \(exceto aéreo de passageiro\)\. Trata\-se exatamente dos documentos gravados nos seguintes registros do arquivo: D100, D300 __ESIPM20009__e D400\.

Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

*\(no caso da classificação 4 \(CTRC’s\) as notas não terão itens na SAFX08, já na classificação 1, poderão ou não ter itens\) *

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100/D300/D400, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados nestes registros ou seus registros “filhos”\.

__Processamento das notas:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__, da seguinte forma:

\- Se município origem for do estado do “ES” à o valor será totalizado normalmente

  para o município de origem  

\- Se município origem for de outros estados à neste caso o valor será totalizado p/o

  município do contribuinte informante 

 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM20009__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ ESIPM20009__”

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

O valor resultante da totalização dos documentos, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\)\.

__RN04__

__SERVIÇOS DE COMUNICAÇÃO E TELECOMUNICAÇÃO__

__Código ESIPM30011 \(Código anterior: ESIPM07\)  \-  Prestação de serviços de comunicação ou telecomunicação__

__\[MFS698113\]__ Inclusão do código ESIPM30011 válido a partir de 01/03/2025\. O código  ESIPM07  foi descontinuado\.

Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 

*Obs: A apuração deste item é feita apenas a partir das operações da SAFX42/SAFX43\. Sendo assim, não são consideradas as operações de venda de aparelhos, equipamentos e acessórios \(conforme orientação da Portaria 34\-R, Ago/2015, Sefaz\-ES\), já que estas vendas são realizadas através de cupom fiscal ou NFe \(conforme alinhamento junto à Informação\) , e portanto, não constam da 42/43\.*

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

__ __

__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos de Telecom \(D500/D600/D700\)\)

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “21” ou “22” ou ‘62’

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data compreendendo o Ano Base informado na Tela\. 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\), e

 para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo __“ESIPM30011”\.__

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     __ “ESIPM30011”\.__

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

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na __RN06__\.

__RN05__

__                                           DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO__

__Código ESIPM43015 \(Código anterior: ESIPM10\) \- Distribuição de gás natural canalizado__

<a id="_Hlk72412856"></a>__\[MFS698113\]__ Inclusão do código ESIPM43015 válido a partir de 01/03/2025\. O código  ESIPM10  foi descontinuado\.

Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do ES, e considera também o valor a ser deduzido de cada municípo, referente às operações de compra de gás natural, conforme orienta a Portaria n\.34\-R, Ago/2015, Sefaz\-ES\. O total a ser deduzido é apurado com base nas notas fiscais parametrizadas \(no menu das deduções\), e rateado entre os municípios utilziando o critério de rateio\. 

<a id="_Hlk72414955"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos   C500, C600 ou C700 para o segmento de gás\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

   

\- \(Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “28”\) 

   __ou__ 

\- \(Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “01” __e__ Empresa é do

   segmento de gás\) __\(\*\)__

__*\(\*\)*__* A verificação do segmento é feita através do CNAE, deve ser = 4020701, 4020702, 3520401 ou 3520402\. O filtro do modelo do documento é diferente para os segmentos de gás e água, pois alguns contribuintes ainda utilizam o modelo 01, ao invés dos códigos específicos 28 e 29, porque várias obrigações ainda não tratam este códigos\.   *

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data compreendendo o Ano Base informado na Tela\. 01/01 à 31/12

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros àRegistro 1400 à Específico por UF” para a operação  __“__<a id="_Hlk188351772"></a>__ESIPM43015” \(__cod\_param = 898\); 

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Apuração do total das deduções a ser rateado entre os municípios:__

O valor total a ser rateado será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

*\(o tratamento das deduções é o mesmo descrito para o item *__ESIPM13005  __*– EE\)*

Critérios de recuperação das notas \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data compreendendo o Ano Base informado na Tela\. 

\- Somente as notas não canceladas

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

1. CFOP/Nat” para a operação do tipo “__ESIPM10__”, __“ESIPM43015” \(__cod\_param = 899\); 

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

O total apurado será rateado entre os municípios processados com base na SAFX42/SAFX43, conforme descrito a seguir: 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\. Neste caso, não será realizado nenhum rateio, já que não tem nenhum valor a ser deduzido\. 

__Rateio do total das deduções entre os municípios:__

Para efetuar o rateio das deduções, será considerado o valor apurado na SAFX42/SAFX43 referente a cada município processado, e o total de todos os municípios\. Com base nestes critérios, será calculado o percentual de participação de cada município\. 

Exemplo:

                       Valor apurado \(X42/X43\)     Percentual de cada município

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Município A =             120\.000,00                          57,9598145 %

Município B =               85\.200,00                          41,1514683 %

Município C =                1\.840,00                             0,8887171 %

Total            =            207\.040,00                               \(100 %\)

No cálculo do percentual serão utilizadas 7 casas decimais, *sem* arredondar a sétima casa, para maior precisão\.

Supondo que o total a ser deduzido fosse de 95\.000,00\.

Neste caso, o valor de dedução correspondente a cada município seria:

Valor de dedução p/o município A =  55\.061,82   \(57,9598145% de 95\.000,00\)

Valor de dedução p/o município B =  39\.093,89   \(41,1514683% de 95\.000,00\)

Valor de dedução p/o município C =      844,28    \(0,8887171% de 95\.000,00\)

Ao calcular a dedução, *não* será feito o arredondamento dos decimais, para que o valor total *não* ultrapasse o total a ser deduzido \(que no exemplo é 95\.000,00\)

\. 

Como resultado apurado para cada município, teríamos:

                     Valor apurado \(X42/X43\)      Dedução         Resultado final

                      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Município A =         120\.000,00                  55\.061,82          64\.938,18

Município B =           85\.200,00                  39\.093,89          46\.106,11

Município C =            1\.840,00                       844,28                995,72

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ ESIPM43015__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ ESIPM43015__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                  \[Valor resultante da totalização – valor da dedução apurada\] 

                                                       \(\+\)

                        \[Campo “Outros Valores” informado manualmente\]

                                                        \(\-\) 

                       \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\), o valor da dedução apurada, e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

\- O valor totalizado das notas \(X42/X43\) será gravado no campo “Valor Apurado”;

\- O valor da dedução calculado será gravado no campo “Deduções”; 

\- O valor final \(valor gravado no 1400\) será gravado no campo “Valor Total”;

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na __RN06__\.

__RN06__

__                                                        Gravação dos Dados__

O resultado apurado __*para cada município*__ será gravado na tabela da manutenção do registro 1400, correspondente ao menu “Geração à Manutenção à Registro 1400”, com as informações abaixo\.

Caso já exista o registro para o *estabelecimento*, *período*, *município* e *código da tabela de itens p/o índice de participação dos municípios*, os valores calculados serão atualizados, mas, os valores informados \(campos “Outros Valores” e “Outras Deduções”\) que possam já ter sido cadastrados serão mantidos\.

Estabelecimento

Estabelecimento da geração

Período

As datas inicial e final do período serão preenchidas com:

Data Inicial à 01/03/nnnn

Data Final à 31/03/nnnn

Sendo “nnnn” ano da Geração do Meio Magnético / Competência\.

Esses valores serão gerados apenas no arquivo da EFD do mês de Março\.

Indicador do Produto

*Os campos referentes ao produto serão preenchidos com um caracter branco \(pois fazem parte da chave da tabela\)\.*

Código do Produto

*Os campos referentes ao produto serão preenchidos com um caracter branco \(pois fazem parte da chave da tabela\)\.*

Município

UF = ES

Município = código do município apurado 

Tabela p/ IPM

Gravar com a Informação da tabela “__5\.9\.1__”

Código da Tabela de Itens p/o Índice de Participação dos Municípios

Para o item “DISTRIBUIÇÃO DE ENERGIA ELÉTRICA” \(conforme __RN02__\):

     Será gravado o conteúdo “__ESIPM13005__”;

Para o item “PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO” \(conforme __RN03__\):

     Será gravado o conteúdo “__ESIPM20009__”; 

Para o item “SERVIÇOS DE COMUNICAÇÃO E TELECOMUNICAÇÃO” \(conforme __RN04__\):

     Será gravado o conteúdo “__ESIPM30011__”;

Para o item “DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO” \(conforme __RN05__\):

     Será gravado o conteúdo “__ESIPM43015__”;

     

Valores Calculados – Valor Apurado

Valor das saídas apurado para o município 

Valores Calculados – Deduções

Valor das deduções apurado para o município\.

Será o total das notas de entrada parametrizadas como dedução, que são utilizadas nos itens:

\- DISTRIBUIÇÃO DE ENERGIA ELÉTRICA

\- PRESTAÇÃO SERVIÇO DE TRANSPORTE DE PASSAGEIRO

\- DISTRIBUIÇÃO DE GÁS NATURAL CANALIZADO

Valores Informados – Outros Valores

*\(campo não atualizado na geração, pois corresponde a valor inserido manualmente\)   *

Valores Informados – Outras Deduções

*\(campo não atualizado na geração, pois corresponde a valor inserido manualmente\)*

Valor Total

O valor deste campo é gerado a partir dos seguintes campos da tabela:

        \[Valor Apurado – Deduções \+ Outros Valores – Outras Deduções\]

= = = = = 

