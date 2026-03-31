# MTZ-Ressarc-RS-IN087_2020_Geracao_Transferência_Entre_Estabelecimentos

> Fonte: MTZ-Ressarc-RS-IN087_2020_Geracao_Transferência_Entre_Estabelecimentos.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Transferência Entre Estabelecimentos



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração  IN-RE 087/20  Geração das Transferências entre Estabelecimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
1.1	Visão de Cadeia de Transferência	1
1.2	Ciclos em Cadeia de transferências	1
1.3	Pré-requisito	1
1.4	Base Legal	1
2.	Parâmetros da Tela	1
3.	Críticas	1
4.	Processamento	1
4.1 Visão Resumida do Processamento	1
4.2 Montagem das Cadeias de Transferência	1
1º Passo – Recuperar os Estabelecimentos que receberam notas de transferência de estabelecimentos do RS:	1
2º Passo – Gravação da Tabela de Cadeia de Transferência (EST_ST_RS_ESTAB_TRANSF)	1
4.3 Processamento das Cadeias de Transferência	1
1º Passo – Recuperar os Valores Médios Unitários do Estabelecimento Origem (PFJ):	1
2º Passo – Atualizar as Notas de Entradas recebidas por Transferência no Estabelecimento Destino – C180:	1
3º Passo – Atualizar as Notas de Devolução das Entradas recebidas por Transferência no Estabelecimento Destino – C186:	1
4º Passo – Recalcular os Médios Unitários, Dev. Saídas e Saídas, do Dia da Transferência em diante no Estabelecimento Destino:	1
5.	Relatório	1


## Introdução


Essa rotina tem como objetivo atualizar os valores unitários do ICMS, BC-ST, ICMS-ST e FECEP-ST dos movimentos de entrada de operações de transferências oriundas dos estabelecimentos da empresa, com os valores médios unitários calculados pelo estabelecimento remetente dessa operação. A movimentação de entrada estão gravados tabela EST_ST_NF_ENT (tabela específica do módulo do Ressarcimento RS, gravada com o resultado do processo de Geração dos Movimentos).

A atualização os valores unitários de um movimento de entrada impacta na devolução dessa entrada (se houver) e a média ponderada do dia e produto transferido. Uma vez a média ponderada atualizada, há necessidade de refazer as Devoluções das Saídas e o Movimento de Saída.
Ou seja, a atualização dos valores médios do movimento de entrada por transferência força o reprocessamento as seguintes rotinas, considerando o produto transferido e período igual ao dia da emissão da transferência até o último dia do mês:
- Geração do Movimento de Devolução de Entrada, relacionada a NF de entrada de transferência (C186)
- Geração do Movimento de Devolução de Saída (C181)
- Cálculo dos Valores Médios Ponderados
- Geração do Movimento de Saída (C185, C380, C480).

### Visão de Cadeia de Transferência


A CADEIA É UMA “FOTO” DAS TRANSFERÊNCIAS DE UM PRODUTO NUM DIA.

Como num determinado dia, um produto pode ser transferido entre vários estabelecimentos da empresa, os estabelecimentos formam uma cadeia de transferência, onde é necessário processá-los em ordem, do primeiro ao último estabelecimento da cadeia. Podemos classificar os estabelecimentos que compões uma cadeia com as seguintes nomenclaturas:
- Estabelecimento Inicial (Nó Raiz): aquele que não recebe, só emite nota de transferência do produto no dia.
- Estabelecimentos intermediários: aquele que recebe e emite nota de transferência do produto no dia.
- Estabelecimento Final (Nó folha): aquele que só recebe, não emite nota de transferência do produto no dia

Exemplo:
1)  Estabelecimento A transfere um produto para o Estabelecimento B.

- Estabelecimento Inicial (Nó Raiz): A
- Estabelecimento Final (Nó folha): B
A nota de entrada do estabelecimento B deve ser atualizada com os valores médios unitários calculados no estabelecimento A. Os valores unitários são oriundos do Cálculo da Média Ponderada do estabelecimento A, do produto e dia da transferência.

2) No exemplo abaixo, temos duas cadeias, uma iniciada no estabelecimento E, outra iniciada no estabelecimento A.

Cadeia de Transferência E:
- Estabelecimento Inicial (Nó Raiz): E
- Estabelecimentos intermediários: C, D
- Estabelecimento Final (Nó folha): F, G

Cadeia de Transferência A:
- Estabelecimento Inicial (Nó Raiz): A
- Estabelecimentos intermediários: B, C, D
- Estabelecimento Final (Nó folha): G

Toda a cadeia de transferência é armazenada na tabela interna (EST_ST_RS_ESTAB_TRANSF), onde para cada transferência, um registro é gravado com a identificação dos estabelecimentos origem (emissor) e destino (receptor), o estabelecimento Início da cadeia (nó raiz) e o nível do estabelecimento de origem.
Vejam como são carregadas as Cadeias de Transferência E e A do exemplo acima:



Percorrendo a Cadeia de Transferência de E:
As notas fiscais de transferência recebida por F e C, emitidas pelo estabelecimento E, serão atualizadas com os valores unitários médios calculados no estabelecimento E. A nota fiscal de transferência recebida por D emitida por C, será atualizada com os valores médios calculados em C. A nota fiscal de transferência recebida por G emitida por D, será atualizada com os valores médios calculados em D.

