---
source: "MTZ-RF_Conf_Balancete_XLS.docx"
category: Report_Fiscal
converted: auto
---



THOMSON REUTERS

**Módulo Report Fiscal**

**Relatório de Balancetes - Formato XLS**


Localização: Menu Básicos, Módulo Report Fiscal, item Gerenciais  Contábil  Geral  Balancete - Formato XLS
Localização: MastersafDW >> SPED >> Escrituração Contábil Digital>> Relatórios>> Conferência (Saldos x Movimentos)




DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



Seu objetivo é a conferência do balancete, gerado em formato XLS.

**[MFS-66964]**
Criação do Relatório de Conferência de Erros, gerado em formato XLS, referente ao Erro não previsto pelo Sistema, em relação a informação do Campo 06 - COD_CONTA_SINT da tabela X2002_PLANO_CONTAS.


Data Inicial – Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos documentos fiscais.

Data Final – Neste campo o usuário informará uma data final, a ser utilizada como filtro dos documentos fiscais

Tipo Balancete – Este campo é uma lista com as seguintes opções: “Analítico”, “Sintético” e “Ambos”. Seu preenchimento é obrigatório.

[MFS37618] Inclusão do novo parâmetro
Saldo das Contas Sintéticas - O parâmetro deve ser do tipo Radiobutton, com as opções:
- Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas
- Utilizar o saldo mensal das contas sintéticas
Obs.: Somente deve ser habilitado quando for escolhida a opção “Tipo de Balancete” igual a “Ambos”.

[MFS40185] Inclusão do novo parâmetro
Estabelecimentos - O parâmetro deve ser do tipo Radiobutton, com as opções:
- Discriminados
- Todos Consolidados
Obs.: Somente deve ser habilitado quando for escolhida a opção “Saldo das Contas Sintéticas” igual a “Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas”.

[MFS47857] Inclusão de dois novos parâmetros

Demonstrar Contas Zeradas - O parâmetro deve ser do tipo checkbox, sendo o default desmarcado.

Saldo Antes do Encerramento - O parâmetro deve ser do tipo checkbox, sendo o default desmarcado.

Estabelecimentos – Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login.


Origem dos dados: Tabelas dos Saldos Mensais (SAFX02), Saldos Contábeis para Centro Custo (SAFX80) e Plano de Contas (SAFX2002).

Critérios de recuperação dos saldos na SAFX02/SAFX80:

- COD_EMPRESA – código da empresa do  login
- COD_ESTAB – estabelecimentos selecionados em tela
- DATA_SALDO – data fiscal que se enquadre no período informado em tela
- Tipo de Balancete – se parâmetro = “Analítico”  serão consideradas apenas as contas da SAFX2002 em que o Indicador da conta seja de Conta Analítica (IND_CONTA = “A”);
se parâmetro = “Sintético” serão consideradas apenas as contas da SAFX2002 em que o Indicador da conta seja de Conta Sintética (IND_CONTA = “S”);
se parâmetro = Ambos  serão consideradas todas as contas;

[MFS37618] Inclusão do novo parâmetro

Parâmetro: Saldo das Contas Sintéticas

Quando for escolhida a opção “Utilizar o saldo mensal das contas sintéticas”, o funcionamento atual do relatório se mantém, gerando o saldo das contas sintéticas a partir da tabela de Saldo Mensal (SAFX02 ou SAFX80).

Quando for escolhida a opção “Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas”, o relatório deve gerar os valores consolidados (Saldo Inicial, Débito, Crédito e Saldo Atual) das Contas Analíticas referentes à Conta Sintética superior, utilizando os níveis, ou seja, os valores das contas analíticas devem ser totalizados e mostrados na sua respectiva conta sintética.
Para cada conta analítica (campo 4 = “A” da SAFX2002) mostrada no relatório, verificar se ela tem uma conta sintética (campo 6 da SAFX2002) relacionada, se possuir, deve-se mostrar no relatório a conta sintética relacionada às contas analíticas, ou seja, a conta sintética deve vir acima das suas respectivas contas analíticas, demonstrando o total dos valores das contas analíticas.  Para relacionar as contas sintéticas às contas analíticas, deve-se observar o nível de cada conta (campo 8 da SAFX2002) para demonstrá-las no relatório, iniciando pela conta de menor nível (nível = 1).  Para as colunas de Saldo Inicial e Saldo Atual, deve-se utilizar o campo Débito/Crédito de cada uma, para calcular o total de cada saldo da conta sintética.  As contas sintéticas não vão possuir dados na tabela de Saldo Mensal, os valores serão sempre calculados a partir dos valores das contas analíticas.
Obs.: O saldo das contas analíticas são recuperados da tabela de Saldo Mensal (SAFX02) ou da tabela de Saldos Contábeis para Centro Custo (SAFX80).

