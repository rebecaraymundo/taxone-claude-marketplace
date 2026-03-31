---
source: "MTZ-RF-Documentos_Fiscais_Cancelados-Utilities.doc"
category: Report_Fiscal
converted: auto
---

RF - Documentos Fiscais Cancelados - Utilities

Localização: Módulo ? RF
                    Menu ? Obrigações Acessórias --> Documentos Fiscais --> Documentos Fiscais Cancelados - Utilities


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2768-J/ OS3424-A
Relatório de Documentos Fiscais Cancelados - Utilities 
A OS2768-J alterou este relatório para mudança na descrição e título do relatório, para trocar o termo "Telecom" por "Utilities", e também para algumas alterações no layout a na forma de seleção das notas. Foram incluídas as colunas de valor (valor total, base ICMS e valor ICMS) e a data de vencimento. A seleção das notas na SAFX42 passou a trabalhar com o parâmetro "Escritura NF's EE (Modelo 06) pela Data de Vencimento", filtrando as notas fiscais de modelo 06 por vencimento.

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN01
Regra de Recuperação das Notas Fiscais:
 
Ao recuperar as notas da SAFX42, aplicar a regra descrita abaixo, que utiliza o parâmetro "Escritura NF's EE (Modelo 06) pela Data de Vencimento",  criado na OS2768-F. Para obter o parâmetro, considerar a UF do Estabelecimento.

Se  modelo (campo 13)  =  06  e  parâmetro  "Escritura NF's EE (Modelo 06) pela Data de Vencimento"   =  S    
       Filtrar as notas pelo campo "32-Data de Vencimento", ou seja, a data do vencimento deve
       se enquadrar no período solicitado em tela para emissão do relatório;  
Senão
       Filtrar as notas normalmente pelo campo "03-Data de Emissão/Escrita Fiscal", ou seja,  esta data deve se
       enquadrar no período solicitado em tela para emissão do relatório (funcionamento original, antes da alteração);

[ALTERADA - OS3424-A] 
Ao recuperar as notas da SAFX42, aplicar a regra descrita abaixo, que utiliza o parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento, criado na OS2768-F. Para obter o parâmetro, considerar: 

Campo 13 - COD_MODELO (SAFX42) = '6', UF Estabelecimento = SP, UF Destinatário = SP

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = S e campo 03 - DAT_FISCAL (SAFX42) tiver data até 31.12.2011, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42.

Se parâmetro 84 - Escritura NF's EE (Modelo 06) pela Data de Vencimento = N, filtrar as notas normalmente pelo campo - 03-Data de Emissão/Escrita Fiscal, ou seja, esta data deve se enquadrar no período solicitado em tela para emissão do relatório (funcionamento original, antes da alteração);

SE campo 03 - DAT_FISCAL (SAFX42) tiver data a partir de 01.01.2012, a escrituração deve ser pela emissão, ou seja pelo campo 03(SAFX42).

Obs.: A UF Destinatário deve ser = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo, as cidades que se localizam em divisas entre estados.
Obs.: A regra acima deve ser válida para reprocessamento.

OS2768-J/ OS3424-A
RN02
Campo Valor Total: Preencher com o conteúdo do campo "17-Valor Total do Documento Fiscal" da SAFX42
OS2768-J
RN03
Campo Base ICMS: Preencher com o valor total da base de cálculo do ICMS dos itens da nota. Para isso, totalizar os itens pelo campo "23-Base Tributada" da SAFX43. 
OS2768-J
RN04
Campo Valor ICMS: Preencher com o valor total do ICMS dos itens da nota. Para isso, totalizar os itens pelo campo "22-Valor ICMS" da SAFX43.
OS2768-J
RN05
Campo Data Vencimento: Preencher com a data de vencimento (campo 32-Data de Vencimento da SAFX42)
OS2768-J

