# MTZ_REINF_Relatorio_Detalhes_Painel_FormatoXLS

> Fonte: MTZ_REINF_Relatorio_Detalhes_Painel_FormatoXLS.docx






THOMSON REUTERS

Módulo EFD-REINF
Relatório de Detalhes do Painel

Localização: Menu SPED, Módulo: EFD-REINF, item de menu Relatórios  Relatório de Detalhes do Painel> Formato XLS



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

Painel de Controle de Eventos menu: (“REINF > Painel > Painel de Controle de Eventos> Formato XLS”).

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




### Layout do Relatório


Relatório será gerado no formato Excel para cada evento selecionado: Relatorio_de_Detalhes_do_Painel.xlsx

Layout para o Tipo de Relatório = “Listagem de Eventos Gerados por Período/Status”
Aba: Eventos Gerados Período-Status

Layout para o Tipo de Relatório = “Detalhamento do Histórico por Evento”
Aba: Histórico por Evento

Layout para o Tipo de Relatório = “Relação de Recibos por Evento Recebido com Sucesso/Advertência”
Aba: Recibos p Evento Sucesso-Advert



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-783762 | Bruna Ribeiro | Inclusão de um check-box para controle da geração de relatório em formato XLS. Quando selecionado, o sistema gerará o relatório nesse formato. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Permitir que o usuário informe o período para emissão do relatório. | MFS-783762 |
| Tipo do Relatório | ComboBox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:   Listagem de Eventos Gerados por Período/Status; Detalhamento do Histórico por Evento;  Relação de Recibos por Evento Recebido com Sucesso/Advertência; | MFS-783762 |
| Eventos | Checkbox | S | S | Default: Todos | Permitir que o usuário informe quais eventos serão emitidos no relatório, Serão listadas as seguintes opções:  R-1000 – Informações do Contribuinte R-1050 – Tabela de Entidades Ligadas R-1070 – Processos Administrativos/Judiciais R-2010 – Retenção de Contribuição Previdenciária – Serviços Tomados R-2020 – Retenção de Contribuição Previdenciária – Serviços Prestados R-2040 – Recursos Recebidos ou Repassados para Clube de Futebol R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria R-2055 - Aquisição de Produção Rural R-2060 – Contribuição Previdenciária Sobre a Receita Bruta – CPRB R-4010 - Pagamentos/créditos a beneficiário pessoa física - SAFX53 R-4010 - Pagamentos/créditos a beneficiário pessoa física – Arquivo externo  R-4020 - Pagamentos/créditos a beneficiário pessoa jurídica – SAFX53 R-4020 - Pagamentos/créditos a beneficiário pessoa jurídica – Arquivo externo  R-4040 - Pagamentos/créditos a beneficiários não identificados R-4080 – Retenção no Recebimento | MFS-783762 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status de todos os eventos para “selecionado” | MFS-783762 |
| Situação | Checkbox | S | S | Default: Todos | Permitir que o usuário informe quais situações serão emitidos no relatório, Serão listadas as seguintes opções: Todos Aguardando Geração do XML Gerando XML  Enviando para Mensageria  Erro na Geração do XML Evento Recebido pela Mensageria Evento Rejeitado pela Mensageria Em Processamento (Mensageria) Evento Recebido pelo Fisco com Sucesso Evento Recebido pelo Fisco com Advertência Evento Rejeitado pelo Fisco Evento Cancelado Evento Excluído na Mensageria Erro Técnico na Mensageria  Tratamento: Se o usuário selecionar no campo Tipo de Relatório a opção “Relação de Recibos por Evento Recebido com Sucesso/Advertência” ficaram habilitadas e selecionadas somente as situações:  Evento Recebido pelo Fisco com Sucesso Evento Recebido pelo Fisco com Advertência  Sem possibilidade de alteração. | MFS-783762 |
| Estabelecimentos | Caixa de seleção de estabs. | S | S | Default: não selecionado | Serão disponibilizados os estabelecimentos que atendam aos seguintes critérios:      - Estabelecimentos parametrizados nos dados iniciais (menu: “Parâmetros  Dados Iniciais”).   A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos existentes para o período informado, cujo eventos já foram gerados e estão sendo apresentados no Painel de Controle de Eventos.  (A pesquisa é baseada na tabela “OC” do eventos,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; | MFS-783762 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível selecionar todos os estabelecimentos demostrados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado. | MFS-783762 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível desmarcar todos os estabelecimentos que estão selecionados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado. | MFS-783762 |