Percorrendo a Cadeia de Transferência de A:
A nota fiscal de transferência recebida por B emitida por A, será atualizada com os valores médios calculados em A. A nota fiscal de transferência recebida por C emitida por B, será atualizada com os valores médios calculados em B. A nota fiscal de transferência recebida por D emitida por C, será atualizada com os valores médios calculados em C. A nota fiscal de transferência recebida por G emitida por D, será atualizada com os valores médios calculados em D.

Uma vez que o estabelecimento receptor da transferência teve sua(s) nota(s) fiscal de transferência(s) atualizada(s), é necessário atualizar a nota de devolução dessa entrada (caso exista) e recalcular os valores unitários médios do produto, a começar pelo o dia da transferência até o último dia do mês. E consequentemente regerar os movimentos de Devolução de Saída (C181) e Saída (C185, C380, C480) desse dia em diante.

Ordem de Processamento dos Estabelecimentos:
Para cada dia e produto podemos ter várias cadeias de transferência entre estabelecimentos, que devem ser processadas começando pelo estabelecimento de menor nível para os de maior nível.

### Ciclos em Cadeia de transferências

Nos exemplos a seguir temos um problema de loop na cadeia (A > B > C > D > A) pois não existe estabelecimento fim da cadeia. Todos os estabelecimentos são emissores e receptores de transferência para um produto/dia.  Para essa situação será emitido mensagem de erro no log da geração e a cadeia não será processada.


### Pré-requisito

a) Todos os estabelecimentos do RS da empresa devem ter executado o processo de Geração do Movimento.

Referências das Tabelas Internas gravadas nos processos de Geração do Movimento e Transferência para EFD Fiscal:



b) As notas de entrada serão consideradas como de transferência, quando o CNPJ da Pessoa Fis/Jur da nota for um CNPJ presente no cadastro dos estabelecimentos da empresa. Não utilizaremos o Indicador de Pessoa Física/Jurídica (IND_FIS_JUR da SAFX04) = ‘3’ e sim o campo 06 (CFP_CGC) da SAFX04 = CNPJ do Estabelecimento.

### Base Legal

IN RE 045/98, tópico 19.3-A.2.1.2.2

19.3-A.2.1.2.2 -
Na hipótese de operação de transferência de mercadorias realizada entre estabelecimentos do contribuinte, as informações apresentadas para fins de escrituração de saídas pelo remetente e de entradas pelo destinatário, deverão utilizar o valor médio ponderado móvel unitário calculado ao final do dia da remessa no estabelecimento remetente, independentemente do valor informado conforme subitem 19.3-A.2.1.2. (Acrescentado pela IN RE 055/22, de 27/06/22. (DOE 29/06/22) - Efeitos a partir de 29/06/22 – Aj. SINIEF 02/09 e Al. "b", nota 02, II, art. 25-B, Livro III do Decreto 37.699/97.)





## Parâmetros da Tela



Período: MM/AAAA

[  ] Utilizar DATA MART para períodos anteriores

[  ] Gerar Relatórios de Conferência


Funcionamento dos campos:




## Críticas


As situações abaixo geram mensagem de aviso no relatório de logs, não interrompendo o processo da geração.
- Estabelecimento sem realizar a Geração do Movimento.
- Existência de loop na cadeia de transferência entre estabelecimentos.


Verificar se a Geração dos Movimentos foi realizada:
Verificar se a Geração dos Movimentos foi realizada para os estabelecimentos do RS que possuam parametrização dos Dados Iniciais.
Para isso recuperar os Estabelecimento pertencentes à parametrização dos Dados Iniciais da IN087/20 (tabela EST_ST_RS_DADOS_INI_IN87) e consultar a tabela de Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND), considerando:
- Código da empresa do login e
- Código Estabelecimento da parametrização dos Dados Iniciais da IN087/20 (tabela EST_ST_RS_DADOS_INI_IN87)
- Data compreendida no Período informado em tela;

Caso exista estabelecimento parametrizado em Dados Iniciais que não possua registro na Tabela de Cálculo da Média Ponderada (EST_ST_RS_MEDIA_POND), então significa que a Geração do Movimento não foi executada para o estabelecimento. Gravar a seguinte mensagem de aviso:
“Faltou realizar a Geração do Movimento para o estabelecimento/período. A Geração do Movimento para todos os estabelecimentos do RS é pré-requisito para execução da Geração das Transferências entre Estabelecimentos”.
Chave de identificação: Empresa XXX – Estabelecimento XXXXXX – Período MM/YYYY


Verificar Existência de Ciclos na Cadeia de Transferência entre estabelecimentos:
Verificar cadeias com ciclos que não serão processadas:
Exemplos:





Caso exista CICLOS. Gravar a seguinte mensagem de aviso:
“Não foi possível atualizar as transferências realizadas para o Produto com o valor médio unitário calculado para o Estabelecimento emitente, conforme tópico 19.3-A.2.1.2.2 da IN RE 045/98, pois a cadeia de transferência desse produto forma ciclos, impossibilitando a identificação do estabelecimento que iniciou as transferências.”.
Chave de identificação: Empresa XXX – Data: DD/MM/AAAA - Produto (grupo-ind-cod): XXXX-X-XXXXXXXX


## Processamento


### 4.1 Visão Resumida do Processamento

