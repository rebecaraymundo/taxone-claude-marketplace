# MTZ_EFD_Parametros_Registro_C176_Ajustes_e_Lancamentos

> Fonte: MTZ_EFD_Parametros_Registro_C176_Ajustes_e_Lancamentos.docx






THOMSON REUTERS

Módulo Sped Fiscal

Manutenção dos Parâmetros p/a Geração de Ajustes e Lançamentos Complementares referentes aos Valores do C176


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro C176  Parâmetros p/Geração dos Ajustes e Lançamentos


DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3


























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de pré-geração do registro C176, realizada no menu “Pré-Geração  Registro C176” do módulo Sped Fiscal.

Estas informações servem para a geração dos ajustes (C195/C197) e lançamentos complementares da Apuração do ICMS, a partir dos valores apurados para o registro C176, de acordo com as orientações da Portaria CAT 158 / 2015.


## Layout da Tela


Alteração da MFS8892:
Foram incluídos novos parâmetros para o lançamento do estorno do lançamento do ressarcimento, conforme orientações da Portaria CAT 113/2016.


Alteração da MFS9749:
Foram incluídos novos parâmetros para os ajustes e lançamentos de estorno de ressarcimento/crédito referente às devoluções (entradas por devolução de mercadorias cuja saída tenha gerado ressarcimento/crédito de ICMS-ST).




Botões da barra de menu:



Na abertura da tela, a janela da opção “GRUPO” será aberta automaticamente, obrigando o usuário a selecionar o grupo desejado. Os critérios para exibição dos grupos serão os mesmos descritos acima. O Grupo selecionado será exibido nos campos “Cód. Observação (C195)”, referentes ao Ajuste de Ressarcimento e ao Ajuste de Crédito.


## Regras de Funcionamento dos Campos






Parâmetros para geração dos ajustes (C195/C197):


– Ajuste de Ressarcimento:







– Ajuste de Crédito:




– Ajuste de Estorno do Ressarcimento (Devoluções):


Alteração da MFS9749: Criação dos parâmetros para o ajuste de estorno do ressarcimento (devoluções).




– Ajuste de Estorno do Crédito (Devoluções):


Alteração da MFS9749: Criação dos parâmetros para o ajuste de estorno do crédito (devoluções).






Parâmetros para geração dos lançamentos da Apuração do ICMS:


– Lançamento de Ressarcimento:





– Lançamento de Crédito:






– Lançamento de Estorno do Ressarcimento (Devoluções):


Alteração da MFS9749: Criação dos parâmetros para o lançamento de estorno do ressarcimento, referente às devoluções.






– Lançamento de Estorno do Crédito (Devoluções):


Alteração da MFS9749: Criação dos parâmetros para o lançamento de estorno do crédito, referente às devoluções.





– Lançamento de Estorno do Ressarcimento (valor a ser transferido p/o registro 1200):


Alteração da MFS8892: Criação dos parâmetros para o lançamento de estorno do ressarcimento, referente ao valor que será transferido para o registro 1200, conforme orientações da Portaria CAT 113/2016.
Alteração da MFS9749: O título deste lançamento na tela foi alterado para não confundir com o outro lançamento de estorno do ressarcimento, que é referente às devoluções.


Obs: Este lançamento, diferente dos dois anteriores, tem um parâmetro a mais, que é o código de ajuste que será utilizado no registro E211. Os lançamentos anteriores não tem este parâmetro, pois são lançamentos referentes aos ajustes do C197, que já tem seu código de ajuste parametrizado nos quadros “Ajuste de Ressarcimento” e “Ajuste de Crédito”.






= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS2772 | Atendimento a Portaria CAT 158 | Criação da parametrização para geração dos ajustes (C195/C197) e lançamentos complementares na Apuração do ICMS, referentes aos valores apurados para o registro C176. | 17/05/2016 |
| CH19356_2016 | Lara Aline | Alteração na regra de seleção dos códigos de ajustes do C197. | 27/09/2016 |
| MFS8892 | Novos parâmetros | Portaria CAT 113/16: criação de parâmetros p/o lançamento de estorno de ressarcimento | 30/12/2016 |
| MFS9749 | Novos parâmetros | Portaria CAT 112/16: criação de parâmetros p/os ajustes e lançamentos de estorno de ressarcimento/crédito referente às devoluções. | 30/12/2016 |
| MFS47510 | Andréa Rocha | Alteração na regra de seleção dos códigos de ajustes do C197, para incluir o terceiro e o quarto caracter do código iguais a 9.  Alteração feita baseada na legislação do RS, que determina que estes códigos devem ir para o registro C197. | 08/01/2021 |
| MFS91835 | Andréa Rocha | Retirar a obrigatoriedade de preenchimento dos parâmetros para o lançamento de estorno de ressarcimento | 22/08/2022 |


| GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento (relacionamento Tabela x Grupos), e o usuário poderá selecionar o grupo desejado. Caso o usuário tenha informado um estabelecimento no login, serão disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, serão exibidos os grupos de todos os estabelecimentos da empresa.    O Grupo selecionado será exibido nos campos “Cód. Observação (C195)”, referentes ao Ajuste de Ressarcimento e ao Ajuste de Crédito. |
| --- | --- |
| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão da parametrização do estabelecimento em questão. |
| CONFIRMA | Opção para salvar as informações incluídas ou alteradas. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Nesse campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão demonstrados para replicação todos os estabelecimentos da mesma empresa e UF do estabelecimento parametrizado. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  (*) Módulo DW, menu  “Manutenção  Códigos Cadastro de Observações” (SAFX2009); |  |
| Cód. Ajuste (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)   [ALTERAÇÃO CH19356_2016]  A alteração do CH19356/16 foi desfeita pela MFS9749, voltando à regra original (vide e-mail anexado no Jira).  [MFS47510] Inclusão do terceiro e quarto caracter iguais a 9  Serão disponibilizados para seleção apenas os códigos com o terceiro caracter = “1” (=Outros Créditos) ou “9” (=Informativo) OU  E quarto caracter = “0” (=Apuração do ICMS próprio)  ou “9” (=Informativo), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Manutenção  Cadastros  Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; | CH19356_2016 MFS9749 MFS47510 |
| Descrição Complementar do Ajuste (C197) | Alfanumérico | N | S |  | Neste campo será informada a descrição complementar do ajuste (tamanho: 250 caracteres). |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  (*) Módulo DW, menu  “Manutenção  Códigos Cadastro de Observações” (SAFX2009); |  |
| Cód. Ajuste (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  [ALTERAÇÃO CH19356_2016]  A alteração do CH19356/16 foi desfeita pela MFS9749, voltando a regra original (vide e-mail anexado no Jira).  [MFS47510] Inclusão do terceiro e quarto caracter iguais a 9  Serão disponibilizados para seleção apenas os códigos com o terceiro caracter = “1” (=Outros Créditos) ou “9” (=Informativo)  OU  E quarto caracter = “0” (=Apuração do ICMS próprio) ou “9” (=Informativo), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Manutenção  Cadastros  Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; | CH19356_2016 MFS9749 MFS47510 |
| Descrição Complementar do Ajuste (C197) | Alfanumérico | N | S |  | Neste campo será informada a descrição complementar do ajuste (tamanho: 250 caracteres). |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  (*) Módulo DW, menu  “Manutenção  Códigos Cadastro de Observações” (SAFX2009); |  |
| Cód. Ajuste (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  [MFS47510] Inclusão do terceiro e quarto caracter iguais a 9  Serão disponibilizados para seleção apenas os códigos com o terceiro caracter = “5” (=Estorno de Crédito) ou “9” (=Informativo)  e quarto caracter = “0” (=Apuração do ICMS próprio) ou “9” (=Informativo), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Manutenção  Cadastros  Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; | MFS47510 |
| Descrição Complementar do Ajuste (C197) | Alfanumérico | N | S |  | Neste campo será informada a descrição complementar do ajuste (tamanho: 250 caracteres). |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  (*) Módulo DW, menu  “Manutenção  Códigos Cadastro de Observações” (SAFX2009); |  |
| Cód. Ajuste (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  [MFS47510] Inclusão do terceiro e quarto caracter iguais a 9  Serão disponibilizados para seleção apenas os códigos com o terceiro caracter = “5” (=Estorno de Crédito) ou “9” (=Informativo)  e quarto caracter = “0” (=Apuração do ICMS próprio) ou “9” (=Informativo), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Manutenção  Cadastros  Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; | MFS47510 |
| Descrição Complementar do Ajuste (C197) | Alfanumérico | N | S |  | Neste campo será informada a descrição complementar do ajuste (tamanho: 250 caracteres). |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S |  |  | Este campo trabalha com janela de seleção da Tabela dos Itens da Apuração do ICMS. Serão disponibilizados para seleção apenas os itens de créditos: “006” e “007”. |  |
| Descrição do Lançamento | Alfanumérico | S |  |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_DISCR). |  |
| Classe de Lançamento | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão.  (*) Módulo Ferramentas, menu “Tabelas Internas  Manter Classes por UF”; |  |
| Amparo/Texto/Ocorrência | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal (*) + Tabela dos Códigos de Subitens do Amparo Legal (**), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Cadastros  Código Amparo / Texto / Ocorrência”;  (**) Módulo DW, menu “Cadastros  Código Subitem Amparo / Texto / Ocorrência”;  Na janela de seleção, os amparos que possuem subitem na tabela dos subitens, são demonstrados no detalhe, com cada um dos subitens existentes. |  |
| Subitem Amp./Texto/Ocor. | Alfanumérico | N |  |  | Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S |  |  | Este campo trabalha com janela de seleção da Tabela dos Itens da Apuração do ICMS. Serão disponibilizados para seleção apenas os itens de créditos: “006” e “007”. |  |
| Descrição do Lançamento | Alfanumérico | S |  |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_DISCR). |  |
| Classe de Lançamento | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão.  (*) Módulo Ferramentas, menu “Tabelas Internas  Manter Classes por UF”; |  |
| Amparo/Texto/Ocorrência | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal (*), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Cadastros  Código Amparo / Texto / Ocorrência”; |  |
| Subitem Amp./Texto/Ocor. | Alfanumérico | N |  |  | Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem.  (*) Módulo DW, menu “Cadastros  Código Subitem Amparo / Texto / Ocorrência”; |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S |  |  | Este campo trabalha com janela de seleção da Tabela dos Itens da Apuração do ICMS. Serão disponibilizados para seleção apenas os itens de débito: “002” e “003”. |  |
| Descrição do Lançamento | Alfanumérico | S |  |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_DISCR). |  |
| Classe de Lançamento | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão.  (*) Módulo Ferramentas, menu “Tabelas Internas  Manter Classes por UF”; |  |
| Amparo/Texto/Ocorrência | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal (*) + Tabela dos Códigos de Subitens do Amparo Legal (**), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Cadastros  Código Amparo / Texto / Ocorrência”;  (**) Módulo DW, menu “Cadastros  Código Subitem Amparo / Texto / Ocorrência”;  Na janela de seleção, os amparos que possuem subitem na tabela dos subitens, são demonstrados no detalhe, com cada um dos subitens existentes. |  |
| Subitem Amp./Texto/Ocor. | Alfanumérico | N |  |  | Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S |  |  | Este campo trabalha com janela de seleção da Tabela dos Itens da Apuração do ICMS. Serão disponibilizados para seleção apenas os itens de débitos: “002” e “003”. |  |
| Descrição do Lançamento | Alfanumérico | S |  |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_DISCR). |  |
| Classe de Lançamento | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão.  (*) Módulo Ferramentas, menu “Tabelas Internas  Manter Classes por UF”; |  |
| Amparo/Texto/Ocorrência | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal (*), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Cadastros  Código Amparo / Texto / Ocorrência”; |  |
| Subitem Amp./Texto/Ocor. | Alfanumérico | N |  |  | Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem.  (*) Módulo DW, menu “Cadastros  Código Subitem Amparo / Texto / Ocorrência”; |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S     N |  |  | Este campo trabalha com janela de seleção da Tabela dos Itens da Apuração do ICMS. Serão disponibilizados para seleção apenas os itens de créditos: “002” e “003” (Outros Débitos e Estorno de Créditos). | MFS8892 MFS91835 |
| Descrição do Lançamento | Alfanumérico | S N |  |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_DISCR). | MFS8892 MFS91835 |
| Classe de Lançamento | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão.  (*) Módulo Ferramentas, menu “Tabelas Internas  Manter Classes por UF”; | MFS8892 |
| Amparo/Texto/Ocorrência | Alfanumérico | N |  |  | Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal (*) + Tabela dos Códigos de Subitens do Amparo Legal (**), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo DW, menu “Cadastros  Código Amparo / Texto / Ocorrência”;  (**) Módulo DW, menu “Cadastros  Código Subitem Amparo / Texto / Ocorrência”;  Na janela de seleção, os amparos que possuem subitem na tabela dos subitens, são demonstrados no detalhe, com cada um dos subitens existentes. | MFS8892 |
| Subitem Amp./Texto/Ocor. | Alfanumérico | N |  |  | Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem. | MFS8892 |
| Cód. Ajuste (E111/E220) | Alfanumérico | S    N | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste de Sped Fiscal (*)  Serão disponibilizados para seleção apenas os códigos com o terceiro caracter = “0” (=Apuração Própria) e quarto caracter = “1” (=Estorno de Crédito), considerando apenas os códigos da UF do estabelecimento em questão.  (*) Módulo ICMS, menu “Apuração > Apuração do ICMS > Lançamentos Complementares  Código de Ajuste Sped Fiscal”;  (observar que não se trata da mesma tabela de ajustes utilizada nos quadros “Ajuste de Ressarcimento” e “Ajuste de Crédito”) | MFS8892 MFS91835 |
