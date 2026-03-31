# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Média Ponderada

> Fonte: MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Média Ponderada.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Cálculo da Média Ponderada Móvel dos Valores Unitários



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração à IN-RE 087/20 à Geração dos Movimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Recuperação dos Dados e Processamento	1
1º Passo – Calcular o Saldo Inicial do Dia	1
2º Passo – Calcular o Total das Devoluções de Saídas do Dia	1
3º Passo: Calcular o Total das Entradas do Dia	1
4º Passo: Calcular o Total das Devoluções de Entradas do Dia	1
5º Passo: Calcular o Saldo Final do Dia e Gravar a tabela EST_ST_RS_MEDIA_POND	1
3.	Relatório de Conferência	1
4.	Tratamento para Produtos não Movimentados:	1


## Introdução


O Cálculo da Média Pondera Móvel dos Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST, tem como base na IN-RE 087/20 tópicos 19.3-A.2.2, 19.3-A.2.2.2 e 19.3-A.2.2.3 e é executado por DIA, para todos os produtos sujeitos ao ICMS-ST vigentes no período da geração.

O cálculo é feito com quatro valores conforme estabelece o tópico 19.3-A.2.2:
(alínea “a”) no saldo inicial do primeiro dia do período, que corresponde ao saldo final do dia anterior;
(alínea “b”): movimento de devolução de saídas do período;
(alínea “c”): movimento de entradas do período;
(alínea “d”): movimento de devolução de entradas do período;
Os valores das alíneas “b”, “c” e “d” foram calculados em etapas anteriores.

O resultado do cálculo é armazenado numa tabela para uso na Geração dos Movimentos de Saídas e em gerações de períodos posteriores: EST_ST_RS_MEDIA_POND.


Pré-requisito:
É necessário que todos os produtos sujeitos a ICMS-ST possuam um registro de inventário (SAFX52) com IND_MOT_INV = 06 no dia imediatamente anterior ao período de geração.

MFS72212: Criação do Cálculo dos Valores Unitários Médios do Inventário:
Para o primeiro período da geração de um Produto sujeito a ICMS-ST, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST devem estar carregados na SAFX52 para o dia imediatamente anterior ao mês da geração.
Antes da MFS72212, para o primeiro período da geração era necessário que os valores médios unitários fossem carregados na SAFX52 (campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO) no último dia do mês anterior ao período da geração, com IND_MOT_INV = 06. A partir da MFS72212, a geração do movimento passou a calcular os valores médios unitários do inventário com base nas últimas notas de entradas do produto.  Sendo assim, o preenchimento dos valores unitários na SAFX52 para o primeiro período de geração tornou-se opcional. Caso valores unitários venham carregados na SAFX52 estes serão utilizados para o cálculo da Média Ponderada, caso contrário a rotina irá calculá-los.
O saldo inicial do primeiro dia do mês da geração será calculado com base nesses valores. Os demais dias, o saldo inicial será o saldo final do dia anterior.

A partir do segundo período de geração, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST não precisam mais ser carregados na SAFX52 para o último dia do mês anterior, pois tais valores já estarão calculados pela geração do mês anterior.
Além disso a rotina atualizará os campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO da Tabela do Inventário (X52_INVENT_PRODUTO) do último dia do mês anterior, com os valores unitários médios calculados. Para isso o cliente deve carregar um registro na SAFX52 do último dia do mês anterior, com IND_MOT_INV = 06, sem os valores unitários médios.

O Sped Fiscal exige que exista um registro H030 com MOTIVO INVENTÁRIO = “06” no arquivo que apresentar pelo menos um registro C180, C181, C185, C186, C330, C380, C430, C480, C815.  Por esse motivo é necessário que todo mês exista um registro na SAFX52 dos produtos sujeitos ao ICMS-ST com IND_MOT_INV = 06, do último dia do mês anterior. Sendo que, no primeiro mês os valores unitários médios devem ser carregados, e nos demais meses não.

Sobre Produtos Associados:
Para identificar os produtos sujeitos a ICMS-ST utilizamos as opções de parametrização do menu Parâmetros à Produtos: “Por Código”, ou “Por NCM” ou “CEST”.  A parametrização Por Código aceita trabalharmos com o conceito de Produtos Associados. Parametriza-se um produto “principal” e N produtos associados. O produto “principal” é gravado na tabela (ESP_SP_PROD_ST), e os associados ao produto principal na tabela ESP_SP_PROD_ST_ASS.  Os produtos associados servem para recuperação dos movimentos de entradas, saídas e devoluções (x07/x08/x993/x994).  Mas todo o controle de inventário (x52) é em nome do Produto Principal.  O Cálculo da Média Ponderada Móvel é gravado em nome do Produto Principal.

Sobre a Tabela EST_ST_RS_MEDIA_POND:
Para um estabelecimento e mês informados na tela geração, a tabela EST_ST_RS_MEDIA_POND deve ser gravada com um registro para cada dia do mês e produto sujeito a ICMS-ST.
Caso exista apenas parametrização do Produto, mas não exista inventário do Produto (x52), nem movimentação do período (x07, x08) o produto não deve ser gravado na tabela EST_ST_RS_MEDIA_POND.

Por exemplo:
Geração do Estabelecimento 001, de janeiro do 2021.
Os produtos sujeitos ao ICMS-ST, parametrizados numa das opções do menu Parâmetros à Produtos, são: PROD01, PROD02.
Ao final da geração a tabela EST_ST_RS_MEDIA_POND conterá 31 registros pra cada produto, um para cada dia do mês:
ESTAB	PRODUTO	DIA		VALORES CALCULADOS
001		PROD01	01/01/2021	....
001		PROD01	02/01/2021	....
001		PROD01	03/01/2021	....
...
001		PROD01	31/01/2021	....
001		PROD02	01/01/2021	....
001		PROD02	02/01/2021	....
001		PROD02	03/01/2021	....
...
001		PROD02	31/01/2021	....



Texto da IN-RE 087/20, Tópico 19.3-A.2.2 que define Cálculo da Média Pondera Móvel dos Valores Unitários:
“19.3-A.2.2 - Para definir, em relação a cada mercadoria, o valor médio ponderado móvel do dia, definido no subitem 19.3-
A.2.1, ao fim de cada dia, o contribuinte deverá seguir as etapas que seguem:
a) identificar o saldo total do estoque inicial do dia de cada mercadoria, por meio da multiplicação da quantidade total
existente em estoque no fim do dia anterior pelo valor médio ponderado móvel apurado no fim do dia anterior;
b) acrescentar ao valor apurado na alínea "a" as informações referentes a todas as devoluções de saídas da mercadoria e
retornos de mercadorias não entregues, de que trata a alínea "c" do subitem 19.3-A.1, ocorridos durante o dia, que corresponderá à soma
das multiplicações da quantidade de mercadorias de cada devolução e retorno pelo valor unitário médio móvel calculado ao fim do dia em que
ocorreu a saída objeto de devolução ou retorno;
c) acrescentar ao valor apurado na alínea "b" as informações referentes a todas as entradas de mercadorias, de que trata
a alínea "b" do subitem 19.3-A.1, ocorridas durante o dia, que corresponderá à soma das multiplicações da quantidade de cada entrada pelo
valor unitário que serviu de base de cálculo do imposto retido por substituição tributária;
d) subtrair do valor apurado na alínea "c" as informações referentes a todas as devoluções de entradas de que trata a
alínea "d" do subitem 19.3-A.1, que corresponderá à soma das multiplicações da quantidade de cada saída em devolução pelo valor unitário
que serviu de base de cálculo do imposto retido por substituição tributária para a mercadoria objeto de devolução;
e) quantificar o total da mercadoria no fim do dia, desconsideradas as saídas de que trata a alínea "a" do subitem 19.3-A.1
registradas durante o dia, que corresponderá à soma da quantidade existente em estoque no fim do dia anterior com a quantidade das
saídas devolvidas ou retornadas durante o dia, bem como da quantidade que entrou no dia, subtraída da quantidade que saiu em devolução
no dia;
f) obter o resultado, que corresponderá à divisão do total dos valores apurados conforme alíneas "a" a "d" pela
quantidade apurada na alínea "e".”


