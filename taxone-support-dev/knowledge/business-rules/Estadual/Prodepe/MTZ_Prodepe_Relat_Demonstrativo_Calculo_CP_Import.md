# MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Import

- **Fonte:** MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Import.docx
- **Modificado:** 2024-05-14
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Módulo PRODEPE

 Relatório Demonstrativo do Cálculo do Crédito Presumido da Importação

__Localização__: Menu Estadual, Módulo: Prodepe, item Relatórios 🡪 Demonstrativo do Cálculo do Crédito Presumido 🡪 Importação

\(este documento de regras é específico do relatório demonstrativo do cálculo do CP do incentivo tipo __Importação__\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS3828

Atualização legal do incentivo da importação

Atualização legal do incentivo da importação \(Lei 15\.675, de 14/12/15, PE\)\.

\(ver item 4\)

05/04/2016 \(criação do documento\)

MFS63900

Tratamento Notas Fiscais de Devolução de Vendas\.

Tratamento nos processos de Cálculo do Crédito Presumido e no Resumo \(P9\) “Detalhamento do Crédito Presumido”\. MFS63900 \(v1\) e MFS63900 \(v2\)\.

04/05/2021

MFS638212

Andréa Rocha

Atualização legal do incentivo da importação \(Lei 18\.305, de 30/09/2023, PE\)\.

\(ver item 4\)

14/05/2024

Sumário

[1\.	Parâmetros da Tela	2](#_Toc447635932)

[2\.	Origem e Recuperação dos Dados	3](#_Toc447635933)

[3\.	Processamento	3](#_Toc447635934)

[4\.	Layout e Preenchimento dos Dados no Relatório	4](#_Toc447635935)

# <a id="_Toc447635932"></a>Parâmetros da Tela 

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

<a id="_Toc350763252"></a><a id="_Toc447635933"></a>

# Origem e Recuperação dos Dados

__Origem dos dados:  __ \- Tabela dos Grupos de Incentivo \(ICT\_GRP\_INCENT\)

                                    \- Tabela das Regras de Incentivo \(ICT\_REGRA\_INCENT\)

                                    \- Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

                                    \- Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\)

As tabelas do valor dos incentivos calculados e do demonstrativo dos incentivos são tabelas que armazenam os resultados do crédito presumido calculado para cada grupo de incentivo e período de apuração\. No incentivo da importação, seus dados são gerados durante o processo do cálculo do crédito presumido\.

A tabela do valor dos incentivos calculados \(ICT\_VLR\_INCENT\) contém uma linha por Grupo de Incentivo e Período, com o resultado final do crédito presumido apurado\.

A tabela do demonstrativo dos incentivos \(ICT\_AP\_DEM\_INCE\) contém todas as informações utilizadas para a emissão de relatório “*Demonstrativo do Cálculo do Crédito Presumido*” e também de um resumo gerado no Livro de Apuração \(P9\) que demonstra detalhes sobre os cálculos do período\.

Serão recuperados os registros da ICT\_VLR\_INCENT para o Estabelecimento e data da apuração informados, que sejam referentes ao incentivo da “Importação”, conforme critérios abaixo:

COD\_EMPRESA      Empresa do login

COD\_ESTAB            Estabelecimento informado     \(poderão ser todos\)

DAT\_APURACAO   data de apuração informada

TIPO\_INCENT          “I”                                           \(todos de Importação\)

Para cada registro de apuração retornado da ICT\_VLR\_INCENT, será obtida a Série/Subsérie do Livro Fiscal na tabela das regras do incentivo \(ICT\_REGRA\_INCENT\) do grupo em questão:

COD\_EMPRESA        Empresa do login

COD\_ESTAB              Estabelecimento

COD\_GRP\_INCENT     grupo de incentivo \(coluna COD\_GRP\_INCENT da ICT\_VLR\_INCENT\)

VALIDADE\_INICIAL   maior data existente que seja <= data de apuração

Com a Série/Subsérie obtidas, serão recuperados os dados para emissão do relatório na tabela ICT\_AP\_DEM\_INCE, conforme critérios abaixo:

COD\_EMPRESA         Empresa do login

COD\_ESTAB               Estabelecimento

COD\_TIPO\_LIVRO     “142”

SERIE\_LIVRO             série do livro obtida na ICT\_REGRA\_INCENT

SUB\_SERIE\_LIVRO   subsérie do livro obtida na ICT\_REGRA\_INCENT

DAT\_APURACAO      data de apuração informada

As linhas desta tabela correspondem aos valores apurados para o demonstrativo dos incentivos que é emitido na Apuração do ICMS \(P9\) dos livros incentivados, no item “*Demonstrativo dos Incentivos*”\. A coluna COD\_DET\_PRODEPE corresponde ao número da linha do demonstrativo, e a coluna VLR\_DET\_PRODEPE corresponde ao valor apurado\.

# <a id="_Toc447635934"></a>Processamento

A partir dos dados recuperados na Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\), o relatório será gerado da seguinte forma:

*Para cada Estabelecimento* será gerada uma página de relatório *para cada grupo de incentivo de Importação* que existir na Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\)\.

*\(lembrando que na tela da geração o usuário pode escolher a opção “Todos” para a lista dos estabelecimentos\)*

Na página será gerado o resumo dos valores conforme layout e preenchimento dos dados descritos no item “*4\-Layout e Preenchimento dos Dados do Relatório*”\.

Os dados serão apresentados em ordem de estabelecimento e grupo de incentivo \(código do grupo\)\.

# <a id="_Toc447635935"></a>Layout e Preenchimento dos Dados no Relatório

__Alteração da MFS63900 \(v1\): O relatório foi alterado para tratar o Estorno de Crédito referente as Devoluções de Vendas, incluído duas linhas:__

__                                                              Grupo de Incentivo: XXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXX__

Importações com ICMS Diferido:                                     *99,99*

ICMS Diferido nas Importações:                                     * 99,99*

Saídas Não\-Incentivadas de Produtos Incentivados:      9*9,99*

__Saídas para fora do Estado__

__Saídas Internas__

Percentual de Incentivo

__* 99,99%*__

__Até 7%__

__7,01% a 12%__

__12,01% a ??%__

__Acima de ??%__

Saídas Incentivadas de Produtos Incentivados

99,99

99,99

99,99

99,99

99,99

Total Saídas Incentivadas

Estorno do Crédito – Devoluções de Vendas

Base para o Crédito Presumido

\- Interestadual: ICMS debitado

\- Interna: Importações

        99,99

       

\(99,99\)

        99,99

        99,99

       \(99,99\)

        99,99

99,99

          \(99,99\)

           99,99

99,99

           \(99,99\)

99,99

99,99

            \(99,99\)

99,99

Crédito Presumido PRODEPE

99,99

99,99

99,99

99,99

99,99

Saldo Devedor do ICMS:			99,99

Saldo a Recolher após Deduções PRODEPE:	99,99

A descrição de cada uma das quatro colunas sob o titulo “Saídas Internas” é fixa, e mostra exatamente a carga tributária das quatro faixas que aparecem na tela da parametrização \(no menu “Parâmetros 🡪 Incentivo – Importação 🡪 Regras de Incentivo”\)\. Com a alteração das duas últimas faixas pela Lei 15\.675, de 14/12/15 \- PE, o título das duas últimas colunas também foi alterado, passando a depender da data da apuração solicitada na emissão do relatório\. 

__Título das colunas das faixas de incentivo:__

Coluna referente às saídas para fora do estado: 

     O título da coluna será o percentual de incentivo parametrizado para as *saídas interestaduais*, no item “*Parâmetros 🡪 Incentivo – Importação 🡪*

*     Regras de Incentivo*”\.

Coluna referentes às saídas internas: 

__     Alteração da MFS3828__: O relatório foi alterado para ajustar a descrição das duas últimas colunas referente às saídas internas:

__     Alteração da MFS638212__: O relatório foi alterado para ajustar a descrição das duas últimas colunas referente às saídas internas:

     O título das duas primeiras faixas será sempre o mesmo, mas as duas últimas dependem do período da apuração, da seguinte forma:

__     Se__ data da apuração <= 31/12/2015 

           Neste caso, as descrições serão as seguintes:

__Até 7%__

__7,01% a 12%__

__12,01% a 17%__

__Acima de 17%__

__     Se__ data da apuração >= 01/01/2016 __e__ <= 31/12/2019

           Neste caso, as descrições serão as seguintes:

__Até 7%__

__7,01% a 12%__

__12,01% a 18%__

__Acima de 18%__

__     Se__ data da apuração >= 01/01/2020__ e__ <= 31/12/2023

           Neste caso, as descrições serão as seguintes:

__Até 7%__

__7,01% a 12%__

__12,01% a 17%__

__Acima de 17%__

__     Se__ data da apuração >= 01/01/2024

           Neste caso, as descrições serão as seguintes:

__Até 7%__

__7,01% a 12%__

__12,01% a 20,5%__

__Acima de 20,5%__

__Alteração da MFS63900 \(v2\): Tratamento das Linhas e Colunas para considerar o Estorno de Crédito referente as Devoluções de Vendas:__

__Total de Saídas Incentivadas:__ Será gravado na linha/coluna o valor do Campo VLR\_TOTAL\_SAI da tabela ICT\_AP\_DEM\_INCE, da seguinte forma:

__Saídas para fora do Estado__

__Saídas Internas \- Até 7%__

__Saídas Internas \- 7,01% a 12%__

__Saídas Internas \- 12,01% a 18%__

__Saídas Internas – Acima de 18%__

__Total de Saídas Incentivadas__

Valor do campo VLR\_TOTAL\_SAI  \(Se houver\)

Valor do campo VLR\_TOTAL\_SAI  \(Se houver\)

Valor do campo VLR\_TOTAL\_SAI  \(Se houver\)

Valor do campo VLR\_TOTAL\_SAI  \(Se houver\)

Valor do campo VLR\_TOTAL\_SAI  \(Se houver\)

Gravar no campo  quando:

COD\_DET\_PRODEPE = 06

COD\_DET\_PRODEPE = 09

COD\_DET\_PRODEPE = 12

COD\_DET\_PRODEPE = 15

COD\_DET\_PRODEPE = 18

__Estorno do Crédito – Devoluções de Vendas:__ Será gravado na linha/coluna o valor do Campo VLR\_TOT\_DEVOL da tabela ICT\_AP\_DEM\_INCE, da seguinte forma:

__Saídas para fora do Estado__

__Saídas Internas \- Até 7%__

__Saídas Internas \- 7,01% a 12%__

__Saídas Internas \- 12,01% a 18%__

__Saídas Internas \- Acima de 18%__

__Estorno do Crédito – Devoluções de Vendas__

Valor  do campo VLR\_TOT\_DEVOL \(Se houver\)

Valor  do campo VLR\_TOT\_DEVOL \(Se houver\)

Valor  do campo VLR\_TOT\_DEVOL \(Se houver\)

Valor  do campo VLR\_TOT\_DEVOL \(Se houver\)

Valor  do campo VLR\_TOT\_DEVOL \(Se houver\)

Gravar no campo  quando:

COD\_DET\_PRODEPE = 06

COD\_DET\_PRODEPE = 09

COD\_DET\_PRODEPE = 12

COD\_DET\_PRODEPE = 15

COD\_DET\_PRODEPE = 18

__Base para o Crédito Presumido: \(VLR\_DET\_PRODEPE\) __Deverá ser gravado na linha de “Base para o Crédito Presumido” o resultado da subtração dos Campos VLR\_TOTAL\_SAI  e VLR\_TOT\_DEVOL, esse valor será a base para o cálculo do crédito presumido, conforme cada faixa de incentivo\.

__Saídas para fora do Estado__

__Saídas Internas \- Até 7%__

__Saídas Internas \- 7,01% a 12%__

__Saídas Internas \- 12,01% a 18%__

__Saídas Internas \- Acima de 18%__

__Base para o Crédito Presumido__ 

Resultado \(VLR\_TOTAL\_SAI \(\-\) VLR\_TOT\_DEVOL\) \(Se houver\)

Resultado \(VLR\_TOTAL\_SAI  \(\-\) VLR\_TOT\_DEVOL\) \(Se houver\)

Resultado \(VLR\_TOTAL\_SAI  \(\-\) VLR\_TOT\_DEVOL\) \(Se houver\)

Resultado \(VLR\_TOTAL\_SAI  \(\-\) VLR\_TOT\_DEVOL\) \(Se houver\)

Resultado \(VLR\_TOTAL\_SAI  \(\-\) VLR\_TOT\_DEVOL\) \(Se houver\)

Gravar no campo  quando:

COD\_DET\_PRODEPE = 06

COD\_DET\_PRODEPE = 09

COD\_DET\_PRODEPE = 12

COD\_DET\_PRODEPE = 15

COD\_DET\_PRODEPE = 18

__Crédito Presumido PRODEPE: __Será gravado o resultado do cálculo da Base para o Crédito Presumido \* o percentual de cada faixa de incentivo conforme regras\.

__Saídas para fora do Estado__

__Saídas Internas \- Até 7%__

__Saídas Internas \- 7,01% a 12%__

__Saídas Internas \- 12,01% a 18%__

__Saídas Internas \- Acima de 18%__

__Crédito Presumido PRODEPE__

Base Crédito Presumido \* Percentual parametrizado\.

Base Crédito Presumido \* 3,5%\.

Base Crédito Presumido \* 6%\.

Base Crédito Presumido \* 8%

Base Crédito Presumido \* 10%\.

Gravar no campo  quando:

COD\_DET\_PRODEPE = 06

COD\_DET\_PRODEPE = 09

COD\_DET\_PRODEPE = 12

COD\_DET\_PRODEPE = 15

COD\_DET\_PRODEPE = 18

__Preenchimento dos dados:__

__              Campo do Relatório__

__              Linha  e  coluna  da  ICT\_AP\_DEM\_INCE __

Importações com ICMS Diferido

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 01

ICMS Diferido nas Importações

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 02

Saídas Não\-Incentivadas de Produtos Incentivados

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 03

Percentual de Incentivo \(da coluna “Saídas para fora do Estado”\)

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 04

__Saídas Incentivadas de Produtos Incentivados:__

Coluna “Saídas para fora do Estado”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 05

Coluna “Saídas Internas – Até 7%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 08

Coluna “Saídas Internas – 7,01% a 12%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 11

Coluna “Saídas Internas – 12,01% a 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 14

Coluna “Saídas Internas – Acima de 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 17

__Base para o Crédito Presumido__:

Coluna “Saídas \(\-\) Devoluções de Vendas para fora do Estado”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 06

Coluna “Saídas Internas \(\-\) Devoluções de Vendas – Até 7%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 09

Coluna “Saídas Internas \(\-\) Devoluções de Vendas – 7,01% a 12%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 12

Coluna “Saídas Internas  \(\-\) Devoluções de Vendas – 12,01% a 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 15

Coluna “Saídas Internas \(\-\) Devoluções de Vendas – Acima de 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 18

__Crédito Presumido PRODEPE__:

Coluna “Saídas para fora do Estado”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 07

Coluna “Saídas Internas – Até 7%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 10

Coluna “Saídas Internas – 7,01% a 12%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 13

Coluna “Saídas Internas – 12,01% a 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 16

Coluna “Saídas Internas – Acima de 17%”

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 19

Saldo Devedor do ICMS

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 20

Saldo a Recolher após Deduções PRODEPE

VLR\_DET\_PRODEPE  da linha com  COD\_DET\_PRODEPE = 21

= = = = = =

 

