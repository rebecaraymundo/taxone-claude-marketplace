# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_MG

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_MG.docx
- **Modificado:** 2025-02-06
- **Tamanho:** 103 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- MG

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

[MFS60170](https://jira.thomsonreuters.com/browse/MFS-60170)

Rogério Ohashi

Alteração na geração do registro __1400__ – Geração Específica para UF = MG

Tratamento na geração do registro __1400,  “3\.5 \- __Prestação de Serviço de Transporte Rodoviário” –  que de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\.1, passa a ser informado __mensalmente__\. 

10/03/2021

[MFS60170](https://jira.thomsonreuters.com/browse/MFS-60170)

Rogério Ohashi

Alteração na geração do registro __1400__ – Geração Específica para UF = MG

Tratamento na geração do registro __1400, item “3\.5 \- __<a id="_Hlk68106826"></a>Prestação de Serviço de Transporte Rodoviário” –  que de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2, passa a ser informado __mensalmente__ e gerado diretamente pelo menu Geração > Meio Magnético\. \(__RN1400\-MG\-05a\)__

31/03/2021

MFS45370

Aline Melo

Alteração na geração do registro 1400, para o código Geracao\_de\_Energia\_Eletrica, para ser gerado de forma automática\.

16/07/2021

MFS68839

Rogerio Ohashi

Alteração do Registro 1400 – Específico por UF, para __MG__, Código 3\.1 \- “Produtos Agropecuários”, alteração na regra para considerar somente o Campo MOVTO\_E\_S =“2”\.

20/07/2021

MFS87167

Andréa Rocha

Alteração na geração para a operação “Transporte Tomado” para ter uma nova forma de recuperar o valor a ser gerado, sem utilizar o campo de valor do frete da SAFX07\.  

21/06/2022

MFS681121

Andréa Rocha

Alteração na geração para a operação “3\.5__ \- __Prestação de Serviço de Transporte Rodoviário”, para retirar a regra da subtração do 20% do valor total\. Conforme verificado pela área de informação, o valor calculado será o valor total das prestações de serviços\.

05/09/2024

MFS710621

Graciela Soares 

Inclusão do modelo 66 na regra da  __Geração de Energia Elétrica para Produção Própria__

03/02/2025

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- MG

__RN1400\-MG__

A geração do 1400 para a modalidade “MG” é feita de acordo com os dados solicitados na Resolução 4\.730, de 17/12/2014, SEF\-MG\.

Os tipos de operação solicitados são os seguintes, conforme os itens descritos na Resolução:

\- Aquisições de Produtos Agropecuários / Hortifrutigranjeiros \(item __3\.1__\);

\- Transporte Tomado \(item __3\.2__\);

\- Cooperativas \(item __3\.3__\);

\- Geração de Energia Elétrica para Produção Própria \(item __3\.4__\)

\- Prestação de Serviços de Transporte Rodoviário \(item __3\.5__\);

\- Outros \(item __3\.6__\);

<a id="_Hlk73452894"></a>Para os quatro primeiros tipos de operação, a entrega é no arquivo mensal da EFD\. 

__\[ALTERAÇÃO \- MFS60170\] Alteração de Regra \(3\.5\) para Geração Mensal à partir de 2021\.__

Para os dois últimos \(3\.5 e 3\.6\), a entrega é apenas no arquivo de Dezembro, pois os valores são referentes a todo o exercício\. Por isso, a apuração destes dois itens tem uma pré\-geração\.

Para o último \(3\.6\), a entrega é apenas no arquivo de Dezembro, pois os valores são referentes a todo o exercício\. Por isso, a apuração destes dois itens tem uma pré\-geração\.

O item “*Geração de Energia Elétrica para Produção Própria*” será gerado apenas a partir da manutenção do registro 1400 disponível no módulo da EFD\.

As regras estão organizadas da seguinte forma:

__RN1400\-MG\-01__ – geração para a operação “Produtos Agropecuários”;

__RN1400\-MG\-02__ – geração para a operação “Transporte tomado”;

	

__RN1400\-MG\-03__ – geração para a operação “Cooperativas”;

__RN1400\-MG\-04__ – geração para a operação “Geração de Energia Elétrica para Produção Própria” ;

__RN1400\-MG\-05__ – geração para a operação “Prestação de Serviços de Transporte Rodoviário”;

__RN1400\-MG\-06__ – geração para a operação “Outros”;

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__OBS2__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D590\.\.\.\)\. A VAF passou a ler diretamente a tabela EFD\_REG\_1400 para obter os registros 1400 gerados no Sped Fiscal\. Qualquer alteração na geração do 1400 deve\-se avaliar se haverá impacto na geração da VAF\-MG \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

__RN1400\-MG\-01__

__Produtos Agropecuários e Hortifrutigranjeiros__

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(do menu “Parâmetros à Registro 1400 à MG\)

\[__ALTERAÇÃO\-MFS68839__\] Tratamento da regra para considerar somente o campo MOVTO\_E\_S = ‘2’\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente as entradas com MOVTO\_E\_S = “1” ou “__2__”

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à MG” para a operação do tipo “*Aquisições de Produtos*

*  Agropecuários / Hortifrutigranjeiros”*

\- O município de origem \(campo 182 da SAFX07\) deve ser um município da UF do

   Estabelecimento

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Apuração dos valores a serem deduzidos:     \(MFS14605\)__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas	

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2, 5 e 8 \(IND\_SITUACAO\_ESP\) 

\- Somente as notas em que a “*UF Origem*” da nota = “MG”;

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__Produtos Agropecuários__”

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município *de origem da nota* \(SAFX07\), utilizando os seguintes valores:

Valor a ser totalizado = valor contábil do item;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                         “Produtos\_Agropecuarios” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “*Aquisições de Produtos Agropecuários / Hortifrutigranjeiros”* 

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

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-MG\-02__

__\[MFS87167\] __Inclusão de uma nova forma de recuperar o valor a ser gerado, dando a opção de não utilizar o valor do frete, já que as vezes o valor do frete não deve estar destacado na nota fiscal 

__Transporte Tomado__

Origem: \- Notas Fiscais \(SAFX07\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(do menu “Parâmetros à Registro 1400 à MG\)

Para apurar o total das operações deste item será feita a totalização das notas fiscais de saída gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente saídas \(MOVTO\_E\_S = “__9__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação da capa da nota \(SAFX07\) deve estar 

   parametrizado no menu “Parâmetros à  Registro 1400 à MG” para a operação do tipo 

   *“Transporte Tomado”*

\- O município de origem \(campo 182 da SAFX07\) deve ser um município da UF do

   Estabelecimento

Valor a ser totalizado:

Se o Valor do Frete \(campo 24 da SAFX07\) estiver preenchido 

      Utilizar o Valor do Frete \(campo 24 da SAFX07\)

Senão

       Utilizar o Valor Serviço de Transporte \- Valor Frete \(campo 76 da SAFX07\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

As notas recuperadas conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                              “Transporte\_Tomado” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

     “*Transporte Tomado”* 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-MG\-03__

__Cooperativas__

Origem: \- Notas Fiscais \(SAFX07 e SAFX08\)

              \- Valores informados manualmente 

              \- Parametrização de CFOP e CFOP/NAT

                \(do menu “Parâmetros à Registro 1400 à MG\)

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de saída gravadas no C100 que atendam aos seguintes critérios:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente saídas \(MOVTO\_E\_S = “__9__”\)

\- Data Fiscal  \-  no período da geração ou data extemporânea no 

                         período da  geração

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à MG” para a operação do tipo *“Cooperativas”*

\- O município de origem \(campo 182 da SAFX07\) deve ser um município da UF do

   Estabelecimento

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município__ \(campo 182 da SAFX07\), e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                    “Cooperativas” 

	

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “Cooperativas*”* 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-MG\-04__

__Geração de Energia Elétrica para Produção Própria__

Origem: \- Valores informados manualmente 

Para este tipo de operação o registro 1400 será gerado apenas com os valores informados manualmente pelo usuário \(menu “Geração à Manutenção à Registro 1400”\), e recuperados da seguinte forma: 

\- Estabelecimento – estabelecimento da geração 

\- Período – mesmo período da tela da geração \(data inicial e final\)

\- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = “Geração de Energia Elétrica para Produção Própria”

__\[MFS45370\]__ A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município de Minas Gerais, em atendimento ao cenário de empresas de Energia Elétrica, levantado pelo cliente CPFL\. 

A regra foi baseada no material montado pela equipe da CPFL “D06\_0046\_JULHO2020\_valores validados\_MG\_14092020\.xls” e também através de reuniões de alinhamento\.

__\[MFS710621\] __Inclusão do modelo de nota “66”

__PARTE 01 – CÁLCULO DO REGISTRO 1400 POR MUNICÍPIO__

Essa regra consiste em somar as __Bases__ de __ICMS Tributada__, __Isenta__ e __Outras__, de acordo determinados códigos de Situação Tributária B e subtrair o Valor do Desconto dos itens de dedução\. Além disso os itens de Dedução tem tratamento particular para cada tipo de base\. Veja o cálculo de cada parcela que compõe o valor da Operação para Energia Elétrica\.

__Origem:__

              \- Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

              \- Valores informados manualmente 

Tratam\-se das notas fiscais __de saída__ gravadas nos registros específicos C500, C600 ou C700 para o segmento de energia elétrica\.

__Critérios para Recuperação das Notas:__

Totalizar o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Data \(campo 03 da SAFX42\) no período da geração ou data extemporânea no período de

   Geração;

\- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);

\- Situação = somente as não canceladas;

\- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\);

\- Município de Terminal Faturado \(campo 76 da SAFX42\) deve ser um município da

  UF do Estabelecimento\.

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Totalização das Notas recuperadas :__

__>> Base Tributada de ICMS__:

Para calcular a Base Tributada de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06 ou 66”;
- Código Situação Tributária B \(campo 33 da SAFX43\)= __“00__”;
- Base Tributada ICMS \(campo 23 da SAFX43\) > 0,00;

Para esses itens, recuperar os campos:

- Base Tributada ICMS \(campo 23 da SAFX43\); 
- Valor do Desconto \(campo 18 da SAFX43\);
- Adição/Desconto \(campo 20 da SAFX43\);

__Base Tributada__

__de ICMS =__

Somatório da Base Tributada ICMS de todos os itens recuperados,

Subtrair o Valor do Desconto dos itens com campo 20\-Adição/Desconto = “D”;

Subtrair o Valor do Desconto dos itens com campo 20\-Adição/Desconto = “D”

__OBS\.: __O valor do Desconto é subtraído duas vezes, pois um é o próprio valor do desconto e o outro é a Base Tributada ICMS Negativada, que na prática é o mesmo valor do desconto\. Como o campo “20\-Adição/Desconto” não é obrigatório, caso esteja __nulo__ é considerado como item de Adição \(“__A__”\)\.

__>> Base Isenta de ICMS__:

Para calcular a Base Isenta de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06 ou 66”;
- Código Situação Tributária B \(campo 33 da SAFX43\)= “__40__”;
- Base Isenta ICMS \(campo 24 da SAFX43\) > 0,00;
- __Desconsiderar__ os itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);
- __MFS58137:__ Considerar todos os produtos ou apenas os Parametrizados com Isenção de ICMS, conforme regra a seguir:
- Caso a opção “__Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica__” esteja marcada na Tela de Dados Iniciais em: 

Tipo de Geração: Específico por UF, no item Dados para geração específica \(MG\): 

Considerar apenas itens da SAFX43 com Produtos \(campos 11 e 12\) pertencentes à Parametrização de Produtos com Isenção de ICMS \(menu: Parâmetros >> Registro 1400 >> <a id="_Hlk74739648"></a>Serviço de Energia Elétrica >> Produto com Isenção de ICMS\)

- Caso a opção “__Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica__” esteja desmarcada na Tela de Dados Iniciais, então:

Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Isenção de ICMS\.

Para esses itens, recuperar o campo:

- Base Isenta ICMS \(campo 24 da SAFX43\); 

__Base Isenta de ICMS = __

Somatório Base Isenta ICMS dos itens recuperados

__>> Base Outras de ICMS \(CST de Diferimento\):__

Para calcular a Base Outras de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06 ou 66”;
- Código Situação Tributária B \(campo 33 da SAFX43\)= “__51__”;
- Base Outras ICMS \(campo 25 da SAFX43\) > 0,00;
- __Desconsiderar__ os itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);

