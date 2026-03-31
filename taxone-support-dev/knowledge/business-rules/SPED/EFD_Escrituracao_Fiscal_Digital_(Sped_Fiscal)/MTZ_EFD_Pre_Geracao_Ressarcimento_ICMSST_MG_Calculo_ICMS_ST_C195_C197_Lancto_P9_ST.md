# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C195_C197_Lancto_P9_ST

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C195_C197_Lancto_P9_ST.docx
- **Modificado:** 2024-04-15
- **Tamanho:** 166 KB

---

THOMSON REUTERS

Módulo Sped Fiscal 

Processamento do Cálculo ICMS\-ST – Registro C195/C197 \+ Lançamentos na Apuração ICMS\-ST 

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré\-Geraçãoà Ressarcimento ICMS\-ST \(Específico MG\) à Pré\-Geração

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS67658__

Liliane Videira Assaf

Criação da geração dos registros C195/C197 e lançamentos complementares na Apuração do ICMS\-ST

27/07/2021

MFS511653

Liliane Videira Assaf

Criação check\-box “Gerar Relatórios de Conferência” na tela da pré\-geração e aplicação na geração dos relatórios dos registros C195, C197 e Lancto\_P9\_ST \(vide etapas 5 e 6\)

07/03/2023

MFS560863

Liliane Videira Assaf

Hoje a geração só considera os valores unitários do C181 presente nos campos 18 – VL\_UNIT\_ICMS\_ST\_CONV\_REST, 20 – VL\_UNIT\_ICMS\_ST\_CONV\_COMPL e 21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL, na geração dos ajustes \(C197\) e lançamentos da apuração \(E210\)\.

Com essa MFS, passaremos a multiplicar os valores unitários do ICMS\-ST e FCP\-ST pela quantidade devolvida \(campo 03 \- QUANT\_CONV do C181\)\.

Também vamos gerar os ajustes apenas se o valor for maior que zero\.

23/08/2023

Sumário

