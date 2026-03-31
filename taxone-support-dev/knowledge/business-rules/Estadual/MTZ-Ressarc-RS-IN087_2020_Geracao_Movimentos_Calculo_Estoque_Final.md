# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Estoque Final

> Fonte: MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Estoque Final.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Relatório de Conferência do Estoque Final



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração à IN-RE 087/20 à Geração dos Movimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Cálculo do Estoque Final:	1
3.	Recuperação dos Dados e Processamento	1
3.1 – Recuperação dos Movimentos de Entrada - C180	1
3.2 – Recuperação dos Movimentos de Saída - C185	1
3.3 – Recuperação dos Movimentos de Saída - C380	1
3.4 – Recuperação da Movimentação de Saída por Cupons Fiscais - C480	1
3.5 – Recuperação dos Movimentos de Devolução de Saídas - C181	1
3.6 – Recuperação dos Movimentos de Devolução de Entradas - C186	1
3.7 – Recuperação do Estoque Inicial – H010/H030	1
4.	RELATORIO DE CONFERÊNCIA	1


## Introdução


O objetivo desse documento é definir a geração do relatório de conferência do estoque final, que tem como base os registros H010/H030, C180, C181, C185, C186, C380 e C480.
Veja os registros gerados pelo processo de “Geração dos Movimentos”, suas tabelas específicas do módulo e as tabelas definitivas relacionadas as “SAFX”, base para geração dos registros do Sped Fiscal.





## Cálculo do Estoque Final:


O Estoque Final é calculado automaticamente pelo programa da GIA-RS, com base nos registros da EFD:

Estoque Final = Saldo Inicial H010/H030 + Entradas C180 + Devoluções de Saídas C181 – Saídas C185 – Saídas C380 – Saídas C480 – Devoluções das Entradas C186

Onde:
- Saldo Inicial do Registro H010/H030 = (Campo 04-QTD do H010 * Campo 02-VL_ICMS_OP) +
- (Campo 04-QTD do H010 * Campo 04-VL_ICMS_ST)
- Entradas do Registro C180 = (Campo 03-QTD_CONV * Campo 06-VL_UNIT_ICMS_OP_CONV) +
- (Campo 03-QTD_CONV * Campo 08-VL_UNIT_ICMS_ST_CONV)
- Devoluções de Saídas do Registro C181 = (Campo 03-QTD_CONV * Campo 13- VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA) +
- (Campo 03-QTD_CONV * Campo 14- VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA)
- Saídas do Registro C185 = (Campo 07-QTD_CONV * Campo 12- VL_UNIT_ICMS_OP_ESTOQUE_CONV) +
- (Campo 07-QTD_CONV * Campo 13- VL_UNIT_ICMS_ST_ESTOQUE_CONV)
- Saídas do Registro C380 = (Campo 03-QTD_CONV * Campo 08- VL_UNIT_ICMS_OP_ESTOQUE_CONV) +
- (Campo 03-QTD_CONV * Campo 09- VL_UNIT_ICMS_ST_ESTOQUE_CONV)
- Saídas do Registro C480 = (Campo 03-QTD_CONV * Campo 08- VL_UNIT_ICMS_OP_ESTOQUE_CONV) +
- (Campo 03-QTD_CONV * Campo 09- VL_UNIT_ICMS_ST_ESTOQUE_CONV)
- Devoluções das Entradas do Registro C186 = (Campo 07-QTD_CONV * Campo 16-VL_UNIT_ICMS_OP_CONV_ENTRADA) +
- (Campo 07-QTD_CONV * Campo 18-VL_UNIT_ICMS_ST_CONV_ENTRADA)


## Recuperação dos Dados e Processamento


A geração do relatório consiste na leitura das tabelas específicas da Geração do Movimento (EST_ST_RS_NF_ENT, EST_ST_RS_MEDIA_POND,...) de todos os produtos presentes nos movimentos (registros C180, C181, C185, C186, C380, C480) ou na média ponderada (H030), consolidação dos valores de ICMS e ICMS-ST por produto e cálculo do estoque final conforme fórmula apresentada no tópico anterior.

A definição da recuperação de cada registro está descrita a seguir.


### 3.1 – Recuperação dos Movimentos de Entrada - C180


Lê tabela EST_ST_RS_NF_ENT com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
Recuperar os campos que são demonstrados no Relatório de Conferência do C180:
- Qtde Conv (C180-03): QTD_CONV
- Vlr Unit ICMS Conv (C180-06): VLR_ICMS_CONV
- Vlr Unit ICMS-ST Conv (C180-08): VLR_UNIT_ICMSS_CONV_ENT

### 3.2 – Recuperação dos Movimentos de Saída - C185

Lê tabela EST_ST_RS_NF_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
- Código do Modelo da nota = 01, 1B, 04, 55, 65
Recuperar os campos que são demonstrados no Relatório de Conferência do C185:
- Qtde Conv (C185-07): QTD_CONV
- Vlr Unit ICMS Estoque Conv (C185-12): VLR_UNIT_ICMS_ESTQ_SAI
- Vlr Unit ICMS-ST Estoque Conv (C185-13): VLR_UNIT_ICMSS_ESTQ_SAI


### 3.3 – Recuperação dos Movimentos de Saída - C380