## Recuperação dos Dados e Processamento


Visão resumida do Processamento
O Cálculo deve ser executado dia por dia, em ordem cronológica.
Para cada dia do mês da geração, executar:
1º: Geração os Movimentos de Devolução das Saídas do dia;
2º: Cálculo da Média Ponderada Móvel dos Valores Unitários do dia.

Geração os Movimentos de Devolução das Saídas do dia:
Veja documento “MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Saidas.docx”.

Cálculo da Média Ponderada Móvel dos Valores Unitários do dia:
1º Passo: Calcular o Saldo Inicial do dia

2º Passo: Calcular o Total das Devoluções de Saídas do dia

3º Passo: Calcular o Total das Entradas do dia

4º Passo: Calcular o Total das Devoluções de Entradas do dia

5º Passo: Calcular o Saldo Final do dia e gravando a tabela EST_ST_RS_MEDIA_POND.



### 1º Passo – Calcular o Saldo Inicial do Dia

Segundo a IN087/20, para calcular o saldo inicial do dia recupera-se o saldo final do dia anterior. Para isso, vamos adotar dois procedimentos, um aplicado ao primeiro dia do mês da geração, e outro para os demais dias do mês:

- Segundo Dia do mês da geração em diante:
Para o segundo ao último dia do mês da geração, recuperar o saldo final do dia anterior da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).

Recuperação do Saldo Final do Dia Anterior da Tabela do Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND)
Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data imediatamente anterior ao DIA que está sendo processado;

- O produto deve constar na parametrização do menu “Parâmetros à Produtos à Por Código”, ou, seu NCM deve estar parametrizado no menu “Parâmetros à Produtos à Por NCM”, ou, seu CEST deve estar parametrizado no menu “Parâmetros à Produtos à Por CEST”.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”. Ao verificar a parametrização por código, basta considerar o produto “principal”. Pois conforme já explicado, o cálculo é gravado em nome do produto “principal” (ESP_SP_PROD_ST).

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada.
-Caso não, é verificado se o NCM do produto (NCM do cadastro do produto) consta na parametrização da opção “Por NCM”.
-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada.
-Caso não, é verificado se o CEST do produto (CEST do cadastro do produto) consta na parametrização da opção “Por CEST”.

Recuperar as seguintes informações:
- Qtde total Convetida Final (QTD_CONV_FIM)
- Valor do ICMS Calculado Final (VLR_ICMS_FIM_MP)
- Valor do ICMS-ST Calculado Final (VLR_ICMS_ST_FIM_MP)
- Valor Base de Cálculo do ICMS-ST Calculado Final (VLR_BC_ST_FIM_MP)
- Valor FECEP-ST Calculado Final (VLR_FECEP_ST_FIM_MP)
- Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAF_MP)

Os campos que compõe o Saldo Inicial do Dia serão preenchidos com os valores do Saldo Final do dia anterior:
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM)
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = Valor do ICMS Calculado Final (VLR_ICMS_FIM_MP)
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = Valor do ICMS-ST Calculado Final (VLR_ICMS_ST_FIM_MP)
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = Valor Base de Cálculo do ICMS-ST Calculado Final (VLR_BC_ST_FIM_MP)
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = Valor FECEP-ST Calculado Final (VLR_FECEP_ST_FIM_MP)

O Saldo Inicial do segundo dia em diante depende a Quantidade Final do dia imediatamente anterior.
1 - Para Quantidade Final (QTD_CONV_FIM) do dia imediatamente anterior IGUAL a Zero:

1.1 - Se o dia corrente possui pelo menos uma Movimentação de Entrada, ou Devolução de Entrada ou Devolução de Saída (QTD_CONV_ENT_MP <>0 ou QTD_CONV_DEV_SAI_MP <> 0 ou
QTD_CONV_DEV_ENT_MP <>0), então:
MFS92151: Subtrair a Quantidade das Saídas do Dia anterior do Saldo Final, para compor o Saldo Inicial (19.3-A.2.2 – “a”)
MFS99147:Só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior (continuação da MFS92151):
Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo (Cálculo da Média Ponderada)” = ‘N’:
Compor a Quantidade Inicial com a Quantidade Final menos quantidade de saídas do dia anterior.
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM) -
- Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP)
Se Quantidade Inicial calculada ficar negativa, exibir a seguinte mensagem de aviso no log da geração:
Cálculo da Média Ponderada Móvel: Valor do Saldo Inicial calculado a partir da movimentacao de saidas, resultou em negativo. Veja os campos <Qtde (Saida do Dia)> e <Qtde Final> do dia anterior no Relatorio de Calculo de Media Ponderada. Dados de Identificação: Empresa: xxx - Estab: xx – Período: 99/99/9999 - Produto(ind/cód) x-xxx – Dia DD/MM/AAAA
- Zera a quantidade de saídas anteriores pois foram utilizadas (Qtde Saída a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP)).
Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo (Cálculo da Média Ponderada)” = ‘S’:
Compor a Quantidade Inicial com a Quantidade Final do dia anterior.
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM)
- Qtde Saída a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) mantém pois não foram utilizadas.
[MFS89648] (19.3-A.2.2.3 da IN-045/98) - Tratamento para Quantidade Final do dia anterior zero:
Verificar se a Quantidade Final foi zerada por conta de ocorrência de devolução de entrada em dias anteriores. Cenário tratado conforme tópico 19.3-A.2.2.3.
Para isso realizar uma busca na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND) com aos critérios:
- Estabelecimento, empresa e produto em questão;
- Data igual ao dia imediatamente anterior ao DIA que está sendo processado;
- Indicador de Utilização do Saldo (19.3-A.2.2.3 IN45/98) (IND_UTIL_DEV_ZERA) seja ‘N’

Se existir registro (significa que em dias anteriores a quantidade final do dia foi zerada por conta de movimentos de devolução de entrada):
Cenário tratado conforme tópico 19.3-A.2.2.3.
Os campos que compõe o Saldo Inicial do Dia serão preenchidos com os campos do “Saldo Inicial p/ próximo dia c /movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3)”.
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = Valor do ICMS (19.3-A.2.2.3 IN45/98) (VLR_ICMS_DEV_ZERA)
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = Valor do ICMS-ST (19.3-A.2.2.3 IN45/98) (VLR_ICMS_ST_DEV_ZERA)
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = Valor Base de Cálculo do ICMS-ST (19.3-A.2.2.3 IN45/98) (VLR_BC_ST_DEV_ZERA)
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = Valor FECEP-ST (19.3-A.2.2.3 IN45/98) (VLR_FECEP_ST_DEV_ZERA)
Atualizar Indicador de Utilização do Saldo (19.3-A.2.2.3 IN45/98) (IND_UTIL_DEV_ZERA) para “S”, do registro da ocorrência de devolução da entrada que zerou a quantidade final.
Senão:
Mantém a regra atual Saldo Inicial = Saldo Final do dia anterior (que no caso é zero).
Cravar zero!
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = 0
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = 0
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = 0
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = 0
Os valores do “Saldo Inicial p/ próximo dia c /movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3)” do dia anterior se mantém inalterados.

