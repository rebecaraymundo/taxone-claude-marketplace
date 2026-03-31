# MTZ_REINF_Geracao_Evento_Cadastro_R1070

> Fonte: MTZ_REINF_Geracao_Evento_Cadastro_R1070.docx






THOMSON REUTERS

Geração evento R-1070 - REINF


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO

Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte



Registro InfoProcesso - Informações do processo (Inclusão)


Registro InfoProcesso/ideProcesso – Informação/Identificação do Processo (Inclusão)



Registro infoSusp – Informação de Suspensão de Exigibilidade de Tributos



Registro dadosProcJud - Informações Complementares do Processo Judicial



Registro InfoProcesso/IdePeriodo - Informações do processo (Alteração)





Registro InfoProcesso/ideProcesso – Informação/Identificação do Processo (Alteração)




Registro infoSusp – Informação de Suspensão de Exigibilidade de Tributos



Registro dadosProcJud - Informações Complementares do Processo Judicial




Registro novaValidade - Informações exclusiva em caso de alteração do período de validade de registro




Registro InfoProcesso/IdePeriodo - Informações do processo (Exclusão)



Registro ideProcesso – Identificação do Processo



Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS10757 | Elenilson Coutinho | Definição de regras para geração do evento de Cadastro R-1070 Reinf |
| MFS13810 | Lara Aline | Ajuste no Layout conforme v1.2 |
| MFS14930 | Lara Aline | Ajuste na geração do campo nrInsc |
| MFS15750 | Lara Aline | Ajuste no Layout conforme v1.3. |
| MFS17237 | Lara Aline | Ajuste na tag novaValidade e nos campos iniValid e fimValid da tag infoContri do tipo Alteração. |
| MFS10287 | Lara Aline | Ajuste no registro InfoProcesso/IdePeriodo - Informações do processo (Exclusão) |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-1070.  O evento R-1070 do SPED - REINF tem por objetivo gerar informações de Processo. Ele será gerado com os registros:  Reinf – EFD - Reinf evtTabProcesso – Evento Tabela de Processos ideEvento – Informações de Identificação do Evento ideContri – Informações de identificação do contribuinte infoProcesso - Informações do Processo inclusão - Inclusão de novas informações idePeriodo - Período de validade das informações incluídas ideProcesso - Informações de identificação do Processo e validade das informações que estão sendo incluídas infoSusp - Informações de Suspensão de Exibilidade de tributos dadosProcJud - Informações Complementares do Processo Judicial alteração - Alteração das informações idePeriodo - Período de validade das informações alteradas ideProcesso - informações de identificação do processo infoSusp - Informações de Suspensão de Exibilidade de tributos dadosProcJud - Informações Complementares do Processo Judicial novaValidade - Novo período de validade das informações exclusão - Exclusão das informações idePeriodo - Período de validade das informações excluídas ideProcesso - Exclusão de processo   Observar orientações existentes no arquivo "TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: SAFX2058, SAFX2059 e Cadastro do Estabelecimento.  Regra de seleção: O Registro R-1070 é utilizado para demonstrar informações de Processos. Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX2058 e SAFX2059 se campo IND_REINF = “S”.  Mensageria Log:   Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda (status 2 - “Evento REINF Enviado”) então exibir a seguinte mensagem:         Evento R1070 – Tabela de Processos Administrativos/Judiciais      “Evento não gerado. Existe evento anterior que foi enviado e ainda aguarda retorno.” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXX   Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco. Não posso gerar evento de exclusão, então exibir a seguinte mensagem:           Evento R1070 – Tabela de Processos Administrativos/Judiciais       “Evento de exclusão não gerado. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência.” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXXX | MFS-10757 MFS-13810 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtTabProcesso  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-10757 |
| RN02 | Campo tpInsc  Será gerado com conteúdo igual a “1”. | MFS-10757 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. | MFS14821 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN02 | Origem das informações: SAFX2058  Regra de seleção: Este registro servirá identificar o período de validade das informações de Processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “I”  Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro inclusao.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 MFS13810 |
| RN03 | Campo iniValid  Informação será recuperada do campo VALID_PROC_ADJ_INI da SAFX2058. | MFS10757 MFS13810 |
| RN04 | Campo fimValid  Informação será recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058. | MFS10757 MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN06 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá identificar o processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “I”  Campos-Chave: tpProc, nrProc, iniValid, fimValid  Nível hierárquico do registro: filho do registro Inclusão  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 MFS13810 |
| RN07 | Campo tpProc  Informação será recuperada do campo IND_TP_PROC_ADJ da SAFX2058 | MFS10757 |
| RN08 | Campo nrProc  Informação será recuperada do campo NUM_PROC_ADJ da SAFX2058. | MFS10757 |
| RN09 | Campo iniValid  Informação será recuperada do campo VALID_PROC_ADJ_INI da SAFX2058. | MFS13810 |
| RN10 | Campo fimValid  Informação será recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058. | MFS13810 |
| RN11 | Campo indAutoria  Recuperar a informação do campo IND_AUTORIA da SAFX2058. | MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN12 | Origem das informações: SAFX2059.  Regra de seleção: Este registro servirá para identificar as informações de Suspensão de exigibilidade de Tributos. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “I”  Campos-Chave: codSusp  Nível hierárquico do registro: filho do registro ideProcesso.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada ideProcesso poderá existir “50” infoSusp. | MFS10757 |
| RN13 | Campo codSusp  Informação será recuperada do campo COD_SUSP da SAFX2059. | MFS10757 |
| RN14 | Campo indSusp  Informação será recuperada do campo IND_SUSP da SAFX2059. | MFS10757 |
| RN15 | Campo dtDecisao  Informação será recuperada do campo DAT_DECISAO da SAFX2059. | MFS10757 |
| RN16 | Campo indDeposito  Informação será recuperada do campo IND_DEPOSITO da SAFX2059. | MFS10757 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN17 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá para identificar as informações Complementares do Processo Judicial. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “I”  Campos-Chave:   Nível hierárquico do registro: filho do registro ideProcesso  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir. | MFS10757 |
| RN18 | Campo ufVara  Informação será recuperada do campo COD_ESTADO da SAFX2058.  Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial “Campo UF Seção Judiciária do cadastro de processos não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 |
| RN19 | Campo codMunic  Informação será recuperada do campo COD_MUNICIPIO da SAFX2058.  [ALTERADO MFS15750] Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial “Campo Código Município não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 MFS15750 |
| RN20 | Campo idVara  Informação será recuperada do campo COD_VARA da SAFX2058.  Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial  “Campo Identificação da Vara do cadastro de processos não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 |
| RN18 | Campo indAutoria  Recuperar a informação do campo IND_AUTORIA da SAFX2058. | MFS10757 MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN02 | Origem das informações: SAFX2058  Regra de seleção: Este registro servirá identificar o período de validade das informações de Processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “A”  Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro Alteracao.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 MFS13810 |
| RN20 | Campo iniValid  Informação será recuperada do campo VALID_PROC_ADJ_INI da SAFX2058. | MFS10757 MFS13810 |
| RN21 | Campo fimValid  Informação será recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058. | MFS10757 MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN21 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá identificar o processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “A”  Campos-Chave: tpProc, nrProc, iniValid, fimValid  Nível hierárquico do registro: filho do registro alteracao  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 MFS13810 |
| RN22 | Campo tpProc  Informação será recuperada do campo IND_TP_PROC_ADJ da SAFX2058 | MFS10757 |
| RN23 | Campo nrProc  Informação será recuperada do campo NUM_PROC_ADJ da SAFX2058 | MFS10757 |
| RN24 | Campo iniValid  [Alterado MFS17237] A informação recuperada do campo VALID_PROC_ADJ_INI da SAFX2058 será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. | MFS13810 MFS17237 |
| RN25 | Campo fimValid  [Alterado MFS17237] A informação recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058 será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar. A informação nova alterada será gerada no Registro novaValidade. | MFS13810 MFS17237 |
| RN26 | Campo indAutoria  Recuperar a informação do campo IND_AUTORIA da SAFX2058. | MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN27 | Origem das informações: SAFX2059.  Regra de seleção: Este registro servirá para identificar as informações de Suspensão de exigibilidade de Tributos. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “A”  Campos-Chave: codSusp  Nível hierárquico do registro: filho do registro ideProcesso.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada ideProcesso poderá existir “50” infoSusp. | MFS10757 |
| RN28 | Campo codSusp  Informação será recuperada do campo COD_SUSP da SAFX2059. | MFS10757 |
| RN29 | Campo indSusp  Informação será recuperada do campo IND_SUSP da SAFX2059. | MFS10757 |
| RN30 | Campo dtDecisao  Informação será recuperada do campo DAT_DECISAO da SAFX2059. | MFS10757 |
| RN31 | Campo indDeposito  Informação será recuperada do campo IND_DEPOSITO da SAFX2059. | MFS10757 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN32 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá para identificar as informações Complementares do Processo Judicial. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “A”  Campos-Chave:   Nível hierárquico do registro: filho do registro ideProcesso  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir. | MFS10757 |
| RN33 | Campo ufVara  Informação será recuperada do campo COD_ESTADO da SAFX2058. Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial  “Campo UF Seção Judiciária do cadastro de processos não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 |
| RN34 | Campo codMunic  Informação será recuperada do campo COD_MUNICIPIO da SAFX2058.  [ALTERADO MFS15750] Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial “Campo Código Município não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 MFS15750 |
| RN35 | Campo idVara  Informação será recuperada do campo COD_VARA da SAFX2058.  Caso campo não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R1070 – Registro Informações Complementares do Processo Judicial  “Campo Identificação da Vara do cadastro de processos não preenchido” Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX | MFS10757 |
| RN36 | Campo indAutoria  Recuperar a informação do campo IND_AUTORIA da SAFX2058. | MFS10757 MFS13810 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN36 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá para identificar as informações de alteração do período de validade do registro. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado.  Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro Alteracao  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir 1 ou não existir. | MFS10757 MFS17237 |
| RN37 | Campo iniValid  Informação será recuperada do campo VALID_PROC_ADJ_INI da SAFX2058. | MFS10757 |
| RN38 | Campo fimValid  Informação será recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058. | MFS10757 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN39 | Origem das informações: SAFX2058  Regra de seleção: Este registro servirá identificar o período de validade das informações de Processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “E”   Campos-Chave: iniValid, fimValid  Nível hierárquico do registro: filho do registro exclusao.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 |
| RN40 | Campo iniValid  Informação será recuperada do campo VALID_PROC_ADJ_INI da SAFX2058. | MFS10757 |
| RN41 | Campo fimValid  Informação será recuperada do campo VALID_PROC_ADJ_FIM da SAFX2058. | MFS10757 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN42 | Origem das informações: SAFX2058.  Regra de seleção: Este registro servirá identificar o processo. Será gerado considerando os seguintes critérios: Tabela REINF_PGER_R1070_OC campo “IND_OPER” igual a “E”. Esse registro será gerado se o usuário efetuar uma exclusão das Informações de Suspensão de Exigibilidade de Tributos (SAFX2059) tanto manualmente pela tela de cadastro no Módulo DW (Manutenção > Códigos > Processo Administrativo Judicial (REINF/eSocial)) como também pela exclusão efetuada pelo módulo Ferramentas (Rotinas Acessórias > Inicialização > Exclusão Processo Administrativo Judicial (REINF/eSocial)).   Campos-Chave: tpProc, nrProc  Nível hierárquico do registro: filho do registro exclusao  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Um por arquivo. | MFS10757 MFS10287 |
| RN43 | Campo tpProc  Informação será recuperada do campo IND_TP_PROC_ADJ da SAFX2058 | MFS10757 |
| RN44 | Campo nrProc  Informação será recuperada do campo NUM_PROC_ADJ da SAFX2058 | MFS10757 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
