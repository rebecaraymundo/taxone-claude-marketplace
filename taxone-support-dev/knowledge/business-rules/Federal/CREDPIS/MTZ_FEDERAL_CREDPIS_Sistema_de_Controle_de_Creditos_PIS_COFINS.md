# MTZ_FEDERAL_CREDPIS_Sistema_de_Controle_de_Creditos_PIS_COFINS

- **Fonte:** MTZ_FEDERAL_CREDPIS_Sistema_de_Controle_de_Creditos_PIS_COFINS.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 64 KB

---

THOMSON REUTERS

CREDPIS

Sistema de Controle de Créditos PIS/COFINS

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH8037\_2016

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento dos campos “Alíquota PIS” e “Alíquota COFINS” do Cadastro de Bens para que o bem importado receba alíquota diferenciada de acordo com MP Nº 668/2015\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

*<reservado para regra geral>*

<MFS>

RN01

__Cadastro de Bens__

__\[ALTERADA – CH8037\_2016\]__

Preenchimento campo Alíquota PIS:

Verifica se o Bem cadastrado na tabela SAFX13 \- Arquivo de Cadastro de Bem controla o crédito de PIS e COFINS e preenche o campo de alíquota do PIS com 1,65 \(quando a PFJ da tabela SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas vinculada ao bem estiver com o campo UF <> EX\) ou com 2,10 \(quando a PFJ da tabela SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas vinculada ao bem estiver com o campo UF = EX\)\.

Preenchimento campo Alíquota COFINS:

Verifica se o Bem cadastrado na tabela SAFX13 \- Arquivo de Cadastro de Bem controla o crédito de PIS e COFINS e preenche o campo de alíquota do COFINS com 7,60 \(quando a PFJ da tabela SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas vinculada ao bem estiver com o campo UF <> EX\) ou com 9,65 \(quando a PFJ da tabela SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas vinculada ao bem estiver com o campo UF = EX\)\.

CH8037\_2016

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