Para esses itens, recuperar o campo:

- Base Outras ICMS \(campo 25 da SAFX43\); 

__Base Outras de ICMS = __

Somatório Base Outras ICMS dos itens recuperados

__>> Desconto ST:__

Para calcular o Desconto ST, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06 ou 66”;
- itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);
- __MFS58137:__ Considerar todos os produtos ou apenas os Parametrizados com Desconto, conforme regra a seguir:
- Caso a opção “__Utilizar a parametrização de produtos com Desconto para Energia Elétrica__” esteja marcada na Tela de Dados Iniciais em:

Tipo de Geração: Específico por UF, no item Dados para geração específica \(MG\) 

Considerar apenas itens da SAFX43 com Produtos \(campos 11 e 12\) pertencentes à Parametrização de Produtos com Desconto \(menu: Parâmetros >> Registro 1400 >> Serviço de Energia Elétrica >> Produto com Desconto\)

- Caso a opção “__Utilizar a parametrização de produtos com Desconto para Energia Elétrica__” esteja desmarcada na Tela de Dados Iniciais, então:

Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Desconto\.

Para esses itens, recuperar o campo:

- Valor do Desconto \(campo 18 da SAFX43\); 

	

__Desconto ST = __

Somatório do Valor do Desconto dos itens recuperados

