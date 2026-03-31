# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Inventário_H030

> Fonte: MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Inventário_H030.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Atualização do Inventário do Último Dia do Mês Anterior



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração  IN-RE 087/20  Transferência dos Movimentos para EFD Fiscal



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Recuperação dos Dados e Processamento	1
2.1 Recuperação dos Valores Unitários do último dia do mês anterior - Tabela do Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND)	1
2.2 - Recuperação do Inventário do último dia do mês anterior - Tabela de Inventário (X52_INVENT_PRODUTO)	1
3.	Gravação dos Dados	1
3.1 – Atualização da Tabela de Inventário X52_INVENT_PRODUTO	1


## Introdução


Essa rotina atualizará os campos relativos à valores unitários do ICMS, ICMS-ST,BC ICMS-ST e FECEP-ST (21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO) da Tabela do Inventário (X52_INVENT_PRODUTO) do último dia do mês anterior, com os valores unitários calculados pela Média Pondera Móvel, que estão armazenados na tabela EST_ST_RS_MEDIA_POND.
Essa atualização será executada a partir do segundo período de geração de um produto sujeito a ICMS-ST, pois o primeiro período exige que os valores unitários do ICMS, ICMS-ST,BC ICMS-ST e FECEP-ST venham carregados na Tabela do Inventário (X52_INVENT_PRODUTO).

MFS72958:
Originalmente esta rotina apenas atualizava os registros da Tabela do Inventário (X52_INVENT_PRODUTO). A MFS72958 introduziu tratamento para novos produtos que iniciam sua movimentação no período e que não possuem inventário. Com isso, essa funcionalidade passou a realizar inserção de registros na tabela do Inventário (X52_INVENT_PRODUTO).

Pré-requisito:
É necessário que todos os produtos sujeitos a ICMS-ST possuam um registro de inventário (SAFX52) com IND_MOT_INV = 06 no dia imediatamente anterior ao período de geração.

MFS72212: Criação do Cálculo dos Valores Unitários Médios do Inventário:
Para o primeiro período da geração de um Produto sujeito a ICMS-ST, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST devem estar carregados na SAFX52 para o dia imediatamente anterior ao mês da geração.
Antes da MFS72212, para o primeiro período da geração era necessário que os valores médios unitários fossem carregados na SAFX52 (campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO) no último dia do mês anterior ao período da geração, com IND_MOT_INV = 06. A partir da MFS72212, a geração do movimento passou a calcular os valores médios unitários do inventário com base nas últimas notas de entradas do produto.  Sendo assim, o preenchimento dos valores unitários na SAFX52 para o primeiro período de geração tornou-se opcional. Caso valores unitários venham carregados na SAFX52 estes serão utilizados para o cálculo da Média Ponderada, caso contrário a rotina irá calculá-los.
O Cálculo da Média Pondera Móvel utilizará esses valores unitários para cálculo do saldo inicial do primeiro dia do mês da geração.

A partir do segundo período de geração, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST não precisam mais ser carregados na SAFX52 para o último dia do mês anterior, pois tais valores já estarão calculados pela geração do mês anterior e armazenados na tabela EST_ST_RS_MEDIA_POND.
A partir do segundo período de geração, essa rotina atualizará os campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO da Tabela do Inventário (X52_INVENT_PRODUTO) do último dia do mês anterior, com os valores unitários médios calculados. Para isso o cliente deve carregar um registro na SAFX52 do último dia do mês anterior, com IND_MOT_INV = 06, sem os valores unitários médios.

O Sped Fiscal exige que exista um registro H030 com MOTIVO INVENTÁRIO = “06” no arquivo que apresentar pelo menos um registro C180, C181, C185, C186, C330, C380, C430, C480, C815.  Por esse motivo é necessário que todo mês exista um registro na SAFX52 dos produtos sujeitos ao ICMS-ST com IND_MOT_INV = 06, do último dia do mês anterior. Sendo que, no primeiro mês os valores unitários médios devem ser carregados, e nos demais meses não.

