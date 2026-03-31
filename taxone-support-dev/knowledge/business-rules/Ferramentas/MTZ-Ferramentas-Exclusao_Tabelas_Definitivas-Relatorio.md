---
source: "MTZ-Ferramentas-Exclusao_Tabelas_Definitivas-Relatório.docx"
category: Ferramentas
converted: auto
---



THOMSON REUTERS

**Módulo Básicos - Ferramentas**

**Relatório dos Processos de Exclusão Tabelas Definitivas**


Localização: Menu Rotinas Acessórias  Inicialização  Exclusão de Tabelas Definitivas  Relatório dos Processos de Exclusão Tabelas Definitivas



DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



O objetivo do relatório é disponibilizar um relatório em Excel, com informação das Exclusão de Tabelas Definitivas realizadas nas opções: Documentos Fiscais, Cadastros, Movimentos e Cadastros Parâmetros. Através desse relatório é possível identificar o processo, a data da execução do processo de exclusão e o usuário responsável pela exclusão nas tabelas definitivas.










O relatório disponibiliza informações que permitem auditar os processos de exclusão nas tabelas definitivas.

O Relatório de Histórico deverá ser disponibilizado no formato XLS para gravação na Aba “Arquivos”.

Nome do Arquivo: REL_EXCLUSÃO_TABELA.xls

O Relatório irá recuperar os processos das tabelas FTR_PROCESSO e LIB_PROC_PARAM que atendam aos seguintes critérios:
- Data Inicial da Execução do Processo compreendida no Período de Execução informado na tela;
- DATA_INICIO da FTR_PROCESSO
- Data Final da Execução do Processo compreendida no Período de Execução informado na tela;
- DATA_FIM da FTR_PROCESSO
- Se Usuário for informado em tela, considerar apenas os processos do Usuário informado;
- COD_USUARIO da FTR_PROCESSO
- Se Número do Processo for informado em tela, considerar apenas o processo do Número informado;
- PROC_ID da FTR_PROCESSO
- Se Período da Parametrização for informado em tela, então considerar os processos que atendam aos critérios abaixo:
- Data Inicial da Parametrização do Processo compreendida no Período da Parametrização informado na tela;
- Data Final da Parametrização do Processo compreendida no Período da Parametrização informado na tela;
- (*) As Datas Inicial e Final da Parametrização do Processo são aquelas presentes nas telas de Exclusão de Tabelas Definitivas.
- (**) Data Inicial da Parametrização do Processo é gravada na tabela LIB_PROC_PARAM no registro com campo NOME = "Data Inicial".
- (***) Data Final da Parametrização do Processo é gravada na tabela LIB_PROC_PARAM no registro com campo NOME = "Data Final".
- Atenção ao caso em que a data final não está preenchida.
- Se o Nome da Tabela for informado em tela, então considerar os processos cujo Nome da Tabela Parametrizada seja igual ao informado;
- (*) O Nome da Tabela Parametrizada do processo de exclusão está gravado na tabela LIB_PROC_PARAM no registro com campo NOME = "Nome Tabela".
- Se o Estabelecimento for informado em tela, então considerar os processos cujo Estabelecimento Parametrizado seja igual ao informado;
- (*) O Estabelecimento Parametrizado do processo de exclusão está gravado na tabela LIB_PROC_PARAM no registro com campo NOME = "Estabelecimento".


O resultado deverá ser disponibilizado conforme layout abaixo:



---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS573091 | Liliane Assaf | Este documento tem como objetivo criar o Relatório dos Processos de Exclusão Tabelas Definitivas | 03/10/2023 |


---

| RN00 | Regras Gerais |
| --- | --- |



---

| RN01 | Parâmetros de Tela |
| --- | --- |



---

