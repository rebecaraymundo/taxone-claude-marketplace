# MTZ_T1_Tela_Inicial_Módulo_Conciliacao

> Fonte: MTZ_T1_Tela_Inicial_Módulo_Conciliacao.docx






THOMSON REUTERS

ONESOURCE TAX ONE

Agrupamento > Reforma Tributária do Consumo

Módulo > CBS / IBS / IS

>> Conciliação





Sumário

1.	CONTROLE DE ALTERAÇÕES	3
2.	INTRODUÇÃO	4
2.1	Fonte de dados	6
2.2	Legislação	6
3.	DOCUMENTOS DE REFERÊNCIA	6
4.	DEFINIÇÃO DAS REGRAS	6
4.1	Telas de navegação	7
4.1.1	Módulo Conciliação - Tela inicial	10
4.1.1.1	Módulo Conciliação – cabeçalho da tela	12
4.1.1.2	Módulo Conciliação – Painel de Inconsistências	18
4.1.1.3	 Módulo Conciliação - Detalhes	27
5.	CENÁRIO DE TESTES	32


## CONTROLE DE ALTERAÇÕES

Descreva nesse item de forma geral tudo o que foi incluído, alterado ou excluído da especificação.





















## INTRODUÇÃO


- Objetivo
- Objetivo deste documento é descrever, de forma detalhada e padronizada, a trilha de acesso na Solução Fiscal ONESOURCE Tax One até o módulo da Reforma Tributária do Consumo, localizado no agrupamento "Reforma Tributária do Consumo", bem como orientar o acesso à aba "Conciliação" do módulo "CBS / IBS / IS".
- Adicionalmente, o documento registra os elementos de interface, o passo a passo de navegação e os estados visuais apresentados durante o percurso (por exemplo: menus, botões, breadcrumbs, telas intermediárias, habilitado/desabilitado, mensagens, carregamento e validações), para garantir reprodutibilidade, clareza operacional e padronização do acesso.

- Escopo do MVP
Esta versão contempla:
Seleção do Agrupamento: Reforma Tributária do Consumo;
Seleção do Módulo: CBS / IBS / IS
Seleção do modal: Conciliação
Estrutura de navegação como abas (Apuração e Conciliação) e componentes de UI (botões, gráficos, painéis e indicadores de status);
Conteúdo e comportamento da aba "Conciliação";
Estados visuais, mensagens do sistema e tratamento de situações de erros e alertas;
Descrição da Tela de Conciliação, incluindo as visões:
Transacional
Fiscal
Contábil

Fora de escopo do MVP
Não faz parte do escopo desta versão:
Os impostos: "ICMS / IPI / ICMS-ST / PIS-PASEP / COFINS;
Configurações do módulo na visão Contábil;
Integrações, requisitos não funcionais (performance) e segurança;
Observações
As regras de negócio referentes aos campos exibidos (definições, origem, cálculo, validações e exceções) serão especificadas e mapeados em outro documento.

## Fonte de dados


N/A
## Legislação


N/A

## DOCUMENTOS DE REFERÊNCIA


N/A
## DEFINIÇÃO DAS REGRAS


- O acesso ao modal de “Conciliação” deve seguir a trilha:
- No ONESOURCE Tax One
- 1 - Agrupamento “Reforma Tributária do Consumo”,
- 2 - Módulo “CBS / IBS / IS”,
- 3 – Modal “Conciliação”.

### Telas de navegação

- Acessando o ONESOURCE Tax One, ao selecionar a empresa, o estabelecimento (único ou todos), agrupamento “Reforma Tributária do Consumo” e módulo CBS / IBS / IS, o usuário será direcionado para um link externo onde acessará o módulo da RTC Apuração. Nessa tela poderá fazer o acesso ao modal “Conciliação” (funcionalidade que depende de licenciamento prévio contratado).





- Clientes sem contratação do módulo CONCILIAÇÃO não terão permissão de navegação.


