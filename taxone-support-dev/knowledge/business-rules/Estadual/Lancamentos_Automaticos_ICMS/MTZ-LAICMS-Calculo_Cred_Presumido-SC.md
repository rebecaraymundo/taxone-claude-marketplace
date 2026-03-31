# MTZ-LAICMS-Calculo_Cred_Presumido-SC

- **Fonte:** MTZ-LAICMS-Calculo_Cred_Presumido-SC.docx
- **Modificado:** 2026-02-25
- **Tamanho:** 69 KB

---

THOMSON REUTERS

                                                          __Módulo Lançamentos Automáticos de ICMS__

__  __

__                                    Cálculo do Lançamento de Crédito Presumido – SC__

__Localização__: Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Lançamentos 🡪 Cálculo dos Lançamentos

__Obs:__ Este menu faz a chamada do cálculo de cada um dos lançamentos automáticos disponíveis no módulo LAICMS\.  Este documento de regras é específico do lançamento “Crédito Presumido – SC”\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS46704

Andréa Rocha

Alteração da forma de cálculo do lançamento para incluir a opção de selecionar qual o valor a ser utilizado para o cálculo do crédito presumido\. Como não existia um documento de regras desta rotina, foi descrita a regra básica de cálculo e está sendo documentada a parte da regra alterada\.

25/02/2021

MFS66742

Andréa Rocha

Alteração da forma de cálculo do lançamento quando se utiliza o parâmetro “Valor Utilizado para o Cálculo” igual a “Base ICMS”, para tratar a situação da nota fiscal que não tem Base de ICMS destacado\. 

16/06/2021

REGRAS DE NEGÓCIO

__RN00 – Regras Gerais__

__Origem dos Dados__: SAFX07 e SFAX08

                                   Tabelas das parametrizações 

                                   \(Classes de Relatórios, Parâmetros p/ Cálculos de Lançamentos, CFOP, Pessoa Física/Jurídica, NCM, Produtos e Pauta de Preço Mínimo de   

                                     Frete\)

Para cada lançamento, o cálculo é realizado nota a nota\. No final, o resultado será o total geral de todas as notas\.

__Critérios referentes a capa da nota__:

- Código da Empresa = empresa do login;
- Código do Estabelecimento = estabelecimento selecionado em tela para o cálculo;
- Data do Movimento = data de emissão ou data fiscal, de acordo com a data selecionada no quadro de Critério p/ Crédito Presumido – SC \(menu  Parâmetros 🡪 Parâmetros p/ Cálculos de Lançamentos\)\.

       \-     Movimento E/S \(MOVTO\_E\_S\) =  de acordo com o campo Mov\. Entrada/Saída da tela de Classes de Relatórios \(menu Parâmetros 🡪  

Parâmetros p/ Cálculos e Relatórios 🡪 Classes de Relatórios\);

       \-     Pessoa Física/Jurídica = pessoa física/jurídica parametrizada \(menu Parâmetros 🡪 Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/  

             Pessoa Física/Jurídica\);

__Critérios referentes ao item da nota__:

     \- O item \(SAFX08\) deve ter o CFOP parametrizado \(menu Parâmetros 🡪 Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/ CFOP\);

      Com a opção de seleção criada na parametrização p/ Cálculos de Lançamentos \(menu “Parâmetros 🡪 Parâmetros p/ Cálculo de Lançamentos”\), a verificação     

      do item em relação aos critérios de NBM e Produto, será feita da seguinte forma:

     \- Se parâmetro “Seleção” = CFOP/NBM 🡪 o NBM do item \(SAFX08\) deve estar parametrizado \(menu Parâmetros 🡪 Parâmetros p/ Cálculos e Relatórios 🡪    

       Parâmetros de Relatórios p/ NBM\);

     \- Se parâmetro “Seleção” = CFOP/Produto 🡪 o produto do item \(SAFX08\) deve estar parametrizado \(menu Parâmetros 🡪 Parâmetros p/ Cálculos e Relatórios     

       🡪  Parâmetros de Relatórios p/ Produto\);

__\[MFS46704\]__ __Alteração da forma de cálculo do valor do lançamento__

__Para cada nota, o cálculo é feito da seguinte forma__:

O cálculo depende da opção utilizada na parametrização para o Cálculo do Lançamento \(menu  Parâmetros 🡪 Parâmetros p/ Cálculos de Lançamentos\)\.

Parâmetro: Valor Utilizado para o Cálculo \(Quadro: Critério p/ Crédito Presumido – SC\)

Opção Valor Contábil do Item 🡪 O crédito é calculado da seguinte forma:

Valor Contábil do Item \* \(Percentual Recuperado / 100\)

*   *  \- Valor Contábil do Item = campo 64 da SAFX08

     \- Percentual Recuperado = Percentual Recuperado da parametrização do Produto ou NBM, conforme parametrização selecionada \(menu Parâmetros 🡪  

        Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/ Produto ou Parâmetros de Relatórios p/ NBM\)

__Obs\.:__ A opção “Valor Contábil do Item” era a forma existente de cálculo, antes de ser criada a parametrização “Valor Utilizado para o Cálculo”\.

Opção Base ICMS 🡪 O crédito é calculado da seguinte forma:

Base ICMS \* \(Percentual Recuperado / 100\)

*   *  \- Base ICMS = campo 56 da SAFX08

     \- Percentual Recuperado = Percentual Recuperado da parametrização do Produto ou NBM, conforme parametrização selecionada \(menu Parâmetros 🡪  

        Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/ Produto ou Parâmetros de Relatórios p/ NBM\)

__     \[MFS66742\]__ __Alteração da forma de cálculo para o parâmetro “Valor Utilizado para o Cálculo” igual a “Base ICMS”,__ __para tratar a situação da nota fiscal  __

__                          que não tem Base de ICMS destacado__

     Se a Base ICMS não estiver preenchida ou estiver preenchida com zero e o CST = ‘51’

          Utilizar o Valor Contábil do Item para fazer o cálculo \(Valor Contábil do Item \* \(Percentual Recuperado / 100\)\)	

   *   *  

         \- CST \(Tabela Situação Estadual “B”\) = campo 31 da SAFX08

   

__RN02 – Gravação dos Resultados__

Os resultados dos lançamentos de crédito de cada estabelecimento, serão gravados em uma tabela auxiliar \(EST\_LANCTO\_P9\), e poderão ser consultados através do menu “Lançamentos 🡪 Listagem / Consulta da Apuração”\.

Posteriormente, estes lançamentos poderão ser lançados na apuração do ICMS, seja manualmente, ou através da rotina de lançamento automático na apuração disponível no módulo \(menu “Lançamentos 🡪 Lançamento no Livro de Apuração”\)\.

                                                          = = = = = / / / = = = = =

