# MTZ_REINF_Geracao_Evento_Movimento_R4080

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R4080.docx






THOMSON REUTERS

Módulo REINF

Geração do Evento R-4080

(Retenção no Recebimento)


Localização: Menu SPED, módulo EFD-REINF, menu REINF à Geração Prévia à Movimentos à Evento R-4080




DOCUMENTO DE REQUISITO








Detalhamento das Regras:

Registro evtRetRec – Evento Retenção no Recebimento



Registro ideEvento - Informações de Identificação do evento.




Registro ideContri - Informações de identificação do contribuinte.



Registro ideEstab- Informações de identificação do estabelecimento




Registro ideFont – Identificação da Fonte Pagadora do Rendimento




Registro ideRend – Identificação do Rendimento




Registro infoRec - Informações relativas ao recebimento do rendimento


Este registro será gerado quando existir informações na SAFX283- Retenção no Recebimento (Evento R-4080).
Agrupar por contribuinte, fonte pagadora e natureza de rendimento.

[EXCLUSÃO MFS-615706] Exclusão da consolidação feita na MFS-511292, dos contribuintes que possuem dados de recebimento com mesma natureza de rendimento, mesma fonte pagadora e datas dentro do mesmo mês da apuração
[ALTERAÇÃO MFS-511292] Consolidação de registros:

Caso exista mais de um registro para o mesmo contribuinte, mesma natureza de rendimento e fonte pagadora, dentro do mesmo período de apuração, gerar apenas um registro para o evento, consolidando os valores e considerar a informação da maior data (campo dtFG) dos registros recuperados.
Serão aceitos normalmente, na geração do XML, mais de um recebimento com a mesma natureza de rendimento, mesma fonte pagadora e de datas que estejam dentro do mês de apuração:
Exemplo de XML , validado com sucesso pelo FISCO:




[ALTERAÇÃO MFS-615706] Consolidação quando há mais de um cadastro para a mesma fonte pagadora (mesmo CNPJ):
Chave: agrupar por fonte pagadora (CNPJ), natureza de rendimento, data

Caso exista mais de um cadastro para uma fonte pagadora (cadastros com o mesmo CNPJ) e no período existir movimentação para essas fontes pagadoras, as informações de todas as tags deste evento, a partir da tag ideFont (Fonte Pagadora), deverão ser consolidadas, gerando as informações no mesmo XML. O sistema irá considerar a movimentação de todas essas fontes pagadoras, em um único arquivo.
A consolidação das informações será feita pelos campos chaves do evento/tags. Já os campos que não compõem a chave, e que são campos de cadastros, serão considerados conforme cadastrados na primeira fonte pagadora recuperada. Os campos de valores devem ser somados apenas se o recebimento for na mesma data, conforme exemplos abaixo:

Ex.: Mesma fonte pagadora com datas distintas:
Fonte Pagadora 1 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 01/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 3000,00; Valor Base:3000,00; Valor IR:30,00; Obs.: 01
Fonte Pagadora 2 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 02/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 4000,00; Valor Base:4000,00; Valor IR:40,00; Obs.: 02


Sairão no XML, os dois recebimentos, considerando os dados cadastrais da Fonte Pagadora 1, com as respectivas datas 01/08/2023 e 02/08/2023 (tag ideRend) e seus respectivos valores e observações.


Ex.: Mesma fonte pagadora com datas iguais:
Fonte Pagadora 1 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 01/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 3000,00; Valor Base:3000,00; Valor IR:30,00; Obs.: 01
Fonte Pagadora 2 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 01/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 4000,00; Valor Base:4000,00; Valor IR:40,00; Obs.: 02

Sairão no XML, os dois recebimentos, considerando os dados cadastrais da Fonte Pagadora 1, consolidando os valores em um único recebimento 01/08/2023 e a consolidação dos valores (Valor Bruto: 7000,00; Valor Base:7000,00; Valor IR:70,00), com a Obs.: 01.

