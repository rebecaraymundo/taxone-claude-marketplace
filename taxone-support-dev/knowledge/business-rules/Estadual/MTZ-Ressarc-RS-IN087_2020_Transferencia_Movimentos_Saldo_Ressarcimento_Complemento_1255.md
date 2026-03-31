# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255

> Fonte: MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Geração do Saldo Consolidado de Ressarcimento e Complementação (1255)



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018),
itens: Geração  IN-RE 087/20  Transferência dos Movimentos para EFD Fiscal



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Limpeza da tabela de Saldo Consolidado da Restituição/Complemento - X304_SALDO_CONS_RES_COMP_ICMS	1
3.	Recuperação dos Dados e Processamento	1
3.1 – Recuperação da Movimentação de Saída por Nota (C185, C380)	1
3.2 – Recuperação da Movimentação de Saída por Cupons Fiscais (C480)	1
3.3 – Recuperação da Movimentação de Saída por Cupons Fiscais Eletrônicos (C815)	1
3.4 – Recuperação da Movimentação de Saída Venda a Consumidor (C330)	1
3.5 – Recuperação da Movimentação do Equipamento ECF (C430)	1
3.6 – Recuperação da Movimentação do Equipamento SAT-CF-E (C880)	1
3.7– Recuperação a Movimentação de Devolução de Saída (C181)	1
4.	Gravação dos Dados na Tabela de Saldo Consolidado da Restituição/Complemento - X304_SALDO_CONS_RES_COMP_ICMS	1
5.	RELATORIO DE CONFERÊNCIA	1


## Introdução


Esse documento tem como objetivo definir a geração do registro 1255 – Saldo Consolidado do Ressarcimento Complementação por Motivo que consiste em:
- Recuperar os valores de ressarcimento e complementação das movimentaçoes do período, oriundos das seguintes tabelas:
- x296_info_compl_st_itens_merc – Movimentos de Saídas (C185, C380);
- x297_inf_comp_st_cupom_ecf – Movimento de Cupons Fiscais (C480) [MFS65137]
- x298_info_comp_st_it_cupom_cfe (C815)
- X299_INF_COMP_ST_RES_MOD_02 (C330)
- x302_inf_comp_st_res_it_ecf (C430)
- x303_inf_comp_st_res_cupom_cfe (C880)
- X308_INFO_COMPL_ST_IT_MERC_DEV – Movimentos de Devolução de Saídas (C181);

- Totalizar os valores por Código de Motivo da Restituição/Complemento
- Gravar o registro resultante da consolidação por Código de Motivo da Restituição/Complementação, na tabela de Saldo Consolidado da Restituição/Complemento - X304_SALDO_CONS_RES_COMP_ICMS, base para geração do registro 1255 no Sped Fiscal.

Sobre os registros C330, C430, C815 e C880:
Hoje a funcionalidade de Geração dos Movimentos do Ressarcimento RS não gera os registros C330, C430, C815 e C880 pois as instruções normativas 087/20 e 096/20 não estabelecem regras para utilização dos mesmos.
Mesmo assim, nada impede do cliente gerar tais registros no Sped Fiscal, através da importação das SAFX298, SAFX299, SAFX302, SAFX303.  Por isso é necessário considerá-los na geração do registro 1255, para obtermos um arquivo do Sped Fiscal consistente.
O Guia Prático esclarece que os valores de ressarcimento e complemento são totalizações dos valores oriundos os registros C181, C185, C330, C380, C430, C480, C815 e C880.Veja:
“Campo 04 (VL_ICMS_ST_REST_MOT) – Validação: o valor informado no campo deve corresponder à soma dos campos VL_UNIT_ICMS_ST_CONV_REST multiplicados pelo campo QUANT_CONV dos registros C181, C185, C330, C380, C430, C480, C815 e C880 para cada código informado no campo COD_MOT_REST_COMPL”


## Limpeza da tabela de Saldo Consolidado da Restituição/Complemento - X304_SALDO_CONS_RES_COMP_ICMS


No início do processamento é necessário excluir os registros da tabela x304_saldo_cons_res_comp_icms com os seguintes critérios:
- Empresa = de login do Manager
- Estab = selecionado na tela de geração;
- Data Apuração compreendida no período informado na tela de geração
- Ind_gravação = '0', '6','7','8'.



## Recuperação dos Dados e Processamento


### 3.1 – Recuperação da Movimentação de Saída por Nota (C185, C380)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C180, C185 e C380) - x296_info_compl_st_itens_merc


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Fiscal – data enquadrada no período informado em tela;

