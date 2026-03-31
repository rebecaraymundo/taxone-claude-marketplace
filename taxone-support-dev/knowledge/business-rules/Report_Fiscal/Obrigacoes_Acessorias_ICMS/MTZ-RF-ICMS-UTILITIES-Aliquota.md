---
source: "MTZ-RF-ICMS-UTILITIES-Aliquota.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Resumo do ICMS Utilities por Alíquota

Localização:
Módulo: Básicos --> Report Fiscal
Menu: Obrigações Acessórias --> ICMS --> Resumo do ICMS Utilities --> Por Alíquota

Obs.:A partir da OS3424-A1 este menu foi renomeado do "Resumos do ICMS TELECOM" para: "Resumos do ICMS Utilities".


DOCUMENTO DE REQUISITO

DR
Nome
Descrição

OS3424-A1


Alteração na regra do Parâmetro 84, conforme alteração do Decreto 57.177/2011


Alteração na regra do Parâmetro 84, conforme alteração do Decreto 57.177/2011


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Critério para geração - Parâmetro por UF: 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento:

Para Opção 01 Analítico e opção 02 Sintético:

Ao recuperar as notas da SAFX42, aplicar a regra descrita abaixo, que utiliza o parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento, criado na OS2768-F. Para obter o parâmetro, considerar: 

Campo 13 - COD_MODELO (SAFX42) = '6', UF Estabelecimento = SP, UF Destinatário = SP

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = S e campo 03 - DAT_FISCAL (SAFX42) tiver data até 31.12.2011, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42.

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = N, filtrar as notas normalmente pelo campo - 03-Data de Emissão/Escrita Fiscal, ou seja, esta data deve se enquadrar no período solicitado em tela para emissão do relatório (funcionamento original, antes da alteração);

SE campo 03 - DAT_FISCAL (SAFX42) tiver data a partir de 01.01.2012, a escrituração deve ser pela emissão, ou seja pelo campo 03(SAFX42).

Obs.: A UF Destinatário deve ser = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo, as cidades que se localizam em divisas entre estados.
Obs.: A regra acima deve ser válida para reprocessamento.
Obs: Quando houver notas que não se enquadrem nessas condições, o relatório deve ser gerado normalmente pela data de emissão.
Obs.: As notas fiscais de Utilities estiverem com o campo 21 - SITUACAO = 'S', ou seja, se a nota for regularmente cancelada, deve ser considerada na geração do relatório.
OS3424-A1
RN01


RN02


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