1.2 - Se o dia corrente não possui Movimentações de Entradas, Devoluções de Entradas e Devoluções de Saídas (QTD_CONV_ENT_MP = 0 e QTD_CONV_DEV_SAI_MP = 0 e QTD_CONV_DEV_ENT_MP =0):
Mantém a regra atual Saldo Inicial = Saldo Final do dia anterior (que no caso é zero).
Cravar zero!
- Qtde Total Convertida Inicial (QTD_CONV_INI) = 0
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = 0
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = 0
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = 0
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = 0

2 - Para Quantidade Final (QTD_CONV_FIM) do dia imediatamente anterior Diferente de Zero, proceder:
MFS92151: Subtrair a Quantidade das Saídas do Dia anterior do Saldo Final, para compor o Saldo Inicial (19.3-A.2.2 – “a”)
MFS99147:Só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior (continuação da MFS92151):
2.1 - Se o dia corrente possui pelo menos uma Movimentação de Entrada, Devolução de Entrada ou Devolução de Saída (QTD_CONV_ENT_MP <>0 ou QTD_CONV_DEV_SAI_MP <> 0 ou QTD_CONV_DEV_ENT_MP <>0):
Compor a Quantidade Inicial com a Quantidade Final menos quantidade de saídas do dia anterior.
Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo (Cálculo da Média Ponderada)” = ‘N’:
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM) -
- Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP)
Se Quantidade Inicial calculada ficar negativa, exibir a seguinte mensagem de aviso no log da geração:
Cálculo da Média Ponderada Móvel: Valor do Saldo Inicial calculado a partir da movimentacao de saidas, resultou em negativo. Veja os campos <Qtde (Saida do Dia)> e <Qtde Final> do dia anterior no Relatorio de Calculo de Media Ponderada. Dados de Identificação: Empresa: xxx - Estab: xx – Período: 99/99/9999 - Produto(ind/cód) x-xxx – Dia DD/MM/AAAA
Zera a quantidade de saídas anteriores pois foram utilizadas (Qtde Saída a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP)).
Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo (Cálculo da Média Ponderada)” = ‘S’:
- Se Qtde total Convetida Final (QTD_CONV_FIM) >= Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) Então:
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM) -
- Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP)
- Qtde Saída a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) = 0  à Zera a quantidade de saídas anteriores pois foi utilizada por completo.
- Se Qtde total Convetida Final (QTD_CONV_FIM) < Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) Então:
- Qtde Total Convertida Inicial (QTD_CONV_INI) = 0
- Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) = Qtde Saídas a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP) -
- Qtde total Convetida Final (QTD_CONV_FIM)
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP)
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP)
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP

2.2 - Se o dia corrente não possui Movimentações de Entradas, Devoluções de Entradas e Devoluções de Saídas (QTD_CONV_ENT_MP = 0 e QTD_CONV_DEV_SAI_MP = 0 e QTD_CONV_DEV_ENT_MP =0):	Mantém a regra para Saldo Inicial = Saldo Final do dia anterior
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Qtde total Convetida Final (QTD_CONV_FIM)
MFS94561: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP)
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP)
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = QTD_CONV_INI * Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP

Mantém a quantidade de saídas anteriores pois não forem utilizadas (Qtde Saída a deduzir p/ próximo dia c/ movimento (QTD_CONV_SAI_MP))



- Primeiro Dia do mês da geração:
Para o Primeiro Dia do mês da geração, calcular o saldo inicial do dia considerando:
- Quantidade Tabela do Inventário (X52_INVENT_PRODUTO) do último dia do mês anterior;
- Os Valores Unitários Médios da Tabela do Inventário ou da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND) do último dia do mês anterior;
[MFS69798]
A quantidade sempre deverá ser recuperada da Tabela do Inventário. Já os valores Unitários Médios, depende se a geração do mês anterior foi realizada ou não.  Ou seja:
Se o produto sujeito a ICMS-ST possui registro para o último dia do mês anterior na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários”
(EST_ST_RS_MEDIA_POND), então:
Considerar os Valores Unitários Médios do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Senão:
Considerar os Valores Unitários Médios do Inventário (X52_INVENT_PRODUTO) do último dia do mês anterior.

Calculando o Saldo Inicial do dia:
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Quantidade do Inventário Convertida (X52_INVENT_PRODUTO)

- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP):
- Se produto possui média calculada para o último dia do mês anterior, então:
- [Quantidade do Inventário Convertida * Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP - EST_ST_RS_MEDIA_POND)]
- Senão
- [Quantidade do Inventário Convertida * Valor de ICMS Médio (VLR_ICMS_MEDIO - X52_INVENT_PRODUTO)].

- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP):
- Se produto possui média calculada para o último dia do mês anterior, então:
- [Quantidade do Inventário Convertida * Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP –
- EST_ST_RS_MEDIA_POND)]
- Senão
- [Quantidade do Inventário Convertida * (Valor de ICMS-ST Médio (VLR_ICMSS_MEDIO) - Valor FECEP Médio (VLR_FCP_MEDIO))]
- Onde VLR_ICMSS_MEDIO e VLR_FCP_MEDIO são campos oriundos da X52_INVENT_PRODUTO.
- [MFS84145] Alteração no cálculo do campo Valor de ICMS-ST Médio, para abater o valor do FECEP Médio quando a origem for da SAFX52.
Quando o resultado do cálculo do Valor do ICMS-ST médio - Valor FECEP Médio, resultar em um valor negativo, será gravada a seguinte mensagem de erro no log:
 “Cálculo da Média Ponderada Móvel: Valor do ICMS-ST Calculado Inicial gerado a partir da subtração dos campos <Valor ICMS-ST Médio> pelo <Valor Fecep Médio> do Inventário, resultou em valor negativo.  Favor rever o Inventário do Produto (SAFX52) de forma a adicionar o Fecep ao valor do ICMS-ST carregado no campo <Valor ICMS-ST Médio>.”
Dados de Identificação: Empresa: xxx - Estab: xx – Período: 99/99/9999 - Produto(ind/cód) x-xxx

- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP):
- Se produto possui média calculada para o último dia do mês anterior, então:
- [Quantidade do Inventário Convertida * Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP –
- EST_ST_RS_MEDIA_POND)]
- Senão
- [Quantidade do Inventário Convertida * Valor Base ICMS-ST Médio (VLR_BASE_ICMSS_MEDIO - X52_INVENT_PRODUTO)].

- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP):
- Se produto possui média calculada para o último dia do mês anterior, então:
- [Quantidade do Inventário Convertida * Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP - EST_ST_RS_MEDIA_POND)]
- Senão
- [Quantidade do Inventário Convertida * Valor FECEP Médio (VLR_FCP_MEDIO - X52_INVENT_PRODUTO)].

