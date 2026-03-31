---
source: "MTZ_Report_Fiscal_Tela_Conferencia_Movimento_Registro_Saida_Modelos_P2_PA.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Report Fiscal
Tela Conferencia do Movimento do Registro de Saídas Modelos P2/P2A



DOCUMENTO DE REQUISITO


Sumário

**1.	TELA A SER DESENVOLVIDA	1**
1.1.	Diagrama de Casos de Uso	1
1.1.1.	UC001 – Manutenção da Estrutura Padrão	1
1.1.1.1.1.	Fluxo Principal	1
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	1
2.	Regras dos Campos	1
3.	Recuperação dos dados:	1
4.	Itens do Relatório	1
4.1 – Principal	1
3.2 – Resumo por Decendio	1
3.3 – Resumo por Quinzena	1
3.4 – Resumo da Observação	1
3.5 – Resumo por UF	1
3.6 – Resumo por Alíquota	1
3.7 – Resumo por CFO	1
5.	Tratamento dos Parâmetros p/ UF	1
6.	Tramentos de Situações especiais	1

# TELA A SER DESENVOLVIDA

[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

## Diagrama de Casos de Uso




## UC001 – Manutenção da Estrutura Padrão

[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]


### Fluxo Principal

[Descrever a ação principal que será realizada na tela especificada.

Ex.: O usuário deseja realizar o cadastro de uma estrutura padrão.



### Fluxo Alternativo 1 – Localizar registros (Exemplo)



# Regras dos Campos

Localização da tela: Básicos >> Report Fiscal

Título da tela: Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart Movimentos de Saídas >> Ajuste SINIEF.




# Recuperação dos dados:

Origem dos Dados: Tabelas de Documento Fiscal (SAFX07, SAFX08, SAFX09).
Critérios de Seleção:
- Codigo da Empresa de login
- Estabelecimento informado na tela
- Data fiscal compreendida no período da geração
- Classificação do Documento Fiscal = 1, 2, 3, 4

São recuperada notas fiscais com e sem itens.


# Itens do Relatório


## 4.1 – Principal

Os livros de saída do modelo Ajuste SINIEF (P2 e P2A), que apresentam os valores das bases (tributada, isenta/redução e outras) em linhas distintas, devem fazer o lançamento das bases da seguinte forma:

Consolidação dos valores por documento fiscal:

As bases tributadas devem ser totalizadas por Imposto (ICMS, IPI ou ST), CFOP e Alíquota

As demais bases (isenta/redução e outras) devem ser totalizadas por Imposto (ICMS, IPI ou ST) e CFOP. Neste caso, a alíquota não precisa ser considerada, uma vez que ela não aparece nas linhas referentes a estes valores.

Exemplo: Supondo uma nota com os seguintes itens:


A demonstração das bases no livro deve será feita da seguinte forma:



## 3.2 – Resumo por Decendio


## 3.3 – Resumo por Quinzena


## 3.4 – Resumo da Observação


## 3.5 – Resumo por UF


## 3.6 – Resumo por Alíquota


## 3.7 – Resumo por CFO


# Tratamento dos Parâmetros p/ UF





# Tramentos de Situações especiais





---

| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-5333 | Registro de Saídas Modelos P2/P2A | Tela Conferencia do Movimento do Registro de Saída Modelos P2/P2A |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal |  |
| Pré- Condições |  |
| Pós-Condições |  |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
| [Descrever a interação do ator com o sistema.  Ex.: O usuário acessa a tela de estrutura padrão]. | [Descrever a ação esperada do sistema Ex.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”.] |
| [Ex.:O usuário preenche os campos da Manutenção de Estrutura do Produto. <<Fluxo Alternativo 1>> | [Ex.:O sistema apresenta os campos preenchidos.] |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário clica no botão “Localizar”. | O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados. |
|  | Fim do fluxo Alternativo |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estab. Centralizador |  |  |  |  | Lista todos os estabelecimentos da empresa de login. Caso o estabelecimento seja um estabelecimento Centralizador pertencente a uma Central de Escrituração (Módulo Controle de Obrigações Estaduais, menu Obrigações >> Central de Escrituração), ao selecionar este estabelecimento, os estabelecimentos centralizados serão apresentados marcados na lista de Estabelecimentos. |  |
| Obrigação Fiscal |  |  |  |  | Lista composta pelos livros - 102 - 104 |  |
| Período |  |  |  |  | Composto pela Data Inicial e Final |  |
| Observação Capa |  |  |  | Check box | Se esta opção for selecionada as observações de ICMS, ICMS-ST e IPI constantes na Capa do Documento Fiscal (SAFX07 – itens 37, 41 e 49) são apresentadas no Resumo da Observação. |  |
| Exibir | Radio Button | S | S | Default: CPF/CNPJ | Este parâmetro se aplica no preenchimento do campo Código do Destinatário da parte Principal do relatório.  Caso selecionado “CPF/CNPJ”, recuperar a informação do campo CPF_CGC (campo 06) da tabela X04_PESSOA_FIS_JUR, vinculado à nota fiscal. Deve conter 11 posições (para CPF) e 14 (para CNPJ)   Caso selecionado “Código do Destinatário”, recuperar a informação do campo COD_FIS_JUR (campo 02) da tabela X04_PESSOA_FIS_JUR, vinculado à nota fiscal. Deve conter 14 posições. | MFS-5333 |
| Emite ‘ISENTO’ se Exterior | Checkbox | N | S | Default: Não Selecionado | Este parâmetro se aplica no preenchimento do campo Código do Destinatário da parte Principal do relatório.  Caso selecionado irá emitir o conteúdo “ISENTO” no campo ‘Código do Destinatário’ para CPF/CNPJ do exterior.  Obs:  Este campo será desabilitado caso selecionada a opção “Código do Destinatário” no campo “Exibir”. | MFS-5333 |
| Campo a ser exibido |  |  |  | radiobutton | Este parâmetro se aplica no preenchimento do campo Codificação da parte Principal do relatório.  Campo composto pelas opções: - Conta Contábil - No de Controle Caso seja escolhida a opção Conta Contábil, na parte Principal do relatório será demonstrada na coluna “Codificação” a Conta Contábil da Capa do Documento Fiscal.  Caso seja escolhida a opção No de Controle, na parte Principal será demonstrada na coluna “Codificação” o No de Controle, que é uma composição do número do documento + código do estabelecimento. |  |
| ICMS Retido/Outras |  |  |  |  | Este parâmetro se aplica a Base Outras de ICMS demonstrada na Parte Principal, nos Resumos p/ Decêndio, p/ Quinzena, p/ UF  e p/ CFOP.  Caso seja selecionado, o Valor do ICMS-ST será somado à Base Outras de ICMS, nas seguintes condições: - Se o campo Apropria ICMS-ST da NF estiver marcado e o parâmetro 25 dos Parâmetros p/ UF do módulo ICMS desmarcado.  - Se o campo Apropria ICMS-ST da NF estiver desmarcado e o parâmetro 26 dos Parâmetros p/ UF do módulo ICMS desmarcado.  Parâmetros p/ UF do módulo ICMS:  Quando os parâmetros 25 e 26 são marcados, o valor do ICMS-ST é demonstrado no Resumo da Observação e não irá compor a Base Outras de ICMS. |  |
| OBS de Redução |  |  |  |  | Esse parâmetro se aplica ao Resumo da Observação.  Se marcado, é atribuída uma observação às notas fiscais que tenham Base Reduzida de ICMS, demonstrando o valor da base reduzida de ICMS. Observação: “Redução de R$9999,99 na Base do ICMS. Onde R$9999,99 é o valor da base reduzida. |  |
|  |  |  |  |  |  |  |


---

|  | Aliq ICMS | ICMS | BASE 1 | BASE 2 | BASE 3 | BASE 4 |
| --- | --- | --- | --- | --- | --- | --- |
| Item 1 (cfop 5101) | 0,00 | 0,00 | 0,00 | 100,00 | 0,00 | 0,00 |
| Item 2 (cfop 5101) | 10,00 | 8,00 | 80,00 | 20,00 | 0,00 | 0,00 |
| Item 3 (cfop 5101) | 12,00 | 48,00 | 400,00 | 0,00 | 0,00 | 0,00 |


---

| CFOP | ICMS / IPI | Cod | Base de Cálculo | Alíquota | Imposto Creditado |
| --- | --- | --- | --- | --- | --- |
| 5101 | ICMS | 1 | 80,00 | 10,00 | 8,00 |
| 5101 | ICMS | 1 | 400,00 | 12,00 | 48,00 |
| 5101 | ICMS | 2 | 120,00 |  |  |


---

| Parâmetro | Regra |
| --- | --- |
| 6 – Observação Redução Base Cálculo | Gera uma observação no Resumo da Observação com o valor da Base de Redução de ICMS. |
| 29- Observação Capa/Item (P1/P2) |  |
|  |  |
| 44 – Cálculo do ICMS c/ base na Resolução SEFCON n 4055 | Zera Alíquota do ICMS, Valor do ICMS e bases tributada, isenta e outras de ICMS. |
|  |  |
|  |  |
|  |  |
|  |  |


---

| Situação | Regra |
| --- | --- |
| Nota Cancelada | Zera valor contábil, ICMS, Alíquota       pItem.VLR_CONTAB_ITEM    := 0;         pItem.VLR_BASE_ICMS_1    := 0;         pItem.VLR_BASE_ICMS_2    := 0;         pItem.VLR_BASE_ICMS_3    := 0;         pItem.ALIQ_TRIBUTO_ICMS  := 0;         pItem.VLR_TRIBUTO_ICMS   := 0;         pItem.COD_CFO            := null; |
| Transferência de Crédito de ICMS | Zera valor contábil,     	 pItem.VLR_CONTAB_ITEM    := 0;           pItem.VLR_BASE_ICMS_1    := 0;           pItem.VLR_BASE_ICMS_2    := 0;           pItem.VLR_BASE_ICMS_3    := 0;           pItem.ALIQ_TRIBUTO_ICMS  := 0;           pItem.VLR_TRIBUTO_ICMS   := 0; |
|  |  |