Um único número de processo será gerado contemplando todos os estabelecimentos da empresa, localizados no Rio Grande do Sul.
Os relatórios de conferência conterão os dados de todos os estabelecimentos processados, por isso quebrar em mais de um volume os arquivos CSV que ultrapassarem 1milhão de linhas.

Como num determinado dia, um produto pode ser transferido entre vários estabelecimentos da empresa, os estabelecimentos formam uma cadeia de transferência, onde é necessário processá-los em ordem, do primeiro ao último estabelecimento da cadeia.

Visão resumida do Processamento

Montagem das Cadeias de Transferência:
1º Passo: Recuperar os estabelecimentos, produtos e dias que receberam as notas de transferência oriundas de estabelecimentos do Rio Grande do Sul.

2º Passo: Armazenar as cadeias de transferência na tabela EST_ST_RS_ESTAB_TRANSF

Processamento das Cadeias de Transferência:
Para cada dia, processar as cadeias dos produtos, em ordem de nível (do primeiro ao último estabelecimento da cadeia), realizando os seguintes passos:
(num dia podem existir várias cadeias de um mesmo produto, e cadeias de diversos produtos)
1º Passo: Recuperar os valores unitários médios calculados no Estabelecimento Origem da transferência.
2º Passo: Atualizar as Notas de Entrada recebidas no Estabelecimento Destino da transferência, na tabela de Movimentos de Entrada – C180 (EST_ST_RS_NF_ENT)
3º Passo: Atualizar as Notas de Devolução de Entradas recebidas por transferência, no Estabelecimento Destino atualizadas no passo 2 – C186 (EST_ST_RS_NF_DEV_ENT)
4º Passo: Do dia da NF de Transferência até o último dia do Mês, atualizar no Estabelecimento Destino:
4.1 – As Notas de Devolução de Saídas do Estabelecimento Destino, produto e dia – C181 (EST_ST_RS_NF_DEV_SAI)
4.2 - A Média Ponderada do Estabelecimento Destino, produto e dia – EST_ST_RS_MEDIA_POND
4.3 - As Notas Fiscais de Saída do Estabelecimento Destino, produto e dia C185, C380, C480 (EST_ST_RS_NF_SAI e EST_ST_RS_ECF)

Para um DIA e PRODUTO a ordem de processamento entre os estabelecimentos é obrigatória (primeiro o estabelecimento origem e depois o estabelecimento destino da transferência), porque a média do estabelecimento origem deve ser repassado para a NF de transferência. Com isso o estabelecimento destino da transferência deve recalcular o valor da média ponderada e repassar para a nota de transferência que ele emite. E assim por diante na cadeia de transferência do produto no dia.

Para cada Data Transferência, processar os estabelecimentos em ordem de nível (do primeiro ao último estabelecimento da cadeia), realizando os passos a seguir:

Considerando um PRODUTO, o processamento deve seguir a ordem cronológica dos dias, pois no cálculo da média Ponderada, o saldo inicial do dia depende do saldo final do dia anterior. E para cada dia, o processamento deve seguir a ordem dos níveis dos estabelecimentos na cadeia (primeiro o estabelecimento origem e depois o de destino da transferência), porque a nota de entrada influencia no valor da média do estabelecimento destino. E a média do estabelecimento origem vai atualizar o valor da entrada do estabelecimento destino.

Nesse processamento, vários produtos podem ser atualizados no mesmo dia.


### 1º Passo – Recuperar os Valores Médios Unitários do Estabelecimento Origem (PFJ):



Origem dos dados:  - Tabela de “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND) com os seguintes critérios:
Critérios:
- Código da Empresa PFJ (origem)
- Código do Estabelecimento PFJ (origem)
- Data = Data da Transferência
- Produtos envolvidos nas transferências do estabelecimento origem p/ destino na Data da Transferência (estão na EST_ST_RS_ESTAB_TRANSF);

Recuperar os Valores Médios:
- Produto
- Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP);
- Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP);
- Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP);
- Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP);
- Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP);


### 2º Passo – Atualizar as Notas de Entradas recebidas por Transferência no Estabelecimento Destino – C180:


Atualizar todas as notas de entradas na tabela EST_ST_RS_NF_ENT que atendam aos critérios a seguir.

Origem dos dados: - Tabela Específica resultante da Geração do Movimento de Entradas (EST_ST_RS_NF_ENT).
Vide MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Entradas.docx

Critérios:
- Código da Empresa (destino)
- Código do Estabelecimento (destino);
- Data Emissão = Data da Transferência;
- Movimento de Entrada (campo 03 da SAFX07 – MOVTO_E_S diferente de ‘9’)
- Nota Normal (campo 04 da SAFX07 – NORM_DEV = ‘1’)

- CNPJ da Pessoa Fis/Jur da nota = CNPJ do Estabelecimento PFJ (origem).
Este é o critério que indica que a nota é de transferência.

- Produto Principal = Produto recuperado da Média Ponderada no passo 1;

Atualizar os campos:

Recuperar as seguintes informações:
- Número, Série, Subsérie da NF Entrada
- Pessoa Fís/Jur da NF Entrada
- Produto da NF (GRUPO_PROD_NF, IND_PROD_NF, COD_PROD_NF)
- Valor Médio Unitário do ICMS (VLR_ICMS_ENT_MP)
- Valor Médio Unitário do ICMS-ST (VLR_UNIT_ICMS_ST_ENT_MP)
- Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP)
- Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_ENT_MP)
- Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_ENT_MP)