[MFS89648] (19.3-A.2.2.2 da IN-045/98) - Tratamento para Valor Médio Ponderado Negativo:
Verificar se Valor Médio Unitário da Base de Cálculo do ICMS-ST do último dia do mês anterior é negativo. Para isso considerar o VLR_UNIT_BC_ST_FIM_MP da EST_ST_RS_MEDIA_POND, caso o produto possua média calculada para o último dia do mês anterior. Caso contrário, considerar o VLR_BASE_ICMSS_MEDIO da X52_INVENT_PRODUTO.
Caso o “Valor Médio Unitário da Base de Cálculo do ICMS-ST” recuperado do último dia do mês anterior for negativo, então:
O Saldo Inicial do primeiro dia do mês será zero.
- Qtde Total Convertida Inicial (QTD_CONV_INI) = Quantidade do Inventário Convertida (X52_INVENT_PRODUTO)
- Valor do ICMS Calculado Inicial (VLR_ICMS_INI_MP) = 0
- Valor do ICMS-ST Calculado Inicial (VLR_ICMS_ST_INI_MP) = 0
- Valor Base de Cálculo do ICMS-ST Calculado Inicial (VLR_BC_ST_INI_MP) = 0
- Valor FECEP-ST Calculado Inicial (VLR_FECEP_ST_INI_MP) = 0

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.
[MFS90131] Arredondar para 8 casas decimais o resultado dos cáculos (qtde x valores unitários)

Recuperação dos Valores Unitários Médios da Tabela do Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND)
Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data igual ao último dia do mês anterior que está sendo processado;

- O produto deve constar na parametrização do menu “Parâmetros à Produtos à Por Código”, ou, seu NCM deve estar parametrizado no menu “Parâmetros à Produtos à Por NCM”, ou, seu CEST deve estar parametrizado no menu “Parâmetros à Produtos à Por CEST”.

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
- Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP)
- Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP)
- Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP)
- Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP)


Recuperação da Quantidade e Valores Unitários Médios da Tabela de Inventário (X52_INVENT_PRODUTO)
Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do Inventário (X52_INVENT_PRODUTO).
Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior que está sendo processado;

- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;

- Grupo Contagem (campo 04 - GRUPO_CONTAGEM) à 1, 2, 3 e 5;

