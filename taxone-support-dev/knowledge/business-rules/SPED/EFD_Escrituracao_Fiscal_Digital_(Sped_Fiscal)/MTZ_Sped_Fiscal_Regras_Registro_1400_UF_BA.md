# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_BA

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_BA.docx
- **Modificado:** 2025-11-25
- **Tamanho:** 311 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- BA

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS68577

Aline Melo

Criação do documento\.

Inclusão do código BAE20 no processo de geração automática do registro 1400, para o estado da Bahia\.

12/07/2021

MFS90839

Andréa Rocha

Alteração dos códigos BAE03 e BAS03 para tratar o parâmetro da DMA\-BA da tela de Dados Iniciais

27/10/2022

MFS99537

Liliane Assaf

Alteração na geração do 1400 tipo de geração “Específicos por UF para Bahia, na geração do código BAE02, para considerar os documentos fiscais de entrada de modelo 62 \(SAFX07/SAFX08\)\.

03/01/2023

MFS98743

Andréa Rocha

Alteração dos códigos BAE03 e BAS03 para tratar o modelo 55 para notas fiscais de energia elétrica\.

05/01/2023

MFS402300

Aline Melo

Inclusão dos códigos BAE80 e BAS80 no processo de geração automática do registro 1400, para o estado da Bahia\.

07/03/2023

MFS402301

Aline Melo

Inclusão dos códigos BAE81 e BAS81 no processo de geração automática do registro 1400, para o estado da Bahia\.

16/03/2023

MFS541919

Andréa Rocha

Alteração do código BAE01 para gerar as informações baseadas na atividade do estabelecimento, e não de acordo com as operações do estabelecimento, que no caso desse código a atividade é transporte\.  Essa alteração está sendo feita de acordo com a resposta enviada por e\-mail pela SEFAZ\-BA para o cliente e para nossa área de informação, as alterações ainda não constam nos manuais desse estado\. 

06/07/2023

29/09/2023

MFS436036

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

Liliane Assaf

MFS589799

Graciela Soares

Alteração dos códigos BAE02 e BA03 para gerar as informações baseadas na atividade do estabelecimento, e não de acordo com as operações do estabelecimento, que no caso dos códigos acima correspondem à Telecomunicação e Comunicação \(BA02\) e Água e Energia Elétrica \(BA03\)\.  Essa alteração está sendo feita de acordo com a resposta enviada por e\-mail pela SEFAZ\-BA para o cliente e para nossa área de informação, as alterações ainda não constam nos manuais desse estado\. 

30/11/2023

 MFS663539

Liliane Assaf 

Inclusão dos códigos BAE21, BAS21, BAE22, BAS22, BAE23, BAS23, BAE24, BAS24\.

- BAE21: msm regra do BAE01;
- BAS21: msm regra do BAS01;
- BAE22: msm regra do BAE02;
- BAS22: msm regra do BAS02;
- BAE23: msm regra do BAE03;
- BAS23: msm regra do BAS03;
- BAE24: msm regra do BAE04;
- BAS24: msm regra do BAS04\.

Os códigos BAE01 a 04 e BAS01 a 04 foram descontinuados, valendo só até 30/06/2024\. A partir de 01/07/2024 valem os códigos BAE21 a 24 e BAS21 a 24

30/07/2024

MFS710621

Graciela Soares

Inclusão do modelo 66 na regra do código BAS03/BAS23 Geração e Distribuição de Energia Elétrica eÁgua – Saídas\.

03/02/2025

MFS753144

Andréa Rocha

Alteração da regra de preenchimento do campo código do município para o código BAS23 \- Geração e Distribuição de Energia Elétrica eÁgua – Saídas\.

19/02/2025

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- BA

__RN1400\-BA__

