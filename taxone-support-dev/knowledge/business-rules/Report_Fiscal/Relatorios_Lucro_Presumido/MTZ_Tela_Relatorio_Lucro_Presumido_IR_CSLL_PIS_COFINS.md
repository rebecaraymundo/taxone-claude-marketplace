---
source: "MTZ_Tela_Relatorio_Lucro_Presumido_IR_CSLL_PIS_COFINS.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Lucro Presumido IR/CSLL/PIS/COFINS
Report Fiscal >> Relatórios >> Lucro Presumido



DOCUMENTO DE REQUISITO


Sumário

**1 - OBJETIVO	3**
2 - TELA	3
3 - Regras dos Campos	3
4. REGRAS DE GERAÇÃO DO RELATÓRIO	5
5. Formato	12
6. Layout	12

# 1 - OBJETIVO

Criar uma tela, para identificar quais contas devem ser incluídas e os métodos de recuperação de valores correspondentes, organizados por agrupamento (definido na tela de Agrupamento de Relatório), a serem considerados na elaboração do relatório de Apuração do Lucro Presumido IR/CSLL/PIS/COFINS."

# 2 - TELA





# 3 - Regras dos Campos

Localização da tela: Módulo: Básicos>> Report Fiscal
Menu: Relatórios >> Lucro Presumido >> Lucro Presumido IR/CSLL/PIS/COFINS

Título da tela: Apuração do Lucro Presumido IR/CSLL/PIS/COFINS



# 4. REGRAS DE GERAÇÃO DO RELATÓRIO

**Regra Geral:**

**Origem das informações para geração:**

Para geração deste relatório, serão consideradas as informações da seguinte origem para os dados contábil:


- SAFX02 – Tabela de Saldos Mensais

- Para os dados fiscais considere as origens:
- SAFX07 – Capa Nota Fiscal
- *SAFX08 – Item de Mercadoria
- *SAFX09 – Item de Serviços
- SAFX147 – Demais documentos e Operações Geradoras de crédito
- SAFX148 – Bens do Ativo Imobilizado Com Base nos Encargos de Depreciação e no valor de aquisição
- SAFX183 – Demais Documentos– Lucro Presumido

**Regra de seleção:**

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Exercício = informado em tela
-Apuração = Informado em tela
-Empresa = empresa


