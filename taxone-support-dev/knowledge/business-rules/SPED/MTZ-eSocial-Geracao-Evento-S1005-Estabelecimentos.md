# MTZ-eSocial-Geracao-Evento-S1005-Estabelecimentos

> Fonte: MTZ-eSocial-Geracao-Evento-S1005-Estabelecimentos.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1005 - Estabelecimento


Localização  Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Cadastros


DOCUMENTO DE REQUISITO




Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	3
4.	Gravação dos Dados	5




Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.
















## Parâmetros da Tela


Este documento é específico das regras de geração do evento S-1005.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Cadastros”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento



Origem dos dados: - Tabela dos Estabelecimentos
- Parametrização “Dados Iniciais” do Módulo eSocial
- Parametrização “Informações do Estabelecimento” do Módulo eSocial


Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;


Critérios para a recuperação dos dados da parametrização “Informações do Estabelecimento”:

Esta parametrização é por estabelecimento centralizador e centralizado, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;
- Validade inicial – Deve ser a > data de validade inicial cujo mês e ano seja <= ao mês e ano inicial do período informado em tela;


Caso o estabelecimento em questão não tenha dados parametrizados na parametrização “Informações do Estabelecimento”, será gerada a mensagem abaixo no log de erros e este estabelecimento não será processado.

“Não foi identificada parametrização válida (Informações do Estabelecimento) para o estabelecimento XXXXXX no período informado. Este estabelecimento não foi processado”

(“XXXXXX” é o código do estabelecimento)



## Verificação do Status de Eventos já Gerados


MFS-16751: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1005_OC, coluna IND_STATUS).

Será verificado se já existe um evento gerado para o estabelecimento em questão (estabelecimento a ser gerado), para a mesma data de validade.

Caso não:

O evento do estabelecimento será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:

A geração de um novo evento para o estabelecimento dependerá do status do evento já existente, da seguinte forma:

[MFS-16757]


Se o status do evento já existente não permitir regeração:
Nesse caso o estabelecimento em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso
no log:
Aviso: Já existe evento anterior gerado para o estabelecimento. O status do evento não permite uma nova geração.
Dados do Registro:  Estabelecimento: XXXXX - XXXXXXXX XXXXXXXXXXXXXXXXXXXX, Validade Inicial: XX/XXXX

Se o status do evento já existente permitir regeração:

Se status = ‘1-Aguardando geração XML’, ‘4-Erro geração XML’, ‘6-Evento rejeitado pela mensageria’ (***), ‘10-Rejeitado pelo Fisco’ (***), ‘14-Evento excluído na mensageria’ ou ‘15-Erro técnico na mensageria’:
Nesse caso o estabelecimento em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente;

Se status = ‘8-Recebido pelo Fisco com sucesso’ (***) ou ‘9-Recebido pelo Fisco com advertência’ (***):
Nesse caso o estabelecimento em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações do estabelecimento ou exclusão das informações do estabelecimento, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão. Se não houver alteração ou exclusão não será permitida a regeração;

Se status = ‘12-Evento Excluído’ (***):
Nesse caso o estabelecimento em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

*** Importante: Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:


Para os demais Status serão descartados e substituídos pelos novos eventos regerados.




## Gravação dos Dados


Para cada estabelecimento centralizador selecionado na tela da geração dos dados, será gerado um único evento S-1005 com as seguintes informações:

Registro evtTabEstab – Evento tabela de Estabelecimentos.



Registro ideEvento - Informações de Identificação do evento.



Registro ideEmpregador - Informações de identificação do empregador.