- Acessando o ONESOURCE Tax One, ao selecionar a empresa, o estabelecimento (único ou todos), agrupamento “Reforma Tributária do Consumo” e módulo CBS / IBS / IS, o usuário será direcionado para um link externo onde acessará o módulo da RTC Apuração. Nessa tela poderá fazer o acesso ao modal “Conciliação” (funcionalidade que depende de licenciamento prévio contratado).







### Módulo Conciliação - Tela inicial


- A tela “Conciliação” da Reforma tributária do consumo deve permitir ao usuário visualizar o status da última conciliação, acompanhar indicadores através do Painel de Inconsistências entre Contribuinte x Fisco (Documentos ausentes, Débitos e Créditos) e acessar detalhes por categoria via seções expansíveis; deve também permitir executar uma nova conciliação e consultar o histórico das conciliações realizadas anteriormente.



### Módulo Conciliação – cabeçalho da tela

- A funcionalidade Conciliação permite ao usuário selecionar obrigatoriamente Empresa e Estabelecimento, pesquisar os dados da competência selecionada e, a partir do resultado, executar a conciliação. A tela também exibe um status informando se já houve conciliação e quando ela ocorreu, além de um indicador quantitativo (por exemplo, total de documentos sem inconsistências) para o recorte pesquisado.
- Além disso, a funcionalidade disponibiliza o Histórico de conciliações por meio de um modal, onde o usuário pode consultar registros anteriores com Data, Hora e Responsável. Esse histórico permite ordenar os registros (pelos cabeçalhos com ícone de ordenação) e pode conter múltiplas ocorrências semelhantes, pois cada linha representa um evento registrado. O modal é fechado pela ação Fechar, retornando o usuário à tela no mesmo estado em que estava.



















Botão: Visualizar histórico

Botão: Conciliar




Onde:




### Módulo Conciliação – Painel de Inconsistências

- A tela possui um Painel de inconsistências voltado para análise e acompanhamento das divergências entre Contribuinte e Fisco. De forma breve, as funções são:
- abas que permitem ao usuário alternar o modo de visualização entre Simplificada e Analítica, mudando o nível de detalhe apresentado.
- filtrar o painel por tributo (Ver todos, CBS, IBS ou IS), restringindo os dados exibidos ao recorte selecionado.
- comparar resultados entre Contribuinte e Fisco para os grupos de informação do painel (Documentos ausentes, Débitos e Créditos), exibindo também o total e a diferença de cada grupo.
- controlar a abrangência dos dados exibidos por meio da opção "Visualizar todos os dados abertos": quando ativada, inclui todos os registros abertos; quando desativada, mostra apenas os respectivos títulos das inconsistências.



Onde:








### 4.1.1.3		Módulo Conciliação - Detalhes


- Essa seção “Detalhes” tem como função apresentar e permitir a consulta rápida das inconsistências entre os valores do Contribuinte e do Fisco, separadas por natureza (Débitos e Créditos) e por tributo (CBS, IBS e IS).
- Dessa forma:
- exibe os totais do Contribuinte e do Fisco para cada tributo, em Débitos e Créditos;
- calcula e apresenta a diferença (divergência) entre as duas origens, indicando também de qual lado está a divergência (ex.: "(Contribuinte)" ou "(Fisco)" quando aplicável);
- permite o acesso ao detalhamento dos valores (quando os totais estiverem apresentados como link/clicáveis), direcionando o usuário para a lista de documentos/lançamentos que compõem o total selecionado.














Onde:







- NOTA:

- 1.Quando não houver nenhuma conciliação realizada para a o período, a tela deverá ser apresentada sem os dados e o status como “Conciliação não executada”.

- 2. Quando uma conciliação já tiver sido realizada anteriormente e o usuário acessar o módulo, então a tela deverá ser apresentada com os dados da última sessão finalizada, ou seja, mantendo os filtros de EMPRESA e ESTABELECIMENTO. A partir dessa visualização novas conciliações poderão ser executadas.

- 3. Quando entrar no módulo da Conciliação o usuário será direcionado para tela (aba) Simplificada, com a visão “Ver todos” do Painel de Inconsistências.

- 4. Painel de Inconsistências – Botões: para lançamento do módulo Conciliação manter o botão CBS selecionado. Os demais não terão ação.