A geração do 1400 para a modalidade “BA” foi desenvolvida de acordo com os dados solicitados na Orientação de Preenchimento disponibilizada pela SEFAZ em [http://www\.sefaz\.ba\.gov\.br/especiais/Registro\_1400\_Orienta%C3%A7%C3%A3o\_Preenchimento\.pdf](http://www.sefaz.ba.gov.br/especiais/Registro_1400_Orienta%C3%A7%C3%A3o_Preenchimento.pdf)

 

As regras estão organizadas da seguinte forma nesse primeiro momento:

__RN1400\-BA\-01__ – geração para os códigos “BAE01” e ”BAE21”

__RN1400\-BA\-02__ – geração para os códigos “BAS01” e “BAS21”

__RN1400\-BA\-03__ – geração para os códigos “BAE02” e “BAE22”

__RN1400\-BA\-04__ – geração para os códigos “BAS02” e “BAS22”

__RN1400\-BA\-05__ – geração para os códigos “BAE03” e “BAE23”

__RN1400\-BA\-06__ – geração para os códigos “BAS03” e “BAS23”

__RN1400\-BA\-07__ – geração para os códigos “BAE04” e “BAE24”

__RN1400\-BA\-08__ – geração para os códigos “BAS04” e “BAS24”

__RN1400\-BA\-09__ – geração para o código “BAE05”

__RN1400\-BA\-10__ – geração para o código “BAS05”

__RN1400\-BA\-11__ – geração para o código “BAE06”

__RN1400\-BA\-12__ – geração para o código “BAS06”

<a id="OLE_LINK183"></a>__RN1400\-BA\-13__ – geração para o código “BAE07”

__RN1400\-BA\-14__ – geração para o código “BAE08”

__RN1400\-BA\-15__ – geração para o código “BAE09”

__RN1400\-BA\-16__ – geração para o código “BAE10”

__RN1400\-BA\-17__ – geração para o código “BAE11”

__RN1400\-BA\-18__ – geração para o código “BAE12”

__RN1400\-BA\-19__ – geração para o código “BAE13”

__RN1400\-BA\-20__ – geração para o código “BAE14”

__RN1400\-BA\-21__ – geração para o código “BAE15”

<a id="OLE_LINK184"></a>__RN1400\-BA\-22__ – geração para o código “BAE16”

__RN1400\-BA\-23__ – geração para o código “BAE17”

__RN1400\-BA\-24__ – geração para o código “BAE18”

__RN1400\-BA\-25__ – geração para o código “BAE19”

__RN1400\-BA\-26__ – geração para o código “BAE20”

__RN1400\-BA\-27__ – geração para o código “BAE99”

__RN1400\-BA\-28__ \- geração para o código “BAE80”

__RN1400\-BA\-29__ \- geração para o código “BAS80”

__RN1400\-BA\-30__ \- geração para o código “BAE81”

__RN1400\-BA\-31__ \- geração para o código “BAS81”

__RN1400\-BA\-Geração Especial__ – geração específica para Empresas de Água__ \[MFS21172\]__

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

Os __códigos de 01 a 04 e de 21 a 24__ são correspondentes aos Quadros 30 e 31 CS\-DMA \(Cédula Suplementar de Declaração e Apuração Mensal do ICMS\) da DMA da Bahia, em que são demonstradas todas as entradas de mercadorias e/ou aquisições de serviços proporcionais às saídas dos municípios baianos e as saídas de mercadorias e/ou prestações de serviços dos municípios baianos\. \[__MFS663539__\] Os códigos 01 ao 04 foram descontinuados valendo só até 30/06/2024\. A partir de 01/07/2024 valem os novos códigos 21 ao 24\.

Os __códigos BAE07, BAE13, BAE14 e BAE20__ são correspondentes ao Quadro 09 da DMD \(Declaração da Movimentação de Produtos com ICMS Diferido\), onde são demonstrados os valores totais de entradas do produto diferido, discriminando\-o por Município e em função das características do contribuinte de origem\. Para esses códigos, devem ser atendidas as regras: RN1400\-BA\-13, 

RN1400\-BA\-19, RN1400\-BA\-20 e RN1400\-BA\-26__\.__

__Cálculo do Rateio para Município:__

Se tratando da Aquisição:

- Será realizada a totalização de todas as entradas independente do município de origem/consumo/fato gerador, pois essa totalização será proporcionalizada às saídas prestadas dentro dos municípios baianos;
- Será realizada a totalização da dedução e depois subtraída as essas aquisições do período;

Se tratando da Prestação:

- Será realizada a totalização das saídas por município de origem/cosumo/fato gerador baiano;
- Será realizada a totalização da dedução também por município de origem/cosumo/fato gerador baiano e depois subtraída as essas saídas do período;
- Será realizada a totalização de todas as saídas desses municípios encontrados e multiplicado para encontrar a proporção que será utilizado para realizar o cálculo das entradas;

Cálculo Proporcional de Entradas pelas Saídas por Município:

- Será utilizado o total das entradas encontrado multiplicado pela proporção das saídas encontrado para cada município;
- Os municípios que serão apresentados no arquivo magnético serão sempre os da saída, relaciolados à unidade federada da Bahia, então se não houver saídas a declarar não haverá aquisição\.

__*Exemplo Cálculo Rateio para Município de Salvador – Códigos 01 a 04 e 21 a 24:*__

Geração dos Registros Referente às Entradas com Proporcionalização dos Valores em Relação às Saídas \(independe do código, mas no exemplo utilizamos o código 02\):

Aquisição:

__*CFOP*__

__*Valor NF*__

__*UF*__

__*Município*__

1\.XXX

600,00

BA

Salvador

2\.XXX

800,00

SP

São Paulo

*Total*

*1400,00*

Dedução – Entradas

__*CFOP*__

__*Valor NF*__

__*UF*__

__*Município*__

5\.XXX

100,00

BA

Salvador

*Total*

*100,00*

Prestação:

__*CFOP*__

__*Valor NF*__

__*Deduções*__

__*UF*__

__*Município*__

5\.XXX

6000,00

2000,00

BA

Salvador

5\.XXX

5000,00

BA

Porto Seguro

5\.XXX

4000,00

BA

Feira de Santana

*Total*

*13000,00*

Dedução – Saídas

__*CFOP*__

__*Valor NF*__

__*UF*__

__*Município*__

1\.XXX

2000,00

BA

Salvador

*Total*

*2000,00*

__Cálculo dos Valores Proporcionais:__

Total das Entradas \(Aquisições – Deduções\) = 1300,00

Proporcional Município de Salvador:

Saídas para Salvador = 4000,00

Dividido pelo Total de Saídas = 13000,00

Proporção das Saídas para Salvador = 0,31

Cálculo da proporção das Entradas pelas Saídas para Salvador:

Total das Entradas = 1300,00

Multiplicado pela proporção das saídas para Salvador = 1300,00 x 0,31 = 400,00

Cálculo Proporcional de Entradas pelas Saídas por Município:

__Salvador__

__400,00__

Considerando os outros municípios do exemplo:

Porto Seguro

500,00

Feira de Santana

400,00

Geração dos Registros 1400 \- Entradas

|1400|BAE02|2927408|400,00|

|1400|BAE02|2925303|500,00|

|1400|BAE02|2910800|400,00|

Geração dos Registros 1400 \- Saídas

|1400|BAS02|2927408|6000,00|

|1400|BAS02|2925303|5000,00|

|1400|BAS02|2910800|4000,00|

__RN1400\-BA\-01__

__\[MFS541919\] __Retirada do filtro de modelo das notas a serem recuperadas para gerar as informações baseadas na atividade do estabelecimento\.  A identificação da atividade do estabelecimento vai ser feita pelas duas primeiras posições do código da atividade, de acordo com a estrutura dos códigos das classes CNAE\.

__\[MFS663539\]__ Inclusão do código BAE21 com a mesma regra do BAE01\. O código BAE01 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAE21\.

__Código BAE01 / BAE21 – Aquisição de Serviços de Transporte  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

              Estabelecimento

Este código será gerado a partir dos documentos da aquisição do transporte \(identificados pelo modelo\), totalizando o valor   contábil   das   entradas   e   aquisições   de   serviço   de   transporte intermunicipal e/ou interestadual, por município baiano, proporcionalmente às saídas informadas, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada aquisição na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no __D100__ que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Atividade Econômica \(campo 06\- COD\_ATIVIDADE da SAFX2064\) do estabelecimento igual a transporte \(2 primeiras posições do código igual a 49 ou 50 ou 51 ou 52\) 
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros àRegistro 1400 à Específico por UF” para a operação “__BAE01__”,  “__BAE21__”\(cod\_param = 877\); 
- BAE01: considerar para gerações com período até 30/06/2024\.
- BAE21: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, ou seja, não será utilizado critério de município baiano para as entradas, serão totalizados todos os municípios de dentro e fora da unidade federada da Bahia para que depois seja realizada a proporção desses valores entre as saídas declaradas aos municípios baianos\.

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAE01__”, “__BAE21__” \(cod\_param = 885\);
- BAE01: considerar para gerações com período até 30/06/2024\.
- BAE21: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, utilizando os seguintes valores:

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAE01__” /“__BAE21__”

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE01__” / “__BAE21__”

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-02__

__\[MFS663539\]__ Inclusão do código BAS21 com a mesma regra do BAS01\. O código BAS01 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAS21\.

__Código BAS01 / BAS21 – Prestação de Serviços de Transporte  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

              

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem do transporte\.

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no __D100__ que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 3, 4, 5 ou 6 \(a NF de modelo 07 usa classificação 1 ou 3 e os conhecimentos classificação 4, 5 ou 6\)/\(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAS01__”, __“BAS21”__ \(cod\_param = 878\);
- BAS01: considerar para gerações com período até 30/06/2024\.
- BAS21: considerar para gerações com períodos a partir de 01/07/2024
- No caso das notas de classificação 1 ou 3 serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja da BA \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);
- No caso das notas de classificação 4, 5 ou 6 serão consideradas apenas as notas em que em que o município de origem da SAFX07 seja da BA ou, quando este não for informado, o município da coleta na SAFX51 seja da BA \(campos 62\-COD\_ESTADO\_COLETA e 42\-COD\_MUNIC\_COLETA da SAFX51\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município de origem\.* 

O município utilizado no agrupamento será o município de origem da NF __ou__ o município de coleta dos itens de frete \(SAFX51\), quando se tratar de notas de frete \(classificação 4/5/6\), conforme descrito acima na regra da recuperação dos dados\.

Valor a ser totalizado:

- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) ou valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\), no caso das notas sem itens;
- Notas de classificação 4, 5 ou 6 \(a nota não terá itens\)  à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