Quando existir o cenário acima (mais de um cadastro de fonte pagadora, com o mesmo CNPJ), exibir a mensagem no log: “No período, há recebimentos com cadastros distintos de fonte pagadora com o mesmo CNPJ. Para evitar a geração de mais de uma linha no XML, e o evento ser rejeitado pelo fisco, as informações foram consolidadas pela fonte pagadora <<CNPJ da fonte pagadora do primeiro registro recuperado>>.”

Poderão existir até 999 registros de recebimento. Será gerado um registro infoRec, com as informações descritas abaixo:




Registro infoProcRet - Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais.

Este registro será gerado quando existir informações na SAFX284 - Processos Administrativos/Judiciais relacionados a não retenção de tributos ou a depósitos judiciais (Evento R-4080).


[ALTERAÇÃO MFS-615706] Consolidação quando há mais de um cadastro para a mesma fonte pagadora (mesmo CNPJ):
Chave: agrupar por fonte pagadora (CNPJ), natureza de rendimento, data, tipo e número de processo e cod_susp


Caso exista mais de um cadastro para uma fonte pagadora (cadastros com o mesmo CNPJ) e no período existir movimentação para essas fontes pagadoras, as informações de todas as tags deste evento, a partir da tag ideFont (Fonte Pagadora), deverão ser consolidadas, gerando as informações no mesmo XML. O sistema irá considerar a movimentação de todas essas fontes pagadoras, em um único arquivo.
A consolidação das informações será feita pelos campos chaves do evento/tags. Já os campos que não compõem a chave, e que são campos de cadastros, serão considerados conforme cadastrados na primeira fonte pagadora recuperada. Os campos de valores devem ser somados apenas se o recebimento for na mesma data, conforme exemplos abaixo:



Ex.: Mesma fonte pagadora com processos iguais:
Fonte Pagadora 1 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 01/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 3000,00; Valor Base:3000,00; Valor IR:30,00; Obs.: 01
Fonte Pagadora 2 – CNPJ: 44.466.777/0001-11 - Data do Recebimento 01/08/2023; Natureza de Rendimento: 20007; Valor Bruto: 4000,00; Valor Base:4000,00; Valor IR:40,00; Obs.: 02

Sairão no XML, os dois recebimentos, considerando os dados cadastrais da Fonte Pagadora 1, consolidando os valores em um único recebimento 01/08/2023 e a consolidação dos valores (Valor Bruto: 7000,00; Valor Base:7000,00; Valor IR:70,00), com a Obs.: 01 e apenas a ocorrência do processo Número: 20240101123 e Cód. Susp. 010101 (do primeiro registro recuperado), deve ser informado no XML (mesmo que os valores entre eles sejam distintos).



Poderão existir 50 registros de processos (infoProcRet). Para cada registro recuperado, será gerado um registro com as informações descritas abaixo:




= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79907 | Alessandra Cristina Navatta | Criação da geração do Evento R-4080- Retenção no Recebimento (atendimento ao layout 2.1 do REINF) | 18/04/2022 |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação. | 02/08/2022 |
| MFS-511292 | Alessandra Cristina Navatta | Consolidação valores para o mesmo contribuinte, fonte pagadora e natureza de rendimento quando os registros estiverem no mesmo período de apuração. Cenário identificado no envio do XML para o Fisco. | 08/02/2023 |
| MFS-537238 | Alessandra Cristina Navatta | Adequação da geração do evento R-4080, para atendimento ao layout 2.1.2  Ajustes efetuados: Inclusão do campo Observ da tag infoRec Alteração na regra do campo Obsev da tag ideRend | 19/07/2023 |
| MFS-615706 | Alessandra Cristina Navatta | Ajustes realizados na demanda: Retirada a consolidação que foi feita na MFS-511292. Feito teste enviando o evento para o fisco e o governo não está mais rejeitando eventos R-4080 do contribuinte com recebimento de mesma natureza de rendimento, mesma fonte pagadora e que estão dentro do mesmo mês de apuração. Consolidação das informações quando existir na base mais de um cadastro para a mesma fonte pagadora (mais de um cadastro com o mesmo CNPJ). | 27/02/2024 |


| DESCRIÇÃO | OS/CH |
| --- | --- |
| Regra Geral de Geração do Evento R-4080.  O evento R-4080 do SPED - REINF tem por objetivo gerar informações de Retenção no Recebimento. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtRetRec – Evento Retenção no Recebimento   ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte ideEstab - Identificação do Estabelecimento ideFont – Identificação da Fonte Pagadora ideRend– Identificação do Rendimento infoRec– Informações relativas ao recebimento do rendimento  infoProcRet– Processos relacionados a não retenção de tributos   Observar orientações existentes no arquivo "TR_REINF_DEXPARA_V2.1.1.xlsx".   Origem das informações: Cadastro do Estabelecimento;                              SAFX283 - Retenção no Recebimento (Evento R-4080);                              SAFX284 - Processos Administrativos/Judiciais relacionados a não retenção de tributos ou a depósitos judiciais (Evento R-4080);  Regra de seleção: O Registro R-4080 é demonstrará as informações de retenção no recebimento.  Ele será gerado com base nas informações da SAFX283 - Retenção no Recebimento (Evento R-4080) e SAFX284 - Processos Administrativos/Judiciais relacionados a não retenção de tributos ou a depósitos judiciais (Evento R-4080), considerando os seguintes critérios:  - O COD_ESTAB seja de um estabelecimento indicado pelo usuário; -Os registros devem estar compreendidos (Data do Recebimento, da SAFX283) no período da Apuração do Arquivo   Tela de Geração Prévia e Painel de Eventos: Pela tela de Geração Prévia, só serão permitidas gerações originais.  Na tela de Painel de Eventos, dependendo do status pode ser feita geração original. Já as gerações retificadoras, sempre serão realizadas pela tela do painel, pela opção ‘Reprocessar Evento’.   Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:  Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original.  Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:  Evento R4080 – Retenção no Recebimento                                  Evento não gerado. Existe evento anterior enviado aguardando retorno.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:  - Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação. - Se existir, evento de exclusão considerar os status, então:  Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:                 Evento R4080 – Retenção no Recebimento                                 Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX            Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência           anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova           ocorrência de arquivo de retificação, se não houver, criar original.                - Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do XML” então, criar nova ocorrência de retificação.               - Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:                                Evento R4080 – Retenção no Recebimento                                  Evento não gerado. Existe evento anterior não enviado.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se não houver, criar original.  Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se não houver, criar original.    Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.  Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.  Se houver ocorrência de geração de evento de fechamento considerar os status então:                        - Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:                                                R4080 – Retenção no Recebimento                                      Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                        - Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte                         mensagem no log de geração:                                    R4080 – Retenção no Recebimento                                      Evento não gerado. Período Fechado.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com Sucesso ou Advertência”, prosseguir com a geração.                 - Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do             XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:                     R4080 – Retenção no Recebimento                                       Evento não gerado. Período Fechado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                      Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,                    prosseguir com a geração.                          - Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de                             geração:                     R4080 – Retenção no Recebimento                                       Evento não gerado. Existe evento de fechamento do período não enviado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Gravação dos Registros: Todos os registros recuperados na geração do evento R-4080; são gravados em uma tabela. Esta tabela é utilizada na emissão do relatório de conferência do evento (formato “Analítico”), que mostra por natureza de rendimento e data de fato gerador as informações de Pagamentos/créditos a beneficiários não identificados. Além do formato sintético, que o agrupamento, não considera a data do movimento. | MFS-79907 MFS-90001 |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:   “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita; Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| indRetif | Este campo será gerado de acordo com a verificação de status descrita no item “3-Verificação do Status de Eventos já Gerados”:  Se for a primeira geração do evento do contribuinte no período:       O campo será gerado com “1” (Arquivo Original); Senão       Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:        Se status do evento original = 8 ou = 9 à O campo será gerado com “2” (Retificação);       Se status do evento original <> 8 e <> 9 à O campo será gerado com “1” (Arquivo Original); |
| --- | --- |
| nrRecibo | Este campo será gerado de acordo com o conteúdo do campo anterior (indRetif), da seguinte forma:  Se indRetif = “1” (Arquivo Original)       Nesse caso este campo não será gerado;  Se indRetif = “2” (Retificação)       Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado. Ou seja, com o conteúdo      do campo nrRecibo que consta no evento original; |
| perApur | Mês e ano do período informado na tela da geração, no formato AAAA-MM (conforme orientação do layout) |
| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do contribuinte) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”.   Obs: A princípio, a definição previa informar neste campo a versão do produto informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita. |


