# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C195_C197_Lancto_P9_ST

> Fonte: MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C195_C197_Lancto_P9_ST.docx






THOMSON REUTERS

Módulo Sped Fiscal


Processamento do Cálculo ICMS-ST – Registro C195/C197 + Lançamentos na Apuração ICMS-ST



Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré-Geraçãoà Ressarcimento ICMS-ST (Específico MG) à Pré-Geração



DOCUMENTO DE REQUISITO




Sumário

1.	Visão Geral	1
2.	Introdução	1
3.	Críticas	1
4.	Processamento	1
5.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:	1
5.2 - Etapa 2: Geração das Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)	1
5.3 – Etapa 3: Geração do Lançamento Complementar na Apuração do ICMS-ST (P9-ST)	1
5.4 – Etapa 4: Atualização do Status da Obrigação da Apuração	1
5.5 – Etapa 5: Geração de Relatório de Conferência Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)	1
5.6 – Etapa 6: Geração de Relatório de Conferência dos Lançamentos Complementares na Apuração do ICMS-ST	1


## Visão Geral


Com base nos tópicos 7 e 8 do “Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo” as notas de devolução de saída que geram registros C181 com códigos de motivo MG600 (Estorno de Ressarcimento) e MG800 (Estorno de Complemento), precisam gerar os registros de Observação do Lançamento Fiscal (C195) e Ajustes Provenientes do Documento Fiscal (C197).  E os ajustes (C197) que geram crédito ou débito na Apuração do ICMS-ST, precisam ser consolidados nos campos 07 e 10 do registro E210.

Esses registros estão organizados na seguinte hierarquia:
C100 – Capa do Documento Fiscal (Nível 2)
.... C170 – Item do Documento Fiscal (Nível 3)
.... .... C181 – Inf Complementares da Dev. Saída (Nível 4)
.... C195 – Obs Lançamento Fiscal (Nível 3)
.... .... C197 – Ajustes Provenientes do Documento Fiscal (Nível 4)
MFS560863: Multiplicar os valores unitários do ICMS-ST e FCP-ST pela quantidade devolvida (campo 03 - QUANT_CONV)
Segundo o tópico 07, para cada nota de devolução de saída (C100) que gerou pelo menos um registro C181 com Estorno do Ressarcimento (MG600), temos que:
Totalizar os valores dos campos (20 – VL_UNIT_ICMS_ST_CONV_COMPL x 03 - QUANT_CONV) e (21 – VL_UNIT_FCP_ST_CONV_COMPL x 03 - QUANT_CONV) dos registros C181 com COD_MOTIVO = ‘MG600’.
Gerar os seguintes registros:
C195 com código de observação definida pelo contribuinte referente a “Estorno de Restituição/Ressarcimento de ICMS ST – Aspecto Quantitativo”;
C197 com código de ajuste igual a “MG41000016” com o valor total do campo 20 – VL_UNIT_ICMS_ST_CONV_COMPL x 03 - QUANT_CONV;
Se houver parcela do FCP adicionado ao ICMS-ST, ou seja, se o valor total do campo 21 – VL_UNIT_FCP_ST_CONV_COMPL for maior que zero, então gerar os registros:
- C197 com código de ajuste igual a “MG21000018” com o valor total do campo 21 – VL_UNIT_FCP_ST_CONV_COMPL x 03 - QUANT_CONV;
- C197 com código de ajuste igual a “MG91000018” com o valor total do campo 21 – VL_UNIT_FCP_ST_CONV_COMPL x 03 - QUANT_CONV;
Já de acordo com o tópico 08, para cada nota de devolução de saída (C100) que gerou pelo menos um registro C181 com Estorno do Complemento (MG800), precisamos:
Totalizar os valores 18 – VL_UNIT_ICMS_ST_CONV_REST x 03 - QUANT_CONV dos registros C181 com COD_MOTIVO = ‘MG800’.
Gerar os seguintes registros:
C195 com código de observação definida pelo contribuinte referente a “Estorno de Complemento do Imposto ICMS ST – Aspecto Quantitativo”;
C197 com código de ajuste igual a “MG11000016” com o valor total do campo 18 – VL_UNIT_ICMS_ST_CONV_REST x 03 - QUANT_CONV;

Em termos de Apuração do ICMS-ST, serão realizados os seguintes lançamentos complementares:
Somatório dos registros C197 com código de ajuste igual a “MG41000016” (valor do campo 20 – VL_UNIT_ICMS_ST_CONV_COMPL x 03 - QUANT_CONV) è Gera 1 lançamento em Outros Débitos (E210 -10)
Somatório dos registros C197 com código de ajuste igual a “MG21000018” (valor do campo 21 – VL_UNIT_FCP_ST_CONV_COMPL x 03 - QUANT_CONV) è Gera 1 lançamento em Estorno Débitos (E210 -07)
Somatório dos registros C197 com código de ajuste igual a “MG11000016” (valor do campo 18 – VL_UNIT_ICMS_ST_CONV_REST x 03 - QUANT_CONV) è Gera 1 lançamento em Outros Créditos (E210 -07)

Obs: O ajuste com código igual a “MG91000018” é apenas informativo, logo não compõe a Apuração do ICMS-ST.

Nota: Esses códigos e ajustes não serão tratados fixos na solução.  Disponibilizamos uma tela de parametrização onde o usuário irá definir os Códigos de Observação do C195, os Códigos de Ajuste do C197 (“MG41000016”...), os códigos de operação da apuração para atribuição dos lançamentos complementares (operação 002 – Outros Debitos, 003 – Estorno de Crédito , ...)

Base Legal: Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo – versão 05.


## Introdução


Essa geração será executada quando na tela de geração o parâmetro “C195/C197 – Observação/Ajuste e Lançamento Complementar na Apuração ICMS-ST” estiver marcado.

Esse processo consiste em gravar os registros C195 e C197 nas tabelas SAFX específicas para geração destes registros do Sped Fiscal. São elas:

