# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_TO

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_TO.docx
- **Modificado:** 2025-02-06
- **Tamanho:** 139 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- TO

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS35318

Aline Melo

Criação do documento\.

Inclusão do código TOIPMS10 no processo automático de geração do registro 1400, estado de Tocantins\.

18/08/2021

MFS94466

Andréa Rocha

Alteração das regras para preencher o código do munícipio para o código TOIPMS10, de acordo com o tipo de CFOP\.

09/12/2022

MFS99537

Liliane Assaf

Alteração na geração do 1400 tipo de geração “Específicos por UF para Tocantins, na geração do código TOIPME08, para considerar os documentos fiscais de entrada de modelo 62 \(SAFX07/SAFX08\)\.

03/01/2023

MFS436036

Liliane Assaf

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

29/09/2023

MFS710672

Graciela Soares

Inclusão do modelo 66 na regra dos códigos TOIPME06 \- Energia Elétrica \(entrada\) e TOIPMS06 \- Energia Elétrica \(saída\)

03/02/2025

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- TO

__RN1400\-TO__

A geração do 1400 para a modalidade “TO” foi desenvolvida de acordo com os dados solicitados na Portaria nº 265, de 23 de março de 2018\.

 

As regras estão organizadas da seguinte forma:

__RN1400\-TO\-01__ – geração para o código “TOIPME04”

__RN1400\-TO\-02__ – geração para o código “TOIPMS04”

__RN1400\-TO\-03__ – geração para o código “TOIPME06”

__RN1400\-TO\-04__ – geração para o código “TOIPMS06”

__RN1400\-TO\-05__ – geração para o código “TOIPME07”

__RN1400\-TO\-06__ – geração para o código “TOIPMS07”

<a id="OLE_LINK256"></a>__RN1400\-TO\-07__ – geração para o código “TOIPME08”

__RN1400\-TO\-08__ – geração para o código “TOIPMS08”

<a id="OLE_LINK257"></a>__RN1400\-TO\-09__ – geração para o código “TOIPME01”

__RN1400\-TO\-10__ – geração para o código “TOIPMS01”

<a id="OLE_LINK258"></a>__RN1400\-TO\-11__ – geração para o código “TOIPME02”

__RN1400\-TO\-12__ – geração para o código “TOIPMS02”

<a id="OLE_LINK259"></a>__RN1400\-TO\-13__ – geração para o código “TOIPME03”

__RN1400\-TO\-14__ – geração para o código “TOIPMS03”

__RN1400\-TO\-15__ – geração para o código “TOIPME05”

__RN1400\-TO\-16__ – geração para o código “TOIPMS05”

__RN1400\-TO\-17__ – geração para o código “TOIPME09”

__RN1400\-TO\-18__ – geração para o código “TOIPMS09”

__RN1400\-TO\-19__ – geração para o código “TOIPME10”

__RN1400\-TO\-20__ – geração para o código “TOIPMS10”

__RN1400\-TO\-21__ – geração para o código “TOIPME11”

__RN1400\-TO\-22__ – geração para o código “TOIPMS11”

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-TO\-01__

__Código TOIPME04 – Transporte \(entrada\)__

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos da aquisição do transporte \(identificados pelo modelo\), totalizando o valor   contábil   das   entradas   e   aquisições   de   serviço   de   transporte intermunicipal e/ou interestadual, por município tocantinense, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada aquisição na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no __D100__ que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPME04__”;
- Serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja de TO \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

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
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “TO”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPME04__”;

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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME04__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME04__” 

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

__RN1400\-TO\-02__

__Código TOIPMS04 – Transporte \(saída\)__

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPMS04__”;
- No caso das notas de classificação 1 ou 3 serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja de TO \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);
- No caso das notas de classificação 4, 5 ou 6 serão consideradas apenas as notas em que em que o município de origem da SAFX07 seja de TO ou, quando este não for informado, o município da coleta na SAFX51 seja de TO \(campos 62\-COD\_ESTADO\_COLETA e 42\-COD\_MUNIC\_COLETA da SAFX51\);

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

