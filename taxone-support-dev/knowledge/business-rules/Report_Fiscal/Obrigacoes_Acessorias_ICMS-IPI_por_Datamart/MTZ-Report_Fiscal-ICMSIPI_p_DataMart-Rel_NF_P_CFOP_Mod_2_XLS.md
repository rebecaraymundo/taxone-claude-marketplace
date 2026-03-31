---
source: "MTZ-Report_Fiscal-ICMSIPI_p_DataMart-Rel_NF_P_CFOP_Mod_2_XLS.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL  


Relatório de NF p/ CFOP Modelo 2 - Formato XLS


Menu: Básicos - Report Fiscal > Obrigações Acessórias --> ICMS/IPI por DataMart -->Relatório de NF p/ CFOP Modelo 2 - Formato XLS

DOCUMENTO DE REQUISITO


DR
Nome
Descrição
MFS32994
Andréa Rocha
Incluir novas colunas no relatório, mostrando os campos BC ICMS ST, Base do PIS e do COFINS, Valores PIS e COFINS.
MFS33071
Andréa Rocha
Incluir novas colunas no relatório, mostrando os campos de Código do Benefício, Valor Desonerado ICMS e Valor Diferido ICMS.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN01
Nova Coluna: Base ICMS-ST:

Preencher com o campo 61- Base ICMS Substituição Tributária da SAFX08.
MFS32994
RN02
Nova Coluna: Base PIS:

Preencher com o campo 86- Base PIS da SAFX08.
MFS32994
RN03
Nova Coluna: Valor PIS:

Preencher com o campo 87- Valor PIS da SAFX08.
MFS32994
RN04
Nova Coluna: Base COFINS:

Preencher com o campo 88- Base COFINS da SAFX08.
MFS32994
RN05
Nova Coluna: Valor COFINS:

Preencher com o campo 89- Valor COFINS da SAFX08.
MFS32994
RN06
Nova Coluna: Código do Benefício:

Preencher com o campo 255- Código do Benefício da SAFX08.
MFS33071
RN07
Nova Coluna: Vlr Desonerado ICMS:

Preencher com o campo 258- Valor Desonerado ICMS da SAFX08.
MFS33071
RN08
Nova Coluna: Vlr Diferido ICMS:

Preencher com o campo 259- Valor Diferido ICMS da SAFX08.
MFS33071


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

