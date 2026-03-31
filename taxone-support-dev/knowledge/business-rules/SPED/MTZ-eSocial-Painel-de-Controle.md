# MTZ-eSocial-Painel-de-Controle

> Fonte: MTZ-eSocial-Painel-de-Controle.docx






THOMSON REUTERS

Módulo eSocial

Painel de Controle dos Eventos


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Painel de Controle dos Eventos


DOCUMENTO DE REQUISITO



Sumário

1.	Layout e Funções do Painel	2
2.	Funcionamento dos campos do Quadro “Parâmetros para Consulta”	5
3.	Funcionamento dos campos do Quadro “Eventos Gerados no Período”	10
4.	RN01 - Recuperação dos Dados dos Eventos	23
5.	RN02 - Geração e Envio dos Arquivos XML	27
6.	RN03 - Download dos Arquivos XML	28
7.	RN04 - Cancelamento de Eventos	29
8.	RN05 - Geração Evento de Exclusão	29
9.	RN06 – Reprocessar Evento	30
10.	RN06 – Histórico do Evento	33



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.





## Layout e Funções do Painel


Esta rotina foi originalmente criada na MFS15868, com apenas duas funcionalidades: Geração e Download dos Arquivos XML.

Posteriormente, foi alterada na MFS16750 para inclusão novas funcionalidades. Esta MFS alterou a tela para apresentar todas as novas funcionalidades (envio dos arquivos p/o integrador do Onesource, cancelamento de eventos, geração de eventos de exclusão, etc .....), nos mesmos padrões do módulo REINF.

Relação das ações:




Layout:




## Funcionamento dos campos do Quadro “Parâmetros para Consulta”







## Funcionamento dos campos do Quadro “Eventos Gerados no Período”


Neste quadro são exibidos todos os eventos que atendam aos parâmetros informados, e o usuário poderá selecionar os eventos desejados para execução de diversas ações.

A seguir serão descritas as regras sobre o funcionamento dos campos deste quadro.

(sobre os critérios p/ recuperação dos eventos a serem demonstrados, ver item “4-RN01-Recuperação dos Dados dos Eventos”)

Observar que as funções “Gerar e Enviar XML”, “Download do XML”, “Cancelar Evento” e “Gerar Evento de Exclusão” estão presentes em dois pontos da tela:

- Na barra de menu do quadro “Eventos Gerados no Período”

- Na coluna “Ações” da linha de detalhe de cada evento

A funcionalidade é exatamente a mesma, a diferença é que na primeira opção a ação é realizada para todos os eventos que estiverem selecionados, e na segunda opção a ação se restringe ao evento da linha em que a opção foi ativada.

No entanto, dependendo do local de onde a ação for ativada, algumas regras sobre habilitar a opção ou não são diferentes.





## RN01 - Recuperação dos Dados dos Eventos


Ao clicar no botão <Consultar>, todos os eventos que atendam aos parâmetros informados pelo usuário serão exibidos no quadro “Eventos gerados no período”.

Abaixo estão descritos os critérios para recuperação dos eventos de cadastro e de movimento, de acordo com os parâmetros informados pelo usuário.

As informações dos eventos recuperados serão exibidas conforme com as regras descritas no item anterior (item “3-Funcionamento dos Campos do Quadro Eventos Gerados no Período”).

Critérios para a recuperação dos eventos de CADASTRO a serem exibidos:

Os eventos de cadastro serão considerados na consulta apenas quando o parâmetro “Tipo de Arquivo” for um dos valores abaixo:

- Todos
- Inclusão (Cadastro)
- Alteração (Cadastro)
- Exclusão (Cadastro)

Os eventos de cadastro serão recuperados a partir das tabelas utilizadas na geração dos dados, considerando para filtro os seguintes critérios:

- Empresa = empresa do login;

- Estabelecimento = apenas os estabelecimentos centralizadores selecionados pelo usuário;

- Evento = apenas os eventos de cadastro (S-1005, S-1010, S-1020 e S-1070) selecionados pelo usuário;

- Validade Inicial do cadastro = deve ser uma data que se enquadre no período informado pelo usuário.

- Versão = a versão da geração dos cadastros deve ser a versão informada no campo “Versão”;

- Considerar apenas os eventos cujo status tenha sido selecionado pelo usuário no campo “Situação”;

- Considerar apenas os eventos do Tipo de Arquivo informado pelo usuário, da seguinte forma:

Se parâmetro “Tipo de Arquivo” = “Todos”
Considerar os eventos de cadastro de qualquer tipo, seja inclusão, alteração ou exclusão de dados;
Se parâmetro “Tipo de Arquivo” = “Inclusão (Cadastro)”
Considerar apenas os eventos de inclusão de dados (eventos com dados no registro inclusão);
Se parâmetro “Tipo de Arquivo” = “Alteração (Cadastro)”
Considerar apenas os eventos de alteração de dados (eventos com dados no registro alteração);
Se parâmetro “Tipo de Arquivo” = “Exclusão (Cadastro)”
Considerar apenas os eventos de exclusão de dados (eventos com dados no registro exclusão);





