# MTZ-LAICMS-Calculo_Estorno_Cred_Presumido-Transporte

- **Fonte:** MTZ-LAICMS-Calculo_Estorno_Cred_Presumido-Transporte.docx
- **Modificado:** 2026-02-25
- **Tamanho:** 69 KB

---

THOMSON REUTERS

                                                          __Módulo Lançamentos Automáticos de ICMS__

__  __

__                                    Cálculo do Lançamento de Estorno de Crédito Presumido Transporte__

__Localização__: Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Lançamentos 🡪 Cálculo dos Lançamentos

__Obs:__ Este menu faz a chamada do cálculo de cada um dos lançamentos automáticos disponíveis no módulo LAICMS\.  Este documento de regras é específico do lançamento “Estorno de Crédito Presumido Transporte”\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS565161

Andréa Rocha

Criação do cálculo do lançamento de estorno do crédito presumido transporte\. 

08/09/2023

REGRAS DE NEGÓCIO

__RN00 – Regras Gerais__

O objetivo desse cálculo é recuperar as notas de entrada, parametrizadas por CFOP/Natureza, que são as anulações da prestação de serviço de transporte, que são usadas para calcular o estorno de crédito presumido de transporte\. Depois do cálculo feito, é gerado um lançamento automático de estorno de crédito presumido de transporte, que posteriormente pode ser lançado na apuração do ICMS\.

Obs\.:  As notas de saída de transporte são usadas para calcular o crédito presumido de transporte, que gera um lançamento automático de crédito presumido de transporte \(vide documento MTZ\-LAICMS\-Calculo\_Cred\_Presumido\-Transporte\.docx\)\.  

__Origem dos Dados__: SAFX07 

                                   Tabelas das parametrizações 

                                   \(Parâmetros p/ Cálculos de Lançamentos, Parâmetros de Lançamentos Automáticos, CFOP, Extensão CFOP, Parâmetros Gerais\)

Para cada lançamento, o cálculo é realizado nota a nota\. No final, o resultado será o total do valor calculado das notas de entrada\.

  

__Critérios de recuperação das notas de entradas \(anulações\)__:

- Código da Empresa = empresa do login;
- Código do Estabelecimento = estabelecimento selecionado em tela para o cálculo;
- Data do Movimento = data fiscal;
- Somente notas de entrada \(MOVTO\_E\_S <> ‘9’\);
- Somente notas não canceladas \(SITUACAO <> ‘S’\);
- CFOP ou CFOP/Natureza deve estar parametrizado no menu Parâmetros 🡪 Imposto sobre Serviço de Transporte 🡪 Crédito Presumido 🡪 Por CFOP – Anulação ou Por Extensão de CFOP \- Anulação;

__Para cada nota, o cálculo é feito da seguinte forma__:

Valor ICMS \* \(Percentual / 100\)

*   *  \- Valor ICMS = campo 35 da SAFX07

     \- Percentual = Percentual recuperado da tela de Parâmetros Gerais \(menu Parâmetros 🡪 Imposto sobre Serviço de Transporte 🡪 Crédito Presumido 🡪 Parâmetros Gerais\)

__RN02 – Gravação dos Resultados__

Os resultados dos lançamentos de estorno de crédito de cada estabelecimento, serão gravados em uma tabela auxiliar \(EST\_LANCTO\_P9\), e poderão ser consultados através do menu “Lançamentos 🡪 Listagem / Consulta da Apuração”\.

Posteriormente, estes lançamentos poderão ser lançados na apuração do ICMS, seja manualmente, ou através da rotina de lançamento automático na apuração disponível no módulo \(menu “Lançamentos 🡪 Lançamento no Livro de Apuração”\)\.

__Tabela__ __EST\_LANCTO\_P9__

__Regra de Preenchimento__

COD\_EMPRESA

Código da empresa do login

COD\_ESTAB

Código do estabelecimento selecionado para geração

DAT\_APURACAO

Data fim do Período informado na tela de Geração

COD\_PAR\_LANCTO

COD\_PAR\_LANCTO\_25 da parametrização de Cálculos de Lançamentos

COD\_OPER\_APUR

Código do item de apuração à débito da parametrização de Lançamentos Automáticos

DSC\_ITEM\_APUR

Descrição do item de apuração à débito da parametrização de Lançamentos Automáticos

COD\_TIPO\_LIVRO

Código do tipo do livro selecionado para geração

VLR\_ESTORNO

Total do valor calculado

COD\_CLASSE

Código da classe de lançamento à débito da parametrização de Lançamentos Automáticos

COD\_AMPARO\_LEGAL

Código do amparo à débito da parametrização de Lançamentos Automáticos

COD\_SUB\_ITEM\_OCORR

Código do subitem à débito da parametrização de Lançamentos Automáticos

COD\_AJUSTE\_ICMS

Código de ajuste à debito da parametrização de Lançamentos Automáticos

IND\_TIPO\_LANC

Indicador do tipo de lançamento da parametrização de Lançamentos Automáticos

                                                          = = = = = / / / = = = = =