[MFS40185] Inclusão do novo parâmetro

Parâmetro: Estabelecimentos

Quando for escolhida a opção “Discriminados”, o funcionamento atual do relatório se mantém, gerando o saldo das contas a partir da tabela de Saldo Mensal (SAFX02 ou SAFX80) por estabelecimento.

Quando for escolhida a opção “Todos Consolidados”, o relatório deve gerar os valores consolidados (Saldo Inicial, Débito, Crédito e Saldo Atual) das Contas Analíticas referentes à Conta Sintética superior, utilizando os níveis, ou seja, os valores das contas analíticas devem ser totalizados e mostrados na sua respectiva conta sintética. E também devem consolidar os valores de todos os estabelecimentos, os valores  (Saldo Inicial, Débito, Crédito e Saldo Atual) devem ser consolidados por Empresa e Conta Contábil.

[MFS47857] Inclusão de dois novos parâmetros

Parâmetro: Demonstrar Contas Zeradas

Quando este parâmetro for marcado, as contas contábeis que estão zeradas devem ser demonstradas no relatório, junto com as contas que possuem valores (saldo/débito/crédito).  Caso contrário, as contas zeradas, ou seja, as contas que não possuem valor de saldo, nem valor de débito e nem de crédito, não devem ser demonstradas no relatório.

Parâmetro: Saldo Antes do Encerramento

Quando este parâmetro for marcado, será realizado o cálculo abaixo.  Caso contrário, a geração do relatório não terá alteração.

Para cada conta, buscar na X01_CONTABIL todos os lançamentos de encerramento que estiverem dentro do período de geração do balancete e que pertencerem à empresa e estabelecimento selecionados na tela de geração (podem existir vários lançamentos de encerramento para uma mesma conta porque o encerramento pode ser feito por centro de custo). Depois de recuperados os lançamentos, sumarizar os valores encontrados (total de créditos – total de débitos) e o resultado dessa sumarização é o valor a ser demonstrado no relatório para aquela conta. Além do valor, o balancete deve demonstrar também o indicador (débito ou crédito), o indicador do saldo antes do encerramento será sempre o inverso do resultado da sumarização dos lançamentos de encerramento, ou seja, se após a sumarização obteve-se um valor de R$1000,00 a Crédito, no relatório será apresentado R$1000,00 a Débito.



[MFS40185] Inclusão do novo parâmetro

Parâmetro: Estabelecimentos = “Discriminados”

Os dados recuperados serão agrupados por Estabelecimento, e para cada Estabelecimento, será gerado um arquivo no formato XLS.

Os dados serão ordenados por Empresa, Estabelecimento, Data do Saldo e Conta Contábil

Parâmetro: Estabelecimentos = “Todos Consolidados”

Os dados recuperados serão agrupados por Empresa, será gerado um arquivo no formato XLS.

Os dados serão ordenados por Empresa, Data do Saldo e Conta Contábil






[MFS37618] Inclusão do novo parâmetro

Exemplo:


Obs.: As colunas de Indicador da Conta e Nível não são demonstradas no relatório, somente foram incluídas para exemplificar a geração das contas analíticas/sintéticas no relatório.


[MFS-66964] Inclusão de Relatório de Conferência de Erros – Contas Sintéticas inválidas

Parâmetros: Deverá ser gerado em tempo de execução do Relatório de Balancete XLS.

A necessidade de criação desse relatório se deve ao erro “não previsto pelo sistema” na geração do Relatório de Conferência do Balancete em Excel, que se referem as “Contas  Sintéticas” invalidadas (inexistentes na tabela) preenchidas no Campo 06 - COD_CONTA_SINT da tabela X2002_PLANO_CONTAS, causando o erro na geração, esses erros deverão ser “apontados” no novo “Relatório de Conferência de Erros”, e agrupados por Estabelecimento, a mesma regra da geração do Relatório de Balancete.

O Relatório de Conferência de Erros deverá ser disponibilizado no formato XLS para gravação na Aba “Arquivos”, somente quando for detectado o erro, e nesse caso não deverá ser disponibilizado o Relatório de Balancete para gravação.

Nome do Arquivo: REL_CONFERENCIA_ERRO.xls