Critérios para a recuperação dos eventos de MOVIMENTO a serem exibidos:

Os eventos de movimento serão considerados na consulta apenas quando o parâmetro “Tipo de Arquivo” for um dos valores abaixo:

- Todos
- Original (Movimento)
- Retificação (Movimento)

Os eventos de movimento serão recuperados a partir das tabelas utilizadas na geração dos dados, considerando para filtro os seguintes critérios:

- Empresa = empresa do login;

- Estabelecimento = apenas os estabelecimentos centralizadores selecionados pelo usuário;

[MFS20750]
[MFS-87543]

- Evento = apenas os eventos de movimento (S-1200, S-1210, S-1250 e S-1300) selecionados pelo usuário;

- Mês/Ano de referência do movimento (***) = mês/ano do período informado pelo usuário.

- Versão = a versão da geração dos movimentos deve ser a versão informada no campo “Versão”;

- Considerar apenas os eventos cujo status tenha sido selecionado pelo usuário no campo “Situação”.

- Considerar apenas os eventos do Tipo de Arquivo informado pelo usuário, da seguinte forma:

Se parâmetro “Tipo de Arquivo” = “Todos”
Considerar os eventos de movimento de qualquer tipo, seja original ou retificação;
Se parâmetro “Tipo de Arquivo” = “Original (Movimento)”
Considerar apenas os eventos cujo campo indRetif (registro ideEvento) = “1” (arquivo original);
Se parâmetro “Tipo de Arquivo” = “Retificação (Movimento)”
Considerar apenas os eventos cujo campo indRetif (registro ideEvento) = “2” (arquivo de retificação);






## RN02 - Geração e Envio dos Arquivos XML


Para cada evento selecionado será gerado um arquivo XML, com base no layout do eSocial da versão informada pelo usuário (campo versão).

Observar os eventos válidos para este procedimento, conforme descrito nas regras do item “3-Funcionamento dos campos do Quadro “Eventos Gerados no Período”.

A geração dos arquivos XML é feita com base nos dados gerados previamente, nos menus “Geração dos Cadastros” e “Geração dos Movimentos”.

Estes arquivos são armazenados numa tabela (staging area – OUT), que posteriormente será utilizada para importação dos dados pelo integrador do Onesource, e também para download dos arquivos numa pasta selecionada pelo usuário (opção  <Download do XML>).

Para cada evento processado, será feita a atualização do status do evento, da seguinte forma:

- Arquivo XML gerado com sucesso  o status será alterado para “3” (Enviando para mensageria);

- Quando ocorrer erro na geração do XML  o status será alterado para “4” (Erro Geração XML);

No caso do status “3-Enviando para mensageria”, o evento ficará disponível para ser lido pelo integrador do Onesource.

Ao finalizar a geração, exibir uma mensagem de geração efetuada com sucesso.


## RN03 - Download dos Arquivos XML


Para cada evento selecionado, será feito o download do arquivo XML de envio, e dos arquivos XML de retorno que possam existir.

Observar os eventos válidos para este procedimento, conforme descrito nas regras do item “3-Funcionamento dos campos do Quadro “Eventos Gerados no Período”.

Os arquivos serão gravados no diretório de destino informado pelo usuário no campo “Pasta de download do XML”, e serão nomeados da seguinte forma:

XML de envio:     “ID_CODEVENTO_ENV.XML”

XML de retorno:  “ID_CODEVENTO_RET_SEQ.XML”

Sendo:

[MFS20750]
[MFS-87543]

ID: Identificador do evento (conteúdo do campo “id”);
CODEVENTO: Código do evento (S-1005, S-1010, S-1020, S-1070, S-1200, S-1210, S-1250, S-1300);

SEQ: Sequencial do XML de retorno (apenas para os arquivos XML de retorno);

O conteúdo “ENV” e “RET” é fixo, e define o tipo de arquivo (XML enviado p/o integrador, ou retornado do integrador).

Ao finalizar a gravação dos arquivos, exibir uma mensagem de download efetuado com sucesso.


## RN04 - Cancelamento de Eventos


(Obs.: A opção “Cancelamento” é na verdade a exclusão do Evento)

Todos os eventos selecionados para esta ação, terão seus dados excluídos das tabelas auxiliares utilizadas na geração dos dados (tabelas utilizadas nas rotinas de Geração dos Cadastros e Geração dos Movimentos para armazenar os dados dos eventos).

Desta forma, os eventos excluídos não aparecerão mais em nenhuma consulta ou relatório.

Observar os eventos válidos para este procedimento, conforme descrito nas regras do item “3-Funcionamento dos campos do Quadro “Eventos Gerados no Período”.

Ao finalizar a exclusão dos dados, exibir uma mensagem de cancelamento efetuado com sucesso.


## RN05 - Geração Evento de Exclusão


Para cada um dos eventos selecionados será gerado um evento de exclusão.