__Valor a ser totalizado:__

Base Tributada de ICMS __\(\+\)__

Base Isenta de ICMS__ \(\+\)__

Base Outras de ICMS__ \(–\)__

Desconto ST

__RESULTADO A = TOTAL__

__PARTE 02 – CÁLCULO DO CONVÊNIO 30__

Essa regra consiste em calcular a __dedução __\(campo VLR\_BASE\_ICMS\_1 da X42\), de notas fiscais canceladas por município, dentro do mês de apuração, cuja data de emissão seja < até 5 anos da data de apuração\.

__Origem:  __Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

__Critérios para Recuperação das Notas:__

Totalizar o Valor Base ICMS das notas da SAFX42 que atendam aos seguintes critérios:

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Data Fiscal \(campo 03 da SAFX42\) seja < até 5 anos da data da geração;

\- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);

\- Situação = somente as canceladas;

\- Data cancelada \(campo da SAFX42\) dentro do período de geração;

\- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\);

\- Município de Terminal Faturado \(campo 76 da SAFX42\) deve ser um município da UF do Estabelecimento\.

__       __

__Totalização das Notas recuperadas:__

  

__DEDUÇÃO = __

Somatório do Valor Base ICMS \(campo VLR\_BASE\_ICMS\_1 da SAFX42\)__ __dos notas recuperados

           