Sobre Produtos Associados:
Para identificar os produtos sujeitos a ICMS-ST utilizamos as opções de parametrização do menu Parâmetros  Produtos: “Por Código”, ou “Por NCM” ou “CEST”.  A parametrização Por Código aceita trabalharmos com o conceito de Produtos Associados. Parametriza-se um produto “principal” e N produtos associados. O produto “principal” é gravado na tabela (ESP_SP_PROD_ST), e os associados ao produto principal na tabela ESP_SP_PROD_ST_ASS.  Os produtos associados servem para recuperação dos movimentos de entradas, saídas e devoluções (x07/x08/x993/x994).  Mas todo o controle de Inventário (SAFX52) é em nome do Produto Principal.  O Cálculo da Média Ponderada Móvel é gravado em nome do Produto Principal.


## Recuperação dos Dados e Processamento


Para a atualização do inventário, realizar o seguinte procedimento:

Passo 1: Consultar a tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND) para o último dia do mês anterior, e recuperar os valores unitários dos produtos sujeitos a ICMS-ST. Ver especificação da consulta à tabela EST_ST_RS_MEDIA_POND no tópico 2.1.

Passo 2: Para cada produto sujeito a ICMS-ST recuperado no passo 1, buscar o Inventário para o último dia do mês anterior  (Tabela do Inventário - X52_INVENT_PRODUTO).
Ver especificação da consulta à tabela X52_INVENT_PRODUTO no tópico 2.2.
MFS72958:
Caso o Inventário não seja encontrado, E o IND_GRAVACAO da EST_ST_RS_MEDIA_POND seja <> B, então gravar a seguinte mensagem de erro no log e não gravar a Tabela do Inventário.
“Registro H030: Não foi possível atualizar o Inventário com os valores unitários calculados pela Média Ponderada Móvel, pois não foi encontrado registro de Inventário para o Produto em DD/MM/AAAA. Importe a SAFX52 ou inclua via manutenção, o inventário para o produto em DD/MM/AAAA.”
Onde: DD/MM/AAAA = último dia do mês anterior
Dados de Indentificação: Estabelecimento: xxx - Produto(ind/cód) x-xxx

[MFS84493] Inclusão da recuperação da Conta Contábil na geração do registro de inventário zerado
Caso o Inventário não seja encontrado, E o IND_GRAVACAO da EST_ST_RS_MEDIA_POND seja = B, então:
Recuperar o campo “Natureza de Estoque” e o campo “Conta Contábil” da Parametrização dos Dados Iniciais da IN087/20 (tabela EST_ST_RS_DADOS_INI_IN87) para o estabelecimento foco da geração.
Caso o campo “Natureza de Estoque” não esteja preenchido, então exibir a mensagem de erro no log e abortar a geração do H030:
“Registro H030: Falta informar a "Natureza de Estoque" na Parametrização dos Dados Iniciais para geração dos registros de inventário. Favor ajustar a parametrização localizada no menu Parâmetros  IN-RE 087/20  Dados Iniciais”
Caso o campo “Natureza de Estoque” esteja preenchido, então inserir registro na Tabela do Inventário (X52_INVENT_PRODUTO). Ver tópico 3.2.
Se o campo “Conta Contábil” estiver preenchido, utilizar o código para inserir o registro na Tabela do Inventário (X52_INVENT_PRODUTO). Ver tópico 3.2.  O campo de Conta Contábil não é obrigatório na tabela de inventário por produto, então não será dada uma mensagem no log quando ele não for preenchido na Parametrização dos Dados Iniciais.

Obs: o IND_GRAVACAO da EST_ST_RS_MEDIA_POND = B identifica os novos produtos que iniciam sua movimentação no período e que não possuem inventário. Para esses produtos o inventário será gravado zerado.
Ver tratamento na Geração do Movimento para os novos produtos que iniciam sua movimentação no período especificado na “MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Tratamento Novo Produto sem Inventário.docx”.

Caso o Inventário seja encontrado, então:
Verificar se os valores unitários estão zerados (campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO da SAFX52).
Se pelo menos um dos valores for diferente de zero e o campo IND_GRAVAÇÃO for diferente de ‘9’, então:
Gravar a seguinte mensagem de aviso no log:
“Registro H030: Os valores médios Unitários de ICMS, ICMS-ST, Base ICMS-ST e FECEP da Tabela de Inventário (SAFX52, campos 21,22,43,44) foram atualizados com os valores unitários calculados pela Média Ponderada Móvel, para o produto em DD/MM/AAAA.  Os valores médios Unitários do inventário que foram previamente inseridos via importação ou manutenção, foram desprezados.”
Onde: DD/MM/AAAA =  último dia do mês anterior
Dados de Indentificação: Estabelecimento: xx -  Produto(ind/cód) x-xxx