[1\.	Visão Geral	1](#_Toc78383906)

[2\.	Introdução	1](#_Toc78383907)

[3\.	Críticas	1](#_Toc78383908)

[4\.	Processamento	1](#_Toc78383909)

[5\.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:	1](#_Toc78383910)

[5\.2 \- Etapa 2: Geração das Observações \(SAFX112\) e Ajustes do Lançamento Fiscal \(SAFX113\)	1](#_Toc78383911)

[5\.3 – Etapa 3: Geração do Lançamento Complementar na Apuração do ICMS\-ST \(P9\-ST\)	1](#_Toc78383912)

[5\.4 – Etapa 4: Atualização do Status da Obrigação da Apuração	1](#_Toc78383913)

[5\.5 – Etapa 5: Geração de Relatório de Conferência Observações \(SAFX112\) e Ajustes do Lançamento Fiscal \(SAFX113\)	1](#_Toc78383914)

[5\.6 – Etapa 6: Geração de Relatório de Conferência dos Lançamentos Complementares na Apuração do ICMS\-ST	1](#_Toc78383915)

# <a id="_Toc78383906"></a>Visão Geral

Com base nos tópicos 7 e 8 do “__Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo__” as notas de devolução de saída que geram registros C181 com códigos de motivo MG600 \(Estorno de Ressarcimento\) e MG800 \(Estorno de Complemento\), precisam gerar os registros de Observação do Lançamento Fiscal \(C195\) e Ajustes Provenientes do Documento Fiscal \(C197\)\.  E os ajustes \(C197\) que geram crédito ou débito na Apuração do ICMS\-ST, precisam ser consolidados nos campos 07 e 10 do registro E210\.

Esses registros estão organizados na seguinte hierarquia:

C100 – Capa do Documento Fiscal \(Nível 2\)

\.\.\.\. C170 – Item do Documento Fiscal \(Nível 3\)

\.\.\.\. \.\.\.\. C181 – Inf Complementares da Dev\. Saída \(Nível 4\)

\.\.\.\. C195 – Obs Lançamento Fiscal \(Nível 3\)

\.\.\.\. \.\.\.\. C197 – Ajustes Provenientes do Documento Fiscal \(Nível 4\)

 __MFS560863__: Multiplicar os valores unitários do ICMS\-ST e FCP\-ST pela quantidade devolvida \(campo 03 \- QUANT\_CONV\)

Segundo o tópico 07, para cada nota de devolução de saída \(C100\) que gerou pelo menos um registro C181 com Estorno do Ressarcimento \(MG600\), temos que:

Totalizar os valores dos campos \(20 – VL\_UNIT\_ICMS\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV\) e \(21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV\) dos registros C181 com COD\_MOTIVO = ‘MG600’\.

Gerar os seguintes registros:

- C195 com código de observação definida pelo contribuinte referente a “Estorno de Restituição/Ressarcimento de ICMS ST – Aspecto Quantitativo”;
- C197 com código de ajuste igual a “MG41000016” com o valor total do campo 20 – VL\_UNIT\_ICMS\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV;

Se houver parcela do FCP adicionado ao ICMS\-ST, ou seja, se o valor total do campo 21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL for maior que zero, então gerar os registros:

- C197 com código de ajuste igual a “MG21000018” com o valor total do campo 21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV;
- C197 com código de ajuste igual a “MG91000018” com o valor total do campo 21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV;

Já de acordo com o tópico 08, para cada nota de devolução de saída \(C100\) que gerou pelo menos um registro C181 com Estorno do Complemento \(MG800\), precisamos:

Totalizar os valores 18 – VL\_UNIT\_ICMS\_ST\_CONV\_REST x 03 \- QUANT\_CONV dos registros C181 com COD\_MOTIVO = ‘MG800’\.

Gerar os seguintes registros:

- C195 com código de observação definida pelo contribuinte referente a “Estorno de Complemento do Imposto ICMS ST – Aspecto Quantitativo”;
- C197 com código de ajuste igual a “MG11000016” com o valor total do campo 18 – VL\_UNIT\_ICMS\_ST\_CONV\_REST x 03 \- QUANT\_CONV;

Em termos de Apuração do ICMS\-ST, serão realizados os seguintes lançamentos complementares:

- Somatório dos registros C197 com código de ajuste igual a “MG41000016” \(valor do campo 20 – VL\_UNIT\_ICMS\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV\) è Gera 1 lançamento em Outros Débitos \(E210 \-10\)
- Somatório dos registros C197 com código de ajuste igual a “MG21000018” \(valor do campo 21 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL x 03 \- QUANT\_CONV\) è Gera 1 lançamento em Estorno Débitos \(E210 \-07\)
- Somatório dos registros C197 com código de ajuste igual a “MG11000016” \(valor do campo 18 – VL\_UNIT\_ICMS\_ST\_CONV\_REST x 03 \- QUANT\_CONV\) è Gera 1 lançamento em Outros Créditos \(E210 \-07\)

Obs: O ajuste com código igual a “MG91000018” é apenas informativo, logo não compõe a Apuração do ICMS\-ST\.

Nota: Esses códigos e ajustes não serão tratados fixos na solução\.  Disponibilizamos uma tela de parametrização onde o usuário irá definir os Códigos de Observação do C195, os Códigos de Ajuste do C197 \(“MG41000016”\.\.\.\), os códigos de operação da apuração para atribuição dos lançamentos complementares \(operação 002 – Outros Debitos, 003 – Estorno de Crédito , \.\.\.\)

Base Legal: __Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo – versão 05\.__

# <a id="_Toc78383907"></a>Introdução

Essa geração será executada quando na tela de geração o parâmetro “__*C195/C197 – Observação/Ajuste e Lançamento Complementar na Apuração ICMS\-ST*__” estiver marcado\.

Esse processo consiste em gravar os registros C195 e C197 nas tabelas SAFX específicas para geração destes registros do Sped Fiscal\. São elas:

     SAFX112 – OBSERVAÇÕES DA NOTA FISCAL \(corresponde ao C195, registro “filho” do C100\);

     SAFX113 – AJUSTES DO LANÇAMENTO FISCAL \(corresponde ao C197, registro “filho” do C195\);

Realizar os lançamentos complementares na Apuração do ICMS\-ST e associá\-los aos ajustes \(SAFX113\)\. As seguintes tabelas serão povoadas:

    ITEM\_APURAC\_SUBST: armazena os lançamentos complementares da Apuração do ICMS\-ST

    ITEM\_APURAC\_SUBST\_X113: vincula o lançamento aos registros de ajustes da X113\.

Os códigos de observação para geração dos registros na SAFX112 \(C195\), os códigos de ajustes da SAFX113 \(C197\) e os códigos de operação para os lançamentos na apuração, serão definidos pelo usuário através da tela de parametrização disponível no menu “*Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/Geração dos Ajustes e Lançamentos*” \(tabela EFD\_PAR\_RESSARC\_MG\)\.

Após a execução da Pré\-Geração Ressarcimento ICMS\-ST \(Específico MG\) e ANTES da Geração do Meio Magnético do SPED FISCAL, é necessário que o usuário realize a Apuração do ICMS \(P9\), no módulo ICMS, para recalcular os totais do resumo da Substituição Tributária\. Este procedimento já é adotado no DW, quando utiliza o Módulo Lançamentos Automáticos ICMS para gerar automaticamente lançamentos na apuração do ICMS e quando criamos manualmente lançamentos no módulo ICMS\. Em ambas as situações, após a criação dos lançamentos, a Apuração do ICMS deve ser executada\.

O Resumo da Apuração do ICMS\-ST serão recalculados a partir dos lançamentos\. Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBST__ são consolidados por código de operação, atualizando os códigos de operação do Resumo da Apuração do ICMS\-ST \(RESUMO\_APUR\_ST\)\.

Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS\. 

Os registros de observação e ajustes gerados nas tabelas SAFX112 e SAFX113 podem ser conferidos via tela de manutenção no módulo Básicos >> Data Warehouse, menu Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria \(Versão Anterior\) aba Observações do Lançamento Fiscal\.

Os lançamentos complementares gerados na Apuração do ICMS\-ST podem ser conferidos via tela de manutenção no módulo Estadual >> ICMS, menu Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF\.

Obs: Geração por Inscrição Estadual Única não está sendo tratada\.

# <a id="_Toc78383908"></a>Críticas 

Os Pré\-requisitos para essa geração são:

- Criar um calendário para a Apuração do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\. 

O estabelecimento e período da geração deve possuir cadastro do Calendário para a Apuração do ICMS, utilizando como código da obrigação 108\.

- Parametrizar os códigos de observação, os códigos de ajustes e lançamentos na tela de parametrização \(*item de menu Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos\)*, disponível neste módulo\.

Antes de inicia o processamento, vamos checar se esses passos foram feitos\. Caso encontre alguma falha nestas verificações, o processo será abortado\.

Verificar se o Cadastro da Obrigação Fiscal para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:

Verificar se existe Cadastro da Obrigação Fiscal para a Apuração do ICMS – P9\.

O cadastro da Obrigação Fiscal está localizado no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Obrigação Fiscal >> Por Estabelecimento\.

Verificar se existe Cadastro da Obrigação Fiscal por Estabelecimento \(tabela OBRIGACAO\_FISCAL\), considerando os critérios: 

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Obrigação Fiscal = “108”

                               

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois não existe Cadastro da Obrigação Fiscal para a Apuração do ICMS – P9 para o estabelecimento informado\. Favor criar o cadastro, no módulo Estadual >> Controle das Obrigações Estaduais, menu Obrigações>> Obrigação Fiscal >> Por Estabelecimento\.”*

Chave: Estabelecimento – Período

Verificar se o Calendário para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:

Verificar se existe calendário para a Apuração do ICMS – P9\.

O cadastro do Calendário das Obrigações está localizado no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.

Verificar se existe Calendário da Obrigação Fiscal por Estabelecimento \(tabela CALEND\_OBRIGACAO\), considerando os critérios: 

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”\.

                               

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois não existe Calendário para a Apuração do ICMS – P9 para o estabelecimento e período informados\. Favor criar o calendário, no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.”*

Chave: Estabelecimento – Período

Verificar o Status da Apuração do ICMS

Para realizar a geração, caso exista Apuração do ICMS realizada para o estabelecimento, período e livro \(108\), esta não pode estar encerrada\.

Para isso vamos consultar o Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manutenção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”

Caso a apuração esteja com Situação = “Apuração Realizada” \(campo IND\_SITUACAO\_APUR = ‘2’\) e Validade = “Válido” \(campo IND\_VALID\_APUR = ‘2’\), então exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois a Apuração do ICMS – P9 encontra\-se encerrada para o estabelecimento e período informados\. Favor reabrir a apuração, no módulo Estadual >> ICMS, menu Manutenção>> Status das Obrigações\.”*

Chave: Estabelecimento – Período 

TABELA: Apuracao 

ind\_situacao\_apur 

ind\_valid\_apur

1 \- Não Apurado

2 \- Apuracao realizada

5 \- Apuracao reaberta

1 \- Não analizado

2 \- Válida

3 \- Não válida

Parametrização dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\):

Verificar se existe parametrização \(*Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos\)* para a Empresa e Estabelecimento foco da geração\.

Se não for encontrada parametrização, exibir a seguinte mensagem no Log da Geração:

*Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois faltou parametrização para Geração dos Ajustes e Lançamentos para o estabelecimento\. Favor incluir  parametrização através da opção de menu Parâmetros >> Ressarcimento ICMS\-ST >> Parâmetros p/ Geração dos Ajustes e Lançamentos”\.*

Chave: Estabelecimento – Período

Verificar registros na tabela SAFX112 – OBSERVAÇÕES DA NOTA FISCAL inseridos via manutenção ou importação:

Não podem existir registros de Observação no período, inseridos via manutenção ou importação, para os códigos de Observação parametrizados via opção “Parâmetros p/ Geração dos Ajustes e Lançamentos”\.

Fazer uma consulta na tabela X112\_OBS\_DOCFIS com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data Fiscal data enquadrada no período informado em tela;

   \- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

   \- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

   \- Tipo de Observação \(campo 13 – SAFX112\) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”

   \- Código de Observação \(campo 12 – SAFX112\) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”; \(\*\) ou 

                                                                                     Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST” \(\*\);

   \- IND\_GRAVACAO <> '0', '6','7','8'\. \(caso que foi incluído via digitação ou importação\)

Caso a consulta acima retorne registro, dar mensagem e abortar a geração:

*“Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois existem Observações da Nota Fiscal importadas através da SAFX112 para o estabelecimento, período e código de observação informado em Parâmetros p/ Geração dos Ajustes e Lançamentos \(vide menu Parâmetros >> Ressarcimento ICMS\-ST\)\. Códigos de Observações parametrizados nessa opção não podem ser utilizados na importação da SAFX112\.”*

            Chave: Estabelecimento – Período – Código de Observação

\(\*\) Códigos de observação oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

Verificar registros na tabela SAFX113 – AJUSTES DO LANÇAMENTO FISCAL inseridos via manutenção ou importação:

Não podem existir registros de Ajustes no período, inseridos via manutenção ou importação, para os códigos de Observação e Códigos de Ajustes parametrizados via opção “Parâmetros p/ Geração dos Ajustes e Lançamentos”\.

Fazer uma consulta na tabela X113\_AJUSTE\_APUR com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data Fiscal data enquadrada no período informado em tela;

   \- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

   \- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

   \- Código de Observação \(campo 12 – SAFX113\) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”; \(\*\) ou 

                                                                                     Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST” \(\*\); 

    \- Código de Ajuste \(campo 13 – SAFX113\) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”; \(\*\) ou

                                                                            Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”; \(\*\) ou

                                                                            Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS\-ST”; \(\*\) ou

                                                                            Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”; \(\*\) 

   \- IND\_GRAVACAO <> '0', '6','7','8'\. \(caso que foi incluído via digitação ou importação\)

Caso a consulta acima retorne registro, dar mensagem e abortar a geração:

*“Não é possível realizar a pré\-geração dos registros C195/C197 e Lançamentos na Apuração, pois existem Ajustes de Lançamentos Fiscal importadas através da SAFX113 para o estabelecimento, período, códigos de observação e ajuste informados em Parâmetros p/ Geração dos Ajustes e Lançamentos \(vide menu Parâmetros >> Ressarcimento ICMS\-ST\)\. Códigos de Observações e ajustes parametrizados nessa opção não podem ser utilizados na importação da SAFX113\.”*

            Chave: Estabelecimento – Período – Código de Observação – Código de Ajuste

\(\*\) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc78383909"></a>Processamento

Depois de realizada as críticas, vamos seguir com as etapas de processamento\.

## <a id="_Toc78383910"></a>5\.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:

Tabelas:

     X112\_OBS\_DOCFIS – OBSERVAÇÕES DA NOTA FISCAL

     X113\_AJUSTE\_APUR – AJUSTES DO LANÇAMENTO FISCAL 

    ITEM\_APURAC\_SUBST: armazena os lançamentos complementares da Apuração do ICMS\-ST

    ITEM\_APURAC\_SUBST\_X113: vincula o lançamento aos registros de ajustes da X113\.

__Eliminação das Observações da Nota Fiscal__

Excluir os registros resultantes da consulta a tabela X112\_OBS\_DOCFIS com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data Fiscal data enquadrada no período informado em tela;

   \- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

   \- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

   \- Tipo de Observação \(campo 13 – SAFX112\) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”

   \- Código de Observação \(campo 12 – SAFX112\) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”; ou 

                                                                                     Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”;

\(\*\) Códigos de observação oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

   

__Eliminação dos Ajustes do Lançamento Fiscal__

Excluir os registros resultantes da consulta a tabela X113\_AJUSTE\_APUR com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data Fiscal data enquadrada no período informado em tela;

   \- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

   \- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

   \- Código de Observação \(campo 12 – SAFX113\) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”; ou 

                                                                                     Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”;

    \- Código de Ajuste \(campo 13 – SAFX113\) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”; ou

                                                                            Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”; ou

                                                                            Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS\-ST”; ou

                                                                            Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”; 

\(\*\) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

__Eliminação dos Lançamentos Complementares na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘M’__ – identificação dos lançamentos gerados por esse processo, diferenciando de outros processos que geram automaticamente lançamentos na apuração ICMS\-ST, importação e tela de manutenção\.

__Eliminação dos Vínculos dos Lançamentos Complementares aos Ajustes da X113 \(ITEM\_APURAC\_SUBST\_X113\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘M’__ – identificação dos lançamentos gerados por esse processo, diferenciando de outros processos que geram automaticamente lançamentos na apuração ICMS\-ST, importação e tela de manutenção\.

## <a id="_Toc78383911"></a>5\.2 \- Etapa 2: Geração das Observações \(SAFX112\) e Ajustes do Lançamento Fiscal \(SAFX113\)

Nesta etapa, a partir das Devoluções de Saída do período com Estorno de Ressarcimento e Estorno de Complemento, serão geradas as Observações \(SAFX112\) e Ajustes do Lançamento Fiscal \(SAFX113\)\.

Leitura da “Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\)” \(X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\) para recuperar as Devoluções de Saída do período\. 

__Recuperação das Devoluções de Saída:__

Consultar a “Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\)” \(X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\) para recuperar as Devoluções de Saída do período\. 

Considerar os seguintes critérios:

\- Empresa: de login

\- Estabelecimento: informado na tela da geração

\- Data Fiscal: pertencente ao período da geração

\- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

\- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

\- Código Motivo igual a MG600, MG800\.

Recuperar os campos de Identificação da Capa da Nota Fiscal de Devolução de Saída, o Código do Motivo e os valores de Ressarcimento e Complemento\. Veja:

SAFX308 

01

Código da Empresa 

COD\_EMPRESA

02

Código do Estabelecimento

COD\_ESTAB

03

Data Escrita Fiscal

DATA\_FISCAL

04

Movimento Entrada / Saída

MOVTO\_E\_S

05

Normal ou Devolução

NORM\_DEV

06

Tipo do Documento

COD\_DOCTO

07

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

08

Código Pessoa Física/Jurídica

COD\_FIS\_JUR

09

Número do Documento Fiscal

NUM\_DOCFIS

10

Série do Documento Fiscal

SERIE\_DOCFIS

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

31

Código Motivo

COD\_MOTIVO

32

__MFS560863:__

Quantidade Convertida

QTD\_CONV

43

Valor Unitário ICMS ST Conv Rest

VLR\_UNIT\_ICMSS\_REST\_SAI

44

Valor Unitário FCP ST Conv Rest

VLR\_UNIT\_FCP\_REST\_SAI

45

Valor Unitário ICMS ST Conv Compl

VLR\_UNIT\_ICMSS\_COMPL\_SAI

46

Valor Unitário FCP ST Conv Compl

VLR\_UNIT\_FCP\_COMPL\_SAI

__MFS560863__: Multiplicar os valores unitários do ICMS\-ST e FCP\-ST pela quantidade convertida \(QTD\_CONV\)

Totalizar os valores de Ressarcimento e Complemento \(campos 43, 44, 45, 46 multiplicados pelo campo 32\)\.

OBS: Uma nota de Devolução de Saída, pode ter N registros na SAFX308\. Um item da nota de devolução referente a um produto devolvido, por ter origem em mais de uma nota de saída\. Uma nota de devolução pode ter mais de um item, ou seja, mais de um produto devolvido\.  Uma única nota de devolução de saída pode ter registros com código de Motivo distintos: MG600, MG800, e MG500\. 

Veja o exemplo abaixo:

__NUM\_DOCFIS  
\(Devolução\)__

IND\_  
PRODUTO

COD\_  
PRODUTO

NUM\_ITEM  
\(Devolução\)

NUM\_DOCFIS\_REF  
\(NF saída orginal\)

COD\_MOTIVO

QTD\_CONV

VLR\_UNIT\_ICMSS  
\_REST\_SAI

VLR\_UNIT\_FCP  
\_REST\_SAI

VLR\_UNIT\_ICMSS  
\_COMPL\_SAI

VLR\_UNIT\_FCP  
\_COMPL\_SAI

9001

1

PROD01

1

6001

MG600

2

em branco

em branco

1,000000

0,150000

9001

1

PROD01

1

6002

MG800

2

26,000000

0,500000

em branco

em branco

9001

1

PROD01

1

6003

MG800

1

0,004000

0,000080

em branco

em branco

9001

1

PROD02

2

6004

MG600

1

em branco

em branco

2,000000

0,150000

9001

1

PROD02

2

6005

MG800

1

22,000000

0,520000

em branco

em branco

9001

1

PROD03

3

6006

__MG500__

1

em branco

em branco

em branco

em branco

9001

1

PROD03

4

6007

__MG500__

1

em branco

em branco

em branco

em branco

9002

1

PROD01

1

6001

__MG600__

1

em branco

em branco

7,880000

0,150000

9002

1

PROD02

2

6004

__MG800__

2

26,000000

0,500000

em branco

em branco

9003

1

PROD03

1

6006

__MG500__

1

em branco

em branco

em branco

em branco

9003

1

PROD03

2

6007

__MG500__

1

em branco

em branco

em branco

em branco

De acordo com o exemplo acima a consulta retornaria os registros:

__NUM\_DOCFIS  
\(Devolução\)__

COD\_MOTIVO

VLR\_UNIT\_ICMSS  
\_REST\_SAI 

x QTD\_CONV

VLR\_UNIT\_FCP  
\_REST\_SAI

x QTD\_CONV

VLR\_UNIT\_ICMSS  
\_COMPL\_SAI

x QTD\_CONV

VLR\_UNIT\_FCP  
\_COMPL\_SAI

x QTD\_CONV

9001

MG600

em branco

em branco

4,000000

0,450000

9001

MG800

74,004000

1,520080

em branco

em branco

9002

__MG600__

em branco

em branco

7,880000

0,150000

9002

__MG800__

52,000000

1,000000

em branco

em branco

__Processamento das Devoluções de Saída:__

Para *cada registro *recuperado *\(Capa NF devolução com motivo\)*, executar os procedimentos a seguir:

    Para Código de Motivo = __MG600__ \(Estorno de Ressarcimento\):

    1\) Gravar um registro de Observação na X112\_OBS\_DOCFIS c/ Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”\.

    2\) Gravar um registro de Ajuste do Lançamento Fiscal na X113\_AJUSTE\_APUR considerando:

         \- Campo 18 \- Valor do ICMS = Valor Unitário ICMS ST Conv Compl \(campo 45 \- VLR\_UNIT\_ICMSS\_COMPL\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

         \- Campo 13 \- Código do Ajuste = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”\.

    Se Valor Unitário FCP ST Conv Compl \(campo 46 \- VLR\_UNIT\_FCP\_COMPL\_SAI da SAFX308\) > 0 então:

    3\) Gravar um registro de Ajuste do Lançamento Fiscal na X113\_AJUSTE\_APUR considerando:

         \-  Campo 18 \- Valor do ICMS = Valor Unitário FCP ST Conv Compl \(campo 46 \- VLR\_UNIT\_FCP\_COMPL\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

         \- Campo 13 \- Código do Ajuste = Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”\.

    4\) Gravar um registro de Ajuste do Lançamento Fiscal na X113\_AJUSTE\_APUR considerando:

        \- Campo 18 \- Valor do ICMS = Valor Unitário FCP ST Conv Compl \(campo 46 \- VLR\_UNIT\_FCP\_COMPL\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

        \- Campo 13 \- Código do Ajuste = Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS\-ST”\.

    

    Para Código de Motivo = __MG800 __\(Estorno Complemento\):

    1\) Gravar um registro de Observação na X112\_OBS\_DOCFIS c/ Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”\.

    2\) Gravar um registro de Ajuste do Lançamento Fiscal na X113\_AJUSTE\_APUR considerando:

     \-  Campo 18 \- Valor do ICMS = Valor Unitário ICMS ST Conv Rest \(campo 43 \- VLR\_UNIT\_ICMSS\_REST\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

     \-  Campo 13 \- Código do Ajuste = Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”\.

\(\*\) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

Dado o exemplo com as notas 9001 e 9002, veja os registros de observação e ajustes que serão gerados\.

__NUM\_DOCFIS  
\(Devolução\)__

COD\_MOTIVO

VLR\_UNIT\_ICMSS  
\_REST\_SAI 

x QTD\_CONV

VLR\_UNIT\_FCP  
\_REST\_SAI

x QTD\_CONV

VLR\_UNIT\_ICMSS  
\_COMPL\_SAI

x QTD\_CONV

VLR\_UNIT\_FCP  
\_COMPL\_SAI

x QTD\_CONV

9001

MG600

em branco

em branco

4,000000

0,450000

9001

MG800

74,004000

1,520080

em branco

em branco

9002

__MG600__

em branco

em branco

7,880000

0,150000

9002

__MG800__

52,000000

1,000000

em branco

em branco

Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\):

![](data:image/png;base64,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)

Resultado:

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Tipo de Observação__

__Descrição Complementar__

 

X112

__9001__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

4

 

 

X113

MG21000018

0,45

 

 

X113

MG91000018

0,45

 

X112

__9001__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG11000016

74,004

 

X112

__9002__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

7,88

 

 

X113

MG21000018

0,15

 

 

X113

MG91000018

0,15

 

X112

__9002__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

 

X113

MG11000016

52

 

__Gravação das Tabelas:__

__ \- Informações da Observações da Nota Fiscal  \(SAFX112\) p/o C195: __

PK

Item

SAFX112

Campo

Regra de Preenchimento

\(\*\)

01

Código da Empresa

COD\_EMPRESA

Código da Empresa da Devolução da Saída

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do Estabelecimento da Devolução da Saída

\(\*\)

03

Data da Escrita Fiscal

DATA\_FISCAL

Data Fiscal da Devolução da Saída

\(\*\)

04

Movimento Entrada/Saída

MOVTO\_E\_S

Movimento Entrada/Saída da Devolução da Saída  


\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicador de Normal ou Devolução da Devolução da Saída

\(\*\)

06

Tipo do Documento

COD\_DOCTO

Código do Tipo de Documento da Devolução da Saída

\(\*\)

07

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

Indicador de Pessoa Física/Jurídica da Devolução da Saída  


\(\*\)

08

Código/Destinatário/Emitente/ Remetente

COD\_FIS\_JUR

Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Devolução da Saída

\(\*\)

09

Número do Documento Fiscal/ Número do Mapa Resumo de Caixa

NUM\_DOCFIS

Número do Documento Fiscal da Devolução da Saída

 

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do Documento Fiscal da Devolução da Saída

 

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal da Devolução da Saída

\(\*\)

12

Código da Observação

COD\_OBS\_LANCTO\_FISCAL

Para __MG600__ preencher com:

Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”\.

Para __MG800__ preencher com:

Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”

\(\*\)

13

Tipo de Observação

IND\_ICOMPL\_LANCTO

Informar:  
L \- Observação referente aos Lançamentos Fiscais da Nota 

 

14

Descrição Complementar

DSC\_COMPLEMENTAR

Preencher com o período informado na tela de geração, concatenando a palavra “Período”\. Veja:

“Período: “\+ MM/AAAA

 

15

Vinculação

VINCULACAO

Informar:  
1 \- EFD ICMS/IPI;

__   \- Informações do Ajustes do Lançamento Fiscal \(SAFX113\) p/o C197: __

PK

Item

SAFX113

Campo

Regra de Preenchimento

\(\*\)

01

Código da Empresa

COD\_EMPRESA

Código da Empresa da Devolução da Saída

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do Estabelecimento da Devolução da Saída

\(\*\)

03

Data da Escrita Fiscal

DATA\_FISCAL

Data Fiscal da Devolução da Saída

\(\*\)

04

Movimento Entrada/Saída

MOVTO\_E\_S

Movimento Entrada/Saída da Devolução da Saída  


\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicador de Normal ou Devolução da Devolução da Saída

\(\*\)

06

Tipo do Documento

COD\_DOCTO

Código do Tipo de Documento da Devolução da Saída

\(\*\)

07

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

Indicador de Pessoa Física/Jurídica da Devolução da Saída  


\(\*\)

08

Código/Destinatário/Emitente/ Remetente

COD\_FIS\_JUR

Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Devolução da Saída

\(\*\)

09

Número do Documento Fiscal/ Número do Mapa Resumo de Caixa

NUM\_DOCFIS

Número do Documento Fiscal da Devolução da Saída

 

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do Documento Fiscal da Devolução da Saída

 

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal da Devolução da Saída

\(\*\)

12

Código da Observação do Lançamento Fiscal

COD\_OBS\_LANCTO\_FISCAL

Para __MG600__ preencher com:

Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”\.

Para __MG800__ preencher com:

Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”

\(\*\)

13

Código do Ajuste

COD\_AJUSTE\_SPED

Para __MG600__ preencher com:

\- Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”\.

Ou

\- Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”\.

Ou

\- Código de Ajuste parametrizado para “Informativo FEM adicionada ao ICMS\-ST”\.

O código é atribuído de acordo com o lançamento que está sendo feito, conforme já explicado no tópico “Processamento das Devoluções de Saída”\. 

Para __MG800__ preencher com:

\- Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”\.

 

14

Descrição Complementar do Ajuste

DSC\_COMP\_AJUSTE

Não preencher\. 

 

15

Número do Item da Nota

NUM\_ITEM

Não preencher\.

 

16

Base de Cálculo do ICMS

VLR\_BASE\_ICMS

Não preencher\.

 

17

Alíquota do ICMS

ALIQUOTA\_ICMS

Não preencher\.

 

18

Valor do ICMS

VLR\_ICMS

Para __MG600__ preencher com:

\- Valor Unitário ICMS ST Conv Compl \(campo 45 \- VLR\_UNIT\_ICMSS\_COMPL\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

Ou

\- Valor Unitário FCP ST Conv Compl \(campo 46 \- VLR\_UNIT\_FCP\_COMPL\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\);

O valor é atribuído de acordo com o lançamento que está sendo feito, conforme já explicado no tópico “Processamento das Devoluções de Saída”\. 

Para __MG800__ preencher com:

\- Valor Unitário ICMS ST Conv Rest \(campo 43 \- VLR\_UNIT\_ICMSS\_REST\_SAI da SAFX308\) multiplicado pela Quantidade Convertida \(campo 32 – QTD\_CONV da SAFX308\)\.

 

19

Outros Valores

VLR\_OUTROS

Não preencher\.

## <a id="_Toc78383912"></a>5\.3 – Etapa 3: Geração do Lançamento Complementar na Apuração do ICMS\-ST \(P9\-ST\)

Nesta etapa, a partir dos Ajustes do Lançamento Fiscal \(SAFX113\) do período gerados na etapa 2, serão gerados Lançamentos Complementares na Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\) e Vínculos com Ajustes do Lançamento Fiscal \(ITEM\_APURAC\_SUBST\_X113\)\.

Os seguintes códigos de ajustes serão considerados:

 \- Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”\.

 \- Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”

 \- Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”\.

__Recuperação dos Ajustes do Lançamento Fiscal__

Consultar a “Tabela de Ajuste do Lançamento Fiscal” \(X113\_AJUSTE\_APUR\), com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data Fiscal data enquadrada no período informado em tela;

   \- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> ‘9’ \(entrada\)

   \- Normal ou Devolução \(NORM\_DEV\) = ‘2’ \(devolução\)

   \- Código de Observação \(campo 12 – SAFX113\) = Código de Observação parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST”; ou 

                                                                                     Código de observação parametrizado para “Estorno de Complemento de ICMS\-ST”;

    \- Código de Ajuste \(campo 13 – SAFX113\) = Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM” ; ou

                                                                            Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST” ; ou

                                                                            Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST” ; 

Recuperar o campo 18 \- Valor do ICMS totalizado por Código de Ajuste\.

O resultado dessa consulta pode retornar até três registros, um para cada código de ajuste\.

\(\*\) Códigos de observação e de ajustes oriundos da tela de parametrização disponível no menu *Parâmetros à Ressarcimento ICMS\-STà Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\)\.*

__Processamento dos Ajustes do Lançamento Fiscal:__

Para cada registro recuperado, realizar a gravação do lançamento complementar\. Ou seja:

1\) Lançamento de Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM:

 Gravar um registro de Lançamento Complementar na Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\) com o Valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM”\.

 Gravar na tabela ITEM\_APURAC\_SUBST\_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR para o referido Código de Ajuste, vinculando\-os ao Lançamento Complementar\.

2\) Lançamento de Estorno do FEM adicionada ao ICMS\-ST:

Gravar um registro de Lançamento Complementar na Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\) com o valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno do FEM adicionada ao ICMS\-ST”\.

