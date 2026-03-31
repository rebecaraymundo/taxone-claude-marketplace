# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal

> Fonte: MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Transferência dos Movimentos para EFD Fiscal



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração à IN-RE 087/20 à Transferência dos Movimentos para EFD Fiscal



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Parâmetros da Tela	1
3.	Críticas	1
4.	Processamento	1
1º Passo: Atualizar o Inventário do Último dia do Mês Anterior	1
2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal	1
3º Passo - Geração Registros de Saldo Consolidado de Ressarcimento e Complemento (1255)	1
4º Passo: Gerar Relatórios de Conferência	1


## Introdução


O objetivo dessa funcionalidade é recuperar os registros gerados pelo processo de “Geração dos Movimentos” a partir das tabelas específicas do módulo, e gravar as tabelas definitivas relacionadas as “SAFX”, que são base para geração dos registros C180, C181, C185, C480, C186, 1250, 1255, H030 do Sped Fiscal.

Como Pré-Requisito para esta execução, não pode existir registro na tabela definitiva, oriundo da importação da SAFX.



Artefatos gerados pela Transferência do Movimento:
O resultado dessa geração pode ser conferido através dos Relatórios:
- Relatório de Conferência do Saldo Consolidado de Ressarcimento e Complemento – registro 1255, gerado em arquivo Excel.
- Relatório Demonstrando o total de Registros Lidos e Gravados em cada tabela definitiva relacionada a SAFX.


Base Legal:
- IN-RE 087/20
- IN-RE 096/20



## Parâmetros da Tela



Período: MM/AAAA

Estabelecimentos
[ ] xxxxxx - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[ ] xxxxxx - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[ ] xxxxxx - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Funcionamento dos campos:






## Críticas



Como pré-requisito, não pode existir registro importado nas tabelas SAFX. Caso exista, o processo será abortado.


Existência de Movimento de Entradas e Saídas importados pela SAFX296
Caso exista Movimento de Entradas e Saídas importados pela SAFX296, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:
“Existem dados importados através da SAFX296 – Informações Complementares das Operações Sujeitas ao ST (C180, C185 e C380) para o estabelecimento e período informados. Nesta rotina os movimentos de entradas e saídas a serem apresentados nos registros C180, C185 e C380 são gerados na tabela definitiva da SAFX296. Como pré-requisito não pode existir movimentos oriundos da Importação da SAFX296. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas.”


[MFS65137]
Existência de Movimento de Cupom Fiscal importado pela SAFX297
Caso exista Movimento de Cupom Fiscal importados pela SAFX297, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:
“Existem dados importados através da SAFX297 – Informações Complementares das Operações Sujeitas ao ST (C480) para o estabelecimento e período informados. Nesta rotina os movimentos de cupons fiscais a serem apresentados no registro C480 são gerados na tabela definitiva da SAFX297. Como pré-requisito não pode existir movimentos oriundos da Importação da SAFX297. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas.”

Existência de Movimento de Devoluções de Entradas e Saídas importados pela SAFX308
Caso exista Movimento de Devoluções de Entradas e Saídas importados pela SAFX308, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:
“Existem dados importados através da SAFX308 – Informações Complementares das Operações de Devolução Sujeitas ao ST (C181 e C186) para o estabelecimento e período informados. Nesta rotina os movimentos de devoluções a serem apresentados nos registros C181 e C186 são gerados na tabela definitiva da SAFX308. Como pré-requisito não pode existir movimentos oriundos da Importação da SAFX308. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas.”

Existência de Saldo Consolidado da Restituição/Complemento importado pela SAFX304

Caso exista Saldo Consolidado da Restituição/Complemento ST importados pela SAFX304, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:
“Existem dados importados através da SAFX304 – Saldo Consolidado da Restituição/Complemento ST (1250 e 1255) para o estabelecimento e período informados. Nesta rotina os saldos a serem apresentados nos registros 1250 e 1255 são gerados na tabela definitiva da SAFX304. Como pré-requisito não pode existir movimentos oriundos da Importação da SAFX304
. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas.”


Acontecendo qualquer erro, finalizar a geração com status = “-1” – Erro.



## Processamento


Visão resumida do Processamento
O processamento requer uma ordem na geração dos movimentos já que algumas etapas dependem do resultado da execução anterior.

Sendo assim vamos executar o processamente seguindo os passos abaixo:
1º Passo: Atualizar o Inventário do Último dia do Mês Anterior

2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal

3º Passo: Gerar os Registros de Saldo Consolidado de Ressarcimento e Complemento (1255)

4º Passo: Gerar Relatórios de Conferência



Segue detalhamento de cada passo do processamento

### 1º Passo: Atualizar o Inventário do Último dia do Mês Anterior

