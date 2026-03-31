# MTZ_REINF_Geracao_Evento_Cadastro_R1050

> Fonte: MTZ_REINF_Geracao_Evento_Cadastro_R1050.docx






THOMSON REUTERS

Geração evento R-1050- Tabela de Entidades Ligada
REINF


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO

Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte

Registro InfoLig – Informações Relacionadas a Entidades Ligadas



Registro Alteração – Alteração de Informações



Registro Nova Validade – Nova Validade das Informações

Registro exclusao – Exclusão de Informações


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-79881 | Alessandra Cristina Navatta | Geração do Evento R-1050 – Tabela de Entidades Ligadas (atendimento ao layout versão 2.1) |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-1050.  O evento R-1050 do SPED - REINF tem por objetivo gerar informações de tabela de entidades ligadas. Ele será gerado com os registros:  Reinf – EFD - Reinf evtTabLig – Evento Tabela de Entidades Ligadas ideEvento – Informações de Identificação do Evento ideContri – Informações de identificação do contribuinte infoLig - Informações relacionadas a entidades ligadas inclusao - Inclusão de novas informações ideEntLig – Identificação da entidade ligada alteracao - Alteração das informações ideEntLig – Identificação da entidade ligada novaValidade - Novo período de validade das informações que estão sendo alteradas exclusao - Exclusão das informações ideEntLig – Identificação da entidade ligada   Observar orientações existentes no arquivo “TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: Tela Tabela de Entidades Ligadas  Regra de seleção: O Registro R-1050 é utilizado para demonstrar informações da tabela de entidades ligadas. Para obtermos as informações para sua geração, devemos recuperar as informações da tela “Tabela de Entidades Ligadas”, considerando o registro vigente da tabela de entidade, ou seja, data inicial e final de validade da tabela entidade deve estar compreendida no período de geração do REINF .  Mensageria Log:   Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda (status 2 - “Evento REINF Enviado”) então exibir a seguinte mensagem:         Evento R1050 – Tabela de Entidades Ligadas      “Evento não gerado. Existe evento anterior que foi enviado e ainda aguarda retorno.” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXX   Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco. Não posso gerar evento de exclusão, então exibir a seguinte mensagem:           Evento R1050 – Tabela de Entidades Ligadas       “Evento de exclusão não gerado. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência.” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXXX | MFS-79881 MFS-90001 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN01 | Origem das informações: Tela Informações do Contribuinte.  Regra de seleção: Este registro servirá para identificar o Contribuinte  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtTabLig  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-10757 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1”. | MFS-79881 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. | MFS-79881 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN04 | Origem das informações: Tela Tabela de Entidades Ligadas  Nível hierárquico do registro: filho do registro evtTabLig  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-79881 |
| RN05 | Campo tpEntLig  Informação será recuperada do campo ‘Classificação da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN06 | Campo cnpjLig  Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN07 | Campo iniValid  Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN08 | Campo fimValid  Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN09 | Origem das informações: Tela Tabela de Entidades Ligadas.  Nível hierárquico do registro: filho do registro infoLig  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-79881 |
| RN10 | Campo tpEntLig  Informação será recuperada do campo ‘Classificação da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN11 | Campo cnpjLig  Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN12 | Campo iniValid  Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN13 | Campo fimValid  Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN14 | Origem das informações: Tela Tabela de Entidades Ligadas.  Regra de seleção: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração das informações do contribuinte quanto à data inicio e/ou fim validade, este será considerado como um novo cadastro, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.   Campos-Chave:   Nível hierárquico do registro: filho do registro alteracao  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-79881 |
| RN15 | Campo iniValid  Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN16 | Campo fimValid  Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN17 | Origem das informações: Tela Tabela de Entidades Ligadas.  Regra de seleção: Este registro servirá identificar o período de validade das informações de Entidades Ligadas. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1050_OC campo “IND_OPER” igual a “E”   Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro InfoLig  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Até um por arquivo. | MFS-79881 |
| RN18 | Campo cnpjLig  Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN19 | Campo iniValid  Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |
| RN20 | Campo fimValid  Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’. | MFS-79881 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
