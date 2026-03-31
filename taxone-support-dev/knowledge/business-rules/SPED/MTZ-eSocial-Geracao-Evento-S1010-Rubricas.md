# MTZ-eSocial-Geracao-Evento-S1010-Rubricas

> Fonte: MTZ-eSocial-Geracao-Evento-S1010-Rubricas.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1010 - Rubricas


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Cadastros



DOCUMENTO DE REQUISITO


Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	3
4.	Gravação dos Dados	5




Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.















## Parâmetros da Tela


Este documento é específico das regras de geração do evento S-1010.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Cadastros”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento


Origem dos dados: - SAFX2114 - Tabela de Cadastro das Rubricas (eSocial)
- Parametrização “Dados Iniciais” do Módulo eSocial


Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos dados da SAFX2114:

- Grupo – Considerar o Grupo de > data de validade que seja <= a data inicial do período informado em tela, para a qual a
SAFX2114 esteja associada;

- Data de Validade Inicial – Apenas as rubricas cuja data de validade inicial se enquadre no período informado em tela;


## Verificação do Status de Eventos já Gerados


MFS16751: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1010_OC, coluna IND_STATUS).

Para cada rubrica recuperada, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para a mesma data de validade.

Caso não:
O evento da rubrica será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:
A geração de um novo evento para a rubrica dependerá do status do evento já existente, da seguinte forma:

[MFS21382]


Se o status do evento já existente não permitir regeração:
Nesse caso a rubrica em questão será desconsiderada da geração, e será gravada a seguinte mensagem de aviso no log:
Aviso: Já existe evento anterior gerado para a rubrica. O status do evento não permite uma nova geração.
Dados do Registro:  Rubrica (Tabela/Cód.): XXXXXXXXXXXXX / XXXXXXXXXXXXXXXXXXXX, Validade Inicial: XX/XXXX

Se o status do evento já existente permitir regeração:

Se status = ‘1-Aguardando geração XML’, ‘4-Erro geração XML’, ‘6-Evento rejeitado pela mensageria’ (***), ‘10-Rejeitado pelo Fisco’ (***), ‘14-Evento excluído na mensageria’ ou ‘15-Erro técnico na mensageria’:
Nesse caso a rubrica em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente;

Se status = ‘8-Recebido pelo Fisco com sucesso’ (***) ou ‘9-Recebido pelo Fisco com advertência’ (***):
Nesse caso a rubrica em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações de rubrica ou exclusão das informações de rubrica, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão. Se não houver alteração ou exclusão não será permitida a regeração;

Se status = ‘12-Evento Excluído’ (***):
Nesse caso a rubrica em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

*** Importante: Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:


Para os demais Status serão descartados e substituídos pelos novos eventos regerados.



## Gravação dos Dados


Para cada rubrica recuperada, será gerado um evento S-1010 com as seguintes informações:

Registro evtTabRubrica – Evento tabela de Rubricas.




Registro ideEvento - Informações de Identificação do evento.



Registro ideEmpregador - Informações de identificação do empregador.




[MFS21382]
Registro ideRubrica - Informações de identificação da rubrica e período de validade das informações (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “I”.



Registro dadosRubrica - Detalhamento das informações da rubrica (Inclusão)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “I”.



Registro idProcessoCP – Informações de processo adm/judicial sobre a não incidência de contribuição previdenciária. (Inclusão)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo 12-Indicador do Tipo de Processo-CP)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “I”.



Registro idProcessoIRRF - Informações de processo administrativo/judicial sobre a não incidência do IRRF. (Inclusão)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo 16-Indicador do Tipo de Processo-IRRF)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “I”.



Registro ideRubrica - Informações de identificação da rubrica e período de validade das informações (Alteração)

Critérios: Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “A”.

Se houve o primeiro envio do evento S1010 com sucesso ou advertência e após for identificado qualquer alteração nas informações do cadastro das rubricas será a condição para o registro ser gerado.