Recupera os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST da tabela EST_ST_RS_MEDIA_POND do último dia do mês anterior e atualiza a Tabela do Inventário (X52_INVENT_PRODUTO) para o registro do último dia do mês anterior com IND_MOT_INV = 06. Gera uma crítica caso o os valores médios tenham sido importados e estejam diferentes dos calculados.

Para maiores detalhes ver documento matriz:
- MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Inventário_H030.docx


### 2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal


Gravação das tabelas definitivas relacionadas as “SAFX”, base para geração dos registros C180, C181, C185, C186, C380 e [MFS65137] C480 do SPED FISCAL, a partir da leitura das tabelas específicas da Geração do Movimento.

Para maiores detalhes ver documento matriz:
MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Tabelas SAFX_C180_C181_C185_C186_C380_C480.docx



### 3º Passo - Geração Registros de Saldo Consolidado de Ressarcimento e Complemento (1255)


Geração dos registros de Saldo Consolidado de Ressarcimento e Complemento (1255).
O registro 1255 é uma consolidação dos valores de complemento e ressarcimento por Código de Motivo da Restituição/Complementação (RS100, RS300, ...) apresentados nos registros C181, C185, C330, C380, C430, [MFS65137] C480, C815 e C880 do Sped Fiscal.
Os registros gerados são gravados na tabela de “Saldo Consolidado da Restituição/Complemento de ICMS” - X304_SALDO_CONS_RES_COMP_ICMS, base para geração do registro 1255 no Sped Fiscal.

Os dados calculados e gravados podem ser consultados na tela SPEDàEFD – Escrituração Fiscal Digital àGeração àManutenção àRegistro 1255.


Para maiores detalhamentos ver documentos matrizes:
- MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255.docx



### 4º Passo: Gerar Relatórios de Conferência

Geração do Relatório de Conferência em arquivos Excel para conferência do registro 1255.
Geração do Resumo demonstrando o total de registros lidos e gravados em tela, na aba “Quantidade Total de Registros Gravados”
- Relatório de Conferência do Saldo Consolidado de Ressarcimento e Complemento (1255).
- ver: MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255.docx

- Resumo “Quantidade Total de Registros Gravados”:
Layout do relatório:





= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
|  |  |  |  |
| MFS48753 | Liliane Videira Assaf | Criação da funcionalidade | 12/01/2021 |
| MFS65137 | Liliane Videira Assaf | Tratamento dos Cupom Fiscal (Mod. 02, 2D e 60) para geração do registro C480 do Sped Fiscal. Os cupons devem ser lidos da tabela EST_ST_RS_ECF e gravados na tabela X297_INF_COMP_ST_CUPOM_ECF, de onde o registro C480 é gerado no Sped Fiscal. | 13/05/2021 |
| MFS72958 | Liliane Videira Assaf | Tratamento de produtos novos sem inventário. Atualizar o Resumo de “Quantidade Total de Registros Gravados” para demonstrar o total de registros lidos e inseridos do H030. | 21/09/2021 |
|  |  |  |  |
|  |  |  |  |


| Tabelas Específicas da Geração do Movimento | Tabelas definitivas relacionadas as SAFX | Registro do SPED FISCAL |
| --- | --- | --- |
| EST_ST_RS_NF_ENT | x296_info_compl_st_itens_merc | C180 |
| EST_ST_RS_NF_DEV_ENT | X308_INFO_COMPL_ST_IT_MERC_DEV | C186 |
| EST_ST_RS_NF_DEV_SAI | X308_INFO_COMPL_ST_IT_MERC_DEV | C181 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C185 |
| EST_ST_RS_NF_SAI | x296_info_compl_st_itens_merc | C380 |
| EST_ST_RS_ECF | X297_INF_COMP_ST_CUPOM_ECF | C480 [MFS65137] |
| EST_ST_RS_MEDIA_POND | X52_INVENT_PRODUTO | H030 |
|  | X304_SALDO_CONS_RES_COMP_ICMS | 1255 |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Neste campo será informado o período (mês e ano) para a geração dos dados.  Deve ser um mês válido. |
| Estabelecimentos | Alfanumérico | S | S |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos de RS (UF do estabelecimento = RS). |
| Selecionar |  | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;  - Somente Estabelecimentos da UF de RS;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos |  | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |


| Tabela Destino | Registros do SPED FISCAL |
| --- | --- |
| X304_SALDO_CONS_RES_COMP_ICMS | 1255 |


| Registro | Total Lidos | Total Inseridos | Total Atualizados |
| --- | --- | --- | --- |
| C180 |  |  |  |
| C181 |  |  |  |
| C185 |  |  |  |
| C186 |  |  |  |
| C380 |  |  |  |
| C480 [MFS65137] |  |  |  |
| H030 | MFS72958 Não se aplica ao H030 | MFS72958 Não se aplica ao H030 |  |
| 1255 | Não se aplica ao 1255 |  |  |
