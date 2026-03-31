# MTZ_Tela_Geracao_Meio_Magnetico_SCP

> Fonte: MTZ_Tela_Geracao_Meio_Magnetico_SCP.docx






THOMSON REUTERS





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
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Obrigações SCP

Título da tela: Geração do Meio Magnético

Está tela realiza a geração do arquivo magnético da EFD-Contribuições para empresas que atuam em sCP. Anteriormente no momento do acesso a            tela, era necessário selecionar a apuração. Com a funcionalidade de multiempresa deve-se informar empresa e definir “Período” e “Situação” e pesquisar as informações selecionadas. Deverá ser mostrada a listagem dos arquivos já gerados através da tela de “Geração dos Registros” (Obrigações SCP >> Geração dos Registros), onde o usuário deverá indicar qual empresa e estabelecimento centralizador ou descentralizador deseja gerar o meio magnético.

Esta tela é uma réplica da tela de Geração do Meio Magnético do menu “Obrigações”, tendo como diferença o campo “Cód. SCP”, uma vez que
deverá ser gerado um arquivo para o Sócio Ostensivo e de “1” a “N” arquivos para as SCPs.

Importante: As informações demonstradas nesta tela devem ser apenas referentes a geração de SCP e não devem demonstrar informações da geração normal. Da mesma forma, através da geração normal não deve ser possível visualizar informações da geração de SCP.


* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-A | Marcos G. de Paula | Definição das regras para a tela de Geração do Meio Magnético para SCP. |
| OS4411 | Elenilson Coutinho | Definição das regras para a tela de Geração do Meio Magnético para SCP. |
|  |  |  |
| CH15677_2014 | Julyana Perrucini | Alteração da lista de seleção do campo “Empresa” incluindo tratamento para demonstrar somente as empresas que o usuário tem permissão de acesso no powerlock. |


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
| Empresa | Dropdown | S | S |  | Por se tratar de Multiempresa”, listar todas as empresas e exibir a descrição “Todas”.  [ALTERADA – CH15677_2014] Tratamento: Listar somente as empresas que o usuário tem permissão de acesso no powerlock em User/Company Maintenance – (usuário).  Campo obrigatório, caso não preenchido retornar a mensagem “Campo Empresa não preenchido”. | OS4411 CH15677_2014 |
| Cód. SCP | Editbox | N | S |  | Deverá listar todos os Cód.SCP cadastrados, mais a opção “Ostensivo”.  Caso campo não preenchido o resultado da pesquisa irá trazer todos. | OS4316-A |
| Período | Editbox | S | S | Formato: DD/MM/AAAA                a DD/MM/AAAA | Campo obrigatório, caso não preenchido retornar a mensagem “Campo Período não preenchido”.  Range de data não poderá ser maior que 1 Mês. | OS4411 |
| Situação | Dropdown | S | S |  | Por se tratar de Multiempresa”,  listar “Apuração Realizada”, “Apuração Reaberta”, “Apuração fechada” e exibir a descrição “Todas”  Campo obrigatório, caso não preenchido retornar a mensagem “Campo Situação não preenchido”. | OS4411 |
| Pesquisar | Botão | N | N |  | Irá fazer a busca das informações parametrizada pelo usuário nos campos acima.  Caso não houver registros, exibir mensagem: “Não existem registros para as parametrizações definidas” | OS4411 |
| Gravação do Arquivo Magnético no Servidor | Checkbox | N | S | Default: selecionado |  | OS4411 |
| Atribuir nome padrão para o arquivo | Checkbox | N | S | Default: Não selecionado | Se selecionado atribuir um nome padrão ao arquivo no seguinte formato: EMPRESA + ESTAB + DATA + COD_SCP  Observações:  Mostrar em nomenclatura do arquivo o número dos estabelecimentos “Centralizador” e “Descentralizador”.  Caso houver o caractere “/” ou “\” no nome padrão do arquivo, deverá existir um tratamento para remoção do mesmo na geração.. | OS4411 |
| Definir diretório padrão para o arquivo | Checkbox | N | S | Default: Selecionado | Irá definir diretório padrão para gravação dos arquivos, assim definido em parametrização pelo usuário. | OS4411 |
| *Campo indicador do diretório | Editbox | N | S |  | Campo será desabilitado caso o Checkbox “Definir diretório padrão para arquivos” não selecionado. |  |
| *Selecionador | Checkbox | N | S | Default: Não selecionado | Será selecionado caso o campo “Marcar Todos” for flegado pelo usuário.  Deverá ser marcado pelo menos “1(Um)” registro caso contrário retornar a mensagem  “Pelo menos um registro dever ser selecionado”. | OS4411 |
| Empresa | Editbox | S | N |  |  | OS4411 |
| Estabelecimento | Editbox | S | N |  |  | OS4411 |
| Cód. SCP | Editbox | S | N |  |  | OS4411 |
| Obrigação Fiscal | Editbox | S | N |  |  | OS4411 |
| Layout | Editbox | S | N |  |  | OS4411 |
| Situação | Editbox | S | N |  |  | OS4411 |
| Data inicial | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data inicial de geração dos registros. | OS4411 |
| Data final | Editbox | S | N | Formato: DD/MM/AAAA | Irá apresentar a data final de geração dos registros. | OS4411 |
| Nome do arquivo | Editbox | S | S |  | Informação será carregada automaticamente e  deverá ser não editável se flegado o checkbox “Atribuir nome padrão para o arquivo”.  Caso checkbox “Atribuir nome padrão para o arquivo” não selecionado deverá existir tratamento para validar se há nome de arquivo duplicado informado pelo usuário, se não informado exibir a seguinte mensagem: “É necessário informar o nome do arquivo a ser gerado”. | OS4411 |
| Diretório | Checkbox | N | S | Defaut: Não selecionado | Campo obrigatório caso o Checkbox “Gravação do Arquivo Magnético no Servidor” e  Definir diretório padrão para arquivos não preenchido, se não informado, exibir mensagem:  “É necessário escolher um diretório para depósito do arquivo gerado”.      Caso o campo “*Selecionador” não marcado, deverá limpar as informações uma vez digitadas pelo usuário e desabilitar o mesmo. | OS4411 |
| Marcar Todos | Checkbox | S | S | Default: Não Selecionado |  | OS4411 |
| Geração | Botão | N | N |  | Por se tratar de Multiempresa, irá gerar o meio magnético por estabelecimento “Centralizador” e “Descentralizador”, e demais parametrizações assim definidas pelo usuário. |  |