SAFX112 – OBSERVAÇÕES DA NOTA FISCAL (corresponde ao C195, registro “filho” do C100);
SAFX113 – AJUSTES DO LANÇAMENTO FISCAL (corresponde ao C197, registro “filho” do C195);

Realizar os lançamentos complementares na Apuração do ICMS-ST e associá-los aos ajustes (SAFX113). As seguintes tabelas serão povoadas:
ITEM_APURAC_SUBST: armazena os lançamentos complementares da Apuração do ICMS-ST
ITEM_APURAC_SUBST_X113: vincula o lançamento aos registros de ajustes da X113.

Os códigos de observação para geração dos registros na SAFX112 (C195), os códigos de ajustes da SAFX113 (C197) e os códigos de operação para os lançamentos na apuração, serão definidos pelo usuário através da tela de parametrização disponível no menu “Parâmetros à Ressarcimento ICMS-STà Parâmetros p/Geração dos Ajustes e Lançamentos” (tabela EFD_PAR_RESSARC_MG).

Após a execução da Pré-Geração Ressarcimento ICMS-ST (Específico MG) e ANTES da Geração do Meio Magnético do SPED FISCAL, é necessário que o usuário realize a Apuração do ICMS (P9), no módulo ICMS, para recalcular os totais do resumo da Substituição Tributária. Este procedimento já é adotado no DW, quando utiliza o Módulo Lançamentos Automáticos ICMS para gerar automaticamente lançamentos na apuração do ICMS e quando criamos manualmente lançamentos no módulo ICMS. Em ambas as situações, após a criação dos lançamentos, a Apuração do ICMS deve ser executada.
O Resumo da Apuração do ICMS-ST serão recalculados a partir dos lançamentos. Os valores dos lançamentos da tabela ITEM_APURAC_SUBST são consolidados por código de operação, atualizando os códigos de operação do Resumo da Apuração do ICMS-ST (RESUMO_APUR_ST).
Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS.


Os registros de observação e ajustes gerados nas tabelas SAFX112 e SAFX113 podem ser conferidos via tela de manutenção no módulo Básicos >> Data Warehouse, menu Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc. Fiscal de Mercadoria (Versão Anterior) aba Observações do Lançamento Fiscal.

Os lançamentos complementares gerados na Apuração do ICMS-ST podem ser conferidos via tela de manutenção no módulo Estadual >> ICMS, menu Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst. Tributária >> Ajuste SINIEF.

Obs: Geração por Inscrição Estadual Única não está sendo tratada.


## Críticas


Os Pré-requisitos para essa geração são:
- Criar um calendário para a Apuração do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento.
- O estabelecimento e período da geração deve possuir cadastro do Calendário para a Apuração do ICMS, utilizando como código da obrigação 108.
- Parametrizar os códigos de observação, os códigos de ajustes e lançamentos na tela de parametrização (item de menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos), disponível neste módulo.

Antes de inicia o processamento, vamos checar se esses passos foram feitos. Caso encontre alguma falha nestas verificações, o processo será abortado.

Verificar se o Cadastro da Obrigação Fiscal para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:
Verificar se existe Cadastro da Obrigação Fiscal para a Apuração do ICMS – P9.
O cadastro da Obrigação Fiscal está localizado no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Obrigação Fiscal >> Por Estabelecimento.
Verificar se existe Cadastro da Obrigação Fiscal por Estabelecimento (tabela OBRIGACAO_FISCAL), considerando os critérios:
- Empresa de login;
- Estabelecimento informado na tela de geração;
- Obrigação Fiscal = “108”

Caso não encontre registro, exibir mensagem de erro no Log da Geração:
“Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois não existe Cadastro da Obrigação Fiscal para a Apuração do ICMS – P9 para o estabelecimento informado. Favor criar o cadastro, no módulo Estadual >> Controle das Obrigações Estaduais, menu Obrigações>> Obrigação Fiscal >> Por Estabelecimento.”
Chave: Estabelecimento – Período

Verificar se o Calendário para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:
Verificar se existe calendário para a Apuração do ICMS – P9.
O cadastro do Calendário das Obrigações está localizado no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento.
Verificar se existe Calendário da Obrigação Fiscal por Estabelecimento (tabela CALEND_OBRIGACAO), considerando os critérios:
- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”.

Caso não encontre registro, exibir mensagem de erro no Log da Geração:
“Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois não existe Calendário para a Apuração do ICMS – P9 para o estabelecimento e período informados. Favor criar o calendário, no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento.”
Chave: Estabelecimento – Período

Verificar o Status da Apuração do ICMS
Para realizar a geração, caso exista Apuração do ICMS realizada para o estabelecimento, período e livro (108), esta não pode estar encerrada.
Para isso vamos consultar o Status da Obrigação Fiscal (tabela APURACAO), no módulo Estadual >> ICMS, item de menu Manutenção >> Status das Obrigações. Considerar os seguintes critérios:
- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”
Caso a apuração esteja com Situação = “Apuração Realizada” (campo IND_SITUACAO_APUR = ‘2’) e Validade = “Válido” (campo IND_VALID_APUR = ‘2’), então exibir mensagem de erro no Log da Geração:

“Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois a Apuração do ICMS – P9 encontra-se encerrada para o estabelecimento e período informados. Favor reabrir a apuração, no módulo Estadual >> ICMS, menu Manutenção>> Status das Obrigações.”
Chave: Estabelecimento – Período

TABELA: Apuracao


Parametrização dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG):
Verificar se existe parametrização (Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos) para a Empresa e Estabelecimento foco da geração.

Se não for encontrada parametrização, exibir a seguinte mensagem no Log da Geração:
Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois faltou parametrização para Geração dos Ajustes e Lançamentos para o estabelecimento. Favor incluir  parametrização através da opção de menu Parâmetros >> Ressarcimento ICMS-ST >> Parâmetros p/ Geração dos Ajustes e Lançamentos”.
Chave: Estabelecimento – Período