__Valor a ser totalizado:__

__RESULTADO B = DEDUÇÃO__

__PARTE 03 \- MANUTENÇÃO – DEDUÇÃO CLIENTE CATIVO__

Essa regra consiste em recuperar o __valor apurado__ __por município__ \(campo Valor Apurado\), da tela de manutenção Dedução Cliente Cativo, do item de menu Registro 1400 > Serviço de Energia Elétrica, de acordo com os seguintes critérios:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela de geração \(data inicial e data final\)

   \- Município – município da totalização 

__Valor a ser totalizado:__

   

__RESULTADO C__ __= VALOR APURADO POR MUNICÍPIO__

__PARTE 04 – VALOR LÍQUIDO DO REGISTRO 1400__

Essa regra consiste em calcular os valores obtidos dos itens, por município:

__RESULTADO A = Resultado obtido do cálculo do registro 1400 por município \(PARTE 01\): __Somatória das Bases de ICMS Tributada, Isenta e Outras, de acordo com determinados códigos de Situação Tributária B e subtração do Valor do Desconto dos itens de dedução\.

__RESULTADO B = Resultado obtido do cálculo do convênio 30 \(PARTE 02\): __Cálculo da __dedução __das notas fiscais canceladas por município\. 

__RESULTADO C__ __= Resultado obtido da tela de manutenção Dedução Cliente Cativo \(PARTE 03\): __Valor apurado por município informado na tela de manutenção\.

