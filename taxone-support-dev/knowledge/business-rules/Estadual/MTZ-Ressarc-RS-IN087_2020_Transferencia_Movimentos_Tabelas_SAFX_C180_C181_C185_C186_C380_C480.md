# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Tabelas SAFX_C180_C181_C185_C186_C380_C480

> Fonte: MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Tabelas SAFX_C180_C181_C185_C186_C380_C480.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Atualização das Tabelas SAFX (C180, C181, C185, C186, C380, C480)



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018),
itens: Geração  IN-RE 087/20  Transferência dos Movimentos para EFD Fiscal



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Limpeza das tabelas definitivas relacionadas as SAFX	1
3.	Recuperação dos Dados e Processamento	1
3.1 – Recuperação dos Movimentos de Entrada e Gravação do C180	1
3.2 – Recuperação dos Movimentos de Saída e Gravação do C185	1
3.3 – Recuperação dos Movimentos de Saída e Gravação do C380	1
3.4 – Recuperação da Movimentação de Saída por Cupons Fiscais e Gravação do C480	1
3.5 – Recuperação dos Movimentos de Devolução de Saídas e Gravação do C181	1
3.6 – Recuperação dos Movimentos de Devolução de Entradas e Gravação do C186	1


## Introdução


O objetivo desse documento é definir a geração dos registros C180, C181, C185, C186, C380 e C480.
Nessa rotina os registros gerados pelo processo de “Geração dos Movimentos” nas tabelas específicas do módulo são lidos e gravados nas tabelas definitivas relacionadas as “SAFX”, base para geração dos registros do Sped Fiscal.





## Limpeza das tabelas definitivas relacionadas as SAFX


No início do processamento é necessário excluir os registros das tabelas x296_info_compl_st_itens_merc, X308_INFO_COMPL_ST_IT_MERC_DEV, [MFS65137] X297_INF_COMP_ST_CUPOM_ECF com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
- Ind_gravação = '0', '6','7','8'.


Sobre o campo IND_GRAVAÇÃO:
O ind_gravação informa a origem do registro nas tabelas definitivas (X) que possuem importação por SAFX.

IND_GRAVACAO:
Valores padrão do campo (tabelas de importação ):
1.  Incluído por Importação
2.  Atualizado por Importação
3.  Incluído por Importação / Atualizado por Digitação
4.  Incluído por Digitação
5.  Incluído por Digitação / Atualizado por Digitação
6.  Gerado pelo Sistema
7.  Gerado pelo Sistema  / Atualizado por Digitação
8. Gerado pelo Sistema  / Atualizado por Importação
O valor 8 foi criado na OS2388-AA, A4, e somente é considerado nas importações das SAFX112 e SAFX113.
9. Atualizado pelo Sistema


## Recuperação dos Dados e Processamento


### 3.1 – Recuperação dos Movimentos de Entrada e Gravação do C180


Lê tabela EST_ST_RS_NF_ENT com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração

Gravar a tabela x296_info_compl_st_itens_merc com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela x296_info_compl_st_itens_merc (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C180: Registro de Movimento de Entrada, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C180 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.


### 3.2 – Recuperação dos Movimentos de Saída e Gravação do C185

Lê tabela EST_ST_RS_NF_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
- Código do Modelo da nota = 01, 1B, 04, 55, 65

Gravar a tabela x296_info_compl_st_itens_merc com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela x296_info_compl_st_itens_merc (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C185: Registro de Movimento de Saída, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C185 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.


### 3.3 – Recuperação dos Movimentos de Saída e Gravação do C380

Lê tabela EST_ST_RS_NF_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração
- Código do Modelo da nota = 02

Gravar a tabela x296_info_compl_st_itens_merc com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela x296_info_compl_st_itens_merc (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C380: Registro de Movimento de Saída, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C380 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.

[MFS65137]
### 3.4 – Recuperação da Movimentação de Saída por Cupons Fiscais e Gravação do C480

Lê tabela EST_ST_RS_ECF com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração;

Gravar a tabela X297_INF_COMP_ST_CUPOM_ECF com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela X297_INF_COMP_ST_CUPOM_ECF (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C480: Registro de Movimento de Cupom Fiscal, incluído via importação/manutenção da SAFX297, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C480 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.


### 3.5 – Recuperação dos Movimentos de Devolução de Saídas e Gravação do C181

Lê tabela EST_ST_RS_NF_DEV_SAI com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração

Gravar a tabela X308_INFO_COMPL_ST_IT_MERC_DEV com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela x296_info_compl_st_itens_merc (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C181: Registro de Movimento de Devolução de Saída, incluído via importação/manutenção da SAFX308, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C181 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”..


### 3.6 – Recuperação dos Movimentos de Devolução de Entradas e Gravação do C186

Lê tabela EST_ST_RS_NF_DEV_ENT com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data compreendida no período informado na tela de geração

Gravar a tabela X308_INFO_COMPL_ST_IT_MERC_DEV com IND_GRAVACAO = ‘6’;
Caso registro já exista na tabela x296_info_compl_st_itens_merc (caso que foi incluído via digitação ou importação) então:
Gravar a seguinte mensagem de aviso no log:
“Registro C186: Registro de Movimento de Devolução de Entrada, incluído via importação/manutenção da SAFX308, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados.”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros lidos, incluídos e atualizados para o C186 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.



= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS48753 | Liliane Videira Assaf | Criação da funcionalidade. Não estamos considerando Cupom Fiscal nesta entrega. | 22/12/2020 |
| MFS65137 | Liliane Videira Assaf | Tratamento dos Cupom Fiscal (Mod. 02, 2D e 60) para geração do registro C480 do Sped Fiscal. Os cupons devem ser lidos da tabela EST_ST_RS_ECF e gravados na tabela X297_INF_COMP_ST_CUPOM_ECF, de onde o registro C480 é gerado no Sped Fiscal. | 13/05/2021 |
|  |  |  |  |


| Tabelas Específicas da Geração do Movimento | Tabelas definitivas relacionadas as SAFX | Registro do SPED FISCAL |
| --- | --- | --- |
| EST_ST_RS_NF_ENT | x296_info_compl_st_itens_merc | C180 |
| EST_ST_RS_NF_DEV_ENT | X308_INFO_COMPL_ST_IT_MERC_DEV | C186 |
| EST_ST_RS_NF_DEV_SAI | X308_INFO_COMPL_ST_IT_MERC_DEV | C181 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C185 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C380 |
| EST_ST_RS_ECF | X297_INF_COMP_ST_CUPOM_ECF | C480 [MFS65137] |
|  |  |  |
|  |  |  |