### 3º Passo – Atualizar as Notas de Devolução das Entradas recebidas por Transferência no Estabelecimento Destino – C186:


Nesse passo, serão atualizadas as notas de devoluções, cujas entradas que foram atualizadas no passo anterior.

Origem dos dados: - Tabela Específica resultante da Geração do Movimento de Devolução das Entradas (EST_ST_RS_NF_DEV_ENT).
Vide MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Entradas.docx

Critérios:
- Código da Empresa (destino)
- Código do Estabelecimento (destino);
- Movimento de Saída (campo 03 da SAFX07 – MOVTO_E_S igual a ‘9’)
- Nota de Devolução (campo 04 da SAFX07 – NORM_DEV = ‘2’)
- Número do Documento Fiscal de Referência = Número da NF Entrada atualizada no passo 2
- Série do Documento Fiscal de Referência =Série da NF Entrada atualizada no passo 2
- Subsérie do Documento Fiscal de Referência = Subsérie da NF Entrada atualizada no passo 2
- Data Escrita Fiscal do Documento de Referência = Data Fiscal da NF Entrada atualizada no passo 2
- Pessoa Física/Jurídica do Documento de Referência = Pessoa Fis/Jur da NF Entrada atualizada no passo 2
- Número do Item do Documento de Referência = Número do Item da NF Entrada atualizada no passo 2
- Produto NF Devolução = Produto da NF Entrada atualizada no passo 2;





### 4º Passo – Recalcular os Valores Médios Unitários e as Devoluções de Saídas do Dia da Transferência em diante no Estabelecimento Destino:


Do dia da NF de Transferência (Data da Transferência) até o último dia do Mês, executar os passos 4.1, 4.2 e 4.3:

4.1 - Atualizar as Notas de Devolução de Saídas para o Estabelecimento Destino, produto (*) e dia – C181
(EST_ST_RS_NF_DEV_SAI)

4.2 - Atualizar a Média Ponderada para o Estabelecimento Destino, produto (*) e dia
(EST_ST_RS_MEDIA_POND)

4.3 - Atualizar as Notas Fiscais de Saída/Cupons Fiscais para o Estabelecimento Destino, produto (*) e dia C185, C380, C480 (**)
(EST_ST_RS_NF_SAI e EST_ST_RS_ECF)

(*) Produtos envolvidos nas transferências do estabelecimento origem p/ destino, na Data da Transferência (estão na EST_ST_RS_ESTAB_TRANSF);

(**) A atualização do C185, C380, C480 pode ser feita ao final, fora do loop, para todos os estabelecimentos de destino, pois a saída não interfere nas médias ponderadas.

Segue a lista de campos que são atualizados, uma vez que regra de preenchimento depende dos valores da Média Ponderada que estão sendo atualizados no passo 4.2.

EST_ST_RS_NF_DEV_SAI (C181)
Ver regra de preenchimento na MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Saidas.docx.


Notas de Saídas - EST_ST_RS_NF_SAI (C185, C380)
Ver regra de preenchimento na MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Saídas.docx.

Cupons Fiscais - EST_ST_RS_ECF (C480):
Ver regra de preenchimento na MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Saídas.docx.


Observação:
A fim de otimizar a performance, se existir mais de uma transferência para o Estabelecimento Destino, com mesma Data da Transferência e Produto, e níveis diferentes, o passo 4 pode ser executado apenas no registro da transferência de maior nível.
Exemplo:


Os seguintes registros de transferência são gravados na tabela EST_ST_RS_ESTAB_TRANSF.

Existem duas transferências recebidas pelo estabelecimento C: E >>C (nível 1) e B >>C (nível 2). O passo 4 só precisa ser executado uma vez para o estabelecimento C, ou seja, no processamento da última transferência B >>C (nível 2).

Exemplo 2:

Os seguintes registros de transferência são gravados na tabela EST_ST_RS_ESTAB_TRANSF.
Nesse exemplo, as duas transferências recebidas pelo estabelecimento C são de nível 1, E >>C (nível 1) e B >>C (nível 1). O passo 4 só precisa ser executado uma vez para o estabelecimento C. Mas como as duas transferências são de mesmo nível, este rodará duas vezes.


## Relatório


Gerar em arquivo excel, os relatórios de conferências abaixo listados, caso o parâmetro da tela “Gerar Relatórios de Conferência” seja selecionado.

Os relatórios conterão os dados de todos os estabelecimentos processados, por isso quebrar em mais de um volume os arquivos CSV que ultrapassarem 1milhão de linhas.


Os relatórios são os mesmos disponibilizados na Geração dos Movimentos, só que contendo todos os estabelecimentos do RS.

Relatório de Movimento de Entrada acrescentado o campo Ind. Transf Atualizada.
Relatório de Movimento de Devolução de Entrada acrescentado o campo Ind. Transf Atualizada.


