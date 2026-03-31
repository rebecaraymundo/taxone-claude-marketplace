# MTZ_REINF_Geracao_Evento_Movimento_R4099

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R4099.docx






THOMSON REUTERS

Geração evento R-4099 - REINF

DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte




Registro ideRespInf – Responsável pelas informações





Registro infoFech – Informações do Fechamento.




Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:





| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-79914 | Alessandra Cristina Navatta | Definição de regras para geração do evento R-4099 Reinf (2.1) |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-4099.  O evento R-4099 do SPED - REINF tem por objetivo informar o encerramento da transmissão dos eventos da série 40 na EFD-Reinf, no período de apuração. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtFech – Evento de Fechamento  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  ideRespInf – Responsável pelas informações   infoFech –Fechamento/reabertura do PA reativo às retenções na fonte  Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: Tela de Dados Iniciais, Cadastro do Estabelecimento, Geração dos Eventos R-4010 a R4080.   Regra de seleção: O Registro R-4099 é utilizado para informar o fechamento ou reabertura da transmissão dos eventos da família 40 na EFD-Reinf, no período de apuração. Caso na geração prévia dos movimentos o parâmetro “R-4099 – Fechamento/reabertura dos eventos da séria 40” estiver selecionado esse evento também será gerado, porém apenas se existir eventos da série 40 no período (R-4010 a R-4080).   Mensageria Log:   1 - Verificar se dentro do período de apuração existe algum evento periódico da família 40 nas tabelas de ocorrência com IND_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R-4099 - Fechamento/reabertura dos eventos da série R-4000 e exibir a seguinte mensagem:   Evento R-4099 - Fechamento/reabertura dos eventos da série R-4000 “Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX   2 - Verificar se já foi efetuada a geração e envio do evento R-4099 - Fechamento/reabertura dos eventos da série R-4000 para esse período de apuração, caso ainda não tenha retorno (IND_STATUS = 2), exibir a seguinte mensagem:  Evento R-4099 - Fechamento/reabertura dos eventos da série R-4000 “O fechamento do período já foi executado e seu evento enviado ao Fisco, mas ainda aguarda retorno. Somente refazer esta operação, caso o retorno seja erro.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX | MFS-79914 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtFech  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-79914 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1” | MFS-79914 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS-79914 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN04 | Origem das informações: Tela de Dados Iniciais   Regra de seleção: Este registro servirá identificar o responsável pelas informações  Campos-Chave: nmResp, cpfResp  Nível hierárquico do registro: filho do registro evtFech.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir | MFS-79914 |
| RN05 | Campo nmResp  Informação será recuperada do campo Nome da tela de “Dados Iniciais”. | MFS-79914 |
| RN06 | Campo cpfResp  Informação será recuperada do campo CPF da tela de “Dados Iniciais”. | MFS-79914 |
| RN07 | Campo telefone  Informação será recuperada do campo Telefone, caso não preenchido será recuperado do campo Celular da tela de “Dados Iniciais”. | MFS-79914 |
| RN08 | Campo email  Informação será recuperada do campo Email da tela de “Dados Iniciais”. | MFS-79914 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN09 | Origem das informações: Eventos R-4010 ao R-4080  Regra de seleção: Este registro apresenta as informações do Fechamento.  Nível hierárquico do registro: filho do registro evtFech  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-79914 |
| RN10 | Campo fetcRet  Informação a ser gravada nesse campo:  Fechamento Reabertura   Na primeira geração do evento, deve ser gravado ‘0’, depois, se for enviado novamente o evento R-4099, este campo deve ser gerado com ‘1’. | MFS-79914 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
