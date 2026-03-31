# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_ES

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_ES.docx
- **Modificado:** 2026-01-27
- **Tamanho:** 122 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- ES

__Localização__: 

##### DOCUMENTO DE REQUISITO

__*Data*__

__*Demanda*__

__Descrição__

__Responsável__

08/09/2015

MFS1507

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Ver as observações descritas no cabeçalho do reg\. 1400, e as regras específicas do ES: __RN1400\-ES e RN1400\-ES\-“nn”__\.

Vânia Dias Mattos

11/09/2015

MFS1513

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Geração auitomática dos códigos 01, 02, 03 e 06\. 

\(ver __RN1400\-ES\-01__,__  RN1400\-ES\-02, RN1400\-ES\-03 __e__ RN1400\-ES\-06\)__

Vânia Dias Mattos

14/09/2015

MFS1566

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Geração auitomática dos códigos 05, 07, 09 e 10\. 

\(ver __RN1400\-ES\-05__,__  RN1400\-ES\-07__,__ RN1400\-ES\-09  __e__ RN1400\-ES\-10\)__

Vânia Dias Mattos

29/09/2023

MFS436036

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

Liliane Assaf

21/01/2023

MFS698113

Ajuste das operações automáticas dos códigos ESIPM05, ESIPM06, ESIPM07 e ESIPM10  que foram alterados para ESIPM13005, ESIPM20009, ESIPM30011 e ESIPM43015 respectivamente, com alguns ajustes de regras e sua peridiocidade foi alterada de mensal para anual, onde foram inclusos na rotina de Pré Geração\.  
Ajuste nos códigos ESIPM01, ESIPM02, ESIPM03 e ESIPM09 que foram descontinuados com data fim a partir de 03/10/2024

Graciela Soares

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração – Específico por UF<a id="_Toc75782998"></a> – ES

__RN1400\-ES__

A geração do 1400 para a modalidade “ES” é feita de acordo com os dados solicitados na Portaria N\. 34\-R, de Ago/2015, SEF\-ES\.

__*MFS1507*__*: Alterou a geração do 1400 para o estado do ES\. *Na liberação da MFS1507 todos os códigos serão gerados *apenas* a partir da manutenção do registro 1400\. __*MFS1513*__*: Fez a geração automática dos códigos 01, 02, 03 e 06;*

__*MFS1566*__*: Fez a geração automática dos códigos 05, 07, 09 e 10;*

Os tipos de operação solicitados são os seguintes, conforme os itens descritos na Portaria:

\- Produção rural própria \(código ESIPM01\);

\- Cooperativas e contribuintes que possuam REOA \(código ESIPM02\);

\- Aquisições de pessoas físicas \(código ESIPM03\);

\- Operação de geração de energia elétrica \(código ESIPM04\); 

\- Operação de distribuição de energia elétrica \(código ESIPM05\);

\- Prestação de serviço de transporte intermunicipal e interestadual \(código ESIPM06\);

\- Prestação de serviços de comunicação ou telecomunicação \(código ESIPM07\);

\- Produção de petróleo ou gás natural \(código ESIPM08\);

\- Distribuição de água canalizada \(código ESIPM09\);

\- Distribuição de gás natural canalizado \(código ESIPM10\);

\- Outras atividades \(código ESIPM11\);

\- Fomento agropecuário \(código ESIPM12\);

\- Mudança para outro município \(código ESIPM13\);

As regras estão organizadas da seguinte forma:

