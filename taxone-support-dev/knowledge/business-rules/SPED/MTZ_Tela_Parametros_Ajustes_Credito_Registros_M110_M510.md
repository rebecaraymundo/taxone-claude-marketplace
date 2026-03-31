# MTZ_Tela_Parametros_Ajustes_Credito_Registros_M110_M510

> Fonte: MTZ_Tela_Parametros_Ajustes_Credito_Registros_M110_M510.docx





THOMSON REUTERS

Parâmetro de Ajustes de Crédito dos
Registros M110 e M510

(Somente para TAX ONE)



DOCUMENTO DE REQUISITO



Sumário


SUGESTão do LAYOUT	3	12
REGRAS DOS CAMPOS	12

## Sugestão do Layout




## Regras dos Campos


Localização da tela: Módulo: SPED » EFD – Escrituração Fiscal Digital das Contribuições
Menu: Parâmetros » Parâmetro de Ajustes de Crédito dos Registros M110/M510

Título da tela: Parâmetro de Ajustes de Crédito dos Registros M110/M510

Esse item estará disponível exclusivamente para o Tax One.

O objetivo desse parâmetro será um facilitador para os CST’s 49 e 98 para as situações de alíquotas de PIS e COFINS podendo inserir manualmente, e poderá selecionar o Tipo de Crédito e o Código de Ajuste de Contribuição correspondentes, dessa forma o usuário passará a definir a melhor condição.






| OS/CH/MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-97881 | Elisabete Costa | TAX ONE - Criação do Parâmetro de Ajustes de Crédito dos Registros M110/M510 para CST 49 e 98 |


| RN | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RN01 | Estabelecimento | Editbox | S | S | Default:  Estab. informado na tela | Informar o Estabelecimento que corresponde a parametrização (aparecerá automaticamente quando informado no login).  Tratamento: Campo desabilitado quando informado estabelecimento na tela inicial; Se o estabelecimento não for informado na tela inicial, será demonstrado o combo box em branco;  Se não for selecionado um estabelecimento, ao salvar o registro emitir a mensagem na tela: “Selecionar o Estabelecimento”.  Quando o usuário entrar no modulo com o estabelecimento definido trazer para o campo o estabelecimento que o usuário acesso o módulo. Agora se o usuário acessar o modulo sem definir o estabelecimento trazer a lista de todos os estabelecimentos disponíveis para determinada empresa. | MFS-97881 |
| RN02 | Alíquota PIS | Numérico | S | S | Formato:  Text Input 0,0000 Tamanho: 003V004  Default:  Habilitado | Se preenchido informar a alíquota PIS (em percentual), de acordo com as tabelas externas disponibilizadas pela RFB. | MFS-97881 |
| RN03 | Alíquota COFINS | Numérico | S | S | Formato:  Text Input 0,0000 Tamanho: 003V004  Default:  Habilitado | Se preenchido Informar a alíquota COFINS (em percentual), de acordo com as tabelas externas disponibilizadas pela RFB. | MFS-97881 |
| RN04 | Cód.Tipo Crédito | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Neste campo deverá apresentada uma lista:  Ao confirmar, se nenhum tipo de crédito estiver preenchido, exibir a mensagem: “Informar Tipo de Crédito”  Conteúdo: 101 - Crédito vinculado a receita tributada no mercado interno - Alíquota Básica                                          102 - Crédito vinculado a receita tributada no mercado interno - Alíquotas Diferenciadas                                  108 - Crédito vinculado a receita tributada no mercado interno - Importação | MFS-97881 |
| RN05 | Cód. Ajustes de Contribuição | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo deve possuir as opções abaixo.    Ao confirmar, se nenhum tipo de crédito estiver preenchido, exibir a mensagem: “Informar Código de Ajustes de Contribuição”  Conteúdo: 05 - Ajuste Oriundo de Outras Situações 06 - Estorno | MFS-97881 |
| RN06 | Replicar para os Estabelecimentos | Check-box | N | S | Default:  Não selecionado | Serão apresentados no componente, todos os estabelecimentos da empresa que está logada. E só ficarão habilitados para serem marcados se a opção “Replicar para os Estabelecimentos” estiver selecionada. Neste caso, poderá ser selecionado um ou mais estabelecimentos.  Se a opção “Replicar para os Estabelecimentos” estiver selecionada, os botões “Selecionar Todos” e “Desmarcar Todos” devem ficar habilitados.   Ao selecionar o botão “Selecionar Todos”, todos os estabelecimentos do componente ‘Replicar para os Estabelecimentos serão selecionados.’  Ao selecionar o botão “Desmarcar Todos”, todos os estabelecimentos do componente ‘Replicar para os Estabelecimentos serão desmarcados.’  Se a opção “Replicar para os Estabelecimentos” estiver marcada e clicar em confirma, pelo menos um estabelecimento deve estar marcado para replicar a parametrização, caso contrário, exibir a mensagem: ‘Selecionar pelo menos um estabelecimento para a Replicação.’  Se a opção “Replicar para os Estabelecimentos” estiver marcada e existir um ou mais estabelecimentos selecionados, ao clicar no botão confirma, a parametrização criada, será replicada a todos os estabelecimentos que foram selecionados no componente. | MFS-97881 |