[MFS-16757]
Registro ideEstab - Informações de identificação do estabelecimento (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.



Registro dadosEstab - Detalhamento das informações do estabelecimento (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.




Registro aliqGilrat - Informações sobre a alíquota RAT e o FAP  (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.



Registro procAdmJudRat - Informações de processo sobre a alíquota RAT   (Inclusão)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo do tipo de processo da alíquota Gilrat)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.




Registro procAdmJudFap – Informações de processo sobre o FAP   (Inclusão)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo do tipo de processo do FAP)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.



Registro infoTrab - Informações trabalhistas sobre o estabelecimento  (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.




Registro infoApr – Informações sobre contratação de aprendiz   (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.



Registro infoEntEduc – Identificação de entidade educativa / prática desportiva   (Inclusão)

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.




Registro infoPCD – Informações sobre contratação de pessoas com deficiência   (Inclusão)

Este registro será gerado apenas se as condições a seguir forem verdadeiras:

- Quando se tratar do estabelecimento matriz, ou seja, quando o estabelecimento da geração tiver o campo “Matriz/Filial” = Matriz;
- Quando o campo “Contratação” (quadro “Informações sobre contratação de pessoa com deficiência”) estiver preenchido;

Regra de Seleção: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “I”.



Registro ideEstab - Informações de identificação do estabelecimento (Alteração)

Critérios: Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.

Se houve o primeiro envio do evento S1005 com sucesso ou advertência e após for identificado qualquer alteração nas informações de cadastro do estabelecimento será a condição para o registro ser gerado.






Registro dadosEstab - Detalhamento das informações do estabelecimento (Alteração)


Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.





Registro aliqGilrat - Informações sobre a alíquota RAT e o FAP (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.





Registro procAdmJudRat - Informações de processo sobre a alíquota RAT    (Alteração)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo do tipo de processo da alíquota Gilrat)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.




Registro procAdmJudFap – Informações de processo sobre o FAP    (Alteração)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo do tipo de processo do FAP)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.




Registro infoTrab - Informações trabalhistas sobre o estabelecimento     (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.



Registro infoApr – Informações sobre contratação de aprendiz   (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.



Registro infoEntEduc – Identificação de entidade educativa / prática desportiva   (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.



Registro infoPCD – Informações sobre contratação de pessoas com deficiência   (Alteração)

Este registro será gerado apenas se as condições a seguir forem verdadeiras:

- Quando se tratar do estabelecimento matriz, ou seja, quando o estabelecimento da geração tiver o campo “Matriz/Filial” = Matriz;

- Quando o campo “Contratação” (quadro “Informações sobre contratação de pessoa com deficiência”) estiver preenchido;

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “A”.


Registro novaValidade - Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento.

Critério: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.



Registro ideEstab - Informações de identificação do estabelecimento (Exclusão)

Critérios: Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1005_OC campo “IND_OPER” igual a “E”.

Se houve o primeiro envio do evento S1005 com sucesso ou advertência e após for identificado a exclusão das informações de cadastro do estabelecimento será a condição para o registro ser gerado.



= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15509 | Vânia Mattos | Geração do evento S-1005 - Cadastro do Estabelecimento | 14/12/2017  (criação do documento) |
| MFS16751 | Vânia Mattos | Críticas em relação a regeração dos eventos. | 28/03/2018 |
| MFS16757 | Lara Aline | Inclusão da rotina de geração de Alteração e Exclusão. | 16/08/2018 |
| MFS23883 | Eduardo Vieira Cruz | Parametrização “Informações do Estabelecimento” por centralizador e centralizado | 01/02/2019 |
| MFS-88128 | Elisabete Costa | Alterações para versão S1.0 | 14/06/2022 |
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


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:  “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ do estabelecimento – 8 primeiras posições do CNPJ, completando com zeros à direita;  Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do empregador) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”.   Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as  8 primeiras posições do CNPJ, completando com zeros à direita; |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento (neste caso, deve ser o CNPJ completo, com as 14 posições); |
| iniValid | Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização) |
| fimValid | Campo “Validade Final” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |


| cnaePrep | CNAE do estabelecimento centralizador da geração (campo “Atividade Econômica” do cadastro do estabelecimento) |
| --- | --- |
| cnpjResp | CNPJ responsável pela inscrição no cadastro de obras da RFB. A partir da versão S1.0 foi criado o campo cnpjResp. O mesmo não deve ser gerado, pois o campo tpInsc possui o conteúdo fixo=’1’ e de acordo com o layout o campo cnpjResp deve ser igual a '4' (CNO-Cadastro Nacional de Obras) |


| aliqRat | Campo “Alíquota” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento;  Obs: No layout do eSocial está alíquota é um campo numérico de apenas 1 posição. Mas na tabela da parametrização o campo foi criado com 4 casas decimais apenas por precaução, caso no futuro as alíquotas passem a utilizar decimais. |
| --- | --- |
| fap | Campo “Fator Acidentário de Prevenção (FAP)” da parametrização das informações do estabelecimento; |
| aliqRatAjust MFS-88128:VrsS-1.0 | Resultado da multiplicação: aliqRat x fap;   Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |


| tpProc | Tipo do processo do campo “Processo” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento ; |
| --- | --- |
| nrProc | Número do processo do campo “Processo” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento; |
| codSusp | Código do Indicativo da Suspensão (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento; |


| tpProc | Tipo do processo do campo “Processo” (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |
| --- | --- |
| nrProc | Número do processo do campo “Processo” (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |
| codSusp | Código do Indicativo da Suspensão (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |


| regPt  MFS-88128:VrsS-1.0 | Opção do campo “Sistema de Controle de Ponto”, da parametrização das informações do estabelecimento;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |


| contApr  MFS-88128:VrsS-1.0 | Opção do campo “Contratação” (quadro “Informações sobre contratação de aprendiz”), da parametrização das informações do estabelecimento;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |
| nrProcJud | Número do processo do campo “Processo” (quadro “Informações sobre contratação de aprendiz”) da parametrização das informações do estabelecimento. Caso este número de processo não esteja preenchido, este campo não será gerado. |
| contEntEd  MFS-88128:VrsS-1.0 | Se o conteúdo do campo “Contratação”  = “1” ou “2”,  Será gravado o conteúdo do campo “Contratação p/intermédio de entidade educativa/prática desportiva” (S/N), da       parametrização das informações do estabelecimento;  Senão (conteúdo = “0”)      Este campo não será gerado;   Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |


| nrInsc | Campo “CNPJ” (quadro “Informações sobre contratação de aprendiz”) da parametrização das informações do estabelecimento.  Caso o CNPJ não esteja preenchido, este campo não será gerado. |
| --- | --- |


| contPCD  MFS-88128:VrsS-1.0 | Opção do campo “Contratação” (quadro “Informações sobre contratação de pessoa com deficiência”), da parametrização das informações do estabelecimento; Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |
| nrProcJud | Número do processo do campo “Processo” (quadro “Informações sobre contratação de pessoa com deficiência”) da parametrização das informações do estabelecimento. Caso este número de processo não esteja preenchido, este campo não será gerado. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento (neste caso, deve ser o CNPJ completo, com as 14 posições); |
| iniValid | Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização)  Obs: A informação recuperada do campo “Validade Inicial” da parametrização “Informações do Estabelecimento” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |
| fimValid | Campo “Validade Final” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado.  Obs: A informação recuperada do campo “Validade Final” da parametrização “Informações do Estabelecimento” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |


| cnaePrep | CNAE do estabelecimento centralizador da geração (campo “Atividade Econômica” do cadastro do estabelecimento) |
| --- | --- |
| cnpjResp MFS-88128:VrsS-1.0 | CNPJ responsável pela inscrição no cadastro de obras da RFB. A partir da versão S1.0 foi criado o campo cnpjResp. O mesmo não deve ser gerado, pois o campo tpInsc possui o conteúdo fixo=’1’ e de acordo com o layout o campo cnpjResp deve ser igual a '4' (CNO-Cadastro Nacional de Obras) |


| aliqRat | Campo “Alíquota” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento;  Obs: No layout do eSocial está alíquota é um campo numérico de apenas 1 posição. Mas na tabela da parametrização o campo foi criado com 4 casas decimais apenas por precaução, caso no futuro as alíquotas passem a utilizar decimais. |
| --- | --- |
| fap | Campo “Fator Acidentário de Prevenção (FAP)” da parametrização das informações do estabelecimento; |
| aliqRatAjuste  MFS-88128:VrsS-1.0 | Resultado da multiplicação: aliqRat x fap;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |


| tpProc | Tipo do processo do campo “Processo” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento ; |
| --- | --- |
| nrProc | Número do processo do campo “Processo” (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento; |
| codSusp | Código do Indicativo da Suspensão (quadro “Informações sobre a alíquota Gilrat”) da parametrização das informações do estabelecimento; |


| tpProc | Tipo do processo do campo “Processo” (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |
| --- | --- |
| nrProc | Número do processo do campo “Processo” (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |
| codSusp | Código do Indicativo da Suspensão (quadro “Informações sobre o FAP”) da parametrização das informações do estabelecimento; |


| regPt  MFS-88128:VrsS-1.0 | Opção do campo “Sistema de Controle de Ponto”, da parametrização das informações do estabelecimento;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |


| contApr  MFS-88128:VrsS-1.0 | Opção do campo “Contratação” (quadro “Informações sobre contratação de aprendiz”), da parametrização das informações do estabelecimento; Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |
| nrProcJud | Número do processo do campo “Processo” (quadro “Informações sobre contratação de aprendiz”) da parametrização das informações do estabelecimento. Caso este número de processo não esteja preenchido, este campo não será gerado. |
| contEntEd  MFS-88128:VrsS-1.0 | Se o conteúdo do campo “Contratação”  = “1” ou “2”,       Será gravado o conteúdo do campo “Contratação p/intermédio de entidade educativa/prática desportiva” (S/N), da       parametrização das informações do estabelecimento; Senão (conteúdo = “0”)      Este campo não será gerado;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |


| nrInsc | Campo “CNPJ” (quadro “Informações sobre contratação de aprendiz”) da parametrização das informações do estabelecimento.  Caso o CNPJ não esteja preenchido, este campo não será gerado. |
| --- | --- |


| contPCD  MFS-88128:VrsS-1.0 | Opção do campo “Contratação” (quadro “Informações sobre contratação de pessoa com deficiência”), da parametrização das informações do estabelecimento; Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| --- | --- |
| nrProcJud | Número do processo do campo “Processo” (quadro “Informações sobre contratação de pessoa com deficiência”) da parametrização das informações do estabelecimento. Caso este número de processo não esteja preenchido, este campo não será gerado. |


| iniValid | Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| fimValid | Campo “Validade Final” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento (neste caso, deve ser o CNPJ completo, com as 14 posições); |
| iniValid | Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização) |
| fimValid | Campo “Validade Final” da parametrização “Informações do Estabelecimento” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |
