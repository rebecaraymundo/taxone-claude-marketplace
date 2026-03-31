# MTZ_REINF_Tela_Param_Ajustes_CPRB_Servicos

> Fonte: MTZ_REINF_Tela_Param_Ajustes_CPRB_Servicos.docx






THOMSON REUTERS

Módulo EFD-REINF
Tela de Parâmetros dos Ajustes da CPRB – Serviços




DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3
2.	Layout de Tela	7

## Regras dos Campos


Localização da tela: Menu SPED, Módulo: EFD-REINF, item de menu Parâmetros > CPRB > Parâmetros dos Ajustes da CPRB > Serviços

Título da tela: Parâmetros dos Ajustes da CPRB - Serviços

Opções da barra de menu:

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado.

FECHA – Fecha a janela da parametrização.

















## Layout de Tela




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS15093 | Lara Aline | Criação da Tela de Parâmetros dos Ajustes da CPRB - Serviços |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Dropdown | S | S | Default: não selecionado | Nesse campo serão listados todos os estabelecimentos da empresa logada, que usuário tenha permissão de acesso e que possuam o cadastro nos Dados Iniciais preenchido  Caso não preenchido exibir a seguinte mensagem: O Estabelecimento deve ser informado. | MFS15093 |
| Indicador da Atividade Econômica | Pasta | S | S | Default = Não selecionado | Deverá apresentar somente os códigos de atividade da TACES75 que estiverem com IND_ATIVIDADE igual a: 1 e 4. Caso não preenchido exibir a seguinte mensagem "Informar o Indicador de Atividade Econômica" | MFS15093 |
| Código da Receita | Dropdown | S | S | Default = Não selecionado | Este campo será recuperado da dwt_cod_receita filtrando o tributo CPRB. Caso não preenchido exibir a seguinte mensagem "Informar o Código da Receita" | MFS15093 |
| Tipo de Ajuste | Dropdown | S | S | Default = Não selecionado | Listar os valores:  Ajuste de redução; Ajuste de acréscimo.  Caso não preenchido exibir a seguinte mensagem: “O campo Tipo de Ajuste deve ser informado” De início para essa MFS15093 esse campo ficará default a opção 0 - Ajuste de redução sem possibilidade de alteração. | MFS15093 |
| Código de Ajuste |  |  |  |  | Listar os valores:  6 - Vendas canceladas e os descontos incondicionais concedidos.   Quando selecionada a opção 0 – Ajuste de Redução no campo Código de Ajuste serão apresentadas apenas as opções de código de ajuste igual a 6.  Caso não preenchido exibir a seguinte mensagem: “O campo Código de Ajuste deve ser informado” | MFS15093 |
| Informar Código/Descrição para Pesquisa | ComboBox | N | S | Default: não selecionado | Este campo é destinado para pesquisa do Serviço via código ou descrição.  Campos Código e Descrição são Checkbox. | MFS15093 |
| Código de Serviço: * | Código de Serviço: * | Código de Serviço: * | Código de Serviço: * | Código de Serviço: * | Código de Serviço: * | Código de Serviço: * |
| Código de Serviço* | Caixa de seleção de CFOP´s. | S | S | Default: não selecionado | Exibir a lista de Código de Serviços da SAFX2018  Nesse campo será exibido apenas os códigos de serviços que não possuam cadastro para outro Código de Ajuste.  Obs: O código de serviço só pode ser associado a um código de atividade. | MFS15093 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Quando acionado, muda o status dos Código de Serviços que não estão selecionados para selecionado. | MFS15093 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Quando acionado, muda o status dos Código de Serviços que estão selecionados para não selecionado. | MFS15093 |
| Réplica para estabelecimentos* | Réplica para estabelecimentos* | Réplica para estabelecimentos* | Réplica para estabelecimentos* | Réplica para estabelecimentos* | Réplica para estabelecimentos* | Réplica para estabelecimentos* |
| Replicar para os Estabelecimentos | Checkbox | N | S | Default: não selecionado |  | MFS15093 |
| Estabelecimentos* | Caixa de seleção de estabs. | N | S | Default: não selecionado | Exibir a lista de estabelecimentos da empresa que acessou o módulo, para que seja possível replicar a parametrização.  Será possível selecionar o estabelecimento somente quando a opção “Replicar para os Estabelecimentos” estiver selecionada. | MFS15093 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Deve ser habilitado apenas quando a opção “Replicar para os Estabelecimentos” estiver selecionada.  Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado. | MFS15093 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Deve ser habilitado apenas quando a opção “Replicar para os Estabelecimentos” estiver selecionada.  Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado. | MFS15093 |