Registro dadosRubrica - Detalhamento das informações da rubrica (Alteração)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “A”.




Registro idProcessoCP – Informações de processo adm/judicial sobre a não incidência de contribuição previdenciária. (Alteração)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo 12-Indicador do Tipo de Processo-CP)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “A”.





Registro idProcessoIRRF - Informações de processo administrativo/judicial sobre a não incidência do IRRF. (Alteração)

Caso não exista a informação deste tipo de processo, este registro não será gerado.

(a verificação será feita pelo preenchimento do campo 16-Indicador do Tipo de Processo-IRRF)

Critérios: Será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “A”.



Registro novaValidade - Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento.

Critério: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.




Registro ideRubrica - Informações de identificação da rubrica (Exclusão)

Critérios: Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: Tabela ESOCIAL_PGER_S1010_OC campo “IND_OPER” igual a “E”.

Se houve o primeiro envio do evento S1010 com sucesso ou advertência e após for identificado a exclusão das nas informações do cadastro das rubricas será a condição para o registro ser gerado.

= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15868 | Geração do evento das Rubricas (S-1010) | Geração dos dados do evento das Rubricas (S-1010) | 12/12/2017  (criação do documento) |
| MFS16751 | Controle dos Status x Regeração | Críticas em relação a regeração dos eventos. | 23/03/2018 |
| MFS21382 | Lara Aline | Inclusão da rotina de geração de Alteração e Exclusão. | 03/10/2018 |
| MFS-88129 | Elisabete Costa | Alterações para versão S-1.0 | 21/06/2022 |
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


| tpInsc | Conteúdo fixo = “1” (CNPJ) |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita; |


| codRubr | Campo Código da Rubrica – Informar o código atribuído pelo empregador que identifica a rubrica em sua folha de pagamento. |
| --- | --- |
| ideTabRubr | Campo Código da Tabela da Rubrica - Preencher com o identificador da Tabela de Rubricas no âmbito do empregador |
| iniValid | Mês a ano da data de validade inicial da rubrica (campo 03-Data de Validade Inicial) |
| fimValid | Mês a ano da data de validade final da rubrica (campo 04-Data de Validade FinaI). Se a validade final não estiver preenchida, este campo não será gerado. |