*Obs\.: Os CTRC’s têm a classificação 4, 5 ou 6, e não têm itens na SAFX08\. Os seus itens ficam na SAFX51, e se referem aos dados das notas fiscais das mercadorias carregadas\. Desta forma, o valor do serviço de transporte é sempre o valor da capa \(SAFX07\), pois os valores da SAFX51 são os valores das notas do carregamento\.*

Sobre o município de coleta dos itens de frete \(SAFX51\):

Ao utilizar o município de coleta da SAFX51, caso exista mais de um item de frete para o mesmo documento, e eles tiverem municípios de coleta *diferentes*, será gravada a seguinte mensagem no log, e o documento *não* será considerado:* “Existem na base de dados itens de frete para o documento com mais de um município de coleta\. O documento não será considerado p/o registro 1400, código BAS01”\. *Caso o município da SAFX51 também não esteja preenchido, será gravada a seguinte mensagem no log, e o documento *não* será considerado: *“Para gerar o registro 1400, cód BAS01, é necessário que o município de origem esteja preenchido \(UF/munic origem da SAFX07 ou munic Coleta da SAFX51\)\. O documento não será considerado”\.*

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas que não sejam transferências \(campo 74\-IND\_TRANSF\_CRED da SAFX07 = 0\);
- Somente notas com situação especial \(campo 125\-IND\_SITUACAO\_ESP da SAFX07\) diferente de 1, 2 e 8;
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “BA”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAS01__”,__ “BAS21”__ \(cod\_param = 886\);
- BAS01: considerar para gerações com período até 30/06/2024\.
- BAS21: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por *município de origem da nota* \(SAFX07\), utilizando os seguintes valores:

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens;
- Para as notas sem itens, será totalizado o valor total da nota;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAS01__” /__“BAS21”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAS01__” /__“BAS21”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.  O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-03__