Gravar na tabela ITEM\_APURAC\_SUBST\_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR para referido Código de Ajuste, vinculando\-os ao Lançamento Complementar\.

3\) Lançamento de Estorno do Complemento de ICMS\-ST:

Gravar um registro de Lançamento Complementar na Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\) com o valor do ICMS totalizado para o Código de Ajuste parametrizado para “Estorno do Complemento de ICMS\-ST”\.

Gravar na tabela ITEM\_APURAC\_SUBST\_X113, todos os Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR para referido Código de Ajuste, vinculando\-os ao Lançamento Complementar\.

Dado o exemplo com as notas 9001 e 9002, veja os registros de lançamentos que serão gerados\.

__NUM\_DOCFIS  
\(Devolução\)__

COD\_MOTIVO

VLR\_UNIT\_ICMSS  
\_REST\_SAI 

x QTD\_CONV

VLR\_UNIT\_FCP  
\_REST\_SAI

x QTD\_CONV

VLR\_UNIT\_ICMSS  
\_COMPL\_SAI

x QTD\_CONV

VLR\_UNIT\_FCP  
\_COMPL\_SAI

x QTD\_CONV

9001

MG600

em branco

em branco

4,000000

0,450000

9001

MG800

74,004000

1,520080

em branco

em branco

9002