O Relatório terá como base as informações do Cadastro do Plano de Contas, referente a conta contábil relacionada ao Saldo Contábil das tabelas SAFX02 e SAFX80, ou no caso dos Lançamentos antes do Encerramento a tabela SAFX01.

Obs.: O problema ocorre porque o Campo 06 - COD_CONTA_SINT da tabela X2002_PLANO_CONTAS não é um campo chave (Foreign Key) possibilitando ao usuário excluir a Conta Sintética da tabela, ocasionando o erro, porém para não causar impactos a outros clientes, a opção adotada foi criar o Relatório de Erro.

Quando ocorrer o erro, criar Log de Mensagem na Aba “Log”:

Log de Mensagem: “A Conta Sintética informado no Campo 06 - COD_CONTA_SINT da tabela X2002_PLANO_CONTAS é inválida ou inexistente, para correção do cadastro de Plano de Contas foi disponibilizado o Relatório “REL_CONFERENCIA_ERRO.xls” na Aba “Arquivos”.

**Preenchimento dos Dados do Relatório**





---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS36831 | Andréa Rocha | Este documento tem como objetivo criar o relatório do balancete em formato XLS | 15/05/2020 |
| MFS37618 | Andréa Rocha | Este documento tem como objetivo incluir a opção de demonstrar o saldo das contas sintéticas a partir dos saldos das contas analíticas. | 22/06/2020 |
| MFS40185 | Andréa Rocha | Este documento tem como objetivo incluir a opção de demonstrar os valores discriminados por estabelecimento ou todos consolidados. | 08/07/2020 |
| MFS-46761 | Alessandra Cristina Navatta | Disponibilizar o relatório também no SPED Contábil | 18/11/2020 |
| MFS-47857 | Andréa Rocha | Este documento tem como objetivo incluir dois novos parâmetros na tela, um para demonstrar as contas zeradas e o outro para demonstrar o Saldo Antes do Encerramento. | 15/12/2020 |
| MFS-66964 | Rogério Ohashi | Este documento tem como objetivo criar o relatório de Conferência de Erros em formato XLS, referente ao problema das Contas Sintéticas (Erro não previsto pelo Sistema). | 02/07/2021 |


---

| RN00 | Regras Gerais |
| --- | --- |



---

| RN01 | Parâmetros de Tela |
| --- | --- |



---

| RN02 | Recuperação dos Dados |
| --- | --- |



---

| RN03 | Processamento |
| --- | --- |



---

| RN04 | Preenchimento dos Dados |
| --- | --- |



---

| Empresa | Código da empresa do login |
| --- | --- |
| Estabelecimento | [MFS40185] Inclusão do novo parâmetro Se Parâmetro Estabelecimentos = “Discriminados”    Código do estabelecimento da tabela Estabelecimento Senão     Esta coluna não será gerada. |
| Razão Social | [MFS40185] Inclusão do novo parâmetro Se Parâmetro Estabelecimentos = “Discriminados”      Razão social da tabela Estabelecimento Senão       Esta coluna não será gerada. |
| CNPJ | [MFS40185] Inclusão do novo parâmetro Se Parâmetro Estabelecimentos = “Discriminados”       CNPJ da tabela Estabelecimento Senão       Esta coluna não será gerada. |
| Insc. Estadual | [MFS40185] Inclusão do novo parâmetro Se Parâmetro Estabelecimentos = “Discriminados”      Inscrição estadual da tabela Registro Estadual, referente a UF do estabelecimento Senão       Esta coluna não será gerada. |
| Período Inicial | Data inicial informada em tela |
| Período Final | Data final informada em tela |
| Conta Número | Código da conta contábil: Se o saldo for da SAFX02  campo 03- Conta Contábil;  Se o saldo for da SAFX80  campo 04- Conta Contábil; |
| Descrição | Descrição da conta (campo 03 da SAFX2002) referente a conta contábil |
| Centro de Custo | Centro de Custo: Se o saldo for da SAFX02  neste caso, a coluna não será preenchida;  Se o saldo for da SAFX80  campo 05-Centro de Custo; |
| Saldo Anterior | Saldo Anterior  Se o saldo for da SAFX02  campo 05- Saldo Inicial;  Se o saldo for da SAFX80  campo 06- Saldo Contábil Anterior; |
| Ind. Saldo Anterior | Indicador de Débito/Crédito do Saldo Anterior  Se o saldo for da SAFX02  campo 06- Débito/Crédito;  Se o saldo for da SAFX80  campo 07-Crédito / Débito Anterior; |
| Débitos | Total do Débito  Se o saldo for da SAFX02  campo 10- Total Débito;  Se o saldo for da SAFX80  campo 08- Total Débito; |
| Créditos | Total do Crédito  Se o saldo for da SAFX02  campo 09- Total Crédito;  Se o saldo for da SAFX80  campo 09- Total Crédito; |
| Saldo Atual | Saldo Atual  Se o saldo for da SAFX02  campo 07- Saldo Final;  Se o saldo for da SAFX80  campo 10- Saldo Contábil Atual; |
| Ind. Saldo Atual | Indicador de Débito/Crédito do Saldo Atual Se o saldo for da SAFX02  campo 08- Débito/Crédito;  Se o saldo for da SAFX80  campo 11-Crédito / Débito Anterior; |
| Saldo Ant Encerramento | [MFS47857] Essa coluna só deve ser demonstrada no relatório, se o parâmetro “Saldo Antes do Encerramento” estiver marcado.    Saldo Antes do Encerramento  campo 07- Valor do Lançamento Contábil da SAFX01 Obs.: Para maiores detalhes, consultar a regra do parâmetro “Saldo Antes do Encerramento”. |
| Ind. Saldo Ant Encerramento | [MFS47857] Essa coluna só deve ser demonstrada no relatório, se o parâmetro “Saldo Antes do Encerramento” estiver marcado.    Indicador de Débito/Crédito do Saldo Antes do Encerramento Preencher de acordo com o valor de lançamento da coluna “Saldo Ant Encerramento”. Obs.: Para maiores detalhes, consultar a regra do parâmetro “Saldo Antes do Encerramento”. |