- Nota de saída (MOVTO_E_S = “9”);

Recuperar os campos:
- 24-Código Motivo (Saídas) (COD_MOTIVO_SAI)
- 16-Quantidade Convertida (QTD_CONV)
- 29- Valor Unitário ICMS-ST Conv. Rest. (Saídas) (VLR_UNIT_ICMSS_REST_SAI)
- 30- Valor Unitário FCP-ST Conv. Rest. (Saídas)  (VLR_UNIT_FCP_REST_SAI)
- 31-Valor Unitário ICMS-ST Conv. Compl. (Saídas) (VLR_UNIT_ICMSS_COMPL_SAI)
- 32-Valor Unitário FCP-ST Conv. Compl. (Saídas) (VLR_UNIT_FCP_COMPL_SAI)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST) = VLR_UNIT_ICMSS_REST_SAI x QTD_CONV
- Valor do FCP-ST  Restituição (VLR_FCP_ST_REST) =  VLR_UNIT_FCP_REST_SAI x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_SAI x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP) = VLR_UNIT_FCP_COMPL_SAI x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


[MFS65137]
### 3.2 – Recuperação da Movimentação de Saída por Cupons Fiscais (C480)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C480) - x297_inf_comp_st_cupom_ecf


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Emissão – data enquadrada no período informado em tela;

Recuperar os campos:
- 9-Código do Motivo (COD_MOTIVO)
- 10-Quantidade Convertida (QTD_CONV)
- 18- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 19- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 20-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 21-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


### 3.3 – Recuperação da Movimentação de Saída por Cupons Fiscais Eletrônicos (C815)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C815) - x298_info_comp_st_it_cupom_cfe


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Emissão – data enquadrada no período informado em tela;

Recuperar os campos:
- 7-Código do Motivo (COD_MOTIVO_SAI)
- 8-Quantidade Convertida (QTD_CONV)
- 16- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 17- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 18-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 19-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST  Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV
[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


### 3.4 – Recuperação da Movimentação de Saída Venda a Consumidor (C330)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C330) - X299_INF_COMP_ST_RES_MOD_02


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Emissão – data enquadrada no período informado em tela;

Recuperar os campos:
- 14-Código do Motivo (COD_MOTIVO)
- 15-Quantidade Convertida (QTD_CONV)
- 23- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 24- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 25-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 26-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST  Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.

### 3.5 – Recuperação da Movimentação do Equipamento ECF (C430)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C430) - x302_inf_comp_st_res_it_ecf


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data do Movimento (DATA_FISCAL) – data enquadrada no período informado em tela;

Recuperar os campos:
- 10-Código do Motivo (COD_MOTIVO)
- 11-Quantidade Convertida (QTD_CONV)
- 19- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 20- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 21-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 22-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST  Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


### 3.6 – Recuperação da Movimentação do Equipamento SAT-CF-E (C880)


Origem dos dados: - Tabela Informações Complementares das Operações Sujeitas ao ST (C430) - x303_inf_comp_st_res_cupom_cfe


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data da Emissão (DATA_EMISSAO) – data enquadrada no período informado em tela;

Recuperar os campos:
- 11-Código do Motivo (COD_MOTIVO)
- 12-Quantidade Convertida (QTD_CONV)
- 20- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 21- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 22-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 23-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST  Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


### 3.7– Recuperação a Movimentação de Devolução de Saída (C181)


Origem dos dados: - Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST (C181 e C186) - X308_INFO_COMPL_ST_IT_MERC_DEV;


Critérios da recuperação:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Fiscal – data enquadrada no período informado em tela;

- Nota de entrada (MOVTO_E_S <> “9”);

Recuperar os campos:
- 31-Código do Motivo (COD_MOTIVO)
- 32-Quantidade Convertida (QTD_CONV)
- 43- Valor Unitário ICMS-ST Conv. Rest. (VLR_UNIT_ICMSS_REST_CONV)
- 44- Valor Unitário FCP-ST Conv. Rest.  (VLR_UNIT_FCPS_REST_CONV)
- 45-Valor Unitário ICMS-ST Conv. Compl. (VLR_UNIT_ICMSS_COMPL_CONV)
- 46-Valor Unitário FCP-ST Conv. Compl. (VLR_UNIT_FCPS_COMPL_CONV)

Calcular os valores de ICMS-ST e FECEP-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade. Veja:
- Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST)      = VLR_UNIT_ICMSS_REST_CONV x QTD_CONV
- Valor do FCP-ST Restituição (VLR_FCP_ST_REST)         =  VLR_UNIT_FCPS_REST_CONV x QTD_CONV
- Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) = VLR_UNIT_ICMSS_COMPL_CONV x QTD_CONV
- Valor do FCP-ST Complemento (VLR_FCP_ST_COMP)     = VLR_UNIT_FCPS_COMPL_CONV x QTD_CONV

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.


