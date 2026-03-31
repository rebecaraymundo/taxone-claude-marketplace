---
source: "MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _TELAS E MENUS - ICMS PROPRIO (1).docx"
category: Tax Payments
converted: auto
---





THOMSON REUTERS

Novo Módulo Integração Guias de Pagamento DOOTAX


















DOCUMENTO DE REQUISITO

Sumário

**1.	Objetivo	3**
2.	Localização do Menu	4
3.	Layout da Tela e fluxo de integração	7
3.1 Dados que definem a chave de identificação da Parametrização:	7
3.2 Dados que definem a chave de identificação da “Guia de Pagamento”:	12
3.4 Dados que definem a chave de identificação da aba LOG	22
3.5 Abertura de Nova Guia para Armazenamento do Relatório	25
3.6	Estrutura do “Relatório” na aba Arquivo	27
5. Views importantes:	30













# Objetivo

O novo módulo de “Guia de Pagamento” foi desenvolvido com base na estrutura de um processo customizado já existente “DOOTAX”. Essa estrutura será reaproveitada e integrada a outro menu dentro do Onesource Tax One e Onesource BR.

O reaproveitamento visa otimizar a implementação, mantendo a lógica de negócio previamente validada e adaptando-a às especificidades do menu onde será inserido. Essa abordagem visa reduzir esforços de implementação, garantir a consistência operacional e facilitar a manutenção futura, assegurando que o novo módulo atenda às necessidades específicas de processamento de Guias de Pagamento.

Deverá transformar a funcionalidade customizada em um módulo produtizável (Produtização = Preparado para comercialização), garantindo que não contenha dados ou referências específicas ao cliente original.

Todas as tabelas, procedures, views e outros objetos do banco de dados relacionados à funcionalidade deverão ser renomeados para evitar conflitos e manter a independência do novo módulo. Os dados existentes associados ao cliente original deverão ser descartados ou tratados para garantir que a nova função seja limpa e genérica. É necessário garantir que nenhuma referência explícita aos dados ou padrões do cliente original permaneça na implementação. Desta forma, é necessário ajustar todas as chamadas de procedures, tabelas e views para refletir os novos nomes, garantindo compatibilidade total com o novo módulo.
















# Localização do Menu

O módulo deve ser adicionado em um novo menu no Tax One, com nomenclatura adequada e aderente aos padrões do sistema.

O novo menu abrange integração entre o sistema Tax One (OBI) e a plataforma DOOTAX, utilizando APIs para a automação de processos relacionados a Guias de pagamento de tributos.


Localização: Básicos > Data Warehouse > Manutenção > Guia de Pagamento

Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Parâmetros

Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Geração

Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Relatório de Conferência/Executar













# Layout da Tela e fluxo de integração

# 3.1 Dados que definem a chave de identificação da Parametrização:

Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Parâmetros







# 3.2 Dados que definem a chave de identificação da “Guia de Pagamento”:

Básicos > Data Warehouse > Manutenção > Guia de Pagamento

S










**3.3 Dados que definem a chave de identificação da aba “Processos”:**

Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Processos





















# 3.4 Dados que definem a chave de identificação da aba LOG
Básicos > Data Warehouse > Manutenção > Guia de Pagamento > Processos > Log






































# 3.5 Abertura de Nova Guia para Armazenamento do Relatório

















# Estrutura do “Relatório” na aba Arquivo


O relatório gerado deverá conter os seguintes campos, que são essenciais para identificar e detalhar





















# Views importantes:



= = = = = =

---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS XXX | Paloma Dias Brondi | Novo Módulo Integração Guias de Pagamento Tax Payments | 13.02.2025 |
|  |  |  |  |


---

| Nome do Campo | BOTÃO / MENU | Funcionalidade | Seleção de Dados | Regra (Origem dos Dados) | Obrigatório | Mensagens do Sistema | Formato | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Impostos | - | Define o tipo de imposto a ser consultado. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| UF | - | Filtra as guias pelo estado de arrecadação. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Lista | - |
| Município | - | Filtra as guias pelo município de arrecadação. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Lista | - |
| Código de Arrecadação | - | Especifica o código de arrecadação do tributo. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| Código de Receita | - | Permite consultar as guias pelo código de receita. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| Status | - | Indica a situação da guia dentro do fluxo de pagamento. | Selecionado pelo usuário | Pode assumir os valores: "Pendente", "Enviado", "Pago", "Cancelado". | Não | - | Lista | Cada status reflete um estágio do processamento: "Pendente" (aguardando envio), "Enviado" (dados enviados ao Dootax), "Pago" (pagamento confirmado via API de retorno), "Cancelado" (guia cancelada). |
| Tipo de Execução | - | Indica o tipo de execução a ser realizada. | Selecionado pelo usuário | Valores predefinidos | Não | - | Lista | - |
| Data e Hora da Execução | - | Exibe a data e hora da execução. | Automático | Gerado pelo sistema | Não | "Data obrigatória" | Data/hora | - |
| Período | - | Define o intervalo de tempo para consulta. | Selecionado pelo usuário | Deve estar dentro do intervalo permitido | Sim | "Período obrigatório" | Data | - |
| Guia Complementar | - | Permite complementar o valor de um imposto que gerou saldo a pagar. | Selecionado pelo usuário | O usuário deverá informar o ID da guia de pagamento original para que o sistema identifique e complemente o valor faltante. | Não | "ID da guia original obrigatório para complemento" | Checkbox | Caso o usuário opte por complementar uma guia, ele deverá indicar a guia original para vinculação. |
| INSERIR | - | Permite incluir uma nova guia manualmente ou complementar uma guia existente. | Ação do usuário | O usuário deve selecionar se deseja inserir um pagamento avulso manual ou uma guia complementar. Se for complementar, o ID da guia original deverá ser informado. Se for uma guia manual, apenas os campos obrigatórios devem ser preenchidos. | Não | "Selecione o tipo de guia" | Botão | O botão deve oferecer a opção de selecionar entre 'Pagamento Avulso Manual' e 'Guia Complementar'. |
| BUSCAR REGISTRO | - | Pesquisa registros conforme os filtros aplicados. | Ação do usuário | - | Não | "Nenhum registro encontrado" | Botão | - |
| EXCLUIR REGISTRO | - | Remove registros selecionados. | Selecionado pelo usuário | - | Não | "Registro excluído com sucesso" | Botão | - |
| CONFIRMAR REGISTRO | - | Valida um registro inserido/modificado. | Selecionado pelo usuário | - | Não | "Registro confirmado" | Botão | - |
| RELATÓRIO DOS REGISTROS DO PERÍODO SELECIONADO | - | Gera um relatório de registros filtrados. | Ação do usuário | - | Não | "Relatório gerado com sucesso" | Botão | O usuário poderá salvar o relatório nos formatos Excel e PDF. |
| SELECIONAR TODAS AS GUIAS | - | Marca todas as guias listadas. | Selecionado pelo usuário | - | Não | - | Checkbox | - |
| EXECUTAR | - | Gera todos os dados analisados e atualiza a tabela temporária que armazena os dados das guias dessa tela. Isso permite que, após a conferência, o usuário clique em "Enviar" para gerar e transmitir o arquivo JSON ao sistema Dootax. | Ação do usuário | - | Sim | "Execução concluída com sucesso" | Botão | Apenas para conferência; não realiza o envio imediato. |
| MARCAR TODOS | - | Seleciona todos os registros visíveis na tela. | Selecionado pelo usuário | - | Não | - | Checkbox | - |
| Editar Guia | - | Modifica os dados de uma guia antes da execução/envio. | Selecionado pelo usuário | - | Não | - | Botão | - |
| Excluir Guia | - | Remove uma guia específica da lista. | Selecionado pelo usuário | - | Não | "Guia excluída" | Botão | - |
| ENVIAR | - | Envia as guias para pagamento no Dootax (gera JSON). | Selecionado pelo usuário | - | Sim | "Envio realizado com sucesso" | Botão | - |
| CANCELAR | - | Cancela guias já enviadas ao Dootax. | Selecionado pelo usuário | O cancelamento só será permitido para guias com status "Enviado". Não será permitido cancelar guias com status "Pago". | Não | "Guia cancelada com sucesso" | Botão | O cancelamento é irreversível e poderá ser restrito por perfil de usuário. |