## CENÁRIO DE TESTES

1. Acesso e Estado Inicial da Tela
Valida o acesso ao aplicativo e seu estado antes de qualquer interação do usuário.



| Data | Demanda | Descrição | Autor |
| --- | --- | --- | --- |
| 18/02/2026 | ???? | Especificação referente ao acesso via ONESOURCE Tax One e tela do módulo CBS / IBS / IS - “Conciliação” dos impostos, somente tela inicial, sem regras de negócio. | Elaine Brasil |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |  |
| --- | --- | --- | --- | --- | --- | --- |
| Breadcrumb principal ("Home / Tax One / Conciliação") | Breadcrumb | - | - | - | Criar o breadcrumb de navegação das telas, incluindo o rastreamento das telas por onde o sistema passou até chegar na tela atual. |  |
| Título da tela ("Reforma tributária do consumo") | Seção/Título | - | - | - | Exibe o título da funcionalidade/módulo atual acessado. |  |
| Subtítulo ("Conciliação") | Seção/Título | - | - | - | Exibe o nome da tela dentro do módulo. |  |
| Status ("Status: Conciliado em 01/01/2026 às 15:25") | Badge/Status | N | N | "Status: em DD/MM/AAAA às HH:MM" | Exibe o estado atual do processo e carimbo de data/hora. Status possíveis: - Conciliação não executada - Processando - Conciliada em DD/MM/AAA às 00:00h |  |
| Botão "Visualizar histórico" | Botão | N | N | Ação | Ao clicar, abre a visualização de histórico em formato modal, com as seguintes informações em 3 colunas: Data, Hora, Responsável. Todas as colunas permitiram colocar os dados em ordem crescente ou decrescente. Por padrão a aplicação exibirá os últimos 5 registros. Dentro do modal haverá duas formas de fechá-lo:  - pelo botão FECHAR localizado na base direita do modal ou - pelo botão X no topo direito do modal. |  |
| Botão "Conciliar" | Botão | N | N | Ação | Ao clicar no botão “Conciliar”, um modal é aberto para que o usuário possa indicar o período inicial e final da competência. Como regra o usuário só poderá conciliar uma amplitude de até 31 dias dentro de uma competência (observados os dias corridos dentro de cada mês do ano calendário). Informado o período o botão “conciliar” ficará ativo para ser acionado. Um botão “cancelar” também estará disponível para ser acionado a qualquer momento. Se a conciliação já estiver sido realizada o botão “conciliar” apresentará o estado desabilitado. Uma vez acionado o botão para concluir um pop up com a mensagem “Conciliação iniciada com sucesso.” será exibido. O usuário deverá clicar no botão “Fechar” para fechar o pop up. Se ocorrer algum erro técnico um pop up vermelho será aberto com a mensagem: "Infelizmente não foi possível executar a conciliação, tente novamente e caso o erro persista contate o administrador do sistema!” |  |
| Empresa | Dropdown combo | S | S | Padrão: Sem pré-seleção | Obrigatório. O dropdown deve exibir apenas empresas permitidos ao usuário logado. Ao consultar, filtrar resultados pela seleção. Se vazio, impedir consulta e mostrar mensagem "Campo Empresa é obrigatório. |  |
| Estabelecimento | Dropdown combo | S | S | Padrão: Sem pré-seleção | Obrigatório. O dropdown deve exibir apenas estabelecimentos permitidos ao usuário logado. Ao consultar, filtrar resultados pela seleção. Se vazio, impedir consulta e mostrar mensagem "Campo Estabelecimento é obrigatório”. |  |
| Limpar | Botão | S | N | Padrão: inativado | Ao acionar, resetar todos os campos ao estado inicial (defaults). |  |
| Pesquisar | Botão | S | N | Padrão: inativado | Ao acionar, validar campos obrigatórios. Se válido, executar consulta aplicando filtros preenchidos e atualizar a lista de resultados. Impedir múltiplos disparos. |  |
| Indicador: Documentos sem inconsistências | Badge/Status | - | - | Texto explicativo e indicador numérico | Exibe total de documentos sem inconsistências até o período já conciliado. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |  |
| --- | --- | --- | --- | --- | --- | --- |
| Simplificada | TabBar | - | N | Padrão: selecionada – visão do usuário ao acessar o módulo | Ao entrar no módulo de “Conciliação” usuário visualizará duas abas podendo navegar por ambas. Ao selecionar a aba, recarrega/atualiza os componentes da página conforme seu conteúdo. |  |
| Analítica | TabBar | - | N | Padrão: inativa | Alterna a visão para a versão "Analítica". Ao selecionar a aba, recarrega/atualiza os componentes da página conforme seu conteúdo. |  |
| Painel de inconsistências (container) | Seção/Container | S | N | Padrão: visível | Exibir 3 cards lado a lado (Documentos ausentes, Débitos, Créditos). Deve manter alinhamento e espaçamento responsivo. |  |
| Botões:  Ver todos | CBS | IBS | IS | Grupo de botões | N | S | Padrão: botão “Ver todos” selecionado. | Por padrão o usuário visualizará o montante dos documentos e impostos refletidos nos gráficos. Ao selecionar o botão referente a um dos impostos os gráficos deverão refletir o resultado referente apenas aquele imposto. Não é permitido selecionar mais de um imposto. Nota 4. |  |
| Card – Documentos ausentes | Card/Container | S | N | Título fixo | Deve exibir gráfico comparativo + legenda + resumo numérico (Quantidade de documentos - Total). |  |
| Gráfico – Documentos ausentes | Gráfico semicircular (gauge/donut) | S | N | Cores: Contribuinte (marrom), Fisco (verde) | Representar proporção/participação entre Contribuinte e Fisco. Se não houver dados, exibir estado "Sem dados" (ex.: 0/0) e não quebrar layout. |  |
| Legenda | Legenda/Chip | S | N | "Contribuinte" e "Fisco" | As cores da legenda devem corresponder às fatias do gráfico. |  |
| Quantidade | Seção/Divisão | S | N | Padrão: texto fixo | Exibe o texto centralizado: Quantidade de documentos - total |  |
| Contribuinte | KPI/Texto + link | S | N | Formato: inteiro com separador de milhar (ex.: 3.000) | Exibir total de documentos do Contribuinte. Quanto apresentar uma quantidade numérica do lado do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de detalhamento de "Documentos ausentes – Contribuinte". |  |
| Fisco | KPI/Texto | S | N | Formato: inteiro com separador de milhar (ex.: 2.967) | Exibir total de documentos do Fisco. |  |
| Diferença | KPI/Texto | S | N | Formato: inteiro com separador de milhar | Exibir o valor de diferença entre a contagem de documentos do Contribuinte e Fisco |  |
| Card – Débitos | Card/Container | S | N | Título fixo | Deve exibir gráfico comparativo + legenda + resumo "Valor dos Impostos - Total" (Contribuinte/Fisco). |  |
| Gráfico – Débitos | Gráfico semicircular (gauge/donut) | S | N | Cores: Contribuinte (vermelho), Fisco (azul escuro) | Representar proporção/participação entre débitos Contribuinte vs Fisco. Se valores forem 0, apresentar gráfico "zerado" e manter legenda. |  |
| Legenda – Débitos | Legenda/Chip | S | N | "Contribuinte" e "Fisco" | As cores devem corresponder às fatias do gráfico. |  |
| Valor dos impostos - Total | Seção/Divisão | S | N | Padrão: texto fixo | Exibe o texto centralizado: Valor dos impostos - Total |  |
| Rótulo – Impostos - Total (Débitos) | Label/Texto | S | N | Texto fixo | Exibir acima dos valores monetários do card de Débitos. |  |
| Total – Débitos / Contribuinte | KPI/Texto moeda | S | N | Padrão: R$ 0,00 | Exibir soma total de débitos do Contribuinte. Regra: sempre formatar em moeda BRL; suportar valores altos; tratar nulos como R$ 0,00. |  |
| Total – Débitos / Fisco | KPI/Texto moeda | S | N | Padrão: R$ 0,00 | Exibir soma total de débitos do Fisco. Regra: sempre formatar em moeda BRL; suportar valores altos; tratar nulos como R$ 0,00. |  |
| Diferença | KPI/Texto | S | N | Formato: inteiro com separador de milhar | Exibir o valor de diferença entre o valor de débitos do Contribuinte e Fisco |  |
| Card – Créditos | Card/Container | S | N | Título fixo | Deve exibir gráfico comparativo + legenda + resumo "Impostos - Total" (Contribuinte/Fisco). |  |
| Gráfico – Créditos | Gráfico semicircular (gauge/donut) | S | N | Cores: Contribuinte (laranja), Fisco (roxo) | Representar proporção/participação entre créditos Contribuinte vs Fisco. Se valores forem 0, apresentar gráfico "zerado". |  |
| Legenda – Créditos | Legenda/Chip | S | N | "Contribuinte" e "Fisco" | As cores devem corresponder às fatias do gráfico. |  |
| Rótulo: Valor dos impostos - Total | Seção/Divisão | S | N | Padrão: texto fixo | Exibe o texto centralizado: Valor dos impostos – Total (exibir acima dos valores monetários) |  |
| Total – Créditos / Contribuinte | KPI/Texto moeda | S | N | Padrão: R$ 0,00 | Exibir soma total de créditos do Contribuinte. Formatar em BRL; tratar nulos como 0,00. |  |
| Total – Créditos / Fisco | KPI/Texto moeda | S | N | Padrão: R$ 0,00 | Exibir soma total de créditos do Fisco. Formatar em BRL; tratar nulos como 0,00. |  |
| Diferença | KPI/Texto | S | N | Formato: inteiro com separador de milhar | Exibir o valor de diferença entre o valor de créditos do Contribuinte e Fisco |  |
| Estado – Erro ao carregar | Mensagem/Alerta | S | N | Padrão: oculto | Em falha de API/consulta, exibir mensagem de erro e opção de "Tentar novamente em alguns minutos". |  |
| Estado – Sem dados | Mensagem/Placeholder | S | N | Padrão: oculto | Quando retorno vazio/0, exibir "Sem dados no período" e manter estrutura do painel. |  |
| Regras de cálculo (base) | Regra de negócio | S | N | - | Os totais "Contribuinte" e "Fisco" devem ser calculados a partir da mesma base/recorte (mesmo período/filtros da tela). O gráfico deve refletir exatamente os mesmos números exibidos nos KPIs. |  |
| Visualizar todos os dados abertos | Toggle/Switch | N | S | Padrão: desligado (conforme print) | Ao alternar, deve atualizar os valores exibidos no painel (recarregar ou reaplicar filtro). Ligado (expandido): exibe todos os dados com detalhamento dos impostos CBS/IBS/IS. Desligado (retraído): exibe apenas os títulos de cada faixa. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |  |
| --- | --- | --- | --- | --- | --- | --- |
| Detalhes | Seção/Container | S | N | Padrão: visível | Agrupa e exibe os blocos "Divergências nos débitos" e "Divergências nos créditos". Deve manter layout em 3 colunas (CBS/IBS/IS) e separadores. |  |
| Inconsistências nos débitos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – CBS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Débitos nos Documentos do Contribuinte". |  |
| Inconsistências nos débitos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – IBS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Débitos nos Documentos do Contribuinte". |  |
| Inconsistências nos débitos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – IS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Débitos nos Documentos do Contribuinte". |  |
| Inconsistências nos créditos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – CBS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Créditos nos Documentos do Contribuinte". |  |
| Inconsistências nos créditos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – IBS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Créditos nos Documentos do Contribuinte". |  |
| Inconsistências nos créditos | Card/Bloco (Container) | S | N | Padrão: visível | Exibe comparativo de bases Contribuinte vs Fisco e a Diferença entre elas – IS. Quanto apresentar valores na linha do Contribuinte será acompanhada de um link clicável. Acionando-o navegar para tela de “Detalhamento de Créditos nos Documentos do Contribuinte". |  |
