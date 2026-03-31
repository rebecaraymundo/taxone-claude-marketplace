# MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Central_Distribuição

> Fonte: MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP_Central_Distribuição.docx






THOMSON REUTERS

Módulo PRODEPE

Relatório Demonstrativo do Cálculo do Crédito Presumido de Central de Distribuição


Localização: Menu Estadual, Módulo: Prodepe, item Relatórios  Demonstrativo do Cálculo do Crédito Presumido  Central de Distribuição


(este documento de regras é específico do relatório demonstrativo do cálculo do CP do incentivo tipo Central de Distribuição)

DOCUMENTO DE REQUISITO





Sumário

1.	Parâmetros da Tela	2
2.	Origem e Recuperação dos Dados	3
3.	Processamento	3
4.	Layout e Preenchimento dos Dados no Relatório	4




















## Parâmetros da Tela






## Origem e Recuperação dos Dados



Origem dos dados:   - Tabela dos Grupos de Incentivo (ICT_GRP_INCENT)
- Tabela das Regras de Incentivo (ICT_REGRA_INCENT)
- Tabela dos Valores dos Incentivos Calculados (ICT_VLR_INCENT)
- Tabela do Demonstrativo dos Incentivos (ICT_AP_DEM_INCE)

As tabelas do valor dos incentivos calculados e do demonstrativo dos incentivos são tabelas que armazenam os resultados do crédito presumido calculado para cada grupo de incentivo e período de apuração. Seus dados são gerados durante o processo do cálculo do crédito presumido.

A tabela do valor dos incentivos calculados (ICT_VLR_INCENT) contém uma linha por Grupo de Incentivo e Período, com o resultado final do crédito presumido apurado.

A tabela do demonstrativo dos incentivos (ICT_AP_DEM_INCE) contém todas as informações utilizadas para a emissão de relatório “Demonstrativo do Cálculo do Crédito Presumido” e, também de um resumo gerado no Livro de Apuração (P9) que demonstra detalhes sobre os cálculos do período.

Serão recuperados os registros da ICT_VLR_INCENT para o Estabelecimento e data da apuração informados, que sejam referentes ao incentivo da “Importação”, conforme critérios abaixo:

COD_EMPRESA      Empresa do login
COD_ESTAB            Estabelecimento informado     (poderão ser todos)
DAT_APURACAO   data de apuração informada
TIPO_INCENT          “I”                                           (todos de Importação)

Para cada registro de apuração retornado da ICT_VLR_INCENT, será obtida a Série/Subsérie do Livro Fiscal na tabela das regras do incentivo (ICT_REGRA_INCENT) do grupo em questão:

COD_EMPRESA        Empresa do login
COD_ESTAB              Estabelecimento
COD_GRP_INCENT     grupo de incentivo (coluna COD_GRP_INCENT da ICT_VLR_INCENT)
VALIDADE_INICIAL   maior data existente que seja <= data de apuração

Com a Série/Subsérie obtidas, serão recuperados os dados para emissão do relatório na tabela ICT_AP_DEM_INCE, conforme critérios abaixo:

COD_EMPRESA         Empresa do login
COD_ESTAB               Estabelecimento
COD_TIPO_LIVRO     “142”
SERIE_LIVRO             série do livro obtida na ICT_REGRA_INCENT
SUB_SERIE_LIVRO   subsérie do livro obtida na ICT_REGRA_INCENT
DAT_APURACAO      data de apuração informada

As linhas desta tabela correspondem aos valores apurados para o demonstrativo dos incentivos que é emitido na Apuração do ICMS (P9) dos livros incentivados, no item “Demonstrativo dos Incentivos”. A coluna COD_DET_PRODEPE corresponde ao número da linha do demonstrativo, e a coluna VLR_DET_PRODEPE corresponde ao valor apurado.


## Processamento


A partir dos dados recuperados na Tabela do Demonstrativo dos Incentivos (ICT_AP_DEM_INCE), o relatório será gerado da seguinte forma:

Para cada Estabelecimento será gerada uma página de relatório para cada grupo de incentivo de Central de Distribuição que existir na Tabela dos Valores dos Incentivos Calculados (ICT_VLR_INCENT).

(lembrando que na tela da geração o usuário pode escolher a opção “Todos” para a lista dos estabelecimentos)

Na página será gerado o resumo dos valores conforme layout e preenchimento dos dados descritos no item “4-Layout e Preenchimento dos Dados do Relatório”.

Os dados serão apresentados em ordem de estabelecimento e grupo de incentivo (código do grupo).






## Layout e Preenchimento dos Dados no Relatório


Alteração da MFS81635: Alteração na descrição da coluna “Operações Incentivadas – Valor Contábil":

Tratamento:

Alterar a descrição de: Operações Incentivadas (Valor Contábil)
Para: Operações Incentivadas (Valor da Operação), conforme abaixo:



= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS81635 | Rogério Ohashi | Alteração na Descrição da Coluna de “Operação Incentivadas – Valor Contábil”. | 04/04/2022 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |


| Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição | Demonstrativo do Cálculo do Crédito Presumido – Central de Distribuição |  |
| Filial: | Filial: | Filial: | Filial: | Filial: | Filial: | Filial: | Filial: |  |
| Grupo de Incentivo | Descrição | Percentual | Percentual | Operações Incentivadas (Valor da Operação) (Valor Contábil) | Operações Incentivadas (Valor da Operação) (Valor Contábil) | Crédito Presumido | Crédito Presumido |  |
| Grupo de Incentivo | Descrição | Entradas | Saídas | Entradas | Saídas | Entradas | Saídas |  |
|  |  |  |  |  |  |  |  |  |