Verificar registros na tabela SAFX112 – OBSERVAÇÕES DA NOTA FISCAL inseridos via manutenção ou importação:
Não podem existir registros de Observação no período, inseridos via manutenção ou importação, para os códigos de Observação parametrizados via opção “Parâmetros p/ Geração dos Ajustes e Lançamentos”.
Fazer uma consulta na tabela X112_OBS_DOCFIS com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 12 – SAFX112) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”; (*) ou
Código de observação parametrizado para “Estorno de Complemento de ICMS-ST” (*);
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e abortar a geração:

“Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois existem Observações da Nota Fiscal importadas através da SAFX112 para o estabelecimento, período e código de observação informado em Parâmetros p/ Geração dos Ajustes e Lançamentos (vide menu Parâmetros >> Ressarcimento ICMS-ST). Códigos de Observações parametrizados nessa opção não podem ser utilizados na importação da SAFX112.”
Chave: Estabelecimento – Período – Código de Observação

(*) Códigos de observação oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Verificar registros na tabela SAFX113 – AJUSTES DO LANÇAMENTO FISCAL inseridos via manutenção ou importação:
Não podem existir registros de Ajustes no período, inseridos via manutenção ou importação, para os códigos de Observação e Códigos de Ajustes parametrizados via opção “Parâmetros p/ Geração dos Ajustes e Lançamentos”.
Fazer uma consulta na tabela X113_AJUSTE_APUR com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Código de Observação (campo 12 – SAFX113) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”; (*) ou
Código de observação parametrizado para “Estorno de Complemento de ICMS-ST” (*);
- Código de Ajuste (campo 13 – SAFX113) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”; (*) ou
Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”; (*) ou
Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS-ST”; (*) ou
Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”; (*)
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e abortar a geração:

“Não é possível realizar a pré-geração dos registros C195/C197 e Lançamentos na Apuração, pois existem Ajustes de Lançamentos Fiscal importadas através da SAFX113 para o estabelecimento, período, códigos de observação e ajuste informados em Parâmetros p/ Geração dos Ajustes e Lançamentos (vide menu Parâmetros >> Ressarcimento ICMS-ST). Códigos de Observações e ajustes parametrizados nessa opção não podem ser utilizados na importação da SAFX113.”
Chave: Estabelecimento – Período – Código de Observação – Código de Ajuste

(*) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Acontecendo qualquer erro, finalizar a geração com status = “-1” – Erro.


## Processamento


Depois de realizada as críticas, vamos seguir com as etapas de processamento.


### 5.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:


Tabelas:
X112_OBS_DOCFIS – OBSERVAÇÕES DA NOTA FISCAL
X113_AJUSTE_APUR – AJUSTES DO LANÇAMENTO FISCAL
ITEM_APURAC_SUBST: armazena os lançamentos complementares da Apuração do ICMS-ST
ITEM_APURAC_SUBST_X113: vincula o lançamento aos registros de ajustes da X113.

Eliminação das Observações da Nota Fiscal
Excluir os registros resultantes da consulta a tabela X112_OBS_DOCFIS com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 12 – SAFX112) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”; ou
Código de observação parametrizado para “Estorno de Complemento de ICMS-ST”;

(*) Códigos de observação oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Eliminação dos Ajustes do Lançamento Fiscal
Excluir os registros resultantes da consulta a tabela X113_AJUSTE_APUR com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Código de Observação (campo 12 – SAFX113) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”; ou
Código de observação parametrizado para “Estorno de Complemento de ICMS-ST”;
- Código de Ajuste (campo 13 – SAFX113) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”; ou
Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”; ou
Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS-ST”; ou
Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”;
(*) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Eliminação dos Lançamentos Complementares na Tabela de Lançamentos da Apuração do ICMS-ST (ITEM_APURAC_SUBST)
Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado.
- Indicador de Lançamento Digitado/calculado (ind_dig_calculado) = ‘M’ – identificação dos lançamentos gerados por esse processo, diferenciando de outros processos que geram automaticamente lançamentos na apuração ICMS-ST, importação e tela de manutenção.

Eliminação dos Vínculos dos Lançamentos Complementares aos Ajustes da X113 (ITEM_APURAC_SUBST_X113)
Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado.
- Indicador de Lançamento Digitado/calculado (ind_dig_calculado) = ‘M’ – identificação dos lançamentos gerados por esse processo, diferenciando de outros processos que geram automaticamente lançamentos na apuração ICMS-ST, importação e tela de manutenção.



### 5.2 - Etapa 2: Geração das Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)


Nesta etapa, a partir das Devoluções de Saída do período com Estorno de Ressarcimento e Estorno de Complemento, serão geradas as Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113).

Leitura da “Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST (C181 e C186)” (X308_INFO_COMPL_ST_IT_MERC_DEV) para recuperar as Devoluções de Saída do período.

Recuperação das Devoluções de Saída:
Consultar a “Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST (C181 e C186)” (X308_INFO_COMPL_ST_IT_MERC_DEV) para recuperar as Devoluções de Saída do período.
Considerar os seguintes critérios:
- Empresa: de login
- Estabelecimento: informado na tela da geração
- Data Fiscal: pertencente ao período da geração
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Código Motivo igual a MG600, MG800.

Recuperar os campos de Identificação da Capa da Nota Fiscal de Devolução de Saída, o Código do Motivo e os valores de Ressarcimento e Complemento. Veja:

MFS560863: Multiplicar os valores unitários do ICMS-ST e FCP-ST pela quantidade convertida (QTD_CONV)

Totalizar os valores de Ressarcimento e Complemento (campos 43, 44, 45, 46 multiplicados pelo campo 32).

OBS: Uma nota de Devolução de Saída, pode ter N registros na SAFX308. Um item da nota de devolução referente a um produto devolvido, por ter origem em mais de uma nota de saída. Uma nota de devolução pode ter mais de um item, ou seja, mais de um produto devolvido.  Uma única nota de devolução de saída pode ter registros com código de Motivo distintos: MG600, MG800, e MG500.
Veja o exemplo abaixo:

De acordo com o exemplo acima a consulta retornaria os registros:


Processamento das Devoluções de Saída:
Para cada registro recuperado (Capa NF devolução com motivo), executar os procedimentos a seguir:
Para Código de Motivo = MG600 (Estorno de Ressarcimento):
1) Gravar um registro de Observação na X112_OBS_DOCFIS c/ Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”.
2) Gravar um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
- Campo 18 - Valor do ICMS = Valor Unitário ICMS ST Conv Compl (campo 45 - VLR_UNIT_ICMSS_COMPL_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308);
- Campo 13 - Código do Ajuste = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”.

Se Valor Unitário FCP ST Conv Compl (campo 46 - VLR_UNIT_FCP_COMPL_SAI da SAFX308) > 0 então:
3) Gravar um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
-  Campo 18 - Valor do ICMS = Valor Unitário FCP ST Conv Compl (campo 46 - VLR_UNIT_FCP_COMPL_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308);
- Campo 13 - Código do Ajuste = Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”.
4) Gravar um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
- Campo 18 - Valor do ICMS = Valor Unitário FCP ST Conv Compl (campo 46 - VLR_UNIT_FCP_COMPL_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308);
- Campo 13 - Código do Ajuste = Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS-ST”.

Para Código de Motivo = MG800 (Estorno Complemento):
1) Gravar um registro de Observação na X112_OBS_DOCFIS c/ Código de observação parametrizado para “Estorno de Complemento de ICMS-ST”.
2) Gravar um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
-  Campo 18 - Valor do ICMS = Valor Unitário ICMS ST Conv Rest (campo 43 - VLR_UNIT_ICMSS_REST_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308);
-  Campo 13 - Código do Ajuste = Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”.

(*) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Dado o exemplo com as notas 9001 e 9002, veja os registros de observação e ajustes que serão gerados.

Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG):

Resultado:

Gravação das Tabelas:

- Informações da Observações da Nota Fiscal  (SAFX112) p/o C195:



- Informações do Ajustes do Lançamento Fiscal (SAFX113) p/o C197:





### 5.3 – Etapa 3: Geração do Lançamento Complementar na Apuração do ICMS-ST (P9-ST)


Nesta etapa, a partir dos Ajustes do Lançamento Fiscal (SAFX113) do período gerados na etapa 2, serão gerados Lançamentos Complementares na Apuração do ICMS-ST (ITEM_APURAC_SUBST) e Vínculos com Ajustes do Lançamento Fiscal (ITEM_APURAC_SUBST_X113).
Os seguintes códigos de ajustes serão considerados:
- Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”.
- Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”
- Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”.

Recuperação dos Ajustes do Lançamento Fiscal
Consultar a “Tabela de Ajuste do Lançamento Fiscal” (X113_AJUSTE_APUR), com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Movimento Entrada/Saída (MOVTO_E_S) <> ‘9’ (entrada)
- Normal ou Devolução (NORM_DEV) = ‘2’ (devolução)
- Código de Observação (campo 12 – SAFX113) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”; ou
Código de observação parametrizado para “Estorno de Complemento de ICMS-ST”;
- Código de Ajuste (campo 13 – SAFX113) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM” ; ou
Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST” ; ou
Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST” ;

Recuperar o campo 18 - Valor do ICMS totalizado por Código de Ajuste.
O resultado dessa consulta pode retornar até três registros, um para cada código de ajuste.

(*) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu Parâmetros à Ressarcimento ICMS-STà Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG).

Processamento dos Ajustes do Lançamento Fiscal:
Para cada registro recuperado, realizar a gravação do lançamento complementar. Ou seja:
1) Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM:
Gravar um registro de Lançamento Complementar na Apuração do ICMS-ST (ITEM_APURAC_SUBST) com o Valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”.
Gravar na tabela ITEM_APURAC_SUBST_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR para o referido Código de Ajuste, vinculando-os ao Lançamento Complementar.

2) Lançamento de Estorno do FEM adicionada ao ICMS-ST:
Gravar um registro de Lançamento Complementar na Apuração do ICMS-ST (ITEM_APURAC_SUBST) com o valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”.
Gravar na tabela ITEM_APURAC_SUBST_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR para referido Código de Ajuste, vinculando-os ao Lançamento Complementar.

3) Lançamento de Estorno do Complemento de ICMS-ST:
Gravar um registro de Lançamento Complementar na Apuração do ICMS-ST (ITEM_APURAC_SUBST) com o valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”.
Gravar na tabela ITEM_APURAC_SUBST_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR para referido Código de Ajuste, vinculando-os ao Lançamento Complementar.

Dado o exemplo com as notas 9001 e 9002, veja os registros de lançamentos que serão gerados.







Parâmetros p/ Geração dos Ajustes e Lançamentos (tabela EFD_PAR_RESSARC_MG):

Resultado Lançamento na Apuração do ICMS-ST:


Gravação das Tabelas:

- Tabela de Lançamentos da Apuração do ICMS-ST (ITEM_APURAC_SUBST):

Os campos sinalizados com asterisco compõem a chave da tabela.


- Vínculos com Ajustes do Lançamento Fiscal (ITEM_APURAC_SUBST_X113)

Os campos sinalizados com asterisco compõem a chave da tabela.



### 5.4 – Etapa 4: Atualização do Status da Obrigação da Apuração



Gravação da Tabela de Status da Obrigação (APURACAO)
Verificar se existe registro de Status da Obrigação Fiscal (tabela APURACAO), no módulo Estadual >> ICMS, item de menu Manutenção >> Status das Obrigações. Considerar os seguintes critérios:
- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”.
Caso não exista registro, criar um registro com as seguintes informações:
Os campos sinalizados com asterisco compõem a chave da tabela.


### 5.5 – Etapa 5: Geração de Relatório de Conferência Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)

[MFS511653]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré-geração:
Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré-geração seja marcado, disponibilizar os arquivos em formato Excel dos relatórios de conferência dos registros C195 e C197 gerados na etapa 2.

