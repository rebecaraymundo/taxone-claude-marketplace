# MTZ-eSocial-Geracao-Evento-S1070-Processos

> Fonte: MTZ-eSocial-Geracao-Evento-S1070-Processos.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1070 – Processos Administrativos / Judiciais


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Cadastros



DOCUMENTO DE REQUISITO



Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	3
4.	Gravação dos Dados	5



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.















## Parâmetros da Tela


Este documento é específico das regras de geração do evento S-1070.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Cadastros”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento



Origem dos dados: - SAFX2058 - Tabela de Processos Administrativos / Judiciais
- SAFX2059 – Tabela de Informações de Suspensão de Exigibilidade de Tributos
- Parametrização “Dados Iniciais” do Módulo eSocial


Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;


Critérios para a recuperação dos processos na SAFX2058:

- Grupo – Considerar o Grupo de > data de validade que seja <= a data inicial do período informado em tela, para a qual a
SAFX2058 esteja associada;

- Data de Validade Inicial – Apenas os processos cuja data de validade inicial se enquadre no período informado em tela;

- Indicador de Incidência no eSocial = “S” (apenas os processos a serem enviados para o eSocial)



Os processos serão recuperados de acordo com os critérios acima, e para cada processo, serão recuperados os registros “filhos” na tabela SAFX2059 (estes registro “filhos” da SAFX2059 serão utilizados para gerar o registro infoSusp).



## Verificação do Status de Eventos já Gerados


MFS16751: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1070_OC, coluna IND_STATUS).

Para cada processo recuperado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para a mesma data de validade.

Caso não:

O evento do processo será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:

A geração de um novo evento para o processo dependerá do status do evento já existente, da seguinte forma:



[MFS-21384]



Se o status do evento já existente não permitir regeração:
Nesse caso o processo em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:
Aviso: Já existe evento anterior gerado para o processo. O status do evento não permite uma nova geração.
Dados do Registro:  Processo (Tipo/Número): X – XXXXXXXXXXXXXXXXXXXX, Validade Inicial: XX/XXXX

Se o status do evento já existente permitir regeração:

Se status = ‘1-Aguardando geração XML’, ‘4-Erro geração XML’, ‘6-Evento rejeitado pela mensageria’ (***), ‘10-Rejeitado pelo Fisco’ (***), ‘14-Evento excluído na mensageria’ ou ‘15-Erro técnico na mensageria’:
Nesse caso o processo/suspensão em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente;

Se status = ‘8-Recebido pelo Fisco com sucesso’ (***) ou ‘9-Recebido pelo Fisco com advertência’ (***):
Nesse caso o processo/suspensão em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações do processo/suspensão ou exclusão das informações do processo/suspensão, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão. Se não houver alteração ou exclusão não será permitida a regeração;

Se status = ‘12-Evento Excluído’ (***):
Nesse caso o processo/suspensão em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

*** Importante: Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:


Para os demais Status serão descartados e substituídos pelos novos eventos regerados.



(***) Os status 8 e 9 (Recebido pelo Fisco com Sucesso ou Advertência) permitem a regeração de um evento de cadastro no caso de uma alteração ou exclusão do cadastro. No entanto, este cenário ainda não será tratado no eSocial, uma vez que ainda não foi implementado o controle das alterações (manutenção e importação dos cadastros).

## Gravação dos Dados


Para cada processo recuperado, será gerado um evento S-1070 com as seguintes informações:


Registro evtTabProcesso – Evento tabela de Processos.



Registro ideEvento - Informações de Identificação do evento.



Registro ideEmpregador - Informações de identificação do empregador. (Inclusão)



