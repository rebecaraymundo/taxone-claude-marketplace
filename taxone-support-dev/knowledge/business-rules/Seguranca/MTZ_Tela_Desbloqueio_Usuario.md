---
source: "MTZ_Tela_Desbloqueio_Usuario.docx"
category: Seguranca
converted: auto
---





THOMSON REUTERS





DOCUMENTO DE REQUISITO


Sumário

**1.	TELA A SER DESENVOLVIDA	3**
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

# TELA A SER DESENVOLVIDA

[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

## Diagrama de Casos de Uso



## UC001 – Manutenção da Estrutura Padrão

[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



### Fluxo Principal


### Fluxo Alternativo 1 – Novo Registro



# Regras dos Campos

**Localização da tela:**
Módulo: Básicos >> Segurança >> PowerLock ou Tela de acesso ao Manager >> Opções >> Configurar Segurança >> PowerLock
Menu: File >> Controle de Segurança

Título da tela: Desbloqueio de Usuários


* Descrição não disponível em tela

Sugestão de layout da tela:




---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4381 | Marcos G. de Paula | Definição das regras para a tela de Desbloqueio de Usuário. |
|  |  |  |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Usuário | Checkbox | S | S | Default: não selecionado |  | OS4381 |
| Usuário | Editbox | S | N |  | Deverá exibir a relação de usuários logados no Mastersaf DW, demonstrando a informação conforme cadastro de usuários do PowerLock, com a seguinte formatação:  <Login Name> - <First Name + Last Name>  Exemplo: Login Name: fulano First Name: Fulano Last Name: de Tal  Será exibido: “fulano – Fulano de Tal” | OS4381 |
| Selecionar Todos | Botão | N | S |  | Quando acionado este botão, os registros do campo usuário que estiverem com checkbox não selecionados passarão para o status de selecionados. | OS4381 |
| Desmarcar Todos | Botão | N | S |  | Quando acionado este botão, os registros do campo usuário que estiverem com checkbox selecionados passarão para o status de não selecionados. | OS4381 |
| Desbloquear Selecionados | Botão | N | S |  | Quando acionado este botão, as seguintes ações devem ser realizadas:  Se nenhum usuário estiver com checkbox selecionado, retornar a mensagem: “Não existem usuários selecionados para desbloqueio”. Se existirem usuários selecionados, estes deverão ser excluídos da tabela de registro de conexão e deverá ser possível uma nova conexão para aquele usuário | OS4381 |
