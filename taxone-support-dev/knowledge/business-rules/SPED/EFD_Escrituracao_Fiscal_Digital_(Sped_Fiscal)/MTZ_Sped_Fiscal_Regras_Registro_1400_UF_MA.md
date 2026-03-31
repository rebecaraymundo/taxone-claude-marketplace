# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_MA

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_MA.docx
- **Modificado:** 2024-10-21
- **Tamanho:** 89 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- MA

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS47088

Aline Melo

Criação do documento\.

Inclusão de todos os códigos no processo de geração manual e dos códigos MAVAF005, MAVAF006 e MAVAF007 no processo automático do registro 1400, para o estado de Maranhão\.

13/10/2021

MFS651551

Liliane Assaf

Geração automática do código MAVAF002

02/09/2024

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- MA

__RN1400\-MA__

A geração do 1400 para a modalidade “MA” foi desenvolvida de acordo com os dados solicitados na Portaria nº 52, de 21/12/18\.

 

Para os códigos abaixo, os valores serão gerados <a id="_Hlk535225528"></a>apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MAVAF001__ \- Atividades de Distribuição de Energia Elétrica;

__MAVAF003__ \- Produção de Petróleo e Gás Natural \- Na Hipótese da Produção se Estender por Mais de um Município;

__MAVAF004__ \- Atividades de Prestação de Serviço de Transporte Ferroviário de Passageiros\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__Código selecionado \(\*\)__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ Código selecionado \(\*\)__” 

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

__\(\*\) Código selecionado__ – o código será um dos códigos cadastrados na TACES89 para MA\.  

Exemplo: __MAVAF001__\. 

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

Para os códigos abaixo, o registro será gerado de forma automática e via tela de manutenção:

__MAVAF002__ \- Atividades de Prestação de Serviços de Comunicação/Telecomunicação;

Ver regra __RN1400\-MA\-01__; \[MFS651551\]

__MAVAF005 \-__ Prestação de Serviço de Transporte Rodoviário Intermunicipal e Interestadual de Passageiros\. 

Ver regra __RN1400\-MA\-02__;

__MAVAF006__ \- Prestação de Serviço de Transporte Aquaviário de Passageiros\. 

Ver regra __RN1400\-MA\-03__;

__MAVAF007:__ Aquisições de produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários sem NFA\-e do produtor\. 

Ver regra __RN1400\-MA\-04\.__

__RN1400\-MA\-01__

__Código MAVAF002 \- Atividades de Prestação de Serviços de Comunicação/Telecomunicação__

\[MFS651551\]: Inclusão da geração automática do 1400 para o código MAVAF002\.

Base Legal: PORTARIA Nº 164/20 – GABIN

*\*não será tratada a parametrização para Deduções, pois a Portaria não fornece esclarecimentos\. Para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\.*

__Origem dos dados:__ Notas Fiscais \(SAFX42 e SAFX43\)

                                  Valores informados manualmente 

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

Apuração do valor referente a cada município na SAFX42/SAFX43:

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

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__MAVAF002__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR__ à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

__      __“__MAVAF002” __

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “*O campo VALOR esta com conteúdo inválido \(valor negativo\)*”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-MA\-02__

__Código MAVAF005 \- Prestação de Serviço de Transporte Rodoviário Intermunicipal e Interestadual de Passageiros__

__MFS47088:__ A partir dessa demanda, a geração do código “MAVAF005”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de transporte __rodoviário intermunicipal e interestadual de passageiros__ \(identificados pelo modelo\), totalizando os valores por município de origem\.

Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de __saída__ gravadas no registro no __D100 e D300__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 07, 13 e 67;

__Baseados no registro D100__

__Origem SAFX07 e SAFX08 \(Notas com item e sem item\)__

Classificação Fiscal = ‘1’ __E__ Modelo de Documento = ’07’ ou ‘67’;

__Origem SAFX07 \(Notas somente sem item\)__

Classificação Fiscal =’4’ __E__ Modelo de Documento = ‘67’

__Baseados no registro D300 \- Origem SAFX07 \(Notas somente sem item\)__

Classificação Fiscal = ‘1’ ou ‘3’ __E__ Modelo de Documento = ‘13’\.

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 4;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à   Registro 1400 à Específico por UF” para o operação “MAVAF005”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve estar preenchido;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

\- Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

\- Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

\- Para as notas com itens \(Classificação = ‘1’ ou ‘3’\): será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

\- Para as notas sem itens \(Classificação = ‘1’ ou ‘4’\): será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Os CTRC’s com classificação 4 não possuem itens da SAFX08\. 

Classificação Fiscal = 3 é somente item, por se tratar de nota mista\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ” __MAVAF005__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__MAVAF005__”

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

__RN1400\-MA\-03__

__Código MAVAF006 \- Prestação de Serviço de Transporte Aquaviário de Passageiros__

__MFS47088:__ A partir dessa demanda, a geração do código “MAVAF006”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de transporte __aquaviário de passageiros__ \(identificados pelo modelo\), totalizando os valores por município de origem\.

Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de __saída__ gravadas no registro __D300\.__

__Critérios de recuperação das notas na SAFX07:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 14;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à   Registro 1400 à Específico por UF” para o operação “MAVAF006”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve estar preenchido;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

\- Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

\- Para as notas sem itens \(Classificação = ‘1’\): será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__MAVAF006__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__MAVAF006__”

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

__RN1400\-MA\-04__

__Código MAVAF007\-Aquisições de produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários sem NFA\-e do produtor\.__

__MFS47088:__ A partir dessa demanda, a geração do código “MAVAF007”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de entrada de mercadorias, emitidas pelo contribuinte \(Emissão Própria\) , para acobertar a entrada dos produtos, totalizando por municipio de origem \(localização do produtor remetente\)\.

Para apurar o total das operações deste item, será feita a totalização das notas fiscais de __entradas__  gravadas nos registros no __C100\.__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada de emissão própria \(MOVTO\_E\_S da SAFX07 = “__2__”\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo 13\-MODELO da SAFX07\) igual a 01, 1B, 04, 55 ou 65;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);

\- Somente notas com itens;

\- Somente itens de mercadoria;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à 

  Registro 1400 à Específico por UF” para a operação “MAVAF007”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve estar preenchido;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido\.

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__MAVAF007__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__MAVAF007__”

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

