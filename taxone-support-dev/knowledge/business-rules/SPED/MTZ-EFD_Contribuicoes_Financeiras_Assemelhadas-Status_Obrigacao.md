# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Status_Obrigacao

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Status_Obrigacao.docx






THOMSON REUTERS

Matriz da tela Status da Obrigação



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD- Contribuições Financeira/Assemelhada
Menu: Obrigações

Título da tela: Status da Obrigação

Funcionamento da tela: Esta tela altera o status de um arquivo gerado com informações da EFD-Contribuições Financeira/Assemelhada. Anteriormente no momento do acesso a tela, era necessário selecionar a apuração. Com a funcionalidade de multiempresa deve-se informar empresa e definir “Período” e “Situação” e pesquisar as informações selecionadas. Deverá ser mostrada a listagem dos arquivos já gerados através da tela de “Geração dos Registros” (Obrigações >> Geração dos Registros), onde o usuário deverá indicar para qual arquivo deseja alterar o Status.




* Descrição não disponível em tela




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4498 | Elenilson Coutinho | Definição das regras para a tela de Status da Obrigação. |
| OS4707 | Elenilson Coutinho | Alteração da lista de seleção do campo “Situação” inclusão da opção “Todas” para listas todas as apurações . |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Dropdown | S | S |  | Por se tratar de Multiempresa, listar todas a empresas e exibir a descrição “Todas”.  Campo obrigatório, caso não preenchido retornar a mensagem “Campo Empresa não preenchido”. | OS4498 |
| Período | Editbox | S | S | Formato: DD/MM/AAAA a DD/MM/AAAA | Campo obrigatório, caso não preenchido retornar a mensagem “Campo Período não preenchido”.  Range de data não poderá ser maior que 1 Mês. | OS4498 |
| Situação | Dropdown | S | S |  | Campo obrigatório, caso não preenchido retornar a mensagem “Campo Situação não preenchido”.  Caso apuração “Reaberta” exibir a mensagem: "A apuração será reaberta, nesse caso a geração dos dados e as manutenções dos dados da apuração do período terão que ser reprocessadas. Caso deseja recuperar os registros de manutenções, será necessário executar o processo de “Restauração dos Lançamentos Manuais”, disponíveis no Menu Obrigações, após a Geração dos Registros. Se houver períodos posteriores, com status da Apuração Fechada, esses períodos também serão reabertos e terão que ser reprocessados. Deseja Reabrir a apuração? | OS4498 |
| Pesquisar | Botão | N | N |  | Irá fazer a busca das informações parametrizada pelo usuário nos campos acima.  Caso não houver registros, exibir mensagem: “Não existem registros para as parametrizações definidas” | OS4498 |
| * Selecionador | Checkbox | N | S | Default: Não selecionado | Será selecionado caso o campo “Marcar Todos” for flegado pelo usuário.  Deverá ser marcado pelo menos “1(Um)” registro caso contrário retornar a mensagem  “Pelo menos um registro dever ser selecionado”. | OS4498 |
| Empresa | Editbox | S | N |  |  | OS4498 |
| Estabelecimento | Editbox | S | N |  |  | OS4498 |
| Situação | Dropdown | S | S |  | Campo irá exibir “Apuração Realizada”, “Apuração Reaberta” e “Apuração fechada”. | OS4498 |
| Data Inicial | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data inicial de geração dos registros. | OS4498 |
| Data Final | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data final de geração dos registros. | OS4498 |
| Obrigação Fiscal | Editbox | S | N |  |  | OS4498 |
| Observação | Editbox | N | S |  |  | OS4498 |
| Marcar Todos | Checkbox | S | S | Default: Não Selecionado |  | OS4498 |
| Reabrir todos | Botão | N | N |  | Por se tratar de Multiempresa, irá reabrir todas as apurações listadas como “Fechadas”, parametrizada pelo usuário. | OS4498 |
| Fechar todos | Botão | N | N |  | Por se tratar de Multiempresa, irá fechar todas as apurações listadas como “Realizadas”, parametrizada pelo usuário. | OS4498 |
