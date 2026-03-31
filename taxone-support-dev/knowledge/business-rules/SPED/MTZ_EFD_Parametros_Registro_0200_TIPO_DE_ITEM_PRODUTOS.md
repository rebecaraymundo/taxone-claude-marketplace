# MTZ_EFD_Parametros_Registro_0200_TIPO_DE_ITEM_PRODUTOS

> Fonte: MTZ_EFD_Parametros_Registro_0200_TIPO_DE_ITEM_PRODUTOS.docx






THOMSON REUTERS

Tipo de Item X Produto
MTZ_TIPO_DE_ITEM_PRODUTOS



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	5

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso





### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]


#### Fluxo Principal


[Descrever a ação principal que será realizada na tela especificada.

Ex.: O usuário deseja realizar o cadastro de uma estrutura padrão.



#### Fluxo Alternativo 1 – Localizar registros (Exemplo)




## Regras dos Campos


Localização da tela:

Modulo: SPED > EFD Escrituração Fiscal Digital
Menu: Parâmetros > Registro 0200 > Tipo de Item

Título da tela: Tipo de Item x Produto

Funcionamento da tela: Esta tela foi criada com a finalidade de parametrizar “Produto” por “Tipo do Item”, ou seja, será possível vincular um produto para vários tipos de item respeitando o início de validade. Essa parametrização foi criada para atender o registro 0200 campo TIPO_ITEM, pois, conforme orientação do manual de preenchimento da EFD, quando um mesmo código de produto possuir mais de um tipo de item, deverá ser informado o tipo de maior relevância para o estabelecimento. Assim, o objetivo desta parametrização é permitir que o usuário informe qual o tipo de item a ser utilizado em cada um dos estabelecimentos. Caso não houver parametrização, será recuperado o tipo do item do cadastro do produto SAFX2013.

[MFS-5400]
Obs: As parâmetros de seleção definidos nesta tela serão replicados para a mesma tela no módulo Escrituração Fiscal Digital das Contribuições.


No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:

A pesquisa de produtos irá considerar o grupo selecionado no momento da entrada na tela.




Sugestão de leiaute:



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS_2552 | EFD Fiscal Tipo de Item Produto | Criação de tela Tipo de Item Produto |
| MFS-5400 | EFD Fiscal Tipo de Item Produto | Replicar parametrização para EFD- Contribuições |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | [Quem executará o evento. Ex.: Usuário do sistema]. |
| Pré- Condições | [Condições necessárias para execução. Ex.: Estabelecimento cadastrado] |
| Pós-Condições | [Resultado após executar caso de uso. Ex.: Informação armazenada no banco de dados] |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| [Descrever a interação do ator com o sistema.  Ex.: O usuário acessa a tela de estrutura padrão]. | [Descrever a ação esperada do sistema Ex.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”.] |
| [Ex.:O usuário preenche os campos da Manutenção de Estrutura do Produto. <<Fluxo Alternativo 1>> | [Ex.:O sistema apresenta os campos preenchidos.] |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário clica no botão “Localizar”. | O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados. |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Editbox | S | N |  | Será preenchido com o código + razão social do estabelecimento que foi selecionado na tela de Estabelecimento/Grupo/Validade no acesso à parametrização. | MFS-2552 |
| Grupo Produto | Editbox | S | N | Desabilitado | O Campo grupo de produto será preenchido na hora que o usuário entrar na tela. O sistema perguntará qual o grupo de produtos será utilizado | MFS-2552 |
| Produto (Grp./Ind./Cód./Desc.) | Pasta de Seleção | S | S |  | Este campo deve possibilitar o usuário buscar o produto na SAFX2013, ou digitar o indicador do produto e código manualmente na tela, carregando a descrição.  Serão listadas as seguintes opções para o “Indicador do Produto”:  1 - Produto Acabado  2 - Insumo 3 - Embalagem 4 - Consumo  5 - Outros  6 - Em Elaboração 7 - Intermediário  8 – Miscelânias  Caso não preenchido deverá ser exibida a seguinte mensagem: “O campo Produto deve ser informado”. | MFS-2552 |
| Tipo de Item | Dropdown | S | S |  | Deve permitir o usuário escolher entre as seguintes opões: Mercadoria para Revenda Matéria Prima Embalagem Produto em Processo Produto Acabado Subproduto Produto Indeterminado Material de Uso e Consumo Ativo Imobilizado Serviços Outros Insumos 99- Outras  Caso não preenchido deverá ser exibida a seguinte mensagem: “O campo Tipo de Item deve ser informado”. | MFS-2552 |
| Início da Validade | Editbox | S | S | DD/MM/AAAA | Permitir o usuário preencher a partir de qual data a parametrização estará em execução.  Obs: Caso informada mesma data para um mesmo produto exibir a seguinte mensagem: “Existem produtos repetidos para mesma data de validade. Cada produto só pode ser parametrizado uma única vez para cada data. Favor verificar”.  Caso não preenchido deverá ser informada a seguinte mensagem: “O campo Inicio de Validade deve ser informado”. | MFS-2552 |
| Replicar para os estabelecimentos | Checbox | N | S | Não Selecionado | Quando selecionado irá habilitar para seleção os estabelecimentos listados e deverá replicar a parametrização para os estabelecimentos que forem selecionados. | MFS-2552 |
| Selecionar Todos | Botão | N | S |  | Quando acionado irá selecionar todos os estabelecimentos.  Obs: Será habilitado quando selecionado o checkbox “Replicar para os estabelecimentos”. | MFS-2552 |
| Desmarcar Todos | Botão | N | S |  | Quando acionado irá desmarcar todos os estabelecimentos selecionados  Obs: Será habilitado quando selecionado o checkbox “Replicar para os estabelecimentos”. | MFS-2552 |
