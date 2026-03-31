# MTZ-eSocial-Geracao-dos-Arquivos-XML

> Fonte: MTZ-eSocial-Geracao-dos-Arquivos-XML.docx






THOMSON REUTERS

Módulo eSocial

Geração dos Arquivos XML


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Arquivos XML


DOCUMENTO DE REQUISITO








Sumário

1.	Parâmetros da Tela	2
2.	RN01 – Eventos Gerados no Período	8
3.	RN02 - Geração dos Arquivos XML	11
4.	RN03 - Download dos Arquivos XML	11
















## Parâmetros da Tela



Esta rotina tem apenas duas ações:


- Geração dos Arquivos XML;

- Download dos Arquivos XML gerados;


A geração dos arquivos XML é feita com base nos dados gerados previamente, nos menus “Geração dos Cadastros” e “Geração dos Movimentos”.

Após a geração, o usuário poderá baixá-los através da opção “Download”.


Obs: Esta funcionalidade foi criada nos moldes do “Painel de Controle de Eventos” do módulo REINF. Mas a princípio, não haverá o envio dos arquivos, e nem os controles de status dos retornos. A previsão é que tudo isso seja desenvolvido posteriormente.


Layout:







## RN01 – Eventos Gerados no Período


Ao clicar no botão <Consultar>, todos os eventos que atendam aos parâmetros informados pelo usuário serão exibidos no quadro “Eventos gerados no período”.


Critérios para a recuperação dos eventos de CADASTRO a serem exibidos:

Os eventos de cadastro serão recuperados a partir das tabelas utilizadas na geração dos dados, considerando para filtro os seguintes critérios:

- Empresa = empresa do login;
- Estabelecimento = apenas os estabelecimentos centralizadores selecionados pelo usuário;
- Evento = apenas os eventos de cadastro (S-1005, S-1010, S-1020 e S-1070) selecionados pelo usuário;
- Validade Inicial do cadastro = deve ser uma data que se enquadre no período informado pelo usuário.
- Versão = a versão da geração dos cadastros deve ser a versão informada no campo “Versão”;



Critérios para a recuperação dos eventos de MOVIMENTO a serem exibidos:

Os eventos de movimento serão recuperados a partir das tabelas utilizadas na geração dos dados, considerando para filtro os seguintes critérios:

- Empresa = empresa do login;
- Estabelecimento = apenas os estabelecimentos centralizadores selecionados pelo usuário;
- Evento = apenas os eventos de movimento (S-1200, S-1210 e S-1300) selecionados pelo usuário;
- Mês/Ano de referência do movimento (***) = mês/ano do período informado pelo usuário.
- Versão = a versão da geração dos movimentos deve ser a versão informada no campo “Versão”;




Dados dos eventos a serem demonstrados:





## RN02 - Geração dos Arquivos XML



Ao clicar no botão <Gerar XML>, serão gerados os arquivos XML conforme o layout do eSocial.

Estes arquivos serão armazenados numa tabela (staging area – OUT), que posteriormente será utilizada para leitura e download dos arquivos (e ainda, para leitura e envio ao Fisco, funcionalidade não disponível, que ainda será desenvolvida no futuro).

- Serão considerados para a geração do XML, apenas os eventos selecionados pelo usuário no quadro “Eventos gerados no período”;

- Para cada evento será gerado um arquivo XML;

Ao finalizar a geração, exibir mensagem de geração efetuada com sucesso.


- Ao finalizar a geração dos XML, o quadro “Eventos gerados no período” será atualizado nas colunas “XML já gerado” e “Data”. O objetivo é exibir a informação correta em relação aos eventos que acabaram de ser gerados. Assim, o usuário poderá visualizar a informação já atualizada.


## RN03 - Download dos Arquivos XML



Ao clicar no botão <Download do XML>, será aberta uma janela para seleção do diretório (local/rede) onde serão gravados os arquivos.

Serão considerados para download apenas os seguintes eventos:

- Eventos selecionados pelo usuário no quadro “Eventos gerados no período”;

- Eventos que já tenham XML gerado;

Os arquivos serão gravados no diretório de destino informado pelo usuário, e serão nomeados da seguinte forma:

“ID_CODEVENTO_ENV.XML”

Sendo:

ID: identificador do evento (conteúdo do campo “id”)
CODEVENTO: código do evento (S-1005, S-1010, S-1020, S-1070, S-1200, S-1210, S-1300)

(o REINF segue esta mesma nomenclatura para os arquivos gerados na opção download)
(conforme documento “MTZ_REINF_Tela_Painel_Controle_Eventos”, campo “AÇÕES”, opção “Download do XML”)


Ao finalizar a gravação dos arquivos, exibir mensagem de download efetuado com sucesso.


= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15868 | Geração dos Arquivos XML | Criação do item de menu para a geração dos arquivos XML | 16/01/2018  (criação do documento) |
| MFS17022 | Alteração na tela da geração | Incluído o campo “Referência” para demonstrar uma informação que identifique o evento exibido em tela. | 05/03/2018 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano dos eventos a serem exibidos para seleção.  Deve ser um mês válido. |  |
| Versão | Alfanumérico | S | N | Listbox | Este campo é uma lista, que a princípio terá apenas uma opção: [2.4.01] |  |
| Eventos | Alfanumérico | S | N |  | Neste quadro são exibidos os eventos para seleção do usuário:  S-1005 - Estabelecimentos S-1010 - Rubricas S-1020 - Lotações  S-1070 - Processos Administrativos / Judiciais S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social S-1210 - Pagamentos de Rendimentos do Trabalho S-1300 – Contribuições Sindicais |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os eventos demonstrados no quadro “Eventos”. |  |
| Estabelecimentos Centralizadores | Alfanumérico | S | N |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos da Empresa cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (lembrando que esta parametrização só trabalha com os estabelecimentos centralizadores das obrigações federais) |  |
| Selecionar | Alfanumérico | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimentos Centralizadores”:  - Somente Estabelecimentos da empresa do login; - Somente Estabelecimentos parametrizados nos Dados Iniciais;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos Centralizadores” já marcados. |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos Centralizadores”. |  |
| Consultar | Alfanumérico | N | N |  | Ao clicar neste botão, os eventos que atendam aos parâmetros informados serão exibidos no quadro “Eventos gerados no período” (ver regras do funcionamento deste quadro na RN01). |  |
| Limpar | Alfanumérico | N | N |  | Ao clicar neste botão, todos os parâmetros informados para consulta serão limpos. |  |
| Eventos gerados no período | Alfanumérico | N | N |  | Neste quadro são exibidos todos os eventos que atendam aos parâmetros informados, e o usuário poderá selecionar os eventos desejados para geração/download dos arquivos XML.  Ver regras do funcionamento deste quadro na RN01 abaixo. |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os eventos demonstrados no quadro “Eventos gerados no período”. |  |
| Gerar XML | Alfanumérico | N | N |  | Esta opção será habilitada apenas quando houverem eventos selecionados no quadro “Eventos gerados no período”.  Ao clicar neste botão, serão gerados os arquivos XML referentes à todos os eventos selecionados no quadro “Eventos gerados no período”.  Ver regras da geração dos arquivos XML na RN02 abaixo. |  |
| Download do XML | Alfanumérico | N | N |  | Esta opção será habilitada apenas quando houverem eventos selecionados no quadro “Eventos gerados no período” e pelo menos um destes eventos já tenha XML gerado.   Ao clicar neste botão, será aberta uma janela para o usuário selecionar um diretório onde serão gravados os arquivos XML a serem baixados.  Ver regras do download dos arquivos XML na RN03 abaixo. |  |


| Exemplo, supondo os seguintes cadastros:  Cad01 – validade inicial = 01/01/2017 Cad02 – validade inicial = 01/05/2017 Cad03 – validade inicial = 20/05/2017 Cad04 – validade inicial = 10/06/2017  Na Geração dos Dados para o período de 05/2018 à 06/2018, seriam gerados os cadastros:  - Cad02 – validade inicial = 01/05/2017 - Cad03 – validade inicial = 20/05/2017 - Cad04 – validade inicial = 10/06/2017  Na Geração dos Dados para o período de 06/2018 à 06/2018, seriam gerados os cadastros:  - Cad04 – validade inicial = 10/06/2017  Na Geração do XML para o período = 05/2018, seriam gerados os cadastros:  - Cad02 – validade inicial = 01/05/2017 - Cad03 – validade inicial = 20/05/2017  Na Geração do XML para o período = 06/2018, seriam gerados os cadastros:   - Cad04 – validade inicial = 10/06/2017 |
| --- |


| (***) Este mês/ano de referência do movimento varia de acordo com o movimento, e é exatamente o período usado para filtro na rotina da “Geração dos Movimentos”:  - Para o evento S-1200, é o mês/ano de competência do Demonstrativo de Pagamento; - Para o evento S-1210, é o mês/ano do pagamento; - Para o evento S-1300, é o mês/ano da contribuição sindical; |
| --- |


| Estabelecimento | Código e razão social do estabelecimento centralizador para o qual foi gerado o evento. |
| --- | --- |
| Evento | Sigla do evento: S-1005, S-1010, S-1020, S-1070, S-1200, S-1210 ou S-1300. |
| Referência   (campo criado na MFS17022) | O objetivo desta coluna é mostrar ao usuário alguma informação que identifique o evento em questão.  A informação a ser exibida depende do tipo de evento, da seguinte forma:  S-1005 – Campo nrInsc do registro ideEstab, no formato:                             N. Inscrição Estabelecimento: XXXXXXXXXXXXXXX  S-1010 – Campos ideTabRubr e codRubr do registro ideRubrica (tabela e código da Rubrica), no formato:               Tabela/Cód Rubrica: XXXXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    S-1020 – Campos codLotacao do registro ideLotacao (código do setor), no formato:                                      Lotação: XXXXXXXXXXXXXXXXXXXXXXX   S-1070 – Campos tpProc e nrProc do registro ideProcesso (tipo e número do processo), no formato:                          Tipo/Número do Processo: X - XXXXXXXXXXXXXXXXXXXX   S-1200 – Campo cpfTrab do registro ideTrabalhador, no formato:                                  CPF Trabalhador: XXX.XXX.XXX-XX   S-1210 – Campo cpfBenef do registro ideBenef, no formato:                                  CPF Beneficiário: XXX.XXX.XXX-XX   S-1300 – Campo nrInsc do registro ideEmpregador, no formato:                             N. Inscrição Empregador: XXXXXXXXXXXXXXX |
| XML já gerado | O conteúdo dessa coluna depende da data que será (ou não) exibida no próximo campo:  Se coluna “Data” = brancos  exibir “N” Se coluna “Data” <> brancos  exibir “S” |
| Data | Nesta coluna será exibida a data em que foi gerado o último XML para o evento em questão, quando for o caso.  O objetivo desta coluna é mostrar ao usuário se o evento já tem ou não um XML gerado anteriormente. É apenas informativo, e não impede que o usuário solicite uma nova geração.  Quando o evento ainda não tiver sido gerado em XML, esta coluna aparecerá em branco. |
| Identificação do evento | Código de identificação única do evento, conforme regras do layout do eSocial.  Trata-se da informação gerada para o campo “id”, presente em todos os eventos. |