---

| Nome do Campo | BOTÃO | Funcionalidade | Seleção de Dados | Regra (Origem dos Dados) | Obrigatório | Mensagens do Sistema | Formato | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Impostos | - | Define o tipo de imposto a ser consultado. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| UF | - | Filtra as guias pelo estado de arrecadação. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Lista | - |
| Município | - | Filtra as guias pelo município de arrecadação. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Lista | - |
| Código de Arrecadação | - | Especifica o código de arrecadação do tributo. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| Código de Receita | - | Permite consultar as guias pelo código de receita. | Selecionado pelo usuário | Tabela de Parametros | Não | - | Texto | - |
| Status | - | Indica a situação da guia dentro do fluxo de pagamento. | Selecionado pelo usuário | Pode assumir os valores: "Pendente", "Enviado", "Pago", "Cancelado". | Não | - | Lista | Cada status reflete um estágio do processamento: "Pendente" (aguardando envio), "Enviado" (dados enviados ao Dootax), "Pago" (pagamento confirmado via API de retorno), "Cancelado" (guia cancelada). |
| Tipo de Execução | - | Opções: *Imediata – A guia será executada assim que o usuário confirmar. Esta opção vem preenchida como opção default (padrão); *Programada – Permite agendar a execução para uma data futura. Validações e Mensagens do Sistema Aplicável somente para: Execução programada. | Selecionado pelo usuário | Valores predefinidos | Não | Opções: Imediata – A guia será executada assim que o usuário confirmar. Erro de Validação: Condição: O usuário selecionou "Programada" mas não preencheu a data da execução. Mensagem: "Por favor, informe a data de execução para a programação." Exibição: Ao clicar em "Executar" sem preencher a data. Comportamento: Destacar o campo "Data de Execução" em vermelho. | Lista | - |
| Data e Hora da Execução | - | Aplicável somente para: Execução programada. | Automático | Gerado pelo sistema | Apenas o campo da data é obrigatório. | "Data obrigatória" | Data/hora | - |
| Período | - | Define o intervalo de tempo para consulta. | Selecionado pelo usuário | Deve estar dentro do intervalo permitido | Sim | "Período obrigatório" | Data | -chave de validação período comportamento para não gerar a mesma guia em duplicidade incluir mensagem  erros “Guia gerada” chave = cod.empresa cod. Estab cod receita e série período status |
| Guia Complementar | - | Permite complementar o valor de um imposto que gerou saldo a pagar. | Selecionado pelo usuário | O usuário deverá informar o ID da guia de pagamento original para que o sistema identifique e complemente o valor faltante. | Não | "ID da guia original obrigatório para complemento" | Checkbox | Caso o usuário opte por complementar uma guia, ele deverá indicar a guia original para vinculação. |
| INSERIR | - | Permite incluir uma nova guia manualmente ou complementar uma guia existente. | Ação do usuário | O usuário deve selecionar se deseja inserir um pagamento avulso manual ou uma guia complementar. Se for complementar, o ID da guia original deverá ser informado. Se for uma guia manual, apenas os campos obrigatórios devem ser preenchidos. | Não | "Selecione o tipo de guia" | Botão | O botão deve oferecer a opção de selecionar entre 'Pagamento Avulso Manual' e 'Guia Complementar'. |
| BUSCAR REGISTRO | - | Pesquisa registros conforme os filtros aplicados. | Ação do usuário | - | Não | "Nenhum registro encontrado" | Botão | - |
| EXCLUIR REGISTRO | - | Remove registros selecionados. | Selecionado pelo usuário | - | Não | "Registro excluído com sucesso" | Botão | - |
| CONFIRMAR REGISTRO | - | Valida um registro inserido/modificado. | Selecionado pelo usuário | - | Não | "Registro confirmado" | Botão | - |
| RELATÓRIO DOS REGISTROS DO PERÍODO SELECIONADO | - | Gera um relatório de registros filtrados. | Ação do usuário | - | Não | "Relatório gerado com sucesso" | Botão | O usuário poderá salvar o relatório nos formatos Excel . |
| SELECIONAR TODAS AS GUIAS | - | Marca todas as guias listadas. | Selecionado pelo usuário | - | Não | - | Checkbox | - |
| EXECUTAR | - | Gera todos os dados analisados e atualiza a tabela temporária que armazena os dados das guias dessa tela. Isso permite que, após a conferência, o usuário clique em "Enviar" para gerar e transmitir o arquivo JSON ao sistema Dootax. | Ação do usuário | - | Sim | "Execução concluída com sucesso" | Botão | Apenas para conferência; não realiza o envio imediato. |
| MARCAR TODOS | - | Seleciona todos os registros visíveis na tela. | Selecionado pelo usuário | - | Não | - | Checkbox | - |
| Editar Guia | - | Modifica os dados de uma guia antes da execução/envio. | Selecionado pelo usuário | - | Não | - | Botão | - |
| Excluir Guia | - | Remove uma guia específica da lista. | Selecionado pelo usuário | - | Não | "Guia excluída" | Botão | - |
| ENVIAR | - | Envia as guias para pagamento no Dootax (gera JSON). | Selecionado pelo usuário | - | Sim | "Envio realizado com sucesso" | Botão | - |
| CANCELAR | - | Cancela guias já enviadas ao Dootax. | Selecionado pelo usuário | O cancelamento só será permitido para guias com status "gerado". Não será permitido cancelar guias com status "Pago" ou “Enviados”. | Não | "Guia cancelada com sucesso" | Botão | O cancelamento é irreversível e poderá ser restrito por perfil de usuário. |


