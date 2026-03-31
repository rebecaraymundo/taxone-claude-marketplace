---
source: "MTZ-Report_Fiscal-Gerenciais-Conferencia_de_entradas.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Conferência de Entradas (Ajuste SINEF)

Módulo: Básicos --> Report Fiscal
Menu: Gerencias --> Documentos Fiscais --> Conferência dos movimentos p/ DataMart --> Movimento de entrada --> Ajuste SINIEF


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3519
Critério de ordenação "Data + Série + Subsérie + Nº Documento"

Incluído novo critério de ordenação para a geração do relatório.

CH4675_2013
Ordenação dos valores dentro do relatório
Alterado o critério de ordenação dos valores de ICMS, IPI e ICMS ST do relatório.

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Regras Gerais

RN01
Ordenação por "Data + Série + Subsérie + Nº Documento"

Se este critério for selecionado, ordenar os dados por ordem crescente, onde:

Data = Campos 03 (DATA_FISCAL) da SAFX08 e SAFX09
Série = Campo 10 (SERIE_DOCFIS) da SAFX08 e SAFX09
SubSérie = Campo 11 (SUB_SERIE_DOCFIS) da SAFX08 e  SAFX09
Nº Documento: Campo 09 (NUM_DOCFIS) da SAFX08 e SAFX09


Para quando não houver item no documento fiscal, então ordenar os dados de acordo com os campos da SAFX07:

Data = DATA_FISCAL da SAFX07
Série = Campo 09 (SERIE_DOCFIS) da SAFX07
SubSérie = Campo 10 (SUB_SERIE_DOCFIS) da SAFX07
Nº Documento: Campo 08 (NUM_DOCFIS) da SAFX07

OS3519
RN02
Ordenação dos valores demonstrados no relatório:

Os valores das notas fiscais apresentadas no relatório devem seguir a seguinte ordem independente do critério de seleção utilizado na tela de geração do mesmo:

ICMS 1  -  Para valores destacados de ICMS tributável
ICMS 2  -  Para valores de ICMS na base ISENTAS
ICMS 3  -  Para valores de ICMS na base OUTRAS
IPI 1  -  Para valores destacados de IPI tributável
IPI 2  -  Para valores de ICMS na base ISENTAS
IPI 3  -  Para valores de ICMS na base OUTRAS
ICMS ST 1  -  Para valores destacados de ICMS ST tributável
ICMS ST 2  -  Para valores de ICMS ST na base ISENTAS
ICMS ST 3  -  Para valores de ICMS ST na base OUTRAS

 
CH4675_2013
RN03
Opção dos critérios de seleção do relatório:

Os critérios de TIPO DE ORDENAÇÃO do relatório devem ficar disponíveis para seleção tanto para a opção CONTA CONTÁBIL ou Nº DE CONTROLE do parâmetro CAMPO A SER EXIBIDO. Trazendo como opção DEFAULT os campos "CONTA CONTÁBIL" e "DATA + SERIE + SUBSERIE + Nº DO DOCUMENTO" 


CH4675_2013


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

