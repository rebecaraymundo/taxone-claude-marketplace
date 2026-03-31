# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Tratamento Novo Produto sem Inventário

> Fonte: MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Tratamento Novo Produto sem Inventário.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Tratamento para Novos Produtos sem Inventários



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração  IN-RE 087/20  Geração dos Movimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Recuperação dos Dados e Processamento	1
1º passo Limpeza	1
2º Passo – Recuperar os Produtos Sujeitos a ST Movimentados no período de geração e sem registro Inventário	1
3º Passo – Gravação da Tabela de Médias Ponderadas	1


## Introdução


Essa rotina faz o tratamento para produtos novos. Ou seja, produtos que iniciaram sua movimentação no período da geração, não existia movimentação em período anterior e o cliente não carrega o inventário do último dia do mês anterior pois este registro não existe no sistema ERP de origem.
Exemplo: geração do mês de setembro de 2021. Primeira movimentação do produto (nota de entrada) em 15/09/2021. Produto sem inventário na X52 para 31/08/2021.

Esta rotina irá identificar tais produtos e carregar a tabela de médias ponderadas (EST_ST_RS_MEDIA_POND), para o produto e dia imediatamente anterior ao mês da geração com quantidades e valores zerados.  A rotina de Transferência dos Movimentos para EFD Fiscal irá ler esse registro da tabela de médias ponderadas (EST_ST_RS_MEDIA_POND), e gerar um registro na X52 com quantidade e valores zerados.

Essa rotina deve ser executada após o cálculo da média ponderada.

Observação: Originalmente a rotina de Geração do Movimento exigia que todos os Produto sujeito a ICMS-ST tivessem inventário carregados na SAFX52 para o dia imediatamente anterior ao mês da geração.  Mas o cliente Magazine Luiza possui na faixa de 2000 produtos novos no mês e não carrega inventário para esses novos produtos.






## Recuperação dos Dados e Processamento



### 1º Passo – Recuperar os Produtos Sujeitos a ST Movimentados no período de geração e sem registro Inventário


Vamos recuperar os produtos sujeitos a ST, que exista movimento no período da geração e que não possua registro de inventário para o último dia do mês anterior.
Para isso vamos fazer duas consultas:
- Consulta recuperando os produtos com movimento de entrada, devolução de entrada e devolução de saída no período, através da leitura da tabela de Média Ponderada (com pelo menos um dia com quantidade >0) e que não possua registro de inventário para o último dia do mês anterior.
- Consulta recuperando os produtos com movimentação de saída no período, através da leitura da Tabela da Movimentação de Saída (EST_ST_RS_NF_SAI) e que não possua registro de inventário para o último dia do mês anterior.

Veja o detalhamento das consultas a seguir:

a) Consulta da tabela de Média Ponderada:

Origem dos dados:  - Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data – pertencente ao período que está sendo processado;

- Qtde total Convertida Inicial (QTD_CONV_INI) >0 OU Quantidade de Devolução de Saída (QTD_CONV_DEV_SAI_MP) > 0 OU
Quantidade Entrada Convertida (QTD_CONV_ENT_MP)>0 OU Quantidade Devolução de Entrada (QTD_CONV_DEV_ENT_MP) >0 OU
Qtde total Convertida Final (QTD_CONV_FIM)> 0

- NÃO EXISTE registro de Inventário para o produto na Tabela do Inventário (X52_INVENT_PRODUTO), com os critérios:
- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;
- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;
- IND_GRAVACAO (X52)  <> 9 -- significa que o cliente não carregou a x52
[MFS518178]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), dos registros com IND_GRAVACAO = B foi incluída no início da Geração dos Movimentos. Dessa forma esse critério se tornou desnecessário:
Ou
EXISTE registro de Inventário para o produto na Tabela do Inventário (X52_INVENT_PRODUTO), com os critérios:
- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;
- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;
- IND_GRAVACAO (X52) = 9 -- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), com os critérios abaixo atendidos:
- - Empresa – código da empresa do login;
- - Estabelecimento – código do estabelecimento selecionado para geração;
- - Data = último dia do mês anterior que está sendo processado;
- - Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- - IND_GRAVACAO = ‘B’ – significa que o os valores unitários foram calculados por essa rotina

- Só recuperar os Produtos estão no primeiro período de geração.
Ou seja, o Produto que não possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:
Origem dos dados: - Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data pertencente ao mês anterior que está sendo processado;
- Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- Qtde total Convertida Inicial (QTD_CONV_INI) >0 OU Quantidade de Devolução de Saída (QTD_CONV_DEV_SAI_MP) > 0 OU
Quantidade Entrada Convertida (QTD_CONV_ENT_MP)>0 OU Quantidade Devolução de Entrada (QTD_CONV_DEV_ENT_MP) >0 OU
Qtde total Convertida Final (QTD_CONV_FIM)> 0
[MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar os Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o produto da Média Ponderada:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código


b) Consulta da tabela de Movimentação de Saída:
Vamos recuperar os produtos sujeitos a ST, que exista movimento de saída no período e que não possua registro de inventário para o último dia do mês anterior. Para isso fazer a consulta a seguir:

Origem dos dados:  - Tabela da Movimentação de Saída do Ressarcimento (EST_ST_RS_NF_SAI)
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Fiscal – pertencente ao período que está sendo processado;

- NÃO EXISTE registro de Inventário para o produto na Tabela do Inventário (X52_INVENT_PRODUTO), com os critérios:
- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;
- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;
- IND_GRAVACAO (X52)  <> 9 -- significa que o cliente não carregou a x52

