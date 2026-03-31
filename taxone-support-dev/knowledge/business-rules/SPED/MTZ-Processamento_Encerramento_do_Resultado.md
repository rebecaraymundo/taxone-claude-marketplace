# MTZ-Processamento_Encerramento_do_Resultado

> Fonte: MTZ-Processamento_Encerramento_do_Resultado.docx






THOMSON REUTERS

Módulo Sped Contábil

Processamento Encerramento do Resultado


Localização: Menu Sped, Módulo: Escrituração Contábil Digital à Geraçãoà Encerramento do Resultado

Sumário

CONTROLE DE ALTERAÇÕES	3
1.1.	INTRODUÇÃO	3
1.2.	DOCUMENTOS DE REFERÊNCIA	3
1.3.	DEFINIÇÃO DAS REGRAS	4






















## CONTROLE DE ALTERAÇÕES












## INTRODUÇÃO

Este processo deverá ser utilizado pelas empresas que não tenham realizado os lançamentos contábeis de encerramento das contas de resultado.




## DOCUMENTOS DE REFERÊNCIA


MTZ-Tela_Encerramento_de_Resultado.docx
## DEFINIÇÃO DAS REGRAS



| Data | Demanda | Descrição | Autor |
| --- | --- | --- | --- |
| 14/07/2020 | MFS-39909 | Criação do Documento. Nesta demanda estamos documentando o que foi implementado, através de Engenharia Reversa. | Alessandra Cristina Navatta |
| 18/08/2020 | MFS-34603 | Ajuste na funcionalidade, considerando os estudos realizados na MFS39910 (RP01 e RP03) | Alessandra Cristina Navatta |
| 13/04/2021 | MFS-62795 | Tratamento na geração do Processo “Criar os Lançamento de Encerramento”, para “bloquear” a geração caso seja identificado que o processo foi executado, sem antes executar o Processo de “Excluir os Lançamentos de Encerramento Criados pelo Sistema”. O objetivo é evitar que o usuário gere 2 vezes seguidas o processo de “Criar os Lançamento de Encerramento”, causando erros na base. | Rogério Ohashi |
| 17/06/2021 | MFS-67497 | Tratamento na geração do Campo 16 - NUM_LANCAMENTO da tabela SAFX01, na criação dos lançamentos de encerramento, deverá ser concatenado “E” + “MM” + “AAAA” antes do número sequencial. (na Partida e Contrapartida). | Rogério Ohashi |
| 12/07/2021 | MFS-68760 | Ajustes na funcionalidade do Parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” regra RP01 e Aba de Relatório de Conferência regra RP04. | Rogério Ohashi |
| 21/09/2021 | MFS-72676 | Alteração na geração do Encerramento Contábil para considerar os Saldos se a conta contábil estiver inativada, porém houver a mesma conta com Data de Validade Anterior com a situação Ativa. | Rogério Ohashi |
| 13/07/2022 | MFS-89543 | Tratamento na geração do Processo de Encerramento do Exercício, para considerar o campo “Centro de Custo de Contrapartida” para efetuar os lançamentos de contrapartida para a tabela de Saldos por Centro de Custos (SAFX80). | Rogério Ohashi |
| 11/11/2022 | MFS-96911 | Tratamento na geração do Processo de Encerramento do Exercício, para considerar o Campo de “Dia e Mês do Encerramento do Exercício Social”, para atendimento aos clientes com Situação Especial, em que a data seja diferente de 31/12. | Rogério Ohashi |
| 04/05/2023 | MFS-532288 | Readequação da Regra para Geração do arquivo Meio Magnético para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, recuperando o Saldo das Tabelas SAFX02 e SAFX80, da mesma conta contábil para o mesmo período. | Rogério Ohashi |
| 20/02/2026 | MFS-1040618 | Inclusão de dois novos parâmetros para gerar os lançamentos de encerramento: “Centralizado” e “Geração para empresas com lançamentos/saldos entre filiais” conforme cenário/solicitação do cliente Bunge. | Lyene Benvenutti |


