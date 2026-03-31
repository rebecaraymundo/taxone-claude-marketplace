# MTZ-eSocial-Geracao-Evento-S1300-Contribuicao-Sindical

> Fonte: MTZ-eSocial-Geracao-Evento-S1300-Contribuicao-Sindical.docx






THOMSON REUTERS

Módulo eSocial

Geração Evento S-1300

(Contribuição Sindical Patronal)


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração Prévia dos Movimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento	2
3.	Verificação do Status de Eventos já Gerados	4
4.	Gravação dos Dados	6


















O Evento S-1300 não deve ser gerado a partir da versão S-1.0
[MFS-87543]
## Parâmetros da Tela


Este documento é específico das regras de geração do evento S-1300.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ-eSocial-Geracao-Movimentos”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento


Origem dos dados: - Parametrização “Dados Iniciais” do Módulo eSocial;
- SAFX251 - Tabela das Contribuições Sindicais do Período;

A partir da versão S1.0 esse evento não será mais gerado.

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;


Critérios para a recuperação das contribuições sindicais do período na SAFX251:

- Empresa – empresa do estabelecimento centralizador selecionado;
- Estabelecimento – Serão recuperadas as contribuições de todos os estabelecimentos envolvidos na centralização (o estabelecimento
centralizador, que é o selecionado em tela, e os centralizados), de acordo com a parametrização das obrigações federais do módulo
Parâmetros (menu Preliminares > Centralização da Escrituração de Obrigações Federais);
- Ano Referência – ano do período informado na tela da geração (campo “Período”);
- Mês Referência – mês do período informado na tela da geração (campo “Período”);

Agrupamento dos dados:

Para cada estabelecimento centralizador será gerado um único evento S-1300, com as informações descritas no item “Gravação dos Dados”.

As contribuições recuperadas para cada estabelecimento centralizador, serão agrupadas e totalizadas pelas seguintes informações:

- Sindicato (campo 05-Código do Sindicato);
- Tipo da Contribuição (campo 06-Tipo da Contribuição);
- Campo a ser totalizado: 07-Valor da Contribuição

O resultado de cada totalização irá gerar um registro contribSind. Desta forma, se dois estabelecimentos envolvidos na centralização tiverem contribuições na SAFX251 para um mesmo Sindicato, e que sejam do mesmo tipo, será gerado um único registo contribSind no evento.

Exemplo: Supondo que os estabelecimentos ESOC1 e ESOC2 estejam centralizados, sendo o ESOC1 o centralizador, e que existam na SAFX251 as seguintes contribuições:




O resultado do agrupamento seria o seguinte, e seriam gravados quatro registros contribSind:


## Verificação do Status de Eventos já Gerados



MFS16751: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração (ESOCIAL_PGER_S1300_OC, coluna IND_STATUS).

Para cada estabelecimento a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este estabelecimento no mesmo período de referência.

Caso não:

O evento do estabelecimento será gerado normalmente, como definido no item “4-Gravação dos Dados”.

Caso sim:

A geração de um novo evento para o estabelecimento dependerá do status do evento já existente, da seguinte forma:


Se o status do evento já existente não permitir regeração:

Nesse caso, o estabelecimento em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:

Aviso: Já existe evento anterior gerado para o estabelecimento. O status do evento não permite uma nova geração.
Dados do Registro:  Estabelecimento: XXXXXX  /  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX, Período: XX/XXXX

Se o status do evento já existente permitir regeração:

Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação ORIGINAL ou uma
RETIFICAÇÃO, dependendo do status do evento original, como descrito a seguir:

- Se status do evento original = 8 ou = 9  Nesse caso, o novo evento será gerado como RETIFICAÇÃO;

- Se status do evento original <> 8 e <> 9  Nesse caso, o novo evento será gerado como ORIGINAL;




[MFS16762]
Importante: Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação (Critérios estão no documento de tela do Painel de Controle de Eventos) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.

## Gravação dos Dados


As contribuições recuperadas, agrupadas e totalizadas conforme a regra acima, serão geradas num único evento S-1300, com as seguintes informações:

(os registros não citados não serão gerados)

Registro evtContrSindPatr – Evento Contribuição Sindical Patronal



Registro ideEvento - Informações de Identificação do evento.




Registro ideEmpregador - Informações de identificação do empregador.



Registro contribSind - Informações da contribuição sindical patronal.

Este registro é gerado a partir das contribuições agrupadas e totalizadas conforme descrito no item “2-Recuperação dos Dados e Processamento”.

Para cada combinação de Sindicato e Tipo da Contribuição, será gerado um registro contribSind com o valor total das contribuições.





= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15871 | Geração do evento S-1300 | Geração dos dados do evento S-1300 (Contribuição Sindical Patronal) | 28/12/2017  (criação do documento) |
| MFS16751 | Controle Status x Regeração | Críticas em relação a regeração dos eventos. | 28/03/2018 |
| MFS16762 | Lara Aline | Inclusão rotina de Reprocessar Evento | 28/08/2018 |
| MFS-87543 | Elisabete Costa | Exclusão do Evento S-1300 - Para versão S-1.0 | 06/06/2022 |


| Estabelecimento | Sindicato | Tipo | Valor |
| --- | --- | --- | --- |
| ESOC1 | SD-1 | 1 | 4.500,00 |
| ESOC1 | SD-1 | 2 | 1.200,00 |
| ESOC1 | SD-2 | 1 | 850,00 |
| ESOC2 | SD-1 | 1 | 6.000,00 |
| ESOC2 | SD-2 | 1 | 2.400,00 |
| ESOC2 | SD-3 | 1 | 700,00 |


| Sindicato | Tipo | Valor |
| --- | --- | --- |
| SD-1 | 1 | 10.500,00 |
| SD-1 | 2 | 1.200,00 |
| SD-2 | 1 | 3.250,00 |
| SD-3 | 1 | 700,00 |


| Status | Permite regeração dos dados |
| --- | --- |
| 1-Aguardando geração XML | Sim |
| 3-Enviando para mensageria | Não |
| 4-Erro geração XML | Sim |
| 5-Evento recebido pela mensageria | Não |
| 6-Evento rejeitado pela mensageria | Sim |
| 7-Em Processamento (mensageria) | Não |
| 8-Recebido pelo Fisco com sucesso | Sim (Retificação) |
| 9-Recebido pelo Fisco com advertência | Sim (Retificação) |
| 10-Rejeitado pelo Fisco | Sim |
| 12-Evento Excluído | Sim |
| 14-Evento excluído na mensageria | Sim |
| 15-Erro técnico na mensageria | Sim |


| Sobre a limpeza do evento já existente: Se o status do evento já existente for = 1 (Aguardando geração XML), 4 (Erro geração XML) ou 14 (Evento excluído na mensageria), este evento será apagado ao efetuar a regeração de um novo evento. Nos demais casos, a limpeza do evento já existente não será feita (para manter o histórico dos erros ocorridos), e será feita apenas a regeração de um novo evento. |
| --- |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:  “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita; Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| indRetif | Conteúdo fixo = “1” (Arquivo original) OBS: A princípio, este campo será gerado sempre como “1” (Arquivo original). Somente após a criação do painel é que teremos o controle automático, para verificar se é uma retificação ou não.  MFS16751: Alteração para gerar também os eventos de retificação.  Este campo será gerado de acordo com a verificação de status descrita no item “3-Verificação do Status de Eventos já Gerados”:  Se for a primeira geração do evento do estabelecimento no período:       O campo será gerado com “1” (Arquivo Original); Senão       Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:        Se status do evento original = 8 ou = 9  O campo será gerado com “2” (Retificação);       Se status do evento original <> 8 e <> 9  O campo será gerado com “1” (Arquivo Original); |
| --- | --- |
| nrRecibo | Este campo não será preenchido OBS: Este campo será gerado somente após a criação do painel, quando teremos o controle automático para verificar se é uma retificação ou não.  MFS16751: Alteração para gerar também os eventos de retificação.  Este campo será gerado de acordo com o conteúdo do campo anterior (indRetif), da seguinte forma:  Se indRetif = “1” (Arquivo Original)       Nesse caso este campo não será gerado;  Se indRetif = “2” (Retificação)       Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado. Ou seja, com o conteúdo      do campo nrRecibo que consta no evento original; |
| indApuracao | Conteúdo fixo = “1” (= Mensal)  (como os autônomos não têm décimo terceiro salário, este campo será gerado sempre como “1”) |
| perApur | Mês e ano do período informado na tela da geração, no formato AAAA-MM (conforme orientação do layout) |
| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do empregador) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”.  Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita; |


| cnpjSindic | Este campo será gerado com a informação do CNPJ do sindicato, recuperado da SAFX2048 (Tabela dos Sindicatos, campo CNPJ do Sindicato), através do campo 05-Código do Sindicato da SAFX251.  Caso o CNPJ do Sindicato não esteja preenchido na SAFX2048, será gerada a seguinte mensagem de aviso no log de erros:  Erro: O campo CNPJ da entidade Sindical Beneficiária (cnpjSindic) é de preenchimento obrigatório e não foi informado Origem: Campo “05-CNPJ do Sindicato” da Tabela de Sindicatos (SAFX2048) Dados do Registro: Sindicato: XXXXX |
| --- | --- |
| tpContribSind | Campo 06-Tipo da Contribuição |
| vlrContribSind | Campo 07-Valor da Contribuição (total agrupado por Sindicato e Tipo da Contribuição) |