O valor é calculado da seguinte forma:

__RESULTADO A \(\-\)__

__RESULTADO B \(\-\)__

__RESULTADO C__

__RESULTADO D = TOTAL POR MUNICÍPIO__

__PARTE 05 \- INDÍCE DE RATEIO P/ MUNICÍPIO__

Essa regra consiste em calcular o percentual, referente ao índice de rateio por município:

O indíce é calculado da seguinte forma:

__RESULTADO D \( / \)__

__soma de todos os municípios da parte 04 \( \* \) 100__

__RESULTADO E = INDICE POR MUNICÍPIO__

__PARTE 06 – BASE DE RATEIO TOTAL x NOTA FISCAL MICROGERADOR__

Essa regra consiste em calcular a __diferença entre o valor líquido__ do registro 1400 para todos os municípios e o __valor total dos itens de saída__, de acordo com a parametrização feita na tela de Nota Fiscal Microgerador, do item de menu Registro 1400 > Serviço de Energia Elétrica > MG\.

As notas fiscais são emitidas mensalmente pela CPFL e são nomeadas como NF Microgerador\.

__Origem:  __Notas Fiscais \(SAFX07 e SAFX08\)

__Critérios para Recuperação das Notas__

Totalizar o valor do item \(campo 28\-VLR\_ITEM\) das notas da SAFX08 que atendam aos seguintes critérios: 

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- MOVTO\_E\_S – somente saídas \(MOVTO\_E\_S = “__9__”\)

\- Data Fiscal  \-  no período da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- CFOP informado no item \(campo 22\-COD\_CFO da SAFX08\) = CFOP informado no campo CFOP da tela de Nota Fiscal Microgerador;

\- Produto informado no item \(campo 14\-COD\_PRODUTO da SAFX08\) = Produto informado no campo Produto da tela Nota Fiscal Microgerador;

\- Sit\.Trib\. B infomado no item \(campo 31\-COD\_SITUACAO\_B da SAFX08\) = Código informado no campo Sit\. Tributária B da tela Nota Fiscal Microgerador\.

__Valor a ser totalizado: __

__VALOR TOTAL = SOMATÓRIO VALOR ITEM __

No passo seguinte, deve ser feito o seguinte cálculo:

__RESULTADO D \(\-\)__

__VALOR TOTAL__

__RESULTADO F =__ __BASE DE RATEIO TOTAL__

__TOTALIZAÇÃO DO REGISTRO__

Valor total adicionado do registro 1400 – MG:

__TOTAL POR MUNICÍPIO =__

__RESULTADO F \(\*\) ÍNDICE POR MUNICÍPIO/ 100__

__GERAÇÃO DO REGISTRO__

Os itens recuperados conforme os critérios acima serão totalizados __por município__, e para cada município será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                    “Geracao\_de\_Energia\_Eletrica” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização \(__RESULTADO FINAL__\) mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “Geracao\_de\_Energia\_Eletrica” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

__\(\+\)__

\[Campo “Outros Valores” informado manualmente\]

__\(\-\)__

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

<a id="_Hlk73452957"></a>__RN1400\-MG\-05__

<a id="_Hlk73453150"></a>__Prestação de Serviço de Transporte Rodoviário – \(Regra válida até 31/12/2020\)__

Origem: \- Tabela da manutenção do registro 1400 

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de MG\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\.

Este item será gerado no registro 1400 apenas quando o período da geração for Dezembro\. __\(Processo válido até 31/12/2020\)\.__

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\. 

Critérios para recuperação dos dados na tabela da manutenção do 1400:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\) 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

*          “Prestação de Serviço de Transporte Rodoviário” *

