# MTZ_REINF_Geracao_Evento_Cadastro_R1000

> Fonte: MTZ_REINF_Geracao_Evento_Cadastro_R1000.docx






THOMSON REUTERS

Geração evento R-1000 - REINF


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO

Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte









Registro InfoContri


Registro infoCadastro – Informações do Contribuinte



Registro Contato – Informações de Contato



Registro softHouse – Informações da empresa desenvolvedora das aplicações.


Registro infoEFR – Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR




Registro novaValidade - Informações exclusiva em caso de alteração do período de validade de registro




Registro IdePeriodo - Informações do processo (Exclusão)


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-10819 | Elenilson Coutinho | Definição de regras para geração do evento de Cadastro R-1000 Reinf |
| MFS14930 | Lara Aline | Ajuste na geração do campo nrInsc |
| MFS15750 | Lara Aline | Ajuste no Layout conforme v1.3. |
| MFS17237 | Lara Aline | Ajuste na tag novaValidade e nos campos iniValid e fimValid da tag infoContri do tipo Alteração. |
| MFS18226 | Lara Aline | Inclusão regra para geração do evento R-1000 de Limpeza para o Tipo de Ambiente = Produção Restrita. |
| MFS20215 | Lara Aline | Ajuste no campo foneFixo (RN16) |
| MFS-81450 | Alessandra Cristina Navatta | Ajuste no Layout conforme V2.1  Atualização do documento, referenciando a tela “Informações do Contribuinte” ao invés da tela de “Dados Iniciais” nos registros Informações de Identificação do Contribuinte, InfoContri, infoCadastro – Informações do Contribuinte; Contato – Informações de Contato, softHouse – Informações da empresa desenvolvedora das aplicações, novaValidade - Informações exclusiva em caso de alteração do período de validade de registro e IdePeriodo - Informações do processo (Exclusão) |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação |
| MFS-523048 | Alessandra Cristina Navatta | Inclusão da regra do campo indUniao (inclusão e alteração) |
| MFS-840399 | Alessandra Cristina Navatta | Inclusão da regra do campo indPertIRRF (inclusão e alteração), para atendimento do evento R-1000, versão 2.1.2 (Nota Técnica 02/2025) |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-1000.  O evento R-1000 do SPED - REINF tem por objetivo gerar informações de Processo. Ele será gerado com os registros:  Reinf – EFD - Reinf evtInfoContri – Evento de informações do Contribuinte ideEvento – Informações de Identificação do Evento ideContri – Informações de identificação do contribuinte infoContri - Informações do Processo inclusão - Inclusão de novas informações idePeriodo - Período de validade das informações incluídas infoCadastro - Informações do Contribuinte contato - Informações de contato softHouse - Informações da empresa desenvolvedora da aplicação que gera os arquivos infoEFR - Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR (não geramos essa TAG) alteracao - Alteração das informações idePeriodo - Período de validade das informações alteradas infoCadastro - Informações do contribuinte contato - Informações de contato softHouse - Informações da empresa desenvolvedora da aplicação que gera os arquivos infoEFR - Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR (não geramos essa TAG)   novaValidade - Novo período de validade das informações exclusão - Exclusão das informações idePeriodo - Período de validade das informações excluídas  Observar orientações existentes no arquivo "TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: Tela de Cadastro de Informações do Contribuinte  Regra de seleção: O Registro R-1000 é utilizado para demonstrar informações do Contribuinte Para obtermos as informações para sua geração, devemos recuperar as informações da tela de “Informações do Contribuinte”  Mensageria Log:   Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda (status 2 - “Evento REINF Enviado”) então exibir a seguinte mensagem:    Evento R1000 – Informações do Contribuinte “Evento não gerado. Existe evento anterior que foi enviado e ainda aguarda retorno.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX   Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco. Não posso gerar evento de exclusão, então exibir a seguinte mensagem:     Evento R1000 – Informações do Contribuinte “Evento de exclusão não gerado. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência.” Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód. do Estab.: XXXXXX  MFS-18226]  Limpeza da Base de Pré-Produção: Critérios de geração do evento:  O evento R-1000 de limpeza será responsável por apagar todos os dados de determinado contribuinte, ou seja, todos os eventos já gerados ou enviados do contribuinte com sucesso ou não serão excluídos do governo, mensageria e DW. Porém apenas se o Tipo de Ambiente for 2 – Produção Restrita para o contribuinte que o usuário desejar excluir os dados. Dessa forma o critério principal para possibilidade de geração desse evento é o Tipo de Ambiente = 2 – Produção Restrita.  Critério para apresentar o evento de Limpeza R-1000 no Painel de Controle de Eventos:  1 - O evento R-1000 de Limpeza será apresentado no painel de controle de eventos para geração apenas se existir um evento R-1000 com a situação Evento Recebido pelo fisco com sucesso/advertência e o Tipo de Ambiente = 2 – Produção Restrita de acordo com os dados pesquisados no Parâmetro para consulta, ou seja, apenas se o governo já recebeu a informação cadastral de determinado contribuinte. Nesse caso o evento R-1000 de Limpeza será demostrado com a situação Aguardando Geração de XML no Painel.  2 - O evento R-1000 de Limpeza será demostrado no painel se o evento R-1000 de ‘Limpeza’ já tiver sido recebido pelo fisco com sucesso (Situação: Evento Recebido pelo fisco com sucesso/advertência) nesse caso irá aparecer no painel apenas para consulta do usuário (Histórico).  Esse evento de Limpeza será igual a um evento de R-1000 original de inclusão, com a diferença de existir uma tag <verProc>RemoverContribuinte</verProc>  A geração/envio do evento R-1000 de Limpeza é possível para o status abaixo:  1 - Aguardando Geração do XML.  Abaixo será listado os status que será possível efetuar outro envio e geração do evento, caso ocorra algum erro na primeira tentativa de envio/geração:  14 - Evento Excluído na Mensageria; 4 - Erro na Geração do XML;  15 - Erro Técnico na Mensageria; 6 - Evento Rejeitado pela Mensageria; 10 - Evento Rejeitado pelo Fisco. | MFS-10819 MFS18226 MFS-81450 MFS-90001 |


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
| RN01 | Origem das informações: Tela de “Informações do Contribuinte”.  Regra de seleção: Este registro servirá para identificar o Contribuinte.  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtInfoContri  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-10819 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1”. | MFS-10819 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. | MFS14821 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN04 | Origem das informações: Tela de “Informações do Contribuinte”.   Regra de seleção: Este registro servirá para identificar informações do Contribuinte. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1000_OC campo “IND_OPER” igual a “I” (Inclusão) e “A” (Alteração)  Campos-Chave:   Nível hierárquico do registro: filho do registro evtInfoContri.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-10819 |
| RN05 | Campo iniValid  Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”. .  [Alterado MFS17237] Importante: Para o tipo de arquivo = ‘Alteração’ (campo “IND_OPER” igual a “A” - Alteração): Nesse caso a informação recuperada do campo Início Validade da tela de “Informações do Contribuinte” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. | MFS-10819 MFS17237 |
| RN06 | Campo fimValid  Informação será recuperada do campo Fim Validade da Tela de “Informações do Contribuinte”. .  [Alterado MFS17237] Importante: Para o tipo de arquivo = ‘Alteração’ (campo “IND_OPER” igual a “A” - Alteração): Nesse caso a informação recuperada do campo Início Validade da tela de  “Informações do Contribuinte” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. | MFS-10819 MFS17237 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN07 | Origem das informações: Tela de Informações do Contribuinte. Regra de seleção: Este registro servirá para identificar informações do Contribuinte. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1000_OC campo “IND_OPER” igual a “I” (Inclusão) e “A” (Alteração)  Campos-Chave:   Nível hierárquico do registro: filho do registro Inclusão  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-10819 MFS-81450 |
| RN08 | Campo ClassTrib  Informação será recuperada do campo Classificação Tributária da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN09 | indEscrituracao  Informação será recuperada do campo Escrituração Contábil na ECD da Tela de “Informações do Contribuinte” | MFS-10819 MFS-81450 |
| RN10 | indDesoneracao  Informação será recuperada do campo Desoneração da Folha da Tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN11 | indAcordoIsenMulta  Informação será recuperada do campo Acordo de Isenção de Multa da Tela de “Informações do Contribuinte”.  [ALTERADO MFS15750] Caso preenchido ‘1 – Com acordo’ e o campo ClassTrib for preenchido com valor diferente de ‘60’ exibir a seguinte mensagem no log de pré-geração:  Evento R1000 – Registro Informações do Contribuinte “Campo ’Indicativo da existência de acordo internacional para isenção de multa’ só pode ser igual a ‘1’ se campo ‘Classificação Tributária’ for igual a ‘60’” Identificação do Contribuinte: Número de Inscrição: XXXXXXXXXXXX | MFS-10819 MFS15750 MFS-81450 |
| RN12 | indSitPJ  Informação será recuperada do campo Situação Pessoa Jurídica da Tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN12.1 | indUniao  Este campo passa a existir no REINF, a partir da versão 2.1 2.1.1 do REINF. [ALTERAÇÃO MFS-523048] - Informação será recuperada do campo Indicativo de Entidade Vinculada a União’ da Tela de “Informações do Contribuinte”.Caso o campo esteja sem informação na tela, não gerar este campo.  Campo não Obrigatório | MFS-81450 MFS-90001 MFS-523048 |
| RN12.2 | dtTransfFinsLucr  Este campo passa a existir no REINF, a partir da versão 2.1 2.1.1 do REINF. Informação será recuperada do campo ‘Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos - Art. 13 - Lei 11096/2005.’ da Tela de “Informações do Contribuinte”.   Campo não Obrigatório | MFS-81450 MFS-90001 |
| RN12.3 | dtObito  Este campo passa a existir no REINF, a partir da versão 2.1 2.1.1 do REINF.  Este campo só deve ser informado, quando tpInsc do contribuinte for igual a [2], como não geramos essa opção, não preencher este campo.  Campo não Obrigatório | MFS-81450 MFS-90001 |
| RN12.4 | Este campo passa a existir no REINF, a partir da versão 2.1.2 do REINF. Informação será recuperada do campo Pertencimento do IRRF da Tela de “Informações do Contribuinte”,  se o campo estiver marcado gravar ‘S’, caso contrário, não gravar nada.   Campo não Obrigatório | MFS-840399 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN13 | Origem das informações: Tela de “Informações do Contribuinte”.  Regra de seleção: Este registro servirá para identificar informações do Contribuinte. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1000_OC campo “IND_OPER” igual a “I” (Inclusão) e “A” (Alteração).  Campos-Chave: codSusp  Nível hierárquico do registro: filho do registro infoCadastro.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por Arquivo. | MFS-10819 MFS-81450 |
| RN14 | Campo nmCtt  Informação será recuperada do campo Nome do Contato da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN15 | Campo cpfCtt  Informação será recuperada do campo CPF da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN16 | Campo foneFixo  Informação será recuperada do campo Telefone da tela de “Informações do Contribuinte”.  [MFS20215] Obs: Caso número de telefone seja maior que 10 posições a informação será truncada no XML, utilizando as 10 ultimas posições da direita para esquerda. | MFS-10819 MFS20215 MFS-81450 |
| RN17 | Campo foneCel  Informação será recuperada do campo Celular da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN18 | Campo email  Informação será recuperada do campo email da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN19 | Origem das informações: Tela Informações do Contribuinte  Regra de seleção: Este registro servirá para identificar informações do Contribuinte. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1000_OC campo “IND_OPER” igual a “I” (Inclusão) e “A” (Alteração).  Campos-Chave:   Nível hierárquico do registro: filho do registro infoCadastro  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir nenhum ou 99. | MFS-10819 MFS-81450 |
| RN20 | Campo cnpjSoftHouse   Informação será recuperada do campo CNPJ da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN21 | Campo nmRazao  Informação será recuperada do campo Nome/Razão da tela de “Informações do Contribuinte”.. | MFS-10819 MFS-81450 |
| RN22 | Campo nmCont  Informação será recuperada do campo Nome do contato da tela de  “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN23 | Campo telefone  Informação será recuperada do campo telefone da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN24 | Campo email  Informação será recuperada do campo E-mail da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN24 | Esta tag não é gerada pelo sistema, pois, não temos clientes de Órgãos Públicos | MFS-81450 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN25 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração das informações do contribuinte quanto à data inicio e/ou fim validade, este será considerado como um novo cadastro, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.   Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro Alteracao  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir. | MFS-10819 MFS17237 |
| RN26 | Campo iniValid  Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN27 | Campo fimValid  Informação será recuperada do campo Fim Validade da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |


| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN28 | Origem das informações: SAFX2058  Regra de seleção: Este registro servirá para identificar informações do Contribuinte. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1000_OC campo “IND_OPER” igual a “E”.   Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro exclusao.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS-10819 |
| RN29 | Campo iniValid  Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |
| RN30 | Campo fimValid  Informação será recuperada do campo Fim Validade da tela de “Informações do Contribuinte”. | MFS-10819 MFS-81450 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