---

| Nome | Regra |
| --- | --- |
| LISTAR | Descrição da Função: |
| LISTAR | Este botão permite ao usuário filtrar e exibir os logs de processos realizados nos últimos X dias. |
| LISTAR | Comportamento Esperado: |
| LISTAR | Ao clicar, o sistema deve exibir apenas os logs de processos que ocorreram dentro do intervalo de dias selecionado. |
| LISTAR | O número de dias pode ser configurável (ex.: "últimos 7 dias", "últimos 30 dias", etc.). |
| LISTAR | Caso o usuário deseje alterar o intervalo de dias, ele poderá inserir o número de dias desejado. |
| LISTAR | Após a execução, os logs devem ser atualizados automaticamente na interface da aba PROCESSOS. |
| LISTAR |  |
| EXCLUI PROCESSOS SELECIONADOS | Este botão permite ao usuário excluir processos selecionados da lista. |
| EXCLUI PROCESSOS SELECIONADOS | Comportamento Esperado: |
| EXCLUI PROCESSOS SELECIONADOS | O botão deve ser habilitado somente quando um ou mais processos estiverem selecionados. |
| EXCLUI PROCESSOS SELECIONADOS | Ao clicar, o sistema deve exibir uma mensagem de confirmação (ex.: "Tem certeza de que deseja excluir os processos selecionados?"). |
| EXCLUI PROCESSOS SELECIONADOS | Após a confirmação, os processos selecionados devem ser removidos da lista e do banco de dados, se aplicável. |
| EXCLUI PROCESSOS SELECIONADOS | Caso algum erro ocorra durante a exclusão (ex.: falha ao acessar o banco de dados), o sistema deve exibir uma mensagem de erro apropriada. |
| EXCLUI PROCESSOS SELECIONADOS | Após a exclusão, a lista de processos deve ser atualizada automaticamente. |
| EXCLUI PROCESSOS SELECIONADOS |  |
| SELECIONAR TODOS | Este botão permite ao usuário selecionar todos os processos exibidos na lista. |
| SELECIONAR TODOS | Comportamento Esperado: |
| SELECIONAR TODOS | Ao clicar, todos os processos na lista devem ser selecionados (indicado por um checkbox ativado ou outra marcação visual). |
| SELECIONAR TODOS | Caso todos os processos já estejam selecionados, o botão deve alternar para "Desmarcar Todos", permitindo desmarcar todas as seleções de uma vez. |
| SELECIONAR TODOS |  |
| ABRIR PROCESSO | Este botão permite ao usuário abrir os detalhes de um processo específico. |
| ABRIR PROCESSO | Comportamento Esperado: |
| ABRIR PROCESSO | §  Ao clicar, o sistema deve abrir uma nova tela ou modal com as informações detalhadas do processo selecionado. |
| ABRIR PROCESSO | O processo selecionado será identificado por seu ID ou outra chave única. |
| ABRIR PROCESSO | A tela/modal de detalhes deve permitir ao usuário visualizar todas as informações relevantes, como status, logs associados e dados do processo. |
| ABRIR PROCESSO | O botão Abrir Processo deve estar habilitado somente quando um processo estiver selecionado na lista. |
| ABRIR PROCESSO |  |
| ABRIR PROCESSO | ·  Após a abertura de um log na tela de detalhes, o usuário terá a opção de salvar esse log em um arquivo, utilizando o botão de Arquivos do sistema Tax One. |
| ABRIR PROCESSO | ·  Comportamento Esperado: |
| ABRIR PROCESSO | O botão de Arquivos será exibido na tela de detalhes do log, permitindo que o usuário faça o download ou exporte o log visualizado para um arquivo. |
| ABRIR PROCESSO | O formato de arquivo para exportação pode ser excell ou outro formato compatível com os requisitos do sistema Tax One. |
| ABRIR PROCESSO | O sistema deve fornecer uma interface simples para salvar o log, com um diálogo de escolha de pasta/local de destino. |
| ABRIR PROCESSO | Ao salvar, o sistema deve exibir uma mensagem de confirmação (ex.: "Log salvo com sucesso no arquivo [nome do arquivo]"). |
| ABRIR PROCESSO | Caso ocorra algum erro durante a exportação (ex.: erro de permissão), o sistema deve exibir uma mensagem de erro apropriada (ex.: "Erro ao salvar o log. Verifique as permissões do diretório."). |
| ABRIR PROCESSO |  |
| ABRIR PROCESSO |  |


