---
source: "MTZ-Ferramentas_Relatório_Historico_Alterações_de_Operações.docx"
category: Ferramentas
converted: auto
---



THOMSON REUTERS

**Módulo Básicos - Ferramentas**

**HISTÓRICO DE ALTERAÇÕES DE OPERAÇÕES**


Localização: Menu Relatório  Histórico de Alterações de Operações



DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



O menu de geração do “Histórico de Alteração de Operações” deverá ser disponibilizado no caminho: Menu Relatório, abaixo do item “Historico da Mantenção das NFs”.





**Localização da tela:**

Módulo: Ferramentas  Menu Relatório  Histórico de Alteração de Operações

Título da tela: Histórico de Alteração de Operações

Funcionamento da tela: Esta tela foi criada com a finalidade de possibilitar o acompanhamento/consultas de todos os processos, de alteração, exclusão e inclusões de valores realizados nas tabelas de Créditos Disponíveis e dos Créditos a Utilizar, do módulo de EFD Contribuições, com o intuito de identificar possíveis falhas do sistema ou alterações indevidas via banco de dados, posteriormente a estrutura de tabela de auditoria poderá ser utilizada para outros propósitos de monitoramento.







A necessidade de criação desse relatório se deve aos diversos problemas reportados pelos clientes em relação a “perda” dos créditos disponíveis de períodos anteriores, atualmente essa funcionalidade está preparada, somente, para auditar o módulo de EFD Contribuições, porém futuramente a estrutura da tabela de auditoria poderá ser utilizada para outros propósitos de monitoramento.

O Relatório de Histórico deverá ser disponibilizado no formato XLS para gravação na Aba “Arquivos”.

Nome do Arquivo: REL_HISTORICO_ALT_OPER.xls

O Relatório terá como base as informações da tabela AUD_OPER_TABLE e deverá ser disponibilizado conforme layout abaixo:




Sendo:



---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS64713 | Rogério Ohashi | Este documento tem como objetivo criar a Tela e Relatório de Auditoria de Tabelas | 23/08/2021 |


---

| RN00 | Regras Gerais |
| --- | --- |



---

| RN01 | Parâmetros de Tela |
| --- | --- |



---

| Campo | Regra | Demanda |
| --- | --- | --- |
| Data Inicial | Neste campo será informado a data inicial, a ser utilizada como filtro para seleção das informações de auditoria a partir do Campo DATAHORA da tabela AUD_OPER_TABLE. | MFS-64713 |
| Data Final | Neste campo será informado a data final, a ser utilizada como filtro para seleção das informações de auditoria a partir do Campo DATAHORA da tabela AUD_OPER_TABLE. | MFS-64713 |
| Lista Tabela | Funcionamento da lista de Tabelas:  Parâmetro do tipo “Listbox” disponibilizando para seleção a lista das Tabelas (Distinct do Campo “TABELA” da tabela AUD_OPER_TABLE) + opção “Todas”.  Default = “Todas” | MFS-64713 |


---

| RN02 | Relatório - Preenchimento dos Dados |
| --- | --- |



---

| Período | Sessão | Tabela Alterada | Operação | Antes | Depois | Rastro | Informações Gerais |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |


---

| Período | Conteúdo do Campo DATAHORA |
| --- | --- |
| Sessão | Conteúdo do Campo SESSAO |
| Tabela Alterada | Conteúdo do Campo TABELA |
| Operação | Conteúdo do Campo OPERACAO |
| Antes | Conteúdo do Campo ANTES |
| Depois | Conteúdo do Campo DEPOIS |
| Rastro | Conteúdo do Campo RASTRO |
| Informações Gerais | Conteúdo do Campo ID |