| dscRubr | Campo 19-Descrição da Rubrica - Informar a descrição (nome) da rubrica no sistema de folha de pagamento da empresa. |
| --- | --- |
| natRubr | Campo 20-Natureza da Rubrica - Informar o código de classificação da rubrica. |
| tpRubr | Campo 21-Tipo de Rubrica – Informar o Tipo de rubrica. |
| codIncCP  MFS-88129:VrsS-1.0 | Campo 22- Incidência Previdência Social - Código de incidência tributária da rubrica para a Previdência Social.  Tabela de Referência TACES62 Tipo = “1”  Até a versão 2.5.0. os valores válidos são: 00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 34, 35, 51, 61, 91, 92, 93, 94, 95, 96, 97, 98.  A partir da versão S-1.0, os valores válidos são: 00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 25, 26, 31, 32, 34, 35, 51, 91, 92, 93, 94, 95, 96, 97, 98. |
| codIncIRRF  MFS-88129:VrsS-1.0 | Campo 23- Incidência IRRF - Código de incidência tributária da rubrica para o Imposto de Renda Retido na Fonte - IRRF.  Tabela de Referência TACES62 Tipo = “2”  Até a versão 2.5.0. os valores válidos são: 00, 01, 09, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 51, 52, 53, 54, 55, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 94, 95.  A partir da versão S-1.0, os valores válidos são: 0, 1, 9, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 48, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 700, 701, 79, 81, 82, 83, 91, 92, 93, 94, 95, 9011, 9012, 9013, 9014, 9031, 9032, 9033, 9034, 9831, 9832, 9833, 9834, 9041, 9042, 9043, 9046, 9047, 9048, 9051, 9052, 9053, 9054, 9061, 9062, 9063, 9064, 9065, 9066, 9067, 9082, 9083  Tamanho: 04 |
| codIncFGTS | Este campo 24 será gerado com “00” - Código de incidência da rubrica para o Fundo de Garantia do Tempo de Serviço – FGTS. |
| CodIncSIND  MFS-88129:VrsS-1.0 | Este campo será gerado com “00” Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |
| codIncCPRP  MFS-88129:VrsS-1.0 | Campo 25- Incidência CPRP- Código de incidência da rubrica para as contribuições do Regime Próprio de Previdência Social - RPPS/regime militar.    A partir da versão S1.0 foi criado o campo codIncCPRP. O mesmo não deve ser gerado, pois se trata de contribuições de regime militar  Os valores válidos são: 00, 11, 12, 31, 32, 91.  Para registrar as incidências das contribuições previdenciárias dos servidores ativos, aposentados ou pensionistas vinculados aos RPPS, essas devem ser informadas no campo {codIncCPRP}, sob pena de, não o fazendo, acarretar a rejeição dos referidos eventos periódicos (S1202 ou S-1207). |
| tetoRemun  MFS-88129:VrsS-1.0 | Campo 26- Teto Remuneratório - Informar se a rubrica compõe o teto remuneratório específico (art. 37, XI, da CF/1988).  A partir da versão S1.0 foi criado o campo tetoRemun. O mesmo não deve ser gerado, pois é obrigatório se a natureza jurídica do declarante for Administração Pública (grupo [1])  Em relação aos servidores públicos, independentemente do regime de previdência adotado, e aos empregados públicos, é obrigatório informar se a rubrica compõe o teto remuneratório no campo {tetoRemun}, conforme descrito no art. 37, inciso XI e o seu § 9º da CF/1988 |
| Observação | Campo 19-Observação - Observações relacionadas à rubrica ou à sua utilização. Se a observação não estiver preenchida, este campo não será gerado |


| tpProc | Campo 12-Indicador do Tipo de Processo (CP) - Preencher com o código correspondente ao tipo de processo. |
| --- | --- |
| nrProc | Campo 13-Número do Processo (CP) - Informar um número de processo cadastrado |
| extDecisao | Campo 15-Extensão da Decisão/Sentença (CP) - Extensão da decisão/sentença |
| codSusp | Campo 14-Código do Indicativo da Suspensão (CP) -Código do indicativo da suspensão, atribuído pelo empregador em S-1070. |


| nrProc | Campo 17-Número do Processo (IRRF) - Informar um número de processo judicial cadastrado |
| --- | --- |
| codSusp | Campo 18-Código do Indicativo da Suspensão (IRRF) - Código do indicativo da suspensão, atribuído pelo empregador em S-1070. |


| codRubr | Campo 02-Código da Rubrica - Código atribuído pelo empregador que identifica a rubrica em sua folha de pagamento. |
| --- | --- |
| ideTabRubr | Campo 01-Código da Tabela da Rubrica - Identificador da Tabela de Rubricas no âmbito do empregador. |
| iniValid | Mês a ano da data de validade inicial da rubrica (campo 03-Data de Validade Inicial) - Mês e ano de início da validade das informações prestadas no evento.  Obs: A informação recuperada do campo data de validade inicial da rubrica será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. |
| fimValid | Mês a ano da data de validade final da rubrica (campo 04-Data de Validade FinaI). - Mês e ano de término da validade das informações,  Obs: A informação recuperada do campo data de validade final da rubrica será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. Se a validade final não estiver preenchida, este campo não será gerado. |


