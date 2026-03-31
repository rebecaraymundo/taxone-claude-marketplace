# MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_CFOP

> Fonte: MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_CFOP.docx






THOMSON REUTERS

Identificador da Nat. da Base de Crédito (por CFOP)


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





#### Fluxo Alternativo 1 – Localizar registros (Exemplo)




## Regras dos Campos


Localização da tela:
Módulo: SPED  EFD-Escrituração Fiscal Digital das Contribuições
Menu:    Parâmetros

Título da tela: Identificador da Nat. da Base de Crédito (por CFOP)

Funcionamento da Tela: A parametrização desta tela servirá para que o sistema deduza informações que são solicitadas em alguns registros e também na apuração do PIS/COFINS, porém não são carregadas em documentos fiscal, dessa forma, se faz necessária esta parametrização.






| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4156 | Elenilson Coutinho | Ident. da Nat. da Base de Crédito (por CFOP) – Inclusão do campo “Replicar para estabelecimentos”. |


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
| Estabelecimento | Editbox | S | N |  | Irá apresentar o Estabelecimento de login no sistema. |  |
| Nat. da Base de Crédito | Dropdown | S | S | Default: Não selecioando | Lista das naturezas da base de crédito, disponível na  tabela 4.3.7 do layout de geração da EFD-PIS/PASEP/COFINS conforme tabela abaixo:  Obs: Cada natureza da base de cálculo será associada a um grupo de CFOP’s, então, quando o usuário selecionar a natureza da base de crédito (campo 02), o sistema deve exibir no quadro “CFOP’s” os CFOP’s associados àquela natureza. |  |
| CFOP´s | Checbox | S | S | Default: Não selecionado | Deverão estar disponíveis para seleção todos os CFOP-s de entrada.  Obs: Quando o usuário marca um CFOP para associá-lo a uma determinada natureza, o sistema deve verificar se aquele CFOP já não está associado a alguma outra natureza que tenha sido previamente parametrizada. Caso isso ocorra deve emitir a seguinte mensagem:  “O CFOP <cod_cfo> já está associado à Natureza da Base de Crédito: <cod+descrição da natureza já parametrizada>. Não foi possível associá-lo à Natureza da Base de Crédito: <cod+descrição da natureza da tela>. Favor verificar.” |  |
| Selecionar Todos | Botão | N | N |  | Irá selecionar todos os CFOP´s listados em tela. |  |
| Desmarcar Todos | Botão | N | N |  | Irá desmarcar todos os CFOP´s listados em tela. |  |
| Replicar para os estabelecimentos | Checkbox | N | S | Default: Não selecionado | Deverá listar todos os estabelecimentos da empresa de login do sistema. | OS4156 |
| Selecionar Todos | Botão | N | N |  | Irá selecionar todos os CFOP´s listados em tela.  Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado. | OS4156 |
| Desmarcar Todos | Botão | N | N |  | Irá desmarcar todos os CFOP´s listados em tela.  Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado. | OS4156 |