Além dos relatórios em arquivo excel, apresentar uma aba o seguinte resumo:
- “Quantidade Total de Registros Atualizados”:
Layout do relatório:


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS93537 | Liliane Videira Assaf | Tratamento para transferência entre estabelecimentos da empresa conforme IN RE 045/98, tópico 19.3-A.2.1.2.2 | 10/10/2021 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
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
| EST_ST_RS_MEDIA_POND | X52_INVENT_PRODUTO | H030 |
|  | X304_SALDO_CONS_RES_COMP_ICMS | 1255 |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Neste campo será informado o período (mês e ano) para a geração dos dados.  Deve ser um mês válido. |
| Utilizar DATA MART para períodos anteriores | Alfanumérico | N | S | Check box | Caso esse parâmetro seja marcado, a recuperação das notas fiscais de períodos anteriores, referenciadas pelas devoluções, será feita pelas tabelas DATA MART. Caso contrário a busca será pelas tabelas normais (X07/X08). |
| Gerar Relatórios de Conferência | Alfanumérico | N | S | Check box | Campo habilitado para seleção. Se marcado os relatórios serão gravados em arquivo formato csv: - Movimento de Entradas (C180) - Movimento de Devolução de Saída (C181) - Movimento de Saídas (C185)  - Movimento de Saídas (C380) - Movimento de Cupom Fiscal (C480) - Movimento de Devolução de Entrada (C186) - Cálculo da Média Ponderada do Produto |


|  |
| --- |
|  |
|  |
| 4.2 Montagem das Cadeias de Transferência Nessa etapa, a partir do movimento de entradas (EST_ST_RS_NF_ENT), identificamos as transferências entre estabelecimentos ocorridas no período e armazenamos as cadeias de transferência na tabela EST_ST_RS_ESTAB_TRANSF.  1º Passo – Recuperar os Estabelecimentos que receberam notas de transferência de estabelecimentos do RS:    Origem dos dados:  - Tabela Movimento de Entradas (EST_ST_RS_NF_ENT)   Critérios:  - Empresa = código da empresa do login;  - Data Fiscal pertencente ao período que está sendo processado;  - Movimento de Entrada (campo 03 da SAFX07 – MOVTO_E_S diferente de ‘9’)  - Nota Normal (campo 04 da SAFX07 – NORM_DEV = ‘1’)  - CNPJ da Pessoa Fis/Jur da nota = CNPJ de algum estabelecimento da empresa (cadastro dos estabelecimentos da empresa).  Este é o critério que indica que a nota é de transferência.   Recuperar as seguintes informações da transferência: - Estabelecimento (receptor da nota) - Data fiscal da nota - Data Emissão (considerar a data da emissão ao invés da data fiscal, pois na entrada a data fiscal pode não ser igual a data da emissão. E temos que considerar a data da emissão para bater com a data da nota de saída) - Pessoa Física Jurídica (emissor da nota)  - Código de Estabelecimento relacionado à Pessoa Física Jurídica (emissor da nota)  - Produto (grupo, indicador e código do produto principal)  Se existir mais de uma nota de entrada de transferência para o estabelecimento, data fiscal, Pessoa Física Jurídica e produto, essa consulta deve retornar apenas um registro. Todos os registros recuperados são transferências entre estabelecimentos que serão gravados na tabela EST_ST_RS_ESTAB_TRANSF.   Observação: Utilizaremos qualquer Indicador de Pessoa Física/Jurídica (IND_FIS_JUR da SAFX04), não apenas o ‘3’ – Estabelecimento. O cliente DIMED não utiliza corretamente esse indicador. Nesse momento vamos considerar apenas estabelecimentos da empresa de login, devido a volumetria de notas processadas. Caso haja necessidade, ampliaremos para tratar transferência dos estabelecimentos entre empresas.   2º Passo – Gravação da Tabela de Cadeia de Transferência (EST_ST_RS_ESTAB_TRANSF)  Para cada produto e dia, identificar as cadeias de transferência entre estabelecimentos, onde:   - Estabelecimento Inicial (Nó Raiz): aquele que não recebe, só emite nota de transferência do produto no dia, sendo então o primeiro Estabelecimento da Cadeia (nível 1).  - Estabelecimentos intermediários: aquele que recebe e emite nota de transferência do produto no dia (nível 2, 3...)  - Estabelecimento Final (Nó folha): aquele que só recebe, não emite nota de transferência do produto no dia, sendo então o último Estabelecimento da Cadeia  Observação:  - Num dia podemos ter várias cadeias de transferência de um produto. - Atribuímos a cada estabelecimento um número de nível que é sua ordem na cadeia. - Todos os registros são gravados com o Estabelecimento Inicial (Nó Raiz) da cadeia.   Tabela EST_ST_RS_ESTAB_TRANSF  Os campos sinalizados com asterisco compõem a chave da tabela.   Exemplo: As notas fiscais abaixo são de entrada por transferência recebidas pelos Estabelecimentos, considerando um determinado dia e produto.   Essas notas formam duas cadeias, uma iniciada no estabelecimento E, outra iniciada no estabelecimento A. Veja:      Os seguintes registros de transferência são gravados na tabela EST_ST_RS_ESTAB_TRANSF.     4.3 Processamento das Cadeias de Transferência  Recuperar as Cadeias de Transferência identificadas e gravadas no tópico 4.2.  Origem dos dados:  - Tabela de Cadeia de Transferência (EST_ST_RS_ESTAB_TRANSF)   Critérios:  - Empresa = código da empresa do login; - Data Transferência pertencente ao período que está sendo processado; - Indicador de Processar (IND_PROCESSAR) = ‘S’;  Recuperar as informações da cadeia: - Código da Empresa (destino) - Código do Estabelecimento (destino) - Código da Empresa PFJ (origem)  - Código do Estabelecimento PFJ (origem) - Data Transferência - Nível Recuperar as cadeias ordenadas por Data Transferência e Nível (NUM_NIVEL). |


