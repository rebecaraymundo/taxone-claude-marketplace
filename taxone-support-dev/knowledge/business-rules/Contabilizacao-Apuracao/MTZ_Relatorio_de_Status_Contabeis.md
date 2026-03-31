---
source: "MTZ_Relatório de Status Contábeis.docx"
category: Contabilização -Apuração
converted: auto
---





THOMSON REUTERS

Matriz da tela Contabilização

**Relatório de Status Contábeis**




DOCUMENTO DE REQUISITO


Sumário

**1.	INTRODUÇÃO	3**
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados – Relatório de Status	3
2.3	Prótotipo Relatório Status Contábeis	5
2.4	Lista de campos:	5
2.5	Exemplos de Relatórios:	8


# INTRODUÇÃO

O objetivo é criar um relatório que reflita os parâmetros configurados na tela de "Parâmetros de Apuração de Ajustes e Outros Lançamentos da Apuração", permitindo que o usuário visualize os parâmetros existentes relacionados às contas contábeis nestes relatórios.

# Documento de Referência


# Fluxo Principal Seleção de dados – Relatório de Status












**Localização da Tela:**
- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >>Relatórios de Parametrização
- Menu: Acesso Principal >> Seleção de Dados
















# Prótotipo Relatório Status Contábeis












# Lista de campos:











# Exemplos de Relatórios:















---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO - | Millys Lopes | Relatório de Status Contábeis |
|  |  |  |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições |  |
| Pós-Condições |  |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |


---

| Cód. | Campo | Tipo | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- |
| RN00 | EMPRESA | Alfanúmerico | Código Descrição | Exibe o código e a descrição da empresa que foi recuperada. | ADO |
| RN01 | ESTABELECIMENTO | Alfanúmerico | Código Descrição | Exibe o código e a descrição das filiais para seleção de acordo com a empresa selecionada |  |
| RN02 | UF | Texto | UF | Exibe as UFs dos estabelecimentos ou todas as UFs, conforme a seleção realizada, e recupera os dados correspondentes |  |
| RN03 | DATA INICIAL | Data | DD/MM/AAAA | Seleção de Período: O usuário deve inserir um período de seleção para visualizar os parâmetros relacionados. Isso inclui a entrada das datas inicial Busca de Informações: Após a entrada do período, o sistema deve efetuar uma busca nas informações gravadas nas telas de acordo com os campos Data de Inclusão/Exclusão e Alteração: Parâmetros de Ajustes da Apuração: Buscar dados relativos aos parâmetros do Ajustes da apuração para o período selecionado. Outros Lançamentos da Apuração: Buscar dados relativos aos parâmetros outros lançamentos relevantes para a apuração no período especificado. |  |
| RN04 | DATA FINAL | Data | DD/MM/AAAA | Seleção de Período: O usuário deve inserir um período de seleção para visualizar os parâmetros relacionados. Isso inclui a entrada das datas final Busca de Informações: Após a entrada do período, o sistema deve efetuar uma busca nas informações gravadas nas telas de acordo com os campos Data de Inclusão/Exclusão e Alteração: Parâmetros de Ajustes da Apuração: Buscar dados relativos aos parâmetros do Ajustes da apuração para o período selecionado. Outros Lançamentos da Apuração: Buscar dados relativos aos parâmetros outros lançamentos relevantes para a apuração no período especificado. |  |
| RN05 | GRUPO_IMPOSTO | Dropdown | Texto | Seleciona  todos ou  Federal ou Estadual. |  |
| RN06 | TIPO PARAMETRO | Dropdown | Alfanúmerico | Sistema deve apresentar ao usuário as seguintes opções de seleção: 01 - Todos os Parâmetros: Exibe todas as informações disponíveis, incluindo ajustes da apuração e outros lançamentos contábeis. 02 - Ajustes da Apuração: Exibe apenas os dados relacionados aos ajustes realizados na apuração do período selecionado. 03 - Outros Lançamentos Contábeis: Exibe somente os outros lançamentos contábeis do período selecionado. |  |
| RN07 | IMPOSTO | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN08 | REFERENCIA | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN09 | LOCAL_NEGÓCIO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN10 | DIVISAO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN11 | CENTRO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN12 | TIPO_PARAMETRO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro |  |
| RN13 | Código de Ajustes | Alfanúmerico |  | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro = Ajuste do da Apuração |  |
| RN14 | OUTRO LANCAMENTOS CONTABEIS | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro =Outros Lançamentos |  |
| RN15 | CODIGO DA NATUREZA OP OU F100 | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro= Outros Lançamentos |  |
| RN16 | INDICADOR DA CONTA_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN17 | CONTA CONTABIL_ D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN18 | DESCRICAO DA CONTA_D | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN19 | CHAVE DE LANÇAMENTOS_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN20 | CENTRO DE CUSTOS_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN21 | CENTRO DE LUCRO_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN22 | TEXTO HISTÓRICO_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN23 | OBSERVAÇÕES LANÇAMENTOS_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN24 | INDICADOR DE CONTA_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN25 | CONTA CONTABIL_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN26 | DESCRICAO DA CONTA_C | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN27 | CHAVE DE LANÇAMENTOS_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN28 | CENTRO DE CUSTOS_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN29 | CENTRO DE LUCRO_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN30 | TEXTO HISTÓRICO_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN31 | OBSERVAÇÕES LANÇAMENTOS_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN32 | USUARIO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN33 | DATA INCLUSAO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN34 | DATA ALTERAÇÃO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
| RN35 | DATA DE EXCLUSÃO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. |  |