| Campo | Regra | Demanda |
| --- | --- | --- |
| Período de Execução | Neste campo serão informadas as datas inicial e final, para recuperação dos processos executados nesse período. Data Inicial é obrigatória. Data final não obrigatória. Caso a data final seja preenchida, a Data inicial deve ser menor ou igual à final. Caso a Data Inicial não seja preenchida, a Data Final menor que a Data Inicial, exibir mensagens e não prosseguir com a execução. | MFS573091 |
| Período da Parametrização | Nesse campo serão informadas as datas inicial e final para recuperação dos processos parametrizados dentro desse período (Datas Inicial e Final parametrizados nas telas de Exclusão de Tabelas Definitivas, opções Documentos Fiscais, Cadastros e Movimentos). Campo de preenchimento não obrigatório. As seguintes configurações são permitidas: - Data Inicial e Data final não preenchidas. - Data Inicial e Data final preenchidas. Nesse caso a Data inicial deve ser menor ou igual à final. - Data Inicial preenchida e Data final não preenchida. Não é permitido preencher apenas a data final.  Nas duas situações abaixo, exibir mensagens e não prosseguir com a execução: - Data Final preenchida e a Inicial não preenchida. - Ambas preenchidas e a Data Final menor que a Data Inicial. | MFS573091 |
| Usuário | Campo texto para livre digitação. Se for possível ao invés do campo texto, exibir uma lista fixa com os usuários da aplicação Tabela : pl_usr??? Campo de preenchimento não obrigatório. | MFS573091 |
| Número do Processo | Caso deseje emitir o relatório de um determinado processo, informar aqui o número do processo. Campo de preenchimento não obrigatório. | MFS573091 |
| Tipo da Tabela | Lista fixa demonstrando as seguintes opções: - Cadastros - Cadastros Parâmetros - Documentos Fiscais - Movimentos Campo de preenchimento não obrigatório. | MFS573091 |
| Nome Tabela | Apresentar a lista das tabelas relacionadas ao tipo selecionado no campo “Tipo da Tabela”. Campo só deve ser habilitado caso o usuário selecione um tipo no campo “Tipo da Tabela”.  Mesmas as listas presentes nas telas de Exclusão de Tabelas Definitivas, opções Documentos Fiscais, Cadastros, Movimentos e Cadastros Parâmetros. Campo de preenchimento não obrigatório. Mas caso o “Tipo da Tabela” seja selecionado, o campo Nome Tabela deve ser preenchido. | MFS573091 |
| Período do Dado Excluído | Campo a ser implementado futuramente: Neste campo serão informadas as datas inicial e final, formando o período em que os dados excluídos pertenciam. Data inicial deve ser menor ou igual à final. Campo só deve ser habilitado caso o usuário selecione o Tipo da Tabela =. Cadastros ou Documentos Fiscais ou Movimentos. Campo de preenchimento não Obrigatório. |  |
| Estabelecimento | Lista de estabelecimentos. Selecionar o estabelecimento ao qual os dados excluídos pertenciam. Campo só deve ser habilitado caso o usuário selecione o Tipo da Tabela =. Cadastros Parâmetros ou Documentos Fiscais ou Movimentos. Campo de preenchimento não Obrigatório. | MFS573091 |
| Mostrar Tabelas Vinculadas Excluídas | Campo a ser implementado futuramente: |  |


---

| RN02 | Relatório - Preenchimento dos Dados |
| --- | --- |



---

| Campos do Relatório | Regra de recuperação Campo                             Tabela | Regra de recuperação Campo                             Tabela |
| --- | --- | --- |
| Número do Processo | PROC_ID | FTR_PROCESSO |
| Data Inicial da Execução do Processo | DATA_INICIO | FTR_PROCESSO |
| Data Final da Execução do Processo | DATA_FIM | FTR_PROCESSO |
| Data Inicial da Parametrização | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "Data Inicial" |
| Data Final da Parametrização | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "Data Final" |
| Usuário | COD_USUÁRIO | FTR_PROCESSO |
| Nome Tabela Excluída | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "Nome Tabela" |
| Estabelecimento | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "Estabelecimento" |
| Grupo de Cadastro | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "Grupo" |
| LIMPAR também os dados de TABELAS VINCULADAS à tabela selecionada? | VALOR_APRESENTA | LIB_PROC_PARAM, recuperar o registro com campo NOME = "LIMPAR também os dados de TABELAS VINCULADAS à tabela selecionada?" |
