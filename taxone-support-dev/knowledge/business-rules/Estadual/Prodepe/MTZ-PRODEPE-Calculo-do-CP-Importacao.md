# MTZ-PRODEPE-Calculo-do-CP-Importacao

- **Fonte:** MTZ-PRODEPE-Calculo-do-CP-Importacao.docx
- **Modificado:** 2024-10-02
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Módulo PRODEPE – Cálculo do Crédito Presumido \- Importação

__Localização__: Menu Estadual, Módulo Prodepe 🡪 Obrigações 🡪Cálculo do Crédito Presumido

Neste item de menu é executado o cálculo do Prodepe referente às três modalidades de incentivo existentes no módulo: Indústria, Importação e Central de Distribuição\. Cada modalidade tem o seu cálculo específico, executado por procedures distintas, da seguinte forma:

Indústria

SAF\_CPRES\_INCENT1  

Importação

SAF\_CPRES\_INCENT2  __\(\*\*\*\)__

Central de Distribuição

SAF\_CPRES\_INCENT3  

__\(\*\*\*\)__ Este documento de regras é específico do cálculo do incentivo da __Importação__ \(SAF\_CPRES\_INCENT2\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS3828

Atualização legal do incentivo da importação

Atualização legal do incentivo da importação \(Lei 15\.675, de 14/12/2015, PE\)\.  

\(ver item 3\-Processamento\)

04/04/2016 \(criação do documento\)

MFS63900

Tratamento Notas Fiscais de Devolução de Vendas\.

Tratamento nos processos de Cálculo do Crédito Presumido e no Resumo \(P9\) “Detalhamento do Crédito Presumido”\. __MFS\-63900 – v01 e MFS\-63900 – v02\.__

04/05/2021

MFS638212

Andréa Rocha

Atualização legal do incentivo da importação \(Lei 18\.305 de 30/09/2023, PE\)\.  

\(ver item 3\-Processamento\)

14/05/2024

MFS691134

Andréa Rocha

Inclusão da nota fiscal de entrada com o Movimento Entrada/Saída igual a “4”, no tratamento das Notas Fiscais de Devolução de Vendas\.

02/10/2024

Sumário

[1\.	Parâmetros da Tela	2](#_Toc447617861)

[2\.	Origem e Recuperação dos Dados	3](#_Toc447617862)

[3\.	Processamento \(Etapa I \- Cálculo do Crédito Presumido\)	4](#_Toc447617863)

[4\.	Processamento \(Etapa II – Apuração dos Dados p/Relatórios e SEF II – PE\)	7](#_Toc447617864)

[5\.	Gravação dos Dados	7](#_Toc447617865)

# <a id="_Toc447617861"></a>Parâmetros da Tela 

# <a id="_Toc350763252"></a><a id="_Toc447617862"></a>Origem e Recuperação dos Dados

Entrada: \- Tabela dos Grupos de Incentivo \(ICT\_GRP\_INCENT\)

               \- Tabela das Regras de Incentivo \(ICT\_REGRA\_INCENT\)

               \- Tabela de Controle dos Incentivos \(ICT\_GUIA\_INCENT\)

               \- Tabela dos Itens de Documentos Fiscais \(DWT\_ITENS\_MERC\)

Saída: \- Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

           \- Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\)

Os dados da Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\) são utilizados no Livro de Apuração Incentivado \(P9\), no resumo “Detalhamento do Incentivo”, e no relatório “Demonstrativo do Cálculo do Crédito Presumido”\.

Os dados da Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\) são utilizados no lançamento automático dos incentivos\.

O cálculo dos incentivos é feito por Estabelecimento e Grupo de Incentivo\.

A geração irá executar os cálculos de cada um dos grupos de incentivo do tipo “Importação” existente para o Estabelecimento\. 

Os grupos da importação são aqueles que têm o campo “Tipo de Incentivo” \(ICT\_GRP\_INCENT\) = “2” \(Importação\-Diferimento/Crédito Presumido\)\. 

O cálculo é feito grupo a grupo, lendo as notas fiscais na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\), e recuperando os dados de cada nota na DWT\_ITENS\_MERC

__Critérios para a recuperação das notas na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\):__

\- COD\_EMPRESA         \-  código da empresa do login

\- COD\_ESTAB               \-  código do estabelecimento em questão

\- DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

\- IDENT\_ITENS\_MERC   <> zero 

\- IND\_E\_S                         = “S”

\- COD\_GRP\_INCENT       =  grupo de incentivo em questão

\- IND\_INCENT                  = “I”

Para obter os dados da nota, recuperar a linha correspondente na DWT\_ITENS\_MERC pelos idents \(IDENT\_DOCTO\_FISCAL e  IDENT\_ITENS\_MERC\);

\[__MFS\-63900 – v01__\] Tratamento Notas Fiscais de Devoluções de Vendas \(Estorno de Crédito\)

# Origem e Recuperação dos Dados – Devoluções de Vendas

__\[MFS691134\] __Inclusão do tipo de movimento igual a 4 \(Documento de Entrada emitida pelo Estabelecimento, outros motivos legais\)

As operações de Devoluções de Vendas serão utilizadas no cálculo do Crédito Presumido e consequentemente no Livro de Apuração Incentivado \(P9\), no resumo “Detalhamento do Incentivo”, o objetivo é ajustar o processo de cálculo do Incentivo de Importação que não considerava o estorno do crédito referente as Notas Fiscais de Devoluções de Vendas\. 

Trata entradas “devoluções de vendas”: As operações de Devoluções de Vendas serão identificadas conforme critérios de recuperação a partir da leitura das tabelas de ICT\_GUIA\_INCENT e Documentário Fiscal \(DWT\_DOCTO\_FISCAL e DWT\_ITENS\_MERC\), conforme abaixo:

\- COD\_EMPRESA         \-  código da empresa do login

\- COD\_ESTAB               \-  código do estabelecimento em questão

\- DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

\- IDENT\_ITENS\_MERC   <> zero 

\- IND\_E\_S                         = “E”

\- COD\_GRP\_INCENT       = grupo de incentivo em questão

\- IND\_INCENT                  = “I”

\- MOVTO\_E\_S                  = ‘1’  ou ‘4’ \(DWT\_ITENS\_MERC\)

\- NORM\_DEV                   = ‘2’  \(DWT\_ITENS\_MERC\)

\- COD\_SITUACAO\_A    \- deve ser igual à 1, 2, 6 e 7 \(DWT\_ITENS\_MERC\)

Para tratar o cenário de devolução de vendas no Demonstrativo do Cálculo do Crédito Presumido, deverá ser incluído as linhas “Total Saídas Incentivadas” e “Estorno do Crédito – Devoluções de Vendas” no Demonstrativo do Cálculo do Crédito Presumido, para isso será necessário incluir dois campos na tabela ICT\_AP\_DEM\_INCE\. 

__VLR\_TOTAL\_SAI : __Nesse campo deverá ser gravado o cálculo efetuado para cada faixa 1, 2, 3, 4 e 5 dos Produtos Incentivados referentes as Notas Fiscais de Saídas \(Realizado no Processamento do Item 3\), referente a linha “Total Saídas Incentivadas”\.

Formato do Campo: NUMBER\(17,2\)\.

__VLR\_TOT\_DEVOL__: Nesse campo deverá ser gravado o cálculo efetuado para cada faixa 1, 2, 3, 4 e 5 dos Produtos Incentivados referentes as Notas Fiscais de Devoluções de Vendas \(Realizado no Processamento do Item 3\), referente a linha “Estorno do Crédito – Devoluções de Vendas”\.

Formato do Campo: NUMBER\(17,2\)\.

Exemplo: Cálculo Campo para os Campos: VLR\_TOTAL\_SAI e VLR\_TOT\_DEVOL:

COD\_DET\_PRODEPE

VLR\_DET\_PRODEPE

VLR\_TOTAL\_SAI  \(Campo novo\)

VLR\_TOT\_DEVOL \(Campo novo\)

Faixa 5

06

Resultado \(VLR\_TOTAL\_SAI  – VLR\_TOT\_DEVOL\)

VLR\_ICMS

VLR\_ICMS

Faixa 1

09

Resultado \(VLR\_TOTAL\_SAI  – VLR\_TOT\_DEVOL\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Faixa 2

12

Resultado \(VLR\_TOTAL\_SAI  – VLR\_TOT\_DEVOL\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Faixa 3

15

Resultado \(VLR\_TOTAL\_SAI  – VLR\_TOT\_DEVOL\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Faixa 4

18

Resultado \(VLR\_TOTAL\_SAI  – VLR\_TOT\_DEVOL\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

Resultado \(VLR\_CUSTO\_UNIT \* QUANTIDADE\)

__Campos utilizados para o cálculo:__

\- Preço de Custo Unitário = campo “136 \- Preço de Custo Unitário” da SAFX08;  

\- Quantidade = campo “24 \- Quantidade” da SAFX08;

\- Valor do ICMS = campo “43\-Valor ICMS” da SAFX08;

# IMPORTANTE\* Os campos deverão ser preenchidos em tempo de execução do Item 3 \- Processamento \(Etapa I \- Cálculo do Crédito Presumido\) e se houver a operação para faixa de cálculo\.

# <a id="_Toc447617863"></a>Processamento \(Etapa I \- Cálculo do Crédito Presumido\)

A partir dos itens das notas fiscais recuperadas para o período, conforme descrito no item “2\-Origem dos Dados”, e subitem “2\.1\-Origem dos Dados\-Devoluções de Vendas”,  o cálculo de crédito presumido será feito para cada uma das quatro faixas de saídas internas e devoluções de vendas internas, e uma quinta faixa, que é referente às saídas interestaduais e devoluções de vendas interestaduais, da seguinte forma:

__                                                                                           Cálculo do CP da Importação__:

Faixa 1

Saídas Internas e Devoluções de Vendas com alíquota de ICMS até __7 %__

Totalizar Saídas Internas \(preço de custo unitário \* quantidade\) – Devoluções de Vendas \(preço de custo unitário \* quantidade\) de todas as notas da faixa, e aplicar sob o resultado obtido o percentual de 3,5 % 

__Gravar Resultado do Cálculo \(preço de custo unitário \* quantidade\):  __

Saídas Internas: Gravar resultado no campo VLR\_TOTAL\_SAI , com o campo COD\_DET\_PRODEPE igual a 09 \(Se houver\)\.

Devoluções de Vendas: Gravar resultado no campo VLR\_TOT\_DEVOL, com o campo COD\_DET\_PRODEPE igual a 09 \(Se houver\)\.

Faixa 2

Saídas Internas e Devoluções de Vendas com alíquota de ICMS de __7,01%__ a __12%__

Totalizar Saídas Internas \(preço de custo unitário \* quantidade\) – Devoluções de Vendas \(preço de custo unitário \* quantidade\) de todas as notas da faixa, e aplicar sob o resultado obtido o percentual de 6 %\.

__Gravar Resultado do Cálculo \(preço de custo unitário \* quantidade\):  __

Saídas Internas: Gravar resultado no campo VLR\_TOTAL\_SAI , com o campo COD\_DET\_PRODEPE igual a 12 \(Se houver\)\.

Devoluções de Vendas: Gravar resultado no campo VLR\_TOT\_DEVOL, com o campo COD\_DET\_PRODEPE igual a 12 \(Se houver\)\.

Faixa 3

__MFS3828__: As alíquotas enquadradas na Faixa 3 dependem do período da apuração em questão, conforme o período exibido na tela da geração

__MFS638212__: As alíquotas enquadradas na Faixa 3 dependem do período da apuração em questão, conforme o período exibido na tela da geração

\- Para períodos até 31/12/2015:

      Saídas Internas e Devoluções de Vendas com alíquota de ICMS de __12,01%__ a __17%__ 

\- Para períodos de Jan/2016 a Dez/2019:

      Saídas Internas e Devoluções de Vendas com alíquota de ICMS de __12,01%__ a __18%__ 

\- Para períodos de Jan/2020 a Dez/2023:

      Saídas Internas e Devoluções de Vendas com alíquota de ICMS de __12,01%__ a __17%__ 

\- Para períodos a partir de Jan/2024:

      Saídas Internas e Devoluções de Vendas com alíquota de ICMS de __12,01%__ a __20,5%__ 

Totalizar Saídas Internas \(preço de custo unitário \* quantidade\) – Devoluções de Vendas \(preço de custo unitário \* quantidade\) de todas as notas da faixa, e aplicar sob o resultado obtido o percentual de 8 %

__Gravar Resultado do Cálculo \(preço de custo unitário \* quantidade\):  __

Saídas Internas: Gravar resultado no campo VLR\_TOTAL\_SAI , com o campo COD\_DET\_PRODEPE igual a 15 \(Se houver\)\.

Devoluções de Vendas: Gravar resultado no campo VLR\_TOT\_DEVOL, com o campo COD\_DET\_PRODEPE igual a 15 \(Se houver\)\.

Faixa 4

__MFS3828__: As alíquotas enquadradas na Faixa 4 dependem do período da apuração em questão, conforme o período exibido na tela da geração:

__MFS638212__: As alíquotas enquadradas na Faixa 3 dependem do período da apuração em questão, conforme o período exibido na tela da geração

\- Para períodos até 31/12/2015:

     Saídas Internas e Devoluções de Vendas com alíquota de ICMS superior a __17%__

\- Para períodos de Jan/2016 a Dez/2019:

     Saídas Internas e Devoluções de Vendas com alíquota de ICMS superior a __18%__

\- Para períodos de Jan/2020 a Dez/2023:

     Saídas Internas e Devoluções de Vendas com alíquota de ICMS superior a __17%__

\- Para períodos a partir de Jan/2024:

     Saídas Internas e Devoluções de Vendas com alíquota de ICMS superior a __20,5%__

Totalizar Saídas Internas \(preço de custo unitário \* quantidade\) – Devoluções de Vendas \(preço de custo unitário \* quantidade\) de todas as notas da faixa, e aplicar sob o resultado obtido o percentual de 10%\.

__Gravar Resultado do Cálculo \(preço de custo unitário \* quantidade\):  __

Saídas Internas: Gravar resultado no campo VLR\_TOTAL\_SAI , com o campo COD\_DET\_PRODEPE igual a 18 \(Se houver\)\.

Devoluções de Vendas: Gravar resultado no campo VLR\_TOT\_DEVOL, com o campo COD\_DET\_PRODEPE igual a 18 \(Se houver\)\.

Faixa 5

Saídas Interestaduais e Devoluções de Vendas

Totalizar o Saídas Interestadual \(Valor do ICMS\) – Devolução de Venda Interestadual \(valor de ICMS\) das notas, e aplicar sob o resultado obtido o percentual parametrizado p/as saídas interestaduais\.

__Gravar Resultado da Soma \(Valor de ICMS\):  __

Saídas Internas: Gravar resultado no campo VLR\_TOTAL\_SAI , com o campo COD\_DET\_PRODEPE igual a 06 \(Se houver\)\.

Devoluções de Vendas: Gravar resultado no campo VLR\_TOT\_DEVOL, com o campo COD\_DET\_PRODEPE igual a 06 \(Se houver\)\.

 

__Valor Total do Crédito Presumido__: CP Faixa 1 \+ CP Faixa 2 \+ CP Faixa 3 \+ CP Faixa 4 \+ CP Faixa 5

__Considerações sobre o cálculo:__

Saídas Internas – primeiro dígito do CFOP  = 5;

Saídas Interestaduais – primeiro dígito do CFOP  > 5;

Devoluções de Vendas Internas – Verificar o primeiro dígito do CFOP  = 1;

Devoluções de Vendas Interestaduais \- Verificar o primeiro dígito do CFOP  = 2;

__Saídas Internas e Devoluções de Vendas Internas:__

Os percentuais utilizados para as saídas internas são tratados de forma “fixa”, conforme descrito no quadro acima, e também demonstrado na tela da parametrização das regras específicas do incentivo da Importação \(menu *“Parâmetros 🡪 Incentivo – Importação 🡪 Regras de Incentivo”\)\.*

Para as faixas de saídas internas __menos __o valor das Devoluções de Venda, o valor do crédito presumido será: __\[\(\(total do preço de custo das NFs \* total Qtd das NFs\) – \(NFs Devoluções\) \* percentual da faixa\]__

__Obs: NFs Devoluções \(Internas\) = VLR\_CUSTO\_UNIT \* QUANTIDADE__

__Saídas Interestaduais e Devoluções de Vendas Interestaduais:__

O percentual utilizado para as saídas interestaduais é parametrizado pelo usuário no campo “*Percentual Incentivo das Saídas Interestaduais*” da parametrização das regras do grupo de incentivo em questão \(item *“Parâmetros 🡪 Incentivo – Importação 🡪 Regras de Incentivo”*, tabela ICT\_REGRA\_INCENT\)\. Para recuperar os dados da parametrização, utilizar os seguintes critérios:

   \- COD\_EMPRESA         \-  código da empresa do login

   \- COD\_ESTAB               \-  código do estabelecimento em questão

   \- COD\_GRP\_INCENT   \-  código do grupo de incentivo 

   \- VALIDADE\_INICIAL \-  maior data existente que seja <= data inicial do período da apuração exibido na tela da geração

   \- VALIDADE\_FINAL    \-  nula ou  >=  data final do período da apuração exibido na tela da geração

Para a faixa das saídas interestaduais __menos__ o valor das devoluções de vendas interestaduais, o valor do crédito presumido será: __\[\(\(total do valor do ICMS das NFs\) – \(NFs Devoluções\) \*  percentual da faixa \]__

__Obs: Valor de devoluções \(Interestadual\) = Valor de ICMS\.__

 

__Valores do item utilizados no cálculo do crédito presumido:__

\- Quantidade = campo “24\-Quantidade” da SAFX08;

\- Preço de Custo Unitário = campo “136\-Preço de Custo Unitário” da SAFX08;      

\- Alíquota do ICMS da nota = campo “42\-Alíquota do ICMS” da SAFX08; 

\- Valor do ICMS = campo “43\-Valor ICMS” da SAFX08;

__Valores a serem armazenados:__

Alguns valores processados durante o cálculo serão armazenados em tabelas auxiliares, da seguinte forma:

Faixas 1, 2, 3 e 4 🡪 para cada faixa das saídas internas serão armazenados os seguintes valores: 

 

         \- Total do valor contábil dos itens processados na faixa \(campo “64\-Valor Contábil do Item”\);

         \- Total do preço de custo \* quantidade dos itens processados na faixa \(Saídas\);

         \- Total do preço de custo \* quantidade dos itens processados na faixa \(Devoluções de Vendas\);

         \- Valor do crédito presumido calculado \(que será o resultado do cálculo Saídas \(\-\) Devoluções de Vendas \(se houver\)  \* percentual de incentivo\);

 Faixa 5 🡪 para a faixa das saídas interestaduais serão armazenados os seguintes valores:

         \- Percentual de incentivo das saídas interestaduais;

         \- Percentual de incentivo das Devoluções de Vendas interestaduais;

         \- Total do valor contábil dos itens processados na faixa;

         \- Total do valor do ICMS dos itens processados na faixa;

         \- Valor do crédito presumido calculado \(que será o resultado do valor saídas interestaduais \(\-\) o valor das Devoluções de Vendas interestaduais \* percentual de incentivo\);

OBS: Ver procedimentos sobre a gravação dos dados no item \(5\)\. 

# <a id="_Toc447617864"></a>Processamento \(Etapa II – Apuração dos Dados p/Relatórios e SEF II – PE\)

Além do cálculo do crédito presumido, a geração também apura algumas informações necessárias para posterior emissão de relatórios e geração do SEFII–PE\.

Estas informações serão armazenadas na Tabela do Demonstrativo dos Incentivos \(__ICT\_AP\_DEM\_INCE__\), com os códigos 01, 02, 03, 20 e 21 *\(ver procedimentos sobre a gravação dos dados no item 5\)*\.

Processamento dos códigos “01”  e  “02”:

Para estes códigos será totalizado o valor contábil \(VLR\_CONTAB\_ITEM\) e o valor do ICMS Não Escriturado \(VLR\_ICMS\_NDESTAC\) de todas as notas fiscais de *entrada* de importação, que tenham direito ao incentivo \(diferimento do ICMS\)\.

Critérios para a recuperação das notas na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\):

\- COD\_EMPRESA         \-  código da empresa do login

\- COD\_ESTAB               \-  código do estabelecimento em questão

\- DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

\- IDENT\_ITENS\_MERC   <> zero 

\- IND\_E\_S                         = __“E”__

\- COD\_GRP\_INCENT       = grupo de incentivo em questão

\- IND\_INCENT                  =__ “I”__

Processamento do código “03”:

Para este código será totalizado o valor contábil \(VLR\_CONTAB\_ITEM\) de todas as notas de *saídas não incentivadas*\. Serão as notas da ICT\_GUIA\_INCENT com indicador de incentivo <> __“I”__:

Critérios para a recuperação das notas na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\):

\- COD\_EMPRESA         \-  código da empresa do login

\- COD\_ESTAB               \-  código do estabelecimento em questão

\- DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

\- IDENT\_ITENS\_MERC   <> zero 

\- IND\_E\_S                          = __“S”__

\- COD\_GRP\_INCENT       = grupo de incentivo em questão

\- IND\_INCENT                  __<> “I”__

Processamento do código “20”:

O valor deste código representa o saldo da apuração do livro incentivado do grupo\. O valor será apurado em três etapas, conforme descrito a seguir nos passos 1, 2 e 3:

Passo 1 🡪 Apuração do valor total dos __débitos__:

Totalização do valor do ICMS \(VLR\_TRIBUTO\_ICMS\) de todas as notas de *saída* da ICT\_GUIA\_INCENT, incentivadas __e__ não incentivadas:

Critérios para a recuperação das notas na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\):

 COD\_EMPRESA         \-  código da empresa do login

 COD\_ESTAB               \-  código do estabelecimento em questão

 DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

 IDENT\_ITENS\_MERC   <> zero 

 IND\_E\_S                          = __“S”__

 COD\_GRP\_INCENT        = grupo de incentivo em questão

Ao total dos débitos apurado, será somado o valor dos lançamentos complementares à __débito__ que possam existir para a apuração do período:

Tabela dos lançamentos complementares: ICT\_AP\_DISC\_INCE

Será totalizada a coluna VAL\_ITEM\_DISCRIM  de acordo com os seguintes critérios:

COD\_EMPRESA       = código da empresa do login

COD\_ESTAB             = código do estabelecimento em questão

DAT\_APURACAO     = data final do período da apuração 

COD\_TIPO\_LIVRO    = ‘142’

SERIE\_LIVRO           = Série do livro do grupo de incentivo \(\*\)

SUB\_SERIE\_LIVRO = Subsérie do livro do grupo de incentivo \(\*\)

DAT\_APURACAO     = data final do período da apuração 

COD\_OPER\_APUR   =  ‘002’ ou ‘003’

\(\*\) Para identificar a série/subsérie do livro, recuperar o registro da parametrização das regras de incentivo do grupo em questão \(ICT\_REGRA\_INCENT\), conforme

     já explicado anteriormente no item \(3\)\.

Passo 2 🡪 apurar o valor total dos __créditos__:

Totalização do valor do ICMS \(VLR\_TRIBUTO\_ICMS\) de todas as notas de *entrada* da ICT\_GUIA\_INCENT, incentivadas e não incentivadas:

Critérios para a recuperação das notas na tabela de controle dos incentivos \(ICT\_GUIA\_INCENT\):

COD\_EMPRESA       = código da empresa do login

COD\_ESTAB             = código do estabelecimento em questão

DATA\_FISCAL             \- deve ser uma data enquadrada no período da apuração exibido na tela da geração

IDENT\_ITENS\_MERC   <> zero 

IND\_E\_S                        = __“E”__

COD\_GRP\_INCENT      = grupo de incentivo em questão

Ao total dos créditos apurado, será somado o valor dos lançamentos complementares à __crédito__ que possam existir para a apuração do período:

Tabela dos lançamentos complementares: ICT\_AP\_DISC\_INCE

Será totalizada a coluna VAL\_ITEM\_DISCRIM  de acordo com os seguintes critérios:

COD\_EMPRESA       = código da empresa do login

COD\_ESTAB             = código do estabelecimento em questão

DAT\_APURACAO     = data final do período da apuração 

COD\_TIPO\_LIVRO   = ‘142’

SERIE\_LIVRO           = Série do livro do grupo de incentivo \(\*\)

SUB\_SERIE\_LIVRO = Subsérie do livro do grupo de incentivo \(\*\)

COD\_OPER\_APUR   =  ‘006’ e ‘007’ 

\(\*\) Para identificar a série/subsérie do livro, recuperar o registro da parametrização das regras de incentivo do grupo em questão \(ICT\_REGRA\_INCENT\), conforme

     já explicado anteriormente no item \(3\)\.

 Além do valor dos lançamentos à débito, será somado também o valor do saldo credor resultante do período anterior\. Para isso, será verificado se no período anterior existe saldo credor a transportar para o período atual\. A pesquisa é feita na tabela ICT\_AP\_CALC\_INCE, para verificar a existência da linha correspondente ao COD\_OPER\_APUR = 014, conforme exemplo a seguir\. Caso exista, será utilizado o valor da coluna VAL\_APURACAO:

Tabela a ser pesquisada:  ICT\_AP\_CALC\_INCE

COD\_EMPRESA       = código da empresa do login

COD\_ESTAB             = código do estabelecimento em questão

DAT\_APURACAO    = maior data de apuração existente que seja menor que a data de apuração atual

COD\_TIPO\_LIVRO   = ‘142’

SERIE\_LIVRO           = Série do livro do grupo de incentivo \(\*\)

SUB\_SERIE\_LIVRO = Subsérie do livro do grupo de incentivo \(\*\)

COD\_OPER\_APUR   =  ‘014’  

\(\*\) Para identificar a série/subsérie do livro, recuperar o registro da parametrização das regras de incentivo do grupo em questão \(ICT\_REGRA\_INCENT\), conforme

     já explicado anteriormente no item \(3\)\.

Passo 3 🡪 Apuração do resultado final para o campo 20 do demonstrativo:

Valor do campo 20  = \(total débito apurado no passo 1\) – \(total crédito apurado no passo 2\)

Se o valor resultante for credor \(valor negativo\), será considerado resultado = zero\.

Processamento do código “21”:

O valor deste código representa o saldo a recolher após dedução dos incentivos, do livro incentivado do grupo\.

O cálculo é feito da seguinte forma:

Se campo 20 = zero

     Campo 21 = zero

Senão 

    Campo 21 =  Campo 20 – \(campo 07 \+ campo 10 \+ campo 13 \+ campo 16 \+ campo 19\), ou seja,

                         Campo 20 – \(total do crédito presumido calculado para todas as 5 faixas\)

     Se o valor resultante for credor \(valor negativo\), considerar resultado = zero;

 

 

# <a id="_Toc447617865"></a>Gravação dos Dados

Os resultados obtidos nas duas etapas do processamento, conforme descrito nos itens \(3\) e \(4\), serão armazenados em duas tabelas:

     \- Tabela dos Valores dos Incentivos Calculados \(__ICT\_VLR\_INCENT__\)

     \- Tabela do Demonstrativo dos Incentivos \(__ICT\_AP\_DEM\_INCE__\)

Os dados da Tabela dos Valores dos Incentivos Calculados \(__ICT\_VLR\_INCENT__\) são utilizados no lançamento automático dos incentivos\.

Os dados da Tabela do Demonstrativo dos Incentivos \(__ICT\_AP\_DEM\_INCE__\) são utilizados no Livro de Apuração Incentivado \(P9\), no resumo “Detalhamento do  Incentivo”, no relatório “Demonstrativo do Cálculo do Crédito Presumido”, e também na geração do SEF II – PE\.

__Gravação dos Dados na Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\):__

O crédito presumido calculado para cada grupo de incentivo, conforme descrito no item \(3\), será gravado na tabela da seguinte forma:

COD\_EMPRESA

Código da empresa do login

COD\_ESTAB

Código do estabelecimento em questão

DAT\_APURACAO

Data final do período da apuração

COD\_GRP\_INCENT

Grupo de incentivo 

PERCENTUAL\_INCENT

Zero  \(esta coluna é utilizada somente p/os incentivos tipo “Indústria”\)

TIPO\_INCENT

“I”

VLR\_BASE\_CPRES

\(\*\*\*\)

VLR\_CPRES

Valor total do crédito presumido calculado para o grupo de incentivo \(total de todas as 5 faixas\)

VLR\_FAT\_BRUTO

\(\*\*\*\)

NUM\_PROCESSO

Número do processo

VLR\_CRED\_ICMS

\(\*\*\*\)

VLR\_DEB\_ICMS

\(\*\*\*\)

VLR\_TOTAL\_SAI

\(\*\*\*\)

PERC\_TOTAL\_SAI

\(\*\*\*\)

VLR\_CRED\_ICMS\_LANC

\(\*\*\*\)

VLR\_DEB\_ICMS\_LANC

\(\*\*\*\)

__\(\*\*\*\)__ Estes campos não são preenchidos, pois não são utilizados no incentivo do tipo Importação\. 

__Gravação dos Dados na Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\):__

Nesta tabela serão gravadas ao todo 21 linhas, que é exatamente a quantidade de linhas existente no layout do relatório “*Demonstrativo dos Incentivos*” utilizado para o incentivo do tipo Importação\.

Cada linha contém um código e um valor\. O código identifica a linha do demonstrativo\. 

Os 21 valores a serem gravados são informações diversas, apuradas durante as duas etapas do processamento, conforme descrito nos itens \(3\) e \(4\)\.

Campos da tabela:

 

COD\_EMPRESA

Código da empresa do login

COD\_ESTAB

Código do estabelecimento em questão

COD\_TIPO\_LIVRO

Código do livro de apuração incentivado do Prodepe \(= “142”\)

SERIE\_LIVRO

Série do livro incentivado \(conforme parametrizado na regra do grupo\)

SUB\_SERIE\_LIVRO

Subsérie do livro incentivado \(conforme parametrizado na regra do grupo\)

DAT\_APURACAO

Data final do período da apuração

COD\_DET\_PRODEPE

Código da linha do demonstrativo, conforme tabela abaixo      __\(\*\*\*\)__

PERCENTUAL\_INCENT

Este campo não será preenchido, pois não é utilizado no incentivo do tipo Importação

VLR\_DET\_PRODEPE

Valor da linha do demonstrativo, conforme tabela abaixo         __\(\*\*\*\)__

__\(\*\*\*\)__ O quadro abaixo descreve o conteúdo do código e do valor a ser gravado em cada uma das 21 linhas do demonstrativo \(colunas COD\_DET\_PRODEPE e VLR\_DET\_PRODEPE\):

Os valores referentes aos códigos 04 ao 19, são valores tratados durante o cálculo do crédito presumido das saídas internas \(\-\) as Devoluções de Vendas Internas \(faixa 1, 2, 3 e 4\), e das saídas interestaduais \(\-\) as Devoluções de Vendas Interestaduais \(faixa 5\), definidos no item __3\-Processamento \(Etapa I\)__\.

Os outros valores são informações apuradas conforme definição do item __4\-Processamento \(Etapa II\)__\.

   

__COD\_DET\_PRODEPE__

__                                              VLR\_DET\_PRODEPE__

01

Total do valor contábil das notas de importação incentivadas           *\(conforme definido no item 4\)*

02

Total do ICMS diferido das notas processadas para o campo 01     *\(conforme definido no item 4\)*

03

Total do valor contábil das saídas NÃO incentivadas                       *\(conforme definido no item 4\)*

04

Percentual de incentivo das saídas interestaduais __\(faixa 5\)__

05

Total do valor contábil dos itens processados na __faixa 5__

06

Total do ICMS dos itens processados \- \(Devoluções de Vendas\) na __faixa 5 __

07

Valor do crédito presumido calculado p/a __faixa 5__ \(= campo 06 \* percentual do campo 04\)

08

Total do valor contábil dos itens processados na __faixa 1 __

09

Total do preço de custo \* quantidade dos itens processados \- \(Devoluções de Vendas\) na __faixa 1 __

10

Valor do crédito presumido calculado p/a __faixa 1__ \(= campo 09 \* 3,5 %\)

11

Total do valor contábil dos itens processados na __faixa 2 __

12

Total do preço de custo \* quantidade dos itens processados \- \(Devoluções de Vendas\) na __faixa 2__

13

Valor do crédito presumido calculado p/a __faixa 2__ \(= campo 12  \*  6 %\)

14

Total do valor contábil dos itens processados na __faixa 3 __

15

Total do preço de custo \* quantidade dos itens processados \- \(Devoluções de Vendas\) na __faixa 3__

16

Valor do crédito presumido calculado p/a __faixa 3__ \(= campo 15 \* 8 %\)

17

Total do valor contábil dos itens processados na __faixa 4 __

18

Total do preço de custo \* quantidade dos itens processados \- \(Devoluções de Vendas\) na __faixa 4__

19

Valor do crédito presumido calculado p/a __faixa 4__ \(= campo 18 \* 10 %\)

20

Saldo da apuração \(conforme descrito no item \(4\)\)

21

Saldo a Recolher após dedução dos incentivos                             *\(conforme definido no item 4\)*

\[__MFS\-63900 – v02__\] Tratamento Notas Fiscais de Devoluções de Vendas – Alteração da Descrição das Linhas 06, 09, 12, 15 e 18\.

Alterar a descrição do Item “Detalhamento do Cálculo dos Incentivos Relativos ao Prodepe”\.

   

__COD\_DET\_PRODEPE__

__                                              VLR\_DET\_PRODEPE__

04

Percentual de incentivo das saídas para fora do estado

05

Saídas Incentivadas de Produtos Incentivados para fora do estado

06

ICMS Debitado nas saídas incentivadas de produtos incentivados \(–\) Devoluções de Vendas para outro estado

07

Crédito Presumido PRODEPE nas Saídas para fora do estado \(04 \* 06\)

08

Saídas Incentivadas de Produtos Incentivados \- Faixa 01 – até 7%

09

Importações \- Base para Crédito Presumido PRODEPE \(–\) Devoluções de Vendas \- Faixa 01 – até 7%

10

Crédito Presumido PRODEPE nas Saídas Internas – Faixa 01 \- até 7% \(3,5% \* 09\)

11

Saídas Incentivadas de Produtos Incentivados \- Faixa 02 – até 7,01% a 12%

12

Importações \- Base para Crédito Presumido PRODEPE \(–\) Devoluções de Vendas \- Faixa 02 – até 7,01% a 12%

13

Crédito Presumido PRODEPE nas Saídas Internas – Faixa 02 – até 7,01% a 12% \(6% \* 12\)

14

Saídas Incentivadas de Produtos Incentivados \- Faixa 03 – até 12% a 17%

15

Importações \- Base para Crédito Presumido PRODEPE \(–\) Devoluções de Vendas \- Faixa 03 – até 12,01% a 17%

16

Crédito Presumido PRODEPE nas Saídas Internas – Faixa 03 – de 12% a 17% \(8% \* 15\)

17

Saídas Incentivadas de Produtos Incentivados \- Faixa 04 – acima de 17%

18

Importações \- Base para Crédito Presumido PRODEPE \(–\) Devoluções de Vendas \- Faixa 04 – acima de 17%

19

Crédito Presumido PRODEPE nas Saídas Internas – Faixa 04 – acima de 17% \(10% \* 18\)

= = = = = =

