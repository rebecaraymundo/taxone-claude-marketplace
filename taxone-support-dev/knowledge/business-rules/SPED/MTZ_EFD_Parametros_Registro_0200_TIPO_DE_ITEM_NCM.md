# MTZ_EFD_Parametros_Registro_0200_TIPO_DE_ITEM_NCM

> Fonte: MTZ_EFD_Parametros_Registro_0200_TIPO_DE_ITEM_NCM.docx






THOMSON REUTERS

Tipo de Item x NCM
MTZ_TIPO_DE_ITEM_NCM



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

Título da tela: Tipo de Item x NCM

Funcionamento da tela: Esta tela foi criada com a finalidade de parametrizar “NCM” por “Tipo do Item”, ou seja, será possível vincular um NCM para vários tipos de item respeitando o início de validade.

[MFS-5400]
Obs: As parâmetros de seleção definidos nesta tela serão replicados para a mesma tela no módulo Escrituração Fiscal Digital das Contribuições.





Sugestão de leiaute:



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS_2552 | EFD Fiscal Tipo de Item x NCM | Criação de tela Tipo de Item x NCM |
| MFS-5400 | EFD Fiscal Tipo de Item x NCM | Replicar parametrização para EFD- Contribuições |


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
| Estabelecimento | Editbox | S | N |  | Quando o usuário entrar no modulo com o estabelecimento definido trazer para o campo o estabelecimento que o usuário acesso o modulo. Agora se o usuário acessar o modulo sem definir o estabelecimento trazer a lista de todos os estabelecimentos disponíveis para determinada empresa. | MFS_2552 |
| NCM (Capitulo/Posição) | Pasta de seleção | S | N |  | Este campo deve possibilitar o usuário buscar os 4 primeiros dígitos do NCM na SAFX2043 ou digitar o código manualmente na tela, carregando a descrição.  Caso não preenchido deverá ser exibida a seguinte mensagem: “O campo NCM deve ser informado”. | MFS_2552 |
| Tipo de Item | Dropdown | S | S |  | Deve permitir o usuário escolher entre as seguintes opões: Mercadoria para Revenda Matéria Prima Embalagem Produto em Processo Produto Acabado Subproduto Produto Indeterminado Material de Uso e Consumo Ativo Imobilizado Serviços Outros Insumos 99- Outras  Caso não preenchido deverá ser exibida a seguinte mensagem: “O campo Tipo de Item deve ser informado”. | MFS_2552 |
| Início da Validade | Data | S | S | DD/MM/AAAA | Permitir o usuário preencher a partir de qual data a parametrização estará em execução.  Obs: Caso informada mesma data para um mesmo NCM exibir a seguinte mensagem: “Existem NCM´s repetidos para mesma data de validade. Cada NCM só pode ser parametrizado uma única vez para cada data. Favor verificar”. | MFS_2552 |
| Replicar para os estabelecimentos | Checbox | N | S |  | Quando selecionado irá habilitar para seleção os estabelecimentos listados e deverá replicar a parametrização para os estabelecimentos que forem selecionados. | MFS_2552 |
| Selecionar Todos | Botão | N | S |  | Quando acionado irá selecionar todos os estabelecimentos.  Obs: Será habilitado quando selecionado o checkbox “Replicar para os estabelecimentos”. | MFS-2552 |
| Desmarcar Todos | Botão | N | S |  | Quando acionado irá desmarcar todos os estabelecimentos selecionados  Obs: Será habilitado quando selecionado o checkbox “Replicar para os estabelecimentos”. | MFS-2552 |
