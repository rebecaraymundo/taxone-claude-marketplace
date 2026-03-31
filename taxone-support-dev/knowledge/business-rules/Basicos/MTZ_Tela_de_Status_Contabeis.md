# MTZ_Tela de Status Contábeis

> Fonte: MTZ_Tela de Status Contábeis.docx






THOMSON REUTERS

Matriz da tela Contabilização

Tela de Status Contábeis


DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	3
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados:	3
4.	Tela de Status Contábeis Funcionalidades:	5
4..1.	Parâmetro:	5
4..2.	Processos:	8
4..1.	Arquivos	9
4..2.	Log	10
4..3.	REGRAS DE NEGÓCIO	12
4..1.	Exemplo de arquivo gerado:	13


## Introdução


A tela de status é projetada para proporcionar aos usuários uma visão clara e atualizada do status dos arquivos JSON gerados, desde a criação até o envio. Essa tela desempenha um papel crucial na gestão e no monitoramento dos processos de lançamentos contábeis, garantindo transparência e controle efetivo sobre as operações realizadas. Todas as informações geradas na tela da geração serão espelhadas no Relatório de Status

## Documento de Referência


MTZ _Tela Seleção de dados
MTZ _ Tela de Parâmetros Ajustes da Apuração Contábeis
MTZ_Tela de Parâmetros de Outros Lançamentos Contábeis
MTZ_Tela de Estorno Contábeis
MTZ_Tela Lançamentos complementares
MTZ_Tela Geração do Arquivo
MTZ_Tela Relatório de Status

## Fluxo Principal Seleção de dados:

Este caso de uso descreve o processo para a geração de arquivos – Lançamentos Contábeis




Localização da Tela:

- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >> Tela de Status Contábeis
- Menu: Acesso Principal >> Tela de Status Contábeis



Prótotipo




## Tela de Status Contábeis Funcionalidades:

- Visualização de Status: Mostrar o status atual de cada arquivo JSON, como "Aguardando Envio", "Em Processamento", "Enviado" ou "Erro".
- Ações Disponíveis: Permitir que o usuário execute ações como reenviar um arquivo que falhou no envio inicial ou cancelar um envio que ainda está no Status “"Aguardando Envio"

## Parâmetro:


















## Processos:




## Arquivos




## Log


Botões












































| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO 915377 | Millys Lopes | Tela de Status Contábeis |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | Os parâmetros devem estar configurados corretamente no sistema através das telas de Ajustes da Apuração e Outros Lançamentos Contábeis O processo de estorno e os lançamentos complementares devem ser realizados, contabilização automática caso sejam necessários. Geração do Arquivo: A geração do arquivo deve ser efetuada na tela de geração, assegurando que o arquivo insumo esteja completo e que os dados estejam prontos para visualização na tela de status. |
| Pós-Condições | Os arquivos disponíveis para envio do JSON devem ser exibidos na tela de status. O usuário deve clicar no botão "Executar" para realizar o envio dos arquivos JSON. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário acessa a Tela Status | O sistema exibe o menu principal com as opções disponíveis: Parâmetros, Processos e Arquivos. |
| O usuário clica no botão "Parâmetros": | O Sistema abre a tela de Parâmetros, permitindo ao usuário  para configurar filtros e critérios como datas, grupos de impostos e outras especificações necessárias. |
| Usuário clicar no botão processos | O sistema exibe a tela de Processos, apresentando uma lista detalhada dos processos registrados, com informações como status e data de geração. |
| Usuário clicar no botão executar | O sistema exibe a lista de arquivos gerados, permitindo que o usuário visualize ou baixe os arquivos conforme as configurações realizadas. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Campo | S | S | Código Descrição | Exibe o código e a descrição da empresa que selecionada |  |
| Estabecimento | Checkbox | S | S | Default: Não selecionado | Lista os códigos e descrições dos estabelecimentos vinculados à empresa selecionada. |  |
| UF | Checkbox | Não | S | Default: Não selecionado | Lista as UFs dos estabelecimentos vinculados ou todas as UFs. |  |
| Grupo Imposto | Dropdown | Sim | Sim | Default: Não preenchido | Todos", "Federal”, Estadual" “Extra_Apur”. |  |
| Imposto | Dropdown | Sim | Sim | Default: Não preenchido | Ao selecionar o 'Grupo Imposto', as opções disponíveis serão:  'Federal' for selecionado, os tributos listados serão: PIS Cumulativo PIS Não Cumulativo COFINS Cumulativo COFINS Não Cumulativo IPI  'Estadual' for selecionado, os tributos listados serão: ICMS Próprio ICMS-ST (Substituição Tributária) ICMS Antecipado FCP (Fundo de Combate à Pobreza) DIFAL (Diferencial de Alíquota) SCANC  'Extra_Apur' for selecionado, os tributos listados serão ICMS-ST (Importado via SAFX-345) |  |
| Periodo | Campo | Sim | Sim | MM/AAAA | Este campo deve ser preenchido pelo usuário com o mês (MM) e o ano (AAAA) do exercício da apuração para que seja possível buscar os dados gravados. O preenchimento correto é crucial, pois determina o período específico associado ao imposto previamente selecionado. A data inserida define o intervalo temporal necessário para a busca e o processamento adequado dos dados fiscais |  |
| Tipo de Lançamentos Contábil | Dropdown | S | S | Texto | Dropdown Este campo permite ao usuário selecionar o tipo de lançamentos contábeis que deseja incluir na geração de arquivos. A seleção é crucial para especificar o escopo dos dados a serem processados. As opções disponíveis no menu dropdown são: Todos os Lançamentos: Inclui todos os registros disponíveis para a geração de arquivos contábeis. Ajustes da Apuração: Inclui somente os ajustes específicos realizados durante o processo de apuração. Outros Lançamentos: Inclui somente os outros lançamentos específicos realizados durante o processo de apuração. Extra Apuração: Refere-se aos dados importados relacionados ao processo de extra apuração via Safx 345. Complemento da Apuração: Inclui lançamentos adicionais que complementam a apuração inicial. Estorno: Permite a reversão de lançamentos previamente contabilizados.  Regras de Funcionamento: O sistema deve realizar uma busca nas tabelas geradas através da Tela de Geração com base nos seguintes parâmetros informados pelo usuário: Empresa, Estabelecimento, UFs, Grupo de Imposto, Imposto, Periodo Caso não sejam identificados dados gerados para os parâmetros informados, o sistema exibirá a seguinte mensagem de erro: "Não foram identificados dados gerados para os parâmetros informados. Por favor, verifique se há apuração para o período selecionado ou realize a geração dos dados correspondentes ao período informado." |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Processos Gerados nos últimos | Campo | Sim | Sim | Númerico |  |  |
| Nº Processo | Lista | Sim | Sim | Númerico | Um número único de processo deve ser gerado automaticamente toda vez que uma operação de geração for realizada. Esse número servirá para controle interno e dará visibilidade ao usuário, permitindo que ele visualize todos os processos gerados ou pesquise por um processo específico. |  |
| Descrição | Lista | Sim | Sim | Alfanúmerico | A descrição deve detalhar informações como a data de apuração, o imposto envolvido e o estabelecimento ao qual o processo está vinculado. Essa descrição ajudará o usuário a identificar rapidamente os dados relacionados a cada processo. |  |
| Situação | Lista | Sim | Sim | Dropdown | Esta regra deve mostrar ao usuário o status atual do arquivo gerado, indicando se a execução está "Iniciada" ou "Encerrada". Essa informação proporciona transparência e permite que o usuário acompanhe o progresso das operações. |  |
| Início Execução | Data/Hora | Sim | Sim | DD/MM/AAAA HH:MM | A tela deve exibir a data e a hora em que a execução do processo foi iniciada. Essa informação é crucial para que o usuário possa monitorar e gerenciar as operações em tempo real, assegurando que esteja ciente do início das atividades. |  |
| Fim Execução | Data/Hora | Sim | Sim | DD/MM/AAAA HH:MM | Deve-se mostrar a data e a hora em que a execução do processo foi concluída. Essa informação é importante para o usuário avaliar a duração da operação e para documentação de quando os processos são finalizados. |  |
| Usuário | Lista | Sim | Sim | Texto | Esta regra deve exibir o nome do usuário  que realizou a geração do arquivo. A apresentação dessa informação é essencial para rastrear a responsabilidade pelas operações executadas |  |
| Será permito um arquivo por periodo/cod ajuste/conta contabil |  |  |  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Controle de quantidades de arquivos | Campo | Sim | Sim | Númerico |  |
| Status de arquivo | Lista | Sim | Sim | Númerico | Um número único de processo deve ser gerado automaticamente toda vez que uma operação de geração for realizada. Esse número servirá para controle interno e dará visibilidade ao usuário, permitindo que ele visualize todos os processos gerados ou pesquise por um processo específico. |
| Exclusão de arquivos | Lista | Sim | Sim | Alfanúmerico | A descrição deve detalhar informações como a data de apuração, o imposto envolvido e o estabelecimento ao qual o processo está vinculado. Essa descrição ajudará o usuário a identificar rapidamente os dados relacionados a cada processo. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Salvar Arquivos Selecionados | Lista | Sim | Sim |  | Esta funcionalidade permite que o usuário visualize e selecione arquivos gerados, associados a números de processos específicos e visualizar arquivos sem número de processos ou seja que apresentaram erro de logs |  |
| Título | Lista | Sim | Sim |  | Demostrar para usuário as informações a seguir: Nome do Arquivo: O nome do arquivo gerado. Data de Geração: A data em que o arquivo foi criado. Formato do exemplo de listagem: " - Nome: IPI_202508.TXT |  |