[MFS518178]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), dos registros com IND_GRAVACAO = B foi incluída no início da Geração dos Movimentos. Dessa forma esse critério se tornou desnecessário:
Ou
EXISTE registro de Inventário para o produto na Tabela do Inventário (X52_INVENT_PRODUTO), com os critérios:
- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;
- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;
- IND_GRAVACAO (X52) = 9 -- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), com os critérios abaixo atendidos:
- - Empresa – código da empresa do login;
- - Estabelecimento – código do estabelecimento selecionado para geração;
- - Data = último dia do mês anterior que está sendo processado;
- - Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- - IND_GRAVACAO = ‘B’ – significa que o os valores unitários foram calculados por essa rotina

- Só recuperar os Produtos estão no primeiro período de geração.
Ou seja, o Produto que não possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:
Origem dos dados: - Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data pertencente ao mês anterior que está sendo processado;
- Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- Qtde total Convertida Inicial (QTD_CONV_INI) >0 OU Quantidade de Devolução de Saída (QTD_CONV_DEV_SAI_MP) > 0 OU
Quantidade Entrada Convertida (QTD_CONV_ENT_MP)>0 OU Quantidade Devolução de Entrada (QTD_CONV_DEV_ENT_MP) >0 OU
Qtde total Convertida Final (QTD_CONV_FIM)> 0
[MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar os Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o produto do movimento de saída:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código



### 2º Passo – Gravação da Tabela de Médias Ponderadas


Para cada Produto sujeito ao ICMS-ST(*), gravar um registro na tabela EST_ST_RS_MEDIA_POND com os valores zerados, para o último dia do mês anterior.



Tabela EST_ST_RS_MEDIA_POND

Os campos sinalizados com asterisco compõem a chave da tabela.


[MFS518178]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), dos registros com IND_GRAVACAO = B foi transferida para o início da Geração dos Movimentos:

Obs: Limpar os registros de processos anteriores da tabela EST_ST_RS_MEDIA_POND com IND_GRAVACAO = B com os seguintes critérios:
- Empresa = Código da empresa de login
- Estabelecimento = Código do estabelecimento SELECIONADO na tela de geração
- Data = último dia do mês anterior que está sendo processado.
- IND_GRAVACAO = ‘B’ – significa que o os valores unitários foram calculados por essa rotina
- Número do Processo diferente do número do processo da geração em execução

Limpar os registros de processos anteriores na Tabela do Inventário (X52_INVENT_PRODUTO), com os seguintes critérios:
- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;
- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), com os critérios abaixo atendidos:
- - Empresa – código da empresa do login;
- - Estabelecimento – código do estabelecimento selecionado para geração;
- - Data = último dia do mês anterior que está sendo processado;
- - Produto = Produto do inventário
- - IND_GRAVACAO = ‘B’ – significa que o os valores unitários foram calculados por essa rotina
- - Numero do Processo diferente do número do processo da geração em execução


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS72958 | Liliane Videira Assaf | Tratamento de produtos novos sem inventário. | 21/09/2021 |
| MFS81749 | Liliane Assaf | Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473 | 15/03/2022 |
| MFS518178 | Liliane Assaf | Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), dos registros com IND_GRAVACAO = B foi transferida para o início da Geração dos Movimentos | 27/12/2023 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


| PK | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- |
| (*) | Código do Estabelecimento | COD_ESTAB | Código do estabelecimento SELECIONADO na tela de geração |
| (*) | Código da Empresa | COD_EMPRESA | Código da empresa de login |
| (*) | Código do Estabelecimento | COD_ESTAB_ORIG | Código do estabelecimento SELECIONADO na tela de geração |
| (*) | Data | DATA | Último dia do mês anterior. |
| (*) | Produto | Grupo_Produto, Ind_Produto, Cod_Produto | Produto sujeito ao ICMS-ST foco do processamento. |
| Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia |
|  | Qtde total Convetida Inicial | QTD_CONV_INI | Preencher com zero. |
|  | Valor do ICMS Calculado Inicial | VLR_ICMS_INI_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado Inicial | VLR_ICMS_ST_INI_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado Inicial | VLR_BC_ST_INI_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado Inicial | VLR_FECEP_ST_INI_MP | Preencher com zero. |
| Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_SAI_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_SAI_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_SAI_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_SAI_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_SAI_MP | Preencher com zero. |
| Entradas do Dia | Entradas do Dia | Entradas do Dia | Entradas do Dia |
|  | Quantidade Entrada Convertida | QTD_CONV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Entrada | VLR_ICMS_ENT_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Entrada | VLR_ICMS_ST_ENT_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Entrada | VLR_BC_ST_ENT_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Entrada | VLR_FECEP_ST_ENT_MP | Preencher com zero. |
| Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_ENT_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_ENT_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_ENT_MP | Preencher com zero. |
| Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia |
|  | Qtde total Convetida Final | QTD_CONV_FIM | Preencher com zero. |
|  | Valor do ICMS Calculado Final | VLR_ICMS_FIM_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado Final | VLR_ICMS_ST_FIM_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado Final | VLR_BC_ST_FIM_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado Final | VLR_FECEP_ST_FIM_MP | Preencher com zero. |
| Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia |
|  | Valor Médio Unitário do ICMS | VLR_UNIT_ICMS_FIM_MP | Preencher com zero. |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP | VLR_UNIT_ICMS_ST_FIM_MP | Preencher com zero. |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP | VLR_UNIT_ICMS_ST_FECEP_FIM_MP | Preencher com zero. |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST | VLR_UNIT_BC_ST_FIM_MP | Preencher com zero. |
|  | Valor Médio Unitário do FECEP-ST | VLR_UNIT_FECEP_ST_FIM_MP | Preencher com zero. |
|  | Indicador de Gravação | IND_GRAVACAO | ‘B’ – significa que o os valores unitários foram calculados por essa rotina |
|  | Número do Processo | PROC_ID | Número do Processo da geração do movimento |
