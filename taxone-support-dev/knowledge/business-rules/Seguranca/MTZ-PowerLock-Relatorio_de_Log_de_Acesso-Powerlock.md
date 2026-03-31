---
source: "MTZ-PowerLock-Relatorio_de_Log_de_Acesso-Powerlock.docx"
category: Seguranca
converted: auto
---

# Segurança – Relatório de Log de Acesso - PowerLock




DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO



**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS3893 | DW - BASICOS - SEGURANÇA - Tratamento para controle de acessos e armazenamento dos logs | O objetivo da OS é criar o relatório de log de acesso para o usuário PowerLock. |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Regra p/ tela de critério de seleção A tela deve conter os campos Período e Acesso. E os botões Ok e Cancel.  Quando o botão Ok for acionado, o sistema deve gerar o relatório de acordo com os critérios escolhidos anteriormente. Quando o botão Cancel for acionado, o sistema deve fechar a tela de critério de seleção. | OS3893 |
| RN01 | Regra geral do relatório Recuperar as informações gravadas na tabela PL_AUD com as seguintes características: - Data Início e Data Fim dentro do período informado na tela de critério de seleção - Acesso de acordo com o escolhido na tela de critério de seleção.   - Quando selecionada a opção CONFIRMADO, deverão ser recuperadas as informações que contiverem o status “S” no campo ACESSO_OK da tabela PL_AUD.   - Quando selecionada a opção NEGADO, deverão ser recuperadas as informações que contiverem o status “N” no campo ACESSO_OK da tabela PL_AUD.   - Quando selecionada a opção TODOS, ambas as condições (tanto “S” quanto “N”) deverão ser consideradas na geração do relatório. | OS3893 |
| RN02 | Regra p/ campo Emissão (Cabeçalho) Preencher com o dia e hora em que o relatório foi gerado. Utilizar SYSDATE. Formato: DD/MM/AAAA HH:MM:SS. | OS3893 |
| RN03 | Regra p/ campo Período (Cabeçalho) Preencher com o período informado na tela de critério de seleção. Formato: DD/MM/AAAA.  O campo deve conter um textbox + “a” + textox. Mascara de data para o textbox: DD/MM/AAAA. | OS3893 |
| RN04 | Regra p/ campo Acesso (Cabeçalho) Preencher com o Acesso informado na tela de critério de seleção, podendo ser: Confirmado, Negado ou Todos.  Por default, deve-se manter a opção Todos marcada. | OS3893 |
| RN05 | Regra p/ campo Módulo (Cabeçalho) Preencher com “PowerLock”. | OS3893 |
| RN06 | Regra p/ campo Usuário (Cabeçalho) Preencher com o campo “ADM_NAME” da tabela PL_ADMIN, de acordo com o usuário que realizou o login no módulo Power Lock | OS3893 |
| RN07 | Regra p/ campo Data Inicio Preencher com o campo AUD_START_TIME da tabela PL_AUD. | OS3893 |
| RN08 | Regra p/ campo Data Fim O Preencher com o campo AUD_END_TIME da tabela PL_AUD. | OS3893 |
| RN09 | Regra p/ campo Acesso Preencher com o campo ACESSO_OK da tabela PL_AUD.  Se o campo estiver preenchido com “S”, o relatório deve exibir “SIM”. Se o campo estiver preenchido com “N”, o relatório deve exibir “NÃO”. | OS3893 |
| RN10 | Regra p/ campo Login do Windows Preencher com o campo USUARIO_WINDOWS da tabela PL_AUD. | OS3893 |
| RN11 | Regra p/ campo Máquina Preencher com o campo NOME_MAQUINA da tabela PL_AUD. | OS3893 |
| RN12 | As informações demonstrada no relatório “Access Log Report – PowerLock” devem demonstrar as informações de acesso do usuário admin ao módulo do Powerlock. A informação apresentada deve refletir as tentativas e acesso ao Powerlock independente do acesso ao DW.  Estas informações devem ser armazenadas por, no mínimo, três meses. | OS4079 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