__\[MFS589799\] __Retirada do filtro de modelo das notas a serem recuperadas para gerar as informações baseadas na atividade do estabelecimento\.  A identificação da atividade do estabelecimento vai ser feita pelas duas primeiras posições do código da atividade, de acordo com a estrutura dos códigos das classes CNAE\.

__\[MFS663539\]__ Inclusão do código BAE22 com a mesma regra do BAE02\. O código BAE02 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAE22\.

__Código BAE02 / BAE22– __<a id="_Hlk152246711"></a>__Aquisição de Serviços de Comunicação/Telecomunicação  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

               Estabelecimento

Este código será gerado a partir dos documentos de entrada de comunicação/telecomunicação \(identificados pelo modelo\), totalizando o valor contábil das entradas e aquisições de serviço de comunicação, por município baiano, proporcionalmente às saídas, excluindo\-se as operações dedutíveis\.

__\[MFS99537\] Inclusão do Modelo 62__

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Atividade Econômica \(campo 06\- COD\_ATIVIDADE da SAFX2064\) do estabelecimento igual a transporte \(2 primeiras posições do código igual a 61\) 
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 21 ou 22 ou 62;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAE02__”, __“BAE22”__ \(cod\_param = 879\);
- BAE02: considerar para gerações com período até 30/06/2024\.
- BAE22: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, ou seja, não será utilizado critério de município baiano para as entradas, serão totalizados todos os municípios de dentro e fora da unidade federada da Bahia para que depois seja realizada a proporção desses valores entre as saídas declaradas aos municípios baianos\.

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX42/SAFX43\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAE02__”, __“BAE22”__ \(cod\_param = 887\);
- BAE02: considerar para gerações com período até 30/06/2024\.
- BAE22: considerar para gerações com períodos a partir de 01/07/2024

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, utilizando os seguintes valores:

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAE02__” /__“BAE22”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE02__” /__“BAE22”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-04__

__\[MFS663539\]__ Inclusão do código BAS22 com a mesma regra do BAS02\. O código BAS02 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAS22\.

__Código BAS02 / BAS22 – Prestação de Serviços de Comunicação/Telecomunicação  __

Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\.Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

__Apuração do valor referente a cada município na SAFX42/SAFX43:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 21 ou 22 ou ‘62’;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAS02__”, __“BAS22”__ \(cod\_param = 880\);
- BAS02: considerar para gerações com período até 30/06/2024\.
- BAS22: considerar para gerações com períodos a partir de 01/07/2024
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município da BA \(campo 75\-UF\_CONSUMO da SAFX42\);

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.* 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAS02__”, “__BAS22”__ \(cod\_param = 888\);
- BAS02: considerar para gerações com período até 30/06/2024\.
- BAS22: considerar para gerações com períodos a partir de 01/07/2024
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município da BA \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAS02__” /“__BAS22”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAS02__” / “__BAS22”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-05__

__\[MFS589799\] __Retirada do filtro de modelo das notas a serem recuperadas para gerar as informações baseadas na atividade do estabelecimento\.  A identificação da atividade do estabelecimento vai ser feita pelas duas primeiras posições do código da atividade, de acordo com a estrutura dos códigos das classes CNAE\.

__\[MFS663539\]__ Inclusão do código BAE23 com a mesma regra do BAE03\. O código BAE03 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAE23\.

__Código BAE03 / BAE23 – __<a id="_Hlk152246758"></a>__Geração e Distribuição de Energia Elétrica e Água \- Entradas  __

__\[MFS90839\] __Inclusão do tratamento do parâmetro da DMA\-BA da tela de Dados Iniciais

__\[MFS98743\] __Inclusão do tratamento do modelo 55 para as notas fiscais de energia elétrica

Quando o parâmetro “Utilizar a geração específica para Empresas de Água” do registro 1400 estiver marcado \(Dados para a geração específica \(DMA\-BA\)\) na parametrização de Dados Iniciais \(Parâmetros à Dados Iniciais\)

      Não deve ser feita a geração deste código \(BAE03\), porque a geração vai ser feita na rotina de Pré Geração \- Registro 1400 \- DMA BA\.

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

              Estabelecimento

