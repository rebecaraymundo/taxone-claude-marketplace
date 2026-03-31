# MTZ_REINF_Geracao_Evento_Movimento_R2098

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2098.docx






THOMSON REUTERS

Geração evento R-2098 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte






Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-11898 | Lara Aline | Definição de regras para geração do evento R-2098 Reinf |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2098.  O evento R-2098 do SPED - REINF tem por objetivo informar a reabertura do movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtReabreEvPer – Evento de reabertura de eventos periódicos  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx ".  Origem das informações: Cadastro do Estabelecimento.   Regra de seleção: O Registro R-2098 é utilizado para informar a reabertura do movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos.   Mensageria Log:   1 - Verificar se dentro do período de apuração existe algum evento periódico nas tabelas de ocorrência com IND_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R-2098 – Reabertura e exibir a seguinte mensagem:  Evento R-2098 – Reabertura dos Eventos Periódicos “Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXX  2 - Verificar se já foi efetuada a geração e envio do evento R-2098 – Reabertura para esse período de apuração, caso ainda não tenha retorno (IND_STATUS = 2), exibir a seguinte mensagem:  Evento R-2098 – Reabertura dos Eventos Periódicos “A reabertura do período já foi executada e seu evento enviado ao Fisco, mas ainda aguarda retorno. Somente refazer esta operação, caso o retorno seja erro.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX | MFS-11898 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtFechaEvPer   Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-11898 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1” | MFS-11898 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS-11898 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