__MG600__

em branco

em branco

7,880000

0,150000

9002

__MG800__

52,000000

1,000000

em branco

em branco

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Tipo de Observação__

__Descrição Complementar__

 

X112

__9001__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

3

 

 

X113

MG21000018

0,3

 

 

X113

MG91000018

0,3

 

X112

__9001__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG11000016

48,004

 

X112

__9002__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

7,88

 

 

X113

MG21000018

0,15

 

 

X113

MG91000018

0,15

 

X112

__9002__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

 

X113

MG11000016

26

 

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Tipo de Observação__

__Descrição Complementar__

 

X112

__9001__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

4

 

 

X113

MG21000018

0,45

 

 

X113

MG91000018

0,45

 

X112

__9001__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG11000016

74,004

 

X112

__9002__

1001

L

mm/aaaa

           Referente ao MG600

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

X113

MG41000016

7,88

 

 

X113

MG21000018

0,15

 

 

X113

MG91000018

0,15

 

X112

__9002__

1002

L

mm/aaaa

           Referente ao MG800

 

__TABELA__

__Código Ajuste__

__Valor do ICMS__

 

 

 

X113

MG11000016

52

 

Parâmetros p/ Geração dos Ajustes e Lançamentos \(tabela EFD\_PAR\_RESSARC\_MG\):

