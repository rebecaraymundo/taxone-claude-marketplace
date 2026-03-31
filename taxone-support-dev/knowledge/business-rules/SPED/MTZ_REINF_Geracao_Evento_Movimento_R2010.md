# MTZ_REINF_Geracao_Evento_Movimento_R2010

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2010.docx






THOMSON REUTERS

Geração evento R-2010 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO


Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte



Registro ideEstabObra – Identificação do Estabelecimento /Obra Contratante dos Serviços



Registro idePrestServ – Identificação do Prestador de Serviços Mediante cessão de mão de obra ou empreitada



Registro nfs - Registro de Detalhamento das notas fiscais de serviços prestados pela empresa




Registro infoTpServ - Registro de Informações do Tipo de Serviços




Registro infoProcRetPr - Registro de Informações de Processo Retenção Principal


Registro infoProcRetAd - Registro de Informações de Processo Retenção Adicional

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-8958 | Elenilson Coutinho | Definição de regras para geração do evento R-2010 Reinf |
| MFS-10357 | Elenilson Coutinho | Alteração/ Inclusão de registros |
| MFS-11894 | Lara Aline | Inclusão mensagens de logs RN03, 06, 09, 59, 60, 64 e 65. |
| MFS-12176 | Elenilson Coutinho | Regra para tipo de arquivo Original/Retificação |
| MFS-12180 | Elenilson Coutinho | Regra de geração considerando eventos de fechamento/reabertura |
| MFS-13131 | Elenilson Coutinho | Alteração na geração considerando parametrização de Código de Atividade x Serviços Por Prestador |
| MFS-13205 | Lara Aline | Ajuste nos campos vlrServicos15, vlrServicos20 e vlrServicos25 para recuperar informação dos novos campos da SAFX09. |
| MFS13362 | Lara Aline | Exclusão dos campos codAnaCont, vlrMatEquip, vlrDedAlim, vlrDedTrans e codAtivEcon e ajuste na ocorrência do grupo idePrestServ. Conforme Leiautes versão 1.2. |
| MFS13947 | Lara Aline | Ajuste no campo nrInscEstab. |
| MFS14222 | Lara Aline | Ajuste para considerar o campo “Desconsiderar NFs sem Valor de Retenção informado” da tela de Dados Iniciais |
| MFS14463 | Lara Aline | Ajuste na geração do evento R-2010 para receber informações de notas de serviço de transporte (SAFX08) |
| MFS14129 | Lara Aline | Inclusão de regra para o campo observação do registro nfs. |
| MFS15338 | Lara Aline | Ajuste para considerar o campo “Desconsiderar NFs fora da Competência” da tela de Geração Prévia dos Movimentos. |
| MFS16568 | Lara Aline | Ajuste no campo vlrBruto (RN26) |
| MFS17043 | Lara Aline | Ajuste no campo numDocto (RN24) |
| MFS17138 | Lara Aline | Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura |
| MFS17304 | Lara Aline | Ajuste campo indCPRB e inclusão regra de agrupamento por CPF_CGC da x04 |
| MFS16936 | Lara Aline | Inclusão de regra para as parametrizações de Retenção Previdenciárias. |
| MFS18702 | Lara Aline | Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos |
| MFS19130 | Lara Aline | Inclusão do modelo 55 para notas conjugadas. |
| MFS20045 | Lara Aline | Ajuste no campo indCPRB |
| MFS20384 | Lara Aline | Incluisão de log quando encontrar valor negativo nas notas fiscais. |
| MFS20732 | Lara Aline | Inclusão campo Período de Entrada das NFs. |
| MFS21130 | Lara Aline | Inclusão de mensagem de log para campo nrlnscEstab |
| MFS21632 | Lara Aline | Ajuste no parâmetro Período de Entrada das NFs. |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2010.  O evento R-2010 do SPED - REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária – Serviços Tomados. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtServTom – Evento de Serviços Tomados   ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  infoServTom – Ser. Tomados (Cessão Mão de Obra ou Empreitada)  ideEstabObra – Identificação do Estabelecimento/Obra Tomador dos Serviços  idePrestServ -  Identificação do prestador de servi-ços mediante cessão de mão de obra ou empreitada.  nfs - Notas Fiscais de Serviços (CMO) - Emitidas por Terceiros  [MFS10357]  infoTpServ - Informações sobre os tipos de Serviços constantes da NF infoProcRetPr – Informação de Processo Retenção Principal infoProcRetAd - Informação de Processo Retenção Adicional   Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx”  Origem das informações: SAFX04, SAFX07, SAFX08, SAFX09 e Cadastro do Estabelecimento.  Regra de seleção: O Registro R-2010 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária - Tomadores de Serviços. Ele será gerado com base em Informações de Notas Fiscais de Serviço. Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07, SAFX08 e SAFX09, considerando os seguintes critérios:  - O COD_ESTAB seja de um estabelecimento indicado pelo usuário;  - NFs cujo campo MOVTO_E_S seja diferente de "9"; - O campo DATA_EMISSAO deve compreender o período de geração. Caso na tela de Geração Prévia dos Movimentos o parâmetro “Desconsiderar NFs fora da Competência” estiver selecionado, o campo DATA_SAIDA_REC também deve compreender o período de geração. [MFS20732/MFS21632] - Caso o campo ‘Período de Entrada das NFs’ estiver preenchido, o campo DATA_EMISSAO e DATA_SAIDA_REC deve compreender o período de geração, mais as notas que o campo DATA_EMISSAO compreender o período de geração e que o campo DATA_SAIDA_REC compreender o período informado no campo Período de Entrada das NFs, ou seja, iremos recuperar todas as notas que a Data de Emissão e Data de Entrada/Saída da nota compreender o período de geração E as notas que a Data de Emissão compreender o período de geração e Data de Entrada/Saída da nota compreender o período informado no ‘Período de Entrada das NFs’. - O campo SITUACAO deve ser diferente de "S"; - Mercadoria : O campo COD_CLASS_DOC_FIS deve ser igual a "1" ou "3"; - Serviço : O campo COD_CLASS_DOC_FIS deve ser igual a "2" ou "3"; - O COD_SERVICO OU COD_PRODUTO deve ter sido associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF; - Para todas notas encontradas com o COD_PRODUTO associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF, deverão ser recuperadas APENAS as notas fiscais cujo COD_MODELO seja igual a ‘07’, ‘55’ ou ‘67’.  Regra de Agrupamento: O Registro R-2010 será agrupado por CPF_CGC da SAFX04.   Tratamento:  [MFS20384] Caso encontrado valores negativos (-) nos campos de valores das notas recuperadas (SAFX08/SAFX09), a geração não será finalizada e será exibido a seguinte mensagem no log de geração:         Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados        ‘A geração não foi concluída pois foi encontrado campo com valor negativo, favor verificar’.        Empresa/Estabelecimento: XX / XXXXX / Identificação do Nota: NF: XXXXX / Serie: XXXXXX        Identificação do Campo: XXXXXX   [Alterado MFS16936] Regra para as parametrizações de Retenção Previdenciária: As parametrizações de Retenção Previdenciária são possíveis efetua-las para qualquer Estabelecimento sendo ou não o Estabelecimento Centralizador, por padrão deverá ser utilizada a parametrização do estabelecimento Centralizador para todos os estabelecimentos que não possuam sua parametrização.  Para os estabelecimentos que possuem parametrização na geração será considerada a sua parametrização conforme exemplo abaixo:  Exemplo: Estabelecimento Centralizador: REINFP – Possui ‘parametrização 1’ Estabelecimento Centralizado: REINF1 – Possui ‘parametrização 2’ Estabelecimento Centralizado: REINF2 – Não possui parametrização  1 - Na geração dos dados do Estabelecimento Centralizador REINFP utilizaremos a ‘parametrização 1’; 2 - Na geração dos dados do Estabelecimento Centralizado REINF1 utilizaremos a ‘parametrização 2’; 3 - Na geração dos dados do Estabelecimento Centralizado REINF2 utilizaremos a ‘parametrização 1’;  Importante: Para os estabelecimentos que possuírem grupos diferentes do Estabelecimento Centralizador esses estabelecimentos somente serão considerados se houver a sua própria parametrização. Caso contrário todas as notas desse estabelecimento centralizado não serão consideradas na geração.     [Alterado MFS14222] Importante: Caso o campo “Desconsiderar NFs sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais, deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e/ou Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado.   [MFS-12176]  Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:  Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original.  Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:                Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados               Evento não gerado. Existe evento anterior enviado aguardando retorno.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX.  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:  - Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação.  - Se existir, evento de exclusão considerar os status, então:  Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:                 Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados              Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX            Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência           anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova           ocorrência de arquivo de  retificação, se não houver, criar original.                           - Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação.               - Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:                                Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados               Evento não gerado. Existe evento anterior não enviado.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.   Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.   [MFS18702] Importante: Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.  [MFS-12180]              Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.  Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.  Se houver ocorrência de geração de evento de fechamento considerar os status então:                        - Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:                                          Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados                   Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                        - Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte                         mensagem no log de geração:                                    Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados                   Evento não gerado. Período Fechado.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com Sucesso ou Advertência”, prosseguir com a geração.                   [Alterado MFS17138]        - Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do             XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:                     Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados                    Evento não gerado. Período Fechado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                      Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,                    prosseguir com a geração.                          - Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de                             geração:                     Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados                    Evento não gerado. Existe evento de fechamento do período não enviado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX | MFS-8958 MFS-10357 MFS-12176 MFS-12180  MFS14222  MFS14463 MFS15338 MFS17138 MFS17304 MFS16936 MFS18702 MFS19130 MFS20384 MFS20732 MFS21632 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInscTom, nrInscTom  Nível hierárquico do registro: filho do registro evtServTom  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS-8958 |
| RN02 | Campo TpInsc  Será gerado com conteúdo "1", uma vez que não atendemos PF. | MFS8958 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento.  Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador.  [ALTERADA MFS11894] Obs:  Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Informações de Identificação do Contribuinte “Campo Número de Inscrição tem tamanho inferior a 14 posições."  Identificação do Contribuinte: CNPJ: XXXXX / Nome/Razão: XXXX | MFS11894 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN04 | Origem das informações: SAFX04, SAFX07 e Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá identificar a obra ou estabelecimento "contratante" dos serviços prestados mediante cessão de mão de obra.  Campos-Chave: tpInscEstab, nrInscEstab  Nível hierárquico do registro: filho do registro infoServTom.  Ordenação: Não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada InfServTom poderá existir “N” IdeEstabObra. | MFS8958 |
| RN05 | Campo tplnsEstab  Este campo será gerado com a seguinte regra:  Se o campo IND_PREST_SERV da SAFX07 for diferente de "1" ou "2", gerar "1". Se o campo IND_PREST_SERV da SAFX07 for igual a "1" ou "2", gerar "4".  Obs:  Caso não preenchido assumir o valor “1”. Deverá apresentar a seguinte mensagem no log de pré-geração:    Evento R2010 - Registro Identificação do Estabelecimento/Obra Tomador de Serviços “Campo Indicador de Prestação de Serviço não preenchido, assumido o valor “1” para o campo Tipo de Inscrição do registro”. Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8958 |
| RN06 | Campo nrlnscEstab  Este campo será gerado com a seguinte regra:  Se o campo IND_PREST_SERV da SAFX07 for diferente de "1" ou "2", será gerado com o conteúdo do campo CGC do Cadastro do Estabelecimento da NF;  Se o campo IND_PREST_SERV da SAFX07 for igual a "1", será gerado com o conteúdo do campo CEI da SAFX04 da PFJ vinculada a NF;  Obs1: Caso o campo CEI não preenchido exibir a seguinte mensagem no log de pré-geração:   Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços “Campo CEI do cadastro Fis/Jur não preenchido” Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Se o campo IND_PREST_SERV da SAFX07 for igual a "0", será gerado com o conteúdo do campo CGC do Cadastro do Estabelecimento da NF;  Se o campo IND_PREST_SERV da SAFX07 for igual a "1 ou 2", será gerado com o conteúdo do campo COD_CEI da SAFX07;  Se o campo IND_PREST_SERV da SAFX07 for igual a "2", será gerado com o conteúdo do campo COD_CEI da SAFX07;  Obs2: Caso o campo COD_CEI não preenchido exibir a seguinte mensagem no log de pré-geração:  Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços “Campo COD_CEI da Nota não preenchido” Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Caso não preenchido o campo IND_PREST_SERV da SAFX07, gravar "0". Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços  “Campo Indicador de Prestação de Serviço da Nota não preenchido“. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  [ALTERADO MFS21130] Obs3: Caso a informação do campo seja maior que 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro: Identificação do Estabelecimento /Obra Contratante dos Serviços “'Número de Inscrição (Código CEI) maior que o permitido (14 posições)."  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX Inscrição: XXXXXXXX  Obs3: Caso o campo IND_PREST_SERV não preenchido assumir o conteúdo do campo “CGC” do cadastro do Estabelecimento. Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços  “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o “CGC” do Estabelecimento tomador dos serviços para o campo Número de Inscrição do registro. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  [ALTERADO MFS11894] Obs4: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Identificação do Estabelecimento /Obra Contratante dos Serviços “Campo Número de Inscrição tem tamanho inferior a 14 posições."  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8958 MFS11894 MFS13947 MFS21130 |
| RN07 | Campo indObra  Este campo será gerado com a informação carregada no campo IND_PREST_SERV da SAFX07.   Obs:  Caso o campo IND_PREST_SERV não preenchido, assumir o valor “0”. Deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 - Registro Identificação do Estabelecimento/Obra Tomador de Serviços  “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o valor “0” para o campo Indicador de Obra do registro. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXXX / Serie: XXXXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8958 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN08 | Origem das informações: SAFX04, SAFX08 e SAFX09.  Regra de seleção: Este registro servirá identificar o prestador de serviços mediante cessão de mão de obra ou empreitada.  Campos-Chave: cnpjPrestador  Nível hierárquico do registro: filho do registro ideEstabObra  Ordenação: não se aplica.  Agrupamento: Não se aplica.  [Alteração MFS13362] Ocorrência: Um por arquivo. Para cada ideEstabObra poderá existir “N” idePrestServ. | MFS8958 MFS13362 MFS14463 |
| RN09 | Campo cnpjPrestador  Será gerado com a informação do campo CPF_CGC da SAFX04 informado na nota detalhada no registro “nfs”  Obs1:  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 - Registro: Identificação do Prestador de Serviços  “Campo CPF_CGC não preenchido“.  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  [ALTERADO MFS11894] Obs2:  Obs4: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Identificação do Prestador de Serviços “Campo CNPJ Prestador tem tamanho inferior a 14 posições."  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS8958 MFS11894 |
| RN10 | vlrTotalBruto  Será resultado da somatória do campo VLR_ITEM da SAFX08 ou VLR_TOT da SAFX09 informado na nota detalhada no registro “nfs” | MFS8958 MFS14463 |
| RN11 | Campo vlrTotalBaseRet  Será resultado da somatória do campo VLR_BASE_INSS da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ” | MFS8958 MFS14463 |
| RN12 | Campo vlrTotalRetPrinc  Será resultado da somatória do campo VLR_INSS_RETIDO – VLR_RET_SERV da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ”. | MFS8958 MFS14463 |
| RN13 | Campo vlrTotalRetAdic  Será resultado da somatória do campo VLR_TOT_ADIC da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ” | MFS8958 MFS14463 |
| RN14 | Campo vlrTotalNRetPrinc  Será resultado da somatória do campo VLR_N_RET_PRINC da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ” | MFS8958 MFS14463 |
| RN15 |  | MFS8958 |
| RN16 |  | MFS8958 |
| RN17 | Campo vlrTotalINRetAdic  Será o resultado da somatória do campo “VLR_N_RET_ADIC” da SAFX08 ou SAFX09 informado na nota detalhadas na tag “infoTpServ”. | MFS8958 MFS14463 |
| RN18 |  | MFS8958 |
| RN19 |  | MFS8958 |
| RN20 | Campo codAnaCont  Será tratado na geração do registro R-1070 | MFS8958 MFS13362 |
| RN21 | Campo indCPRB  [MFS20045] Caso existir informação no campo VLR_ALIQ_INSS da SAFX08 ou SAFX09 considerar a regra abaixo:  [Alterado MFS13205/MFS17304] Se houver pelo menos uma nota com o campo VLR_ALIQ_INSS da SAFX08 ou SAFX09 = 3,5% gravar ‘1’ Se não, gravar ‘0’  Caso não existir informação no campo VLR_ALIQ_INSS da SAFX08 ou SAFX09 considerar a regra abaixo:  Gravar nulo e apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 - Identificação do Prestador de Serviços “Não foi possível gerar o indicativo da CPRB, pois o campo Alíquota INSS não está preenchido“.   Caso o código do serviço prestado fora parametrizado na tela de  Menu: Parâmetros, gerar “1”, caso contrário gerar “0” | MFS10357 MFS13131 MFS-13205 MFS14463 MFS17304 MFS20045 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN22 | Origem das informações: SAFX07, SAFX08 e SAFX09.  Regra de seleção: Este registro servirá para identificar as notas fiscais de serviços prestados pela empresa declarada no registro idePrestServ.  Campos-Chave: serie, numDocto  Nível hierárquico do registro: filho do registro idePrestServ.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada idePrestServ poderá existir “N” nfs. | MFS8958 MFS14463 |
| RN23 | Campo serie  Informação será recuperada do campo SERIE_DOCFIS da SAFX08 ou SAFX09. Caso não preenchido gravar “0”. | MFS8958 MFS14463 |
| RN24 | Campo NumDocto  Informação será recuperada inicialmente do campo NUM_DOCFIS_SERV da SAFX07, caso não encontrar valor preenchido será recuperada a informação do campo NUM_DOCFIS da SAFX08 ou SAFX09.  Obs: Caso número da nota for maior que 15 posições a informação será truncada, utilizando as 15 ultimas posições da direita para esquerda. | MFS8958 MFS14463 MFS17043 |
| RN25 | Campo dtEmissaoNF  Informação será recuperada do campo DATA_EMISSAO da SAFX07. | MFS8958 |
| RN26 | Campo vlrBruto  Informação será recuperada do campo VLR_ITEM da SAFX08 ou VLR_TOT da SAFX09. Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais. | MFS8958 MFS14463 MFS16568 |
| RN27 | Campo obs  Informação será recuperada do campo OBS_REINF da SAFX07. | MFS8958 MFS14129 |
| RN28 |  | MFS8958 |
| RN29 |  | MFS8958 |
| RN30 |  | MFS8958 |
| RN31 |  | MFS8958 |
| RN32 |  | MFS8958 |
|  |  | MFS8958 |
| RN33 |  | MFS8958 |
| RN34 |  | MFS8958 |
| RN35 |  | MFS8958 |
| RN36 |  | MFS8958 |
| RN37 |  | MFS8958 |
| RN38 |  | MFS8958 |
| RN39 |  | MFS8958 |
| RN40 |  | MFS8958 |
| RN41 |  | MFS8958 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN42 | Origem das informações: SAFX07, SAFX08 e SAFX09.  Regra de seleção: Este registro servirá para identificar os tipos de serviços constantes da nota fiscal.  Campos-Chave: tpServico  Nível hierárquico do registro: filho do registro nfs  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada nfs poderá existir “9” infoTpServ. | MFS10357 MFS14463 |
| RN43 | Campo tpServiço  Pela SAFX08: Caso o código do produto fora parametrizado na tela de “Identificador do Tipo de Serviço > Por Produto” Menu: Retenções Previdenciárias>> Parâmetros, gerar o código do tipo de serviço vinculado.  Pela SAFX09: Caso o código do serviço prestado fora parametrizado na tela de “Identificador do Tipo de Serviço” Menu: Retenções Previdenciárias>> Parâmetros, gerar o código do tipo de serviço vinculado. | MFS10357 MFS14463 |
| RN44 | Campo codAtivEcon  Caso o código do serviço prestado fora parametrizado na tela de  “Código de Atividade x Serviços (Por Prestador)” Menu: Parâmetros >> CPRB, gerar o código de atividade econômica vinculado. | MFS10357 MFS13131 MFS13362 |
| RN45 | Campo vlrMatEquip  Será a somatória dos campos VLR_MAT_PROP + VLR_MAT_TERC da SAFX09. Caso não preenchido gravar “0”. | MFS10357 MFS13362 |
| RN46 | Campo vlrDedAlim  Recuperar a informação do campo VLR_DED_ALIM da SAFX09. Caso não preenchido gravar “0”. | MFS10357 MFS13362 |
| RN47 | Campo vlrDedTrans  Recuperar a informação do campo VLR_DED_TRANS da SAFX09. Caso não preenchido gravar “0”. | MFS10357 MFS13362 |
| RN48 | Campo vlrBaseRet  Recuperar a informação do campo VLR_BASE_INSS da SAFX08 ou SAFX09.  Obs:  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 - Registro: Notas Fiscais de Serviços “Campo Valor Base de Cálculo da Retenção do INSS não preenchido“.  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Item de Serviço: XXXXXX | MFS10357 MFS14463 |
| RN49 | Campo vlrRetencao  Recuperar a informação do campo VLR _INSS_RETIDO da SAFX08 ou SAFX09.  Obs:  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2010 - Registro: Notas Fiscais de Serviços “Campo Valor da Retenção do INSS não preenchido“ Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  Item de Serviço: XXXXX | MFS10357 MFS14463 |
| RN50 | Campo vlrRetSub  Recuperar a informação do campo VLR_RET_SERV da SAFX08 ou SAFX09. | MFS10357 MFS14463 |
| RN51 | Campo vlrNRetPrinc  Recuperar a informação do campo VLR_N_RET_PRINC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |
| RN52 | Campo vlrServicos15  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “15 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_15 da SAFX08 ou SAFX09. | MFS10357 MFS13205 MFS14463 |
| RN53 | Campo vlrServicos20  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “20 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_20 da SAFX08 ou SAFX09. | MFS10357 MFS13205 MFS14463 |
| RN54 | Campo vlrServicos25  Será a somatória do campo VLR_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “25 anos“.  [Alteração MFS13205] Recuperar a informação do campo VLR_SERV_25 da SAFX08 ou SAFX09. | MFS10357 MFS13205 MFS14463 |
| RN55 | Campo vlrAdicional  Recuperar a informação do campo VLR_TOT_ADIC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |
| RN56 | Campo vlrNRetAdic  Recuperar a informação do campo VLR_N_RET_ADIC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN57 | Origem das informações: SAFX08 ou SAFX09.  Regra de seleção: Este registro servirá para identificar os processos de retenção principal relacionados a não retenção da contribuição previdenciária.   Campos-Chave: tpProcRetPrinc, nrProcRetPrinc, codSuspPrinc  Nível hierárquico do registro: filho do registro idePrestServ.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir “50” infoProcRetAd ou não existir | MFS10357 MFS14463 |
| RN58 | Campo tpProcRetPrinc  Recuperar a informação do campo IND_TP_PROC_ADJ_PRINC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |
| RN59 | Campo nrProcRetPrinc  Recuperar a informação do campo NUM_PROC_ADJ_PRINC da SAFX08 ou SAFX09.  [ALTERADO MFS11894] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Informações de Processo Retenção Principal “Campo Número do Processo deve ser numérico." Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10357 MFS11894 MFS14463 |
| RN60 | Campo codSuspPrinc  Recuperar a informação do campo COD_SUSP_PRINC da SAFX08 ou SAFX09.  [ALTERADO MFS11894] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Informações de Processo Retenção Principal “Campo Código do Indicativo da Suspensão deve ser numérico."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10357 MFS11894 MFS14463 |
| RN61 | Campo valorPrinc  Recuperar a informação do campo VLR_N_RET_PRINC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN62 | Origem das informações: SAFX08 ou SAFX09.  Regra de seleção: Este registro servirá para identificar os processos de retenção adicional relacionados a não retenção da contribuição previdenciária.   Campos-Chave: tpProcRetAdic, nrProcRetAdic, codSuspAdic  Nível hierárquico do registro: filho do registro idePrestServ.  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: poderá existir “50” infoProcRetAd ou não existir | MFS10357 MFS14463 |
| RN63 | Campo tpProcRetAdic  Recuperar a informação do campo IND_TP_PROC_ADJ_ADIC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |
| RN64 | Campo nrProcRetAdic  Recuperar a informação do campo NUM_PROC_ADJ_ADIC da SAFX08 ou SAFX09.  ALTERADO MFS11894] Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Informações de Processo Retenção Adicional “Campo Número do Processo deve ser numérico." Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10357 MFS11984 MFS14463 |
| RN65 | Campo codSuspAdic  Recuperar a informação do campo COD_SUSP_ADIC da SAFX08 ou SAFX09.  [ALTERADO MFS11984] Obs:   Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2010 - Registro : Informações de Processo Retenção Adicional “Campo Código do Indicativo da Suspensão deve ser numérico."  Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX | MFS10357 MFS11984 MFS14463 |
| RN66 | Campo valorAdic  Recuperar a informação do campo VLR_N_RET_ADIC da SAFX08 ou SAFX09. | MFS10357 MFS14463 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