| dscRubr | Campo 05-Descrição da Rubrica |
| --- | --- |
| natRubr | Campo 06-Natureza da Rubrica |
| tpRubr | Campo 07-Tipo de Rubrica |
| codIncCP  MFS-88129:VrsS-1.0 | Campo 09- Incidência Previdência Social  Tabela de Referência TACES62 Tipo = “1”  Até a versão 2.5.0. os valores válidos são: 00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 34, 35, 51, 61, 91, 92, 93, 94, 95, 96, 97, 98.  A partir da versão S-1.0, os valores válidos são: 00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 25, 26, 31, 32, 34, 35, 51, 91, 92, 93, 94, 95, 96, 97, 98. |
| codIncIRRF  MFS-88129:VrsS-1.0 | Campo 11- Incidência IRRF  Tabela de Referência TACES62 Tipo = “2”  Até a versão 2.5.0. os valores válidos são: 00, 01, 09, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 51, 52, 53, 54, 55, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 94, 95.  A partir da versão S-1.0, os valores válidos são: 0, 1, 9, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 48, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 700, 701, 79, 81, 82, 83, 91, 92, 93, 94, 95, 9011, 9012, 9013, 9014, 9031, 9032, 9033, 9034, 9831, 9832, 9833, 9834, 9041, 9042, 9043, 9046, 9047, 9048, 9051, 9052, 9053, 9054, 9061, 9062, 9063, 9064, 9065, 9066, 9067, 9082, 9083 |
| codIncFGTS | Este campo será gerado com “00” |
| CodIncSIND  MFS-88129:VrsS-1.0 | Este campo será gerado com “00” Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |
| codIncCPRP  MFS-88129:VrsS-1.0 | Campo 25- Incidência CPRP  A partir da versão S1.0 foi criado o campo codIncCPRP. O mesmo não deve ser gerado, pois se trata de contribuições de regime militar Os valores válidos são: 00, 11, 12, 31, 32, 91.  Para registrar as incidências das contribuições previdenciárias dos servidores ativos, aposentados ou pensionistas vinculados aos RPPS, essas devem ser informadas no campo {codIncCPRP}, sob pena de, não o fazendo, acarretar a rejeição dos referidos eventos periódicos (S1202 ou S-1207). |
| tetoRemun  MFS-88129:VrsS-1.0 | Campo 26- Teto Remuneratório A partir da versão S1.0 foi criado o campo tetoRemun. O mesmo não deve ser gerado, pois é obrigatório se a natureza jurídica do declarante for Administração Pública (grupo [1])  Em relação aos servidores públicos, independentemente do regime de previdência adotado, e aos empregados públicos, é obrigatório informar se a rubrica compõe o teto remuneratório no campo {tetoRemun}, conforme descrito no art. 37, inciso XI e o seu § 9º da CF/1988 |
| observação | Campo 19-Observação Se a observação não estiver preenchida, este campo não será gerado |


| tpProc | Campo 12-Indicador do Tipo de Processo (CP) |
| --- | --- |
| nrProc | Campo 13-Número do Processo (CP) |
| extDecisao | Campo 15-Extensão da Decisão/Sentença (CP) |
| codSusp | Campo 14-Código do Indicativo da Suspensão (CP) |


| nrProc | Campo 17-Número do Processo (IRRF) |
| --- | --- |
| codSusp | Campo 18-Código do Indicativo da Suspensão (IRRF) |


| iniValid | Campo “Validade Inicial” da parametrização “Cadastro das Rubricas” (ver acima a regra para a recuperação dos dados desta parametrização) |
| --- | --- |
| fimValid | Campo “Validade Final” da parametrização “Cadastro das Rubricas” (ver acima a regra para a recuperação dos dados desta parametrização). Se a validade final não estiver preenchida, este campo não será gerado. |


| codRubr | Campo 02-Código da Rubrica |
| --- | --- |
| ideTabRubr | Campo 01-Código da Tabela da Rubrica |
| iniValid | Mês a ano da data de validade inicial da rubrica (campo 03-Data de Validade Inicial) |
| fimValid | Mês a ano da data de validade final da rubrica (campo 04-Data de Validade FinaI). Se a validade final não estiver preenchida, este campo não será gerado. |