Registro ideProcesso - Informações do processo (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “I”.





Registro dadosProc – Dados do processo (inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “I”.








Registro dadosProcJud - Informações complementares do processo judicial  (Inclusão)

Este registro será gerado apenas quando se tratar de processo do tipo judicial, ou seja, quando o campo “01-Indicador do Tipo de Processo” = 2 (Judicial).

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “I”.




Registro infoSusp - Informações de suspensão de exigibilidade de tributos (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “I”.

Este registro contém as informações sobre os códigos de suspensão. Para cada processo da SAFX2058, podem existir vários códigos de suspensão, ou seja, vários registros “filhos” na SAFX2059.

Para geração deste registro, serão recuperados todos os registros “filhos” do processo em questão na SAFX2059, e para cada um, será gerado um registro infoSusp com as seguintes informações:



Registro ideProcesso – Informações do processo (Alteração)

Critérios: Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “A”.

Se houve o primeiro envio do evento S1070 com sucesso ou advertência e após for identificado qualquer alteração nas informações do cadastro dos setores será a condição para o registro ser gerado.



Registro dadosProc – Dados do processo (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “A”.



Registro dadosProcJud - Informações complementares do processo judicial (alteração)

Este registro será gerado apenas quando se tratar de processo do tipo judicial, ou seja, quando o campo “01-Indicador do Tipo de Processo” = 2 (Judicial).

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “A”.




Registro infoSusp - Informações de suspensão de exigibilidade de tributos (alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “A”.

Este registro contém as informações sobre os códigos de suspensão. Para cada processo da SAFX2058, podem existir vários códigos de suspensão, ou seja, vários registros “filhos” na SAFX2059.

Para geração deste registro, serão recuperados todos os registros “filhos” do processo em questão na SAFX2059, e para cada um, será gerado um registro infoSusp com as seguintes informações:



Registro novaValidade - Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento.

Critério: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.




Registro ideProcesso - Informações do processo (Exclusão)

Critérios: Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1070_OC campo “IND_OPER” igual a “E”.

Se houve o primeiro envio do evento S1070 com sucesso ou advertência e após for identificado a exclusão das informações do cadastro dos processos será a condição para o registro ser gerado.



= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-15869 | Geração do evento dos Processos (S-1070) | Geração dos dados do evento dos Processos (S-1070) | 08/01/2018  (criação do documento) |
| MFS-18065 | Atualização do eSocial p/ vrs 2.4.02 | Inclusão de crítica para o número do processo e inclusão do campo Observação | 06/06/2018 |
| MFS-16751 | Controle dos Status x Regeração | Críticas em relação a regeração dos eventos. | 28/03/2018 |
| MFS-21384 | Lara Aline | Inclusão da rotina de geração de Alteração e Exclusão. | 08/10/2018 |
| MFS-88132 | Elisabete Costa | Alterações para versão S-1.0 | 23/06/2022 |
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


| tpProc  MFS-88132:VrsS-1.0 | Campo 01-Indicador do Tipo de Processo   Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4.  A partir da versão S-1.0, os valores válidos são: 1, 2, 4. |
| --- | --- |
| nrProc | Campo 02-Número do Processo    MFS18065: Inclusão da crítica do tamanho do número do processo conforme manual da versão 2.4.02:  Crítica do tamanho do número do processo x tipo do processo:   O conteúdo da informação do número do processo será validado em relação ao tipo informado no campo tpProc, da seguinte forma:  Se tpProc = “1” (processo administrativo)      Nesse caso o número do processo deve ter 17 ou 21 caracteres preenchidos;  Se tpProc = “2” (processo judicial)      Nesse caso o número do processo deve ter 20 caracteres preenchidos;  Se tpProc = “4” (processo FAP)      Nesse caso o número do processo deve ter 16 caracteres preenchidos;   Caso o conteúdo da informação do número do processo não atenda às condições acima, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O tamanho do campo Número do Processo (nrProc) não está de acordo com as orientações de preenchimento do campo no layout do eSocial.  Origem: Campo “02-Número do Processo” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| iniValid | Mês a ano da data de validade inicial do Processo (campo 03-Data Inico/Inclusão/Alteração) |
| fimValid | Mês a ano da data de validade final do Processo (campo 04-Data Término da Validade) Se a validade final não estiver preenchida, este campo não será gerado. |


| indAutoria | Campo 08-Indicador de Autoria Caso este campo não esteja preenchido na SAFX2058 e o Indicador do Tipo de Processo = 2 (Judicial), será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Indicativo da Autoria da Ação Judicial (indAutoria) é de preenchimento obrigatório e não foi informado Origem: Campo “08-Indicador de Autoria” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX  (Obs: Esta mensagem será gerada porque a manutenção da SAFX2058 permite processos do tipo 2 sem informar o campo da autoria da ação judicial) |
| --- | --- |
| indMatProc  MFS-88132:VrsS-1.0 | Campo 11-Matéria do Processo  Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4, 5, 6, 7, 8, 99.  A partir da versão S-1.0, os valores válidos são: 1, 7.  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Indicativo da Matéria do Processo (indMatProc) é de preenchimento obrigatório e não foi informado Origem: Campo “11-Matéria do Processo” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| observação | Campo 13-Observação  (campo incluído no evento pela MFS-18065 para atualização da vrs 2.4.02) |


| ufVara | Campo 05-UF  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo UF da Seção Judiciária (ufVara) é de preenchimento obrigatório e não foi informado Origem: Campo “05-UF” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| --- | --- |
| codMunic | A partir da UF e do município informados no processo (campos “05-UF” e “06-Código do Município”), acessar o registro do município na Tabela dos Municípios do IBGE (tabela MUNICIPIO).  O campo codMunic será gerado a partir da concatenação dos seguintes campos da tabela de municípios:                 Campo “Número UF p/Município” (COD_UF) + campo “Município” (COD_MUNICIPIO)  Obs: Para fazer a concatenação o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário.   Caso o campo “06-Código do Município” não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Município da Seção Judiciária (codMunic) é de preenchimento obrigatório e não foi informado Origem: Campo “06-Código do Município” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| idVara | Campo 07-Código da Vara  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código de Identificação da Vara (idVara) é de preenchimento obrigatório e não foi informado Origem: Campo “07-Código da Vara” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |


| codSusp | Campo 04-Código do Indicativo da Suspensão de Exigibilidade de Tributos (SAFX2059) |
| --- | --- |
| indSusp | Campo 05-Indicador da Suspensão de Exigibilidade de Tributos (SAFX2059) |
| dtDecisao | Campo 06-Data da Decisão |
| indDeposito | Campo 07-Indicador de Depósito |


| tpProc  MFS-88132:VrsS-1.0 | Campo 01-Indicador do Tipo de Processo   Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4.  A partir da versão S-1.0, os valores válidos são:  1, 2, 4. |
| --- | --- |
| nrProc | Campo 02-Número do Processo    MFS18065: Inclusão da crítica do tamanho do número do processo conforme manual da versão 2.4.02:  Crítica do tamanho do número do processo x tipo do processo:  O conteúdo da informação do número do processo será validado em relação ao tipo informado no campo tpProc, da seguinte forma:  Se tpProc = “1” (processo administrativo)      Nesse caso o número do processo deve ter 17 ou 21 caracteres preenchidos;  Se tpProc = “2” (processo judicial)      Nesse caso o número do processo deve ter 20 caracteres preenchidos;  Se tpProc = “4” (processo FAP)      Nesse caso o número do processo deve ter 16 caracteres preenchidos;   Caso o conteúdo da informação do número do processo não atenda às condições acima, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O tamanho do campo Número do Processo (nrProc) não está de acordo com as orientações de preenchimento do campo no layout do eSocial.  Origem: Campo “02-Número do Processo” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| iniValid | Mês a ano da data de validade inicial do Processo (campo 03-Data Inico/Inclusão/Alteração)  Obs: A informação recuperada do campo data de validade inicial do processo será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |
| fimValid | Mês a ano da data de validade final do Processo (campo 04-Data Término da Validade) Se a validade final não estiver preenchida, este campo não será gerado. Obs: A informação recuperada do campo data de validade final do processo será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |


| indAutoria | Campo 08-Indicador de Autoria  Caso este campo não esteja preenchido na SAFX2058 e o Indicador do Tipo de Processo = 2 (Judicial), será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Indicativo da Autoria da Ação Judicial (indAutoria) é de preenchimento obrigatório e não foi informado Origem: Campo “08-Indicador de Autoria” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX (Obs: Esta mensagem será gerada porque a manutenção da SAFX2058 permite processos do tipo 2 sem informar o campo da autoria da ação judicial) |
| --- | --- |
| indMatProc  MFS-88132:VrsS-1.0 | Campo 11-Matéria do Processo  Até a versão 2.5.0. os valores válidos são: 1, 2, 3, 4, 5, 6, 7, 8, 99.  A partir da versão S-1.0, os valores válidos são: 1, 7.  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Indicativo da Matéria do Processo (indMatProc) é de preenchimento obrigatório e não foi informado Origem: Campo “11-Matéria do Processo” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| observação | Campo 13-Observação  (campo incluído no evento pela MFS18065 para atualização da vrs 2.4.02) |


| ufVara | Campo 05-UF  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros: Erro: O campo UF da Seção Judiciária (ufVara) é de preenchimento obrigatório e não foi informado Origem: Campo “05-UF” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| --- | --- |
| codMunic | A partir da UF e do município informados no processo (campos “05-UF” e “06-Código do Município”), acessar o registro do município na Tabela dos Municípios do IBGE (tabela MUNICIPIO).  O campo codMunic será gerado a partir da concatenação dos seguintes campos da tabela de municípios:                 Campo “Número UF p/Município” (COD_UF) + campo “Município” (COD_MUNICIPIO)  Obs: Para fazer a concatenação o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário.   Caso o campo “06-Código do Município” não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Município da Seção Judiciária (codMunic) é de preenchimento obrigatório e não foi informado Origem: Campo “06-Código do Município” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| idVara | Campo 07-Código da Vara  Caso este campo não esteja preenchido na SAFX2058, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo Código de Identificação da Vara (idVara) é de preenchimento obrigatório e não foi informado Origem: Campo “07-Código da Vara” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |


| codSusp | Campo 04-Código do Indicativo da Suspensão de Exigibilidade de Tributos (SAFX2059) |
| --- | --- |
| indSusp | Campo 05-Indicador da Suspensão de Exigibilidade de Tributos (SAFX2059) |
| dtDecisao | Campo 06-Data da Decisão |
| indDeposito | Campo 07-Indicador de Depósito |


| iniValid | Campo “Validade Inicial” da parametrização “Cadastro dos Processos Administrativos/Judiciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| fimValid | Campo “Validade Final” da parametrização “Cadastro dos Processos Administrativos/Judiciais” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |


| tpProc | Campo 01-Indicador do Tipo de Processo |
| --- | --- |
| nrProc | Campo 02-Número do Processo    MFS18065: Inclusão da crítica do tamanho do número do processo conforme manual da versão 2.4.02:  Crítica do tamanho do número do processo x tipo do processo:   O conteúdo da informação do número do processo será validado em relação ao tipo informado no campo tpProc, da seguinte forma:  Se tpProc = “1” (processo administrativo)      Nesse caso o número do processo deve ter 17 ou 21 caracteres preenchidos;  Se tpProc = “2” (processo judicial)      Nesse caso o número do processo deve ter 20 caracteres preenchidos;  Se tpProc = “4” (processo FAP)      Nesse caso o número do processo deve ter 16 caracteres preenchidos;   Caso o conteúdo da informação do número do processo não atenda às condições acima, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O tamanho do campo Número do Processo (nrProc) não está de acordo com as orientações de preenchimento do campo no layout do eSocial.  Origem: Campo “02-Número do Processo” da Tabela de Processos Adm/Judiciais (SAFX2058) Dados do Registro: Tipo / Número do Processo: X / XXXXXXXXXXXXXXXX |
| iniValid | Mês a ano da data de validade inicial do Processo (campo 03-Data Inico/Inclusão/Alteração) |
| fimValid | Mês a ano da data de validade final do Processo (campo 04-Data Término da Validade) Se a validade final não estiver preenchida, este campo não será gerado. |
