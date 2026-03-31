# MTZ-eSocial-Geracao-Evento-S1020-Lotacoes

> Fonte: MTZ-eSocial-Geracao-Evento-S1020-Lotacoes.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1020 - Lotações


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Cadastros



DOCUMENTO DE REQUISITO




Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	3
4.	Gravação dos Dados	5




Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.















## Parâmetros da Tela



Este documento é específico das regras de geração do evento S-1020.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Cadastros”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento



Origem dos dados: - SAFX2037 - Tabela de Cadastro dos Setores
- Parametrização “Dados Iniciais” do Módulo eSocial
- Parametrização “Informações dos Setores do Estabelecimento” do Módulo eSocial


Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos dados da SAFX2037:
- Grupo do Setor (SAFX2037) -  Considerar o Grupo de > data de validade que seja <= a data inicial do período informado em tela, para a qual a SAFX2037 esteja associada;


- Data de Validade Inicial do Setor SAFX2037 – Apenas os setores cuja data de validade inicial se enquadre no período informado em tela;

[MFS25900]
Critério de recuperação da Parametrização “Informações dos Setores do Estabelecimento”:
Caso o estabelecimento selecionado para geração possua parametrização de “Informações dos Setores do Estabelecimento” então:
Recuperar apenas os Setores parametrizados para o Estabelecimento (tabela ESOCIAL_PAR_SETOR_ESTAB).
Considerar os critérios:
- Estabelecimento (ESOCIAL_PAR_SETOR_ESTAB)    = estabelecimento selecionado na tela da geração;
- Grupo do Setor (ESOCIAL_PAR_SETOR_ESTAB)      = Grupo do Setor (SAFX2037);
- Código do Setor (ESOCIAL_PAR_SETOR_ESTAB)    = Código do Setor (SAFX2037);
- Validade do Setor (ESOCIAL_PAR_SETOR_ESTAB) = Validade do Setor (SAFX2037);


## Verificação do Status de Eventos já Gerados


MFS16751: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1020_OC, coluna IND_STATUS).

Para cada lotação recuperada, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para a mesma data de validade.

Caso não:

O evento da lotação será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:

A geração de um novo evento para a lotação dependerá do status do evento já existente, da seguinte forma:

[MFS21383]


Se o status do evento já existente não permitir regeração:
Nesse caso a lotação em questão será desconsiderada da geração, e será gravada a seguinte mensagem de aviso no log:
Aviso: Já existe evento anterior gerado para a lotação. O status do evento não permite uma nova geração.
Dados do Registro:  Código do Setor: XXXXXXX, Validade Inicial: XX/XXXX

Se o status do evento já existente permitir regeração:

Se status = ‘1-Aguardando geração XML’, ‘4-Erro geração XML’, ‘6-Evento rejeitado pela mensageria’ (***), ‘10-Rejeitado pelo Fisco’ (***), ‘14-Evento excluído na mensageria’ ou ‘15-Erro técnico na mensageria’:
Nesse caso o setor em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente;

Se status = ‘8-Recebido pelo Fisco com sucesso’ (***) ou ‘9-Recebido pelo Fisco com advertência’ (***):
Nesse caso o setor em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações de setor ou exclusão das informações de setor, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão. Se não houver alteração ou exclusão não será permitida a regeração;

Se status = ‘12-Evento Excluído’ (***):
Nesse caso o setor em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

*** Importante: Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:


Para os demais Status serão descartados e substituídos pelos novos eventos regerados.




(***) Os status 8 e 9 (Recebido pelo Fisco com Sucesso ou Advertência) permitem a regeração de um evento de cadastro no caso de uma alteração ou exclusão do cadastro. No entanto, este cenário ainda não será tratado no eSocial, uma vez que ainda não foi implementado o controle das alterações (manutenção e importação dos cadastros).


## Gravação dos Dados


Para cada setor recuperado, será gerado um evento S-1020 com as seguintes informações:


Registro evtTabLotação – Evento tabela de Lotações.



Registro ideEvento - Informações de Identificação do evento.



Registro ideEmpregador - Informações de identificação do empregador.