Este código será gerado a partir dos documentos de entrada de geração e distribuição de energia elétrica e água \(identificados pelo modelo\), totalizando o valor contábil das entradas e insumos utilizados na geração e distribuição de energia elétrica ou água, por município baiano, proporcionalmente as saídas, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Atividade Econômica \(campo 06\- COD\_ATIVIDADE da SAFX2064\) do estabelecimento igual a transporte \(2 primeiras posições do código igual a 35 ou 36\) 
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 01, 06, 29 ou 55;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAE03__”, __“BAE23”__ \(cod\_param = 881\);
- BAE03: considerar para gerações com período até 30/06/2024\.
- BAE23: considerar para gerações com períodos a partir de 01/07/2024
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;

__Filtro para as notas de Água: __

- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 01 ou 29 e Empresa é do segmento de Água \(verificar através do CNAE que deve ser igual a “4100901”\), independente do modelo utilizado nestas notas \(01 ou 29\), considerar para o Sped o código igual a 29;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, ou seja, não será utilizado critério de município baiano para as entradas, serão totalizados todos os municípios de dentro e fora da unidade federada da Bahia para que depois seja realizada a proporção desses valores entre as saídas declaradas aos municípios baianos\.

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX42/SAFX43\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAE03__”,__ “BAE23”__ \(cod\_param = 889\);
- BAE03: considerar para gerações com período até 30/06/2024\.
- BAE23: considerar para gerações com períodos a partir de 01/07/2024

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, utilizando os seguintes valores:

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAE03__” /__“BAE23”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE03__” /__“BAE23”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.  O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__	__

__\[MFS663539\]__ Inclusão do código BAS23 com a mesma regra do BAS03\. O código BAS03 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAS23\.

__\[MFS710621\] __Inclusão do modelo de nota “66”

__Código BAS03 / BAS23 – Geração e Distribuição de Energia Elétrica e Água \- Saídas  __

__\[MFS90839\] __Inclusão do tratamento do parâmetro da DMA\-BA da tela de Dados Iniciais

__\[MFS98743\] __Inclusão do tratamento do modelo 55 para as notas fiscais de energia elétrica, incluindo a recuperação das notas fiscais com origem nas tabelas SAFX07/08

Quando o parâmetro “Utilizar a geração específica para Empresas de Água” do registro 1400 estiver marcado \(Dados para a geração específica \(DMA\-BA\)\) na parametrização de Dados Iniciais \(Parâmetros à Dados Iniciais\)

      Não deve ser feita a geração deste código \(BAE03\), porque a geração vai ser feita na rotina de Pré Geração \- Registro 1400 \- DMA BA\.

Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de geração e distribuição de energia elétrica ou água \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

__Apuração do valor referente a cada município na SAFX42/SAFX43:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 01, 06, 29 ou 66;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAS03__”, “__BAS23__” \(cod\_param = 882\);
- BAS03: considerar para gerações com período até 30/06/2024\.
- BAS23: considerar para gerações com períodos a partir de 01/07/2024
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município da BA \(campo 75\-UF\_CONSUMO da SAFX42\);

__Filtro para as notas de Água: __

- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 01 ou 29 e Empresa é do segmento de Água \(verificar através do CNAE que deve ser igual a “4100901”\), independente do modelo utilizado nestas notas \(01 ou 29\), considerar para o Sped o código igual a 29;

__\[MFS753144\] __Alteração da regra de preenchimento do código do município

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 55;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAS03__”, “__BAS23__” \(cod\_param = 882\);
- BAS03: considerar para gerações com período até 30/06/2024\.
- BAS23: considerar para gerações com períodos a partir de 01/07/2024
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;
- Se o Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) estiver preenchido e for um município da BA \(campo 207\-UF\_CONSUMO da SAFX07\)

       Utilizar o código do Município do ponto de consumo

Senão

       Utilizar o código do Município do estabelecimento da geração \(campo 23 da SAFX2064\)

__OBS:__ 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.* 

Valor a ser totalizado:

- Notas de Telecom à valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);
- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAS03__”, “__BAS23__” \(cod\_param = 890\);
- BAS03: considerar para gerações com período até 30/06/2024\.
- BAS23: considerar para gerações com períodos a partir de 01/07/2024
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município da BA \(campo 207\-UF\_CONSUMO da SAFX07\);
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAS03__” /“__BAS23__”

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAS03__” / “__BAS23__”

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.  O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-07__

__\[MFS663539\]__ Inclusão do código BAE24 com a mesma regra do BAE04\. O código BAE04 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAE24\.