| Item SAFX296 | Campo | Nome do campo na tabela | Regra de Preenchimento |
| --- | --- | --- | --- |
| 19 | Valor Unitário ICMS Conv. Campos da EFD correspondes: 06 (C180), 10 (C185) e 06 (C380). | VLR_ICMS_CONV | Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP) |
| 21 | Valor Unitário BC ICMS-ST Conv. (Entradas) Campo da EFD corresponde: 07 (C180) | VLR_UNIT_BC_ICMSS_ENT | Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP) |
| 22 | Valor Unitário ICMS-ST Conv.  (Entradas) Campo da EFD corresponde: 08 (C180). | VLR_UNIT_ICMSS_CONV_ENT | Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP) |
| 23 | Valor Unitário FCP-ST Conv.  (Entradas) Campo da EFD corresponde: 09 (C180). | VLR_UNIT_FCP_CONV_ENT | Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP) |
|  | Valor Médio Unitário do ICMS (b) | VLR_UNIT_ICMS_ENT_MP | Valor Médio Unitário do ICMS (VLR_UNIT_ICMS_FIM_MP) |
|  | Valor Médio Unitário do ICMS-ST (c) | VLR_UNIT_ICMS_ST_ENT_MP | Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_FIM_MP) |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST (d) | VLR_UNIT_BC_ST_ENT_MP | Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_FIM_MP) |
|  | Valor Médio Unitário do FECEP-ST (e) | VLR_UNIT_FECEP_ST_ENT_MP | Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_FIM_MP) |
|  | Valor do ICMS Calculado para Entrada (f) = (a * b) | VLR_ICMS_ENT_MP | Quantidade Entrada Convertida x Valor Médio Unitário do ICMS  (QTD_CONV_ENT_MP x VLR_UNIT_ICMS_FIM_MP) |
|  | Valor do ICMS-ST Calculado para Entrada (g) = (a * c) | VLR_ICMS_ST_ENT_MP | Quantidade Entrada Convertida x Valor Médio Unitário do ICMS-ST s/ FECEP  (QTD_CONV_ENT_MP x VLR_UNIT_ICMS_ST_FIM_MP); |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Entrada (h) = (a * d) | VLR_BC_ST_ENT_MP | Quantidade Entrada Convertida x Valor Médio Unitário da Base de Cálculo do ICMS-ST  (QTD_CONV_ENT_MP x VLR_UNIT_BC_ST_FIM_MP) |
|  | Valor FECEP-ST Calculado para Entrada (i) = (a * e) | VLR_FECEP_ST_ENT_MP | Quantidade Entrada Convertida x Valor Médio Unitário do FECEP-ST  (QTD_CONV_ENT_MP x VLR_UNIT_FECEP_ST_FIM_MP) |
|  | Indicador de Atualização | IND_ATU_TRANSF | S Indicador Criado para “marcar” as notas que foram atualizadas por esse processo de geração as transferências. |


| Item SAFX308 | Campo | Nome do campo na tabela | Regra de Preenchimento |
| --- | --- | --- | --- |
| 35 | Valor Unitário ICMS Conv.OP Campos da EFD correspondentes: 17 do C181 e 16 do C186 | VLR_ICMS_CONV | Valor Médio Unitário do ICMS (VLR_ICMS_ENT_MP) |
| 36 | Valor Unitário Base ICMS ST Conv da Entrada Campo da EFD correspondente: 17 do C186. | VLR_UNIT_BC_ICMSS_ENT | Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_ENT_MP) |
| 37 | Valor Unitário ICMS ST Conv da Entrada Campo da EFD correspondente: 18 do C186. | VLR_UNIT_ICMSS_CONV_ENT | Valor Médio Unitário do ICMS-ST c/ FECEP (VLR_UNIT_ICMS_ST_FECEP_FIM_MP) |
| 38 | Valor Unitário FCP ST Conv da Entrada Campo da EFD correspondente: 19 do C186. | VLR_UNIT_FCP_CONV_ENT | Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_ENT_MP) |
|  | Valor Médio Unitário do ICMS (b) | VLR_UNIT_ICMS_DEV_ENT_MP | Valor Médio Unitário do ICMS (VLR_ICMS_ENT_MP) |
|  | Valor Médio Unitário do ICMS-ST (c) | VLR_UNIT_ICMS_ST_DEV_ENT_MP | Valor Médio Unitário do ICMS-ST s/ FECEP (VLR_UNIT_ICMS_ST_ENT_MP) |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST (d) | VLR_UNIT_BC_ST_DEV_ENT_MP | Valor Médio Unitário da Base de Cálculo do ICMS-ST (VLR_UNIT_BC_ST_ENT_MP) |
|  | Valor Médio Unitário do FECEP-ST (e) | VLR_UNIT_FECEP_ST_DEV_ENT_MP | Valor Médio Unitário do FECEP-ST (VLR_UNIT_FECEP_ST_ENT_MP) |
|  | Valor do ICMS Calculado para Devolução (f) = (a * b) | VLR_ICMS_DEV_ENT_MP | Quantidade Devolvida Convertida x Valor Médio Unitário do ICMS  (QTD_CONV_DEV_ENT_MP x VLR_ICMS_ENT_MP) |
|  | Valor do ICMS-ST Calculado para Devolução (g) = (a * c) | VLR_ICMS_ST_DEV_ENT_MP | Quantidade Devolvida Convertida x Valor Médio Unitário do ICMS-ST s/ FECEP  (QTD_CONV_DEV_ENT_MP x VLR_UNIT_ICMS_ST_ENT_MP); |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução (h) = (a * d) | VLR_BC_ST_DEV_ENT_MP | Quantidade Devolvida Convertida x Valor Médio Unitário da Base de Cálculo do ICMS-ST  (QTD_CONV_DEV_ENT_MP x VLR_UNIT_BC_ST_ENT_MP) |
|  | Valor FECEP-ST Calculado para Devolução (i) = (a * e) | VLR_FECEP_ST_DEV_ENT_MP | Quantidade Devolvida Convertida x Valor Médio Unitário do FECEP-ST  (QTD_CONV_DEV_ENT_MP x VLR_UNIT_FECEP_ST_ENT_MP) |
|  | Indicador de Atualização | IND_ATU_TRANSF | S Indicador Criado para “marcar” as notas que foram atualizadas por esse processo de geração as transferências. |