__Lançamento de Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM__

Item da Apuração

002

Descrição do Lançamento

TESTE 01

Classe de Lançamento

 

__Lançamento de Estorno do FEM adicionado ao ICMS\-ST__

Item da Apuração

007

Descrição do Lançamento

TESTE 02

__Lançamento de Estorno do Complemento de ICMS\-ST__

Item da Apuração

006

Descrição do Lançamento

TESTE 03

Resultado Lançamento na Apuração do ICMS\-ST:

__Tabela__

__Operação da Apuração__

__Valor do Lançamento__

__Descrição do Lançamento__

 

 

 

ITEM\_APURAC\_SUBST

002

11,88

TESTE 01

4 \+ 7,88

 

 

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Código Ajuste__

__Valor do ICMS__

 

X113

__9001__

1001

MG41000016

4

 

X113

__9002__

1001

MG41000016

7,88

 

 

ITEM\_APURAC\_SUBST

007

0,60

TESTE 02

0,45\+ 0,15

 

 

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Código Ajuste__

__Valor do ICMS__

 

X113

__9001__

1001

MG21000018

0,45

 

X113

__9002__

1001

MG21000018

0,15

 

 

ITEM\_APURAC\_SUBST

006

126,004

TESTE 03

74,004 \+ 52

 

 

