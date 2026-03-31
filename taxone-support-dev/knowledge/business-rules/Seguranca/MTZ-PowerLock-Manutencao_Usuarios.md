---
source: "MTZ-PowerLock-Manutencao_Usuarios.docx"
category: Seguranca
converted: auto
---


# Segurança - PowerLock

# Manutenção de Usuários

**Localização:**
Módulo: Básicos  Segurança
Menu: Users



DOCUMENTO DE REQUISITO




## REGRAS DE NEGÓCIO




**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS39518 | Andréa Rocha | O objetivo é criar um controle de concessão e revogação de acessos dos usuários na tela de manutenção. |


---

| Cód. | Descrição | MFS |
| --- | --- | --- |
| RN01 | Regra geral   A tela de manutenção dos usuários será alterada para passar a armazenar as informações de log de concessão e revogação de acessos dos usuários.  As informações de criação e alteração dos usuários serão gravadas na nova tabela que será criada para este controle (PL_USR_AUDIT).  E depois estas informações serão demonstradas no relatório criado para este fim, o Relatório de Concessão/Revogação de Usuários.  Não será criado nenhum campo novo na tela de manutenção dos usuários para fazer este controle.  Esta tabela será gravada quando for criado ou alterado um usuário, e somente serão gravadas as informações referentes ao acesso do usuário, tais como status e data de expiração.  Ou seja, somente será gravada a tabela quando o usuário for criado ou se alterarem o seu status ou a sua data de expiração.  Informações que devem ser armazendas na tabela PL_USR_AUDIT: - Administrador; - Usuário; - Data e hora do registro; - Status do usuário (Ativo/Inativo); - Data de expiração; - Tipo de modificação (Inclusão/Alteração). | MFS39518 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