---

| Nome | Regra |
| --- | --- |
| LOG | A aba LOG será responsável por exibir os registros de execução, incluindo logs detalhados e avisos gerados após a execução do botão Executar. Ela servirá para monitorar o processo, identificar possíveis erros e fornecer informações sobre o status da integração com o sistema Dootax. |
| LOG | Comportamento Esperado: |
| LOG | Exibição de Logs: |
| LOG | o    A aba LOG deve ser visível após a execução do botão Executar, com as informações de logs e mensagens relevantes. |
| LOG | o    A interface da aba LOG deve apresentar uma lista cronológica de eventos e registros, começando do mais recente. |
| LOG | o    Cada registro de log deve conter, no mínimo, os seguintes dados: |
| LOG | Data e hora da execução. |
| LOG | Descrição do evento (ex.: "Arquivo JSON gerado com sucesso", "Falha ao enviar para o Dootax"). |
| LOG | Detalhamento do status (ex.: "Sucesso", "Erro", "Aviso"). |
| LOG | ID da guia ou referência da transação relacionada ao evento (quando aplicável). |
| LOG | Mensagem adicional explicativa, se necessário (ex.: "Erro de autenticação ao tentar conectar com o Dootax"). |
| LOG | Filtros e Pesquisa: |
| LOG | o    Deve ser possível aplicar filtros para visualizar logs específicos, como: |
| LOG | Status (Sucesso, Erro, Aviso) |
| LOG | § Data/ Período de tempo |
| LOG | §  ID da guia ou outras informações relevantes. |
| LOG | o    A barra de pesquisa deve permitir buscar termos específicos dentro dos logs (ex.: "Erro", "Falha", "Sucesso", etc.). |
| LOG | Mensagens de Aviso e Erro: |
| LOG | o    Quando ocorrerem erros, os registros devem ser destacados visualmente (ex.: cor de fundo vermelha, ícone de alerta) e conter informações claras sobre a falha (ex.: "Erro na validação dos dados: campo obrigatório não preenchido"). |
| LOG | o    Avisos ou informações de sucesso devem ser destacados de maneira distinta, com mensagens explicativas (ex.: "Guias processadas com sucesso e enviadas para o Dootax"). |
| LOG | Atualização em Tempo Real: |
| LOG | o    A aba LOG deve ser atualizada automaticamente conforme novos registros de execução sejam gerados após o clique no botão Executar. |
| LOG | o    O usuário deve ser notificado em tempo real sobre o andamento do processo, especialmente em casos de falha ou erro. |
| LOG | Ações Disponíveis: |
| LOG | Exportar Logs: Deve ser possível exportar os logs em formato CSV ou TXT para análise externa ou auditoria. |
| LOG | Limpar Logs: Opcionalmente, o usuário pode limpar os logs antigos para manter a interface limpa e facilitar a análise de novos eventos. |


