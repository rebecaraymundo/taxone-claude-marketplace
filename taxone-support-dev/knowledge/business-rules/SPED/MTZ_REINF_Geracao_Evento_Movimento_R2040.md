# MTZ_REINF_Geracao_Evento_Movimento_R2040

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2040.docx






THOMSON REUTERS

Geração evento R-2040 - REINF


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO


Registro ideEvento – Informações de Identificação do Evento



Registro ideContri – Informações de Identificação do Contribuinte



Registro IdeEstab – Identificação do Estabelecimento que repassou recursos







Registro recursosRep – Recursos Repassados para Associação Desportiva



Registro infoRecurso - Registro de Detalhamento dos Recursos Repassados a Associação Desportiva




Registro infoProc – Informações de processos relacionados a não retenção de contribuição previdenciária.



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-11670 | Elenilson Coutinho | Definição de regras para geração do evento R-2040 Reinf |
| MFS-11925 | Lara Aline | Inclusão mensagens de logs RN10 e 11. |
| MFS-12777 | Elenilson Coutinho | Alteração de Regra para tratamento da geração do evento a partir da SAFX03 – Contas a Pagar |
| MFS-12176 | Elenilson Coutinho | Regra para tipo de arquivo Original/Retificação |
| MFS-12180 | Elenilson Coutinho | Regra de geração considerando eventos de fechamento/reabertura |
| CH17024_2017 | Lara Aline | Inclusão da opção 1 – Patrocínio no campo Tipo de Repasse |
| MFS13861 | Lara Aline | Alteração no layout conforme versão 1.2 |
| MFS14864 | Lara Aline | Alteração para recuperação de notas de entradas. |
| MFS14129 | Lara Aline | Inclusão de regra para o campo observação do registro nfs. |
| MFS15284 | Lara Aline | Ajuste nos campos vlrTotalRep e vlrBruto. |
| MFS16067 | Lara Aline | Ajuste para considerar o campo “Desconsiderar sem Valor de Retenção informado” da tela de Dados Iniciais. |
| MFS17138 | Lara Aline | Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura |
| MFS17269 | Lara Aline | Ajuste no campo vlrTotalNRet conforme nova versão 1.3.02. |
| MFS18702 | Lara Aline | Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos |
| MFS20930 | Lara Aline | Inclusão dos campos chaves na regra do registro infoProc, acordo com layout 1.4 |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da referência do arquivo de de_para (versão 2.1.1)  Obs. O ajuste mapeado nesta demanda, refere-se a atualização funcional. Não há impactos na implementação |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Geração do Evento R-2040.  O evento R-2040 do SPED - REINF tem por objetivo gerar informações de Recursos Repassados para Associação Desportiva. Ele será gerado com os registros:   Reinf – EFD - Reinf  evtAssocDespRep – Evento Recursos Repassados para Associação Desportiva  ideEvento – Informações de Identificação do Evento  ideContri – Informações de Identificação do Contribuinte  ideEstab – Informações de identificação  recursosRep – Recursos repassados para associação desportiva  infoRecurso – Detalhamento dos recursos repassados [Alterado MFS13861]  infoProc – Informações de processos relacionados a não retenção de contribuição previdenciária  Observar orientações existentes no arquivo " TR_REINF_DEXPARA_V2.1.1.xlsx ".  Origem das informações: SAFX03, SAFX04, SAFX09 e Cadastro do Estabelecimento.  Regra de seleção: O Registro R-2040 é utilizado para demonstrar informações de Recursos Repassados para Associação Desportiva. Ele será gerado com base em Informações de Notas Fiscais de Serviço ou Contas a Pagar. Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX03 e SAFX09, considerando os seguintes critérios:  [MFS12777]  - O COD_ESTAB seja de um estabelecimento indicado pelo usuário; - A origem das informações deve ter sido parametrizada na tela de “Dados Iniciais” com a definição de geração com base em “Documentos Fiscais de Serviço” ou “Contas a Pagar”. - Se na tela de Dados Iniciais para o Evento R-2040 – Recursos Repassados a Associação Desportiva houver parametrização para geração com base nas informações de:    [Alteração MFS14864] Documento Fiscal de Serviço, então:   O “Código de Serviço” deve ser associado a um tipo de repasse na parametrização de Identificação do Tipo de Repasse Por Código de Serviço. - NFs cujo campo MOVTO_E_S seja diferente de "9"; - O campo DATA_EMISSAO deve compreender o período de geração; - O campo SITUACAO deve ser diferente de "S"; - O campo COD_CLASS_DOC_FIS deve ser igual a "2", "3" ou “9”;  Contas a Pagar, Então:  - O “Código de Operação” deve ser associado a um tipo de repasse na parametrização de Identificação do Tipo de Repasse Por Código de Operação. - O campo DATA_MOVTO deve compreender o período de geração;   [Alterado MFS16067] Importante: Caso o campo “Desconsiderar sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais:  SAFX09 - Deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e/ou Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado. SAFX03 - Deverão ser desconsiderados todos os Arquivo de Fornecedores (Contas a Pagar) que não tenham o Valor da Retenção (VLR_RET da SAFX03) informado.   [MFS-12176]  Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:  Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original.  Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:                Evento R2040 – Recursos Repassados para Associação Desportiva               Evento não gerado. Existe evento anterior enviado aguardando retorno.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:  - Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação.  - Se existir, evento de exclusão considerar os status, então:  Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:                 Evento R2040 – Recursos Repassados para Associação Desportiva              Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX            Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência           anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova           ocorrência de arquivo de  retificação, se não houver, criar original.                - Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação.               - Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:                                Evento R2040 – Recursos Repassados para Associação Desportiva               Evento não gerado. Existe evento anterior não enviado.               Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.  Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se não houver, criar original.  [MFS18702] Importante: Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.  [MFS-12180]  Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.  Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.  Se houver ocorrência de geração de evento de fechamento considerar os status então:                        - Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:                                          Evento R2040 – Recursos Repassados para Associação Desportiva                   Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                        - Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte                         mensagem no log de geração:                                    Evento R2040 – Recursos Repassados para Associação Desportiva                   Evento não gerado. Período Fechado.                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX  Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com Sucesso ou Advertência”, prosseguir com a geração.                    [Alterado MFS17138]          - Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do             XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:                     Evento R2040 – Recursos Repassados para Associação Desportiva                    Evento não gerado. Período Fechado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX                      Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,                    prosseguir com a geração.                          - Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de                             geração:                     Evento R2040 – Recursos Repassados para Associação Desportiva                    Evento não gerado. Existe evento de fechamento do período não enviado.                    Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX | MFS11670 MFS12777 MFS12176 MFS12180 MFS13861 MFS14864 MFS16067 MFS17138 MFS18702 MFS-90001 |


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
| RN01 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento centralizador (Matriz).  Campos-Chave: tpInsc, nrInsc  Nível hierárquico do registro: filho do registro evtAssocDespRep  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo |  |
| RN02 | Campo TpInsc  Será gerado com conteúdo "1", uma vez que não atendemos PF. | MFS14821 |
| RN03 | Campo nrInsc  Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento.Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador. | MFS14821 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN04 | Origem das informações: Cadastro do Estabelecimento.  Regra de seleção: Este registro servirá para identificar o estabelecimento que repassou recursos  Campos-Chave: tpInscEstab, nrInscEstab  Nível hierárquico do registro: filho do registro ideContri  Ordenação: não se aplica.  Agrupamento: não se aplica.  Ocorrência: Um por arquivo | MFS11670 |
| RN05 | Campo tpInscricao  Gerar com conteúdo igual a “1”. | MFS11670 |
| RN06 | Campo nrInscricao  Gerar com o conteúdo do campo “CGC” do Cadastro do Estabelecimento da NF.  Se para | MFS11670 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN07 | Origem das informações: SAFX03, SAFX04 e SAFX09.  Regra de seleção: Este registro servirá identificar os repasses efetuados a associação Desportiva pelo estabelecimento.  Campos-Chave: Não se aplica.  Nível hierárquico do registro: filho do registro ideEstab  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada ideEstab poderá existir “N” recursosRep | MFS11670 |
| RN08 | Campo cnpjAssocDesp  Este campo será gerado com a informação carregada no campo CPF_CGC da SAFX04.  Obs: CNPJ da Pessoa Jurídica vinculada a NF.  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2040 - Registro: Recursos Repassados para Associação Desportiva  “Campo CPF_CGC não preenchido“.  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  [MFS12777]  Se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar” a descrição da mensagem no log deve ser alterada caso não preenchido o campo, deverá apresentar a seguinte mensagem no log de pré-geração:    Evento R2040 - Registro: Recursos Repassados para Associação Desportiva  “Campo CPF_CGC não preenchido“.  Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS11670 MFS-12777 |
| RN09 | Campo vlrTotalRep  Será resultado da somatória do campo VLR_TOT da SAFX09 informado nos recursos repassados detalhado no registro infoRecurso.  [MFS12777][MFS15284]  Carregar com a resultado da somatória do campo “VLR_BRUTO” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”. | MFS11670 MFS12777 MFS15284 |
| RN10 | Campo vlrTotalRet  Será resultado da somatória do campo VLR_INSS_RETIDO da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”.  [MFS12777]  Carregar com a resultado da somatória do campo “VLR_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”. | MFS11670 MFS12777 |
| RN11 | vlrTotalNRet  Será resultado da somatória do campo VLR_N_RET_PRINC da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”, com exceção dos valores informados com o Indicador de Suspenção (ind_susp) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão (SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos) através do campo Código de Suspensão (COD_SUSP_PRINC) informado na SAFX09.  [MFS12777]  Carregar com a resultado da somatória do campo “VLR_N_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”, com exceção dos valores informados com o Indicador de Suspenção (ind_susp) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão (SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos) através do campo Código de Suspensão (COD_SUSP) informado na SAFX03. | MFS11670 MFS12777 MFS17269 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN12 | Origem das informações: SAFX09 e SAFX03  Regra de seleção: Este registro servirá para identificar os recursos repassados a associação desportiva  Campos-Chave: Não se aplica.  Nível hierárquico do registro: filho do registro recursosRep  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: para cada recursosRep poderá existir “N” infoRecursos. | MFS11670 MFS12777 |
| RN13 | Campo tpRepasse  Informação será recuperada do campo “Tipo de Repasse” da Tela de “Identificador do Tipo de Repasse por Código de Serviço”.  [Alteração CH17024_2017] Valores válidos: 1, 2, 3, 4 e 5.  [MFS12777]  Informação será recuperada do campo “Tipo de Repasse” da tela de “Identificador do Tipo de Repasse por Código de Operação” quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”. | MFS11670 MFS12777 CH17024_2017 |
| RN14 | Campo descRecurso  Nesse campo será gravada a descrição de acordo com o campo “Tipo de Repasse” da Tela de “Identificador do Tipo de Repasse por Código de Serviço”. Conforme abaixo:  1 - 'Patrocínio'; 2 - 'Lic. marcas símbolos'; 3 - ‘Publicidade'; 4 - 'Propaganda'; 5 - 'Transmite espetáculo';  Valores Válidos: 1,2,3,4,5 | MFS13861 |
| RN15 | Campo vlrBruto  Informação será recuperada do campo VLR_TOT da SAFX09.  [MFS12777][MFS15284]  Informação será recuperada do campo “VLR_BRUTO” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”. | MFS11670 MFS12777 MFS15282 |
| RN16 | Campo vlrRetApur  Informação será recuperada do campo VLR_INSS_RETIDO SAFX09.   Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2040 - Registro: Detalhamento dos Recursos Repassados a Associação Desportiva  “Campo Valor da Retenção do INSS não preenchido“. Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX  [MFS12777]  Informação será recuperada do campo “VLR_RET” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”.  Caso não preenchido deverá apresentar a seguinte mensagem no log de pré-geração:   Evento R2040 - Registro: Detalhamento dos Recursos Repassados a Associação Desportiva  “Campo Valor da Retenção do INSS não preenchido“. Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód. Operação: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS11670 MFS12777 |
| RN23 | Campo vlrNRet  Informação será recuperada do campo VLR_N_RET_PRINC da SAFX09.  [MFS12777]  Informação será recuperada do campo “VLR_N_RET” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”. | MFS11670 MFS12777 MFS13861 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN17 | Origem das informações: SAFX09 e SAFX03  Regra de seleção: Este registro servirá identificar os processos relacionados a não retenção de contribuição previdenciária.  Campos-Chave: tpProc, nrProc e codSusp.  Nível hierárquico do registro: filho do registro recursosRep  Ordenação: não se aplica.  Agrupamento: Não se aplica.  Ocorrência: Poderá existir “50” infoProc. | MFS13861 MFS20930 |
| RN18 | Campo tpProc  Informação será recuperada do campo IND_TP_PROC_ADJ_PRINC da SAFX09.  Informação será recuperada do campo IND_TP_PROC_ADJ_PRINC da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”. | MFS13861 |
| RN19 | Campo nrProc  Informação será recuperada do campo NUM_PROC_ADJ_PRINC da SAFX09.   Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2040 - Registro: Recursos Recebidos ou Repassados para Clube de Futebol “Campo Número do Processo deve ser numérico."  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX   Informação será recuperada do campo NUM_PROC_ADJ_PRINC da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”.  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2040 - Registro: Recursos Repassados para Associação Desportiva  “Campo Número do Processo deve ser numérico."  Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS13861 |
| RN20 | Campo codSusp  Informação será recuperada do campo COD_SUSP_PRINC da SAFX09.  Obs:  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2040 - Registro: Recursos Recebidos ou Repassados para Clube de Futebol “Campo Código do Indicativo da Suspensão deve ser numérico."  Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX   Informação será recuperada do campo COD_SUSP da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”.  Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré-geração:  Evento R2040 - Registro: Recursos Repassados para Associação Desportiva  “Campo Código do Indicativo da Suspensão deve ser numérico."  Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX | MFS13861 |
| RN21 | vlrNRet  Será resultado da somatória do campo VLR_N_RET_PRINC da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”.  Carregar com a resultado da somatória do campo “VLR_N_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”. | MFS13861 |
