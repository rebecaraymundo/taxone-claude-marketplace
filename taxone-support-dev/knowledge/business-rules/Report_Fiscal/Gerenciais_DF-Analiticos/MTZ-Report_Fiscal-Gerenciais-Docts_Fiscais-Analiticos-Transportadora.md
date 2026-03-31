---
source: "MTZ-Report_Fiscal-Gerenciais-Docts_Fiscais-Analiticos-Transportadora.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal 

Doctos Fiscais - Analíticos - Transportadora


Localização: Menu Básicos, Módulo Report Fiscal, menu Gerenciais --> Documentos Fiscais --> Analíticos --> Transportadora


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3601
Melhoria no relatório

Melhoria no relatório com a inclusão dos campos CFOP e UF


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Descrição da Regra de Negócio 00
OSNNNN
RN01
Regra para inclusão da coluna CFOP:

Deve ser incluída a coluna CFOP no relatório acima.
Essa informação deve ser recuperada do campo 14 - COD_CFO, da SAFX07.
Essa nova coluna deve ficar entre a coluna Série/ Subsérie e Data de Emissão. Se houver necessidade, a coluna Série/ Subsérie pode sofre redução no seu tamanho.

OS3601

RN02

Regra para inclusão da coluna UF:

Deve ser incluída a coluna UF no relatório acima.
Essa informação deve ser recuperada do campo 19 - UF, da SAFX04.
Essa nova coluna deve ficar após a coluna Cliente.

OS3601


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