---

| Abertura de Nova Guia para Armazenamento do Relatório | Abertura de Nova Guia para Armazenamento do Relatório |
| --- | --- |
| Abertura de Nova Guia para Armazenamento do Relatório | Abertura de Nova Guia para Armazenamento do Relatório |
| Descrição | Após o usuário clicar no botão "Executar" e gerar os dados, o sistema deverá automaticamente criar uma nova guia no menu com o nome "Arquivo".   Nesta guia, será armazenado o relatório gerado na aba de execução, permitindo ao usuário acessá-lo posteriormente. |
| Origem dos Dados | Os dados do relatório serão resgatados de uma tabela temporária, onde são armazenados após a execução (geração dos dados). Esta tabela sofrerá atualizações sempre que houver comandos na tela de execução, garantindo que os dados do relatório reflitam sempre a versão mais recente. |
| Regras | 1. A nova guia "Arquivo" deve ser criada apenas se ainda não existir. 2. O relatório gerado na aba de execução deve ser salvo e acessível na guia "Arquivo". 3. O usuário poderá visualizar e fazer download do relatório a partir da guia "Arquivo". 4. Sempre que o usuário gerar um novo relatório, a tabela temporária será atualizada e o relatório armazenado na guia "Arquivo" deverá refletir essa atualização. 5. O relatório poderá ser salvo nos formatos Excel (.xlsx) e PDF (.pdf). 6. Após o envio dos dados (ação do botão "Fazer Envio"), o relatório deverá sofrer alterações e atualizações, principalmente de status. 7. A API de retorno será responsável por atualizar todas as informações das guias de pagamentos, refletindo qualquer mudança no relatório armazenado na guia "Arquivo". |


---

| Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento | Relatório de Integração das Guias de Pagamento |
| --- | --- | --- | --- | --- | --- | --- |
| ID GUIA | 100200 | 100300 | 100400 | 100500 | 100600 | 100700 |
| Número da Guia | 123456 | 789012 | 345678 | 901234 | 567890 | 123789 |
| Cod. Empresa | 001 | 001 | 001 | 001 | 001 | 001 |
| Cod. Estabelecimento | 0001 | 0001 | 0005 | 0007 | 0010 | 0012 |
| Período | 01/2025 | 02/2025 | 03/2025 | 04/2025 | 05/2025 | 06/2025 |
| Cod. Arrecadação | DAR | GNRE | DAE | DUA | DARE | DARJ |
| Cod. Receita | 13170 | 100048 | 759 | 1260 | 108 | 230 |
| Detalhamento Receita | ICMS | ICMS | ICMS | ICMS | ICMS | ICMS |
| Num. Doc. Origem | 98765 | 54321 | 67890 | 12345 | 11223 | 33445 |
| Série | 1 | 1 | 2 | 4 | 8 | 7 |
| UF Favorecida | SP | SP | MG | RS | BA | PR |
| CNPJ Favorecido | 12.345.678/0001-99 | 12.345.678/0001-99 | 01.234.567/0001-22 | 23.456.789/0001-33 | 45.678.901/0001-44 | 67.890.123/0001-55 |
| IE Favorecida | 123456789 | 123456789 | 123456789 | 654321987 | 789456123 | 321654987 |
| Valor Principal | R$            1.000,00 | ######### | ######### | ######### | R$   800,00 | ########## |
| Data de Vencimento | 10/01/2025 | 15/02/2025 | 20/03/2025 | 25/04/2025 | 30/05/2025 | 05/06/2025 |
| Data de Pagamento | 10/01/2025 | 16/02/2025 | 21/03/2025 | 26/04/2025 |  | 06/06/2025 |
| Valor Multa | R$                    50,00 | R$ 25,00 | R$  60,00 | R$ 30,00 | R$      40,00 | R$     55,00 |
| Valor Juros | R$                    20,00 | R$ 10,00 | R$  25,00 | R$ 15,00 | R$      20,00 | R$     30,00 |
| Info Complementar | - | Notas fiscais | - | - | - | - |
| Valor Fecp | 0 | 0 | 0 | 0 | 0 | 0 |
| Valor Fecp Multa | 0 | 0 | 0 | 0 | 0 | 0 |
| Valor Fecp Juros | 0 | 0 | 0 | 0 | 0 | 0 |
| Convênio |  |  |  |  |  |  |
| Cod. Produto |  |  |  |  |  |  |
| Chave DFE |  |  |  |  |  |  |
| Cadastro Part. |  |  |  |  |  |  |
| Cod. Mun. Favorecido |  |  |  |  |  |  |
| Valor Outros |  |  |  |  |  |  |
| Valor Base Cálculo |  |  |  |  |  |  |
| Campos Extras | N/A | N/A | N/A | N/A | N/A |  |
| Conta Contábil |  |  |  |  |  |  |
| Status da Guia | Em Processamento | Pago | Erro no Pagamento | Cancelado | Pago | Em Processamento |


---

| ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC  COD_EMPRESA GRUPO_FISCAL COD_ESTAB UF COD_ARRECADACAO GRUPO_IMPOSTO TIPO_IMPOSTO COD_RECEITA DETALHE_RECEITA CONVENIO PRODUTO INF_COMPLEMENTAR DIA_VENCTO REGRA_VENCTO CRITERIO_VENCTO REGRA_IMPOSTO DESCR_REGRA_IMPOSTO | FLUX_VW_ESTABELECIMENTO  COD_EMPRESA COD_ESTAB RAZAO_SOCIAL NOME_FANTASIA UF COD | FLUX_HEINEKEN_ESTAB_TEMP_CPROC  ID_PROC EMPRESA ESTAB DT_PERIODO GRP_IMP TAX UF_ESTAB SAIDA |
| --- | --- | --- |