## Gravação dos Dados na Tabela de Saldo Consolidado da Restituição/Complemento - X304_SALDO_CONS_RES_COMP_ICMS


Os valores recuperados nas consultas acima, devem ser consolidados pelo Código de Motivo, gerando um registro para cada código.

Caso registro já exista na tabela x304_saldo_cons_res_comp_icms (caso que foi incluído via digitação ou importação), então:
Gravar a seguinte mensagem de aviso no log:
“Registro 1255: Registro de Saldo incluído via importação/manutenção da SAFX304, foi atualizado pelo processamento da geração. Os dados originalmente inseridos foram desprezados”
Exibir dados para identificação do registro (dados da chave);

Contabilizar o número de registros inseridos e atualizados a ser demonstrado para o 1255 no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.




Sobre o campo IND_GRAVAÇÃO:
O ind_gravação informa a origem do registro nas tabelas definitivas (X) que possuem importação por SAFX.

IND_GRAVACAO:
Valores padrão do campo ( tabelas de importação ):
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




## RELATORIO DE CONFERÊNCIA


Gerar arquivos excel a partir da leitura da tabela x304_saldo_cons_res_comp_icms
Nome do arquivo: Relatório_Conferência_1255_mm_aaaa_cod_estab.xlsx


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS48753 | Liliane Videira Assaf | Criação da funcionalidade. Não estamos considerando Cupom Fiscal nesta entrega. | 22/12/2020 |
| MFS65137 | Liliane Videira Assaf | Os cupons fiscais gravados na tabela X297_INF_COMP_ST_CUPOM_ECF para geração do registro C480, passam a ser considerados na geração do registro 1255 do Sped Fiscal. | 13/05/2021 |
| MFS72429 | Andréa Rocha | Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados.  Conforme informação passada pela SEFAZ/RS. | 11/10/2021 |


| PK | Item SAFX304 | Campo |  | Regra de Preenchimento | Campos para relatório |
| --- | --- | --- | --- | --- | --- |
| Campos do layout da SAFX304 | Campos do layout da SAFX304 | Campos do layout da SAFX304 | Campos do layout da SAFX304 | Campos do layout da SAFX304 |  |
| (*) | 01 | Código da Empresa | COD_EMPRESA | Código da empresa de login. | Cod Empresa |
| (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do estabelecimento SELECIONADO na tela de geração. | Cod Estab |
| (*) | 03 | Data da Apuração | DATA_APURACAO | Último dia do Mês da geração, informado na tela de geração. | Dt Apuração |
| (*) | 04 | Código do Motivo | COD_MOTIVO | Código do Motivo recuperado nas consultas descritas no tópico 3. | Cod Motivo |
|  | 05 | Valor do ICMS | VLR_ICMS | Preencher com Zero. OBS: em conversa com o CAN identificamos que não seria possível calcular esse valor. Caso seja necessário preenche-lo isso ser fará através da tela de manutenção, disponível no módulo Sped Fiscal. | Vlr ICMS |
|  | 06 | Valor do ICMS-ST Restituição | VLR_ICMS_ST_REST | Valor do ICMS-ST Restituição (VLR_ICMS_ST_REST) calculado nas consultas descritas no tópico 3. | Vlr ICMS-ST Rest. |
|  | 07 | Valor do FCP-ST Restituição | VLR_FCP_ST_REST | Valor do FCP-ST Restituição (VLR_FCP_ST_REST) calculado nas consultas descritas no tópico 3. | Vlr FECEP-ST Rest. |
|  | 08 | Valor do ICMS-ST Complemento | VLR_ICMS_ST_COMP | Valor do ICMS-ST Complemento (VLR_ICMS_ST_COMP) calculado nas consultas descritas no tópico 3. | Vlr ICMS-ST Compl. |
|  | 09 | Valor do FCP-ST Complemento | VLR_FCP_ST_COMP | Valor do FCP-ST Complemento (VLR_FCP_ST_COMP) calculado nas consultas descritas no tópico 3. | Vlr FECEP-ST Compl. |
|  |  | Indicador de Gravação | IND_GRAVACAO | ‘6’ |  |
