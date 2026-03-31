# MTZ-Tela_Encerramento_do_Resultado

> Fonte: MTZ-Tela_Encerramento_do_Resultado.docx






THOMSON REUTERS

Módulo Sped ECD

Tela Encerramento de Resultado


Localização: Menu Sped, Módulo: Escrituração Contábil Digital à Geraçãoà Encerramento do Resultado




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
2.1.	Abas que podem ser geradas:	7




## Regras Gerais


O objetivo desta tela é de criar os lançamentos de encerramento das contas de resultado de forma automática.

## Layout da Tela



Campos de preenchimento obrigatório: Empresa, Período, Processo, Histórico do Lançamento de Encerramento (Conta de Resultado) Conta de Contrapartida do Lançamento de Encerramento, Histórico do Lançamento de Encerramento (Contrapartida) Estabelecimentos. Caso um desses campos não esteja preenchidos, verificar a mensagem a ser exibida, nas regras abaixo.




#### Abas que podem ser geradas:




| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-39909 | Criação da tela – Esta tela sem requisito. Nesta demanda estamos documentando o que foi implementado, através de Engenharia Reversa. | Alessandra Cristina Navatta | 13/07/2020 |
| MFS-34603 | Ajuste na funcionalidade, considerando os estudos realizados na MFS39910 | Alessandra Cristina Navatta | 18/08/2020 |
| MFS-89543 | Inclusão do Campo “Centro de Custo de Contrapartida”, o usuário poderá optar em efetuar os lançamentos de contrapartida, do encerramento, utilizando a tabela de Saldo por Centro de Custo (SAFX80). | Rogério Ohashi | 13/07/2022 |
|  | dois novos parâmetros: “Centralizado” e “Geração para empresas com lançamentos/saldos entre filiais” conforme cenário/solicitação do cliente Bunge. |  | 20 |


| Campo | Regra | Demanda |
| --- | --- | --- |
| Empresa | Por default vem preenchida com a empresa logada e pode ser alterada pelo usuário. | MFS-39909 |
| Período | MM/AAAA | MFS-39909 MFS-34603 |
| Processo | Opções Válidas   Criar os Lançamentos de Encerramento Excluir os Lançamentos de Encerramento Criados pelo Sistema A opção default é a Criar os Lançamentos de Encerramento   Se marcada a opção ‘Excluir os Lançamentos de Encerramento Criados pelo Sistema’, os registros de lançamento de encerramento e da contrapartida que foram criados pelo processo e a atualização/criação do saldo (por consequência deste processo) serão excluídos.  Se marcada a opção ‘Criar os Lançamentos de Encerramento, internamente será executado o processo de limpeza das informações para só depois seguir com a geração do processo. | MFS-39909 MFS-34603 |
| Considerar Saldo por Centro de Custo (SAFX80) | Se marcado, deverá ser considerado a SAFX02 e, também as informações da tabela de saldo por centro de custo (SAFX80),  porém se caso houver as duas, deverá ser considerada a SAFX80 e somente zerar o saldo da SAFX02.  Caso a opção esteja desmarcada, não vamos considerar as informações da X80 (saldos por centro de custo), apenas as informações da X02 (saldos contábeis). | MFS-39909 MFS-34603 |
| Histórico da Conta de Resultado | Exibir o texto “Lançamento de encerramento da conta de resultado criado pelo sistema””. Este texto pode ser alterado pelo usuário. | MFS-34603 |
| Conta de Contrapartida | A conta contábil deve estar previamente cadastrada na tabela de plano de contas da empresa (SAFX2002). | MFS-39909 MFS-34603 |
| Centro de Custo de Contrapartida | O centro de custos deve estar previamente cadastrado na tabela de centro de custos da empresa (SAFX2003).  Obs.: Esta opção deverá ser habilitada, para preenchimento, somente se a opção “Considerar Saldo por Centro de Custo (SAFX80)” estive marcada. | MFS-89543 |
| Histórico da Contrapartida | Exibir o texto “Lançamento de encerramento da conta de contrapartida criado pelo sistema” Este texto pode ser alterado pelo usuário. | MFS-34603 |
| Centralizado | [ALTERAÇÃO MFS-1040618] Incluir um novo parâmetro "Centralizado”.   Tipo: Checkbox Padrão: Habilitado | MFS-1040618 |
| Geração para empresas com lançamentos/saldos entre filiais | Geração para empresas com lançamentos/saldos entre filiais. |  |
| Grid Estabelecimentos | Geração para empresas com lançamentos/saldos entre filiais |  |
| Selecionar | Permite que o usuário selecione os Estabelecimentos que serão gerados os cálculos:  Tratamentos:  Modal 'Selecionar Estabelecimentos‘ Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar). | MFS-39909 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos. | MFS-39909 |
| Executar | Mensagens que bloqueiam a geração do processo:  Ao acionar este campo, verificar se na tela:  Campo Período está preenchido. Caso não esteja preenchido exibir a mensagem: Informe o Período. Deve ser marcada pelo menos um estabelecimento. Caso contrário, exibir a mensagem “Selecione pelo menos um Estabelecimento”. Campo Conta de Contrapartida está preenchido. Caso não esteja preenchido exibir a mensagem: Informe a Conta de Contrapartida . Ao executar, se não for encontrada a conta de Contrapartida, no plano de contas, ou se a mesma não estiver com situação ativa, exibir a mensagem: “A conta ‘XXX’ não existe no plano de contas ou não está com situação ‘Ativa’. Ao executar, se não for encontrado o centro de custo de Contrapartida, na tabela de centro de custo (SAFX2003), exibir a mensagem: “O centro de custo ‘XXX’ não consta cadastrada na tabela de centro de custos. Os campos de Histórico (Histórico da Conta de Resultado e Histórico da Contrapartida), são de preenchimento obrigatório, caso um deles não esteja preenchido ao ser executado o processo, considerar o texto default indicado no respectivo campo. Ao acionar este campo, verificar e, se necessário exibir a mensagem na aba de Logs:  Se não há dados no período a ser processo (não há saldo em nenhuma conta de resultado), exibir a mensagem: “O processo não foi executado, pois não foi encontrado saldo em conta de resultado para ser criado o lançamento de encerramento”.  Regras do Processo:  Considerar as regras existentes no documento “MTZ_Processamento_Encerramento_de_Resultado.docx” | MFS-39909 MFS-34603 MFS-89543 |


| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-39909 |
| --- | --- | --- |
| Relatório de Conferência | Esta aba deve demonstrar um resumo (por conta de resultado), do saldo existente anteriormente (antes do processo) e o saldo atualizado. | MFS-39909 |
| Logs | Esta aba deve demonstrar os logs do processo.   Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração. | MFS-39909 |
