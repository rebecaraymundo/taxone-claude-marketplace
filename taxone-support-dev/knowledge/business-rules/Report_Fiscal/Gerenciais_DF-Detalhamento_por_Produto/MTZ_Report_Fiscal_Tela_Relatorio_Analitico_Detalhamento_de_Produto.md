---
source: "MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto.docx"
category: Report_Fiscal
converted: auto
---

**Relatório Analítico por Documento**

Localização: Menu Básicos, Módulo Report Fiscal, Gerenciais, Documentos Fiscais, Analíticos, Detalhamento por Produto

**DOCUMENTO DE REQUISITO**


**REGRAS DE NEGÓCIO**


Considerações deste modelo:
**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**
**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS4073 | Criação do Relatório Analítico por Produto | Validação das Críticas da Tela |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN01 | Campo “Período”: Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA  a  DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para criar o relatório.  Obrigatoriedade: S Obs.: No campo da data final, o usuário deverá informar um período maior ou igual ao período inicial. Caso informe um período menor do que o período inicial retornar a mensagem: “O período final informado deve ser maior ou igual ao período inicial”. | OS4073 |
| RN02 | Campo “Seleção de CFOP’s”:  Este campo exibe todos os códigos fiscais.  Exibir os CFOP’s da SAFX2012. | OS4073 |
| RN03 | Botão “Marcar Todos”:  Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's automaticamente. | OS4073 |
| RN04 | Botão “Desmarcar Todos”:  Este botão ao ser acionado, deverá  desmarcar todos os códigos CFOP's automaticamente . | OS4073 |
| RN05 | Botão “Marcar Entradas”:  Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's de entradas automaticamente (códigos iniciados por 1, 2 ou 3). | OS4073 |
| RN06 | Botão “Desmarcar Entradas”:  Este botão ao ser acionado, deverá desmarcar todos os códigos CFOP's de entradas automaticamente (códigos iniciados por 1, 2 ou 3). | OS4073 |
| RN07 | Botão “Marcar Saídas”:  Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's de saída automaticamente (códigos iniciados por 5, 6 ou 7). | OS4073 |
| RN08 | Botão “Desmarcar Saída”:  Este botão ao ser acionado, deverá desmarcar todos os códigos CFOP's de saída (códigos iniciados por 5, 6 ou 7). | OS4073 |
| RN09 | Campo “UF”:  Campo para informar a UF dos estabelecimentos que deseja para a geração do relatório. | OS4073 |
| RN10 | Campo “Estabelecimento”:  Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do Report Fiscal. Caso o usuário selecione uma UF específica, demonstrar apenas os estabelecimentos pertencentes ao Estado selecionado. | OS4073 |
| RN11 | Botão “Marcar Todos”:  Este botão ao ser acionado, deverá selecionar todos os estabelecimentos automaticamente. | OS4073 |
| RN12 | Botão “Desmarcar Todos”:  Este botão ao ser acionado, deverá  desmarcar todos os estabelecimentos automaticamente . | OS4073 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

