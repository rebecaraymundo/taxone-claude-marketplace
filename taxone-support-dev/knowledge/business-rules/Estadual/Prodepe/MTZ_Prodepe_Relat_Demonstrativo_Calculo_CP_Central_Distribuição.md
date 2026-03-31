# MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Central_Distribuição

- **Fonte:** MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Central_Distribuição.docx
- **Modificado:** 2022-04-04
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Módulo PRODEPE

 Relatório Demonstrativo do Cálculo do Crédito Presumido de Central de Distribuição

__Localização__: Menu Estadual, Módulo: Prodepe, item Relatórios 🡪 Demonstrativo do Cálculo do Crédito Presumido 🡪 Central de Distribuição

\(este documento de regras é específico do relatório demonstrativo do cálculo do CP do incentivo tipo __Central de Distribuição__\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS81635

Rogério Ohashi

Alteração na Descrição da Coluna de “Operação Incentivadas – Valor Contábil”\.

04/04/2022

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

# <a id="_Toc350763252"></a><a id="_Toc447635933"></a>Origem e Recuperação dos Dados

__Origem dos dados:  __ \- Tabela dos Grupos de Incentivo \(ICT\_GRP\_INCENT\)

                                    \- Tabela das Regras de Incentivo \(ICT\_REGRA\_INCENT\)

                                    \- Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

                                    \- Tabela do Demonstrativo dos Incentivos \(ICT\_AP\_DEM\_INCE\)

As tabelas do valor dos incentivos calculados e do demonstrativo dos incentivos são tabelas que armazenam os resultados do crédito presumido calculado para cada grupo de incentivo e período de apuração\. Seus dados são gerados durante o processo do cálculo do crédito presumido\.

A tabela do valor dos incentivos calculados \(ICT\_VLR\_INCENT\) contém uma linha por Grupo de Incentivo e Período, com o resultado final do crédito presumido apurado\.

A tabela do demonstrativo dos incentivos \(ICT\_AP\_DEM\_INCE\) contém todas as informações utilizadas para a emissão de relatório “*Demonstrativo do Cálculo do Crédito Presumido*” e, também de um resumo gerado no Livro de Apuração \(P9\) que demonstra detalhes sobre os cálculos do período\.

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

*Para cada Estabelecimento* será gerada uma página de relatório *para cada grupo de incentivo de Central de Distribuição* que existir na Tabela dos Valores dos Incentivos Calculados \(ICT\_VLR\_INCENT\)\.

*\(lembrando que na tela da geração o usuário pode escolher a opção “Todos” para a lista dos estabelecimentos\)*

Na página será gerado o resumo dos valores conforme layout e preenchimento dos dados descritos no item “*4\-Layout e Preenchimento dos Dados do Relatório*”\.

Os dados serão apresentados em ordem de estabelecimento e grupo de incentivo \(código do grupo\)\.

# <a id="_Toc447635935"></a>Layout e Preenchimento dos Dados no Relatório

__Alteração da MFS81635: Alteração na descrição da coluna “Operações Incentivadas – Valor Contábil":__

__Tratamento: __

Alterar a descrição de: Operações Incentivadas \(Valor Contábil\)

                           Para: Operações Incentivadas \(Valor da Operação\), conforme abaixo:

__Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição__

Filial:

Grupo de Incentivo

Descrição

Percentual

Operações Incentivadas  
\(Valor da Operação\)

\(Valor Contábil\)

Crédito Presumido

Entradas

Saídas

Entradas

Saídas

Entradas

Saídas

 

 

 

 

 

 

 

 

= = = = = =

 