C195:
Nome do arquivo: Relatório_Conferencia_C195_mm_aaaa_cod_estab.csv
Fazer uma leitura na tabela X112_OBS_DOCFIS com as observações das notas de devolução de saída, que foram geradas na etapa 2.
Todos os campos especificados para gravação da SAFX112, devem ser demonstrados no relatório.

C197:
Nome do arquivo: Relatório_Conferencia_C197_mm_aaaa_cod_estab.csv
Fazer uma leitura na tabela X113_AJUSTE_APUR com os ajustes dos lançamentos fiscais das notas de devolução de saída, que foram gerados na etapa 2.
Todos os campos especificados para gravação da SAFX113, devem ser demonstrados no relatório.



### 5.6 – Etapa 6: Geração de Relatório de Conferência dos Lançamentos Complementares na Apuração do ICMS-ST

[MFS511653]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré-geração:
Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré-geração seja marcado, disponibilizar um arquivo formato Excel demonstrando os lançamentos complementares gerados na etapa 3.

Nome do arquivo: Relatório_Conferencia_Lancto_P9_ST_mm_aaaa_cod_estab.csv

Fazer uma leitura na tabela ITEM_APURAC_SUBST com os lançamentos complementares gerados na etapa 3.
Os campos que devem ser apresentados no relatório são:






= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS67658 | Liliane Videira Assaf | Criação da geração dos registros C195/C197 e lançamentos complementares na Apuração do ICMS-ST | 27/07/2021 |
| MFS511653 | Liliane Videira Assaf | Criação check-box “Gerar Relatórios de Conferência” na tela da pré-geração e aplicação na geração dos relatórios dos registros C195, C197 e Lancto_P9_ST (vide etapas 5 e 6) | 07/03/2023 |
| MFS560863 | Liliane Videira Assaf | Hoje a geração só considera os valores unitários do C181 presente nos campos 18 – VL_UNIT_ICMS_ST_CONV_REST, 20 – VL_UNIT_ICMS_ST_CONV_COMPL e 21 – VL_UNIT_FCP_ST_CONV_COMPL, na geração dos ajustes (C197) e lançamentos da apuração (E210). Com essa MFS, passaremos a multiplicar os valores unitários do ICMS-ST e FCP-ST pela quantidade devolvida (campo 03 - QUANT_CONV do C181). Também vamos gerar os ajustes apenas se o valor for maior que zero. | 23/08/2023 |


|  |
| --- |


| ind_situacao_apur | ind_valid_apur |
| --- | --- |
| 1 - Não Apurado 2 - Apuracao realizada 5 - Apuracao reaberta | 1 - Não analizado 2 - Válida 3 - Não válida |


| SAFX308 | SAFX308 | SAFX308 |
| --- | --- | --- |
| 01 | Código da Empresa | COD_EMPRESA |
| 02 | Código do Estabelecimento | COD_ESTAB |
| 03 | Data Escrita Fiscal | DATA_FISCAL |
| 04 | Movimento Entrada / Saída | MOVTO_E_S |
| 05 | Normal ou Devolução | NORM_DEV |
| 06 | Tipo do Documento | COD_DOCTO |
| 07 | Indicador Pessoa Física/Jurídica | IND_FIS_JUR |
| 08 | Código Pessoa Física/Jurídica | COD_FIS_JUR |
| 09 | Número do Documento Fiscal | NUM_DOCFIS |
| 10 | Série do Documento Fiscal | SERIE_DOCFIS |
| 11 | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS |
| 31 | Código Motivo | COD_MOTIVO |
| 32 | MFS560863: Quantidade Convertida | QTD_CONV |
| 43 | Valor Unitário ICMS ST Conv Rest | VLR_UNIT_ICMSS_REST_SAI |
| 44 | Valor Unitário FCP ST Conv Rest | VLR_UNIT_FCP_REST_SAI |
| 45 | Valor Unitário ICMS ST Conv Compl | VLR_UNIT_ICMSS_COMPL_SAI |
| 46 | Valor Unitário FCP ST Conv Compl | VLR_UNIT_FCP_COMPL_SAI |


| NUM_DOCFIS (Devolução) | IND_ PRODUTO | COD_ PRODUTO | NUM_ITEM (Devolução) | NUM_DOCFIS_REF (NF saída orginal) | COD_MOTIVO | QTD_CONV | VLR_UNIT_ICMSS _REST_SAI | VLR_UNIT_FCP _REST_SAI | VLR_UNIT_ICMSS _COMPL_SAI | VLR_UNIT_FCP _COMPL_SAI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9001 | 1 | PROD01 | 1 | 6001 | MG600 | 2 | em branco | em branco | 1,000000 | 0,150000 |
| 9001 | 1 | PROD01 | 1 | 6002 | MG800 | 2 | 26,000000 | 0,500000 | em branco | em branco |
| 9001 | 1 | PROD01 | 1 | 6003 | MG800 | 1 | 0,004000 | 0,000080 | em branco | em branco |
| 9001 | 1 | PROD02 | 2 | 6004 | MG600 | 1 | em branco | em branco | 2,000000 | 0,150000 |
| 9001 | 1 | PROD02 | 2 | 6005 | MG800 | 1 | 22,000000 | 0,520000 | em branco | em branco |
| 9001 | 1 | PROD03 | 3 | 6006 | MG500 | 1 | em branco | em branco | em branco | em branco |
| 9001 | 1 | PROD03 | 4 | 6007 | MG500 | 1 | em branco | em branco | em branco | em branco |
| 9002 | 1 | PROD01 | 1 | 6001 | MG600 | 1 | em branco | em branco | 7,880000 | 0,150000 |
| 9002 | 1 | PROD02 | 2 | 6004 | MG800 | 2 | 26,000000 | 0,500000 | em branco | em branco |
| 9003 | 1 | PROD03 | 1 | 6006 | MG500 | 1 | em branco | em branco | em branco | em branco |
| 9003 | 1 | PROD03 | 2 | 6007 | MG500 | 1 | em branco | em branco | em branco | em branco |