__RN1400\-ES\-01__ – geração para o código ESIPM01; \(Geração Automática \- Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-02__ – geração para o código ESIPM02; \(Geração Automática \- Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-03__ – geração para o código ESIPM03; \(Geração Automática \- Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-04__ – geração para o código ESIPM04; \(Geração Manual \-Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-05__ – geração para o código ESIPM05; Código Revogado; Substituído Por ESIPM13005 

__RN1400\-ES\-06__ – geração para o código ESIPM06; Código Revogado; Substituído Por ESIPM20009 

__RN1400\-ES\-07__ – geração para o código ESIPM07; Código Revogado; Substituído Por ESIPM30011

__RN1400\-ES\-08__ – geração para o código ESIPM08; \(Geração Manual \-Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-09__ – geração para o código ESIPM09; \(Geração Automática \- Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-10__ – geração para o código ESIPM010; Código Revogado; Substituído Por ESIPM43015

__RN1400\-ES\-11__ – geração para o código ESIPM011; \(Geração Manual \-Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-12__ – geração para o código ESIPM012; \(Geração Manual \-Código Revogado; Descontinuado em 03/10/2024\);

__RN1400\-ES\-13__ – geração para o código ESIPM013; \(Geração Manual \-Código Revogado; Descontinuado em 03/10/2024\);

\[MFS698113\] Os Código acima foram revogados, os códigos que apresentavam processo manual, não tem impacto, os processos automáticos, cujos códigos, ESIPM05, ESIPM06, ESIPM07 e ESIPM10, serão adaptados para os novos códigos correspondentes ESIPM13005, ESIPM20009, ESIPM30011 e ESIPM43015, conforme asjuste de regras, constantes no novo manual de orientação do Código IPM – ES publicado para 2025\.

Os demias códigos automáticos, não foram atualizados e deverão ser descontinuados\.

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-ES\-01__

__Código ESIPM01 – Produção Rural Própria__

__\[MFS698113\] __Este código foi descontinuado, geração válida até 03/10/2024\.

__*MFS1513*__*: Alterou a geração do código 01 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.*

Este código será gerado a partir das notas de entrada de emissão própria, considerando que para a entrada dos produtos no estabelecimento, vindos de propriedades rurais \(do informante ou arrendadas\), será necessário o contribuinte emitir nota  para acorbertar a entrada dos produtos \(ver item 3\.1 da Portaria n\. 34\-R, Ago/2015\)\. Este foi o conceito utilizado e alinhado junto à Informação para a geração deste item\. 

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente entradas de emissão própria \(MOVTO\_E\_S = “__2__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no  

   menu “Parâmetros à  Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat” 

   para a operação do tipo “__ESIPM01__”

\- O município de origem da nota \(campo 182 da SAFX07\) deve ser um município da

   UF do Estabelecimento

- Considerar o código __ESIPM01__  para gerações com período até 03/10/2024\. 

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM01__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ESIPM01__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                   \[Valor resultante da totalização\] 

                                                         \(\+\)

                    \[Campo “Outros Valores” informado manualmente\]

                                                         \(\-\) 

                 \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+ Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\)\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-ES\-02__

__Código ESIPM02 – Cooperativas e contribuintes que possuam REOA __

__\[MFS698113\] __Este código foi descontinuado, geração válida até 03/10/2024\.

__*MFS1513*__*: Alterou a geração do código 02 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.*

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente entradas de emissão própria \(MOVTO\_E\_S = “__2__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no  

   menu “Parâmetros à  Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat” 

   para a operação do tipo “__ESIPM02__”

\- O município de origem da nota \(campo 182 da SAFX07\) deve ser um município da

   UF do Estabelecimento

- Considerar o código __ESIPM02__  para gerações com período até 03/10/2024\. 

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM02__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ESIPM02__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                   \(\+\)

                \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

               \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+ Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\)\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-ES\-03__

__Código ESIPM03 – Aquisições de pessoas físicas __

__\[MFS698113\] __Este código foi descontinuado, geração válida até 03/10/2024\.

__*MFS1513*__*: Alterou a geração do código 03 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.*

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente entradas de emissão própria \(MOVTO\_E\_S= “__2__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no  

   menu “Parâmetros à  Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat” 

   para a operação do tipo “__ESIPM03__”

\- O município de origem da nota \(campo 182 da SAFX07\) deve ser um município da

   UF do Estabelecimento

- Considerar o código __ESIPM03__  para gerações com período até 03/10/2024\. 

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM03__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ESIPM03__”

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

__RN1400\-ES\-04__

__Código ESIPM04 – Operação de geração de energia elétrica __

\[MFS698113\] Geração Manual, Código revogado, o Contribuinte deve descontinuar a utilização do código\. 

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__ESIPM04__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ESIPM04__” 

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

__RN1400\-ES\-05__

__Código ESIPM05 Substituído por  ESIPM13005  – Operação de distribuição de energia elétrica __

__\[MFS698113\]__ Inclusão do código ESIPM13005 válido a partir de 01/03/2025\. O código  ESIPM05  foi descontinuado\.

__A partir de 2025 este código passa a ser entregue de forma anual para dados superiores ao ano anterior \(2024\) utilizando a rotina de Pré Geração, esta geração automática será descontinuada com data a apartir de 03/10/2024,conforme data fim apresentada na tabela de itens UF Índice de Participação dos Municípios ES do Sped Fiscal\. __

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

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- ESIPM05: considerar para gerações com período até 03/10/2024\.

\- ESIPM13005: considerar para gerações com períodos a partir de 01/03/2025\.

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

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “ESIPM05”

\- ESIPM05: considerar para gerações com período até 03/10/2024\.

\- ESIPM13005: considerar para gerações com períodos a partir de 01/03/2025\.

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

__\[MFS698113\]__  Nova regra, utilizando o processo de Pré Geração, a partir de 01/03/2025:

Origem: \- Tabela da manutenção do registro 1400  

 

Este item será gerado no registro 1400 apenas quando o período da geração for Abril, competência Março\. 

 

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de ES\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\. 

 

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\.  

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ” ESIPM13005” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ” ESIPM13005”

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

__RN1400\-ES\-06__

__Código ESIPM06 Substituído por ESIPM20009   – Prestação de Serviço de Transporte Intermunicipal e Interestadual __

__*MFS1513*__*: Alterou a geração do código 06 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.*

__\[MFS698113\]__ Inclusão do código ESIPM20009 válido a partir de 01/03/2025\. O código  ESIPM06  foi descontinuado\.

__A partir de 2025 este código passa a ser entregue de forma anual para dados superiores ao ano anterior \(2024\) utilizando a rotina de Pré Geração, esta geração automática será descontinuada com data a apartir de 03/10/2024,conforme data fim apresentada na tabela de itens UF Índice de Participação dos Municípios ES do Sped Fiscal\. __

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem do transporte\. Este item *não* usa parametrização de CFOP’s\. As operações são identificadas pelo modelo, tanto para transportes iniciados no ES, como em municípios de outros estados \(ver item 3\.6 da Portaria n\. 34\-R, Ago/2015\)\. No caso de outros estados, o valor será considerado na totalização do município do contribuinte \(emissor do documento\), conforme prevê a Portaria\. Este foi o conceito utilizado e alinhado junto à Informação para a geração deste item\. 

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Classificação = 1, 3 ou 4

   \(a classificação 4 é utilizada nos CTRC’s, e as classificações 1 /3 poderão constar

    na nota fiscal modelo 07 ou no caso dos bilhetes de passagem\)

<a id="_Hlk187910939"></a>\- Data Fiscal \- no período da geração ou data extemporânea no período da  geração;

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve estar preenchido;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

*   \(neste caso, o município de origem pode ser <> "ES”, pois a Portaria cita que os*

*   transportes iniciados em outras UF’s serão registrados p/o munic\. do emitente\) *

\- Notas com *ou* sem itens na SAFX08; 

\- Modelo \(campo 13\) – todos os modelos de documentos de transporte:

07, 08, 8B, 09, 10, 11, 13, 14, 15, 16, 18, 26, 27 e 57, 67

-  ESIPM06: considerar para gerações com período até 03/10/2024\.
- ESIPM20009: considerar para gerações com períodos a partir de 01/03/2025\.

Serão considerandos os modelos de documento de transporte tanto de cargas como de pessoas, conforme prevê a Portaria \(exceto aéreo de passageiro\)\. Trata\-se exatamente dos documentos gravados nos seguintes registros do arquivo: D100, D300 e D400\.

Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

*\(no caso da classificação 4 \(CTRC’s\) as notas não terão itens na SAFX08, já na classificação 1, poderão ou não ter itens\) *

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100/D300/D400, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados nestes registros ou seus registros “filhos”\.

__\[MFS698113\]__  Nova regra, utilizando o processo de Pré Geração, a partir de 01/03/2025:

Origem: \- Tabela da manutenção do registro 1400  

 

Este item será gerado no registro 1400 apenas quando o período da geração for Abril, competência Março\. 

 

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de ES\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\. 

 

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\.  

__Resultado a ser gravado no registro 1400 para cada município:__

__Processamento das notas:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__, da seguinte forma:

\- Se município origem for do estado do “ES” à o valor será totalizado normalmente

  para o município de origem  

\- Se município origem for de outros estados à neste caso o valor será totalizado p/o

  município do contribuinte informante 

 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ ESIPM20009   __” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ ESIPM20009   __”

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

__RN1400\-ES\-07__

__Código ESIPM07 Substituído por ESIPM30011 \- Prestação de serviços de comunicação ou telecomunicação__

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

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- ESIPM07: considerar para gerações com período até 03/10/2024\.

\- ESIPM30011: considerar para gerações com períodos a partir de 01/03/2025\.

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__A partir de 2025 este código passa a ser entregue de forma anual para dados superiores ao ano anterior \(2024\) utilizando a rotina de Pré Geração, esta geração automática será descontinuada com data a apartir de 03/10/2024,conforme data fim apresentada na tabela de itens UF Índice de Participação dos Municípios ES do Sped Fiscal\. __

__\[MFS698113\]__  Nova regra, utilizando o processo de Pré Geração, a partir de 01/03/2025:

Origem: \- Tabela da manutenção do registro 1400  

 

Este item será gerado no registro 1400 apenas quando o período da geração for Abril, competência Março\. 

 

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de ES\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\. 

 

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\.  

__Resultado a ser gravado no registro 1400 para cada município:__

__Processamento das notas__:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\), e

 para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ ESIPM30011__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ ESIPM30011__”

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

__RN1400\-ES\-08__

__Código ESIPM08 – Produção de petróleo ou gás natural __

\[MFS698113\] Geração Manual, Código revogado, o Contribuinte deve descontinuar a utilização do código\. 

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__ESIPM08__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ESIPM08__” 

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

__RN1400\-ES\-09__

__Código ESIPM09 \- Distribuição de água canalizada__

__\[MFS698113\] __Este código foi descontinuado, geração válida até 03/10/2024\.

<a id="_Hlk72410958"></a>Origem: \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 	

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do ES\. 

<a id="_Hlk72413027"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos   C500 ou C600 para o segmento de água\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

   

\- \(Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “29”\) 

   __ou__ 

\- \(Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “01” __e__ Empresa é do

   segmento de água\) __\(\*\)__

__*\(\*\)*__* A verificação do segmento é feita através do CNAE, deve ser = *4100901*\. O filtro do modelo do documento é diferente para os segmentos de gás e água, pois alguns contribuintes ainda utilizam o modelo 01, ao invés dos códigos específicos 28 e 29, porque várias obrigações ainda não tratam este códigos\.   *

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

- Considerar o código __ESIPM01__  para gerações com período até 03/10/2024\. 

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

<a id="_Hlk72414048"></a>Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__ESIPM09__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ESIPM09__”

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

\- O valor totalizado das notas \(X42/X43\) será gravado no campo “Valor Apurado”;

\- O valor final \(valor gravado no 1400\) será gravado no campo “Valor Total”;

__RN1400\-ES\-10__

__Código ESIPM10 Substituído por ESIPM43015 \- Distribuição de gás natural canalizado__

__\[MFS698113\]__ Inclusão do código ESIPM43015 válido a partir de 01/03/2025\. O código  ESIPM10  foi descontinuado\.

__A partir de 2025 este código passa a ser entregue de forma anual para dados superiores ao ano anterior \(2024\) utilizando a rotina de Pré Geração, esta geração automática será descontinuada com data a apartir de 03/10/2024,conforme data fim apresentada na tabela de itens UF Índice de Participação dos Municípios ES do Sped Fiscal\. __

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

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “ES”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- ESIPM10: considerar para gerações com período até 03/10/2024\.

\- ESIPM43015: considerar para gerações com períodos a partir de 01/03/2025\.

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Apuração do total das deduções a ser rateado entre os municípios:__

O valor total a ser rateado será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

*\(o tratamento das deduções é o mesmo descrito para o item ESIPM05 – EE\)*

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

    CFOP/Nat” para a operação do tipo “__ESIPM10__ 

\- ESIPM10: considerar para gerações com período até 03/10/2024\.

\- ESIPM43015: considerar para gerações com períodos a partir de 01/03/2025\.

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

__\[MFS698113\]__  Nova regra, utilizando o processo de Pré Geração, a partir de 01/03/2025:

Origem: \- Tabela da manutenção do registro 1400  

 

Este item será gerado no registro 1400 apenas quando o período da geração for Abril, competência Março\. 

 

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de ES\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\. 

 

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\.  

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

__RN1400\-ES\-11__

__Código ESIPM11 – Outras atividades __

\[MFS698113\] Geração Manual, Código revogado, o Contribuinte deve descontinuar a utilização do código\. 

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__ESIPM11__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ESIPM11__” 

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

__RN1400\-ES\-12__

__Código ESIPM12 – Fomento agropecuário__

\[MFS698113\] Geração Manual, Código revogado, o Contribuinte deve descontinuar a utilização do código\. 

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__ESIPM12__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ESIPM12__” 

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

__RN1400\-ES\-13__

__Código ESIPM13 – Mudança para outro município__

\[MFS698113\] Geração Manual, Código revogado, o Contribuinte deve descontinuar a utilização do código\. 

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__ESIPM13__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ESIPM13__” 

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

