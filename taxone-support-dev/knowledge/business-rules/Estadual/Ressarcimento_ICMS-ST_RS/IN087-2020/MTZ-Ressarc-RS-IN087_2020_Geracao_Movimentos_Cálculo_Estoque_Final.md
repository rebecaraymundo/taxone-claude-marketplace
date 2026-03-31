# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Estoque Final

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Estoque Final.docx
- **Modificado:** 2024-05-20
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Relatório de Conferência do Estoque Final 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração à IN\-RE 087/20 à Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS602575__

Liliane Videira Assaf

Criação do Relatório de Conferência do Estoque Final\.

20/05/2024 

Sumário

[1\.	Introdução	1](#_Toc167131855)

[2\.	Cálculo do Estoque Final:	1](#_Toc167131856)

[3\.	Recuperação dos Dados e Processamento	1](#_Toc167131857)

[3\.1 – Recuperação dos Movimentos de Entrada \- C180	1](#_Toc167131858)

[3\.2 – Recuperação dos Movimentos de Saída \- C185	1](#_Toc167131859)

[3\.3 – Recuperação dos Movimentos de Saída \- C380	1](#_Toc167131860)

[3\.4 – Recuperação da Movimentação de Saída por Cupons Fiscais \- C480	1](#_Toc167131861)

[3\.5 – Recuperação dos Movimentos de Devolução de Saídas \- C181	1](#_Toc167131862)

[3\.6 – Recuperação dos Movimentos de Devolução de Entradas \- C186	1](#_Toc167131863)

[3\.7 – Recuperação do Estoque Inicial – H010/H030	1](#_Toc167131864)

[4\.	RELATORIO DE CONFERÊNCIA	1](#_Toc167131865)

# <a id="_Toc167131855"></a>Introdução 

O objetivo desse documento é definir a geração do relatório de conferência do estoque final, que tem como base os registros H010/H030, C180, C181, C185, C186, C380 e C480\.

Veja os registros gerados pelo processo de “Geração dos Movimentos”, suas tabelas específicas do módulo e as tabelas definitivas relacionadas as “SAFX”, base para geração dos registros do Sped Fiscal\. 

__Tabelas Específicas da Geração do Movimento__

__Tabelas definitivas relacionadas as SAFX__

__Registro do SPED FISCAL__

EST\_ST\_RS\_NF\_ENT

x296\_info\_compl\_st\_itens\_merc

C180

EST\_ST\_RS\_NF\_DEV\_ENT

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C186

EST\_ST\_RS\_NF\_DEV\_SAI

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C181

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C185

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C380

EST\_ST\_RS\_ECF

X297\_INF\_COMP\_ST\_CUPOM\_ECF

C480

EST\_ST\_RS\_MEDIA\_POND

X52\_INVENT\_PRODUTO

H010/H030

# <a id="_Toc167131856"></a>Cálculo do Estoque Final: 

O Estoque Final é calculado automaticamente pelo programa da GIA\-RS, com base nos registros da EFD:

Estoque Final = Saldo Inicial H010/H030 \+ Entradas C180 \+ Devoluções de Saídas C181 – Saídas C185 – Saídas C380 – Saídas C480 – Devoluções das Entradas C186

Onde:

- Saldo Inicial do Registro H010/H030 = \(Campo 04\-QTD do H010 \* Campo 02\-VL\_ICMS\_OP\) \+

                                                    \(Campo 04\-QTD do H010 \* Campo 04\-VL\_ICMS\_ST\)

- Entradas do Registro C180 = \(Campo 03\-QTD\_CONV \* Campo 06\-VL\_UNIT\_ICMS\_OP\_CONV\) \+

                                     \(Campo 03\-QTD\_CONV \* Campo 08\-VL\_UNIT\_ICMS\_ST\_CONV\)

- Devoluções de Saídas do Registro C181 = \(Campo 03\-QTD\_CONV \* Campo 13\- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA\) \+

                                                           \(Campo 03\-QTD\_CONV \* Campo 14\- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA\)

- Saídas do Registro C185 = \(Campo 07\-QTD\_CONV \* Campo 12\- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\) \+ 

                                  \(Campo 07\-QTD\_CONV \* Campo 13\- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\)

- Saídas do Registro C380 = \(Campo 03\-QTD\_CONV \* Campo 08\- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\) \+ 

                                  \(Campo 03\-QTD\_CONV \* Campo 09\- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\)

- Saídas do Registro C480 = \(Campo 03\-QTD\_CONV \* Campo 08\- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\) \+ 

                                  \(Campo 03\-QTD\_CONV \* Campo 09\- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\)

- Devoluções das Entradas do Registro C186 = \(Campo 07\-QTD\_CONV \* Campo 16\-VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA\) \+

                                                                \(Campo 07\-QTD\_CONV \* Campo 18\-VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA\)

# <a id="_Toc350763252"></a><a id="_Toc167131857"></a>Recuperação dos Dados e Processamento

<a id="_2.1_–_Recuperação"></a>A geração do relatório consiste na leitura das tabelas específicas da Geração do Movimento \(EST\_ST\_RS\_NF\_ENT, EST\_ST\_RS\_MEDIA\_POND,\.\.\.\) de todos os produtos presentes nos movimentos \(registros C180, C181, C185, C186, C380, C480\) ou na média ponderada \(H030\), consolidação dos valores de ICMS e ICMS\-ST por produto e cálculo do estoque final conforme fórmula apresentada no tópico anterior\.

A definição da recuperação de cada registro está descrita a seguir\.

## <a id="_Toc167131858"></a>3\.1 – Recuperação dos Movimentos de Entrada \- C180

Lê tabela EST\_ST\_RS\_NF\_ENT com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Recuperar os campos que são demonstrados no Relatório de Conferência do C180:

\- Qtde Conv \(C180\-03\): QTD\_CONV

\- Vlr Unit ICMS Conv \(C180\-06\): VLR\_ICMS\_CONV

\- Vlr Unit ICMS\-ST Conv \(C180\-08\): VLR\_UNIT\_ICMSS\_CONV\_ENT

## <a id="_Toc167131859"></a>3\.2 – Recuperação dos Movimentos de Saída \- C185

Lê tabela EST\_ST\_RS\_NF\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

\- Código do Modelo da nota = 01, 1B, 04, 55, 65

<a id="_Hlk167130066"></a>Recuperar os campos que são demonstrados no Relatório de Conferência do C185:

\- Qtde Conv \(C185\-07\): QTD\_CONV

\- Vlr Unit ICMS Estoque Conv \(C185\-12\): VLR\_UNIT\_ICMS\_ESTQ\_SAI

\- Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\): VLR\_UNIT\_ICMSS\_ESTQ\_SAI

## <a id="_Toc167131860"></a>3\.3 – Recuperação dos Movimentos de Saída \- C380

Lê tabela EST\_ST\_RS\_NF\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

\- Código do Modelo da nota = 02

Recuperar os campos que são demonstrados no Relatório de Conferência do C380:

\- Qtde Conv \(C380\-03\): QTD\_CONV

\- Vlr Unit ICMS Estoque Conv \(C380\-08\): VLR\_UNIT\_ICMS\_ESTQ\_SAI

\- Vlr Unit ICMS\-ST Estoque Conv \(C380\-09\): VLR\_UNIT\_ICMSS\_ESTQ\_SAI

## <a id="_2.2_–_Recuperação"></a><a id="_Toc167131861"></a>3\.4 – Recuperação da Movimentação de Saída por Cupons Fiscais \- C480 

Lê tabela EST\_ST\_RS\_ECF com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração;

Recuperar os campos que são demonstrados no Relatório de Conferência do C480:

\- Qtde Conv \(C480\-03\): QTD\_CONV

\- Vlr Unit ICMS Estoque Conv \(C480\-08\): VLR\_UNIT\_ICMS\_ESTQ\_CONV

\- Vlr Unit ICMS\-ST Estoque Conv \(C480\-09\): VLR\_UNIT\_ICMSS\_ESTQ\_CONV 

## <a id="_Toc167131862"></a>3\.5 – Recuperação dos Movimentos de Devolução de Saídas \- C181

Lê tabela EST\_ST\_RS\_NF\_DEV\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Recuperar os campos que são demonstrados no Relatório de Conferência do C181:

\- Qtde Conv \(C181\-03\): QTD\_CONV

\- Vlr Unit ICMS Estoque Conv \(C181\-13\): VLR\_UNIT\_ICMS\_ESTQ\_SAI

\- Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\): VLR\_UNIT\_ICMSS\_ESTQ\_SAI

## <a id="_Toc167131863"></a>3\.6 – Recuperação dos Movimentos de Devolução de Entradas \- C186

Lê tabela EST\_ST\_RS\_NF\_DEV\_ENT com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Recuperar os campos que são demonstrados no Relatório de Conferência do C186:

\- Qtde Conv \(C186\-07\): QTD\_CONV

\- Vlr Unit ICMS Conv \(C186\-16\): VLR\_ICMS\_CONV

\- Vlr Unit ICMS\-ST Conv \(C186\-18\): VLR\_UNIT\_ICMSS\_CONV\_ENT

## <a id="_Toc167131864"></a>3\.7 – Recuperação do Estoque Inicial – H010/H030

Lê tabela EST\_ST\_RS\_MEDIA\_POND com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data = __Primeiro dia__ do período informado na tela de geração

Recuperar os campos que são demonstrados na linha “\(1\) Saldo Inicial” do Relatório de Conferência da Média Ponderada:

\- Valor ICMS: VLR\_ICMS\_INI\_MP

\- Valor ICMS\-ST \(c/ Fecep\): VLR\_ICMS\_ST\_INI\_MP \+ VLR\_FECEP\_ST\_INI\_MP

# <a id="_Toc59988570"></a><a id="_Toc167131865"></a>RELATORIO DE CONFERÊNCIA

Gerar o relatório em arquivo excel\.

Nome do arquivo: Relatório\_Conferencia\_Estoque\_Final\_mm\_aaaa\_cod\_estab\.xlsx

__Campos do Relatorio__

Campos

Regra de Preenchimento

Cod Empresa

Cod Estab

Mês/Ano

Ind\-Cod Produto

Produtos recuperados conforme tópicos 3\.1 ao 3\.7

Saldo Inicial \- Valor ICMS

Valor ICMS recuperado conforme tópico 3\.7

Saldo Inicial \- Valor ICMS\-ST

Valor ICMS\-ST recuperado conforme tópico 3\.7

C180 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.1

C180 \- Valor ICMS\-ST

qtde x vlr unit ST recuperados conforme tópico 3\.1

C181 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.5

C181 \- Valor ICMS\-ST

 qtde x vlr unit ST recuperados conforme tópico 3\.5

C185 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.2

C185 \- Valor ICMS\-ST

qtde x vlr unit ST recuperados conforme tópico 3\.2

C380 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.3

C380 \- Valor ICMS\-ST

qtde x vlr unit ST recuperados conforme tópico 3\.3

C480 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.4

C480 \- Valor ICMS\-ST

qtde x vlr unit ST recuperados conforme tópico 3\.4

C186 \- Valor ICMS

qtde x vlr unit ICMS recuperados conforme tópico 3\.6

C186 \- Valor ICMS\-ST

qtde x vlr unit ST recuperados conforme tópico 3\.6

Estoque Final \(Valor ICMS \+ Valor ICMS\-ST\)

Saldo Inicial \(ICMS\) \+ Saldo Inicial \(ICMS\-ST\) \+

C180 \(ICMS\) \+ C180 \(ICMS\-ST\) \+

C181 \(ICMS\) \+ C181 \(ICMS\-ST\) \-

C185 \(ICMS\) \- C185 \(ICMS\-ST\) \-

C380 \(ICMS\) \- C380 \(ICMS\-ST\) \-

C480 \(ICMS\) \- C480 \(ICMS\-ST\) \-

C186 \(ICMS\) – C186 \(ICMS\-ST\)

= = = = = =

 