| tpInscEstab | Conteúdo fixo = “1” |
| --- | --- |
| nrInscEstab | CNPJ do estabelecimento |


| cnpjFont | CNPJ da Fonte Pagadora |
| --- | --- |


| NatRend | Lista de Valores Válidos: 20001; 20002; 20003; 20004; 20005; 20006; 20007; 20008; 20009; 20010   O Registro será recuperado da SAFX283, campo Natureza do Rendimento. |
| --- | --- |
| Observ | [EXCLUSÃO MFS-537238] Exclusão de regra, pois, foi inserido novo campo de observação na tag de infoRec e essa observação refere-se a uma observação da natureza de rendimento, que não estamos considerando no sistema  O Registro será recuperado da SAFX283, campo Observações. |


| dtFG | Campo 03 - Data do Recebimento (SAFX83)  O formato da data deve ser AAAA-MM-DD. | MFS-79907 |
| --- | --- | --- |
| vlrBruto | Campo 08 - Valor Bruto (SAFX283)  Validação: **O valor deve ser maior que zero. (**Esta validação ocorre na importação da SAFX283 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >>Retenções >>Retenção no Recebimento) | MFS-79907 |
| vlrBaseIR | Campo 09 - Valor Base IR (SAFX283)  Validação: **O valor deve ser maior que zero. (**Esta validação ocorre na importação da SAFX283 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Retenção no Recebimento) | MFS-79907 |
| VlrIR | Campo 10 - Valor do Imposto de Renda Retido na Fonte (SAFX283) | MFS-79907 |
| Observ | [ALTERAÇÃO MFS-537238] Observação   Este campo foi inserido na versão 2.1.2 do layout.  Recuperar o campo 07 - Observação da SAFX283. | MFS-537238 |


| TpProcRet | Campo 07 - Tipo do Processo (SAFX284). Este campo deve estar previamente cadastrado na SAFX2058, Campo 01- Tipo do Processo (SAFX2058)  Opções Válidas:  1 - Administrativo; 2 - Judicial.   Valores válidos: 1, 2 | MFS-79907 |
| --- | --- | --- |
| nrProcRet | Campo 08 - Número do Processo (SAFX284). Este campo deve estar previamente cadastrado na SAFX2058, Campo 02 Número do Processo (SAFX2058) | MFS-79907 |
| codSusp | Campo 09 - Código do Indicativo da Suspensão de Exigibilidade de Tributos (SAFX284). Este campo deve estar previamente cadastrado na SAFX2059, Campo 05 - Indicador da Suspensão de Exigibilidade de Tributos (SAFX2059) | MFS-79907 |
| vlrBaseSuspIR | Campo 10- Valor da Base com Exigibilidade Suspensa (SAFX284) Validações:	 **Este campo quando preenchido não pode ser maior que o campo VlrBruto do evento R-4080 (**Esta validação ocorre na importação da SAFX284 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Retenção no Recebimento >> Processos R-4080) | MFS-79907 |
| vlrNIR | Campo 11 - Valor da Retenção que Deixou de ser Efetuada (SAFX284)  Validações: **Este campo é de preenchimento obrigatório se o campo IND_DEPOSITO da SAFX2059 for igual a ‘N’. (**Esta validação ocorre na importação da SAFX284 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Retenção no Recebimento >> Processos R-4080) | MFS-79907 |
| VlrDepIR | Campo 12 - Valor do Depósito Judicial (SAFX284)  Validações: **Este campo é de preenchimento obrigatório se o campo IND_DEPOSITO da SAFX2059 for igual a ‘S’. (**Esta validação ocorre na importação da SAFX284 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Retenção no Recebimento >> Processos R-4080) | MFS-79907 |