| Número | Regra | Demanda |
| --- | --- | --- |
| RP00 | Esta funcionalidade tem o propósito de gerar os lançamentos de encerramento de contas de natureza de resultado, além de criar o respectivo lançamento de contrapartida na conta (indicada na tela de geração ‘Resultado de Encerramento’ e atualizar os saldos das contas de resultados.  Esta rotina será acionada através da tela ‘Resultado de Encerramento’, localizada no Menu Sped, Módulo: Escrituração Contábil Digital à Geraçãoà Encerramento do Resultado  [MFS-96911] Tratamento para considerar o Campo Dia e Mês do Encerramento do Exercício Social da tela de Dados Iniciais  Tratamento:       Considerar o dia/mês da tela de Dados Iniciais, do parâmetro “Dia e Mês do Encerramento do Exercício Social”, como período para execução do processo de Encerramento.  Obs.: Essa alteração é para atendimento aos clientes com Situação Especial, em que a data não seja 31/12.  [MFS-72676] Tratamento para contas inativadas x contas ativas na tabela SAFX2002 (Plano de conta)    Tratamento:           Se a conta contábil da tabela “X2002_PLANO_CONTAS” (maior validade), o campo “IND_SITUACAO” estiver preenchido com “I”;         E se houver a mesma conta contábil com Data de Validade anterior (cadastrada no Plano de Contas) com o campo “IND_SITUACAO” preenchido com “A”;            Então considerar o Saldo das tabelas SAFX02, SAFX80, dessa Conta Contábil na geração do Encerramento Contábil.  Senão não considerar a conta contábil para geração do Encerramento Contábil. | MFS-39909 MFS-72676 MFS-96911 |
| RP01 | Se na tela for marcada a opção do Processo “Geração”:  [MFS-68760] Regra Parâmetro - Considerar Saldos por Centro de Custo (SAFX80)  O sistema deverá buscar os saldos de todas as contas de resultado, com situação igual a ‘Ativa’, de naturezas igual a ‘3’- despesa, ‘4’- receita, ‘5’- mutações ativas e ‘8’– custo e que possuam saldo final diferente de zero no último dia do período indicado na tela.   Parâmetro Desmarcado: Caso o parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” estiver desmarcado, o sistema deverá considerar os saldos por conta contábil (SAFX02) com valores de saldo final diferente de zero.   Importante: Deverão ser considerados somente os saldos por conta contábil da tabela SAFX02, ignorando a tabela de saldo por centro de custos (SAFX80), se existir.  Parâmetro marcado: Caso o parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” estiver marcado, o sistema deverá considerar os saldos por conta contábil (SAFX02) e, também os saldos por centro de custo (SAFX80), com valores de saldo final diferente de zero. Caso contrário, não existindo informações de saldo por centro de custos (SAFX80), serão consideradas as informações da SAFX02.  Importante: Caso houver movimentação de saldo por conta contábil (SAFX02) e por centro de custos (SAFX80) para mesma conta contábil), o sistema deverá efetuar todo o processo de “encerramento” considerando, somente, o saldo por centro de custos (SAFX80), porém o sistema deverá “zerar as contas”, também, os saldos por conta contábil (SAFX02), mas não deverá criar os lançamentos de encerramento (SAFX01), para não causar duplicidades.  [MFS-89543] Tratamento p/ lançamentos de contrapartida utilizando Saldo por Centro de Custo (SAFX80).   Se o campo “Centro de Custo de Contrapartida” estiver preenchido, o sistema deverá efetuar os lançamentos de contrapartida do encerramento, considerando a tabela de Saldos por centro de custo (SAFX80), ou seja, se informado um código de centro de custo válido, os valores dos lançamentos de contrapartida serão gravados no lançamento de Saldo por Centro de Custos (SAFX80), considerando a Conta Contábil + Centro de Custos, informado em tela.   Obs.: Se existir um lançamento por Saldo Contábil (SAFX02), para o período, da conta contábil informado em tela, a mesma deverá ser desprezada.  Senão   Se o campo “Centro de Custo de Contrapartida” não estiver preenchido o sistema deverá seguir conforme regras atuais, utilizando somente a conta contábil de contrapartida (SAFX02), a Conta Contábil informado em tela.  Habilitar o campo “Centro de Custo de Contrapartida” apenas se o parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” estiver marcado.  [ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.  Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.  Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.  Tratamento:  Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá recuperar as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.  Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá recuperar as informações dos Saldos da SAFX02 ou SAFX80, conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”.   Default: Desmarcado.   Importante: A regra de preenchimento dos indicadores de Débito e Crédito, para efetuar os lançamentos para o Saldo por Centro de Custos (SAFX80) e criação dos Lançamentos Contábeis, bem como a regra de exclusão dos lançamentos para reversão do encerramento, deverá ser semelhante ao processo implementada para o Saldo por conta contábil (SAFX02), conforme regras abaixo:  Para cada conta de resultado que for encontrado saldo diferente de zero no último dia do mês indicado na tela, o sistema, deve criar um lançamento de encerramento, para zerar o saldo final desta conta. Abaixo será detalhado como será gerado os valores dos lançamentos e seus indicadores:    Valor e Indicador de cada lançamento:  A composição do valor será feita pela tabela de Saldos   1.1 Para indicador de lançamento do saldo inicial = “D” Valor do saldo a zerar (saldo final) = Saldo Inicial + Débitos – Créditos Indicador do saldo a zerar  Será “D” se o cálculo do valor do saldo a zerar for >0 Será “C” se o cálculo do valor do saldo a zerar for <0 	 1.2 Para indicador de lançamento do saldo inicial = “C” Valor do saldo a zerar (saldo final) = Saldo Inicial - Débitos + Créditos Indicador do saldo a zerar Será “C” se o cálculo do valor do saldo a zerar for >0 Será “D” se o cálculo do valor do saldo a zerar for <0  Valor do lançamento = valor do saldo a zerar (1.1 ou 1.2)   Indicador do lançamento = indicador inverso ao do valor do saldo a zerar: 	Será “D” se o indicador do saldo a zerar = “C” 	Será “C” se o indicador do saldo a zerar = “D”  Dados a serem gravados na SAFX01 (Lançamento de Encerramento):    Para cada Lançamento de encerramento criado, geraremos um lançamento da Contrapartida:      Ao final do processamento (criação dos lançamentos de encerramento), os valores (total de débito, total de crédito e saldo final) das contas de resultado deverão ser recalculados na tabela de saldos/saldos por centro de custo (quando se aplicar).  Isto permitirá que os valores de lançamentos e saldo final da Tabela de Saldos, ou Saldos por Centro de Custo reflitam os novos valores, considerando os lançamentos criados por este processamento.  [MFS-62795] Tratamento Geração Processo – Criar os Lançamentos de Encerramento.  - Quando a opção do Processo “Criar os Lançamento de Encerramento” for marcada, para garantir que não haverá duplicidade de informações, caso seja executado novamente, o sistema deverá bloquear a execução, caso exista lançamentos do Tipo E.     Se houver lançamentos no campo “tipo_lancto” da tabela X01_contabil igual a “E”.      Não executar (Bloquear) a geração do processo do Processo “Criar os Lançamento de Encerramento” e gravar Log de Geração:       Criar os Lançamentos de Encerramento à gravar mensagem no log com a seguinte descrição: “Identificado lançamentos na base com o Tipo de Lançamento Igual a E, antes de executar novamente o processo, executar o processo de “Excluir os Lançamentos de Encerramento Criados pelo Sistema”. | MFS-39909 MFS-34603 MFS-68760 MFS-89543                                                        MFS-67497 MFS-89543 MFS-532288 |
| RP02 | Se na tela for marcada a opção do Processo “Excluir os Lançamento de Encerramento Criados pelo Sistema”:  O sistema deve excluir todos os registros que foram calculados/criados por este processo (excluir os lançamentos de encerramento, o lançamento de contrapartida e voltar os valores (total de crédito, total de débito e saldo final), da tabela de saldos / saldos por centro de custo (quando se aplicar). | MFS-39909 MFS-34603 |
| RP03 | Aba LOGs  Caso já exista na base o lançamento de encerramento para a conta/ou conta e centro de custo de resultado, exibir a mensagem de erro no log “O lançamento de encerramento não foi criado, pois já existe na base”. Exibir no log os campos necessários para facilitar a identificação da conta e lançamento pelo usuário.  Apresentar os totais de quantos lançamentos de encerramento, contrapartida foram criados. Quantos saldos foram atualizados.    Apresentar no log as contas de resultado que não foram calculados/criados os lançamentos de encerramento pois estavam com situação igual a ‘Inativa’, Critério completo de seleção desses cadastros: Situação Inativa, naturezas iguais a ‘3’- despesa, ‘4’- receita, ‘5’ – mutações ativa e ‘8’- custo e que possuem saldo final diferente de zero no último dia do período indicado na tela). Deve ser exibida a mensagem: “Não foi criado o lançamento de encerramento para a conta, pois a mesma está cadastrada com situação Inativa.” Exibir no log os campos necessários para facilitar a identificação da conta. | MFS-39909 MFS-34603 |
| RP04 | Aba Relatório de Conferência  [MFS-68760] Tratamento Relatório de Conferência  Este relatório deverá demonstrar um resumo (por conta de resultado), do saldo existente anteriormente (antes do processo) e o saldo atualizado conforme abaixo:  - Parâmetro: Considerar Saldos por Centro de Custo (SAFX80)  Parâmetro Desmarcado: Caso o parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” estiver desmarcado, o sistema deverá demonstrar no Relatório de Conferência um resumo (por conta de resultado), do saldo existente anteriormente (antes do processo) e o saldo atualizado, considerando somente a SAFX02.  Parâmetro marcado: Caso o parâmetro “Considerar Saldos por Centro de Custo (SAFX80)” estiver marcado, o sistema deverá demonstrar no Relatório de Conferência um resumo (por conta de resultado), do saldo existente anteriormente (antes do processo) e o saldo atualizado, considerando a SAFX80 e SAFX02, (porém a SAFX02 deverá ser utilizado, somente, se não existir o saldo na SAFX80). | MFS-68760 |
| RP05 | [MFS-1040618] Inclusão de dois novos parâmetros conforme cenário/solicitação do cliente Bunge.   Criar um novo parâmetro: "Centralizado" Deve vir habilitado por padrão. Se habilitado:         deve exibir os estabelecimentos que o usuário tem acesso no quadro de estabelecimentos para o usuário selecionar         deve gerar um arquivo com os lançamentos de encerramento para todos os estabelecimentos centralizados que foram selecionados  Criar um novo parâmetro: "Geração para empresas com lançamentos/saldos entre filiais" Deve vir desabilitado por padrão, mantendo o comportamento atual do sistema. Se habilitado:         deve desabilitar automaticamente o parâmetro “Centralizado”         deve exibir apenas a opção “Todos” para o usuário selecionar no quadro de estabelecimentos         deve gerar um arquivo com os lançamentos de encerramento ocorridos entre os estabelecimentos | MFS-1040618 |
|  |  |  |