__TABELA__

__NUM\_DOCFIS  
\(Devolução\)__

__Código da Observação__

__Código Ajuste__

__Valor do ICMS__

 

X113

__9001__

1002

MG11000016

74,004

 

 

X113

__9002__

1002

MG11000016

52

__Gravação das Tabelas:__

__ \- Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\): __

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Gravar o código ‘108’

__\*\*\*__

__Identificador do Estado__

IDENT\_ESTADO

Identificador do Estado na tabela ESTADO para o código do estado = “MG”\.

__\*\*\*__

__Indicador da UF__

IND\_UF

Preencher com ‘1’, que significa mesma UF do estabelecimento\.

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o Código da Operação da Apuração cadastrado na tela de Parâmetros p/ Geração dos Ajustes e Lançamentos \(menu Parâmetros à Ressarcimento ICMS\-ST\) para a empresa e estabelecimento foco da geração\.

Considerar o campo “Item da Apuração” referente ao lançamento a ser gravado:

1\) Lançamento de Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM:

2\) Lançamento de Estorno do FEM adicionada ao ICMS\-ST

3\) Lançamento de Estorno do Complemento de ICMS\-ST

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

Preencher com o total do campo 18 \- Valor do ICMS

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Parâmetros p/ Geração dos Ajustes e Lançamentos \(menu Parâmetros à Ressarcimento ICMS\-ST\) para a empresa e estabelecimento foco da geração\.