__Código BAE04 / BAE24 – Regimes Especiais \- Entradas  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada, totalizando o valor contábil das entradas, por município baiano, para as empresas que possuem regime especial de escrituração centralizada, excluindo\-se as operações dedutíveis e observando o disposto no referido regime\.

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAE04__”, __“BAE24”__ \(cod\_param = 883\);
- BAE04: considerar para gerações com período até 30/06/2024\.
- BAE24: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, ou seja, não será utilizado critério de município baiano para as entradas, serão totalizados todos os municípios de dentro e fora da unidade federada da Bahia para que depois seja realizada a proporção desses valores entre as saídas declaradas aos municípios baianos\.

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAE04__”, __“BAE24”__ \(cod\_param = 891\);
- BAE04: considerar para gerações com período até 30/06/2024\.
- BAE24: considerar para gerações com períodos a partir de 01/07/2024

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, utilizando os seguintes valores:

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAE04__” / __“BAE24”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE04__” / __“BAE24”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.  O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

<a id="OLE_LINK188"></a><a id="OLE_LINK189"></a><a id="OLE_LINK190"></a><a id="OLE_LINK191"></a>__RN1400\-BA\-08__

__\[MFS663539\]__ Inclusão do código BAS24 com a mesma regra do BAS04\. O código BAS04 foi descontinuado valendo só até 30/06/2024\. A partir de 01/07/2024 vale o BAS24\.

<a id="OLE_LINK193"></a><a id="OLE_LINK194"></a><a id="OLE_LINK192"></a>__Código BAS04 / BAS24 – Regimes Especiais \- Saídas  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saída, totalizando o valor contábil das saídas, por município baiano de ocorrência do fato gerador, para as empresas que possuem regime especial de escrituração centralizada, excluindo\-se as operações dedutíveis e observando o disposto no referido regime\.

__Apuração do valor referente a cada município na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__BAS04__”, __“BAS24”__ \(cod\_param = 884\);
- BAS04: considerar para gerações com período até 30/06/2024\.
- BAS24: considerar para gerações com períodos a partir de 01/07/2024
- Serão consideradas apenas as notas em que o município de origem \(município do fato gerador\) seja da BA \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, ou seja, não será utilizado critério de município baiano para as entradas, serão totalizados todos os municípios de dentro e fora da unidade federada da Bahia para que depois seja realizada a proporção desses valores entre as saídas declaradas aos municípios baianos\.

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Apuração dos valores a serem deduzidos:__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas que não sejam transferências \(campo 74\-IND\_TRANSF\_CRED da SAFX07 = 0\);
- Somente notas com situação especial \(campo 125\-IND\_SITUACAO\_ESP da SAFX07\) diferente de 1, 2 e 8;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__BAS04__”, __“BAS24”__ \(cod\_param = 892\);
- BAS04: considerar para gerações com período até 30/06/2024\.
- BAS24: considerar para gerações com períodos a partir de 01/07/2024
- Serão consideradas apenas as notas em que o município de origem \(município do fato gerador\) seja da BA \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por CFOP/ CFOP\-Natureza para todos os municípios em questão*, utilizando os seguintes valores:

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__BAS04__” / __“BAS24”__

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAS04__” / __“BAS24”__

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

\[MFS29417\]

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.  O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-BA\-09__

__Código BAE05 – Exclusões nas Entradas\-IPI e ICMS/ST__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61950: __A partir dessa demanda, a geração do “__BAE05”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem os dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de localização do estabelecimento\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

 Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE05__”\.

\- Município de origem da nota \(campo 182 da SAFX07\) deve ser um município da

   UF do Estabelecimento

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;	

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

Devem ser totalizados os seguintes valores:

\- Capa: Campos  \(48\-VLR\_SUBST\_ICMS\) \+ \(40\-VLR\_IPI\) da SAFX07

\- Itens: Campos \(52\-VLR\_SUBST\_ICMS\) \+ \(40\-VLR\_IPI\)  da SAFX08

\* Os valores ICMS retido por substituição tributária e a parcela do IPI não integram a base de cálculo do ICMS de acordo com a operação informada na nota fiscal, baseada na parametrização de CFOP e CFOP/Natureza\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE05__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAE05__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-10__

__Código BAS05 – Exclusões nas Saídas\-IPI e ICMS/ST__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61950: __A partir dessa demanda, a geração do “__BAS05”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem os dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de localização do estabelecimento\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no C100 que atendam aos seguintes critérios:

__Critérios de recuperação das notas na SAFX07/SAFX08:__

	

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 2 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

 Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAS05__”\.

\- Município de origem da nota \(campo 182 da SAFX07\) deve ser um município da UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

Devem ser totalizados os seguintes valores:

\- Capa: Campos  \(48\-VLR\_SUBST\_ICMS\) \+ \(40\-VLR\_IPI\) da SAFX07

\- Itens: Campos \(52\-VLR\_SUBST\_ICMS\) \+ \(40\-VLR\_IPI\)  da SAFX08

\*Os valores ICMS retido por substituição tributária e a parcela do IPI não integram a base de cálculo do ICMS de acordo com a operação informada na nota fiscal, baseada na parametrização de CFOP e CFOP/Natureza\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAS05__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

\- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAS05__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\)\.

__RN1400\-BA\-11__

__Código BAE06 – Operações NÃO dedutíveis nas Entradas__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61951: __A partir dessa demanda, a geração do “__BAE06”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem os dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de localização do estabelecimento\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

 Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE06__”\.

\- Município de origem da nota \(campo 182 da SAFX07\) deve ser um município da UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

