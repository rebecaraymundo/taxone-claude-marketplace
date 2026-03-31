# MTZ_REINF_Geracao_Evento_Movimento_R2099

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2099.docx






THOMSON REUTERS

Geração evento R-2099 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte




Registro ideRespInf – Responsável pelas informações





Registro infoFech – Informações do Fechamento.





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-11898 | Lara Aline | Definição de regras para geração do evento R-2099 Reinf |
| MFS17973 | Lara Aline | Inclusão da geração do R-2099 sem movimento |
| MFS20930 | Lara Aline | Ajuste nos campos evtPgtos e compSemMovto, conforme Layout 1.4 |
| MFS59340 | Alessandra Cristina Navatta | Inclusão das informações do campo evtAquis, conforme Layout 1.5.1 (RN15.01) |
| MFS-79878 | Alessandra Cristina Navatta | Exclusão dos campos 25 - evtPgtos e 26 – compSemMovto, no evento R-2099, a partir da versão 2.1 do REINF (RN16 e RN17) |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2099.  O evento R-2099 do SPED - REINF tem por objetivo informar o encerramento da transmissão dos eventos periódicos na EFD-Reinf, no período de apuração. Neste momento são consolidadas todas as informações prestadas nos eventos R-2010 a R-2070. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtFechaEvPer – Evento de Fechamento  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  ideRespInf – Responsável pelas informações   infoFech – Informações do Fechamento.   Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: Tela de Dados Iniciais, Cadastro do Estabelecimento.   Regra de seleção: O Registro R-2099 é utilizado para informar o encerramento da transmissão dos eventos periódicos na EFD-Reinf, no período de apuração. Neste momento são consolidadas todas as informações prestadas nos eventos R-2010 a R-2070. Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado esse evento também será gerado, porém apenas se não existir eventos de movimento gerados no período R-2010 a R-2070.  Mensageria Log:   1 - Verificar se dentro do período de apuração existe algum evento periódico nas tabelas de ocorrência com IND_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R-2099 – Fechamento e exibir a seguinte mensagem:   Evento R-2099 – Fechamento dos Eventos Periódicos “Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX    2 - Verificar se já foi efetuada a geração e envio do evento R-2099 – Fechamento para esse período de apuração, caso ainda não tenha retorno (IND_STATUS = 2), exibir a seguinte mensagem:  Evento R-2099 – Fechamento dos Eventos Periódicos “O fechamento do período já foi executado e seu evento enviado ao Fisco, mas ainda aguarda retorno. Somente refazer esta operação, caso o retorno seja erro.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX   Tratamento para geração do Evento R-2099 - Fechamento dos Eventos Periódicos – Sem Movimento:  Esse evento será gerado apenas se não existir nenhum evento de movimento (R-2010 a R-2070) gerado no período que o usuário estiver tentando efetuar a geração prévia, caso encontrado algum evento de movimento no período será gerada uma mensagem de erro no log da tela de Geração Prévia dos Movimentos, e a geração não será efetuada: “Evento R-2099 sem movimento não será gerado, pois existe evento de movimento gerado nesse período.”. | MFS-11898 MFS17973 MFS-90001 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtFechaEvPer  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-11898 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1” | MFS-11898 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS-11898 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN04 | Origem das informações: Tela de Dados Iniciais   Regra de seleção: Este registro servirá identificar o responsável pelas informações  Campos-Chave: nmResp, cpfResp  Nível hierárquico do registro: filho do registro evtFechaEvPer.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir | MFS-11898 |
| RN05 | Campo nmResp  Informação será recuperada do campo Nome da tela de “Dados Iniciais”. | MFS-11898 |
| RN06 | Campo cpfResp  Informação será recuperada do campo CPF da tela de “Dados Iniciais”. | MFS-11898 |
| RN07 | Campo telefone  Informação será recuperada do campo Telefone, caso não preenchido será recuperado do campo Celular da tela de “Dados Iniciais”. | MFS-11898 |
| RN08 | Campo email  Informação será recuperada do campo Email da tela de “Dados Iniciais”. | MFS-11898 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN09 | Origem das informações: Eventos R-2010 ao R-2070  Regra de seleção: Este registro apresenta as informações do Fechamento.  Nível hierárquico do registro: filho do registro evtFechaEvPer.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-11898 |
| RN10 | Campo evtServTm  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2010 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN11 | Campo evtServPr  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2020 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN12 | Campo evtAssDespRec  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2030 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN13 | Campo evtAssDespRep  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2040 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN14 | Campo evtComProd  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2050 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN15 | Campo evtCPRB  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2060 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-11898 MFS17973 |
| RN15.01 | Campo evtAquis  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2055 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’ | MFS-59340 |
| RN16 | Campo evtPgtos  Informação a ser gravada nesse campo:  S – Sim; N – Não.  Validação: Se existir evento R-2070 para o período de apuração com IND_STATUS = ‘3’, gravar ‘S – Sim’. Caso contrário gravar ‘N – Não’.  A partir do layout 1.4 gravaremos nesse campo sempre o valor ‘N – Não’.  Até a inclusão da família de eventos "R-40" que substituirão o evento R-2070, esse campo possivelmente sofrerá alteração de regra de validação nesse momento.  [MFS17973] Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’  [MFS20930] Este campo deve ser gerado se período da apuração for menor ou igual a 31/10/2018  [ALTERAÇÃO MFS-90001] – Alteração de versão [ALTERAÇÃO MFS79876]  A partir da versão 2.1 2.1.1 do REINF este campo não deve ser mais gerado. | MFS-11898 MFS17973 MFS20930 MFS-79878 MFS-90001 |
| RN17 | Campo compSemMovto  [MFS17973/MFS20930] Caso estiver preenchido o campo “Comp. Sem Movto MM/AAAA” da tela de Geração Prévia do Movimentos será gravada a informação preenchida no mesmo. Caso na geração prévia dos movimentos o parâmetro “R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo será gravada a informação preenchida no campo “Comp. Sem Movto MM/AAAA” da tela de Geração Prévia do Movimentos se estiver preenchido.  Caso contrário, esse campo será gerado como nulo, sem informação.  [ALTERAÇÃO MFS-90001] – Alteração de versão [ALTERAÇÃO MFS79876]  A partir da versão 2.1 2.1.1 do REINF este campo não deve ser mais gerado. | MFS-11898 MFS17973 MFS20930 MFS-79878 MFS-90001 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
