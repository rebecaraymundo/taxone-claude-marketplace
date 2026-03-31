---
source: "MTZ_REPORT_FISCAL_Balancete_Moeda_Funcional.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Balancete Moeda Funcional



DOCUMENTO DE REQUISITO


Sumário

**1.	TELA A SER DESENVOLVIDA	3**
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	5
2.1.	Leiaute da Tela	7
3.	Regras de Geração do Relatório	8

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

**Localização da tela**
Módulo: Basicos >> Report Fiscal
Menu: Gerenciais >> Contabil >>Geral >> Balancete Moeda Funcional

Módulo: SPED >> ECD – Escrituração Contábil Fiscal
Menu: Relatórios >> Balancete Moeda Funcional




Título da tela: Balancete Moeda Funcional


## Leiaute da Tela














# Regras de Geração do Relatório

Origem das informações para geração: SAFX226 – Saldo Contábil em Moeda Funcional, SAFX227 – Saldo Contábil por Centro de Custo em moeda funcional e  SAFX225 Lançamento Contábil em Moeda Funcional.

Regra de seleção: Para emissão do relatório devem ser consideradas as tabelas SAFX226 Saldo Contábil em Moeda Funcional, SAFX227 Saldo por centro de custo em moeda funcional (quando o parâmetros estiver selecionado) ,SAFX2002 Plano de Contas e SAFX225 Lançamento Contábil em Moeda Funcional.


O relatório deverá conter os dados compreendidos no período informados na tela de parametrização no campo período <<PERIODO>>.

Quando selecionado a opção <<SALDO ANTES DO ENCERRAMENTO>> na tela de parametrização do relatório, este deverá exibir a coluna SALDO ANTES DO ENCERRAMENTO.

**[ALTERADA – MFS3790]**
Quando o campo de Considerar Saldos por Centro de Custo estiver marcado na tela de emissão do balancete, será adicionado uma coluna com o nome “Centro de Custo” (nesse caso haverá mudança de layout do relatório e a coluna Descrição ficará como linha abaixo do código da conta e o centro de custo será demonstrado na coluna ao lado do código da conta).

Quando a opção de Considerar Saldos por Centro de Custo estiver marcada na tela de emissão do balancete, será adicionado o seguinte processamento (além do processamento já realizado atualmente): A recuperação será feita por meio de duas tabelas, pela SAFX226 e SAFX227, porém quando o registro de saldo estiver demonstrado na SAFX227 não demonstrar os saldos dos registros contidos na SAFX226.


O relatório deverá considerar o range de dados indicados pelos códigos das contas contábeis que será informado pelo usuário nos campos <<Conta Contábil Inicial>> e <<Conta Contábil Final>> na tela de parametrização. No caso em que não for parametrizada nenhuma conta, então deverá trazer todos os saldos disponíveis.

A opção <<Tipo Balancete>> da tela de parametrização traz as seguintes condições para o relatório: Se a opção <<Analítico>> estiver marcada o relatório terá trazer os saldos informados das tabelas SAFX226 ou SAFX232 das contas contábeis cujo campo <<IND_CONTA>> da tabela SAFX2002 estiver preenchido com “A”; Se a opção <<Sintético>> estiver marcada o relatório terá que trazer os saldos informados das tabelas SAFX226 ou SAFX232 das contas contábeis cujo campo <<IND_CONTA>> da tabela SAFX2002 estiver preenchido com “S”.

A opção <<Estabelecimentos>> da tela de parametrização é habilitado quando o usuário informa no campo <<ESTABELECIMENTO>> da tabela de geração a opção “TODOS”, definindo assim trazer os dados de todos os estabelecimentos daquela empresa, sendo assim é apresentada a seguinte definição para estes campos: Se a opção <<Discriminados>> estiver marcada os dados do relatório deverão estar separados por página informando o código e o nome do Estabelecimento no campo <<FILIAL>> no cabeçalho do Relatório; Se a opção <<Todos Consolidados> estiver marcado os dados serão trazidos todos juntos sem separação e no campo <<FILIAL>> no cabeçalho do Relatório será exibida a informação “Todos os Estabelecimentos”.







Exemplo:




Ordenação: CODIGO DE CONTA CONTABIL





---

| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-2712 | Eric Celestrino | Criação de tela para geração balancete funcional |
| MFS-3790 | Eric Celestrino | Inserção de parâmetro considerar saldos por centro de custo. |
| MFS-46761 | Alessandra Cristina Navatta | Disponibilizar o relatório também no módulo SPED Contábil |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | [Quem executará o evento. Ex.: Usuário do sistema]. |
| Pré- Condições | [Condições necessárias para execução. Ex.: Estabelecimento cadastrado] |
| Pós-Condições | [Resultado após executar caso de uso. Ex.: Informação armazenada no banco de dados] |


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
| Estabelecimento | Quadro de seleção de Estabs | S | S |  | Conter uma opção de todos os estabelecimentos e Todos os estabelecimentos da empresa que o usuário estiver acessado o módulo. | MFS-2712 |
| Período (data inicial) | Editbox | S | S | Formato: DD/MM/AAAA | Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Informe a Data Inicial”. | MFS-2712 |
| Período (data finall) | Editbox | S | S | Formato: DD/MM/AAAA | Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Informe a Data Final”.  A Data Final informada deve ser maior ou igual à Data Inicial. Caso seja menor, retornar mensagem: “Data Final deve ser maior ou igual à Data Inicial”. | MFS-2712 |
| Imprime Contas Zeradas | Checkbox | N | S | Default: não selecionado | Ao marcar essa opção o relatório deverá vir com as contas zeradas. | MFS-2712 |
| Saldo Antes do Encerramento | Checkbox | N | S | Default: não selecionado | Ao marcar este campo o Relatório exibirá a coluna de <<Saldo Antes do Encerramento>> no relatório. | MFS-2712 |
| Considerar Saldos por Centro de Custo (Saldos por Centro de Custo) | Checkbox | N | S | Default: não selecionado | Ao marcar este campo o Relatório exibirá a coluna de <<Centro de Custo >> no relatório. | MFS3790 |
| Conta Contábil Inicial | Pasta | S | S |  | Ao selecionar a pasta serão apresentados os códigos das contas contábeis conforme cadastro na SAFX2002.  Obs.: Caso não preenchido exibir a seguinte mensagem: “Conta Contábil Inicial deve ser preenchido”. | MFS-2712 |
| Conta Contábil Final | Pasta | S | S |  | Ao selecionar a pasta serão apresentados os códigos das contas contábeis conforme cadastro na SAFX2002.  Obs.: Caso não preenchido exibir a seguinte mensagem: “Conta Contábil Final deve ser preenchido”. | MFS-2712 |
| Tipo de Balancete   Analítico  Sintético | Radio Button | N | S |  | As opções Tipo de Balancete (analítico ou sintético) tem a seguinte regra: Quando o Analítico estiver marcado o Sintético estará desmarcado e vice e versa. | MFS-2712 |
| Estabelecimentos  Discriminados  Todos Consolidados | Radio Button | N | S |  | As opções Estabelecimentos (Discriminados ou Todos Consolidados) tem a seguinte regra: Quando a opção Discriminados estiver marcado o Todos Consolidados estará desmarcado e vice e versa. | MFS-2712 |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa: | Texto |  | Demonstrar a Razão Social da empresa que acessou o módulo. | MFS-2712 |
| Período: | Data | Formato:  Período: DD/MM/AAAA a DD/MM/AAAA | Demonstrar o período de geração parametrizado. | MFS-2712 |
| Data/Hora da Geração | Data e Hora | Formato: Data/Hora de Geração: DD/MM/AAAA - HH:MM:SS | Demonstrar a Data e Hora da emissão do relatório. | MFS-2712 |
| Página: | Texto |  | Demonstrar a paginação do relatório. | MFS-2712 |
| Filial: | Texto |  | Demonstrar a Razão Social do Estabelecimento Centralizador selecionado no momento da emissão do relatório, conforme informado no Cadastro do Estabelecimento. | MFS-2712 |
| CNPJ: | Texto | Formato: XX.XXX.XXX/XXXX-XX | Demonstrar o CNPJ do Estabelecimento Centralizador selecionado no momento da emissão do relatório, conforme informado no Cadastro do Estabelecimento. | MFS-2712 |
| Corpo do Relatório – Neste Tópico do relatório teremos as informações dispostas da seguinte maneira: | Corpo do Relatório – Neste Tópico do relatório teremos as informações dispostas da seguinte maneira: | Corpo do Relatório – Neste Tópico do relatório teremos as informações dispostas da seguinte maneira: | Corpo do Relatório – Neste Tópico do relatório teremos as informações dispostas da seguinte maneira: | Corpo do Relatório – Neste Tópico do relatório teremos as informações dispostas da seguinte maneira: |
| Conta Número | Texto |  | Demonstrar o Código da Conta Contábil (COD_CONTA) conforme informado na tabela de Saldo Contábil em Moeda Funcional (SAFX226) | MFS-2712 |
| Descrição | Texto |  | Demonstrar a descrição da conta contábil retirando do campo descrição da SAFX2002 | MFS-2712 |
| Centro de Custo | Texto |  | Demonstrar o Código do Centro de custo (COD_CUSTO) conforme informado na tabela de Saldo Contábil por Centro de Custo em Moeda Funcional (SAFX227). Este campo só deve ser demonstrado quando o parâmetro de considerar Saldos por centro de custo estiver marcado. | MFS-3790 |
| Saldo Anterior | Numérico | 0,00 | Demonstrar o saldo anterior buscando do campo VLR_SALDO_INI Concatenado com o campo IND_SALDO_INI da tabela SAFX226 | MFS-2712 |
| Débitos | Numérico | 0,00 | Demonstrar o valor do debito buscando do campo VLR_TOT_DEBITO da tabela SAFX226 | MFS-2712 |
| Créditos | Numérico | 0,00 | Demonstrar o valor do debito buscando do campo VLR_TOT_CREDITO da tabela SAFX226 | MFS-2712 |
| Saldo Atual | Numérico | 0,00 | Demonstrar o valor do saldo atual buscando o campo VLR_SALDO_FIM Concatenado com o campo IND_SALDO_FIM da tabela SAFX226 | MFS-2712 |
| Saldo Antes do Encerramento | Numérico | 0,00 | Este campo só será exibido no relatório se o usuário estiver marcando o campo <<Saldo antes do encerramento>> na tela de parametrização do relatório.  Para cada conta, buscar na SAFX225 - Lançamento Contábil em Moeda Funcional todos os lançamentos de encerramento que estiverem dentro do período de geração do balancete e que pertencerem à empresa e estabelecimento selecionados na tela de geração (podem existir vários lançamentos de encerramento para uma mesma conta porque o encerramento pode ser feito por centro de custo). Depois de recuperados os lançamentos, sumarizar os valores encontrados (total de créditos – total de débitos) e o resultado dessa sumarização é o valor a ser demonstrado no relatório para aquela conta. Além do valor, o balancete deve demonstrar também o indicador (débito ou crédito).  Obs.: Mesmo conceito utilizado no Balancete normal no momento, pois os dois precisam ficar padronizados. | MFS-2712 |
| Totalização – Neste item demonstrará totalizador dos campos de valores do relatório. | Totalização – Neste item demonstrará totalizador dos campos de valores do relatório. | Totalização – Neste item demonstrará totalizador dos campos de valores do relatório. | Totalização – Neste item demonstrará totalizador dos campos de valores do relatório. | Totalização – Neste item demonstrará totalizador dos campos de valores do relatório. |
| Saldo Anterior | Numérico | 0,00 | Conforme no exemplo esta informação terá duas linhas. A totalização do somatório do Saldo anterior distinto por indicador de débito ou crédito. Esta informação pode ser obtida Somando o campo VLR_SALDO_INI da tabela SAFX226 separando pelo campo IND_SALDO_INI | MFS-2712 |
| Débitos | Numérico | 0,00| | Valor do somatório da coluna Débitos do relatório. Este valor pode ser obtido somando o campo VLR_TOT_DEBITO da tabela SAFX226 | MFS-2712 |
| Créditos | Numérico | 0,00 | Valor do somatório da coluna Créditos do relatório. Este valor pode ser obtido somando o campo VLR_TOT_CREDITO da tabela SAFX226 | MFS-2712 |
| Saldo Atual | Numérico | 0,00 | Demonstrar o valor do somatório do saldo atual buscando o campo VLR_SALDO_FIM separando os resultados pelo campo IND_SALDO_FIM da tabela SAFX226 | MFS-2712 |
| Saldo Antes do Encerramento | Numérico | 0,00 | Este campo só será exibido no relatório se o usuário estiver marcado o campo <<Saldo antes do encerramento>> na tela de parametrização do relatório.   Demonstrar um somatório de todas as linhas que foram apuradas no processo abaixo:  Para cada conta, buscar na SAFX225 - Lançamento Contábil em Moeda Funcional todos os lançamentos de encerramento que estiverem dentro do período de geração do balancete e que pertencerem à empresa e estabelecimento selecionados na tela de geração (podem existir vários lançamentos de encerramento para uma mesma conta porque o encerramento pode ser feito por centro de custo). Depois de recuperados os lançamentos, sumarizar os valores encontrados (total de créditos – total de débitos) e o resultado dessa sumarização é o valor a ser demonstrado no relatório para aquela conta. Além do valor, o balancete deve demonstrar também o indicador (débito ou crédito).  Obs.: Mesmo conceito utilizado no Balancete normal no momento, pois os dois precisam ficar padronizados. | MFS-2712 |