Devem ser totalizados os seguintes valores:

\- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

\- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE06__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAE06__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-12__

__Código BAS06 – Operações NÃO dedutíveis nas Saídas__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61951: __A partir dessa demanda, a geração do “__BAS06”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem os dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de localização do estabelecimento\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no C100 que atendam aos seguintes critérios:

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

 Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAS06__”\.

\- Município de origem da nota \(campo 182 da SAFX07\) deve ser um município da UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

Devem ser totalizados os seguintes valores:

\- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

\- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAS06__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAS06__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\)\.

__RN1400\-BA\-13__

__Código BAE07 – Aquisição de produto diferido – Eucalipto__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61948: __A partir dessa demanda, a geração do “__BAE07”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem os dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

                                Parametrização para Produto

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de origem\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

 Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE07__”;

\- Somente itens com código de produto parametrizado no menu:

 Parâmetros à Registro 1400 à Específico por UF à BA – Produto para o campo Grupo Produto = “Eucalipto”\.

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

__As regras abaixo são baseadas na DMD \(Declaração da Movimentação de Produtos com ICMS Diferido\), Quadro 09 \- ENTRADAS DE PRODUTOS DIFERIDOS__:

\- Somente itens com Situação Tributária B \(campo COD\_SITUACAO\_B da SAFX08\) = “51”;

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO” OU 

\- Pessoa Fís/Jur informada na nota como Produtor Rural \(campo IND\_PRODUTOR\_RURAL da SAFX04 = “S”\) 

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município de origem__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE07__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAE07__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-14__

__Código BAE08 – Aquisição de produto diferido – Animais Vivos__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE08__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE08__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-15__

__Código BAE09 – Aquisição de produto diferido – Leite Fresco__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE09__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE09__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-16__

__Código BAE10 – Aquisição de produto diferido – Mariscos/Peixes__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE10__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE10__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-17__

__Código BAE11 – Aquisição de produto diferido – Sucatas__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE11__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE11__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-18__

__Código BAE12 – Aquisição de produto diferido – Couros e Peles__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE12__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE12__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-19__

__Código BAE13 – Aquisição de produto diferido – Materiais para combustão__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61948: __A partir dessa demanda, a geração do “__BAE13”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

                                Parametrização para Produto

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de origem\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: 

Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE13__”;

\- Somente itens com código de produto parametrizado no menu: 

Parâmetros à Registro 1400 à Específico por UF para o campo Grupo Produto = “__Materiais para combustão__”

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município de origem__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE13__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “__BAE13__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”:será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-20__

__Código BAE14 – Aquisição de produto diferido – Embalagens e insumos__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS61948: __A partir dessa demanda, a geração do “__BAE14”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                Valores informados manualmente

                                Parametrização CFOP e CFOP/NAT

                                Parametrização para Produto

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de origem\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE14__”;

\- Somente itens com código de produto parametrizados no menu:

Parâmetros à Registro 1400 à Específico por UF para o campo Grupo Produto = “__Embalagens e insumos__”

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município de origem__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE14__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAE14__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado: 

Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”:será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-21__

__Código BAE15 – Aquisição de produto diferido – Cravo da Índia__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE15__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE15__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-22__

__Código BAE16 – Aquisição de produto diferido – Bambu__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

__As regras abaixo são baseadas na DMD \(Declaração da Movimentação de Produtos com ICMS Diferido\), Quadro 09 \- ENTRADAS DE PRODUTOS DIFERIDOS__:

\- Somente itens com Situação Tributária B \(campo COD\_SITUACAO\_B da SAFX08\) = “51”;

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO” OU 

\- Pessoa Fís/Jur informada na nota como Produtor Rural \(campo IND\_PRODUTOR\_RURAL da SAFX04 = “S”\) 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE16__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE16__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__As regras abaixo são baseadas na DMD \(Declaração da Movimentação de Produtos com ICMS Diferido\), Quadro 09 \- ENTRADAS DE PRODUTOS DIFERIDOS__:

\- Somente itens com Situação Tributária B \(campo COD\_SITUACAO\_B da SAFX08\) = “51”;

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO” OU 

\- Pessoa Fís/Jur informada na nota como Produtor Rural \(campo IND\_PRODUTOR\_RURAL da SAFX04 = “S”\) 

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-23__

__Código BAE17 – Aquisição de produto diferido – Resíduo papel/papelão__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE17__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE17__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-24__

__Código BAE18 – Aquisição de produto diferido – Sebo, osso, chifre e casco__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE18__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE18__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-25__

__Código BAE19 – Aquisição de produto diferido – Argila__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE19__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE19__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-BA\-26__

__Código BAE20\-Aquisição de produto diferido – Outros__

__MFS68577: __A partir dessa demanda, a geração do “__BAE20”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Esse código trata Informar o valor das aquisições internas de outros produtos não especificados  nas linhas  anteriores, oriundas  de  contribuintes  não inscritos, inclusive do produtor rural pessoa física inscrito, por município baiano de origem, acobertadas pelo regime de diferimento\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização CFOP e CFOP/NAT

                                  Parametrização para Produto

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por municipio de origem\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\)

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE20__”;

