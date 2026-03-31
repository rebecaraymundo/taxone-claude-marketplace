# MTZ_REINF_Geracao_Evento_Movimento_R2060

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2060.docx






THOMSON REUTERS

Geração evento R-2060 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO





Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte



Registro IdeEstab – Identificação do Estabelecimento que Comercializou a Produção





Registro TipoCod – Identificação do Valor Total da Receita por Tipo de Código de Atividade Econômica






Registro nfs - Registro de Detalhamento da Receita Bruta




Registro tipoAjuste - Registro Tipo de Ajuste



Registro infoProc – Informações de processos relacionados a Suspensão da CPRB



Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-9074 | Geração Evento | Definição de regras para geração do evento R-2060 Reinf. |
| MFS-10589 | Geração Evento | Inclusão de Campo no Registro IdeEstab |
| MFS-12176 | Elenilson Coutinho | Regra para tipo de arquivo Original/Retificação |
| MFS-12180 | Elenilson Coutinho | Regra de geração considerando eventos de fechamento/reabertura |
| MFS14002 | Lara Aline | Alteração no layout conforme versão 1.2 |
| MFS14476 | Lara Aline | Inclusão de observação no campo codAjuste |
| MFS14461 | Lara Aline | Inclusão de regra de geração para o registro infoProc |
| MFS14129 | Lara Aline | Inclusão de regra para o campo observação do registro nfs. |
| MFS14997 | Lara Aline | Inclusão da informação da SAFX252 no registro tipoAjuste |
| MFS16053 | Lara Aline | Alteração no layout conforme versão 1.3 |
| MFS17138 | Lara Aline | Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura |
| MFS17269 | Lara Aline | Ajuste no campo VlrCPRBSuspTotal conforme nova versão 1.3.02. |
| MFS18674 | Lara Aline | Inclusão regra para sumarização dos valores do registro tipoCod |
| MFS18702 | Lara Aline | Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos |
| MFS18785 | Lara Aline | Ajuste na geração dos campos vlrExcRecBruta e vlrAdicRecBruta para recuperar da SAFX252. |
| MFS21178 | Lara Aline | Ajuste no campo vlrCPRBapur |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2060.  O evento R-2060 do SPED - REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária Sobre a Receita Bruta. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtCPRB – Evento da Contribuição Previdenciária Sobre a Receita Bruta- CPRB  ideEvento – Informações de Identificação do Evento  ideContrib – Informações de Identificação do Contribuinte  infoCPRB – Informações da Contribuição Previdenciária Sobre a Receita Bruta  ideEstab – Identificação do Estabelecimento  tipoCod – Registro que apresenta o valor total da receita por tipo de código de atividade econômica. [Alterado MFS14002] [MFS-10589]  nfs– Detalhamento do Receita Bruta  tipoAjuste – Tipo do ajuste da CPRB  infoProc – Informações de processos relacionados a Suspensão da CPRB  Observar orientações existentes no arquivo " "TR_REINF_DEXPARA_V2.1.1.xlsx".  Origem das informações: SAFX185, SAFX252 e SAFX2113  Regra de seleção: O Registro R-2060 é utilizado para demonstrar informações de Contribuição Previdenciária sobre a Receita Bruta - CPRB. Ele será gerado com base em Informações da tabela de Apuração da Contribuição Previdenciária sobre a Receita Bruta. Para obtermos as informações para sua geração, devemos recuperar registros da tabela SAFX185, SAFX252 e SAFX2113, considerando os seguintes critérios: - O COD_ESTAB seja de um estabelecimento indicado pelo usuário; - Os campos DATA_INI e DATA_FIM compreendam o período informado pelo usuário;    [MFS-12176]  Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:  Se não houver ocorrência de geração de evento anterior, criar uma nova ocorrência de arquivo original.  Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:                Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB               Evento não gerado. Existe evento anterior enviado aguardando retorno.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:  - Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação.  - Se existir, evento de exclusão considerar os status, então:  Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:                 Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB              Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX            Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência           anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar uma ocorrência de arquivo de retificação, se não houver, criar original.                - Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar uma ocorrência de retificação.               - Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:                                Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB               Evento não gerado. Existe evento anterior não enviado.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  uma ocorrência de arquivo de retificação, se não houver, criar original.  Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar uma ocorrência de arquivo de retificação, se não houver, criar original.  [MFS18702] Importante: Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.  [MFS-12180]              Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.  Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.  Se houver ocorrência de geração de evento de fechamento considerar os status então:                        - Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:                                          Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB                   Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                        - Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte                         mensagem no log de geração:                                    Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB                   Evento não gerado. Período Fechado.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com Sucesso ou Advertência”, prosseguir com a geração.                 [Alterado MFS17138]         - Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do             XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:                     Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB                    Evento não gerado. Período Fechado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                      Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,                    prosseguir com a geração.                          - Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de                             geração:                     Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta - CPRB                    Evento não gerado. Existe evento de fechamento do período não enviado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX | MFS-9074 MFS-10589 MFS-12176 MFS12180 MFS14002 MFS14461 MFS17138 MFS18702 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evttCPRB  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS9074 |
| RN02 | Campo TpInsc  Será gerado com conteúdo "1", uma vez que não atendemos PF. | MFS14821 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS14821 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN02 | Origem das informações: Cadastro do Estabelecimento e SAFX185  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInscEstab, nrInscEstab  Nível hierárquico do registro: filho do registro infoCPRB  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Para cada infoCPRB poderá existir “N” ideEstab | MFS-9074 |
| RN03 | Campo tpInsEstab  Será gerado com conteúdo igual a “1” | MFS9074 |
| RN04 | nrInscEstab  Será Gerado com o conteúdo do campo “CGC” do Cadastro do Estabelecimento informado na SAFX185. | MFS9074 |
| RN05 | VlrRecBrutaTotal  Será gerado com o conteúdo do campo “VLR_REC_BRT” da SAFX185 | MFS9074 |
| RN06 | VlrCPApurTotal  Será gerado com a somatória do conteúdo do campo “VLR_CONT_PREV_REINF” da SAFX185. | MFS9074 |
| RN07 | VlrCPRBSuspTotal  Será gerado com a somatória do conteúdo do campo “VLR_PREV_EXIG_SUSP” da SAFX2113, com exceção dos valores informados com o Indicador de Suspenção (ind_susp) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão (SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos) através do campo Código de Suspensão (COD_SUSP) informado na SAFX2113. | MFS14461 MFS17269 |
| RN08 | tpProcesso | MFS9074 MFS14002 |
| RN09 | nrProcesso | MFS9074 MFS14002 |
| RN10 | codSusp | MFS10589 MFS14002 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN11 | Origem das informações: SAFX185, Aba Ajustes (Tela de “Contribuição Previdenciária da Receita da Bruta”)  Regra de seleção: Este registro servirá identificar valor total da receita por tipo de código de atividade econômica.  Campos-Chave: codAtivEcon  Nível hierárquico do registro: filho do registro ideEstab.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada ideEstabPrest poderá existir “N” tipoCod | MFS9074 |
| RN12 | Campo codAtivEcon   Será gerado com o conteúdo do campo “COD_ATIV_CONT_PREV” da SAFX185 | MFS9074 |
| RN13 | Campo vlrRecBrutaAtiv  Será gerado com o conteúdo do campo VLR_REC_BRT_ATIV da SAFX185, sumarizado por Atividade (campo COD_ATIV_CONT_PREV). | MFS9074 MFS18674 |
| RN14 | Campo vlrExcRecBruta  Será gerado com o conteúdo do campo “VL_AJ_REINF” quando “IND_AJ_REINF = 0 - Ajuste de redução” da SAFX252, sumarizado por Atividade (campo COD_ATIV_CONT_PREV). Caso não preenchido gravar “0”. | MFS9074 MFS18674 MFS18785 |
| RN15 | vlrAdicRecBruta  Será gerado com o conteúdo do campo “VL_AJ_REINF” quando “IND_AJ_REINF = 1 - Ajuste de acréscimo” da SAFX252, sumarizado por Atividade (campo COD_ATIV_CONT_PREV). Caso não preenchido gravar “0”. | MFS9074 MFS18674 MFS18785 |
| RN16 | vlrBcCPRB  Será gerado com o conteúdo do campo “VLR_BASE_CONT_PREV_REINF” da SAFX185, sumarizado por Atividade (campo COD_ATIV_CONT_PREV). | MFS9074 MFS18674 |
| RN17 | Campo vlrCPRBapur  Será gerado com o conteúdo do campo “VLR_CONT_PREV_REINF” da SAFX185, sumarizado por Atividade (campo COD_ATIV_CONT_PREV).  [MFS21178] O valor deve ser truncado na segunda casa decimal. | MFS9074 MFS18674 MFS21178 |
| RN18 | Campo codAnaCont  Será tratado na geração do registro R-1000 | MFS9074 MFS14002 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN19 | Origem das informações: SAFX07 e SAFX09 (Notas fiscais que são apresentadas na aba "Detalhamento da Receita Bruta")  Regra de seleção: Este registro servirá para detalhar a receita bruta no nível de nota.  Campos-Chave: serie, numDocto  Nível hierárquico do registro: filho do registro tipoCod.  Ordenação: não se aplica.  Agrupamento: Não se aplica. [MFS10589] Ocorrência: para cada tipoCod poderá existir “N” nfs. | MFS9074 MFS10589 MFS14002 |
| RN20 | Campo serie  Será gerado com o conteúdo do campo SERIE_DOCFIS da SAFX07/09. Caso não preenchido gravar “0”. | MFS9074 MFS14002 |
| RN21 | Campo numDocto  Será gerado com a informação do campo NUM_DOCFIS da SAFX07/09. | MFS9074 MFS14002 |
| RN22 | Campo dtEmissaoNF  Será gerado com o conteúdo do campo DATA_EMISSAO da SAFX07/09. | MFS9074 MFS14002 |
| RN23 | Campo vlrBruto  Será gerado com o conteúdo do campo VALOR_PRODUTO da SAFX07. | MFS9074 MFS14002 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN24 | Origem das informações: Aba Ajustes (Tela de “Contribuição Previdenciária da Receita da Bruta”) (SAFX252)  Regra de seleção: Registro de Identificação do tipo de Ajuste  Campos-Chave: Não se aplica.  Nível hierárquico do registro: filho do registro tipoCod.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá não existir ou existir “N” tipoAjuste. | MFS9074 MFS14997 |
| RN25 | Campo tpAjuste  Será gerado com o conteúdo do campo “Tipo de Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada (SAFX252) | MFS9074 MFS14997 |
| RN26 | Campo codAjuste  Será gerado com o conteúdo do campo “Código de Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada (SAFX252)  Obs: Caso selecionado os códigos 11, 12, ou 13 deverá considerar sempre o código “11”, pois para EFD-REINF o código é genérico para as três situações. | MFS9074 MFS14476 MFS14997 |
| RN27 | Campo vlrAjuste  Será gerado com o conteúdo do campo “Valor do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada (SAFX252) | MFS9074 MFS14997 |
| RN28 | Campo descAjuste  Será gerada com o conteúdo do campo “Descrição do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada (SAFX252) | MFS9074 MFS14997 |
| RN29 | Campo dtAjuste  Será gerado com o conteúdo do campo “Data do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada (SAFX252) | MFS9074 MFS14997 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN30 | Origem das informações: SAFX2113, Aba Processos relacionados a Suspensão da CPRB (Tela de “Contribuição Previdenciária da Receita da Bruta”).  Regra de seleção: Este registro servirá para informar os processos relacionados a Suspensão da CPRB  Campos-Chave: nrProc  Nível hierárquico do registro: filho do registro tipoCod.  Ordenação: não se aplica.   Agrupamento: Não se aplica.  Ocorrência: para cada tipoCod poderá existir “50” infoProc | MFS14461 MFS16053 |
| RN31 | Campo tpProc  Será gerado com o conteúdo do campo “IND_TIP_PROC” da SAFX2113 | MFS14461 |
| RN32 | Campo nrProc  Será gerado com o conteúdo do campo “NUM_PROC” da SAFX2113. | MFS14461 |
| RN33 | Campo codSusp  Será gerado com o conteúdo do campo “COD_SUSP” da SAFX2113.   Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2060 - Registro: Informações de processos relacionados a Suspensão da CPRB “Campo Código do Indicativo da Suspensão deve ser numérico."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / Data Movimento: XXXX | MFS14461 |
| RN34 | Campo vlrCPRBSusp  Será gerado com o conteúdo do campo “VLR_PREV_EXIG_SUSP” da SAFX2113 | MFS14461 |
|  |  |  |
|  |  |  |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
