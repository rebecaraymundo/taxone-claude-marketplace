# MTZ-LAICMS-Calculo_Cred_Presumido-Transporte

- **Fonte:** MTZ-LAICMS-Calculo_Cred_Presumido-Transporte.docx
- **Modificado:** 2025-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

                                                          __Módulo Lançamentos Automáticos de ICMS__

__  __

__                                    Cálculo do Lançamento de Crédito Presumido Transporte__

__Localização__: Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Lançamentos 🡪 Cálculo dos Lançamentos

__Obs:__ Este menu faz a chamada do cálculo de cada um dos lançamentos automáticos disponíveis no módulo LAICMS\.  Este documento de regras é específico do lançamento “Crédito Presumido Transporte”\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS565161

Andréa Rocha

Alteração da forma de cálculo do lançamento para recuperar as notas fiscais de anulação para fazer o estorno no cálculo do crédito presumido\. Como não existia um documento de regras desta rotina, foi descrita a regra básica de cálculo e está sendo documentada a parte da regra alterada\.

04/09/2023

MFS747010

Andréa Rocha

Inclusão da gravação dos lançamentos complementares para o tipo de lançamento igual a 1 ou 2, fazendo o vínculo com os documentos fiscais\.  Esse cálculo só gerava os lançamentos com o tipo de lançamento igual a 3, que não tem vínculo com documento fiscal\.

28/02/2025

REGRAS DE NEGÓCIO

__RN00 – Regras Gerais__

O objetivo desse cálculo é recuperar as notas de saída de transporte, que são usadas para calcular o crédito presumido de transporte\. Depois do cálculo feito, é gerado um lançamento automático de crédito presumido de transporte, que posteriormente pode ser lançado na apuração do ICMS\.

__Origem dos Dados__: SAFX07 

                                   Tabelas das parametrizações 

                                   \(Classes de Relatórios, Parâmetros p/ Cálculos de Lançamentos, CFOP, Extensão CFOP, Parâmetros Gerais\)

Para cada lançamento, o cálculo é realizado nota a nota\. No final, o resultado será o total do valor calculado das notas de saída\.

__Critérios de recuperação das notas de saídas__:

- Código da Empresa = empresa do login;
- Código do Estabelecimento = estabelecimento selecionado em tela para o cálculo;
- Data do Movimento = data fiscal;
- Somente notas de saída \(MOVTO\_E\_S = ‘9’\);
- Somente notas não canceladas \(SITUACAO <> ‘S’\);
- Classificação de documento fiscal igual '4' ou '5' ou '6';

__Para cada nota, o cálculo é feito da seguinte forma__:

O cálculo depende da parametrização para o Cálculo do Lançamento \(menu  Parâmetros 🡪 Imposto sobre Serviço de Transporte 🡪 Crédito Presumido 🡪 Parâmetros Gerais\)\.

Parâmetros: Situação Tributária a considerar e Percentual 

Se a UF do Estabelecimento <> ‘MG’, ‘AM’, ‘BA, ‘SP’

     Se CST = ‘00’ E indicador de Situação Tributária do CST \(00\) estiver marcado

           Valor Calculado = Valor ICMS \* \(Percentual / 100\)

     Senão Se CST = ‘10’ E indicador de Situação Tributária do CST \(10\) estiver marcado

                Valor Calculado = Valor ICMS Substituição Tributária \* \(Percentual / 100\)

     Senão Se CST = ‘20’ E indicador de Situação Tributária do CST \(20\) estiver marcado

                Valor Calculado = Valor ICMS \* \(Percentual / 100\)

     Senão Se CST = ‘50’ E indicador de Situação Tributária do CST \(50\) estiver marcado

                Valor Calculado = ICMS Não Escriturado \* \(Percentual / 100\)

     Senão Se CST = ‘51’ E indicador de Situação Tributária do CST \(51\) estiver marcado

                Valor Calculado = ICMS Não Escriturado \* \(Percentual / 100\)

     Senão Se CST = ‘60’ E indicador de Situação Tributária do CST \(60\) estiver marcado

                Valor Calculado = Base Outras ICMS\-S \* \(Percentual / 100\)

     Senão Se CST = ‘70’ E indicador de Situação Tributária do CST \(70\) estiver marcado

                Valor Calculado = Valor ICMS Substituição Tributária \* \(Percentual / 100\)

     Senão Se CST = ‘90’ E indicador de Situação Tributária do CST \(90\) estiver marcado

                Valor Calculado = ICMS Não Escriturado \* \(Percentual / 100\)