Observar os eventos válidos para este procedimento, conforme descrito nas regras do item “3-Funcionamento dos campos do Quadro “Eventos Gerados no Período”.

A ação de gerar um evento de exclusão consiste em dois procedimentos:


1- Gerar o evento de exclusão S-3000 referenciando o evento original em questão;

2- Alterar o status do evento original em questão para “Excluído (Gerado Evento de Exclusão)”;



## RN06 – Reprocessar Evento


Para cada evento selecionado será regerado um arquivo XML, com base no layout do eSocial da versão informada pelo usuário (campo versão).

Observar os eventos válidos para este procedimento, conforme descrito nas regras do item “3-Funcionamento dos campos do Quadro “Eventos Gerados no Período”.

Estes arquivos são armazenados numa tabela (staging area – OUT), que posteriormente será utilizada para importação dos dados pelo integrador do Onesource, e também para download dos arquivos numa pasta selecionada pelo usuário (opção <Download do XML>).

Para cada evento reprocessado, será feita a atualização do status do evento, da seguinte forma:

- Arquivo XML gerado com sucesso  o status será alterado para “3” (Enviando para mensageria);

- Quando ocorrer erro na geração do XML  o status será alterado para “4” (Erro Geração XML);

No caso do status “3-Enviando para mensageria”, o evento ficará disponível para ser lido pelo integrador do Onesource.



Gravação dos dados do evento “S-3000 – Exclusão de Eventos”:

Obs.: Além dos dados que serão armazenados para posterior geração do XML, será armazenado também o identificador do evento objeto da exclusão (campo “Id”). O objetivo de armazenar esta informação é mostrar ao usuário qual o evento que foi excluído, através da coluna “Referência” do painel.

Registro evtExclusão – Evento de Exclusão



Registro ideEvento - Informações de Identificação do evento.



Registro ideEmpregador - Informações de Identificação do empregador.




Registro infoExclusao – Identificação do evento objeto da exclusão.




Registro ideTrabalhador – Informações de identificação do trabalhador.

Este registro será gerado apenas quando o evento objeto da exclusão for = S-1200 ou S-1210.

[MFS20750]
[MFS-87543]
Quando a exclusão for referente aos eventos S-1250 ou S-1300, estes registros não serão gerados.



Registro ideFolhaPagto – Identificação da folha de pagamento do evento excluído.

Este registro informa o período da apuração referente ao evento objeto da exclusão.



Ao finalizar a geração dos eventos de exclusão, exibir uma mensagem de geração efetuada com sucesso.


## RN06 – Histórico do Evento



Os dados do histórico do evento são recuperados da tabela de log (ESOCIAL_PGER_LOG_MSG), que contém as informações sobre os retornos do integrador, e também os erros ocorridos na geração do XML.

Caso não existam informações sobre o histórico do evento, será exibida a mensagem:


Caso contrário, será aberta uma janela com o layout abaixo, onde serão exibidas as informações sobre o histórico do evento, registro a registro.

Será exibido um registro de histórico por linha, utilizando barra de rolagem quando necessário.

Os registros de histórico serão ordenados por data, do mais atual para o mais antigo, e para uma mesma data, ordenados por número de protocolo.

Layout da janela de exibição do histórico:




Preenchimento dos campos:




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15868 | Geração dos Arquivos XML | Criação do item de menu para a geração dos arquivos XML | 16/01/2018  (criação do documento) |
| MFS17022 | Alteração na tela da geração | Incluído o campo “Referência” para demonstrar uma informação que identifique o evento exibido em tela. | 05/03/2018 |
| MFS16750 | Inclusão de funcionalidades no painel | Inclusão de novas funcionalidades no painel do eSocial | 13/03/2018 |
| MFS18065 | Atualização do eSocial para versão 2.4.02. | Alteração da versão demonstrada no campo “Versão” da tela da geração | 07/06/2018 |
| MFS16762 | Lara Aline | Inclusão rotina de Reprocessar Evento | 28/08/2018 |
| MFS20750 | Lara Aline | Inclusão do evento S-1250 | 03/10/2018 |
| MFS27266 | Alessandra Cristina Navatta | Inclusão de filtro de funcionário, na tela do painel (para os eventos S-1200, S-1210). | 29/08/2019 |
| MFS-87292 | Elisabete Costa | Alterações  para versão S-1.0 | 06/06/2022 |
| MFS-87543 | Elisabete Costa | Exclusão dos eventos S-1250 e S-1300 para versão S-1.0 | 06/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Geração dos Arquivos XML e Envio p/o Integrador do Onesource |
| --- |
| Download dos Arquivos XML gerados |
| Cancelamento de Eventos |
| Geração de Eventos de Exclusão |
| Consulta do Histórico do Evento |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano dos eventos a serem exibidos para seleção.  Deve ser um mês válido. |
| Versão | Alfanumérico | S | N | Listbox | Este campo é uma lista, com as opções: [2.4.01] 2.4.02 2.5.00 S-1.0  (MFS18065: Alteração para versão 2.4.02) (MFS-87292: Alteração para a versão S-1.0) |
| Tipo do Arquivo | Alfanumérico | S | N | Listbox Default: Todos | Este campo é uma lista com as seguintes opções:  - Todos - Original (Movimento) - Retificação (Movimento) - Inclusão (Cadastro) - Alteração (Cadastro) - Exclusão (Cadastro)  (Todos=0, Original=1, Retificação=2, Inclusão=I, Alteração=A e Exclusão=E) |
| Eventos | Alfanumérico | S | N |  | Neste quadro são exibidos os eventos para seleção do usuário:  S-1005 - Estabelecimentos S-1010 - Rubricas S-1020 - Lotações  S-1070 - Processos Administrativos / Judiciais S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social S-1210 - Pagamentos de Rendimentos do Trabalho [MFS20750] [MFS-87543] S-1250 - Aquisição de Produção Rural S-1300 – Contribuições Sindicais  A partir da versão S1.0 não devem ser exibidos os eventos S-1250 e S-1300.  Através da opção “Marcar Todos” o usuário poderá marcar e desmarcar simultaneamente todos os eventos. |
| Situação | Alfanumérico | S | N |  | Neste quadro são exibidos os status dos eventos para seleção do usuário:  - Aguardando Geração do XML - Enviando para Mensageria - Erro na Geração do XML - Recebido pela Mensageria - Rejeitado pela Mensageria - Em Processamento (Mensageria) - Recebido pelo Fisco com Sucesso - Recebido pelo Fisco com Advertência - Rejeitado pelo Fisco - Excluído (Gerado Evento de Exclusão)  - Excluído na Mensageria - Erro Técnico na Mensageria  Através da opção “Marcar Todos” o usuário poderá marcar e desmarcar simultaneamente todos os status.  Obs.: Não foram tratados os status “Gerando XML”, “Evento Cancelado” e “Evento Rejeitado”, pois estes status constam no REINF, mas não são utilizados.  (para ver o código referente a cada status, consultar a planilha “Status_eSocial”) |
| Estabelecimentos Centralizadores | Alfanumérico | S | N |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos da Empresa cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (lembrando que esta parametrização só trabalha com os estabelecimentos centralizadores das obrigações federais)  [MFS20750] [MFS-87543] Caso no campo Eventos for selecionado o evento S-1250 - Aquisição de Produção Rural: A partir da versão S1.0 não devem ser exibidos os eventos S-1250 Serão disponibilizados para seleção todos os estabelecimentos da Empresa que possuam vinculo de centralização com os estabelecimentos centralizadores cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (Nesse caso está parametrização trabalhará com os estabelecimentos centralizadores e os estabelecimentos centralizados nesses centralizadores nas obrigações federais.) |
| Selecionar | Alfanumérico | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimentos Centralizadores”:  - Somente Estabelecimentos da empresa do login; - Somente Estabelecimentos parametrizados nos Dados Iniciais;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos Centralizadores” já marcados. |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos Centralizadores”. |
| Selecionar | Filtro | N | S |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais funcionários através de uma janela de seleção da tabela de funcionários.  O filtro dos funcionários disponibilizados para seleção segue a mesma regra descrita para o quadro “Funcionários”: - Somente Funcionários dos estabelecimentos selecionados e dos eventos S-1200 ou S-1210.  Quando esta opção é utilizada, após escolher os funcionários e clicar no botão <OK> da janela de seleção, os funcionários selecionados pelo usuário serão demonstrados no quadro “Funcionários” já marcados.  Na tela padrão de seleção serão exibidas as colunas: Evento, Código Estabelecimento, Código Pessoa Física, Nome, CPF. |
| Funcionários | Quadro |  |  |  | Neste quadro serão exibidas a lista dos funcionários dos estabelecimentos selecionados no quadro “Estabelecimentos Centralizadores”.  Os eventos que apresentam informações de funcionários são os S-1200 e S-1210.  Os registros devem ser ordenados por evento, Cód. Empresa, Cód. Estabelecimento, e Cód. Pessoa Física  Se nenhum destes dois eventos forem selecionados, o quadro “Funcionário” deve ficar desabilitado. |
| Marcar todos | Check-box | - | - |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os funcionários demonstrados no quadro “Funcionários”. |
| Consultar | Alfanumérico | N | N |  | Ao clicar neste botão, os eventos que atendam aos parâmetros informados serão exibidos no quadro “Eventos gerados no período”. Ver regras sobre a exibição dos eventos no item “4-RN01-Recuperação dos Dados dos Eventos”.  Antes de exibir os eventos, será verificado se o integrador está disponível, e caso contrário, será exibida a seguinte mensagem:  “O integrador está fora, envio indisponível. Verifique com o Administrador do Sistema”   Somente após a exibição da mensagem, é que será feita a consulta e exibição dos eventos.   Obs.: Observar que mesmo com o integrador fora, existem várias ações que o usuário pode realizar. Na verdade, a única ação que será bloqueada neste caso é ”Gerar/Enviar XML” |
| Limpar | Alfanumérico | N | N |  | Ao clicar neste botão, todos os parâmetros informados para consulta serão limpos. |
| Pasta de download do XML | Alfanumérico | N | N |  | Este campo exibe a lista dos diretórios para que o usuário selecione a pasta desejada, onde será feito o download dos arquivos XML. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os eventos demonstrados no quadro “Eventos gerados no período”. |
| Gerar e Enviar XML | Alfanumérico | N | N |  | Esta opção ficará desabilitada sempre que uma, ou as duas condições abaixo forem verdadeiras:     - Não existir nenhum evento selecionado;    - O integrador estiver fora;  Se o integrador estiver fora (ver campo <Consultar>), ao passar o mousse sobre esta opção, aparecerá a seguinte mensagem: “O integrador está fora, envio indisponível”.  Caso as duas condições acima sejam falsas, ao clicar nesta opção será verificado se alguns dos eventos selecionados tem o status diferente de “Aguardando Geração do XML”. Caso sim, será exibida a seguinte mensagem, e os eventos nesta situação serão desconsiderados da geração/envio do XML.  A geração e envio dos arquivos XML só é permitida para os eventos com situação = “Aguardando Geração do XML”. Os eventos com situações diferentes serão desconsiderados da geração   A seguir, serão gerados os arquivos XML para todos os eventos selecionados, que tenham status = “Aguardando Geração do XML”.  Ver regras da geração e envio dos arquivos XML no item “5-RN02-Geraçao e Envio dos Arquivos XML”. |
| Download do XML | Alfanumérico | N | N |  | Esta opção ficará desabilitada sempre que não existirem eventos selecionados.   Ao clicar neste botão será verificado se o usuário informou a pasta para a gravação dos arquivos no campo “Pasta de Download do XML”. Caso não, será exibida a mensagem abaixo, e a ação não será executada:  “Favor informar a pasta para download dos arquivos”  O download será feito apenas para os eventos com XML já gerado, ou seja, os eventos com status = “Aguardando Geração do XML” serão desconsiderados, uma vez que o XML não foi gerado ainda.  Ver regras sobre o download dos arquivos XML no item “6-RN03-Downlod os Arquivos XML”. |
| Cancelar Evento | Alfanumérico | N | N |  | Esta opção ficará desabilitada sempre que não existirem eventos selecionados.   Ao clicar neste botão será apresentada a seguinte mensagem de confirmação:  A ação “Cancelar Evento” exclui todos os dados do evento.                         Deseja continuar?                          <Sim>   <Não>  Caso “Não”, a ação não será realizada.  Caso “Sim” a execução da ação prossegue normalmente, e será feita a seguinte verificação:  Se algum dos eventos selecionados tiver o status diferente das opções listadas a seguir, será exibida a mensagem abaixo, e os eventos nesta situação serão desconsiderados do cancelamento.  - Aguardando Geração do XML; - Erro na Geração do XML;  - Excluído na Mensageria; - Erro Técnico na Mensageria;  O cancelamento de eventos só é permitido para os eventos com situação = “Aguardando Geração do XML”,  “Erro na Geração do XML”, “Excluído na Mensageria” e “Erro Técnico na Mensageria”. Os eventos com situações diferentes serão desconsiderados do cancelamento.  A seguir, será feita a exclusão de todos os eventos selecionados, cujo status seja igual às opções citadas acima. Ver regras da ação de cancelamento no item “7-RN04-Cancelamento de Eventos”. |
| Gerar Evento de Exclusão | Alfanumérico | N | N |  | Esta opção ficará desabilitada sempre que não existirem eventos selecionados.   [MFS20750]  [MFS-87543] Esta opção é válida apenas para os eventos S-1200, S-1210, S-1250 e S-1300, com status de já recebido pelo Fisco.  A partir da versão S1.0 não devem ser exibidos os eventos S-1250 e S-1300 Por isso, será verificado se dentre os eventos selecionados pelo usuário existe eventos nas situações a seguir:    - Eventos diferentes de S-1200, S-1210, S-1250 e S-1300;    - Eventos S-1200, S-1210, S-1250 ou S-1300 com status diferente     de “Recebido pelo Fisco com Sucesso” e “Recebido pelo     Fisco com Advertência”  Caso sim, será exibida a mensagem abaixo, e os eventos nestas situações serão desconsiderados da geração.  A geração de eventos de exclusão só é permitida para os eventos S-1200, S-1210, S-1250 e S-1300, com situação = “Recebido pelo Fisco com Sucesso” ou “Recebido pelo Fisco com Advertência”. Os eventos fora destas condições serão desconsiderados da geração.  A seguir, será feita a geração dos eventos de exclusão para todos os eventos selecionados, considerando apenas os eventos S-1200, S-1210, S-1250 e S-1300, cujo status seja igual às opções citadas acima. Ver regras da geração dos eventos de exclusão no item “8-RN05-Geração dos Eventos de Exclusão”. |
| Reprocessar Evento | Alfanumérico | N | N |  | Este terá a função de reprocessar os eventos que estejam com situação de ‘Evento recebido pelo fisco com sucesso’, ‘Evento recebido pelo fisco com advertência’, ‘Evento rejeitado pela mensageria’ ou ‘Evento Rejeitado pelo Fisco’.  Caso selecionado o botão “*Marcar todos” e houver registros com situação diferente de:   Evento recebido pelo fisco com sucesso Evento recebido pelo fisco com advertência  Evento rejeitado pela mensageria Evento Rejeitado pelo Fisco  Exibir a seguinte mensagem:  Ação de Reprocessar evento não é permitido para registros com situação diferente de:   Evento recebido pelo fisco com sucesso  Evento recebido pelo fisco com advertência  Evento rejeitado pela mensageria Evento Rejeitado pelo Fisco  Estes registros serão desconsiderados.  Caso acionado o botão sem selecionar ao menos um registro a seguinte mensagem deverá ser apresentada:   “Ao menos um registro deve ser selecionado.”  Caso o evento estiver com situação Evento recebido pelo fisco com sucesso ou Evento recebido pelo fisco com advertência o evento será reprocessado e será criada uma nova linha do evento com o tipo do arquivo Retificação, ou seja, se o evento já foi recepcionado pelo fisco com sucesso/advertência o botão reprocessar Evento será uma retificação onde será mandado para o fisco o evento corrigido.  Caso o evento estiver com situação Evento rejeitado pela mensageria ou Evento Rejeitado pelo Fisco o evento será reprocessado e será criada uma nova linha do evento com o mesmo tipo do arquivo do evento original, ou seja, se o evento que foi rejeitado pela mensageria/fisco for do tipo do arquivo Original e nova linha criada será do tipo do arquivo Original, caso o tipo for Retificação a nova linha será do tipo Retificação. O botão reprocessar Evento será um reprocessamento do mesmo evento com os ajustes necessários para que seja enviado com sucesso. |
| Ações |  |  |  |  | Sob a coluna “AÇÕES”, ficarão todas as funcionalidades que o usuário poderá executar isoladamente para um determinado evento.  As opções são as seguintes:  No primeiro botão – opção Gerar/Enviar XML  No segundo botão – opção Download do XML  No terceiro botão – opção Reprocessar Evento  No campo lista, as demais opções:     - Histórico    - Cancelar Evento    - Gerar Evento de Exclusão  Tanto os botões “Gerar/Enviar XML”, “Download do XML” e “Reprocessar Evento”, como o campo lista com as demais opções, serão habilitados apenas se o evento da linha em questão estiver selecionado.  O funcionamento de cada uma destas opções está descrito nas regras a seguir. |
| Ações – Gerar/Enviar XML | Alfanumérico | N | N |  | A geração/envio do XML a partir desta opção, depende das seguintes condições:  - O evento deve estar selecionado - Status deve ser = Aguardando Geração do XML” - O integrador deve estar ativo;  Quando uma ou mais condições não forem atendidas:  Neste caso, esta opção ficará desabilitada. E caso o integrador esteja fora (ver campo <Consultar>), ao passar o mousse sobre esta opção, aparecerá a seguinte mensagem: “O integrador está fora, envio indisponível”.  Quando as três condições forem atendidas:  Neste caso, será gerado o arquivo XML referente ao evento selecionado.  Ver regras da geração e envio dos arquivos XML no item “5-RN02-Geraçao e Envio dos Arquivos XML”. |
| Ações – Download do XML | Alfanumérico | N | N |  | Esta opção será habilitada apenas quando:  - O evento estiver selecionado; - O status for <> “Aguardando Geração do XML”;  Quando alguma destas condições não for verdadeira, esta opção ficará desabilitada.  Ao clicar neste botão será verificado se o usuário informou a pasta para a gravação dos arquivos no campo “Pasta de Download do XML”. Caso não, será exibida a mensagem abaixo, e a ação não será executada:  “Favor informar a pasta para download do arquivo”  Ver regras sobre o download dos arquivos XML no item “6-RN03-Downlod os Arquivos XML”. |
| Ações – Reprocessar Evento | Alfanumérico | N | N |  | Este terá a função de fazer o reprocessamento do evento.  Esta opção será habilitada apenas quando:  - O evento estiver selecionado; - O status for = “Evento recebido pelo fisco com sucesso”, “Evento recebido pelo fisco com advertência”, “Evento rejeitado pela mensageria” ou “Evento Rejeitado pelo Fisco”; - O período estiver “Aberto ou Reaberto”.;  Quando alguma destas condições não for verdadeira, esta opção ficará desabilitada.  Ver regras sobre o Reprocessar Evento no item “9-RN06 – Reprocessar Evento”. |
| Ações - Histórico | Alfanumérico | N | N |  | Obs.: Conforme descrito acima para a coluna “AÇÕES”, esta lista de opções será habilitada apenas se o evento da linha em questão estiver selecionado.  Esta ação é permitida para qualquer status de evento. Caso não existam dados no histórico, será exibida uma mensagem (ver detalhes na RN06 citada abaixo).  Ver regras sobre a exibição do histórico do evento no item “9-RN06-Histórico do Evento”. |
| Ações – Cancelar Evento | Alfanumérico | N | N |  | Obs.: Conforme descrito acima para a coluna “AÇÕES”, esta lista de opções será habilitada apenas se o evento da linha em questão estiver selecionado.  Quando esta opção da lista for acionada, e o status do evento for diferente das opções listadas a seguir, será exibida a mensagem abaixo e a ação não será realizada:   - Aguardando Geração do XML; - Erro na Geração do XML;  - Excluído na Mensageria; - Erro Técnico na Mensageria;  O cancelamento de eventos não é permitido para a situação deste evento.  Se o status do evento for válido para a ação, será exibida uma mensagem de confirmação, da seguinte forma:  A ação “Cancelar Evento” exclui todos os dados do evento.                         Deseja continuar?                          <Sim>   <Não>  Caso “Não”, a ação não será realizada.  Caso “Sim”, será feita a exclusão do evento conforme as regras descritas no item “7-RN04-Cancelamento de Eventos”. |
| Ações – Gerar Evento de Exclusão | Alfanumérico | N | N |  | Obs.: Conforme descrito acima para a coluna “AÇÕES”, esta lista de opções será habilitada apenas se o evento da linha em questão estiver selecionado.  Quando esta opção da lista for acionada, e o status do evento for diferente das opções listadas a seguir, será exibida a mensagem abaixo e a ação não será realizada:   - Recebido pelo Fisco com Sucesso - Recebido pelo Fisco com Advertência  A geração de eventos de exclusão não é permitida para a situação deste evento.  Ver regras da geração dos eventos de exclusão no item “8-RN05-Geração dos Eventos de Exclusão”. |
| Colunas das informações dos eventos: |  |  |  |  | Ver regras sobre a recuperação dos dados dos eventos no item “4-RN01-Recuperação dos Dados dos Eventos”. |
| Estabelecimento | Alfanumérico | N | N |  | Código e razão social do estabelecimento centralizador para o qual foi gerado o evento. |
| Evento | Alfanumérico | N | N |  | [MFS-87543] Sigla do evento: S-1005, S-1010, S-1020, S-1070, S-1200, S-1210, S-1250 ou S-1300.  A partir da versão S-1.0 não devem ser exibidos os eventos S-1250 e S-1300. |
| Referência | Alfanumérico | N | N |  | O objetivo desta coluna é mostrar ao usuário alguma informação que identifique o evento em questão.  A informação a ser exibida depende do tipo de evento, da seguinte forma:  S-1005 – Campo nrInsc do registro ideEstab, no formato:      N. Inscrição Estabelecimento: XXXXXXXXXXXXXXX  S-1010 – Campos ideTabRubr e codRubr do registro ideRubrica (tabela e código da Rubrica), no formato:  Tabela/Cód Rubrica: XXXXXXX - XXXXXXXXXXXXXXX    S-1020 – Campos codLotacao do registro ideLotacao (código do setor), no formato:         Lotação: XXXXXXXXXXXXXXXXXXXXXXX   S-1070 – Campos tpProc e nrProc do registro ideProcesso (tipo e número do processo), no formato:      Tipo/Número do Processo: X - XXXXXXXXXXXXXXXX   S-1200 – Campo cpfTrab do registro ideTrabalhador, no formato:                CPF Trabalhador: XXX.XXX.XXX-XX   S-1210 – Campo cpfBenef do registro ideBenef, no formato:                CPF Beneficiário: XXX.XXX.XXX-XX     [MFS20750] [MFS-87543] S-1250 – Campo nrInscAdq do registro infAquisProd, no formato:        N. Inscrição Adquirente: XXX.XXX.XXX-XX   [MFS-87543 S-1300 – Campo nrInsc do registro ideEmpregador, no formato:        N. Inscrição Empregador: XXXXXXXXXXXXXXX  S-3000 – Campo tpEvento do registro infoExclusao, e a informação do ID do evento objeto da exclusão, no formato:    Evento excluído: X-XXXX Id: XXXXXXXXXXXXXXXXXX  Obs.: O evento S-3000 é um evento gerado pelo próprio painel, conforme a opção “Gerar Evento de Exclusão”. Observar que a informação do ID do evento original (objeto da exclusão) não consta no layout do S-3000, mas é uma informação armazenada internamente para termos a referência do evento original. |
| Situação | Alfanumérico | N | N |  | Neste campo será exibida a descrição do status do evento, conforme aa descrições a seguir:  1- Aguardando Geração do XML 3- Enviando para Mensageria 4- Erro na Geração do XML 5- Recebido pela Mensageria 6- Rejeitado pela Mensageria 7- Em Processamento (Mensageria) 8- Recebido pelo Fisco com Sucesso 9- Recebido pelo Fisco com Advertência 10- Rejeitado pelo Fisco 12- Excluído  14- Excluído na Mensageria 15- Erro Técnico na Mensageria |
| Tipo do Arquivo | Alfanumérico | N | N |  | Neste campo será exibido o tipo do evento, conforme os tipos existentes:  - Original - Retificação - Inclusão - Alteração - Exclusão  “Original” é um evento de movimento com o campo indRetif = “1”;  “Retificação” é um evento de movimento com o campo indRetif = “2”;  “Inclusão” é um evento de cadastro onde os dados informados estão no registro inclusão;  “Alteração” é um evento de cadastro onde os dados informados estão no registro alteração;  “Exclusão” é um evento de cadastro onde os dados informados estão no registro exclusão; |
| Identificação do Evento | Alfanumérico | N | N |  | Código de identificação única do evento, conforme regras do layout do eSocial.  Trata-se da informação gerada para o campo “id”, presente em todos os eventos. |


| Exemplo sobre as datas de validade, supondo os seguintes cadastros:  Cad01 – validade inicial = 01/01/2017 Cad02 – validade inicial = 01/05/2017 Cad03 – validade inicial = 20/05/2017 Cad04 – validade inicial = 10/06/2017  Na Geração dos Dados para o período de 05/2018 a 06/2018, seriam gerados os cadastros:  - Cad02 – validade inicial = 01/05/2017 - Cad03 – validade inicial = 20/05/2017 - Cad04 – validade inicial = 10/06/2017  Na Geração dos Dados para o período de 06/2018 a 06/2018, seriam gerados os cadastros:  - Cad04 – validade inicial = 10/06/2017  Na Geração do XML para o período = 05/2018, seriam gerados os cadastros:  - Cad02 – validade inicial = 01/05/2017 - Cad03 – validade inicial = 20/05/2017  Na Geração do XML para o período = 06/2018, seriam gerados os cadastros:   - Cad04 – validade inicial = 10/06/2017 |
| --- |


| (***) Este mês/ano de referência do movimento varia de acordo com o movimento, e é exatamente o período usado para filtro na rotina da “Geração dos Movimentos”:  - Para o evento S-1200, é o mês/ano de competência do Demonstrativo de Pagamento; - Para o evento S-1210, é o mês/ano do pagamento; - Para o evento S-1250, é o mês/ano de competência da Aquisição de Produção; - Para o evento S-1300, é o mês/ano da contribuição sindical; |
| --- |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:  “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita.  Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora.   Obs. No caso deste evento de exclusão, o CNPJ a ser considerado será o mesmo CNPJ do campo “id” do evento objeto da exclusão. |
| --- | --- |


| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais”  A parametrização “Dados Iniciais” é por estabelecimento centralizador.   Para gerar o evento de exclusão, a recuperação dos dados da parametrização será feita considerado o estabelecimento do evento objeto da exclusão (a informação poderia ser copiada do evento original, no entanto, a parametrização pode ter sido alterada). |
| --- | --- |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do empregador) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”. |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | Neste campo será gravada a informação do campo nrInsc do registro ideEmpregador do evento objeto da exclusão. |