| NUM_DOCFIS (Devolução) | COD_MOTIVO | VLR_UNIT_ICMSS _REST_SAI  x QTD_CONV | VLR_UNIT_FCP _REST_SAI x QTD_CONV | VLR_UNIT_ICMSS _COMPL_SAI x QTD_CONV | VLR_UNIT_FCP _COMPL_SAI x QTD_CONV |
| --- | --- | --- | --- | --- | --- |
| 9001 | MG600 | em branco | em branco | 4,000000 | 0,450000 |
| 9001 | MG800 | 74,004000 | 1,520080 | em branco | em branco |
| 9002 | MG600 | em branco | em branco | 7,880000 | 0,150000 |
| 9002 | MG800 | 52,000000 | 1,000000 | em branco | em branco |


| NUM_DOCFIS (Devolução) | COD_MOTIVO | VLR_UNIT_ICMSS _REST_SAI  x QTD_CONV | VLR_UNIT_FCP _REST_SAI x QTD_CONV | VLR_UNIT_ICMSS _COMPL_SAI x QTD_CONV | VLR_UNIT_FCP _COMPL_SAI x QTD_CONV |
| --- | --- | --- | --- | --- | --- |
| 9001 | MG600 | em branco | em branco | 4,000000 | 0,450000 |
| 9001 | MG800 | 74,004000 | 1,520080 | em branco | em branco |
| 9002 | MG600 | em branco | em branco | 7,880000 | 0,150000 |
| 9002 | MG800 | 52,000000 | 1,000000 | em branco | em branco |


| TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Tipo de Observação | Descrição Complementar |  |
| --- | --- | --- | --- | --- | --- |
| X112 | 9001 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 4 |  |
|  |  | X113 | MG21000018 | 0,45 |  |
|  |  | X113 | MG91000018 | 0,45 |  |
| X112 | 9001 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 74,004 |  |
| X112 | 9002 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 7,88 |  |
|  |  | X113 | MG21000018 | 0,15 |  |
|  |  | X113 | MG91000018 | 0,15 |  |
| X112 | 9002 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 52 |  |