Lê tabela EST_ST_RS_NF_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
- Código do Modelo da nota = 02
Recuperar os campos que são demonstrados no Relatório de Conferência do C380:
- Qtde Conv (C380-03): QTD_CONV
- Vlr Unit ICMS Estoque Conv (C380-08): VLR_UNIT_ICMS_ESTQ_SAI
- Vlr Unit ICMS-ST Estoque Conv (C380-09): VLR_UNIT_ICMSS_ESTQ_SAI


### 3.4 – Recuperação da Movimentação de Saída por Cupons Fiscais - C480

Lê tabela EST_ST_RS_ECF com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração;
Recuperar os campos que são demonstrados no Relatório de Conferência do C480:
- Qtde Conv (C480-03): QTD_CONV
- Vlr Unit ICMS Estoque Conv (C480-08): VLR_UNIT_ICMS_ESTQ_CONV
- Vlr Unit ICMS-ST Estoque Conv (C480-09): VLR_UNIT_ICMSS_ESTQ_CONV


### 3.5 – Recuperação dos Movimentos de Devolução de Saídas - C181

Lê tabela EST_ST_RS_NF_DEV_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
Recuperar os campos que são demonstrados no Relatório de Conferência do C181:
- Qtde Conv (C181-03): QTD_CONV
- Vlr Unit ICMS Estoque Conv (C181-13): VLR_UNIT_ICMS_ESTQ_SAI
- Vlr Unit ICMS-ST Estoque Conv (C181-14): VLR_UNIT_ICMSS_ESTQ_SAI



### 3.6 – Recuperação dos Movimentos de Devolução de Entradas - C186

Lê tabela EST_ST_RS_NF_DEV_ENT com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
Recuperar os campos que são demonstrados no Relatório de Conferência do C186:
- Qtde Conv (C186-07): QTD_CONV
- Vlr Unit ICMS Conv (C186-16): VLR_ICMS_CONV
- Vlr Unit ICMS-ST Conv (C186-18): VLR_UNIT_ICMSS_CONV_ENT


### 3.7 – Recuperação do Estoque Inicial – H010/H030

Lê tabela EST_ST_RS_MEDIA_POND com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data = Primeiro dia do período informado na tela de geração
Recuperar os campos que são demonstrados na linha “(1) Saldo Inicial” do Relatório de Conferência da Média Ponderada:
- Valor ICMS: VLR_ICMS_INI_MP
- Valor ICMS-ST (c/ Fecep): VLR_ICMS_ST_INI_MP + VLR_FECEP_ST_INI_MP


## RELATORIO DE CONFERÊNCIA


Gerar o relatório em arquivo excel.
Nome do arquivo: Relatório_Conferencia_Estoque_Final_mm_aaaa_cod_estab.xlsx

Campos do Relatorio




= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS602575 | Liliane Videira Assaf | Criação do Relatório de Conferência do Estoque Final. | 20/05/2024 |
|  |  |  |  |
|  |  |  |  |


| Tabelas Específicas da Geração do Movimento | Tabelas definitivas relacionadas as SAFX | Registro do SPED FISCAL |
| --- | --- | --- |
| EST_ST_RS_NF_ENT | x296_info_compl_st_itens_merc | C180 |
| EST_ST_RS_NF_DEV_ENT | X308_INFO_COMPL_ST_IT_MERC_DEV | C186 |
| EST_ST_RS_NF_DEV_SAI | X308_INFO_COMPL_ST_IT_MERC_DEV | C181 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C185 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C380 |
| EST_ST_RS_ECF | X297_INF_COMP_ST_CUPOM_ECF | C480 |
| EST_ST_RS_MEDIA_POND | X52_INVENT_PRODUTO | H010/H030 |
|  |  |  |


|  |
| --- |


| Campos | Regra de Preenchimento |
| --- | --- |
| Cod Empresa |  |
| Cod Estab |  |
| Mês/Ano |  |
| Ind-Cod Produto | Produtos recuperados conforme tópicos 3.1 ao 3.7 |
| Saldo Inicial - Valor ICMS | Valor ICMS recuperado conforme tópico 3.7 |
| Saldo Inicial - Valor ICMS-ST | Valor ICMS-ST recuperado conforme tópico 3.7 |
| C180 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.1 |
| C180 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.1 |
| C181 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.5 |
| C181 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.5 |
| C185 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.2 |
| C185 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.2 |
| C380 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.3 |
| C380 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.3 |
| C480 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.4 |
| C480 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.4 |
| C186 - Valor ICMS | qtde x vlr unit ICMS recuperados conforme tópico 3.6 |
| C186 - Valor ICMS-ST | qtde x vlr unit ST recuperados conforme tópico 3.6 |
| Estoque Final (Valor ICMS + Valor ICMS-ST) | Saldo Inicial (ICMS) + Saldo Inicial (ICMS-ST) + C180 (ICMS) + C180 (ICMS-ST) + C181 (ICMS) + C181 (ICMS-ST) - C185 (ICMS) - C185 (ICMS-ST) - C380 (ICMS) - C380 (ICMS-ST) - C480 (ICMS) - C480 (ICMS-ST) - C186 (ICMS) – C186 (ICMS-ST) |
