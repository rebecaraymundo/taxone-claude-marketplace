# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_RJ

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_RJ.docx
- **Modificado:** 2025-10-14
- **Tamanho:** 111 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- RJ

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS35221

Aline Melo

Inclusão dos códigos RJVAF20002 e RJVAF20003 no processo de geração automática do registro 1400, para o estado do Rio de Janeiro

20/09/2021

MFS86117

Aline Melo

Inclusão dos códigos RJVAF00006 e RJVAF10006 no processo de geração automática do registro 1400, para o estado do Rio de Janeiro

27/05/2022

MFS547634

Graciela Soares

Inclusão dos códigos RJVAF00005 e RJVAF10005 no processo de geração automática do registro 1400, para o estado do Rio de Janeiro

21/05/2023

MFS556958

Graciela Soares

Inclusão dos códigos RJVAF00009 e RJVAF10009 no processo de geração automática do registro 1400, para o estado do Rio de Janeiro

07/08/2023

MFS551008

Graciela Soares

Inclusão dos códigos RJVAF00007 e RJVAF10007 no processo de geração automática do registro 1400, para o estado do Rio de Janeiro

12/09/2023

MFS436036

Liliane Assaf

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

29/09/2023

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração – Específico por UF<a id="_Toc75782998"></a> – RJ

__RN1400\-RJ__

A geração do 1400 para a modalidade “RJ” foi desenvolvida de acordo com os dados solicitados na Portaria nº 52, de 21/12/18\. 

Para os códigos os valores serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__Código selecionado \(\*\)__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__  este campo será preenchido com ”__ Código selecionado \(\*\)__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo  Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

Resultado final = zero  O registro 1400 não será gravado para este município;

__\(\*\) Código selecionado__ – o código será um dos códigos cadastrados na TACES89 para RJ\.  Exemplo: RJVAF20001\. 

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

Para os códigos abaixo, o registro será gerado de forma automática:

__RJVAF20002__ – Valor adicionado por aquisições de produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários sem nota fiscal de produtor\.

Ver regra __RN1400\-RJ\-01__;

__RJVAF20003 __\- Valor adicionado pela prestação de serviço de transporte intermunicipal e interestadual\.

Ver regra __RN1400\-RJ\-02__;

__RJVAF00006__ \-  Contribuinte autorizado, em processo ou legislação específica, a consolidar valor adicionado de outros estabelecimentos ou locais em sua declaração\.

Ver regra __RN1400\-RJ\-03 __

__RJVAF10006 \- __Contribuinte autorizado, em processo ou legislação específica, a consolidar valor adicionado de outros estabelecimentos ou locais em sua declaração\.

Ver regra __RN1400\-RJ\-04 __

__RJVAF00005\- __Prestação de serviço de comunicação ou telecomunicação oneroso para consumidor final \- Valor das Entradas

Ver regra __RN1400\-RJ\-05 __

__RJVAF10005 \- __Prestação de serviço de comunicação ou telecomunicação oneroso para consumidor final \- Valor das Saídas

Ver regra __RN1400\-RJ\-06__

__RJVAF00009 – __Fornecimento de Gás Natural Canalizado__ \- __Valor das Entradas

Ver regra __RN1400\-RJ\-07 __

__RJVAF00009 – __Fornecimento de Gás Natural Canalizado__ \- __Valor das Saídas

Ver regra __RN1400\-RJ\-08 __

__RJVAF00007 – __Fornecimento de energia elétrica por distribuidora \- Valor das Entradas

Ver regra __RN1400\-RJ\-09 __

__RJVAF00007 – __Fornecimento de energia elétrica por distribuidora \- Valor das Saídas

Ver regra __RN1400\-RJ\-10 __

__RN1400\-RJ\-01__

__Código RJVAF20002 – Valor adicionado por aquisições de produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários sem nota fiscal de produtor\.__

__MFS72445:__ A partir dessa demanda, a geração do código “RJVAF20002”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

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

\- Modelo \(campo13\-MODELO da SAFX07\) igual a 01, 1B, 04, 55 ou 65;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);

\- Somente notas com itens;