[MFS21383]
Registro ideLotacao - Informações de identificação da lotação (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “I”.




Registro dadosLotacao - Detalhamento das informações da lotação (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “I”.




Registro fpasLotacao – Informações do FPAS e Terceiros (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “I”.



Registro procJudTerceiro – Informações de processo sobre as contribuições destinadas a outras Entidades e Fundos (Terceiros). (Inclusão)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

A verificação será feita pelo preenchimento do campo “12-Código Terceiros – Processo”, ou seja, sempre que este campo estiver preenchido na SAFX2037, o registro procJudTerceiro será gerado.

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “I”.



Registro dadosOpPort – Informações do operador portuário. (Inclusão)

Caso não exista a informação, este registro não será gerado.

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “I”.




Registro ideLotacao - Informações de identificação da lotação (Alteração)

Critérios: Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “A”.

Se houve o primeiro envio do evento S1020 com sucesso ou advertência e após for identificado qualquer alteração nas informações do cadastro dos setores será a condição para o registro ser gerado.



Registro dadosLotacao - Detalhamento das informações da lotação (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “A”.





Registro fpasLotacao – Informações do FPAS e Terceiros (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “A”.



Registro procJudTerceiro – Informações de processo sobre as contribuições destinadas a outras Entidades e Fundos (Terceiros). (Alteração)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

A verificação será feita pelo preenchimento do campo “12-Código Terceiros – Processo”, ou seja, sempre que este campo estiver preenchido na SAFX2037, o registro procJudTerceiro será gerado.

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “A”.




Registro dadosOpPort – Informações do operador portuário. (Alteração)

Caso não exista a informação, este registro não será gerado.

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “A”.




Registro novaValidade - Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento. (Alteração)

Critério: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração no cadastro dos setores quanto à data início e/ou fim validade, este será considerado como um novo cadastro dos setores, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.




Registro ideLotacao - Informações de identificação da lotação (Exclusão)

Critérios: Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1020_OC campo “IND_OPER” igual a “E”.

Se houve o primeiro envio do evento S1020 com sucesso ou advertência e após for identificado a exclusão das informações do cadastro dos setores será a condição para o registro ser gerado.




= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15869 | Geração do evento das Lotações (S-1020) | Geração dos dados do evento das Lotações (S-1020). | 08/01/2018  (criação do documento) |
| MFS16751 | Controle dos Status x Regeração | Críticas em relação a regeração dos eventos. | 28/03/2018 |
| MFS21383 | Lara Aline | Inclusão da rotina de geração de Alteração e Exclusão. | 08/10/2018 |
| MFS25900 | Liliane Assaf | Criação da parametrização de setores relacionados aos Estabelecimentos Centralizadores. | 15/04/2019 |
| MFS-88130 | Elisabete Costa | Alterações para versão S1.0. | 21/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Status | Permite regeração dos dados |
| --- | --- |
| 1-Aguardando geração XML | Sim |
| 3-Enviando para mensageria | Não |
| 4-Erro geração XML | Sim |
| 5-Evento recebido pela mensageria | Não |
| 6-Evento rejeitado pela mensageria | Sim |
| 7-Em Processamento (mensageria) | Não |
| 8-Recebido pelo Fisco com sucesso | Sim (Alteração/Exclusão) |
| 9-Recebido pelo Fisco com advertência | Sim (Alteração/Exclusão) |
| 10-Rejeitado pelo Fisco | Sim |
| 12-Evento Excluído | Sim |
| 14-Evento excluído na mensageria | Sim |
| 15-Erro técnico na mensageria | Sim |


| 6-Evento rejeitado pela mensageria |
| --- |
| 8-Recebido pelo Fisco com sucesso |
| 9-Recebido pelo Fisco com advertência |
| 10-Rejeitado pelo Fisco |
| 12-Evento Excluído |


| Sobre a limpeza do evento já existente: Se o status do evento já existente for = 1 (Aguardando geração XML), 4 (Erro geração XML) ou 14 (Evento excluído na mensageria), este evento será apagado ao efetuar a regeração de um novo evento. Nos demais casos, a limpeza do evento já existente não será feita (para manter o histórico dos erros ocorridos), e será feita apenas a regeração de um novo evento. |
| --- |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:  “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita; Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do empregador) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”.   Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita; |


| codLotacao | Campo 01-Código do Setor |
| --- | --- |
| iniValid | Mês a ano da data de validade inicial do Setor (campo 02-Data Inico/Inclusão/Alteração) |
| fimValid | Mês a ano da data de validade final do Setor (campo 05-Data de Validade FinaI) Se a validade final não estiver preenchida, este campo não será gerado. |


| tpLotacao | Campo 06-Tipo de Lotação Tributária  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Tipo de Lotação Tributária (tpLotacao) é de preenchimento obrigatório e não foi informado Origem: Campo “06-Tipo de Lotação Tributária” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| --- | --- |
| tpInsc | Campo 07-Tipo de Inscrição da Lotação  Caso este campo não esteja preenchido na SAFX2037 e o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Tipo de Inscrição (tpInscr) é de preenchimento obrigatório e não foi informado Origem: Campo “07-Tipo de Inscrição da Lotação” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| nrInsc | Campo 08-Número de Inscrição da Lotação  Caso este campo não esteja preenchido na SAFX2037 e o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Número de Inscrição (tpInscr) é de preenchimento obrigatório e não foi informado Origem: Campo “08-Número de Inscrição da Lotação” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |


| fpas | Campo 09-Código FPAS  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código FPAS (fpas) é de preenchimento obrigatório e não foi informado Origem: Campo “09-Código FPAS” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| --- | --- |
| codTercs | Campo 10-Código Terceiros  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código de Terceiros (codTercs) é de preenchimento obrigatório e não foi informado Origem: Campo “10-Código Terceiros” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| codTercsSusp | Campo 11-Código Combinado de Terceiros (Recolhimento Suspenso) |


| codTerc | Campo 12-Código Terceiros – Processo |
| --- | --- |
| nrProcJud | Campo 14-Número do Processo  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Número de Processo Judicial (nrProcJud) é de preenchimento obrigatório e não foi informado Origem: Campo “14-Número do Processo” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| codSusp | Campo 15-Código do Indicativo da Suspensão  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código do Indicativo da Suspensão (codSusp) é de preenchimento obrigatório e não foi informado Origem: Campo “15-Código do Indicativo da Suspensão” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |


| aliqRat  MFS-88130:VrsS-1.0 | Campo 16-Alíquota RAT  A partir da versão S1.0, os valores válidos são:  1, 2, 3.   Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos {aliqRat} e {fap} com os valores correspondentes. |
| --- | --- |
| Fap  MFS-88130:VrsS-1.0 | Campo 17-Fator Acidentário de Prevenção  A partir da versão S-1.0  Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos {aliqRat} e {fap} com os valores correspondentes. |


| codLotacao | Campo 01-Código do Setor |
| --- | --- |
| iniValid | Mês a ano da data de validade inicial do Setor (campo 02-Data Início/Inclusão/Alteração)  Obs: A informação recuperada do campo data de validade inicial do setor será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |
| fimValid | Mês a ano da data de validade final do Setor (campo 05-Data de Validade FinaI) Se a validade final não estiver preenchida, este campo não será gerado.  Obs: A informação recuperada do campo data de validade final do setor será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |


| tpLotacao | Campo 06-Tipo de Lotação Tributária  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Tipo de Lotação Tributária (tpLotacao) é de preenchimento obrigatório e não foi informado Origem: Campo “06-Tipo de Lotação Tributária” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| --- | --- |
| tpInsc | Campo 07-Tipo de Inscrição da Lotação  Caso este campo não esteja preenchido na SAFX2037 e o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Tipo de Inscrição (tpInscr) é de preenchimento obrigatório e não foi informado Origem: Campo “07-Tipo de Inscrição da Lotação” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| nrInsc | Campo 08-Número de Inscrição da Lotação  Caso este campo não esteja preenchido na SAFX2037 e o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Número de Inscrição (tpInscr) é de preenchimento obrigatório e não foi informado Origem: Campo “08-Número de Inscrição da Lotação” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |


| fpas | Campo 09-Código FPAS  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código FPAS (fpas) é de preenchimento obrigatório e não foi informado Origem: Campo “09-Código FPAS” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| --- | --- |
| codTercs | Campo 10-Código Terceiros  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código de Terceiros (codTercs) é de preenchimento obrigatório e não foi informado Origem: Campo “10-Código Terceiros” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| codTercsSusp | Campo 11-Código Combinado de Terceiros (Recolhimento Suspenso) |


| codTerc | Campo 12-Código Terceiros – Processo |
| --- | --- |
| nrProcJud | Campo 14-Número do Processo  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Número de Processo Judicial (nrProcJud) é de preenchimento obrigatório e não foi informado Origem: Campo “14-Número do Processo” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |
| codSusp | Campo 15-Código do Indicativo da Suspensão  Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código do Indicativo da Suspensão (codSusp) é de preenchimento obrigatório e não foi informado Origem: Campo “15-Código do Indicativo da Suspensão” da Tabela de Setores (SAFX2037) Dados do Registro: Código do Setor: XXXXXXXXXX |


| aliqRat  MFS-88130:VrsS-1.0 | Campo 16-Alíquota RAT  A partir da versão S1.0, os valores válidos são:  1, 2, 3.   Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos {aliqRat} e {fap} com os valores correspondentes. |
| --- | --- |
| Fap MFS-88130:VrsS-1.0 | Campo 17-Fator Acidentário de Prevenção A partir da versão S-1.0:  Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos {aliqRat} e {fap} com os valores correspondentes. |


| iniValid | Campo “Validade Inicial” da parametrização “Cadastro dos Setores” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| fimValid | Campo “Validade Final” da parametrização “Cadastro dos Setores” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |


| codLotacao | Campo 01-Código do Setor |
| --- | --- |
| iniValid | Mês a ano da data de validade inicial do Setor (campo 02-Data Inico/Inclusão/Alteração) |
| fimValid | Mês a ano da data de validade final do Setor (campo 05-Data de Validade FinaI) Se a validade final não estiver preenchida, este campo não será gerado. |
