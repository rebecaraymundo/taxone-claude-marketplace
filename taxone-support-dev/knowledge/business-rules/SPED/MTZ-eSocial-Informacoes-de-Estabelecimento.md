# MTZ-eSocial-Informacoes-de-Estabelecimento

> Fonte: MTZ-eSocial-Informacoes-de-Estabelecimento.docx






THOMSON REUTERS

Módulo eSocial

Manutenção das Informações do Estabelecimento


Localização: Menu SPED, módulo Informações para o eSocial, menu Parâmetros  Informações do Estabelecimento




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3





Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.



















## Regras Gerais


A parametrização das informações do estabelecimento foi criada na MFS15509 (criação do módulo eSocial).

Estrutura da tabela:



OBS: O campo Alíquota Gilrat foi criado com decimais já prevendo alguma alteração futura. No entanto, as alíquotas atuais previstas na legislação trabalhista são apenas 1, 2 ou 3. Por isso teremos essa validação na manutenção deste campo.


Campos que compõe a chave da tabela:

- Código da Empresa
- Código do Estabelecimento
- Validade Inicial



## Layout da Tela






Botões da barra de menu:





## Regras de Funcionamento dos Campos










= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15509 | Criação do módulo eSocial | Criação da parametrização “Informações do Estabelecimento” do módulo eSocial.... | 18/12/2017 |
| MFS18065 | Atualização do eSocial p/ vrs 2.4.02 | Inclusão de nova opção na lista de valores do campo Tipo de Processo (somente para o processo relacionado ao FAP) | 05/06/2018 |
| MFS23883 | Atualização do eSocial p/ vrs 2.5 | Parametrização por Estabelecimento Centralizador e Centralizado | 01/02/2019 |
| MFS-88128 | Elisabete Costa | Alterações para versão S1.0. | 15/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Descrição | Tamanho | Tipo |
| --- | --- | --- |
| Código da Empresa | 003 | A |
| Código do Estabelecimento | 006 | A |
| Validade Inicial | 008 | Data (DDMMAAAA) |
| Validade Final | 008 | Data (DDMMAAAA) |
| Alíquota Gilrat | 9v9999 (ver OBS abaixo) | N |
| Indicador do Tipo de Processo (Gilrat) | 001 | A |
| Número do Processo (Gilrat) | 021 | A |
| Código do Indicativo da Suspensão (Gilrat) | 014 | A |
| FAP | 9v9999 | N |
| Indicador do Tipo de Processo (FAP) | 001 | A |
| Número do Processo (FAP) | 021 | A |
| Código do Indicativo da Suspensão (FAP) | 014 | A |
| Sistema de Controle de Ponto | 001 | A |
| Contratação de Aprendiz | 001 | A |
| Indicador do Tipo de Processo (Aprendiz) | 001 | A |
| Número do Processo (Aprendiz) | 021 | A |
| Contratação p/intermédio de entidade educativa/prática desportiva | 001 | A |
| CNPJ | 014 | A |
| Contratação de Pessoa com Deficiência | 001 | A |
| Indicador do Tipo de Processo (Aprendiz) | 001 | A |
| Número do Processo (Aprendiz) | 021 | A |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão do registro. |
| CONFIRMA | Opção para salvar as informações do registro incluído ou alterado. |
| RELATÓRIO | Esta opção permite imprimir os dados da tabela. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Listbox | Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário.   Serão disponibilizados para seleção apenas os estabelecimentos centralizadores e centralizados da parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais). | MFS23883 |
| Validade Inicial | Numérico | S | S | (MMAAAA) | Neste campo será informado o mês e ano de validade inicial da parametrização (deve ser um mês válido).  Como o campo na tabela é do tipo DATE, o conteúdo gravado será sempre a data referente ao primeiro dia do mês e ano informado. |  |
| Validade Final | Numérico | N | S | (MMAAAA) | Neste campo será informado o mês e ano de validade final da parametrização (deve ser um mês válido).  Como o campo na tabela é do tipo DATE, o conteúdo gravado será sempre a data referente ao último dia do mês e ano informado.  O mês/ano informado não pode ser inferior ao mês/ano da validade inicial. Caso contrário, será exibida a mensagem abaixo e a operação não será salva:  “A validade final deve ser maior ou igual à validade inicial” |  |
| Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: | Informações sobre a alíquota Gilrat: |
| Alíquota | Numérico | S | S |  | Neste campo será informada uma alíquota.   O número informado deve ser igual a um dos seguintes valores:   1,0000 2,0000 3,0000  Caso não atenda à condição, será exibida a mensagem abaixo e a operação não será salva:  “A Alíquota Gilrat deve ser igual a 1, 2 ou 3” |  |
| Processo (Tipo/Número) | Alfanumérico | N | S |  | O primeiro campo corresponde ao Tipo do Processo, que é uma lista com as opções abaixo + uma linha em branco:  1-Administrativo 2-Judicial   O campo ao lado é o número do processo, que trabalha com janela de seleção da Tabela de Cadastro de Processos Administrativos / Judiciais (SAFX2058).  Para seleção, serão disponibilizados apenas os processos do Tipo selecionado pelo usuário, e válidos em relação à data informada no campo “Validade Inicial”. Assim, o processo deve atender as seguintes condições:  -Grupo –Grupo de maior data de validade existente, que seja   <= a data Validade Inicial informada, para o qual o   estabelecimento esteja vinculado;  - Validade inicial <= data Validade Inicial informada; - Validade final nula ou > = data da Validade Inicial Informada;  - Tipo do Processo – apenas os processos do tipo escolhido;  Caso o número do processo seja digitado, será verificada a sua existência na tabela SAFX2058, considerando os critérios descritos acima. Caso não exista, será exibida mensagem de erro padrão e a operação não será salva.   Obs: A informação deste processo é obrigatória quando a alíquota Gilrat informada for diferente da alíquota definida pela legislação para o CNAE do estabelecimento. No entanto, esta obrigatoriedade não será criticada, será apenas descrita no help deste campo. |  |
| Cód. Indicativo da Suspensão |  | N | S |  | Este campo trabalha com janela de seleção da Tabela de Informações de Suspensão de Exigibilidade de Tributos (SAFX2059).  Para seleção, serão disponibilizados apenas os códigos da SAFX2059 que sejam “filhos” do processo informado no campo “Processo Gilrat”.  Caso o código seja digitado, será validada a sua existência na SAFX2059, considerando as condições descritas acima. Se o código não existir, será exibida mensagem de erro padrão e a operação não será salva. |  |
| Informações sobre o FAP: | Informações sobre o FAP: | Informações sobre o FAP: | Informações sobre o FAP: | Informações sobre o FAP: | Informações sobre o FAP: | Informações sobre o FAP: |
| Fator Acidentário de Prevenção (FAP) |  | S | S |  | Neste campo será informado o fator acidentário de prevenção.   O número informado deve atender as seguintes condições:  - Deve ser >= 0,5000; - Deve ser <= a 2,0000;  Caso não atenda à condição, será exibida a mensagem abaixo e a operação não será salva: “O FAP deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000” |  |
| Processo (Tipo/Número) | Alfanumérico | N | S |  | O primeiro campo corresponde ao Tipo do Processo, que é uma lista com as opções abaixo + uma linha em branco:  1-Administrativo 2-Judicial 4-Processo FAP MFS18065: Inclusão do tipo de processo = 4 (Processo FAP). Este tipo de processo será utilizado apenas p/o processo do quadro “Informações sobre o FAP”. Demais processos desta tela não trabalham com o tipo = 4.   O campo ao lado é o número do processo, que trabalha com janela de seleção da Tabela de Cadastro de Processos Administrativos / Judiciais (SAFX2058).  Para seleção, serão disponibilizados apenas os processos do Tipo selecionado pelo usuário, e válidos em relação à data informada no campo “Validade Inicial”. Assim, o processo deve atender as seguintes condições:  -Grupo –Grupo de maior data de validade existente, que seja   <= a data Validade Inicial informada, para o qual o   estabelecimento esteja vinculado; - Validade inicial <= data Validade Inicial informada; - Validade final nula ou > = data da Validade Inicial Informada; - Tipo do Processo – apenas os processos do tipo escolhido;  Caso o número do processo seja digitado, será verificada a sua existência na tabela SAFX2058, considerando os critérios descritos acima. Caso não exista, será exibida mensagem de erro padrão e a operação não será salva.   Obs: A informação deste processo é obrigatória quando o FAP informado for diferente do FAP definido pela legislação para o CNAE do estabelecimento. No entanto, esta obrigatoriedade não será criticada, será apenas descrita no help deste campo. |  |
| Cód. Indicativo da Suspensão |  | N | S |  | Este campo trabalha com janela de seleção da Tabela de Informações de Suspensão de Exigibilidade de Tributos (SAFX2059).  Para seleção, serão disponibilizados apenas os códigos da SAFX2059 que sejam “filhos” do processo informado no campo “Processo Gilrat”.  Caso o código seja digitado, será validada a sua existência na SAFX2059, considerando as condições descritas acima. Se o código não existir, será exibida mensagem de erro padrão e a operação não será salva. |  |
| Sistema de Controle de Ponto |  | S | N | Listbox | Este campo é uma lista com as seguintes opções: 0 - Não utiliza;  1 - Manual; 2 - Mecânico;  3 - Eletrônico (Portaria MTE 1.510/2009); 4 - Não eletrônico alternativo (art. 1° da Portaria TEM      373/2011); 5 - Eletrônico alternativo (art. 2° da Portaria MTE 373/2011);  6 - Eletrônico - outros. |  |
| Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: | Informações sobre contratação de aprendiz: |
| Contratação |  | N | N | Listbox | Este campo é uma lista com as seguintes opções:  0 - Dispensado de acordo com a lei; 1 - Dispensado, mesmo que parcialmente, em virtude de      processo judicial;  2 - Obrigado.   O campo deixa de ser obrigatório pois o mesmo foi removido a partir da versão S1.0. | MFS-58405 |
| Processo (Tipo/Número) | Alfanumérico | N | S |  | O primeiro campo corresponde ao Tipo do Processo, que é uma lista com as opções abaixo + uma linha em branco:  1-Administrativo 2-Judicial   O campo ao lado é o número do processo, que trabalha com janela de seleção da Tabela de Cadastro de Processos Administrativos / Judiciais (SAFX2058).  Para seleção, serão disponibilizados apenas os processos do Tipo selecionado pelo usuário, e válidos em relação à data informada no campo “Validade Inicial”. Assim, o processo deve atender as seguintes condições:  -Grupo –Grupo de maior data de validade existente, que seja   <= a data Validade Inicial informada, para o qual o   estabelecimento esteja vinculado; - Validade inicial <= data Validade Inicial informada; - Validade final nula ou > = data da Validade Inicial Informada; - Tipo do Processo – apenas os processos do tipo escolhido;  Caso o número do processo seja digitado, será verificada a sua existência na tabela SAFX2058, considerando os critérios descritos acima. Caso não exista, será exibida mensagem de erro padrão e a operação não será salva.   Crítica de obrigatoriedade:   Ao salvar a operação será feita a seguinte validação:  A informação deste tipo de processo é obrigatória quando o campo “Contratação de Aprendiz” for = “1”.   Nesse caso, se o processo deste campo não for informado, será exibida a mensagem abaixo e a operação não será salva:  “Quando o campo Contratação de Aprendiz for = 1, é obrigatório informar um processo” |  |
| Contratação p/intermédio de entidade educativa/prática desportiva |  | N | N | Checkbox | Campo do tipo S/N onde o usuário indica se a contratação do aprendiz é feita por intermédio de alguma entidade.  Se marcado  será gravado o conteúdo “S”;  Se desmarcado  será gravado o conteúdo “N”;  O campo deixa de ser obrigatório pois o mesmo foi removido a partir da versão S1.0. | MFS-58405 |
| CNPJ |  | N | S |  | Neste campo poderá ser informado o CNPJ da entidade educativa / prática desportiva, quando for o caso.  Quando informado, deve ser um CNPJ válido.   A informação do CNPJ será obrigatória caso o campo “Contratação p/intermédio de entidade educativa/prática desportiva” seja selecionado. Neste caso, se o CNPJ da entidade não for informado, será exibida a mensagem abaixo e a operação não será salva:  “Informar o CNPJ da entidade educativa/prática desportiva” |  |
| Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: | Informações sobre contratação de pessoa com deficiência: |
| Contratação |  | N | N | Listbox | Este campo é uma lista com as opções abaixo + uma linha em branco:  0 - Dispensado de acordo com a lei;  1 - Dispensado, mesmo que parcialmente, em virtude de      processo judicial; 2 - Com exigibilidade suspensa, mesmo que       parcialmente em virtude de Termo de Compromisso       firmado com o Ministério do Trabalho;  9 - Obrigado. |  |
| Processo (Tipo/Número) | Alfanumérico | N | S |  | O primeiro campo corresponde ao Tipo do Processo, que é uma lista com as opções abaixo + uma linha em branco:  1-Administrativo 2-Judicial   O campo ao lado é o número do processo, que trabalha com janela de seleção da Tabela de Cadastro de Processos Administrativos / Judiciais (SAFX2058).  Para seleção, serão disponibilizados apenas os processos do Tipo selecionado pelo usuário, e válidos em relação à data informada no campo “Validade Inicial”. Assim, o processo deve atender as seguintes condições:  -Grupo –Grupo de maior data de validade existente, que seja   <= a data Validade Inicial informada, para o qual o   estabelecimento esteja vinculado; - Validade inicial <= data Validade Inicial informada; - Validade final nula ou > = data da Validade Inicial Informada; - Tipo do Processo – apenas os processos do tipo escolhido;  Caso o número do processo seja digitado, será verificada a sua existência na tabela SAFX2058, considerando os critérios descritos acima. Caso não exista, será exibida mensagem de erro padrão e a operação não será salva.   Crítica de obrigatoriedade:   Ao salvar a operação será feita a seguinte validação:  A informação deste tipo de processo é obrigatória quando o campo “Contratação de Pessoa com Deficiência” for = “1”.   Nesse caso, se o processo deste campo não for informado, será exibida a mensagem abaixo e a operação não será salva:  “Quando o campo Contratação de Pessoa c/Deficiência for = 1, é obrigatório informar um processo” |  |