Ao utilizar o município de coleta da SAFX51, caso exista mais de um item de frete para o mesmo documento, e eles tiverem municípios de coleta *diferentes*, será gravada a seguinte mensagem no log, e o documento *não* será considerado:* “Existem na base de dados itens de frete para o documento com mais de um município de coleta\. O documento não será considerado p/o registro 1400, código TOIPMS04”\. *Caso o município da SAFX51 também não esteja preenchido, será gravada a seguinte mensagem no log, e o documento *não* será considerado: *“Para gerar o registro 1400, cód TOIPMS04, é necessário que o município de origem esteja preenchido \(UF/munic origem da SAFX07 ou munic Coleta da SAFX51\)\. O documento não será considerado”\.*

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
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “TO”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPMS04__”;

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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPMS04__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS04__” 

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

<a id="OLE_LINK27"></a><a id="OLE_LINK28"></a><a id="OLE_LINK29"></a><a id="OLE_LINK30"></a>__RN1400\-TO\-03__

<a id="OLE_LINK26"></a>__Código __<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>__TOIPME06 \- Energia Elétrica \(entrada\)  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada de comercialização e distribuição de energia elétrica \(identificados pelo modelo\), totalizando o valor contábil das entradas e insumos utilizados na comercialização e distribuição de energia elétrica, por município tocantinense, excluindo\-se as operações dedutíveis\.

__\[MFS710672\] __Inclusão do modelo de nota “66”

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 06 ou 66;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “<a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>__TOIPME06__”;
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “<a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>__TOIPME06__”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.* 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME06__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME06__” 

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

__RN1400\-TO\-04__

__Código __<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a><a id="OLE_LINK35"></a>__TOIPMS06 \- Energia Elétrica \(saída\)  __

<a id="_Hlk72402711"></a>Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comercialização e distribuição de energia elétrica \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

__\[MFS710672\] __Inclusão do modelo de nota “66”

<a id="_Hlk72402725"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 06 ou 66;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “<a id="OLE_LINK36"></a><a id="OLE_LINK37"></a>__TOIPMS06__”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

<a id="_Hlk72402747"></a>__OBS:__ 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Processamento das notas__:

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPMS06__”;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);
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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPMS06__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS06__” 

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

__RN1400\-TO\-05__

__Código TOIPME07 \- Água Canalizada \(entrada\)  __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada de comercialização e distribuição de água canalizada \(identificados pelo modelo\), totalizando o valor contábil das entradas e insumos utilizados na comercialização e distribuição de água canalizada, por município tocantinense, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 29;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPME07__”;
- As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPME07__”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.* 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME07__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME07__” 

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

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total\.

<a id="OLE_LINK9"></a>__RN1400\-TO\-06__

__Código TOIPMS07 \- Água Canalizada \(saída\)  __

<a id="_Hlk72412790"></a>Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comercialização e distribuição de água canalizada \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

<a id="_Hlk72413078"></a>__Apuração do valor referente a cada município na SAFX42/SAFX43:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 29;
- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\);
- Notas com itens \(documentos utilities sempre terão itens\);
- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FISda SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPMS07__”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

__OBS:__ 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

<a id="_Hlk72414095"></a>__Processamento das notas__:

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPMS07__”;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);
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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPMS07__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS07__” 

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

__RN1400\-TO\-07__

<a id="OLE_LINK13"></a>__Código __<a id="OLE_LINK21"></a><a id="OLE_LINK31"></a>__TOIPME08\- Comunicação e Telecomunicação \(entrada\) __

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entrada de comunicação/telecomunicação \(identificados pelo modelo\), totalizando o valor contábil das entradas e aquisições de serviço de comunicação, por município tocantinense, excluindo\-se as operações dedutíveis\.

__\[MFS99537\] Inclusão do Modelo 62__

__Apuração do valor referente a cada entrada na SAFX07/SAFX08:__

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 21 ou 22 ou 62;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPME08__”;
- Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “<a id="OLE_LINK65"></a><a id="OLE_LINK66"></a><a id="OLE_LINK67"></a><a id="OLE_LINK68"></a><a id="OLE_LINK69"></a><a id="OLE_LINK70"></a><a id="OLE_LINK71"></a><a id="OLE_LINK72"></a>__TOIPME08__”;
- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.* 

Valor a ser totalizado:

