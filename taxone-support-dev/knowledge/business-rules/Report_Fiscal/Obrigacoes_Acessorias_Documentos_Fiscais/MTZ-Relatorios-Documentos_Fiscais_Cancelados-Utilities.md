---
source: "MTZ-Relatorios-Documentos_Fiscais_Cancelados-Utilities.doc"
category: Report_Fiscal
converted: auto
---

RF - Documentos Fiscais Cancelados - Utilities

Módulo RF,  menu Obrigações Acessórias --> Documentos Fiscais --> Documentos Fiscais Cancelados - Utilities


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2768-J
Relatório de Documentos Fiscais Cancelados - Utilities 
A OS2768-J alterou este relatório para mudança na descrição e título do relatório, para trocar o termo "Telecom" por "Utilities", e também para algumas alterações no layout a na forma de seleção das notas. Foram incluídas as colunas de valor (valor total, base ICMS e valor ICMS) e a data de vencimento. A seleção das notas na SAFX42 passou a trabalhar com o parâmetro "Escritura NF's EE (Modelo 06) pela Data de Vencimento", filtrando as notas fiscais de modelo 06 por vencimento.
MFS15157
Relatório de Documentos Fiscais Cancelados - Utilities 
Essa alteração tem como objetivo realizar o tratamento para desconsiderar os valores nos campos Base ICMS e Valor ICMS dos itens do documento fiscal que possuírem o indicador desconto no campo "Adição/Desconto".


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
 
MFS-15157 Regra para Inclusão de Parâmetro:

Inclusão do Checkbox "Deduzir descontos nos itens das notas fiscais ". 

A seguir a tela em que o parâmetro será incluído:
Módulo Básicos ? Report Fiscal
Obrigações Acessórias ? Documentos Fiscais > Documentos Fiscais Cancelados Utilities

Regras do Parâmetro:
Por default o campo estará desmarcado.

Regras para Geração do Relatório:
Se o parâmetro "Deduzir descontos nos itens das notas fiscais " for marcado na tela de parametrização do relatório, o sistema deverá verificar os itens do documento fiscal que possuem o campo 20 - IND_ADIC_DESC da SAFX43 = 'D' E deduzir o valor contido destes itens nos campos 23 - VLR_BASE_ICMS_1 e VLR_TRIB_ICMS.

Se não, manter a regra atual de geração do relatório que soma os itens do documento fiscal.

OS2768-J
MFS-15157
RN02
Campo Valor Total: Preencher com o conteúdo do campo "17-Valor Total do Documento Fiscal" da SAFX42
OS2768-J
RN03
Campo Base ICMS: Preencher com o valor total da base de cálculo do ICMS dos itens da nota. Para isso, totalizar ou deduzir (vide RN01) os itens pelo campo "23-Base Tributada" da SAFX43. 
OS2768-J
MFS-15157
RN04
Campo Valor ICMS: Preencher com o valor total do ICMS dos itens da nota. Para isso, totalizar ou deduzir (vide RN01) os itens pelo campo "22-Valor ICMS" da SAFX43.
OS2768-J
MFS-15157
RN05
Campo Data Vencimento: Preencher com a data de vencimento (campo 32-Data de Vencimento da SAFX42)
OS2768-J