Atualizar os valores unitários na Tabela do Inventário (X52_INVENT_PRODUTO). Ver tópico 3.1.

Senão:
Atualizar os valores unitários na Tabela do Inventário (X52_INVENT_PRODUTO). Ver tópico 3.1.


Sobre o campo IND_GRAVAÇÃO:
O ind_gravação informa a origem do registro nas tabelas definitivas (X) que possuem importação por SAFX. Essa rotina ao atualizar os registros da X52_INVENT_PRODUTO e grava o IND_GRAVACAO com 9. Qualquer outro valor indica que o registro originou-se de outro processo (importação, digitação).

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

Sobre o “Cálculo da Média Pondera Móvel dos Valores Unitários”
Os valores unitários calculados são armazenados na tabela EST_ST_RS_MEDIA_POND.
Para maiores informações veja o documento matriz “MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Média Ponderada.docx”.


### 2.1 Recuperação dos Valores Unitários do último dia do mês anterior - Tabela do Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND)


Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data imediatamente anterior ao primeiro dia do Período (Mês/Ano) informado na Tela de Geração;

- O produto deve constar na parametrização do menu “Parâmetros  Produtos  Por Código”, ou, seu NCM deve estar parametrizado no menu “Parâmetros  Produtos  Por NCM”, ou, seu CEST deve estar parametrizado no menu “Parâmetros  Produtos  Por CEST”.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”. Ao verificar a parametrização por código, basta considerar o produto “principal”. Pois conforme já explicado, o cálculo é gravado em nome do produto “principal” (ESP_SP_PROD_ST).

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada.
-Caso não, é verificado se o NCM do produto (NCM do cadastro do produto) consta na parametrização da opção “Por NCM”.
-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada.
-Caso não, é verificado se o CEST do produto (CEST do cadastro do produto) consta na parametrização da opção “Por CEST”.
[MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar a Média Ponderada de Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar a Média Ponderada:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código

Recuperar as seguintes informações:
- Produto (grupo, indicador e código)
- Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP);
- Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP);
- Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP)
- Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP)
- Indicador de Gravação (IND_GRAVACAO)
[MFS90131] Arredondar para 6 casas decimais os valores médios unitários recuperados da Média Ponderada.


### 2.2 - Recuperação do Inventário do último dia do mês anterior - Tabela de Inventário (X52_INVENT_PRODUTO)

Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do Inventário (X52_INVENT_PRODUTO).
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data do Inventário (campo 03 - DATA_INVENTARIO) imediatamente anterior ao primeiro dia do Período (Mês/Ano) informado na Tela de Geração;

- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;

- Grupo Contagem (campo 04 - GRUPO_CONTAGEM)  1, 2, 3 e 5;

- Produto  recuperado da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), conforme consulta especificada no tópico 2.1.
MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar o inventário de Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o inventário:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto do inventário estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código

Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto. Caso isso ocorra, recuperar registro a registro, individualmente. Considerar as seguintes informações:
- Produto (grupo, indicador e código)
- 21 - Valor de ICMS Médio (VLR_ICMS_MEDIO)
- 22 - Valor de ICMS-ST Médio (VLR_ICMSS_MEDIO)
- 43 - Valor Base ICMS-ST Médio (VLR_BASE_ICMSS_MEDIO)
- 44 - Valor FECEP Médio (VLR_FCP_MEDIO)




## Gravação dos Dados


Os registros de Inventário recuperados no tópico 2.2 serão atualizados, conforme definido a seguir.

### 3.1 – Atualização da Tabela de Inventário X52_INVENT_PRODUTO


Contabilizar o número de registros atualizados a ser demonstrado para o H030 no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.


### 3.2 – Inserção de registros na Tabela