\- Somente itens com código de produto parametrizados no menu:

Parâmetros à Registro 1400 à Específico por UF para o campo Grupo Produto = “__Outros__”

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

 

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais

__Gravação do registro 1400: __

Os itens recuperados conforme os critérios acima, serão totalizados __por município de origem__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE20__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAE20__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado: 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”:será gravado o valor resultante da totalização das notas;

No campo “Deduções”: será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-BA\-27__

__Código BAE99 – Outros ajustes nas entradas__

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__BAE99__*”* 

__As regras abaixo são baseadas na DMD \(Declaração da Movimentação de Produtos com ICMS Diferido\), Quadro 09 \- ENTRADAS DE PRODUTOS DIFERIDOS__:

\- Somente itens com Situação Tributária B \(campo COD\_SITUACAO\_B da SAFX08\) = “51”;

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO” OU 

\- Pessoa Fís/Jur informada na nota como Produtor Rural \(campo IND\_PRODUTOR\_RURAL da SAFX04 = “S”\) 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__BAE99__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\- BA\-28__

__Código BAE80\-ICMS/ST nas Entradas__

__MFS402300: __A partir dessa demanda, a geração do “__BAE80”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Esse código deve tratar o valor do ICMS correspondente à Substituição Tributária \(ST\) destacado nas notas fiscais de entrada\.   

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização CFOP e CFOP/NAT

                                  

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por município de localização do estabelecimento\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\)

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE80__”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve ser um município da

   UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

- Notas com itens à Valor ICMS\-ST do item \(campo 52\-VLR\_SUBST\_ICMS SAFX08\);
- Notas sem itens à Valor ICMS\-ST da nota \(campo 48\-VLR\_SUBST\_ICMS da SAFX07\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE80__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAE80__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\- BA\-29__

__Código BAS80\-ICMS/ST nas Saídas__

__MFS402300: __A partir dessa demanda, a geração do “__BAS80”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Esse código deve tratar o valor do ICMS correspondente à Substituição Tributária \(ST\) destacado nas notas fiscais de saída\.   

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização CFOP e CFOP/NAT

                            

Este código será gerado a partir dos documentos de saída de produtos \(SAFX07/SAFX08\), totalizando os valores por município de localização do estabelecimento\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\)

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAS80__”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve ser um município da UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

- Notas com itens à Valor ICMS\-ST do item \(campo 52\-VLR\_SUBST\_ICMS SAFX08\);
- Notas sem itens à Valor ICMS\-ST da nota \(campo 48\-VLR\_SUBST\_ICMS da SAFX07\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAS80__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAS80__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\- BA\-30__

__Código BAE81\- IPI nas Entradas__

__MFS402301: __A partir dessa demanda, a geração do “__BAE81”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Esse código deve tratar a parcela do IPI que não integra a base de cálculo do ICMS\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização CFOP e CFOP/NAT

                                  

Este código será gerado a partir dos documentos de entrada de produtos \(SAFX07/SAFX08\), totalizando os valores por município de localização do estabelecimento\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\)

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAE81__”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve ser um município da

   UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa\.

__Totalização dos valores:__

- Notas com itens à Valor IPI da nota \(campo 48\- VLR\_IPI da SAFX08\);
- Notas sem itens à Valor IPI da nota \(campo 40\- VLR\_IPI da SAFX07\)\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAE81__”\.

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAE81__”\.

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\)\.

__RN1400\- BA\-31__

__Código BAS81\- IPI nas Saídas__

__MFS402301: __A partir dessa demanda, a geração do “__BAS81”__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Esse código deve tratar a parcela do IPI que não integra a base de cálculo do ICMS\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de produtos \(SAFX07/SAFX08\), totalizando os valores por município de localização do estabelecimento\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\)

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu:

“Parâmetros à Registro 1400 à Específico por UF para o campo Operação = “__BAS81__”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve ser igual a ‘__BA__’;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve ser um município da UF do Estabelecimento\.

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

- Notas com itens à Valor IPI da nota \(campo 48\- VLR\_IPI da SAFX08\);
- Notas sem itens à Valor IPI da nota \(campo 40\- VLR\_IPI da SAFX07\)\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __município do estabelecimento\.__

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__BAS81__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__BAS81__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\)\.

__RN1400\-BA\-Geração Especial__

__\[MFS21172\]__

A geração especial do registro 1400 para BA, será feita quando for selecionada a opção “Utilizar a geração específica para Empresas de Água” do registro 1400 \(Dados para a geração específica \(DMA\-BA\)\) na parametrização de Dados Iniciais \(Parâmetros à Dados Iniciais\)\.

A geração especial dos dados foi executada anteriormente, na rotina de pré\-geração do Registro 1400 – DMA BA \(Pré\-Geração à Registro 1400 – DMA BA\)\.  Os dados gerados foram gravados na tabela de resumo por UF/Município/Produto\.

Os valores gerados serão recuperados da tabela EST\_RES\_MUNIC\_PROD, da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Estado – código do estado igual a “BA”

   

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o código do produto\. 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor contábil\.

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