\- Somente itens de mercadoria;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- CFOP ou CFOP/NAT do item da nota parametrizados no menu “Parâmetros  

  Registro 1400  Específico por UF” para o operação “RJVAF20002”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve estar preenchido;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

__Totalização dos valores:__

\- Será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

__OBS__: 

Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__  este campo será preenchido com o conteúdo ”__RJVAF20002__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = ”__ RJVAF20002__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo  Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero  O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-02__

__Código RJVAF20003 \- Valor adicionado pela prestação de serviço de transporte intermunicipal e interestadual\.__

__MFS72445:__ A partir dessa demanda, a geração do código “RJVAF20003”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saídas de transporte \(identificados pelo modelo\), totalizando os valores por município de origem\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais gravadas nos registros no __D100, D300 e D400\.__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais gravadas nos registros no __D100, D300 e D400__ que atendam aos seguintes critérios:

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 07, 08, 8B, 09, 10, 11, 13, 14, 15, 16, 18,

26, 27, 57 e 67;

Para a correta geração dos registros baseados no D100, D300 e D400, seguir a combinação:

 

__Baseados no registro D100__

__Origem SAFX07 e SAFX08__

Classificação Fiscal = ‘1’ __E__ Modelo de Documnto = ’07, ‘08’, ‘57’ ou ‘67’;

__Origem SAFX07__

Classificação Fiscal =’4’ __E__ Modelo de Documento =’08’, ‘8B’, ‘09’, ‘10’, ‘11’, ‘26’, ‘27’, ‘57’ ou ‘67’;

__Baseados no registro D300 \- Origem SAFX07 e SAFX08__

Classificação Fiscal = ‘1’ ou ‘3’ __E__ Modelo de Documento =’13’, ‘14’, ‘15’ ou ‘16’;

__Baseados no registro D400 \- Origem SAFX07 e SAFX08__

Classificação Fiscal = ‘1’ ou ‘3’ __E__ Modelo de Documento = ‘18’

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 3 ou 4;

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros  

  Registro 1400  Específico por UF” para o operação “__RJVAF20003__”;

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

__02\-COD\_ITEM\_IPM__  este campo será preenchido com o conteúdo ”__RJVAF20003__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Regitsro 1400”\)\.

  

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ RJVAF20003__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo  Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero  O registro 1400 não será gravado para este município\.

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-03__

__Código RJVAF00006 \- Contribuinte autorizado, em processo ou legislação específica, a consolidar valor adicionado de outros estabelecimentos ou locais em sua declaração \(Valores de Entrada\)__

__MFS86117:__ A partir dessa demanda, a geração do código “RJVAF00006”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir da __soma das notas de entradas__,  ocorridas em todos os estabelecimentos centralizados, totalizando os valores por município de origem\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais gravadas no registro __C100\.__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento __CENTRALIZADOR__

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = __55__ e __65__

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 3 ou 4;

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros  

  Registro 1400  Específico por UF” para o operação “__RJVAF00006__”;

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

1. Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__  este campo será preenchido com o conteúdo ”__RJVAF00006__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Regitsro 1400”\)\.

  

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ RJVAF00006__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo  Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero  O registro 1400 não será gravado para este município\.

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-04__

__Código RJVAF10006 \- Contribuinte autorizado, em processo ou legislação específica, a consolidar valor adicionado de outros estabelecimentos ou locais em sua declaração \(Valores de Saída\)__

__MFS86117:__ A partir dessa demanda, a geração do código “RJVAF10006”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir da __soma das notas de saídas__,  ocorridas em todos os estabelecimentos centralizados, totalizando os valores por município de origem\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais gravadas no registro __C100\.__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento __CENTRALIZADOR__

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = __55__ e __65__

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 3 ou 4;

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros  

  Registro 1400  Específico por UF” para o operação “__RJVAF10006__”;

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

1. Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__  este campo será preenchido com o conteúdo ”__RJVAF10006__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Regitsro 1400”\)\.

  

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__ RJVAF10006__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo  Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero  O registro 1400 não será gravado para este município\.

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-05__

<a id="OLE_LINK13"></a>__Código RJVAF00005\- Prestação de serviço de comunicação ou telecomunicação oneroso para consumidor final \- Valor das Entradas__

