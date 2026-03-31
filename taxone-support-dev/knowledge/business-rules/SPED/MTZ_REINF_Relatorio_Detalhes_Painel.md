# MTZ_REINF_Relatorio_Detalhes_Painel

> Fonte: MTZ_REINF_Relatorio_Detalhes_Painel.docx






THOMSON REUTERS

Módulo EFD-REINF
Relatório de Detalhes do Painel

Localização: Menu SPED, Módulo: EFD-REINF, item de menu Relatórios  Relatório de Detalhes do Painel



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
1.1.	Layout da Tela	8
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	9
2.1.	Layout do Relatório	18

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD-REINF, item de menu Relatórios > Relatório de Detalhes do Painel
Título da tela: Relatório de Detalhes do Painel
























### Layout da Tela





## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas informações das seguintes origens:

Painel de Controle de Eventos menu: (“REINF > Painel > Painel de Controle de Eventos”).

Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

O usuário poderá escolher uma das seguintes opções de geração possíveis do relatório através do campo Tipo de Relatório na tela de geração do relatório:

- “Listagem de Eventos Gerados por Período/Status”;
- “Detalhamento do Histórico por Evento”;
- “Relação de Recibos por Evento Recebido com Sucesso/Advertência”;

A seguinte regra será aplicada para o modelo de relatório Listagem de Eventos Gerados por Período/Status:

Serão recuperados todos os eventos gerados que são demostrados no Painel de acordo com, Período, Estabelecimento(s), Eventos(s), Situação(es) e Tipo(s) de Arquivo informados na tela.
Para que os eventos sejam recuperados, deverá ser respeitado o período informado na tela de geração do relatório.

A seguinte regra será aplicada para o modelo de relatório Detalhamento do Histórico por Evento:

Serão recuperados todos históricos dos eventos gerados que são demostrados no Painel de acordo com, Período, Estabelecimento(s), Eventos(s), Situação(es) e Tipo(s) de Arquivo informados na tela.
Para que os históricos dos eventos sejam recuperados, deverá ser respeitado o período informado na tela de geração do relatório.


A seguinte regra será aplicada para o modelo de relatório Relação de Recibos por Evento Recebido com Sucesso/Advertência:

Serão recuperados todas as relações de recibos gerados dos eventos que foram recebidos com Sucesso/Advertência que são demostrados no Painel de acordo com, Período, Estabelecimento(s), Eventos(s), Situação(es) igual a “Evento Recebido pelo Fisco com Sucesso” e/ou “Evento Recebido pelo Fisco com Advertência” e Tipo(s) de Arquivo informados na tela.
Somente serão recuperados os eventos que estiver com a situação igual a “Evento Recebido pelo Fisco com Sucesso” e/ou “Evento Recebido pelo Fisco com Advertência” que são status que geram número de recibo.
Para que os recibos dos eventos sejam recuperados, deverá ser respeitado o período informado na tela de geração do relatório.


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “SEM MOVIMENTO” no relatório.


Regra de agrupamento:

A seguinte regra será aplicada para o modelo de relatório Listagem de Eventos Gerados por Período/Status:

•	Serão agrupados todos os eventos por Situação/Status.

A seguinte regra será aplicada para o modelo de relatório Detalhamento do Histórico por Evento:

•	Serão agrupados todos históricos por Evento, Identificação de Evento, Tipo de Arquivo, Ambiente e ID Evento.

A seguinte regra será aplicada para o modelo de relatório Relação de Recibos por Evento Recebido com Sucesso/Advertência:

•	Serão agrupados todos os recibos por Eventos com a situação igual a “Evento Recebido pelo Fisco com Sucesso” e/ou “Evento Recebido pelo Fisco com Advertência”.



Ordenação:

Para o modelo de relatório Listagem de Eventos Gerados por Período/Status, os dados serão ordenados da seguinte forma:

- Estabelecimento
- Situação
- Evento

Para o modelo de relatório Detalhamento do Histórico por Evento, os dados serão ordenados da seguinte forma:

- Estabelecimento
- Evento
- Data/Hora Evento por ordem Decrescente, do mais atual ao mais antigo.

Para o modelo de relatório Relação de Recibos por Evento Recebido com Sucesso/Advertência, os dados serão ordenados da seguinte forma:

- Estabelecimento
- Evento


Segue regras do preenchimento dos dados no relatório:



### Layout do Relatório


Consultar o Layout no Excel: Relatorio_de_Detalhes_do_Painel.xlsx

Layout para o Tipo de Relatório = “Listagem de Eventos Gerados por Período/Status”
Aba: Eventos Gerados Período-Status

Layout para o Tipo de Relatório = “Detalhamento do Histórico por Evento”
Aba: Histórico por Evento