Considerar o campo “Descrição do Lançamento” referente ao lançamento a ser gravado:

1\) Lançamento de Estorno de Restituição/Ressarcimento de ICMS\-ST \+FEM:

2\) Lançamento de Estorno do FEM adicionada ao ICMS\-ST

3\) Lançamento de Estorno do Complemento de ICMS\-ST

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“1”\.__

Este valor significa que o lançamento possui vínculo com os Ajustes do Lançamento Fiscal \(SAFX113\)\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “M”\.

Demais campos não mencionados não precisam ser preenchidos

__  \- Vínculos com Ajustes do Lançamento Fiscal \(ITEM\_APURAC\_SUBST\_X113\)__

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

Código da empresa

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

Código do estabelecimento

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

Data da Escrita Fiscal

DATA\_FISCAL

Data Fiscal do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Movimento Entrada/Saída

MOVTO\_E\_S

Movimento Entrada/Saída do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Normal ou Devolução

NORM\_DEV

Indicador de Normal ou Devolução do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Tipo do Documento

COD\_DOCTO

Código do Tipo de Documento do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

Indicador da Pessoa Fis/Jur do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Código/Destinatário/Emitente/ Remetente

COD\_FIS\_JUR

Código da Pessoa Fis/Jur do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Número do Documento Fiscal/ Número do Mapa Resumo de Caixa