---

| RN05 | Exemplo do cálculo do saldo das contas sintéticas a partir do saldo das contas analíticas |
| --- | --- |



---

| Relatório de Balancete | Relatório de Balancete | Relatório de Balancete | Relatório de Balancete | Relatório de Balancete | Relatório de Balancete | Relatório de Balancete |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Conta Contábil | Saldo Inicial | IND D/C | Débito | Crédito | Saldo Final | IND D/C | Indicador da Conta | Nível |
| 1 - Ativo | 2300,00 | D | 3100,00 | 1700,00 | 3700,00 | D | S | 1 |
| 1.1- Ativo Circulante | 1400,00 | D | 1500,00 | 800,00 | 2100,00 | D | S | 2 |
| 1.1.001 – Conta A | 1100,00 | D | 800,00 | 300,00 | 1600,00 | D | A | 3 |
| 1.1.002 – Conta B | 100,00 | D | 500,00 | 400,00 | 200,00 | D | A | 3 |
| 1.1.003 – Conta C | 200,00 | D | 200,00 | 100,00 | 300,00 | D | A | 3 |
| 1.2- Ativo não Circulante | 900,00 | D | 1600,00 | 900,00 | 1600,00 | D | S | 2 |
| 1.2.001 – Conta J | 1000,00 | D | 900,00 | 500,00 | 1400,00 | D | A | 3 |
| 1.2.002 – Conta L | 100,00 | C | 700,00 | 400,00 | 200,00 | D | A | 3 |


---

| RN06 | Relatório de Conferência de Erro |
| --- | --- |



---

| Empresa | Código da empresa do Login       (Conforme Relatório de Balancete Formato XLS) |
| --- | --- |
| Estabelecimento | Código de Estabelecimento         (Conforme Relatório de Balancete Formato XLS) Senão     Esta coluna não será gerada. |
| Conta Número | Código da Conta Contábil            (Conta Contábil que ocasionou o Erro não Previsto pelo Sistema) |
| Validade Conta | Validade da Conta Contábil         (Informações da Conta Contábil) |
| Descrição | Descrição da Conta Contábil       (Informações da Conta Contábil) |
| Indicador da Conta | Indicador da Conta Contábil        (Informações da Conta Contábil) |
| Natureza da Conta | Natureza da Conta Contábil        (Informações da Conta Contábil) |
| Nível | Nível da Conta Contábil               (Informações da Conta Contábil) |
| Situação | Situação da Conta Contábil         (Informações da Conta Contábil) |
| Código Conta Sintética | Código da Conta Sintética           (Informações da Conta Contábil) |
| Erro | Mensagem de Log: O campo de “Código de Conta Sintética” Informado, não existente ou inválida na tabela de Plano de Contas. Consulte o Cadastro no Caminho: Básicos>>Data Warehouse>>Manutenção>>Códigos>>Plano de Contas. |