- Será totalizado o valor do serviço \(campo 19\-VLR\_SERVICO da SAFX43\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME08__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME08__” 

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

__RN1400\-TO\-08__

<a id="OLE_LINK266"></a>__Código TOIPMS08\- Comunicação e Telecomunicação \(saída\) __

Origem: Notas Fiscais \(SAFX42 e SAFX43\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPMS08__”;
- <a id="OLE_LINK20"></a>Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de TO \(campo 75\-UF\_CONSUMO da SAFX42\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

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
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPME08__”;
- <a id="OLE_LINK14"></a>Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de TO \(campo 207\-UF\_CONSUMO da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

<a id="OLE_LINK15"></a>As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.* 

Valor a ser totalizado:

- Notas com itens à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Notas sem itens à valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME08__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME08__” 

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

__RN1400\-TO\-09__

__Código TOIPME01\- Agricultura \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “<a id="OLE_LINK267"></a><a id="OLE_LINK268"></a>__TOIPME01__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPME01__” 

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

__RN1400\-TO\-10__

__Código TOIPMS01\- Agricultura \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS01__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPMS01__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este Município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-TO\-11__

__Código TOIPME02\- Pecuária \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “<a id="OLE_LINK275"></a><a id="OLE_LINK276"></a><a id="OLE_LINK277"></a>__TOIPME02__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPME02__” 

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

__RN1400\-TO\-12__

__Código TOIPMS02\- Pecuária \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS02__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPMS02__” 

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

__RN1400\-TO\-13__

__Código TOIPME03\- Pesca \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME03__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPME03__” 

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

__RN1400\-TO\-14__

__Código TOIPMS03\- Pesca \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS03__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPMS03__” 

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

__RN1400\-TO\-15__

__Código TOIPME05\- Produção de Energia Elétrica \(Usinas\) \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS35133__: A partir desta demanda, a geração do __TOIPME05__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

 

Origem dos dados: 

\- Notas Fiscais \(SAFX07 e SAFX08\)

\- Valores informados manualmente 

\- Parametrização de CFOP e CFOP/NAT

  \(menu Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos da SAFX07/SAFX08, totalizando os valores por município do ponto de consumo \(campos 207/208 da SAFX07\)\.

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03 da SAFX07 <> 9\); 

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo 13 da SAFX07\) = “06”, “55” ou “66”;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\); 

\- Classificação fiscal \(campo 12 da SAFX07\) = 1 ou 3;

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à 

  Registro 1400 à Específico por UF” para o operação __TOIPME05__;

\- A UF do ponto de consumo deve ser = “__TO__” \(campo 207 da SAFX07\); 

\- O município do ponto de consumo deve estar preenchido \(campo 208 da SAFX07\); 

__*OBS*__*: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. *

Totalização das notas recuperadas:

A totalização dos valores será feita *por município* da nota \(campo 208 da SAFX07\)\.

Valor a ser totalizado:

   \- Notas com itens à Valor Contábil do Item;

   \- Notas sem itens à Valor Total da Nota;

__*OBS*__*: Sobre as “operações dedutíveis” que consta no texto da Portaria 265/2018, \(Anexo II\), o cliente CPFL afirmou na reunião de JUN/20, que no caso da Usina deles de TO não existem tais operações\. Por isso, a geração deste item não terá tratamento de deduções\.*

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo: “__TOIPME05__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização, mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME05__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

*\(lembrando que para este código não há tratamento de Deduções automático, conforme observação descrita acima\)*

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

\-No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

\-No campo “Deduções”:      será gravado zero;

\-No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-TO\-16__

__Código TOIPMS05\- Produção de Energia Elétrica \(Usinas\) \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

__MFS35133__: A partir desta demanda, a geração do __TOIPMS05__ passou a ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Origem dos dados: 

\- Notas Fiscais \(SAFX07 e SAFX08\)

\- Valores informados manualmente 

\- Parametrização de CFOP e CFOP/NAT

  \(menu Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

*Obs: Para este código, as operações de saída são recuperadas da SAFX07 / SAFX08, e não da SAFX42/SAFX43\. Isso porque de acordo com o cliente CPFL \(reunião de Jun/20\), a Usina de Tocantins não usa a SAFX42/SAFX43, devido a quantidade de operações muito pequena\.  *

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03 da SAFX07 = 9\); 

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo 13 da SAFX07\) = “06”, “55” ou “66”;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\); 

