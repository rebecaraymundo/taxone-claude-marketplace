# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Parametrizacao_Folha_de_Salarios-M350

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Parametrizacao_Folha_de_Salarios-M350.docx






THOMSON REUTERS

Parametrização Folha de Salários (M350)
Automatização do registro M350



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


Localização da tela: Módulo: Sped EFD – Contribuições Financeiras Assemelhadas
Menu: Parâmetros Parametrização Folha de Salários (M350)

Título da tela: Parametrização Folha de Salários (M350)

Funcionamento da tela: Está tela foi criada para que usuário possa parametrizar as contas que irão receber os respectivos valores de Folha e Exclusão. Como seleção chave teremos os campos “Estabelecimento e o indicador (Valor da Folha de Salários ou Valor das Exclusões à Base de Cálculo)”

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:









Layout da tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4322 | Elenilson Coutinho | Tela para parametrização e geração automática do registro M350 |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | [Quem executará o evento. Ex.: Usuário do sistema]. |
| Pré- Condições | [Condições necessárias para execução. Ex.: Estabelecimento cadastrado] |
| Pós-Condições | [Resultado após executar caso de uso. Ex.: Informação armazenada no banco de dados] |


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
| Estabelecimento | Drop Down | S | S | Descentralizador/Centralizados – Cód. Estab – Desc. | Deverá exibir o estabelecimento selecionado no momento do acesso à tela e poderá ser alterado caso o usuário acione o botão de seleção de grupo da barra de ferramentas, para as situações onde no acesso ao módulo não foi parametrizado um estabelecimento no manager. | OS4322 |
| Valor da Folha de Salários | Radio Button | S | S | Default: Selecionado | Quando selecionado usuário define que as contas parametrizadas no campo “Conta Contábil” irão receber os valores referente a folha de salários. | OS4322 |
| Valor das Exclusões à Base de Cálculo | Radio Button | S | S |  | Quando selecionado usuário define que as contas parametrizadas no campo “Conta Contábil” irão receber o valor referente a Exclusões Base de Cálculo. | OS4322 |
| Alíquota PIS | TextBox | S | S |  | Usuário deverá informar a alíquota PIS/PASEP para cálculo da contribuição sobre a folha de salário.  Campo obrigatório, caso não preenchido retornar a mensagem “Alíquota PIS não informada”. | OS4322 |
| Informar Conta/Descrição para pesquisa | TextBox | N | S |  | Usuário irá fazer uma busca no campo por descrição, caso o campo “Descrição” esteja selecionado. Se o campo “Conta” for selecionado a busca deverá ser por código da conta. | OS4322 |
| Conta | Radio Button | N | S | Default: Selecionado | Quando selecionado usuário indica que a busca no campo “Informar Conta/Descrição para pesquisa” será por Código da conta. | OS4322 |
| Descrição | Radio Button | N | S |  | Quando selecionado usuário indica que a busca no campo “Informar Conta/Descrição para pesquisa” será por Descrição da conta. | OS4322 |
| Pesquisar | Button | N | N |  | Irá pesquisar as contas analíticas se por código ou descrição assim parametrizado pelo usuário. | OS4322 |
| Conta Contábil | CheckBox | S | S |  | Irá listar todas as contas analíticas (Tabela X2002 campo IND_CONTA = ‘A’).  Ao menos uma conta deverá ser preenchida para um respectivo indicador de valor, caso contrário retornar a mensagem: “Informar conta contábil”.  Obs: Quando selecionada uma conta para associá-la ao indicador “Valor da Folha de Salários”, esta, NÃO deverá aparecer em lista para o indicador “Exclusões à Base de Cálculo” e vice-versa.” | OS4322 |
| Selecionar Todos | Button | N | N |  | Quando acionado irá selecionar todas as contas listadas em pesquisa. | OS4322 |
| Desmarcar todos | Button | N | N |  | Quando acionado irá Desmarcar todas as contas listadas em pesquisa. | OS4322 |
| Mostrar Parametrizadas | Button | N | N |  | Quando acionado irá listar somente as contas parametrizadas pelo usuário. | OS4322 |
| Replicar para os estabelecimentos | CheckBox | N | S |  | Quando selecionado irá replicar toda parametrização realizadas pelo usuário para os estabelecimentos selecionados. | OS4322 |
| Selecionar Todos | Button | N | N | Default: Desabilitado | Quando selecionado irá selecionar todos os estabelecimentos listados.   Botão será habilitado quando o campo “Replicar para os estabelecimentos” estiver selecionado. | OS4322 |
| Desmarcar Todos | Button | N | N | Default: Desabilitado | Quando selecionado irá Desmarcar todos os estabelecimentos selecionados.   Botão será habilitado quando o campo “Replicar para os estabelecimentos” estiver selecionado. | OS4322 |