Contabilizar o número de registros inseridos a ser demonstrado para o H030 no relatório de “Resumo Registros Gerados”, especificado no “MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx”.


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS48753 | Liliane Videira Assaf | Criação da funcionalidade. Esta entrega não estão sendo contemplados: - Parametrização com Produtos Associados | 12/01/2021 |
| MFS66171 | Liliane Videira Assaf | Alteração na atualização da X52 para considerar o Valor Médio Unitário ICMS-ST c/ FECEP”. Base Legal: Guia Prático EFD – registro H030 – campo 04: “Campo 04 (VL_ICMS_ST) : Preenchimento: Informar o valor médio unitário do ICMS ST pago ou retido limitado à parcela do ICMS ST correspondente ao fato gerador presumido que ainda não se realizou. Quando a mercadoria estiver sujeita, também, ao FCP adicionado ao ICMS ST, neste campo deve ser informado o valor médio unitário total da parcela do ICMS ST + a parcela do FCP vinculado a este.” | 07/06/2021 |
| MFS72958 | Liliane Videira Assaf | Tratamento de produtos novos sem inventário. - Realizar o insert na tabela X52_INVENT_PRODUTO. - Contabilizar o número de Registros Lidos da tabela EST_ST_RS_MEDIA_POND.  - Contabilizar o número de registros inseridos na tabela X52_INVENT_PRODUTO. Contadores de registros lidos e inseridos são demonstrados no Resumo de “Quantidade Total de Registros Gravados”. | 21/09/2021 |
| MFS81749 | Liliane Assaf | Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473 | 15/03/2022 |
| MFS84493 | Andréa Rocha | Tratamento de produtos novos sem inventário: - Inclusão da recuperação da Conta Contábil | 22/04/2022 |
| MFS90131 | Liliane Assaf | Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte. | 01/08/2022 |
| MFS89648 | Liliane Assaf | Atualização legal IN55/22:  Tratamento para Valor Médio Ponderado Móvel calculado ao final do dia negativo  (19.3-A.2.2.2 da  na IN-045/98)  Quando o Valor Médio Ponderado Móvel do último dia do mês anterior for negativo: Zerar os valores unitários a serem apresentados no H030 do mês; | 10/08/2022 |


| Campo X52_INVENT_PRODUTO | Regra de Preenchimento |
| --- | --- |
| Valor de ICMS Médio (21 - VLR_ICMS_MEDIO) | Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP) da EST_ST_RS_MEDIA_POND [MFS90131] Arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do H030.  [MFS89648]: Tratamento para Valor Médio Ponderado negativo: Caso o “Valor Médio Unitário da Base de Cálculo do ICMS-ST” (VLR_UNIT_BC_ST_FIM_MP), recuperado no tópico 2.1 for negativo, então:     Desconsiderar a regra acima e preencher este campo com ZERO. |
| Valor de ICMS-ST Médio (22 - VLR_ICMSS_MEDIO) | Valor Médio Unitário do ICMS-ST (VLR_UNIT_ICMS_ST_FIM_MP) da EST_ST_RS_MEDIA_POND [MFS66171] Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP) da EST_ST_RS_MEDIA_POND [MFS90131] Arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do H030.  [MFS89648]: Tratamento para Valor Médio Ponderado negativo: Caso o “Valor Médio Unitário da Base de Cálculo do ICMS-ST” (VLR_UNIT_BC_ST_FIM_MP), recuperado no tópico 2.1 for negativo, então:     Desconsiderar a regra acima e preencher este campo com ZERO. |
| Valor Base ICMS-ST Médio (43 - VLR_BASE_ICMSS_MEDIO) | Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP) da EST_ST_RS_MEDIA_POND [MFS90131] Arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do H030.  [MFS89648]: Tratamento para Valor Médio Ponderado negativo: Caso o “Valor Médio Unitário da Base de Cálculo do ICMS-ST” (VLR_UNIT_BC_ST_FIM_MP), recuperado no tópico 2.1 for negativo, então:     Desconsiderar a regra acima e preencher este campo com ZERO. |
| Valor FECEP Médio (44 - VLR_FCP_MEDIO) | Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP) da EST_ST_RS_MEDIA_POND [MFS90131] Arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do H030.  [MFS89648]: Tratamento para Valor Médio Ponderado negativo: Caso o “Valor Médio Unitário da Base de Cálculo do ICMS-ST” (VLR_UNIT_BC_ST_FIM_MP), recuperado no tópico 2.1 for negativo, então:     Desconsiderar a regra acima e preencher este campo com ZERO. |
| IND_GRAVACAO | Fixo ‘9’ |