Se de acordo com os critérios informados, caso não existam informações recuperadas (saldo ou nenhuma informação das origens fiscais o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.
Se não for encontrada parametrizações (agrupamento e/ou recuperação de contas), exibir a mensagem: NÃO EXISTEM PARAMETRIZAÇÕES PARA A GERAÇÃO DO RELATÓRIO”

**Regra de processamento:**

Para cada empresa selecionada em tela será gerado um relatório.
Serão recuperadas as informações com base no agrupamento criado (tela Agrupamento Relatório) e as respectivas contas associadas a esse agrupamento (Tela Recuperação de Contas), considerando inclusive, qual campo será considerado para a recuperação dos valores. Essa estrutura será construída no momento da geração do relatório, de acordo com as definições de filtro (apuração, período e empresa), indicados na tela de geração do relatório.
Quando o agrupamento se tratar de recuperação de contas, ele será apresentado no relatório, uma conta abaixo da outra (ordenado pelo campo código de conta).
Já o agrupamento (Totalizador), será considerado o valor total, das contas associadas ao agrupamento (uma única linha).
Independente do Comportamento do Agrupamento, sempre deverá ser considerado a informação indicada no campo recuperação de valores, para saber qual campo de valor deve ser considerado.

Recuperação de Valores = Crédito: Considera o campo 09 – VLR_TOT_CRE da SAFX02

Recuperação de Valores = Débito: Considera o campo 10 – VLR_TOT_DEB da SAFX02

Recuperação de Valores = Movimento: Considera o resultado da expressão (campo 10 – VLR_TOT_DEB – campo 09 – VLR_TOT_CRE) da SAFX02

Recuperação de Valores = Saldo Final: Considera o campo 07 – VLR_SALDO_FIM da SAFX02

Para a coluna fiscal, considerar o valor da base de COFINS, da conta vinculada às tabelas X08, X09, X147X, X148 e X183, considerando:

**Nas tabelas X08_ITENS_MERC e X09_ITENS_SERV**
COD_EMPRESA
IDENT_CONTA
DATA_FISCAL
VLR_BASE_COFINS

**Na tabela X147_OPER_CRED**
COD_EMPRESA
IDENT_CONTA
DATA_OPER
VLR_BASE_COFINS

**Na tabela X148_BENS_ATIVO_IMOB**
COD_EMPRESA
IDENT_CONTA
DATA_LANCTO
VLR_BASE_COFINS

**Na tabela X183_PJ_APUR_LP (X183)**
COD_EMPRESA
IDENT_CONTA
DATA_OPER
VLR_BASE_COFINS

Exemplo para Montagem do relatório: O relatório será gerado dinamicamente, de acordo com os agrupamentos criados na tela de Agrupamento Relatório, seguindo a ordem cronológica indicada na parametrização. Exemplo:


Os Agrupadores estáticos, contendo os totalizadores, ordenados, conforme print e coluna IRCS (as colunas Comentário, IRCS e PC, não são apresentadas no relatório, apenas servirá de referência para desenvolvimento)


Segue regras do preenchimento dos dados no relatório:



# 5. Formato

Gerar o relatório em formato CSV

# 6. Layout

O layout do relatório está disponível no arquivo Relatório de Apuração Lucro Presumido IRCSLL Sinergia PISCOFINS.xlsx (conforme abas Apuração Mensal e Apuração Trimestral). No arquivo há o detalhamento das regras em cada célula, exemplificando melhor os cenários e os cálculos a serem executados.
**IMPORTANTE!!! Não deve ser exibido no relatório as colunas C, D, E e F**


---

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-865787 | Alessandra Cristina Navatta | Criação do Documento |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Exercício | Texto | S | S | Default: Ano corrente | Informar o exercício que será considerado para a geração do relatório.  Com base no exercício informado (AAAA), deverá ser considerado o período (anual completo), ou seja, 01/01/AAAA até 31/12/AAAA, para a recuperação das informações na base.  Campo numérico.  Trazer por default o ano corrente, mas, o usuário pode editar. | MFS-865787 |
| Apuração | Lista | S | S | Default: Mensal | Lista de Valores Válidos;  Mensal Trimestral | MFS-865787 |
| Empresa | Lista | S | S | Cód – Razão Social | Exibe todas as empresas que o usuário tem acesso.  Pode ser selecionada uma ou mais empresas.   Como facilitador, poderão ser utilizadas as opções “Marcar Todos” e “Selecionar”. | MFS-865787 |
| Confirma | Botão |  |  |  | Campos obrigatórios não preenchidos:  Quando o campo Exercício, não for preenchido, exibir a mensagem: “Informe o Exercício”  Quando o campo Apuração, não for preenchido, exibir a mensagem: “Informe a Apuração”   Pelo menos uma empresa deve ser selecionada, caso contrário, exibir a mensagem:”Selecione pelo menos uma Empresa” | MFS-865787 |


---

| Cabeçalho | Cabeçalho | Cabeçalho |
| --- | --- | --- |
| Título | Título | Título |
| Descrição do Agrupamento |  | Agrupamento 1 – Recuperação de Contas (tela de Agrupamento  Relatório) |
| 3010100000 - xxx | Conta Contábil selecionada | Conforme Recuperação de Contas (vinculada ao agrupamento 1, conta 1) |
| 3010701010 - xxx | Conta Contábil selecionada | Conforme Recuperação de Contas (vinculada ao agrupamento 1, conta2) |
| Totalizador |  | Totalizador - (Somatório das contas associadas ao agrupamento1) |


---

|  | Comentário | IRCS | PC |  |
| --- | --- | --- | --- | --- |
| Base de Cálculo Imposto de Renda |  |  |  |  |
| Receita operacional bruta (8%) | Totalizador agrupamento | IR08 | x | Conforme Agrupamento Usuário (Soma Código Base IR08 *8%) |
| Receita operacional bruta (32%) | Totalizador agrupamento | IR32 | x | Conforme Agrupamento Usuário (Soma Código Base IR32 *32%) |
| Receitas financeiras | Totalizador agrupamento | IRRF | x | Conforme Agrupamento Usuário (Soma Código Base IRRF) |
| Demais Receita Tributáveis | Totalizador agrupamento | IRDR | x | Conforme Agrupamento Usuário (Código Base IRDR) |
| Base de Cálculo antes da Compensação: | Cálculo |  | x |  |
| Base de Cálculo do Imposto IRPJ | Cálculo |  | x |  |
|  |  |  |  |  |
| Imposto e Adicional: |  |  | x |  |
| IRPJ 15% | Cálculo |  | x |  |
| IRPJ 10% Adicional | Cálculo |  | x |  |
| Imposto Devido IRPJ | Cálculo |  | x |  |
|  |  |  |  |  |
| Base de Cálculo da Contribuição: |  |  |  |  |
| Receita operacional bruta (12%) | Totalizador agrupamento | IR08 | x | Conforme Agrupamento Usuário - Soma Código Base IR08 *12% |
| Receita operacional bruta (32%) | Totalizador agrupamento | IR32 | x | Conforme Agrupamento Usuário - Soma Código Base IR32 *32% |
| Receitas Financeiras | Totalizador agrupamento | IRRF | x | Conforme Agrupamento Usuário - Soma Código Base IRRF |
| Demais Receita Tributáveis | Totalizador agrupamento | IRDR | x | Conforme Agrupamento Usuário - Código Base IRDR |
| Base de Cálculo antes da Compensação | Cálculo |  | x | Soma |
|  |  |  |  |  |
| Base de Cálculo da Csll | Cálculo |  | x |  |
| CSLL a Pagar 9% | Cálculo |  | x |  |
|  |  |  |  |  |
| Resumo |  |  | x |  |
| IRPJ a Pagar | Cálculo |  | x |  |
| CSLL a Pagar | Cálculo |  | x |  |
| Total | Cálculo |  | x |  |
|  |  |  |  |  |
| PIS/COFINS |  |  |  |  |
| PIS |  |  |  |  |
| Base de Cálculo - Não Cumulativo 0,65% | Totalizador agrupamento | x | PCNC | Conforme Agrupamento Usuário - Soma Código Base PCNC *0,65% |
| Base de Cálculo - Cumulativo | Totalizador agrupamento | x | PCCM | Conforme Agrupamento Usuário - Soma Código Base PCNC *1,65% |
| COFINS |  |  |  |  |
| Base de Cálculo - Não Cumulativo 3,00% | Totalizador agrupamento | x | PCNC | Conforme Agrupamento Usuário - Soma Código Base PCNC *3,00% |
| Base de Cálculo - Cumulativo | Totalizador agrupamento | x | PCCM | Conforme Agrupamento Usuário - Soma Código Base PCNC *7,60% |
|  |  |  |  |  |
| PIS A RECOLHER | Cálculo | x |  |  |
| COFINS A RECOLHER | Cálculo | x |  |  |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| CNPJ da Empresa | Texto | 99.999.999/9999-99 | Apresenta o CNPJ da empresa | MFS-865787 |
| Razão Social da Empresa | Texto | Código – Razão Social | Apresenta o Cód e Razão Social da Empresa | MFS-865787 |
| Exercício | Texto |  | Informação do campo Exercício indicado na tela | MFS-865787 |
| Período do Processamento |  | DD/MM/AAAA à DD/MM/AAAA | Informação do início e fim do exercício. | MFS-865787 |
| Data e Hora Geração | Texto | DD/MM/AAAA às HH:MM:SS hs | Data e hora que o relatório foi gerado | MFS-865787 |
| Título | Texto |  | Título do relatório: “Apuração Lucro Presumido com Sinergia PIS/COFINS” | MFS-865787 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Agrupamento | Texto |  | Apresentar os agrupamentos, de acordo com o num. Ordem indicado na tela de parametrização.  Os agrupamentos de Comportamento Recuperação de Contas, serão detalhados (linha a linha), cada conta vinculada a ele (ordenadas pelo código da conta).  Se o agrupamento for de Comportamento Totalizador, será consolidado todos os valores das contas vinculadas a esse agrupamento em uma única linha. | MFS-865787 |
| Meses/Trimestres/Anual | Colunas |  | Serão apresentados sempre os valores por mês. Se a apuração = Mensal, será exibida após o mês de dezembro uma coluna  Anual.  Apenas será exibida as colunas (1º Trimestre, 2º Trimestre, 3ºTrimestre, 4ºTrimestre, quando for selecionado na tela de geração do relatório a Apuração Trimestral. Além das colunas mensais.  Quando houver as colunas trimestrais, deve ser consolidados os valores gerados nos respectivos meses do trimestre. Exemplo: Período 01/01 à 03/06, serão geradas as colunas de janeiro, fevereiro, março, 1º trimestre (totalizando os três meses), abril, maio, junho, 2º Trimestre (totalizando os três meses)  IMPORTANTE!!! As colunas Trimestres e Anual, totalizam os valores da coluna ‘’Contábil’, dos meses em questão (3 e 12 respectivamente). | MFS-865787 |
| contábil | Coluna |  | Considera as informações das contas, conforme os agrupamentos, com base nas regras de Comportamento e as tabelas do item 1 do tópico: Origem das informações para geração, deste documento. | MFS-865787 |
| Fiscal | Coluna |  | Considera as informações das contas, conforme os agrupamentos, com base nas tabelas do item 2 do tópico: Origem das informações para geração, deste documento. | MFS-865787 |
| check | Coluna |  | Resultado da Expressão: (Valor da Coluna Contábil – Valor da Coluna Fiscal) | MFS-865787 |
