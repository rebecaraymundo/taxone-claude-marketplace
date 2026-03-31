---
source: "MTZ-PowerLock-Relatorio_de_Controle_de_Acesso_Usuarios.docx"
category: Seguranca
converted: auto
---


# Segurança - PowerLock

# Relatório de Concessão/Revogação de Usuários

**Localização:**
Módulo: Básicos  Segurança
Menu: Reports  Users Control Report



DOCUMENTO DE REQUISITO




## REGRAS DE NEGÓCIO




**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS39518 | Andréa Rocha | O objetivo é criar um relatório para demonstrar o log de concessão e revogação de acessos dos usuários. |


---

| Cód. | Descrição | MFS |
| --- | --- | --- |
| RN00 | Parâmetros de tela:  - Período: informar a data inicial e a data final, campos do tipo data no formato DD/MM/AAAA.  - Administrador: campo do tipo listbox, que irá mostrar todos os administradores cadastrados e mais a opção “TODOS”. | MFS39518 |
| RN01 | Regra geral do relatório  O relatório irá recuperar as informações dos usuários da nova tabela criada para o controle de criação e alteração de usuários (PL_USR_AUDIT).  Esta tabela será gravada quando for criado ou alterado um usuário, e somente serão gravadas as informações referentes ao acesso do usuário, tais como status e data de expiração.   Os filtros para o relatório são:  - Data do registro dentro do período informado em tela; - Administrador de acordo com o informado em tela ou todos. | MFS39518 |
| RN02 | Regra p/ campo Emissão (Cabeçalho)  Preencher com o dia e hora em que o relatório foi gerado. Utilizar SYSDATE. Formato: DD/MM/AAAA HH:MM:SS. | MFS39518 |
| RN03 | Regra p/ campo Período (Cabeçalho)  Preencher com o período informado na tela de critério de seleção. Formato: DD/MM/AAAA.  O campo deve conter um textbox + “à” + textox. Mascara de data para o textbox: DD/MM/AAAA. | MFS39518 |
| RN04 | Regra p/ campo Administrador (Cabeçalho)  Preencher com o campo “ADM_KEY” da tabela PL_USR_AUDIT. | MFS39518 |
| RN05 | Regra p/ campo Login (Nome)  Preencher com o campo USR_KEY da tabela PL_USR_AUDIT. | MFS39518 |


---

| RN06 | Regra p/ campo Status  O Preencher com o campo USR_STATUS da tabela PL_USR_AUDIT.  Se o campo for igual a “0”       Mostrar “Inativo” Senão se o campo for igual a “1”       Mostrar “Ativo” Senão        Mostrar “Não preenchido”. | MFS39518 |
| --- | --- | --- |
| RN07 | Regra p/ campo Expira em  Preencher com o campo USR_EXPIRE_DATE da tabela PL_USR_AUDIT.   Se o campo não estiver preenchido      Mostrar “Não preenchido”. | MFS39518 |
| RN08 | Regra p/ campo Registrado em  Preencher com o campo DT_REG da tabela PL_USR_AUDIT. | MFS39518 |
| RN09 | Regra p/ campo Tipo do Registro  Preencher com o campo USR_MODIFY da tabela PL_USR_AUDIT.  Se o campo for igual a “I”       Mostrar “Criação” Senão se o campo for igual a “U”       Mostrar “Alteração”. | MFS39518 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

