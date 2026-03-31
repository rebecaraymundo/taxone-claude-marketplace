---
source: "MTZ_Report_Fiscal_Saldo_Consolidado_ICMS_SAFX304_XLS.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal

Relatório do Saldo Consolidado da Restituição/Complemento de ICMS (SAFX304)

Localização: Menu Básicos à Report Fiscal, item de menu Obrigações Acessórias à ICMS por Substituição à Operações com Substituição Tributária à Saldo Consolidado Rest./Compl. ICMS (SPED-EFD 1250 e 1255) – Formato XLS



DOCUMENTO DE REQUISITO


Sumário

**TELA A SER DESENVOLVIDA	3**
1.	REGRAS DA TELA	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4

# TELA A SER DESENVOLVIDA

# REGRAS DA TELA




# REGRAS DE GERAÇÃO DO RELATÓRIO

**Origem das informações para geração:**

Para geração deste relatório, serão consideradas as informações da seguinte tabela:

SAFX304 - Tabela do Saldo Consolidado da Restituição/Complemento de ICMS;
Gerar as informações em um único arquivo no Formato XLS de todos os estabeleciemnto selecionados.

**Regra de seleção do Relatório:**

Deverá criar um relatório de conferência dos dados da tabela do Saldo Consolidado da Restituição/Complemento de ICMS (SAFX304) em formato XLS.

Como filtro para emissão do relatório, deve utilizar um período (data inicial e data final) e o estabelecimento.








---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS561102 | Andréa Rocha | Criação do Relatório do Saldo Consolidado da Restituição/Complemento de ICMS – Formato XLS. |
| MFS571642 | Graciela Soares | Ajuste na geração do relatório para gerar as informações de todos os estabelecimentos selecionados em um único arquivo no formato XLS. |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos registros do relatório. | MFS561102 |
| Data Final | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório. | MFS561102 |
| UF | Alfanumérico | S | S | Listbox | Neste campo será disponibilizada a lista montada com todas as Unidades Federativas, adicionando a opção * Todas as UFs*. Origem:Tabela ESTADO Montar a lista começando pela opção * Todas as UFs* e as demais opções em ordem crescente pela descrição da UF. | MFS561102 |
| Estabelecimento |  | S | S |  | Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login.   Serão disponibilizados para seleção os estabelecimentos que atendam a “UF” informada em tela.  Para montagem dessa listagem, fazer uma consulta envolvendo a tabela:     - ESTABELECIMENTO       Se campo “UF” for preenchido com opção  *Todas as Ufs*:         Considerar os estabelecimentos de todas as Unidades Federativas     Senão        Considerar apenas os estabelecimentos da UF selecionada.   Demonstrar os seguintes campos de forma concatenada, na listagem de estabelecimentos:     - COD_ESTAB + RAZAO_SOCIAL   Incluir a opção de selecionar todos os estabelecimentos. | MFS561102 |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Empresa | Texto |  | Código da empresa do login. | MFS561102 |
| Estabelecimento | Texto |  | Código do estabelecimento. | MFS561102 |
| CNPJ | Alfanumérico |  | Campo CNPJ da tabela Estabelecimento. | MFS561102 |
| Razão Social | Texto |  | Campo Razão social da tabela Estabelecimento. | MFS561102 |
| Data da Apuração | Numérico | Formato: DD/MM/AAAA | Campo 03- Data da Apuraçãoda SAFX304. | MFS561102 |
| Código do Motivo | Alfanumérico |  | Campo 04- Código do Motivo da SAFX304. | MFS561102 |
| Valor do ICMS | Numérico |  | Campo 05- Valor do ICMS da SAFX304. | MFS561102 |
| Valor do ICMS-ST Restituição | Numérico |  | Campo 06- Valor do ICMS-ST Restituição da SAFX304. | MFS561102 |
| Valor do FCP-ST  Restituição | Numérico |  | Campo 07- Valor do FCP-ST  Restituição da SAFX304. | MFS561102 |
| Valor do ICMS-ST Complemento | Numérico |  | Campo 08- Valor do ICMS-ST Complemento da SAFX304. | MFS561102 |
| Valor do FCP-ST Complemento | Numérico |  | Campo 09- Valor do FCP-ST Complemento da SAFX304. | MFS561102 |