NUM\_DOCFIS

Número do Documento Fiscal do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Série do Documento Fiscal

SERIE\_DOCFIS

Série do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Código da Observação

COD\_OBS\_LANCTO\_FISCAL

Código de Observação do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Tipo de Observação

IND\_ICOMPL\_LANCTO

Informar:  
L \- Observação referente aos Lançamentos Fiscais da Nota 

__\*\*\*__

Código do Ajuste

COD\_AJUSTE\_SPED

Código do Ajustes do Lançamento Fiscal recuperados da X113\_AJUSTE\_APUR

__\*\*\*__

Número do Item da Nota

DISCRI\_ITEM

Não preencher\.

__Código do Livro __

COD\_TIPO\_LIVRO

Gravar o código ‘108’, gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Data da Apuração__

DAT\_APURACAO

Último dia do mês e ano do Período da informado na tela de geração, gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Identificador do Estado__

IDENT\_ESTADO

Identificador do Estado na tabela ESTADO para o código do estado = “MG”\. Mesmo que foi gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Indicador da UF__

IND\_UF

Preencher com ‘1’, que significa mesma UF do estabelecimento\. Mesmo que foi gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Operação da Apuração__

COD\_OPER\_APUR

Código da Operação da Apuração gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial gravado no Lançamento Complementar na ITEM\_APURAC\_SUBST\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “M”\.

Demais campos não mencionados não precisam ser preenchidos

## <a id="_Toc78383913"></a>5\.4 – Etapa 4: Atualização do Status da Obrigação da Apuração 

 __Gravação da Tabela de Status da Obrigação \(APURACAO\)__

Verificar se existe registro de Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manutenção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”\.

Caso não exista registro, criar um registro com as seguintes informações:

 Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

Situação

IND\_SITUACAO\_APUR

Preencher com ‘1’ – Não Apurado

Validade

IND\_VALID\_APUR

Preencher com ‘1’ – Não Analisado

Data da Realização

DAT\_REALIZACAO

Data da execução da geração\.

## <a id="_Toc78383914"></a>5\.5 – Etapa 5: Geração de Relatório de Conferência Observações \(SAFX112\) e Ajustes do Lançamento Fiscal \(SAFX113\)

\[MFS511653\]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré\-geração:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, disponibilizar os arquivos em formato Excel dos relatórios de conferência dos registros C195 e C197 gerados na etapa 2\.

__C195__:

Nome do arquivo: Relatório\_Conferencia\_C195\_mm\_aaaa\_cod\_estab\.csv

Fazer uma leitura na tabela X112\_OBS\_DOCFIS com as observações das notas de devolução de saída, que foram geradas na etapa 2\. 

Todos os campos especificados para gravação da SAFX112, devem ser demonstrados no relatório\.

__C197__:

Nome do arquivo: Relatório\_Conferencia\_C197\_mm\_aaaa\_cod\_estab\.csv

Fazer uma leitura na tabela X113\_AJUSTE\_APUR com os ajustes dos lançamentos fiscais das notas de devolução de saída, que foram gerados na etapa 2\. 

Todos os campos especificados para gravação da SAFX113, devem ser demonstrados no relatório\.

## <a id="_Toc78383915"></a>5\.6 – Etapa 6: Geração de Relatório de Conferência dos Lançamentos Complementares na Apuração do ICMS\-ST

\[MFS511653\]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré\-geração:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, disponibilizar um arquivo formato Excel demonstrando os lançamentos complementares gerados na etapa 3\.

Nome do arquivo: Relatório\_Conferencia\_Lancto\_P9\_ST\_mm\_aaaa\_cod\_estab\.csv

Fazer uma leitura na tabela ITEM\_APURAC\_SUBST com os lançamentos complementares gerados na etapa 3\. 

Os campos que devem ser apresentados no relatório são: 

__Campo__

__Nome na tabela__

__Código da empresa__

COD\_EMPRESA

__Código do estabelecimento__

COD\_ESTAB

__Data da Apuração__

DAT\_APURACAO

__Código do Livro __

COD\_TIPO\_LIVRO

__Operação da Apuração__

COD\_OPER\_APUR

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

	

= = = = = =

 