| PK | Item SAFX112 | Item SAFX112 | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- | --- |
| (*) | (*) | 01 | Código da Empresa | COD_EMPRESA | Código da Empresa da Devolução da Saída |
| (*) | (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do Estabelecimento da Devolução da Saída |
| (*) | (*) | 03 | Data da Escrita Fiscal | DATA_FISCAL | Data Fiscal da Devolução da Saída |
| (*) | (*) | 04 | Movimento Entrada/Saída | MOVTO_E_S | Movimento Entrada/Saída da Devolução da Saída |
| (*) | (*) | 05 | Normal ou Devolução | NORM_DEV | Indicador de Normal ou Devolução da Devolução da Saída |
| (*) | (*) | 06 | Tipo do Documento | COD_DOCTO | Código do Tipo de Documento da Devolução da Saída |
| (*) | (*) | 07 | Indicador Pessoa Física/Jurídica | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Devolução da Saída |
| (*) | (*) | 08 | Código/Destinatário/Emitente/ Remetente | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Devolução da Saída |
| (*) | (*) | 09 | Número do Documento Fiscal/ Número do Mapa Resumo de Caixa | NUM_DOCFIS | Número do Documento Fiscal da Devolução da Saída |
|  |  | 10 | Série do Documento Fiscal | SERIE_DOCFIS | Série do Documento Fiscal da Devolução da Saída |
|  |  | 11 | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Devolução da Saída |
| (*) | (*) | 12 | Código da Observação | COD_OBS_LANCTO_FISCAL | Para MG600 preencher com: Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”. Para MG800 preencher com: Código de observação parametrizado para “Estorno de Complemento de ICMS-ST” |
| (*) | (*) | 13 | Tipo de Observação | IND_ICOMPL_LANCTO | Informar: L - Observação referente aos Lançamentos Fiscais da Nota |
|  |  | 14 | Descrição Complementar | DSC_COMPLEMENTAR | Preencher com o período informado na tela de geração, concatenando a palavra “Período”. Veja: “Período: “+ MM/AAAA |
|  |  | 15 | Vinculação | VINCULACAO | Informar: 1 - EFD ICMS/IPI; |


| PK | Item SAFX113 | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa | COD_EMPRESA | Código da Empresa da Devolução da Saída |
| (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do Estabelecimento da Devolução da Saída |
| (*) | 03 | Data da Escrita Fiscal | DATA_FISCAL | Data Fiscal da Devolução da Saída |
| (*) | 04 | Movimento Entrada/Saída | MOVTO_E_S | Movimento Entrada/Saída da Devolução da Saída |
| (*) | 05 | Normal ou Devolução | NORM_DEV | Indicador de Normal ou Devolução da Devolução da Saída |
| (*) | 06 | Tipo do Documento | COD_DOCTO | Código do Tipo de Documento da Devolução da Saída |
| (*) | 07 | Indicador Pessoa Física/Jurídica | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Devolução da Saída |
| (*) | 08 | Código/Destinatário/Emitente/ Remetente | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Devolução da Saída |
| (*) | 09 | Número do Documento Fiscal/ Número do Mapa Resumo de Caixa | NUM_DOCFIS | Número do Documento Fiscal da Devolução da Saída |
|  | 10 | Série do Documento Fiscal | SERIE_DOCFIS | Série do Documento Fiscal da Devolução da Saída |
|  | 11 | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Devolução da Saída |
| (*) | 12 | Código da Observação do Lançamento Fiscal | COD_OBS_LANCTO_FISCAL | Para MG600 preencher com: Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST”. Para MG800 preencher com: Código de observação parametrizado para “Estorno de Complemento de ICMS-ST” |
| (*) | 13 | Código do Ajuste | COD_AJUSTE_SPED | Para MG600 preencher com: - Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS-ST +FEM”. Ou - Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS-ST”. Ou - Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS-ST”. O código é atribuído de acordo com o lançamento que está sendo feito, conforme já explicado no tópico “Processamento das Devoluções de Saída”.  Para MG800 preencher com: - Código de Ajuste parametrizado para “Estorno do Complemento de ICMS-ST”. |
|  | 14 | Descrição Complementar do Ajuste | DSC_COMP_AJUSTE | Não preencher. |
|  | 15 | Número do Item da Nota | NUM_ITEM | Não preencher. |
|  | 16 | Base de Cálculo do ICMS | VLR_BASE_ICMS | Não preencher. |
|  | 17 | Alíquota do ICMS | ALIQUOTA_ICMS | Não preencher. |
|  | 18 | Valor do ICMS | VLR_ICMS | Para MG600 preencher com: - Valor Unitário ICMS ST Conv Compl (campo 45 - VLR_UNIT_ICMSS_COMPL_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308); Ou - Valor Unitário FCP ST Conv Compl (campo 46 - VLR_UNIT_FCP_COMPL_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308); O valor é atribuído de acordo com o lançamento que está sendo feito, conforme já explicado no tópico “Processamento das Devoluções de Saída”.  Para MG800 preencher com: - Valor Unitário ICMS ST Conv Rest (campo 43 - VLR_UNIT_ICMSS_REST_SAI da SAFX308) multiplicado pela Quantidade Convertida (campo 32 – QTD_CONV da SAFX308). |
|  | 19 | Outros Valores | VLR_OUTROS | Não preencher. |


| NUM_DOCFIS (Devolução) | COD_MOTIVO | VLR_UNIT_ICMSS _REST_SAI  x QTD_CONV | VLR_UNIT_FCP _REST_SAI x QTD_CONV | VLR_UNIT_ICMSS _COMPL_SAI x QTD_CONV | VLR_UNIT_FCP _COMPL_SAI x QTD_CONV |
| --- | --- | --- | --- | --- | --- |
| 9001 | MG600 | em branco | em branco | 4,000000 | 0,450000 |
| 9001 | MG800 | 74,004000 | 1,520080 | em branco | em branco |
| 9002 | MG600 | em branco | em branco | 7,880000 | 0,150000 |
| 9002 | MG800 | 52,000000 | 1,000000 | em branco | em branco |


| TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Tipo de Observação | Descrição Complementar |  |
| --- | --- | --- | --- | --- | --- |
| X112 | 9001 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 3 |  |
|  |  | X113 | MG21000018 | 0,3 |  |
|  |  | X113 | MG91000018 | 0,3 |  |
| X112 | 9001 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 48,004 |  |
| X112 | 9002 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 7,88 |  |
|  |  | X113 | MG21000018 | 0,15 |  |
|  |  | X113 | MG91000018 | 0,15 |  |
| X112 | 9002 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 26 |  |


| TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Tipo de Observação | Descrição Complementar |  |
| --- | --- | --- | --- | --- | --- |
| X112 | 9001 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 4 |  |
|  |  | X113 | MG21000018 | 0,45 |  |
|  |  | X113 | MG91000018 | 0,45 |  |
| X112 | 9001 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 74,004 |  |
| X112 | 9002 | 1001 | L | mm/aaaa | Referente ao MG600 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG41000016 | 7,88 |  |
|  |  | X113 | MG21000018 | 0,15 |  |
|  |  | X113 | MG91000018 | 0,15 |  |
| X112 | 9002 | 1002 | L | mm/aaaa | Referente ao MG800 |
|  |  | TABELA | Código Ajuste | Valor do ICMS |  |
|  |  | X113 | MG11000016 | 52 |  |


| Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM | Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM |
| --- | --- |
| Item da Apuração | 002 |
| Descrição do Lançamento | TESTE 01 |
| Classe de Lançamento |  |
| Lançamento de Estorno do FEM adicionado ao ICMS-ST | Lançamento de Estorno do FEM adicionado ao ICMS-ST |
| Item da Apuração | 007 |
| Descrição do Lançamento | TESTE 02 |
| Lançamento de Estorno do Complemento de ICMS-ST | Lançamento de Estorno do Complemento de ICMS-ST |
| Item da Apuração | 006 |
| Descrição do Lançamento | TESTE 03 |


| Tabela | Operação da Apuração | Valor do Lançamento | Descrição do Lançamento |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ITEM_APURAC_SUBST | 002 | 11,88 | TESTE 01 | 4 + 7,88 |  |  |
|  |  | TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Código Ajuste | Valor do ICMS |
|  |  | X113 | 9001 | 1001 | MG41000016 | 4 |
|  |  | X113 | 9002 | 1001 | MG41000016 | 7,88 |
|  |  |  |  |  |  |  |
| ITEM_APURAC_SUBST | 007 | 0,60 | TESTE 02 | 0,45+ 0,15 |  |  |
|  |  | TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Código Ajuste | Valor do ICMS |
|  |  | X113 | 9001 | 1001 | MG21000018 | 0,45 |
|  |  | X113 | 9002 | 1001 | MG21000018 | 0,15 |
|  |  |  |  |  |  |  |
| ITEM_APURAC_SUBST | 006 | 126,004 | TESTE 03 | 74,004 + 52 |  |  |
|  |  | TABELA | NUM_DOCFIS (Devolução) | Código da Observação | Código Ajuste | Valor do ICMS |
|  |  | X113 | 9001 | 1002 | MG11000016 | 74,004 |
|  |  | X113 | 9002 | 1002 | MG11000016 | 52 |


| PK | Campo | Nome na tabela | Regra de preenchimento |
| --- | --- | --- | --- |
| *** | Código da empresa | COD_EMPRESA | Código da empresa do login. |
| *** | Código do estabelecimento | COD_ESTAB | Código do estabelecimento selecionado em tela. |
| *** | Data da Apuração | DAT_APURACAO | Úlitmo dia do mes e ano do Período da informado na tela de geração. |
| *** | Código do Livro | COD_TIPO_LIVRO | Gravar o código ‘108’ |
| *** | Identificador do Estado | IDENT_ESTADO | Identificador do Estado na tabela ESTADO para o código do estado = “MG”. |
| *** | Indicador da UF | IND_UF | Preencher com ‘1’, que significa mesma UF do estabelecimento. |
| *** | Operação da Apuração | COD_OPER_APUR | Recuperar o Código da Operação da Apuração cadastrado na tela de Parâmetros p/ Geração dos Ajustes e Lançamentos (menu Parâmetros à Ressarcimento ICMS-ST) para a empresa e estabelecimento foco da geração. Considerar o campo “Item da Apuração” referente ao lançamento a ser gravado: 1) Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM: 2) Lançamento de Estorno do FEM adicionada ao ICMS-ST 3) Lançamento de Estorno do Complemento de ICMS-ST |
| *** | Número do Lançamento | NUM_DISCRIMINACAO | Sequencial único por Operação da Apuração (COD_OPER_APUR).  Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado (ident_estado), Indicador da UF (ind_uf) e a operação da apuração. |
|  | Valor do Lançamento | VAL_ITEM_DISCRIM | Preencher com o total do campo 18 - Valor do ICMS |
|  | Descrição do Lançamento | DSC_ITEM_APURACAO | Recuperar a Descrição do Lançamento cadastrada na tela de Parâmetros p/ Geração dos Ajustes e Lançamentos (menu Parâmetros à Ressarcimento ICMS-ST) para a empresa e estabelecimento foco da geração. Considerar o campo “Descrição do Lançamento” referente ao lançamento a ser gravado: 1) Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM: 2) Lançamento de Estorno do FEM adicionada ao ICMS-ST 3) Lançamento de Estorno do Complemento de ICMS-ST |
|  | Indicador do Tipo do Lançamento | IND_TIPO_LANC | Gravar com “1”. Este valor significa que o lançamento possui vínculo com os Ajustes do Lançamento Fiscal (SAFX113). |
|  | Indicador de Lançamento Digitado/calculado | IND_DIG_CALCULADO | Gravar com “M”. |
|  |  |  | Demais campos não mencionados não precisam ser preenchidos |


