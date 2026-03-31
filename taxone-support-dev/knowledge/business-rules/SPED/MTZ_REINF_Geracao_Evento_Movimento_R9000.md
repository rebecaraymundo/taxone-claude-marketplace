# MTZ_REINF_Geracao_Evento_Movimento_R9000

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R9000.docx






THOMSON REUTERS

Geração evento R-9000 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Registro ideEvento – Informações de Identificação do Evento









Registro ideContri – Informações de Identificação do Contribuinte






Registro infoExclusao – Registro que identifica o evento objeto da exclusão.







Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-11897 | Lara Aline | Definição de regras para geração do evento R-9000 Reinf |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-9000.  O evento R-9000 do SPED - REINF tem por objetivo tornar sem efeito os eventos, quando enviados indevidamente, seja como evento não periódico (R-3010), seja como um dos eventos periódicos (R-2010 a R-2070). Ele será gerado com os registros:   Reinf – EFD - Reinf  evtExclusao – Evento destinado a exclusão de eventos  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  infoExclusao – Registro que identifica o evento objeto da exclusão  Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx".   Origem das informações: Cadastro do Estabelecimento.   Regra de seleção: O Registro R-9000 é utilizado para informar a exclusão de algum evento enviado indevidamente.  Mensageria Log:   1 - Se o evento anterior do processo ainda não foi recebido com sucesso/advertência no fisco (IND_STATUS <> ‘3’) então exibir a seguinte mensagem:   Evento R-9000 – Exclusão de Eventos “Evento não pode ser excluído, enquanto não for recebido pelo fisco com sucesso ou advertência".  Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX  2 - Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda (IND_STATUS = 2 - “Evento REINF Enviado”) então exibir a seguinte mensagem:   Evento R-9000 – Exclusão de Eventos “A exclusão deste evento já foi executada e seu evento enviado ao Fisco, mas ainda aguarda retorno. Somente refazer esta operação caso o retorno seja erro.”  Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab: XXXXXX  3 - Se o evento já foi excluído e recebido com sucesso/advertência no fisco (IND_STATUS = ‘3’) então exibir a seguinte mensagem:   Evento R-9000 – Exclusão de Eventos “Evento já foi excluído. O Evento de Exclusão foi recebido pelo Fisco com sucesso ou advertência. Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX | MFS-11897 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtExclusao  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-11897 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1” | MFS-11897 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS-11897 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