\- Classificação fiscal \(campo 12 da SAFX07\) = 1 ou 3;

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à 

  Registro 1400 à Específico por UF” para o operação __TOIPMS05__;

\- A UF do ponto de consumo deve ser = “__TO__” \(campo 207 da SAFX07\); 

\- O município do ponto de consumo deve estar preenchido \(campo 208 da SAFX07\); 

__*OBS*__*: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações\. *

Totalização das notas recuperadas:

A totalização dos valores será feita *por município* da nota \(campo 208 da SAFX07\)\.

Valor a ser totalizado:

   \- Notas com itens à Valor Contábil do Item;

   \- Notas sem itens à Valor Total da Nota;

* *

__*OBS*__*: Sobre as “operações dedutíveis” que consta no texto da Portaria 265/2018, \(Anexo II\), o cliente CPFL afirmou na reunião de JUN/20, que no caso da Usina deles de TO não existem tais operações\. Por isso, a geração deste item não terá tratamento de deduções\.*

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo: “__TOIPMS05__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização, mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS05__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

*\(lembrando que para este código não há tratamento de Deduções automático, conforme observação descrita acima\)*

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este Município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-TO\-17__

__Código TOIPME09\- Combustível \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME09__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPME09__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este Município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-TO\-18__

__Código TOIPMS09\- Combustível \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS09__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPMS09__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\. O registro 1400 não será gravado para este município

Resultado final = zero à O registro 1400 não será gravado para este município;

__RN1400\-TO\-19__

__Código TOIPME10\- Comércio \(entrada\) __

__\[MFS31044\]__: Alterou a geração do código TOIPME10 para apurar os valores automaticamente\. A partir de então, seus valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.

Origem: Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

               \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entradas de mercadorias para comercialização \(identificados pelo modelo\), totalizando o valor   contábil   das   entradas   e   aquisições   de   mercadorias, por município tocantinense, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada aquisição na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 01, 1B, 04, 55 ou 65;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPME10__”;
- Serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja de TO \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

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
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “TO”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPME10__”;

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

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPME10__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME10__” 

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

__RN1400\-TO\-20__

__Código TOIPMS10\- Comércio \(saída\) __

__\[MFS35318\]__: A partir dessa demanda a geração do código TOIPME10 para apurar os valores passa a ser feita automaticamente\. Os valores são gerados com base nos documentos fiscais, e considerando também valores inseridos manualmente\.

__\[MFS94466\] __Alteração das regras para preencher o código do munícipio de acordo com o CFOP

__Origem:__ Notas Fiscais \(SAFX07 e SAFX08\)

              Valores informados manualmente 

              Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saída de mercadorias para comercialização \(identificados pelo modelo\), totalizando o valor   contábil   das   saídas, por município tocantinense, excluindo\-se as operações dedutíveis\.

__Apuração do valor referente a cada aquisição na SAFX07/SAFX08:__

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 01, 1B, 04, 55 ou 65;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__TOIPMS10__”;
- Se o CFOP iniciar com “5” \(Operação Interna\)

                    Serão consideradas apenas as notas em que o município de destino seja de TO \(campos       

                    122\-UF\_DESTINO e 183\-COD\_MUNICIPIO\_DEST da SAFX07\)

              Senão \(Operações interestaduais e exterior\)

                    Serão consideradas apenas as notas em que o município de origem \(município onde 

                    ocorreu a saída da mercadoria\) seja de TO \(campos 117\-UF\_ORIG\_DEST e 182\-

                    COD\_MUNICIPIO\_ORIG da SAFX07\)

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

__Valor a ser totalizado:__

- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) ou valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\), no caso das notas sem itens;

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
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “TO”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “__TOIPMS10__”;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

 __Processamento das notas:__

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

__Valor a ser totalizado:__

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

             

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo: “__TOIPMS10__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS10__” 

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

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.                                                    

             

__RN1400\-TO\-21__

__Código TOIPME11\- Indústria \(entrada\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPME11__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPME11__” 

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

__RN1400\-TO\-22__

__Código TOIPMS11\- Indústria \(saída\) __

A princípio os valores deste código serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__TOIPMS11__*”* 

Poderão existir  vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__TOIPMS11__” 

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