| Campo X52_INVENT_PRODUTO | Campo X52_INVENT_PRODUTO | Campo X52_INVENT_PRODUTO | Regra de Preenchimento |
| --- | --- | --- | --- |
| 01 | Código da Empresa | COD_EMPRESA | código da empresa do login; |
| 02 | Código do Estabelecimento | COD_ESTAB | código do estabelecimento selecionado para geração; |
| 03 | Data do Inventário | DATA_INVENTARIO | Dia imediatamente anterior ao primeiro dia do Período (Mês/Ano) informado na Tela de Geração |
| 04 | Grupo de Contagem | GRUPO_CONTAGEM | Preencher com “1” |
| 05 | Código de Classificação Fiscal - NBM | COD_NBM | Não preencher |
| 06 | Indicador do Produto | IND_PRODUTO | Indicador do Produto recuperado no passo 1 |
| 07 | Produto | COD_PRODUTO | Indicador do Produto recuperado no passo 1 |
| 08 | Unidade Padrão | COD_UND_PADRAO | Código de Unidade Padrão do Produto recuperado no passo 1 (campo 20 da SAFX2013) |
| 09 | Almoxarifado | COD_ALMOX | Não preencher |
| 10 | Centro de Custo | COD_CUSTO | Não preencher |
| 11 | Natureza de Estoque | COD_NAT_ESTOQUE | Campo “Natureza de Estoque” da Parametrização dos Dados Iniciais da IN087/20 (tabela EST_ST_RS_DADOS_INI_IN87). |
| 12 | Unidade de Medida | COD_MEDIDA | Código de Unidade de Medida do Produto recuperado no passo 1 (campo 14 da SAFX2013) |
| 13 | Quantidade de Inventário | QUANTIDADE | Preencher com zero. |
| 14 | Custo Total | VLR_TOT | Preencher com zero. |
| 15 | Custo Unitário | VLR_UNIT | Preencher com zero. |
| 16 | Observação | OBSERVACAO | Não preencher |
| 17 | Valor do ICMS | VLR_ICMS | Preencher com zero. |
| 18 | Código Conta Contábil | COD_CONTA | [MFS84493] Inclusão do preenchimento da Conta Contábil Campo “Conta Contábil” da Parametrização dos Dados Iniciais da IN087/20 (tabela EST_ST_RS_DADOS_INI_IN87). |
| 19 | Débito/Crédito | IND_DEB_CRE | Não preencher |
| 20 | Discriminação | DESCRICAO_RIPI | Não preencher |
| 21 | Valor de ICMS Médio | VLR_ICMS_MEDIO | Preencher com zero. |
| 22 | Valor de ICMS-ST Médio | VLR_ICMSS_MEDIO | Preencher com zero. |
| 23 | Inscrição Estadual | INSC_ESTADUAL | Não preencher |
| 24 | Indicador de Pessoa Física/Jurídica | IND_FIS_JUR | Não preencher |
| 25 | Código de Pessoa Física/Jurídica | COD_FIS_JUR | Não preencher |
| 26 | Base ICMS | VLR_BASE_ICMS | Preencher com zero. |
| 27 | Base Isenta ICMS | VLR_BASE_ISENTO | Preencher com zero. |
| 28 | Base Outras de ICMS | VLR_BASE_OUTRAS | Preencher com zero. |
| 29 | Base de ICMS-S | VLR_BASE_ICMSS | Preencher com zero. |
| 30 | Código da Observação | COD_OBSERVACAO | Não preencher |
| 31 | Vlr do Custo SAICS | VLR_CUSTO_DCA | Preencher com zero. |
| 32 | Indicador do Produto para Rastreabilidade | IND_PRODUTO_RASTRO | Não preencher |
| 33 | Código do Produto para Rastreabilidade | COD_PRODUTO_RASTRO | Não preencher |
| 34 | Valor do IPI | VLR_IPI | Preencher com zero. |
| 35 | Valor do PIS | VLR_PIS | Preencher com zero. |
| 36 | Valor da COFINS | VLR_COFINS | Preencher com zero. |
| 37 | Valor de Outros Tributos Não-Cumulativos | VLR_TRIB_NC | Preencher com zero. |
| 38 | Código Situação Tributária “A” | COD_SITUACAO_A | Não preencher |
| 39 | Código Situação Tributária “B” | COD_SITUACAO_B | Não preencher |
| 40 | Motivo do Inventário | IND_MOT_INV | Preencher com ‘06’ |
| 41 | Situação Tributária | IND_SIT_TRIB | Não preencher |
| 42 | Valor Total para o IR | VLR_IR | Preencher com zero. |
| 43 | Valor Base ICMS-ST Médio | VLR_BASE_ICMSS_MEDIO | Preencher com zero. |
| 44 | Valor FECEP Médio | VLR_FCP_MEDIO | Preencher com zero. |