| Item SAFX308 | Campo | Nome do campo na tabela |
| --- | --- | --- |
| 39 | Valor Unitário ICMS OP Estoque Conv  Campo da EFD correspondente: 13 do C181. | VLR_UNIT_ICMS_ESTQ_SAI |
| 40 | Valor Unitário ICMS ST Estoque Conv  Campo da EFD correspondente: 14 do C181. | VLR_UNIT_ICMSS_ESTQ_SAI |
| 41 | Valor Unitário FCP ICMS ST Estoque Conv  Campo da EFD correspondente: 15 do C181. | VLR_UNIT_FCP_ESTQ_SAI |
| 42 | Valor Unitário ICMS na Operação Conv  Campo da EFD correspondente: 16 do C181. | VLR_UNIT_ICMS_OPER_SAI |
|  | Valor Médio Unitário do ICMS no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_SAI |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_SAI |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_FECEP_SAI |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST no dia Saída (Tabela de Média Diária) | VLR_UNIT_BC_ST_SAI |
|  | Valor Médio Unitário do FECEP-ST no dia Saída (Tabela de Média Diária) | VLR_UNIT_FECEP_ST_SAI |
|  | Valor Médio Unitário do ICMS (b) | VLR_UNIT_ICMS_DEV_SAI_MP |
|  | Valor Médio Unitário do ICMS-ST (c) | VLR_UNIT_ICMS_ST_DEV_SAI_MP |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST (BC-Entrada) (d) | VLR_UNIT_BC_ST_DEV_SAI_MP |
|  | Valor Médio Unitário do FECEP-ST (e) | VLR_UNIT_FECEP_ST_DEV_SAI_MP |
|  | Valor do ICMS Calculado para Devolução (f) = (a*b) | VLR_ICMS_DEV_SAI_MP |
|  | Valor do ICMS-ST Calculado para Devolução (g) = (a * c) | VLR_ICMS_ST_DEV_SAI_MP |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução (h) = (a * d) | VLR_BC_ST_DEV_SAI_MP |
|  | Valor FECEP-ST Calculado para Devolução (i) = (a * e) | VLR_FECEP_ST_DEV_SAI_MP |
|  | OBSERVAÇÃO | DSC_OBS |


| Item SAFX296 | Campo | Nome do campo na tabela |
| --- | --- | --- |
| 19 | Valor Unitário ICMS Conv.  Campos da EFD correspondes: 06 (C180), 10 (C185) e 06 (C380). | VLR_ICMS_CONV |
| 24 | Código Motivo (Saídas) Campos da EFD correspondes: 06 (C185) e 02 (C380). | COD_MOTIVO_SAI |
| 26 | Valor Unitário ICMS Estoque Conv. (Saídas) Campos da EFD correspondes: 12 (C185) e 08 (C380). | VLR_UNIT_ICMS_ESTQ_SAI |
| 27 | Valor Unitário ICMS-ST Estoque Conv. (Saídas) Campos da EFD correspondes: 13 (C185) e 09 (C380). | VLR_UNIT_ICMSS_ESTQ_SAI |
| 28 | Valor Unitário FCP-ST Estoque Conv. (Saídas) Campos da EFD correspondes: 14 (C185) e 10 (C380). | VLR_UNIT_FCP_ESTQ_SAI |
| 29 | Valor Unitário ICMS-ST Conv. Rest. (Saídas) Campos da EFD correspondes: 15 (C185) e 11 (C380). | VLR_UNIT_ICMSS_REST_SAI |
| 30 | Valor Unitário FCP-ST Conv. Rest. (Saídas) Campos da EFD correspondes: 16 (C185) e 12 (C380). | VLR_UNIT_FCP_REST_SAI |
| 31 | Valor Unitário ICMS-ST Conv. Compl. (Saídas) Campos da EFD correspondes: 17 (C185) e 13 (C380). | VLR_UNIT_ICMSS_COMPL_SAI |
| 32 | Valor Unitário FCP-ST Conv. Compl. (Saídas) Campos da EFD correspondes: 18 (C185) e 14 (C380). | VLR_UNIT_FCP_COMPL_SAI |
|  | Valor Médio Unitário do ICMS no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_SAI |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_SAI |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_FECEP_SAI |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST no dia Saída (Tabela de Média Diária) | VLR_UNIT_BC_ST_SAI |
|  | Valor Médio Unitário do FECEP-ST no dia Saída (Tabela de Média Diária) | VLR_UNIT_FECEP_ST_SAI |
|  | OBSERVAÇÃO | DSC_OBS |