Para cada linha recuperada, ou seja, para cada município, será gerado um registro 1400, da seguinte forma:

	

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                         “Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor do campo “Valor Total” da tela de manutenção\.

__Crítica:__

Caso o valor a ser gravado for negativo ou zero, o procedimento  será o seguinte:

Resultado final negativo à será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à o registro 1400 não será gravado para este município;

<a id="_Hlk73453181"></a>__RN1400\-MG\-05a__

__Prestação de Serviço de Transporte Rodoviário__:

<a id="_Hlk73454118"></a>__\[MFS60170\] Alteração de Regra para Geração Mensal à partir de 2021\.__

<a id="_Hlk73454386"></a>Neste caso a apuração é feita a partir dos documentos de transporte rodoviário da SAFX07\.

À partir do período de 2021 o cálculo para este item deverá ser gerado no registro 1400 __mensalmente__, \(de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\)\.

Será totalizado o valor das saídas por município de origem, conforme as regras descritas a seguir\.

__Origem dos dados__ àTabelas dos Documentos Fiscais – Capa e Itens de Mercadoria  \(SAFX07 e SAFX08\)

__Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:__

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

  No caso de geração por I\.E\.U\. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,

  \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle

  das Obrigações Estaduais;

\- Classificação = 1 ou 4: 

           \- NF de modelo 07 usa classificação 1;

           \- CTRC’s usam classificação 4; 

           \- NF modelo 07 é nota fiscal de transporte rodoviário de carga\.

\- Data Fiscal \(ou data extemporânea\) – deve ser a data inicial e final de acordo com __mês/ ano__ preenchido na tela de geração\.

\- Modelo \(campo 13\) – somente modelos de transporte rodoviário ou multimodal \(07, 08, 8B, 26, 57, 67\) 

Observar que no caso do modelo do CTe \(57\), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte\. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos \(aéreo, rodoviário, etc\.\.\.\)\. Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação\.

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Situação \- somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve ser “MG”;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

\- Somente notas com  CFOP ou CFOP/Natureza parametrizado <a id="_Hlk68105584"></a>no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP

   ou CFOP/Natureza de Operação”, <a id="_Hlk68105738"></a>para a operação = “__Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario__” da UF = MG;

\- Notas com ou sem itens na SAFX08; 

\- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

\- Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

__Processamento das notas:__

__\[MFS681121\] __Exclusão da regra da subtração do 20% do valor total\.

Para cada linha recuperada, ou seja, para cada município, será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                         “Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à As notas serão agrupadas __*por município de origem*__, e __*para cada município*__ será apurado o total das saídas, conforme o “Valor a ser totalizado”\. O resultado final será calculado da seguinte forma:

  

     A =  Total das notas de saída

     B =  20% do valor de A

     C = A – B

  

Para cada município apurado, será gravado o resultado final, que corresponde ao valor “C” representado no quadro acima\.

__Crítica:__

Caso o valor a ser gravado for negativo ou zero, o procedimento  será o seguinte:

Resultado final negativo à será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à o registro 1400 não será gravado para este município;

__RN1400\-MG\-06__

__Outras Entradas a Detalhar por Município__

Origem: \- Tabela da manutenção do registro 1400 

Da mesma forma que o item anterior, este item será gerado no registro 1400 apenas quando o período da geração for Dezembro\.

O valor deste item deve ser calculado previamente, antes de gerar o Sped, na geração preliminar executada no menu “Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF” para UF de MG\. O resultado desta geração é gravado na tabela da manutenção do registro 1400\.

E assim como os demais itens, também poderão ser informados valores manualmente na tela de manutenção\. 

Critérios para recuperação dos dados na tabela da manutenção do 1400:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\) 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

*          “Outras Entradas a Detalhar por Município”*

Para cada linha recuperada, ou seja, para cada município, será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                         “Outras\_Entradas\_a\_Detalhar\_por\_Município” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor do campo “Valor Total” da tela de manutenção\.

__Crítica:__

Caso o valor a ser gravado for negativo ou zero, o procedimento  será o seguinte:

Resultado final negativo à será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à o registro 1400 não será gravado para este município;