| tpEvento | [MFS20750] [MFS-87543] Tipo do evento objeto da exclusão: S-1200, S-1210, S-1250 ou S-1300. |
| --- | --- |
| nrRecEvt | Número do recibo gerado pelo Fisco, referente a entrega do evento objeto da exclusão  Obs.: Esta informação é gravada na tabela que contém os retornos do integrador. É a coluna RECIBO_ONESOURCE da STG_EVENTOS_ESOCIAL_IN. _ |


| cpfTrab | Neste campo será gravado o mesmo CPF do trabalhador informado no evento objeto da exclusão, da seguinte forma:  Se evento de referência for o S-1200 – conteúdo do campo cpfTrab do registro ideTrabalhador;  Se evento de referência for o S-1210 – conteúdo do campo cpfBenef do registro ideBenef; |
| --- | --- |
| nisTrab | Este campo será gerado apenas quando o evento objeto da exclusão for o S-1200.Caso contrário (se for o S-1210), este campo não será gerado (conforme regra que consta no manual do eSocial vrs 2.4.01).   A informação a ser gravada é a mesma do evento original, ou seja, o conteúdo do campo nisTrab do registro ideTrabalhador. |


| IndApuracao | Neste campo será gravada a informação do campo indApuracao (registro ideEvento ) do evento objeto da exclusão. |
| --- | --- |
| perApur | Neste campo será gravada a informação do campo perApur (registro ideEvento) do evento objeto da exclusão. |


| Não existem informações no histórico do evento                     <OK> |
| --- |


| Campo | Coluna da tabela de log |
| --- | --- |
| Data/Hora do Evento | DAT_CRIACAO |
| Protocolo Onesource | PROTOCOLO_ONESOURCE |
| Status | STATUS_PROC |
| Código da Mensagem | COD_MENSAGEM_ONESOURCE |
| Descrição da Mensagem | DES_MENSAGEM_ONESOURCE |
| Recibo | RECIBO_ONESOURCE |
| Hashcode | HASH_ONESOURCE |
