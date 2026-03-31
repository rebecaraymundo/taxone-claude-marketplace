---
source: "MTZ_PowerLock_Acessos_Simultaneos.docx"
category: Seguranca
converted: auto
---

# Power Lock – Acessos Simultâneos

**Localização:**
Powerlock



DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO





**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**





---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS4381 | DW - BASICOS - Powerlock - USUÁRIOS SIMULTANEOS | Definição da regra do parâmetro Acessos Simultâneos. |
|  |  |  |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN01 | Regra de Negócio para o parâmetro “Bloquear acessos simultâneos” do Controle de Segurança >> Parâmetros Quando o parâmetro “Bloquear acessos simultâneos” estiver selecionado na tela de Parâmetros do submenu Controle de Segurança do PowerLock (Menu File >> Controle de Segurança >> Parâmetros), o sistema não deve permitir que um mesmo usuário realize logon em mais de uma instância do manager do Mastersaf DW, seja em um mesmo computador ou em máquinas distintas.  Devem ser realizados os seguintes tratamentos quando o parâmetro estiver selecionado: Se o usuário acessou o manager e a partir do manager, acessar outros módulos, sem acessar outra instância do manager: Não há impactos. Se o usuário acessou o manager e a partir do manager, acessar outros módulos e tentar acessar outra instância do manager, bloquear o acesso e retornar a mensagem: “Não é permitido acessos simultâneos para um mesmo usuário”. Se o usuário acessou o manager e a partir do manager, acessar outros módulos e tentar fechar a instância aberta do manager, mas manter aberta a conexão dos outros módulos, não permitir que o manager seja fechado e retornar a mensagem: “O Manager não pode ser encerrado enquanto outros módulos estiverem em execução”. Se o usuário acessou o manager e a partir do manager, acessar outros módulos e encerrou o acesso aos outros módulos e ao manager e tentou acessar outra instância do manager: Não há impactos  Estamos considerando como fechar e encerrar o acesso o ato do usuário de fechar a tela pelo ícone de fechar ou clicar em sair nos módulos (menu Arquivo >> Sair) ou Alt + F4. | OS4381 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