| PK | Campo | Nome na tabela | Regra de preenchimento |
| --- | --- | --- | --- |
| *** | Código da empresa | COD_EMPRESA | Código da empresa do login. |
| *** | Código do estabelecimento | COD_ESTAB | Código do estabelecimento selecionado em tela. |
| *** | Data da Escrita Fiscal | DATA_FISCAL | Data Fiscal do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Movimento Entrada/Saída | MOVTO_E_S | Movimento Entrada/Saída do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Normal ou Devolução | NORM_DEV | Indicador de Normal ou Devolução do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Tipo do Documento | COD_DOCTO | Código do Tipo de Documento do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Indicador Pessoa Física/Jurídica | IND_FIS_JUR | Indicador da Pessoa Fis/Jur do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Código/Destinatário/Emitente/ Remetente | COD_FIS_JUR | Código da Pessoa Fis/Jur do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Número do Documento Fiscal/ Número do Mapa Resumo de Caixa | NUM_DOCFIS | Número do Documento Fiscal do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Série do Documento Fiscal | SERIE_DOCFIS | Série do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS | Subsérie do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Código da Observação | COD_OBS_LANCTO_FISCAL | Código de Observação do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Tipo de Observação | IND_ICOMPL_LANCTO | Informar: L - Observação referente aos Lançamentos Fiscais da Nota |
| *** | Código do Ajuste | COD_AJUSTE_SPED | Código do Ajustes do Lançamento Fiscal recuperados da X113_AJUSTE_APUR |
| *** | Número do Item da Nota | DISCRI_ITEM | Não preencher. |
|  | Código do Livro | COD_TIPO_LIVRO | Gravar o código ‘108’, gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Data da Apuração | DAT_APURACAO | Último dia do mês e ano do Período da informado na tela de geração, gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Identificador do Estado | IDENT_ESTADO | Identificador do Estado na tabela ESTADO para o código do estado = “MG”. Mesmo que foi gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Indicador da UF | IND_UF | Preencher com ‘1’, que significa mesma UF do estabelecimento. Mesmo que foi gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Operação da Apuração | COD_OPER_APUR | Código da Operação da Apuração gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Número do Lançamento | NUM_DISCRIMINACAO | Sequencial gravado no Lançamento Complementar na ITEM_APURAC_SUBST. |
|  | Indicador de Lançamento Digitado/calculado | IND_DIG_CALCULADO | Gravar com “M”. |
|  |  |  | Demais campos não mencionados não precisam ser preenchidos |


| PK | Campo | Nome na tabela | Regra de preenchimento |
| --- | --- | --- | --- |
| *** | Código da empresa | COD_EMPRESA | Código da empresa do login. |
| *** | Código do estabelecimento | COD_ESTAB | Código do estabelecimento selecionado em tela. |
| *** | Data da Apuração | DAT_APURACAO | Úlitmo dia do mes e ano do Período da informado na tela de geração. |
| *** | Código do Livro | COD_TIPO_LIVRO | Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:     Gravar o código ‘165’ Senão     Gravar o código ‘108’ |
|  | Situação | IND_SITUACAO_APUR | Preencher com ‘1’ – Não Apurado |
|  | Validade | IND_VALID_APUR | Preencher com ‘1’ – Não Analisado |
|  | Data da Realização | DAT_REALIZACAO | Data da execução da geração. |


| Campo | Nome na tabela |
| --- | --- |
| Código da empresa | COD_EMPRESA |
| Código do estabelecimento | COD_ESTAB |
| Data da Apuração | DAT_APURACAO |
| Código do Livro | COD_TIPO_LIVRO |
| Operação da Apuração | COD_OPER_APUR |
| Valor do Lançamento | VAL_ITEM_DISCRIM |
| Descrição do Lançamento | DSC_ITEM_APURACAO |