- O produto deve constar na parametrização do menu “Parâmetros à Produtos à Por Código”, ou, seu NCM deve estar parametrizado no menu “Parâmetros à Produtos à Por NCM”, ou, seu CEST deve estar parametrizado no menu “Parâmetros à Produtos à Por CEST”.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”. Ao verificar a parametrização por código, basta considerar o produto “principal”. Pois conforme já explicado, as informações do inventário estão registradas em nome do produto “principal” (ESP_SP_PROD_ST).

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada.
-Caso não, é verificado se o NCM do produto (NCM do cadastro do produto) consta na parametrização da opção “Por NCM”.
-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada.
-Caso não, é verificado se o CEST do produto (CEST do cadastro do produto) consta na parametrização da opção “Por CEST”.
[MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar o inventário de Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o inventário:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto do inventário estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código


Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto. Caso isso ocorra, recuperar registro a registro, individualmente. Considerar as seguintes informações:
- 12 - Unidade de Medida (COD_MEDIDA)
- 13 - Quantidade de Inventário (QUANTIDADE)
- 21 - Valor de ICMS Médio (VLR_ICMS_MEDIO)
- 22 - Valor de ICMS-ST Médio (VLR_ICMSS_MEDIO)
- 43 - Valor Base ICMS-ST Médio (VLR_BASE_ICMSS_MEDIO)
- 44 - Valor FECEP Médio (VLR_FCP_MEDIO)
Calcular a quantidade convertida:
- Qtde total Convetida Final:
Campo 13-Quantidade de Inventário, aplicando a conversão, quando necessário. Veja:
Se unidade do inventário (*) = unidade do cadastro do produto (**)
(*) unidade do inventário = campo “12-Unidade de Medida” da SAFX52
(**) unidade do produto = campo “14-Código de Medida” da SAFX2013
Nesse caso não há necessidade de conversão, e o campo será a própria quantidade do inventário;
Senão
Nesse caso a quantidade do inventário (SAFX52) será convertida para a unidade de medida do cadastro do produto;
[ Quantidade de Inventário (SAFX42) * Fator de Conversão ]
Sobre a conversão de medida:
A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW (menu “Manutenção à Cadastros à Conversão de Unidades de Medida”), da seguinte forma:
- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;
- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:
“Cálculo da Média Ponderada Móvel: Fator de conversão de medida de XXX para XXX não encontrado. Não foi possível calcular o Saldo inicial do dia “XX” para o produto.
(O primeiro “XXX” é a unidade do inventário, e o segundo “XXX”, a unidade do cadastro do produto).
Dados de Indentificação: Estabelecimento: xx -  Produto(ind/cód) x-xxx – Grupo Contagem: x – Natureza de Estoque: xx



### 2º Passo – Calcular o Total das Devoluções de Saídas do Dia

Nesse passo as devoluções de saídas do dia serão recuperadas a partir da tabela EST_ST_RS_NF_DEV_SAI.

Origem dos dados: - Tabela Específica resultante da Geração do Movimento de Devolução das Saídas (EST_ST_RS_NF_DEV_SAI).
Vide MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Saidas.docx

Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Escrita Fiscal - DIA que está sendo processado;

Recuperar as seguintes informações:
- Produto da NF de Devolução (GRUPO_PROD_NF_DEV, IND_PROD_NF_DEV, COD_PROD_NF_DEV)
- Produto Principal (GRUPO_PROD_PRINC, IND_PROD_PRINC, COD_PROD_PRINC)
- Quantidade Devolvida Convertida (QTD_CONV_DEV_SAI_MP)
- Valor do ICMS Calculado para Devolução (VLR_ICMS_DEV_SAI_MP)
- Valor do ICMS-ST Calculado para Devolução (VLR_ICMS_ST_DEV_SAI_MP)
- Valor Base de Cálculo do ICMS-ST Calculado para Devolução (VLR_BC_ST_DEV_SAI_MP)
- Valor FECEP-ST Calculado para Devolução (VLR_FECEP_ST_DEV_SAI_MP)
Somarizar a quatindade e os valores recuperados acima por Produto: considerar o Produto Principal, caso este esteja preenchido, e o Produto da NF de Devolução caso o Principal não esteja preenchido.


### 3º Passo: Calcular o Total das Entradas do Dia

Nesse passo as entradas do dia serão recuperadas a partir da tabela EST_ST_RS_NF_ENT.

Origem dos dados: - Tabela Específica resultante da Geração do Movimento de Entradas (EST_ST_RS_NF_ENT).
Vide MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Entradas.docx

Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Escrita Fiscal - DIA que está sendo processado;

Recuperar as seguintes informações:
- Produto da NF (GRUPO_PROD_NF, IND_PROD_NF, COD_PROD_NF)
- Produto Principal (GRUPO_PROD_PRINC, IND_PROD_PRINC, COD_PROD_PRINC)
- Quantidade Entrada Convertida (QTD_CONV_ENT_MP)
- Valor do ICMS Calculado para Entrada (VLR_ICMS_ENT_MP)
- Valor do ICMS-ST Calculado para Entrada (VLR_ICMS_ST_ENT_MP)
- Valor Base de Cálculo do ICMS-ST Calculado para Entrada (VLR_BC_ST_ENT_MP)
- Valor FECEP-ST Calculado para Entrada (VLR_FECEP_ST_ENT_MP)
Somarizar a quatindade e os valores recuperados acima por Produto: considerar o Produto Principal, caso este esteja preenchido, e o Produto da NF caso o Principal não esteja preenchido.


### 4º Passo: Calcular o Total das Devoluções de Entradas do Dia

Nesse passo as devoluções de entradas do dia serão recuperadas a partir da tabela EST_ST_RS_NF_DEV_ENT.

Origem dos dados: - Tabela Específica resultante da Geração do Movimento de Devolução das Entradas (EST_ST_RS_NF_DEV_ENT).
Vide MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Entradas.docx

Critérios:
- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Escrita Fiscal - DIA que está sendo processado;

Recuperar as seguintes informações:
- Produto da NF de Devolução (GRUPO_PROD_NF_DEV, IND_PROD_NF_DEV, COD_PROD_NF_DEV)
- Produto Principal (GRUPO_PROD_PRINC, IND_PROD_PRINC, COD_PROD_PRINC)
- Quantidade Devolvida Convertida (QTD_CONV_DEV_ENT_MP)
- Valor do ICMS Calculado para Devolução (VLR_ICMS_DEV_ENT_MP)
- Valor do ICMS-ST Calculado para Devolução (VLR_ICMS_ST_DEV_ENT_MP)
- Valor Base de Cálculo do ICMS-ST Calculado para Devolução (VLR_BC_ST_DEV_ENT_MP)
- Valor FECEP-ST Calculado para Devolução (VLR_FECEP_ST_DEV_ENT_MP)
Somarizar a quatindade e os valores recuperados acima por Produto: considerar o Produto Principal, caso este esteja preenchido, e o Produto da NF de Devolução caso o Principal não esteja preenchido.


### 5º Passo: Calcular o Saldo Final do Dia e Gravar a tabela EST_ST_RS_MEDIA_POND

Para cada Produto sujeito ao ICMS-ST(*), gravar um registro na tabela com os valores calculados no dia: Saldo Inicial, Total das Devoluções de Saídas, Total das Entradas, Total das Devoluções de Entradas e Saldo Final.

(*) Produto sujeito ao ICMS-ST(*) são os produtos cujo CÓDIGO ou NCM ou CEST esteja parametrizado numa mas opções de menu “Parâmetros à Produtos à Por Código”, ou, “Parâmetros à Produtos à Por NCM”, ou, “Parâmetros à Produtos à Por CEST”, com a data de validade da parametrização  acordo com o período informado na tela da geração.

Observação: Caso as consultas descritas nos passos (1, 2, 3, 4) não retornarem registros para o Produto sujeito ao ICMS-ST(*), gravar a tabela EST_ST_RS_MEDIA_POND com os campos relacionados zerados.  Esse passo é importante, pois o mês pode começar sem inventário e movimento, mas no meio do mês pode iniciar um movimento. A tabela deve possuir um registro pra cada dia do mês. (Veja tópico 4 – que é executado ao final do processamento do período para o produto)


Tabela EST_ST_RS_MEDIA_POND

Os campos sinalizados com asterisco compõem a chave da tabela.


[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados devem ser arredondados, não devem ser truncados.

## Relatório de Conferência

Gerar um arquivo excel a partir da leitura da tabela EST_ST_RS_MEDIA_POND
Nome do arquivo: Relatório_Conferencia_Calculo_Media_Ponderada_mm_aaaa_cod_estab.xlsx

As quantidades e valores (Saldo Inicial, Devolução, Entrada, Saldo final...) serão demonstrados em linhas e não por coluna. Logo por dia/produto serão apresentadas as linhas identificadas pela descrição:
- Saldo Inicial
- Devolução de Saída (+)
- Entrada (+)
- Devolução de Entrada (-)
- Saldo Final (Total Dia)
- Valores Unitários Médios
- Qtde Saída do Dia
- Qtde Saída a deduzir p/ próximo dia c/ movimento
- Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3)

As colunas que compõe o relatório são as seguintes:

Exemplo:


## Tratamento para Produtos não Movimentados:


Ao final do processamento do período, é necessário verificar se o produto sujeito a ST, gravado na tabela EST_ST_RS_MEDIA_POND, possui pelo menos um dia com um dos valores (saldo inicial, devolução de saída, entrada, devolução de entrada) diferente de zero.
Se todos os valores estiverem zerados para todos os dias do período e estabelecimento da geração, esse produto não deve constar na tabela EST_ST_RS_MEDIA_POND. Isso demonstra que o produto foi apenas parametrizado e não foi movimentado nem possui inventário para o estabelecimento e período da geração.
É importante excluir os produtos não movimentados da tabela EST_ST_RS_MEDIA_POND ao final do processamento, para evitar que num período subsequente ele seja movimentado e o Saldo Inicial não seja recuperado corretamente da Tabela do Inventário (X52_INVENT_PRODUTO), por existir registro na EST_ST_RS_MEDIA_POND do período anterior (vide 1º passo).


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS48753 | Liliane Videira Assaf | Criação da funcionalidade. Esta entrega não estão sendo contemplados: - Parametrização com Produtos Associados | 22/12/2020 |
| MFS66171 | Liliane Videira Assaf | Hoje calculamos o campo “Valor Médio Unitário do ICMS-ST” sem FECEP.  Precisamos criar um outro campo para o “Valor Médio Unitário ICMS-ST c/ FECEP”. E renomear o campo “Valor Médio Unitário do ICMS-ST” para “Valor Médio Unitário ICMS-ST s/ FECEP”. | 07/06/2021 |
| MFS69798 | Liliane Videira Assaf | Correção no cálculo do Saldo Inicial do primeiro dia do Mês, para sempre considerar a quantidade do inventário do último dia do mês anterior. Erradamente estava sendo considerada a quantidade da tabela de média ponderada do último dia do mês anterior. | 03/08/2021 |
| MFS72212 | Liliane Videira Assaf | Criação do Cálculo dos Valores Unitários Médios do Inventário. | 09/09/2021 |
| MFS72429 | Andréa Rocha | Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados.  Conforme informação passada pela SEFAZ/RS. | 30/09/2021 |
| MFS81749 | Liliane Assaf | Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473 | 15/03/2022 |
| MFS84145 | Andréa Rocha | Alteração no cálculo do Saldo Inicial para o campo Valor de ICMS-ST Médio, para abater o valor do FECEP Médio incluído no valor do ICMS-ST Médio, quando a origem dos dados for da tabela do Inventário por Produto | 11/04/2022 |
| MFS90131 | Liliane Assaf | Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte. | 01/08/2022 |
| MFS89648 | Liliane Assaf | Atualização legal IN55/22: Alteração no Saldo Inicial para tratar dois cenários: - Valor Médio Ponderado Móvel calculado ao final do dia anterior negativo (19.3-A.2.2.2) - Quantidade final do dia anterior zerada (19.3-A.2.2.3 da IN-045/98) | 10/08/2022 |
| MFS92151 | Liliane Assaf | Tratamento do Saldo Inicial para deduzir a quantidade das saídas do dia anterior (tópico 19.3-A.2.2 – “a”) | 17/08/2022 |
| MFS94561 | Liliane Assaf | Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Unitário Médio Ponderado. Pendência (MFS-97582): Melhorar a conferência dos valores no relatório da média ponderada. | 01/11/2021 |
| MFS99147 | Liliane Assaf | Ajuste na regra do Saldo Inicial do Dia que deduz a quantidade de saídas do dia anterior, para tratar o cenário de saídas sem estoque (Quantidade das Saídas > quantidade saldo final do dia anterior). Correção da regra criada pela MFS92151. Para isso foi criado o Parâmetro na tela de Dados Iniciais “Tratamento p/ saídas com quantidades não acobertadas pelo saldo (Cálculo da Média Ponderada)” Se o parâmetro estiver marcado, só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior. | 19/12/2022 |


| PK | Campo |  | Regra de Preenchimento | Campos para relatório |
| --- | --- | --- | --- | --- |
| (*) | Código do Estabelecimento | COD_ESTAB | Código do estabelecimento SELECIONADO na tela de geração | Não apresentar |
| (*) | Código da Empresa | COD_EMPRESA | Código da empresa da nota de Entrada (SAFX07) | Cod Empresa |
| (*) | Código do Estabelecimento | COD_ESTAB_ORIG | Código do estabelecimento do inventário/movimento recuperado nos passos anteriores. | Cod Estab |
| (*) | Data | DATA | Dia que está sendo processado. | Dia |
| (*) | Produto | Grupo_Produto, Ind_Produto, Cod_Produto | Produto sujeito ao ICMS-ST (*) | Ind-Cod Produto |
| Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia |  |
|  | Qtde total Convetida Inicial | QTD_CONV_INI | “Qtde total Convetida Inicial” calculada no 1º Passo; | Qtde Inicial |
|  | Valor do ICMS Calculado Inicial | VLR_ICMS_INI_MP | “Valor do ICMS Calculado Inicial” calculado no 1º Passo; [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide 1º passo). | Valor ICMS Inicial |
|  | Valor do ICMS-ST Calculado Inicial | VLR_ICMS_ST_INI_MP | “Valor do ICMS-ST Calculado Inicial” calculado no 1º Passo; [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide 1º passo). | Valor ICMS-ST Inicial |
|  | Valor Base de Cálculo do ICMS-ST Calculado Inicial | VLR_BC_ST_INI_MP | “Valor Base de Cálculo do ICMS-ST Calculado Inicial” calculado no 1º Passo; [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide 1º passo). | Valor Base de Cálculo do ICMS-ST Inicial |
|  | Valor FECEP-ST Calculado Inicial | VLR_FECEP_ST_INI_MP | “Valor FECEP-ST Calculado Inicial” calculado no 1º Passo; [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide 1º passo). | Valor FECEP-ST Inicial |
| Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia |  |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_SAI_MP | “Quantidade Devolvida Convertida” recuperada no 2º Passo; | Qtde (Devolução Saída) |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_SAI_MP | “Valor do ICMS Calculado para Devolução” recuperado no 2º Passo; | Valor ICMS (Devolução Saída) |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_SAI_MP | “Valor do ICMS-ST Calculado para Devolução” recuperado no 2º Passo; | Valor ICMS-ST (Devolução Saída) |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_SAI_MP | “Valor Base de Cálculo do ICMS-ST Calculado para Devolução” recuperado no 2º Passo; | Valor Base de Cálculo do ICMS-ST (Devolução Saída) |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_SAI_MP | “Valor FECEP-ST Calculado para Devolução” recuperado no 2º Passo; | Valor FECEP-ST (Devolução Saída) |
| Entradas do Dia | Entradas do Dia | Entradas do Dia | Entradas do Dia |  |
|  | Quantidade Entrada Convertida | QTD_CONV_ENT_MP | “Quantidade Entrada Convertida” recuperada no 3º Passo; | Qtde (Entrada) |
|  | Valor do ICMS Calculado para Entrada | VLR_ICMS_ENT_MP | “Valor do ICMS Calculado para Entrada” recuperado no 3º Passo; | Valor ICMS (Entrada) |
|  | Valor do ICMS-ST Calculado para Entrada | VLR_ICMS_ST_ENT_MP | “Valor do ICMS-ST Calculado para Entrada” recuperado no 3º Passo; | Valor ICMS-ST (Entrada) |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Entrada | VLR_BC_ST_ENT_MP | “Valor Base de Cálculo do ICMS-ST Calculado para Entrada” recuperado no 3º Passo; | Valor Base de Cálculo do ICMS-ST (Entrada) |
|  | Valor FECEP-ST Calculado para Entrada | VLR_FECEP_ST_ENT_MP | “Valor FECEP-ST Calculado para Entrada” recuperado no 3º Passo; | Valor FECEP-ST (Entrada) |
| Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia |  |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_ENT_MP | “Quantidade Devolvida Convertida” recuperada no 4º Passo; | Qtde (Devolução Entrada) |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_ENT_MP | “Valor do ICMS Calculado para Devolução” recuperado no 4º Passo; | Valor ICMS (Devolução Entrada) |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_ENT_MP | “Valor do ICMS-ST Calculado para Devolução” recuperado no 4º Passo; | Valor ICMS-ST (Devolução Entrada) |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_ENT_MP | “Valor Base de Cálculo do ICMS-ST Calculado para Devolução” recuperado no 4º Passo; | Valor Base de Cálculo do ICMS-ST (Devolução Entrada) |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_ENT_MP | “Valor FECEP-ST Calculado para Devolução” recuperado no 4º Passo; | Valor FECEP-ST (Devolução Entrada) |
| Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia |  |
|  | Qtde total Convetida Final | QTD_CONV_FIM | QTD_CONV_INI + QTD_CONV_DEV_SAI_MP + QTD_CONV_ENT_MP - QTD_CONV_DEV_ENT_MP [MFS89648] Se Quantidade Final calculada for negativa, exibir a seguinte mensagem de aviso no log da geração: “Cálculo da Média Ponderada Móvel: Quantidade Final calculada negativa. Favor rever a movimentação de devoluções das entradas, pois a quantidade de saídas superou o saldo inicial + entradas do dia. Dados de Identificação: Empresa: xxx - Estab: xx – Período: 99/99/9999 - Produto(ind/cód) x-xxx – Dia DD/MM/AAAA | Qtde Final |
|  | Valor do ICMS Calculado Final | VLR_ICMS_FIM_MP | VLR_ICMS_INI_MP + VLR_ICMS_DEV_SAI_MP + VLR_ICMS_ENT_MP - VLR_ICMS_DEV_ENT_MP | Valor ICMS Final |
|  | Valor do ICMS-ST Calculado Final | VLR_ICMS_ST_FIM_MP | VLR_ICMS_ST_INI_MP + VLR_ICMS_ST_DEV_SAI_MP + VLR_ICMS_ST_ENT_MP - VLR_ICMS_ST_DEV_ENT_MP | Valor ICMS-ST Final |
|  | Valor Base de Cálculo do ICMS-ST Calculado Final | VLR_BC_ST_FIM_MP | VLR_BC_ST_INI_MP + VLR_BC_ST_DEV_SAI_MP + VLR_BC_ST_ENT_MP - VLR_BC_ST_DEV_ENT_MP | Valor Base de Cálculo do ICMS-ST Final |
|  | Valor FECEP-ST Calculado Final | VLR_FECEP_ST_FIM_MP | VLR_FECEP_ST_INI_MP + VLR_FECEP_ST_DEV_SAI_MP + VLR_FECEP_ST_ENT_MP - VLR_FECEP_ST_DEV_ENT_MP | Valor FECEP-ST Final |
| Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia |  |
|  | Valor Médio Unitário do ICMS | VLR_UNIT_ICMS_FIM_MP | Se QTD_CONV_FIM_MP = 0 então    Preencher com zero. Senão:     Preencher com VLR_ICMS_FIM_MP / QTD_CONV_FIM_MP (*) [MFS90131] arredondar para 8 casas decimais o resultado do cálculo.  (*) [MFS94561]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado. | Valor Médio Unitário ICMS |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP [MFS66171] | VLR_UNIT_ICMS_ST_FIM_MP | Se QTD_CONV_FIM_MP = 0 então    Preencher com zero. Senão:    Preencher com VLR_ICMS_ST_FIM_MP / QTD_CONV_FIM_MP (*) [MFS90131] arredondar para 8 casas decimais o resultado do cálculo. (*) [MFS94561]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado. | Valor Médio Unitário ICMS-ST s/ FECEP |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP [MFS66171] | VLR_UNIT_ICMS_ST_FECEP_FIM_MP | Se QTD_CONV_FIM_MP = 0 então    Preencher com zero. Senão:    Preencher com:   (VLR_ICMS_ST_FIM_MP + VLR_FECEP_ST_FIM_MP) / QTD_CONV_FIM_MP (*) [MFS90131] arredondar para 8 casas decimais o resultado do cálculo. (*) [MFS94561]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado. | Valor Médio Unitário ICMS-ST c/ FECEP |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST | VLR_UNIT_BC_ST_FIM_MP | Se QTD_CONV_FIM_MP = 0 então    Preencher com zero. Senão:    Preencher com VLR_BC_ST_FIM_MP / QTD_CONV_FIM_MP (*) [MFS90131] arredondar para 8 casas decimais o resultado do cálculo. [MFS89468] os valores médios calculados podem ser negativos. (*) [MFS94561]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado. | Valor Médio Unitário Base de Cálculo do ICMS-ST |
|  | Valor Médio Unitário do FECEP-ST | VLR_UNIT_FECEP_ST_FIM_MP | Se QTD_CONV_FIM_MP = 0 então    Preencher com zero. Senão:    Preencher com VLR_FECEP_ST_FIM_MP / QTD_CONV_FIM_MP (*) [MFS90131] arredondar para 8 casas decimais o resultado do cálculo. (*) [MFS94561]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado. | Valor Médio Unitário  FECEP-ST |
| Saídas | Saídas | Saídas | Saídas | Saídas |
|  | Qtde Saída do dia | QTD_CONV_SAI_DIA | MFS92151: Quantidade de Saídas do Dia Para recuperar as notas e cupons de saídas a partir da regra descrita no documento matriz da Geração dos Movimentos de Saída (MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Saídas.docx). A quantidade deve bater com as quantidades das notas e cupons demonstrados nos registros C185, C380, C480. Lembrando de aplicar a conversão de unidades de medidas caso necessário. | Qtde (Saída do dia) |
|  | Qtde Saída a deduzir p/ próximo dia c/ movimento | QTD_CONV_SAI_MP | MFS92151: Quantidade de saídas que será utilizada para deduzir o estoque do próximo dia em que houver movimentações de entradas e/ou devoluções. Preencher com QTD_CONV_SAI_DIA do dia + QTD_CONV_SAI_MP do dia anterior que não foi utilizada para compor o Saldo Inicial do dia corrente conforme 1º Passo. | Qtde (Saída a deduzir p/ próx dia c/ movimento) |
| Saldo Inicial p/ próximo dia c/ movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) | Saldo Inicial p/ próximo dia c/ movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) | Saldo Inicial p/ próximo dia c/ movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) | Saldo Inicial p/ próximo dia c/ movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) | Saldo Inicial p/ próximo dia c/ movimento (caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Indicador de Utilização do Saldo (19.3-A.2.2.3 IN45/98) | IND_UTIL_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0  Então:    Preencher com “N”. Senão    Não Preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o IND_UTIL_DEV_ZERA anterior para o dia corrente.  Não ter movimentação é quando as quantidades são zero: QTD_CONV_ENT_MP =0, QTD_CONV_DEV_SAI_MP = 0 e QTD_CONV_DEV_ENT_MP = 0. | Saldo utilizado p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3 |
|  | Qtde total Convertida   (19.3-A.2.2.3 IN45/98) | QTD_CONV_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0 Então:   Preencher com QTD_CONV_DEV_ENT_MP do dia. Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar a QTD_CONV_DEV_ZERA anterior para o dia corrente. | Qtde (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Valor do ICMS   (19.3-A.2.2.3 IN45/98) | VLR_ICMS_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0 Então:    Preencher com:    (Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada) * qtde Dev Entrada    Ou seja:    (VLR_UNIT_ICMS_FIM_MP do dia anterior –      (VLR_ICMS_DEV_ENT_MP/ QTD_CONV_DEV_ENT_MP do dia)     ) * QTD_CONV_DEV_ENT_MP do dia Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR_ICMS_DEV_ZERA anterior para o dia corrente. Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o VLR_ICMS_MEDIO da X52_INVENT_PRODUTO, ao invés do VLR_UNIT_ICMS_FIM_MP. | Valor ICMS (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Valor do ICMS-ST s/ FECEP  (19.3-A.2.2.3 IN45/98) | VLR_ICMS_ST_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0 Então:    Preencher com:    (Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada) * qtde Dev Entrada    Ou seja:    (VLR_UNIT_ICMS_ST_FIM_MP do dia anterior –      (VLR_ICMS_ST_DEV_ENT_MP/ QTD_CONV_DEV_ENT_MP do dia)     ) * QTD_CONV_DEV_ENT_MP do dia Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR_ICMS_ST_DEV_ZERA anterior para o dia corrente. Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o (VLR_ICMSS_MEDIO - VLR_FCP_MEDIO) da X52_INVENT_PRODUTO, ao invés do VLR_UNIT_ICMS_ST_FIM_MP. | Valor ICMS-ST s/ FECEP (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Valor do ICMS-ST c/ Fecep  (19.3-A.2.2.3 IN45/98) | VLR_ICMS_ST_FECEP_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0 Então:    Preencher com:    (Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada) * qtde Dev Entrada    Ou seja:    (VLR_UNIT_ICMS_ST_FECEP_FIM_MP do dia anterior –      ((VLR_ICMS_ST_DEV_ENT_MP + VLR_FECEP_ST_DEV_ENT_MP)/         QTD_CONV_DEV_ENT_MP do dia)     ) * QTD_CONV_DEV_ENT_MP do dia Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR_ICMS_ST_FECEP_DEV_ZERA anterior para o dia corrente. Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o (VLR_ICMSS_MEDIO) da X52_INVENT_PRODUTO, ao invés do VLR_UNIT_ICMS_ST_FECEP_FIM_MP. | Valor ICMS-ST c/ FECEP (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Valor Base de Cálculo do ICMS-ST (19.3-A.2.2.3 IN45/98) | VLR_BC_ST_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0  Então:    Preencher com:    (Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada) * qtde Dev Entrada    Ou seja:    (VLR_UNIT_BC_ST_FIM_MP do dia anterior –      (VLR_BC_ST_DEV_ENT_MP/ QTD_CONV_DEV_ENT_MP do dia)     ) * QTD_CONV_DEV_ENT_MP do dia Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar a VLR_BC_ST_DEV_ZERA anterior para o dia corrente. Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o VLR_BASE_ICMSS_MEDIO da X52_INVENT_PRODUTO, ao invés do VLR_UNIT_BC_ST_FIM_MP. | Valor Base de Cálculo do ICMS-ST (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |
|  | Valor FECEP-ST  (19.3-A.2.2.3 IN45/98) | VLR_FECEP_ST_DEV_ZERA | [MFS89648] Se Quantidade Final (QTD_CONV_FIM_MP) = 0 e     Quantidade Devolução de Entrada QTD_CONV_DEV_ENT_MP <> 0  Então:    Preencher com:    (Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada) * qtde Dev Entrada    Ou seja:    (VLR_UNIT_FECEP_ST_FIM_MP do dia anterior –      (VLR_FECEP_ST_DEV_ENT_MP/ QTD_CONV_DEV_ENT_MP do dia)     ) * QTD_CONV_DEV_ENT_MP do dia Senão   Não preencher Se o registro do dia anterior estiver com IND_UTIL_DEV_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR_FECEP_ST_DEV_ZERA anterior para o dia corrente. Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar VLR_FCP_MEDIO da X52_INVENT_PRODUTO, ao invés do VLR_UNIT_FECEP_ST_FIM_MP. | Valor FECEP-ST (Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 - 19.3-A.2.2.3) |


| Coluna | Preenchimento |
| --- | --- |
| Cod Empresa |  |
| Cod Estab |  |
| Dia |  |
| Ind Produto (SAFX2013-01) Cod Produto (SAFX2013-02) |  |
| Descrição da Linha | Saldo Inicial  Devolução de Saída (+) Entrada (+) Devolução de Entrada (-) Saldo Final (Total Dia) Valores Unitários Médios Qtde Saída do Dia Qtde Saída a deduzir p/ próximo dia c/ movimento Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3) A linha (9) deve ser incluída apenas se IND_UTIL_DEV_ZERA for diferente de nulo! [MFS89648] |
| QTDE | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a QTD_CONV_INI; Se Devolução de Saída, demonstrar a QTD_CONV_DEV_SAI_MP Se Entrada, demonstrar a QTD_CONV_ENT_MP Se Devolução de Entrada, demonstrar a QTD_CONV_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar QTD_CONV_FIM Se Valores Unitários Médios, não preencher esse campo; Se Qtde Saída Dia, demonstrar a QTD_CONV_SAI_DIA Se Qtde Saída a deduzir p/ próximo dia c/ movimento, demonstrar a QTD_CONV_SAI_MP [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), não demonstrar QTD_CONV_DEV_ZERA; |
| Valor ICMS | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a VLR_ICMS_INI_MP; Se Devolução de Saída, demonstrar a VLR_ICMS_DEV_SAI_MP  Se Entrada, demonstrar a VLR_ICMS_ENT_MP Se Devolução de Entrada, demonstrar a VLR_ICMS_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar VLR_ICMS_FIM_MP Se Valores Unitários Médios, demonstrar VLR_UNIT_ICMS_FIM_MP; Se Qtde Saída Dia, demonstrar não preencher esse campo; Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo; [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), demonstrar VLR_ICMS_DEV_ZERA; |
| Valor ICMS-ST (s/Fecep) | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a VLR_ICMS_ST_INI_MP; Se Devolução de Saída, demonstrar a VLR_ICMS_ST_DEV_SAI_MP  Se Entrada, demonstrar a VLR_ICMS_ST_ENT_MP Se Devolução de Entrada, demonstrar a VLR_ICMS_ST_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar VLR_ICMS_ST_FIM_MP Se Valores Unitários Médios, demonstrar VLR_UNIT_ICMS_ST_FIM_MP; Se Qtde Saída Dia, demonstrar não preencher esse campo; Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo; [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), demonstrar VLR_ICMS_ST_DEV_ZERA; |
| Valor ICMS-ST (c/Fecep) | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a VLR_ICMS_ST_INI_MP + VLR_FECEP_ST_INI_MP; Se Devolução de Saída, demonstrar a VLR_ICMS_ST_DEV_SAI_MP + VLR_FECEP_ST_DEV_SAI_MP Se Entrada, demonstrar a VLR_ICMS_ST_ENT_MP + VLR_FECEP_ST_ENT_MP Se Devolução de Entrada, demonstrar a VLR_ICMS_ST_DEV_ENT_MP + VLR_FECEP_ST_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar VLR_ICMS_ST_FIM_MP + VLR_FECEP_ST_FIM_MP Se Valores Unitários Médios, demonstrar VLR_UNIT_ICMS_ST_FECEP_FIM_MP; Se Qtde Saída Dia, demonstrar não preencher esse campo; Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo; [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), demonstrar VLR_ICMS_ST_FECEP_DEV_ZERA; |
| Valor Base de Cálculo do ICMS-ST | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a VLR_BC_ST_INI_MP; Se Devolução de Saída, demonstrar a VLR_BC_ST_DEV_SAI_MP; Se Entrada, demonstrar a VLR_BC_ST_ENT_MP Se Devolução de Entrada, demonstrar a VLR_BC_ST_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar VLR_BC_ST_FIM_MP  Se Valores Unitários Médios, demonstrar VLR_UNIT_BC_ST_FIM_MP; Se Qtde Saída Dia, demonstrar não preencher esse campo; Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo; [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), demonstrar VLR_BC_ST_DEV_ZERA; |
| Valor FECEP-ST | Este campo é preenchido conforme a Descrição da Linha. Se Saldo Inicial, demonstrar a VLR_FECEP_ST_INI_MP; Se Devolução de Saída, demonstrar a VLR_FECEP_ST_DEV_SAI_MP  Se Entrada, demonstrar a VLR_FECEP_ST_ENT_MP Se Devolução de Entrada, demonstrar a VLR_FECEP_ST_DEV_ENT_MP Se Saldo Final (Total Dia), demonstrar VLR_FECEP_ST_FIM_MP Se Valores Unitários Médios, demonstrar VLR_UNIT_FECEP_ST_FIM_MP; Se Qtde Saída Dia, demonstrar não preencher esse campo; Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo; [MFS89648] Se Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3), demonstrar VLR_FECEP_ST_DEV_ZERA; |


| Cod Empresa | Cod Estab | Dia | Ind-Cod Produto | Descrição da Linha | QTDE | Valor ICMS | Valor ICMS-ST (s/Fecep) | Valor ICMS-ST (c/Fecep) | Valor Base de Cálculo do ICMS-ST | Valor FECEP-ST |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (1) Saldo Inicial | 10 | 100 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (2) Devolução de Saída (+) | 10 | 100 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (3) Entrada (+) | 10 | 100 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (4) Devolução de Entrada (-) | 10 | 100 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (5) Saldo Final (Total Dia) | 20 | 200 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (6) Valores Unitarios Médios |  | 10 |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (7) Qtde Saída do Dia |  |  |  |  |  |  |
| 21 | 162148 | 01/02/2022 | 1-001-000000175 | (8) Qtde Saída a deduzir p/ próximo dia c/ movimento |  |  |  |  |  |  |
|  |  |  |  | (9) Saldo Inicial p/ próximo dia c/ movimento (IN45/98 - 19.3-A.2.2.3) |  |  |  |  |  |  |
