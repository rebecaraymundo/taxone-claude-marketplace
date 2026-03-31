# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PI

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PI.docx
- **Modificado:** 2024-08-27
- **Tamanho:** 97 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- PI

__Localização__: 

##### DOCUMENTO DE REQUISITO

__*Data*__

__*Demanda*__

__Descrição__

__Responsável__

30/01/2024

MFS607283

Criação do documento\.

Inclusão dos códigos 1202 \(UF Alagoas\) e PI004 \(UF Piauí\) no processo automático do registro 1400 para Entradas\.

Graciela Soares

06/02/2024

MFS607284

Inclusão dos códigos 1202 \(UF Alagoas\) e PI004 \(UF Piauí\) no processo automático do registro 1400 para Saídas\.

Graciela Soares

27/08/2024

MFS651592

Geração automática do registro 1400 para o código PI003\.

Liliane Assaf

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração – Específico por UF<a id="_Toc75782998"></a> – PI

__RN1400\-PI__

A geração do 1400 para a modalidade “PI” foi desenvolvida de acordo a PORTARIA SEFAZ\-PI/GASEC/SUPREC/UNATRI Nº 3/2021” e a tabela de Códigos do Índice de Participação dos Municípios disponibilizada no site da Receita Federal\.

Consultar os códigos no link: [http://www\.sped\.fazenda\.gov\.br/spedtabelas/AppConsulta/publico/aspx/](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/)

ConsultaTabelasExternas\.aspx?CodSistema=SpedFiscal

Os tipos de operação solicitados são os seguinte:

\- PI001 \- Geradoras de energia solar ou eólica com geração em município\(s\) diverso\(s\) de sua sede

\- PI002 \- Distribuidoras de energia elétrica

\- PI003 \- Prestadores de serviços de comunicação e telecomunicação \[MFS651592\]

\- PI004 \- Prestadores de serviço de transporte rodoviário intermunicipal e interestadual de passageiros e de cargas

\- PI005 \- Prestadores de serviços de transporte ferroviário intermunicipal e interestadual

\- PI006 – Produtores/industriais que realizem operações c/ produtos adquiridos de produtor rural s/ emissão NF 

\- PI007 \- Produtores rurais, extratores, ou industriais que efetuem sua produção ou extração em município diverso de sua sede

\- PI008 \- Mineradoras, na hipótese de a jazida se estender por mais de um município piauiense

\- PI009 \- Contribuintes que realizem saídas de mercadorias em estabelecimento localizado em município diverso daquele onde ocorreu a efetiva comercialização

\- PI010 \- Contribuintes que realizem operações de marketing porta a porta a consumidor final

\- PI011 \- Cooperativas que realizem operações com mercadorias recebidas para depósito

A geração automática do 1400 se dá apenas para os códigos PI003 e PI004\. Os registros 1400 dos demais códigos são são inseridos manualmente através da tela de  manutenção disponível no menu “Geração 🡪 Manutenção 🡪 Regitsro 1400”\.

As regras estão organizadas da seguinte forma:

__RN1400\-PI\-01__ – geração para o código PI001;

__RN1400\-PI\-02__ – geração para o código PI002;

__RN1400\-PI\-03__ – geração para o código PI003;

__RN1400\-PI\-04__ – geração para o código PI004;

__RN1400\-PI\-05__ – geração para o código PI005;

__RN1400\-PI\-06__ – geração para o código PI006;

__RN1400\-PI\-07__ – geração para o código PI007;

__RN1400\-PI\-08__ – geração para o código PI008;

__RN1400\-PI\-09__ – geração para o código PI009;

__RN1400\-PI\-10__ – geração para o código PI010;

__RN1400\-PI\-11__ – geração para o código PI011;

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-PI\-01__

__PI001 \- Geradoras de energia solar ou eólica com geração em município\(s\) diverso\(s\) de sua sede__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI001__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI001__” 

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

__RN1400\-PI\-02__

__PI002 \- Distribuidoras de energia elétrica__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI002__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI002__” 

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

<a id="_Hlk175678853"></a>__RN1400\-PI\-03__

__PI003 \- Prestadores de serviços de comunicação e telecomunicação__

\[MFS651592\]: Geração automática do 1400 para o código PI003

<a id="_Hlk72401896"></a>Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 	

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do PI, e considera também o valor a ser deduzido de cada município, referente às aquisições de mercadorias/insumos diretamente relacionadas a essas prestações, conforme orienta a PORTARIA Nº 3/2021\- Sefaz\-PI\. O total a ser deduzido é apurado com base nas notas fiscais parametrizadas \(no menu das deduções\), e rateado entre os municípios utilizando o critério de rateio\. 

<a id="_Hlk72401941"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos de Telecom \(D500/D600/D700\)\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “21” ou “22” ou “62”

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “PI”;

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

Critérios de recuperação das notas \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__PI003__”

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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__PI003__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__PI003__”

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

__RN1400\-PI\-04__

__PI004 \- Prestadores de serviço de transporte rodoviário intermunicipal e interestadual de passageiros e de cargas__

__MFS607284:__ A partir dessa demanda, a geração do código “__PI004__”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\) 

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

                            \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entradas dos Documentos de Prestação de Serviços de Transporte Rodoviário \(identificados pelo modelo\), totalizando o valor   contábil   das   entradas   e   aquisições   de   serviço   de   transporte intermunicipal e/ou interestadual, por município do estado do __Piauí__, excluindo\-se as operações dedutíveis

__Apuração do valor referente a cada Aquisição ou Tomada de Serviço na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no __D100__ que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\); \[MFS607284\]
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67, 63;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__PI004__”;
- Serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja de PI \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

Valor a ser totalizado:

- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) ou valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\), no caso das notas sem itens;

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas que não sejam transferências \(campo 74\-IND\_TRANSF\_CRED da SAFX07 = 0\);
- Somente notas com situação especial \(campo 125\-IND\_SITUACAO\_ESP da SAFX07\) diferente de 1, 2 e 8;
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “PI”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__PI004__”;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__PI004__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI004__” 

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

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-PI\-05__

__PI005 \- Prestadores de serviços de transporte ferroviário intermunicipal e interestadual__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI005__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI005__” 

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

__RN1400\-PI\-06__

__PI006 – Produtores/industriais que realizem operações c/ produtos adquiridos de produtor rural s/ emissão NF __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI006__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI006__” 

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

__RN1400\-PI\-07__

__PI007 \- Produtores rurais, extratores, ou industriais que efetuem sua produção ou extração em município diverso de sua sede__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI007__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI007__” 

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

__RN1400\-PI\-08__

__PI008 \- Mineradoras, na hipótese de a jazida se estender por mais de um município piauiense__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI008__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI008__” 

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

__RN1400\-PI\-09__

__PI009 \- Contribuintes que realizem saídas de mercadorias em estabelecimento localizado em município diverso daquele onde ocorreu a efetiva comercialização__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI009__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI009__” 

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

__RN1400\-PI\-10__

__PI010 \- Contribuintes que realizem operações de marketing porta a porta a consumidor final__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI010__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI010__” 

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

__RN1400\-PI\-11__

__PI011 \- Cooperativas que realizem operações com mercadorias recebidas para depósito __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__PI011__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__PI011__” 

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