Origem: Notas Fiscais \(SAFX07, SAFX08 e SAFX09\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros  Registro 1400  Específico p/UF  CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada de comunicação/telecomunicação \(identificados pelo modelo\), totalizando o valor contábil das entradas e aquisições de serviço de comunicação, por município do Rio de Janeiro\.

__Apuração do valor referente a cada entrada na SAFX07/SAFX08/SAFX09:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 21 ou 22 ou 62;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros   Registro 1400  Específico por UF” para a operação “__RJVAF00005__”;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de RJ \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

Valor a ser totalizado:

- Notas com itens classificação fiscal 1  valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) 
- Notas com itens classificação fiscal 3  valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\)  \+ valor total do serviço do item \(campo 15 \- VLR\_TOT SAFX09\);
- Notas sem itens  valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__  este campo será preenchido com o seguinte conteúdo: “__RJVAF00005__” 

__03\-MUN__  Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __ Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração  Manutenção  Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__RJVAF00005__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo  Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero  O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-06__

<a id="OLE_LINK266"></a>__Código RJVAF10005\- Prestação de serviço de comunicação ou telecomunicação oneroso para consumidor final \- Valor das Saídas__

Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

Apuração do valor referente a cada município na SAFX42/SAFX43:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 21, 22, ‘62’;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FIS da SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__RJVAF10005__”;
- <a id="OLE_LINK20"></a>Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de RJ \(campo 75\-UF\_CONSUMO da SAFX42\);

OBS: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município do terminal faturado\. 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Gravação do registro 1400:

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “RJVAF10005” 

03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

__      __“RJVAF10005__” __

Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

Gravação dos valores para tela da manutenção:

O valor resultante da totalização das notas fiscais, o valor das deduções e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-RJ\-07__

__Código RJVAF00009 – Fornecimento de Gás Natural Canalizado \(entrada\)  __

Origem: Notas Fiscais \(SAFX07, SAFX08 e SAFX09\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

              \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada de comercialização e distribuição de água canalizada \(identificados pelo modelo\), totalizando o valor contábil das entradas e insumos utilizados na comercialização e distribuição de Gás Natural Canalizado, por município do Rio de Janeiro\.

Apuração do valor referente a cada entrada na SAFX07/SAFX08/SAFX09:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 28;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual  a 1 ou 3 \(no caso de nota mista \(classif\. = 3\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “RJVAF00009”;
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de RJ \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

OBS: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município do ponto de consumo/ terminal faturado\. 

Valor a ser totalizado:

- Notas com itens classificação fiscal 1  valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) 
- Notas com itens classificação fiscal 3  valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\)  \+ valor total do serviço do item \(campo 15 \- VLR\_TOT SAFX09\);
- Notas sem itens  valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “RJVAF00009” 

03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “RJVAF00009” 

Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

Gravação dos valores para tela da manutenção:

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total\.

<a id="OLE_LINK9"></a>__RN1400\-RJ\-08__

__Código RJVAF10009 \-  Fornecimento de Gás Natural Canalizado \(saída\)  __

<a id="_Hlk72412790"></a>Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comercialização e distribuição de Gás Natural Canalizado \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

<a id="_Hlk72413078"></a>Apuração do valor referente a cada município na SAFX42/SAFX43:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 28;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FIS da SAFX42\) igual a 1;
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “RJVAF10009”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de RJ \(campo 75\-UF\_CONSUMO da SAFX42\);

OBS: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

<a id="_Hlk72414095"></a>Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município do terminal faturado\. 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “RJVAF10009” 

03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “RJVAF10009” 

Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

Gravação dos valores para tela da manutenção:

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

<a id="OLE_LINK27"></a><a id="OLE_LINK28"></a><a id="OLE_LINK29"></a><a id="OLE_LINK30"></a>__RN1400\-RJ\-09__

<a id="OLE_LINK26"></a>__Código RJVAF00007 \- Fornecimento de energia elétrica por distribuidora \- Valor das Entradas__

__Origem: Notas Fiscais \(SAFX07 e SAFX08\)__

__              Valores informados manualmente __

__              Parametrização de CFOP e CFOP/NAT__

__               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)__

