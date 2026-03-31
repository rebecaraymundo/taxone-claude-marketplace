---
source: "MTZ-Report_Fiscal-ICMS-UTILITIES-Aliquota.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Resumo do ICMS Utilities por Alíquota

Localização:
Módulo: Básicos --> Report Fiscal
Menu: Obrigações Acessórias --> ICMS --> Resumo do ICMS Utilities --> Por Alíquota

Obs.:A partir da OS2768-K (25/07/2011) este menu foi renomeado do "Resumos do ICMS TELECOM" para: "Resumos do ICMS Utilities".


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2768-K
Alteração dos relatórios de Utilities para buscar o parâmetro "Escritura NF's EE (Modelo 06) pela Data de Vencimento"
Alteração dos relatórios de Utilities para buscar o parâmetro "Escritura NF's EE (Modelo 06) pela Data de Vencimento".


OS3424-A


Alteração na regra do Parâmetro 84, conforme alteração do Decreto 57.177/2011


Alteração na regra do Parâmetro 84, conforme alteração do Decreto 57.177/2011


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Ao recuperar as notas da SAFX42, aplicar a regra descrita abaixo, que utiliza o parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento, criado na OS2768-F. Para obter o parâmetro, considerar: 

Campo 13 - COD_MODELO (SAFX42) = '6', UF Estabelecimento = SP, UF Destinatário = SP

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = S e campo 03 - DAT_FISCAL (SAFX42) tiver data até 31.12.2011 e o campo 32 - DAT_VENCTO (SAFX 42) tiver data a partir de 01.02.2012, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42.

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = N, filtrar as notas normalmente pelo campo - 03-Data de Emissão/Escrita Fiscal, ou seja, esta data deve se enquadrar no período solicitado em tela para emissão do relatório (funcionamento original, antes da alteração);

SE campo 03 - DAT_FISCAL (SAFX42) tiver data a partir de 01.01.2012, a escrituração deve ser pela emissão, ou seja pelo campo 03(SAFX42).

Obs.: A UF Destinatário deve ser = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo, as cidades que se localizam em divisas entre estados.
OS3424-A
RN01
Opção 01: Analítico

Critério para geração - Parâmetro por UF: 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento:

Buscar a configuração do parâmetro conforme localização abaixo:

Módulo: Estadual -->  ICMS
Menu: Manutenção --> Parâmetros por UF
Parâmetro: 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento

Se estiver habilitado, então acrescentar como critério para geração do Resumo do ICMS Utilities por Alíquota - Analítico a regra do parâmetro. 


OS2768-K
RN02
Opção 02: Sintético

Critério para geração - Parâmetro por UF: 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento:

Buscar a configuração do parâmetro conforme localização abaixo:

Módulo: Estadual -->  ICMS
Menu: Manutenção --> Parâmetros por UF
Parâmetro: 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento

Se estiver habilitado, então acrescentar como critério para geração do Resumo do ICMS Utilities por Alíquota - Sintético a regra do parâmetro. 

OS2768-K


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