Layout para o Tipo de Relatório = “Relação de Recibos por Evento Recebido com Sucesso/Advertência”
Aba: Recibos p Evento Sucesso-Advert



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS18744 | Lara Aline | Criação do Relatório de Detalhes do Painel |
| MFS20746 | Lara Aline | Retirar obrigatoriedade do campo Tipo de Arquivo quando selecionado eventos R-2098 ou R-2099. |
| MFS-47276 | Alessandra Cristina Navatta | Incluir o evento R-2055 - Aquisição de Produção Rural. |
| MFS-79881 | Alessandra Cristina Navatta | Incluir o evento R-1050 – Tabela de Entidades Ligadas |
| MFS-79893 | Alessandra Cristina Navatta | Incluir o R-4040 - Pagamentos/créditos a beneficiários não identificados |
| MFS-79907 | Alessandra Cristina Navatta | Incluir o evento R-4080 – Retenção no Recebimento |
| MFS-79885 | Alessandra Cristina Navatta | Incluir o evento R-4010 - Pagamentos/créditos a beneficiário pessoa física |
| MFS-79890 | Alessandra Cristina Navatta | Incluir o evento R-4020 - Pagamentos/créditos a beneficiário pessoa jurídica |
| MFS-79914 | Alessandra Cristina Navatta | Incluir o evento r-4099 no mesmo tratamento da obrigatoriedade do campo tipo de arquivo (quando selecionado o evento de fechamento) |
| MFS-578020 | Alessandra Cristina Navatta | Inclusão do check-box “Considerar R-4010/R-4020 Arquivos Externos (JCP)” (grid Eventos) no filtro da tela do relatório. |
| MFS-783762 | Bruna Ribeiro | Inclusão de um check-box para controle da geração de relatório em formato XLS. Quando selecionado, o sistema gerará o relatório nesse formato. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Relatório de Detalhes do Painel | ComboBox | S | S | Default: Não selecionado | Este parâmetro definirá o formato de geração do relatório.  Deverão ser listadas as seguintes opções:   Normal Formato XLS | MFS-783762 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Permitir que o usuário informe o período para emissão do relatório. | MFS18744 |
| Tipo do Relatório | ComboBox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:   Listagem de Eventos Gerados por Período/Status; Detalhamento do Histórico por Evento;  Relação de Recibos por Evento Recebido com Sucesso/Advertência; | MFS18744 |
| Eventos | Checkbox | S | S | Default: Todos | Permitir que o usuário informe quais eventos serão emitidos no relatório, Serão listadas as seguintes opções:  R-1000 – Informações do Contribuinte R-1050 – Tabela de Entidades Ligadas R-1070 – Processos Administrativos/Judiciais R-2010 – Retenção de Contribuição Previdenciária – Serviços Tomados R-2020 – Retenção de Contribuição Previdenciária – Serviços Prestados R-2040 – Recursos Recebidos ou Repassados para Clube de Futebol R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria R-2055 - Aquisição de Produção Rural R-2060 – Contribuição Previdenciária Sobre a Receita Bruta – CPRB R-4010 - Pagamentos/créditos a beneficiário pessoa física R-4020 - Pagamentos/créditos a beneficiário pessoa jurídica R-4040 - Pagamentos/créditos a beneficiários não identificados R-4080 – Retenção no Recebimento | MFS18744 MFS-47276 MFS-79881 MFS-79893 MFS-79907 MFS-79885 MFS-79890 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status de todos os eventos para “selecionado” | MFS18744 |
| Considerar R-4010/R-4020 Arquivos Externos (JCP) | Checkbox | N | S | Default: não selecionado | Quando selecionado, inclui na recuperação das informações os eventos de origem arquivos externos (JCP), se selecionados os eventos R-4010 e/ou R-4020. Caso desmarcado, quando os eventos 4010/4020 forem selecionados na grid Eventos, não serão recuperados os eventos R-4010/R-4020 de origem externa. | MFS-578020 |
| Situação | Checkbox | S | S | Default: Todos | Permitir que o usuário informe quais situações serão emitidos no relatório, Serão listadas as seguintes opções:  Aguardando Geração do XML Gerando XML  Enviando para Mensageria  Erro na Geração do XML Evento Recebido pela Mensageria Evento Rejeitado pela Mensageria Em Processamento (Mensageria) Evento Recebido pelo Fisco com Sucesso Evento Recebido pelo Fisco com Advertência Evento Rejeitado pelo Fisco Evento Cancelado Evento Excluído na Mensageria Erro Técnico na Mensageria  Tratamento: Se o usuário selecionar no campo Tipo de Relatório a opção “Relação de Recibos por Evento Recebido com Sucesso/Advertência” ficaram habilitadas e selecionadas somente as situações:  Evento Recebido pelo Fisco com Sucesso Evento Recebido pelo Fisco com Advertência  Sem possibilidade de alteração. | MFS18744 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status de todas as situações para “selecionado” | MFS18744 |
| Tipo do Arquivo: | Checkbox | S | S | Default: Todos | Permitir que o usuário informe quais os tipos de arquivos serão emitidos no relatório, Serão listadas as seguintes opções:  Original Retificação Inclusão  Alteração Exclusão   Campo obrigatório, exceto se selecionados os eventos R-2098, R-2099 ou R-4099. A não obrigatoriedade acontecerá se for selecionado apenas os eventos R-2098, R-2099 ou R-4099 individualmente sem seleção de nenhum outro evento. | MFS18744 MFS20746 MFS-79914 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status de todos os tipos de arquivos para “selecionado” | MFS18744 |
| Estabelecimentos | Caixa de seleção de estabs. | S | S | Default: não selecionado | Serão disponibilizados os estabelecimentos que atendam aos seguintes critérios:      - Estabelecimentos parametrizados nos dados iniciais (menu: “Parâmetros  Dados Iniciais”).   A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos existentes para o período informado, cujo eventos já foram gerados e estão sendo apresentados no Painel de Controle de Eventos.  (A pesquisa é baseada na tabela “OC” do eventos,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; | MFS18744 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível selecionar todos os estabelecimentos demostrados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado. | MFS18744 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível desmarcar todos os estabelecimentos que estão selecionados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado. | MFS18744 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS18744 |
| Data | Data | Formato: DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS18744 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS18744 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS18744 |
| Título | Texto |  | Título do relatório, de acordo com o Tipo de Relatório informado na tela de emissão podendo ser:  “Listagem de Eventos Gerados por Período/Status”, “Detalhamento do Histórico por Evento” ou  “Relação de Recibos por Evento Recebido com Sucesso/Advertência” | MFS18744 |
| Período | Numérico | Formato: MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Emissão. | MFS18744 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado na tela de emissão. | MFS18744 |
| Situação/Status | Texto |  | Situação informada na tela de emissão. Essa informação corresponde ao campo Situação da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Eventos Gerados Período-Status e Recibos p Evento Sucesso-Advert Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Evento | Texto |  | Evento informado na tela de emissão. Essa informação corresponde ao campo ‘Evento’ da aba Eventos Gerados no Período do Painel de Controle de Eventos. | MFS18744 |
| Identificação do Evento | Texto |  | Essa informação corresponde ao campo ‘Identificação do Evento’ da aba Eventos Gerados no Período do Painel de Controle de Eventos. | MFS18744 |
| Tipo de Arquivo | Texto |  | Essa informação corresponde ao campo ‘Tipo de Arquivo’ da aba Eventos Gerados no Período do Painel de Controle de Eventos. | MFS18744 |
| Ambiente | Texto |  | Essa informação corresponde ao campo ‘Ambiente’ da aba Eventos Gerados no Período do Painel de Controle de Eventos. | MFS18744 |
| ID Evento | Texto |  | Essa informação corresponde ao campo ‘ID Evento’ da aba Eventos Gerados no Período do Painel de Controle de Eventos. | MFS18744 |
| Atualização na Mensageria | Data | Formato: DD/MM/AAAA às HH:MM:SS hs | Essa informação corresponde ao campo ‘Atualização na Mensageria’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Eventos Gerados Período-Status Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Data/Hora Evento | Data | Formato: DD/MM/AAAA às HH:MM:SS hs | Essa informação corresponde ao campo ‘Data/Hora Evento’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas nos layouts dos relatórios das abas Histórico por Evento e Recibos p Evento Sucesso-Advert. Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Protocolo Onesource | Alfanumérico |  | Essa informação corresponde ao campo ‘Protocolo Onesource’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Histórico por Evento.  Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Status | Alfanumérico |  | Essa informação corresponde ao campo ‘Status’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Histórico por Evento.  Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Código da Mensageria | Alfanumérico |  | Essa informação corresponde ao campo ‘Código da Mensageria’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Histórico por Evento.  Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Descrição da Mensagem | Alfanumérico |  | Essa informação corresponde ao campo ‘Descrição da Mensagem’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Histórico por Evento.  Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Código de Recibo | Alfanumérico |  | Essa informação corresponde ao campo ‘Código de Recibo’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas nos layouts dos relatórios das abas Histórico por Evento e Recibos p Evento Sucesso-Advert. Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
| Hashcode | Alfanumérico |  | Essa informação corresponde ao campo ‘Hashcode’ do Histórico dos eventos, o Histórico está localizado na opção ‘Mais’ do campo ‘Ações’ da aba Eventos Gerados no Período do Painel de Controle de Eventos.  Esse campo será demonstrado apenas no layout do relatório da aba Histórico por Evento.  Excel: Relatorio_de_Detalhes_do_Painel.xlsx | MFS18744 |