__Este código será gerado a partir dos documentos de entrada de comercialização e distribuição de energia elétrica \(identificados pelo modelo\), totalizando o valor contábil das entradas e insumos utilizados na comercialização e distribuição de energia elétrica, por município do Rio de Janeiro, excluindo\-se as operações dedutíveis\.__

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- __Código da empresa igual da empresa informada na tela de geração;__
- __Código do estabelecimento igual do estabelecimento informado na tela de geração;__
- __Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);__
- __Data Fiscal no período da geração ou data extemporânea no período de geração;__
- __Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 06 ou 66;__
- __Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);__
- __Notas com ou sem itens;__
- __Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);__
- __CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “RJVAF00007”;__
- __As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;__
- __Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de RJ \(campo 207\-UF\_CONSUMO da SAFX07\);__

__Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;__

__Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;__

__OBS: __

__1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.__

__2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.__

__Processamento das notas:__

__As notas/itens recuperados conforme os critérios acima serão totalizados por município do ponto de consumo/ terminal faturado\. __

__Valor a ser totalizado:__

- __Notas com itens classificação fiscal 1 ou 3 __ valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- __Notas sem itens __ __valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);__

__Gravação do registro 1400:__

__O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:__

__02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “RJVAF00007” __

__03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.__

__04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.__

__Estes valores informados manualmente serão recuperados da seguinte forma:__

__   \- Estabelecimento – estabelecimento da geração__

__   \- Período – mesmo período da tela da geração \(data inicial e final\)__

__   \- Município – município da totalização __

__   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = __

__      “RJVAF00007” __

__Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:__

__ __

__                                  \[Valor resultante da totalização\] __

__                                                      \(\+\)__

__                  \[Campo “Outros Valores” informado manualmente\]__

__                                                      \(\-\) __

__                \[Campo “Outras Deduções” informado manualmente\]__

__Crítica:__

__Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:__

__Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.__

__Resultado final = zero à O registro 1400 não será gravado para este município;__

__Gravação dos valores para tela da manutenção:__

__O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. __

__O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.__

__RN1400\-RJ\-10__

__Código RJVAF10007 \- Fornecimento de energia elétrica por distribuidora – Valor das Saídas__

<a id="_Hlk72402711"></a>__Origem: Notas Fiscais \(SAFX42 e SAFX43\)__

__              Valores informados manualmente __

__              Parametrização de CFOP e CFOP/NAT__

__               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)__

__Este código será gerado a partir dos documentos de saídas de comercialização e distribuição de energia elétrica \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.__

<a id="_Hlk72402725"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

- __Código da empresa igual da empresa informada na tela de geração;__
- __Código do estabelecimento igual do estabelecimento informado na tela de geração;__
- __Somente notas de saída \(SAFX42 se aplica apenas para saídas\);__
- __Data Fiscal no período da geração ou data extemporânea no período de geração;__
- __Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 06 ou 66;__
- __Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);__
- __Notas com itens \(documentos utilities sempre terão itens\);__
- __Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);__
- __Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);__
- __CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “RJVAF10007”;__
- __Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de RJ \(campo 75\-UF\_CONSUMO da SAFX42\);__

<a id="_Hlk72402747"></a>__OBS: __

__1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.__

__2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.__

__Processamento das notas:__

__As notas/itens recuperados conforme os critérios acima serão totalizados por município do terminal faturado\. __

__Valor a ser totalizado:__

- __Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);__

__Gravação do registro 1400:__

__O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:__

__02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “RJVAF10007” __

__03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.__

__04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.__

__Estes valores informados manualmente serão recuperados da seguinte forma:__

__   \- Estabelecimento – estabelecimento da geração__

__   \- Período – mesmo período da tela da geração \(data inicial e final\)__

__   \- Município – município da totalização __

__   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = __

__      “RJVAF10007” __

__Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:__

__ __

__                                  \[Valor resultante da totalização\] __

__                                                      \(\+\)__

__                  \[Campo “Outros Valores” informado manualmente\]__

__                                                      \(\-\) __

__                \[Campo “Outras Deduções” informado manualmente\]__

__Crítica:__

__Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:__

__Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.__

__Resultado final = zero à O registro 1400 não será gravado para este município;__

__Gravação dos valores para tela da manutenção:__

__O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. __

__O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.__

