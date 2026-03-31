# MTZ_REINF_Geracao_Evento_Movimento_R2020

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2020.docx






THOMSON REUTERS

Geração evento R-2020 - REINF


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO


Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte



Registro IdeEstabPrest – Identificação do Estabelecimento Prestador de Serviços





Registro ideTomador – Identificação dos Tomadores dos Serviços



Registro nfs - Registro de Detalhamento das notas fiscais de serviços prestados pela empresa


Registro infoTpServ - Registro de Informações do Tipo de Serviço


Registro infoProcRetPr - Registro de Informações de Processo Retenção Principal




Registro infoProcRetAd - Registro de Informações de Processo Retenção Adicional










Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-8959 | Geração Evento | Definição de regras para geração do evento R-2020 Reinf |
| MFS-10414 | Alteração | Alteração/ Inclusão de registros |
| MFS-11895 | Lara Aline | Inclusão mensagens de logs RN06, 54, 55, 56, 59, 60 e 61. |
| MFS-12176 | Elenilson Coutinho | Regra para tipo de arquivo Original/Retificação |
| MFS-12180 | Elenilson Coutinho | Regra de geração considerando eventos de fechamento/reabertura |
| MFS-13205 | Lara Aline | Ajuste nos campos vlrServicos15, vlrServicos20 e vlrServicos25 para recuperar informação dos novos campos da SAFX09. |
| MFS13631 | Lara Aline | Exclusão dos campos codAnaCont, vlrMatEquip, vlrDedAlim, vlrDedTrans e codAtivEcon e ajuste na ocorrência do grupo ideTomador. Conforme Leiautes versão 1.2. |
| MFS14404 | Lara Aline | Ajuste para considerar o campo “Desconsiderar NFs sem Valor de Retenção informado” da tela de Dados Iniciais |
| MFS14129 | Lara Aline | Inclusão de regra para o campo observação do registro nfs. |
| MFS16568 | Lara Aline | Ajuste no campo vlrBruto (RN26) |
| MFS17043 | Lara Aline | Ajuste no campo numDocto (RN21) |
| MFS17138 | Lara Aline | Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura |
| MFS16936 | Lara Aline | Inclusão de regra para as parametrizações de Retenção Previdenciárias. |
| MFS17919 | Lara Aline | Inclusão de tratamento para empresa que possuam Operação de transporte de passageiros |
| MFS18702 | Lara Aline | Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos |
| MFS19169 | Lara Aline | Ajuste na mensagem de log dos campos vlrBaseRet e vlrRetencao. |
| MFS20384 | Lara Aline | Incluisão de log quando encontrar valor negativo nas notas fiscais. |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2020.  O evento R-2020 do SPED - REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária - Prestadores de Serviços. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtServPrest – Evento de Serviços Prestados  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  infoServPrest – Serviços Prestados (Cessão Mão de Obra ou Empreitada)  ideEstabPrest – Registro de Identificação do Estabelecimento Prestador de Serviços mediante cessão de mão de obra  ideTomador -  Identificação dos Tomadores dos Serviços  nfs - Notas Fiscais de Serviços (CMO) - Emitidas por Terceiros  [MFS10414]   InfoTpServ – Informações do Tipo de Serviços Constantes da Nota Fiscal  InfoProcRetPr – Informações de Processo de Retenção Principal  InfoProcRetAd – Informações de Processo de Retenção Adicional   Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx ".  Origem das informações: SAFX04, SAFX07, SAFX09 e Cadastro do Estabelecimento.  Regra de seleção: O Registro R-2020 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária - Prestadores de Serviços. Ele será gerado com base em Informações de Notas Fiscais de Serviço. Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07 e SAFX09, considerando os seguintes critérios:  - O COD_ESTAB seja de um estabelecimento indicado pelo usuário; - NFs cujo campo MOVTO_E_S seja igual a "9"; - O campo DATA_EMISSAO deve compreender o período de geração; - O campo SITUACAO deve ser diferente de "S"; - O campo COD_CLASS_DOC_FIS deve ser igual a "2" ou "3" ou "4" ou "5" ou “6”; - O COD_SERVICO deve ter sido associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF;  Tratamento:  [MFS20384] Caso encontrado valores negativos (-) nos campos de valores das notas recuperadas (SAFX07/SAFX09), a geração não será finalizada e será exibido a seguinte mensagem no log de geração:         Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados        ‘A geração não foi concluída pois foi encontrado campo com valor negativo, favor verificar’.        Empresa/Estabelecimento: XX / XXXXX / Identificação do Nota: NF: XXXXX / Serie: XXXXXX        Identificação do Campo: XXXXXX   Caso o sistema encontre notas que correspondem aos critérios acima e o campo COD_CLASS_DOC_FIS seja igual a "4" ou "5" ou “6” essas notas serão consideradas como Operações de transporte de passageiros:  Tratamento para Operações de transporte de passageiros  Origem das informações: SAFX07, SAFX263 e Cadastro do Estabelecimento.  Regra de seleção: O Registro R-2020 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária - Prestadores de Serviços. Ele será gerado com base em Informações de Notas Fiscais de Serviço no caso de Operações de transporte de passageiros, como nesse caso não possui item a origem das informações se faz pela SAFX07 e origem dos processos pela SAFX263. Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07, considerando os seguintes critérios:  SAFX07: - O COD_ESTAB seja de um estabelecimento indicado pelo usuário; - NFs cujo campo MOVTO_E_S seja igual a "9"; - O campo DATA_EMISSAO deve compreender o período de geração; - O campo SITUACAO deve ser diferente de "S"; - O campo COD_CLASS_DOC_FIS deve ser igual a "4" ou "5" ou “6”; - NFs com Modelo do Documento igual a: 2E - Bilhete de Passagem emitido por ECF 07 - Nota Fiscal de Serviço de Transporte 67 - Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS 63 - Bilhete de Passagem Eletrônico - BP-e 16 - Bilhete de Passagem Ferroviário 57 - Conhecimento de Transporte Eletrônico – CT-e 13 - Bilhete de Passagem Rodoviário 14 - Bilhete de Passagem Aquaviário 15 - Bilhete de Passagem e Nota de Bagagem - Os campos VLR_BASE_INSS  e VLR_INSS_RETIDO devem ser maior que zero;  Fim regra de seleção para Operações de transporte de passageiros.   Regra de Agrupamento: O Registro R-2020 será agrupado por CPF_CGC da SAFX04.  [Alterado MFS16936] Regra para as parametrizações de Retenção Previdenciária: As parametrizações de Retenção Previdenciária são possíveis efetua-las para qualquer Estabelecimento sendo ou não o Estabelecimento Centralizador, por padrão deverá ser utilizada a parametrização do estabelecimento Centralizador para todos os estabelecimentos que não possuam sua parametrização. Para os estabelecimentos que possuem parametrização na geração será considerada a sua parametrização conforme exemplo abaixo:  Exemplo: Estabelecimento Centralizador: REINFP – Possui ‘parametrização 1’ Estabelecimento Centralizado: REINF1 – Possui ‘parametrização 2’ Estabelecimento Centralizado: REINF2 – Não possui parametrização  1 - Na geração dos dados do Estabelecimento Centralizador REINFP utilizaremos a ‘parametrização 1’; 2 - Na geração dos dados do Estabelecimento Centralizado REINF1 utilizaremos a ‘parametrização 2’; 3 - Na geração dos dados do Estabelecimento Centralizado REINF2 utilizaremos a ‘parametrização 1’;  Importante: Para os estabelecimentos que possuírem grupos diferentes do Estabelecimento Centralizador esses estabelecimentos somente serão considerados se houver a sua própria parametrização. Caso contrário todas as notas desse estabelecimento centralizado não serão consideradas na geração.    [Alterado MFS14404] Importante: Caso o campo “Desconsiderar NFs sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais, deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS (VLR_BASE_INSS/SAFX09) e o Valor de INSS Retido (VLR_INSS_RETIDO/SAFX09) informado. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado.   [MFS-12176]  Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:  Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original.  Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:                Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados               Evento não gerado. Existe evento anterior enviado aguardando retorno.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:  - Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação.  - Se existir, evento de exclusão considerar os status, então:  Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:                 Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados              Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX            Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência           anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova           ocorrência de arquivo de  retificação, se não houver, criar original.                - Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação.               - Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:                                Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados               Evento não gerado. Existe evento anterior não enviado.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.  Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.  [MFS18702] Importante: Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.  [MFS-12180]  Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.  Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.  Se houver ocorrência de geração de evento de fechamento considerar os status então:                        - Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:                                          Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados                   Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                        - Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte                         mensagem no log de geração:                                    Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados                   Evento não gerado. Período Fechado.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com Sucesso ou Advertência”, prosseguir com a geração.                  [Alterado MFS17138]        - Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do             XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:                     Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados                    Evento não gerado. Período Fechado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                      Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,                    prosseguir com a geração.                          - Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de                             geração:                     Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados                    Evento não gerado. Existe evento de fechamento do período não enviado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX | MFS-8959 MFS10414 MFS12176 MFS12180 MFS14404 MFS17138 MFS16936 MFS17919 MFS18702 MFS20384 MFS-90001 |


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
|  | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtServPrest  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo |  |
| RN02 | Campo TpInsc  Será gerado com conteúdo "1", uma vez que não atendemos PF. | MFS14821 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento.  Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador.  Obs:  Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 - Registro : Informações de Identificação do Contribuinte “Campo Número de Inscrição tem tamanho inferior a 14 posições."  Identificação do Contribuinte: CNPJ: XXXXX / Nome/Razão: XXXX | MFS14821 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInscEstabPrest, nrInscEstabPrest  Nível hierárquico do registro: filho do registro infoServPrest  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Para cada infoServPrest poderá existir “N” ideEstabPrest | MFS-8959 |
| RN02 | Campo tpInscricao  Gerar com conteúdo igual a “1”. | MFS-8959 |
| RN03 | Campo nrInscricao  Gerar com o conteúdo do campo “CGC” do Cadastro do Estabelecimento da Nota Fiscal. | MFS-8959 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN04 | Origem das informações: SAFX04, SAFX07 e SAFX09.  Regra de seleção: Este registro servirá identificar o estabelecimento "Tomador" de Serviços  Campos-Chave: tpInscTomador, nrInscTomador  Nível hierárquico do registro: filho do registro ideEstabPrest.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  [Alteração MFS13631] Ocorrência: Um por arquivo. para cada ideEstabPrest poderá existir “N” ideTomador | MFS8959 MFS13631 |
| RN05 | Campo tplnscTomador  Este campo será gerado com a seguinte regra:  Se o campo IND_PREST_SERV da SAFX07 for diferente de "1" ou "2", gerar "1". Se o campo IND_PREST_SERV da SAFX07 for igual a "1" ou "2", gerar "4".  Obs:  Caso não preenchido assumir o valor “1”. Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 – Registro: Identificação dos Tomadores de Serviços “Campo Indicador de Prestação de Serviço da Nota não preenchido, assumido o valor “1” para o campo Tipo de Inscrição do registro”. Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8959 |
| RN06 | Campo nrlnscTomador  Este campo será gerado com a seguinte regra:  Se o campo IND_PREST_SERV da SAFX07 for diferente de "1" ou "2", será gerado com o conteúdo do campo CPF_CGC da SAFX04 vinculada a NF.  Obs:  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 - Registro: Identificação dos Tomadores de Serviços  “Campo CPF_CGC não preenchido“.  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Se o campo IND_PREST_SERV da SAFX07 for igual a "1" ou “2”, será gerado com o conteúdo do campo COD_CEI da SAFX07   Obs1: Caso o campo COD_CEI não preenchido exibir a seguinte mensagem no log de pré-geração:   Evento R2020 – Registro Identificação dos Tomadores de Serviços “Campo COD_CEI da Nota Fiscal não preenchido” Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Obs2: Caso o campo IND_PREST_SERV não preenchido assumir o conteúdo do campo “CPF_CGC” da SAFX04. Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 – Registro: Identificação dos Tomadores de Serviços  “Campo Indicador de Prestação de Serviço da Nota não preenchido, assumido o “CPF_CGC” do cadastro da Pessoa Física/Jurídica para o campo Número de Inscrição Tomador do registro”. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX [ALTERADA MFS11895] Obs3: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 – Registro: Identificação dos Tomadores de Serviços  “Campo Número de Inscrição tem tamanho inferior a 14 posições." Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8959 MFS11895 |
| RN07 | Campo indObra  Este campo será gerado com a informação carregada no campo IND_PREST_SERV da SAFX07.  Obs:  Caso o campo IND_PREST_SERV não preenchido, assumir o valor “0”. Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 – Registro: Identificação dos Tomadores de Serviços  “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o valor “0” para o campo Indicador de Obra do registro. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXXX / Serie: XXXXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8959 |
| RN08 | vlrTotalBruto  Será resultado da somatória do campo VLR_TOT da SAFX09 informado na nota detalhada no registro “nfs”  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_TOT_NOTA da SAFX07 informado na nota detalhada no registro “nfs” | MFS8959 MFS17919 |
| RN09 | Campo vlrTotalBaseRet  Será resultado da somatória do campo VLR_BASE_INSS da SAFX09 informado na nota detalhada no registro “infoTpServ”  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_BASE_INSS da SAFX07 informado na nota detalhada no registro “infoTpServ” | MFS8959 MFS17919 |
| RN10 | Campo vlrTotalRetPrinc  Será resultado da somatória do campo VLR_INSS_RETIDO – VLR_RET_SERV da SAFX09 informado na nota detalhada no registro “infoTpServ”  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_INSS_RETIDO – VLR_RET_SERV da SAFX07 informado na nota detalhada no registro “infoTpServ” | MFS8959 MFS17919 |
| RN11 | Campo vlrTotalRetAdic  Será resultado da somatória do campo VLR_TOT_ADIC da SAFX09 informado na nota detalhada no registro “infoTpServ”  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_TOT_ADIC da SAFX07 informado na nota detalhada no registro “infoTpServ” | MFS8959 MFS17919 |
| RN12 | Campo vlrTotalNRetPrinc  Será resultado da somatória do campo VLR_N_RET_PRINC da SAFX09 informado na nota detalhada no registro “infoTpServ”  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_N_RET da SAFX263, somatório do valor informado no campo vlrNRetPrinc na tag “infoTpServ” | MFS8959 MFS17919 |
| RN13 |  | MFS8959 |
| RN14 |  | MFS8959 |
| RN15 | Campo vlrTotalINRetAdic  Será o resultado da somatória do campo “VLR_N_RET_ADIC” das notas fiscais de serviço detalhadas na tag “infoTpServ”.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será resultado da somatória do campo VLR_N_RET da SAFX263, somatório do valor informado no campo vlrNRetAdic na tag “infoTpServ” | MFS8959 |
| RN16 |  | MFS8959 |
| RN17 |  | MFS8959 |
| RN18 | Campo codAnaCont | MFS8959 MFS13631 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN19 | Origem das informações: SAFX07 e SAFX09.  Regra de seleção: Este registro servirá para identificar as notas fiscais de serviços prestados pela empresa declarada no registro ideTomador.  Campos-Chave: serie, numDocto  Nível hierárquico do registro: filho do registro ideTomador.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada ideTomador poderá existir “N” nfs. | MFS8959 |
| RN20 | Campo serie  Informação será recuperada do campo SERIE_DOCFIS da SAFX09. Caso não preenchido gravar “0”.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Informação será recuperada do campo SERIE_DOCFIS da SAFX07. Caso não preenchido gravar “0”. | MFS8959 MFS17919 |
| RN21 | Campo NumDocto   Informação será recuperada inicialmente do campo NUM_DOCFIS_SERV da SAFX07, caso não encontrar valor preenchido será recuperada a informação do campo NUM_DOCFIS da SAFX09.  Obs: Caso número da nota for maior que 15 posições a informação será truncada, utilizando as 15 ultimas posições da direita para esquerda.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Informação será recuperada do campo NUM_DOCFIS da SAFX07. | MFS8959 MFS17043 MFS17919 |
| RN22 | Campo dtEmissaoNF  Informação será recuperada do campo DATA_EMISSAO da SAFX07. | MFS8959 |
| RN23 | Campo vlrBruto  Informação será recuperada do campo VLR_TOT da SAFX09. Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Informação será recuperada do campo VLR_TOT_NOTA da SAFX07. | MFS8959 MFS16568 MFS17919 |
| RN24 |  | MFS8959 MFS10414 |
| RN25 | Campo obs  Informação será recuperada do campo OBS_REINF da SAFX07. | MFS8959 MFS14129 |
| RN26 |  | MFS8959 MFS10414 |
| RN27 |  | MFS8959 MFS10414 |
| RN28 |  | MFS8959 MFS10414 |
| RN29 |  | MFS8959 MFS10414 |
| RN30 |  | MFS8959 MFS10414 |
| RN31 |  | MFS8959 MFS10414 |
| RN32 |  | MFS8959 MFS10414 |
| RN33 |  | MFS8959 MFS10414 |
| RN34 |  | MFS8959 MFS10414 |
| RN35 |  | MFS8959 MFS10414 |
| RN36 |  | MFS8959 MFS10414 |
| RN37 |  | MFS8959 MFS10414 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN38 | Origem das informações: SAFX07, SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – (Tela de “Documento Fiscal”).  Regra de seleção: Este registro servirá para identificar os tipos de serviços constantes da nota fiscal.  Campos-Chave: tpServico  Nível hierárquico do registro: filho do registro nfs  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada nfs poderá existir “9” infoTpServ. | MFS10414 MFS17919 |
| RN39 | Campo tpServico  Caso o código do serviço prestado fora parametrizado na tela de “Identificação do Tipo de Serviço” Menu: Retenções Previdenciárias >> Parâmetros, gerar o código do tipo de serviço vinculado.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Será gerado fixo com o código “100000024” - Operações de transporte de passageiros. | MFS10414 MFS17919 |
| RN40 | Campo codAtivEcon  Caso o código do serviço prestado fora parametrizado na tela de “Código de Atividade x Serviços” Menu: CPRB >> Parâmetros, gerar o código de atividade econômica vinculado. | MFS10414 MFS13631 |
| RN41 | Campo vlrMatEquip  Será a somatória dos campos VLR_MAT_PROP + VLR_MAT_TERC da SAFX09. Caso não preenchido gravar “0”. | MFS10414 MFS13631 |
| RN42 | Campo vlrDedAlim  Recuperar a informação do campo VLR_DED_ALIM da SAFX09. Caso não preenchido gravar “0”. | MFS10414 MFS13631 |
| RN43 | Campo vlrDedTrans  Recuperar a informação do campo VLR_DED_TRANS da SAFX09. Caso não preenchido gravar “0”. | MFS10414 MFS13631 |
| RN44 | Campo vlrBaseRet  Recuperar a informação do campo VLR_BASE_INSS da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_BASE_INSS da SAFX07.  Obs: [MFS19169] Caso não preenchido e o campo “Desconsiderar NFs sem Valor de Retenção informado” NÃO estiver selecionado na tela de Dados Iniciais deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 - Registro: Notas Fiscais de Serviços “Campo Valor Base de Cálculo da Retenção do INSS não preenchido“.  Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXX / Serie: XXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX Item de Serviço: XXXXXX | MFS10414 MFS17919 MFS19169 |
| RN45 | Campo vlrRetencao  Recuperar a informação do campo VLR _INSS_RETIDO da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR _INSS_RETIDO da SAFX07.  Obs:  [MFS19169] Caso não preenchido e o campo “Desconsiderar NFs sem Valor de Retenção informado” NÃO estiver selecionado na tela de Dados Iniciais deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2020 - Registro: Notas Fiscais de Serviços “Campo Valor da Retenção do INSS não preenchido“ Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX Item de Serviço: XXXXX | MFS10414 MFS17919 MFS19169 |
| RN46 | Campo vlrRetSub  Recuperar a informação do campo VLR_RET_SERV da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_RET_SERV da SAFX07. | MFS10414 MFS17919 |
| RN47 | Campo vlrNRetPrinc  Recuperar a informação do campo VLR_N_RET_PRINC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_N_RET da SAFX263, valor informado no campo valorPrinc detalhadas na tag “infoProcRetPr” | MFS10414 MFS17919 |
| RN48 | Campo vlrServicos15  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “15 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_15 da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_SERV_15 da SAFX07. | MFS10414 MFS13205 MFS17919 |
| RN49 | Campo vlrServicos20  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “20 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_20 da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_SERV_20 da SAFX07. | MFS10414 MFS13205 MFS17919 |
| RN50 | Campo vlrServicos25  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “25 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_25 da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_SERV_25 da SAFX07. | MFS10414 MFS13205 MFS17919 |
| RN51 | Campo vlrAdicional  Recuperar a informação do campo VLR_TOT_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_TOT_ADIC da SAFX07. | MFS10414 MFS17919 |
| RN52 | Campo vlrNRetAdic  Recuperar a informação do campo VLR_N_RET_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_N_RET da SAFX263, valor informado no campo valorAdic detalhadas na tag “infoProcRetAd” | MFS10414 MFS17919 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN53 | Origem das informações: SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – (Tela de “Documento Fiscal”).  Regra de seleção: Este registro servirá para identificar os processos de retenção principal relacionados a não retenção da contribuição previdenciária.   Campos-Chave: tpProcRetPrinc, nrProcRetPrinc, codSuspPrinc  Nível hierárquico do registro: filho do registro ideTomador.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir “50” infoProcRetAd ou não existir | MFS10414 MFS17919 |
| RN54 | Campo tpProcRetPrinc  Recuperar a informação do campo IND_TP_PROC_ADJ_PRINC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo IND_TP_PROC_ADJ para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘1 - Principal’ da SAFX263.  [ALTERADO MFS11895] Obs:  Caso o tipo de processo informado seja ‘3’ deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 - Registro: Informações de Processo Retenção Principal “O tipo de processo não poderá ser ‘3’, não corresponde a um valor válido."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN55 | Campo nrProcRetPrinc  Recuperar a informação do campo NUM_PROC_ADJ_PRINC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo NUM_PROC_ADJ para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘1 - Principal’ da SAFX263.  ALTERADO MFS118958] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro: Informações de Processo Retenção Adicional “Campo Número do Processo deve ser numérico." Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN56 | Campo codSuspPrinc  Recuperar a informação do campo COD_SUSP_PRINC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo COD_SUSP para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘1 - Principal’ da SAFX263.  [ALTERADO MFS11895] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 - Registro: Informações de Processo Retenção Principal “Campo Código do Indicativo da Suspensão deve ser numérico.""  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN57 | Campo valorPrinc  Recuperar a informação do campo VLR_N_RET_PRINC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_N_RET para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘1 - Principal’ da SAFX263. | MFS10414 MFS17919 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN58 | Origem das informações: SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – (Tela de “Documento Fiscal”).  Regra de seleção: Este registro servirá para identificar os processos de retenção adicional relacionados a não retenção da contribuição previdenciária.   Campos-Chave: tpProcRetAdic, nrProcRetAdic, codSuspAdic  Nível hierárquico do registro: filho do registro ideTomador.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: poderá existir “50” infoProcRetAd ou não existir | MFS10414 MFS17919 |
| RN59 | Campo tpProcRetAdic  Recuperar a informação do campo IND_TP_PROC_ADJ_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo IND_TP_PROC_ADJ para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘2 - Adicional’ da SAFX263.  [ALTERADO MFS11895] Obs:  Caso o tipo de processo informado seja ‘3’ deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 - Registro: Informações de Processo Retenção Adicional “O tipo de processo não poderá ser ‘3’, não corresponde a um valor válido."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN60 | Campo nrProcRetAdic  Recuperar a informação do campo NUM_PROC_ADJ_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo NUM_PROC_ADJ para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘2 - Adicional’ da SAFX263.  ALTERADO MFS11895] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro: Informações de Processo Retenção Adicional “Campo Número do Processo deve ser numérico." Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN61 | Campo codSuspAdic  Recuperar a informação do campo COD_SUSP_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo COD_SUSP para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘2 - Adicional’ da SAFX263.  [ALTERADO MFS11895] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2020 - Registro: Informações de Processo Retenção Adicional “Campo Código do Indicativo da Suspensão deve ser numérico."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10414 MFS11895 MFS17919 |
| RN62 | Campo valorAdic  Recuperar a informação do campo VLR_N_RET_ADIC da SAFX09.  Caso a nota se enquadrar em Operações de transporte de passageiros (RN00): Recuperar a informação do campo VLR_N_RET para o Indicador de Processo (IND_PRINC_ADIC) igual a ‘2 - Adicional’ da SAFX263. | MFS10414 MFS17919 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