Se a UF do Estabelecimento = ‘MG’

     Se CST = ‘00’ ou ‘20’

           Valor Calculado = Valor ICMS \* \(Percentual / 100\)

     Senão Se CST = ‘10’ ou ‘60’ ou ‘70’

                Valor Calculado = Valor ICMS Substituição Tributária \* \(Percentual / 100\)

Se a UF do Estabelecimento = ‘AM’ ou ‘BA’

     Se CST = ‘00’ ou ‘20’

           Valor Calculado = Valor ICMS \* \(Percentual / 100\)

Se a UF do Estabelecimento = ‘SP

     Se CST = ‘00’ ou ‘20’

           Valor Calculado = Valor ICMS \* \(Percentual / 100\)

    Senão Se CST = ‘10’ ou ‘60’ ou ‘70’ ou ‘90’

                Valor Calculado = Base Outras ICMS\-S \* \(Alíquota ICMS ST/ 100\) \* \(Percentual / 100\)

Campos:

\- CST \(Tabela Situação Estadual “B”\) = campo 180 da SAFX07

\- Valor ICMS = campo 180 da SAFX07

\- Valor ICMS Substituição Tributária = campo 48 da SAFX07

\- ICMS Não Escriturado = campo 168 da SAFX07

\- Base Outras ICMS\-S = campo 111 da SAFX07

   

__RN02 – Gravação dos Resultados__

Os resultados dos lançamentos de crédito de cada estabelecimento, serão gravados em uma tabela auxiliar \(EST\_LANCTO\_P9\), e poderão ser consultados através do menu “Lançamentos 🡪 Listagem / Consulta da Apuração”\.

Posteriormente, estes lançamentos poderão ser lançados na apuração do ICMS, seja manualmente, ou através da rotina de lançamento automático na apuração disponível no módulo \(menu “Lançamentos 🡪 Lançamento no Livro de Apuração”\)\.

__\[MFS747010\] __Inclusão da gravação dos tipos de lançamentos igual a 1 ou 2

__RN03 – Gravação dos Tipos de Lançamentos__

A partir da parametrização feita nos lançamentos automáticos para o lançamento de Crédito Presumido de Transporte, item de menu: Módulo Lançamentos Automáticos de ICMS, item Parâmetros 🡪 Lançamentos Automáticos, serão gravados os documentos fiscais vinculados aos lançamentos complementares de acordo com o tipo de lançamento informado: 

- Quando o tipo do lançamento parametrizado __= 1__, os itens das notas fiscais que compõem o total do lançamento deverão ser gravados numa tabela auxiliar, conforme o padrão dos lançamentos complementares\.
- Quando o tipo do lançamento parametrizado __=__ __2__, os itens das notas fiscais que compõem o total do lançamento deverão ser gravados numa tabela auxiliar, conforme o padrão dos lançamentos complementares \(o objetivo de guardar as notas que originaram o lançamento, é posteriormente gerar o registro E113 do Sped Fiscal\)\. 
- Para o tipo de lançamento parametrizado __= 3 \(ou nulo\)__, a gravação das notas na tabela auxiliar não é realizada, lembrando que quando esta informação não for preenchida na parametrização, o tipo do lançamento será gravado como “3”\.

__Obs__\.: O valor a ser gravado na tabela  \(EST\_LANCTO\_P9\_NF\), que armazenam as notas fiscais deve ser sempre o valor que foi considerado para compor o lançamento, que será o valor calculado\. 

__Obs__\. __2__:  Posteriormente, quando for executada a rotina de lançamento no livro de apuração, os lançamentos com o tipo igual a 1, irão gravar os registros na SAFX112 e SAFX113\.  E os lançamentos com o tipo igual a 2, irão gravar os documentos fiscais vinculados aos lançamentos da apuração\.

