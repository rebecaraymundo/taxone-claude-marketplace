# MTZ_EFD PIS-COFINS_Identificador_Cod_Receita_por_Regime_de_Incidencia

> Fonte: MTZ_EFD PIS-COFINS_Identificador_Cod_Receita_por_Regime_de_Incidencia.docx






THOMSON REUTERS

Identificador do Cód. Receita por Regime de Incidência
EFD - Escrituração Fiscal Digital das Contribuições



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


Localização da tela: Módulo: SPED  Escrituração Fiscal Digital das Contribuições
Menu: Parâmetros  Apuração  Identificador do Cód. Receita por Regime de Incidência

Título da tela: Identificador do Cód. Receita por Regime de Incidência.

Funcionamento da tela: Esta tela foi criada para que o usuário possa vincular os códigos de Receita ao Regime de Incidência Cumulativo ou Não Cumulativo.

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:







| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4584 | Elenilson Coutinho | Criação da tela de Identificador do Cód. Receita por Tipo de Incidência. |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Editbox | S | N | Formato: <COD ESTAB> - <RAZÃO SOCIAL> | Deverá exibir o estabelecimento selecionado no momento do acesso à tela e poderá ser alterado caso o usuário acione o botão de seleção de grupo da barra de ferramentas, para as situações onde no acesso ao módulo não foi parametrizado um estabelecimento no manager. | OS4584 |
| Tributo | Radio Button | S | S | Default Selecionado: PIS/PASEP | Irá exibir os tributos para vinculo com o Regime e Código de Receita correspondente. As opções são:   “PIS/PASEP” e “COFINS” | OS4584 |
| Regime de Incidência | Radio Button | S | S | Default Selecionado: Cumulativo | Irá exibir o Regime de Incidência. As opções são:  “Cumulativa“ e “Não-Cumulativa” | OS4584 |
| Códigos Receita | ChecBox | S | S |  | Deverá exibir os códigos de Receita da DWT_COD_RECEITA.  Se um Código Receita já foi associado a um Regime de Incidência em uma parametrização anterior, este não deve ser exibido para parametrização de um Regime de Incidência distinto.  Obs: Caso selecionado o tributo PIS/PASEP deverá listar os códigos de receita correspondente ao COD_TRIBUTO = 06.   Se selecionado o tributo COFINS deverá listar os códigos de receita correspondente ao COD_TRIBUTO = 07. | OS4584 |
| Selecionar Todos | Botão | N | S |  | Quando acionado, muda o status dos códigos Receita que não estão selecionados para selecionado. | OS4584 |
| Desmarcar Todos | Botão | N | S |  | Quando acionado, muda o status dos códigos Receita que estão selecionados para não selecionado. | OS4584 |
| Replicar para os Estabelecimentos | Checkbox | N | S | Default: não selecionado | Irá replicar a parametrização realizada para os estabelecimentos assim selecionados. | OS4584 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Deve ser habilitado apenas quando a opção “Replicar para os Estabelecimentos” estiver selecionada.  Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado. | OS4584 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Deve ser habilitado apenas quando a opção “Replicar para os Estabelecimentos” estiver selecionada.  Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado. | OS4584 |