| Item SAFX297 | Campo | Nome do campo na tabela |
| --- | --- | --- |
| 09 | Código do Motivo Campo da EFD correspondente: 02 do C480. Obs: mesma regra do C185 – 06. | COD_MOTIVO |
| 13 | Valor Unitário ICMS na Oper. Conv. Campo da EFD correspondente: 06 do C480 Obs: mesma regra do C185 - 10 | VLR_UNIT_ICMS_OPER_CONV |
| 15 | Valor Unitário ICMS Estoque Conv. Campos da EFD correspondes: 08 do C480 Obs: mesma regra do C185 - 12 | VLR_UNIT_ICMS_ESTQ_CONV |
| 16 | Valor Unitário ICMS-ST Estoque Conv.  Campos da EFD correspondes: 09 do C480 Obs: mesma regra do C185 - 13 | VLR_UNIT_ICMSS_ESTQ_CONV |
| 17 | Valor Unitário FCP-ST Estoque Conv.  Campos da EFD correspondes: 10 do C480 Obs: mesma regra do C185 - 14 | VLR_UNIT_FCPS_ESTQ_CONV |
| 18 | Valor Unitário ICMS-ST Conv. Rest.  Campos da EFD correspondes: 11 do C480 Obs: mesma regra do C185 - 15 | VLR_UNIT_ICMSS_REST_CONV |
| 19 | Valor Unitário FCP-ST Conv. Rest.  Campos da EFD correspondes: 12 do C480 Obs: mesma regra do C185 - 16 | VLR_UNIT_FCPS_REST_CONV |
| 20 | Valor Unitário ICMS-ST Conv. Compl.  Campos da EFD correspondes: 13 do C480 Obs: mesma regra do C185 - 17 | VLR_UNIT_ICMSS_COMPL_CONV |
| 21 | Valor Unitário FCP-ST Conv. Compl.  Campos da EFD correspondes: 14 do C480 Obs: mesma regra do C185 - 18 | VLR_UNIT_FCPS_COMPL_CONV |
|  | Valor Médio Unitário do ICMS no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_SAI |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_SAI |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP no dia Saída (Tabela de Média Diária) | VLR_UNIT_ICMS_ST_FECEP_SAI |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST no dia Saída (Tabela de Média Diária) (BC-Entrada) | VLR_UNIT_BC_ST_SAI |
|  | Valor Médio Unitário do FECEP-ST no dia Saída (Tabela de Média Diária) | VLR_UNIT_FECEP_ST_SAI |
|  | OBSERVAÇÃO | DSC_OBS |


| Empresa | Estabelecimento  (destino) | Estabelecimento PFJ (origem) | Pessoa Fis/Jur (origem) | Data Fiscal | Produto | Estabelecimento Inicial (Nó Raiz) | Nível do Estabelecimento PFJ (origem) | Indicador de Processar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 076 | F | E | E | 01/01/2022 | 1-111 | E | 1 | S |
| 076 | C | E | E | 01/01/2022 | 1-111 | E | 1 | S |
| 076 | D | C | C | 01/01/2022 | 1-111 | E | 2 | N |
| 076 | G | D | D | 01/01/2022 | 1-111 | E | 3 | N |
| 076 | B | A | A | 01/01/2022 | 1-111 | A | 1 | S |
| 076 | C | B | B | 01/01/2022 | 1-111 | A | 2 | S |
| 076 | D | C | C | 01/01/2022 | 1-111 | A | 3 | S |
| 076 | G | D | D | 01/01/2022 | 1-111 | A | 4 | S |


| Empresa | Estabelecimento  (destino) | Estabelecimento PFJ (origem) | Pessoa Fis/Jur (origem) | Data Fiscal | Produto | Estabelecimento Inicial (Nó Raiz) | Nível do Estabelecimento PFJ (origem) | Indicador de Processar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 076 | C | E | E | 01/01/2022 | 1-111 | E | 1 | S |
| 076 | C | B | B | 01/01/2022 | 1-111 | B | 1 | S |


| Relatório de Conferência | Tabelas Específicas da Geração do Movimento |
| --- | --- |
| Movimento de Entradas (C180) | EST_ST_RS_NF_ENT |
| Movimento de Devolução de Saída (C181) | EST_ST_RS_NF_DEV_SAI |
| Movimento de Saídas (C185) | EST_ST_RS_NF_SAI, filtrar as notas de Modelo = 01, 1B, 04, 55, 65 |
| Movimento de Saídas (C380) | EST_ST_RS_NF_SAI, filtrar as notas de Modelo = 02 |
| Movimento de Cupons Fiscais (C480) | EST_ST_RS_ECF |
| Movimento de Devolução de Entrada (C186) | EST_ST_RS_NF_DEV_ENT |
| Cálculo da Média Ponderada | EST_ST_RS_MEDIA_POND |


| Registro | Total Atualizados |
| --- | --- |
| C180 |  |
| C181 |  |
| C185 |  |
| C186 |  |
| C380 |  |
| C480 |  |
