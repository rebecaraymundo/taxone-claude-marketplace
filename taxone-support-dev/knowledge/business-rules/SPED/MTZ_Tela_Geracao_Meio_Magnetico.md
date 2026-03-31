# MTZ_Tela_Geracao_Meio_Magnetico

> Fonte: MTZ_Tela_Geracao_Meio_Magnetico.docx






THOMSON REUTERS

Matriz da Tela Geração do Meio Magnético



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	3
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso





### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]


#### Fluxo Principal




#### Fluxo Alternativo 1 – Localizar registros (Exemplo)





## Regras dos Campos


Localização da tela:
Módulo: SPED  EFD- Contribuições Financeira/Assemelhada
Menu:    Obrigações

Título da tela: Geração do Meio Magnético

Funcionamento da Tela: Está tela realiza a geração do arquivo magnético da EFD-Contribuições Financeira/Assemelhada. Anteriormente no momento do acesso a tela, era necessário selecionar a apuração. Com a funcionalidade de multiempresa deve-se informar empresa e definir “Período” e “Situação” e pesquisar as informações selecionadas. Deverá ser mostrada a listagem dos arquivos já gerados através da tela de “Geração dos Registros” (Obrigações >> Geração dos Registros), onde o usuário deverá indicar qual empresa e estabelecimento centralizador ou descentralizador deseja gerar o meio magnético.





* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4498 | Elenilson Coutinho | Definição das regras para a tela de Geração do Meio Magnético |


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
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Dropdown | S | S |  | Por se tratar de Multiempresa”, listar todas as empresas e exibir a descrição “Todas”.  Campo obrigatório, caso não preenchido retornar a mensagem “Campo Empresa não preenchido”. | OS4411 |
| Período | Editbox | S | S | Formato: DD/MM/AAAA                a DD/MM/AAAA | Campo obrigatório, caso não preenchido retornar a mensagem “Campo Período não preenchido”.  Range de data não poderá ser maior que 1 Mês. | OS4411 |
| Situação | Dropdown | S | S |  | Por se tratar de Multiempresa”,  listar “Apuração Realizada”, “Apuração Reaberta”, “Apuração fechada” e exibir a descrição “Todas”  Campo obrigatório, caso não preenchido retornar a mensagem “Campo Situação não preenchido”. | OS4411 |
| Pesquisar | Botão | N | N |  | Irá fazer a busca das informações parametrizada pelo usuário nos campos acima.  Caso não houver registros, exibir mensagem: “Não existem registros para as parametrizações definidas” | OS4411 |
| Gravação do Arquivo Magnético no Servidor | Checkbox | N | S | Defaut: Selecionado |  | OS4411 |
| Atribuir nome padrão para o arquivo | Checkbox | N | S | Defaut: Não selecionado | Se selecionado atribuir um nome padrão ao arquivo no seguinte formato: NUM_EMPRESA + NUM_ESTAB + Data Final  Obs: Mostrar em nomenclatura do arquivo o número dos estabelecimentos “Centralizador” e “Descentralizador”. | OS4411 |
| Definir diretório padrão para arquivos | Checkbox | N | S | Default: Selecionado | Irá definir diretório padrão para gravação dos arquivos, assim definido em parametrização pelo usuário. | OS4411 |
| *Campo indicador do diretório | Editbox | N | S |  | Campo será desabilitado caso o Checkbox “Definir diretório padrão para arquivos” não selecionado. | OS4411 |
| *Selecionador | Checkbox | N | S | Default: Não selecionado | Será selecionado caso o campo “Marcar Todos” for flegado pelo usuário.  Deverá ser marcado pelo menos “1(Um)” registro caso contrário retornar a mensagem  “Pelo menos um registro dever ser selecionado”. | OS4411 |
| Empresa | Editbox | S | N |  |  | OS4411 |
| Estabelecimento | Editbox | S | N |  |  | OS4411 |
| Obrigação Fiscal | Editbox | S | N |  |  | OS4411 |
| Layout | Editbox | S | N |  |  | OS4411 |
| Situação | Editbox | S | N |  |  | OS4411 |
| Data Inicial | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data inicial de geração dos registros. | OS4411 |
| Data Final | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data final de geração dos registros. | OS4411 |
| Nome do arquivo | Editbox | N | S |  | Informação será carregada automaticamente e  deverá ser não editável se flegado o checkbox “Atribuir nome padrão para o arquivo”.  Caso checkbox “Atribuir nome padrão para o arquivo” não selecionado deverá existir tratamento para validar se há nome de arquivo duplicado informado pelo usuário e se não informado, exibir a seguinte mensagem: “É necessário informar o nome do arquivo a ser gerado”. | OS4411 |
| Diretório | Editbox | S | S |  | Campo obrigatório caso o Checkbox “Gravação do Arquivo Magnético no Servidor” e  Definir diretório padrão para arquivos não preenchido, se não informado, exibir mensagem:  “É necessário escolher um diretório para depósito do arquivo gerado”.  Caso o campo “*Selecionador” não marcado, deverá limpar as informações uma vez digitadas pelo usuário e desabilitar o mesmo. | OS4411 |
| Marcar Todos | Checkbox | S | S | Default: Não Selecionado |  | OS4411 |
| Geração | Botão | N | N |  | Por se tratar de Multiempresa, irá gerar o meio magnético por estabelecimento “Centralizador” e “Descentralizador”, conforme registros selecionados pelo usuário. | OS4411 |
