# MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_Servico

> Fonte: MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_Servico.docx






THOMSON REUTERS

Identificador da Nat. da Base de Crédito (por Serviço)


DOCUMENTO DE REQUISITO



## Regras dos Campos


Localização da tela:
Módulo: SPED  EFD-Escrituração Fiscal Digital das Contribuições
Menu:    Parâmetros  Identificador da Nat. da Base de Crédito  Por Código de Serviço

Título da tela: Identificador da Nat. da Base de Crédito (por Serviço)







| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS847777 | Andréa Rocha | Inclusão do código 14 (Transporte de Cargas) no campo Nat. da Base de Crédito. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Editbox | S | N |  | Irá apresentar a lista de Estabelecimentos disponíveis para a Empresa. |  |
| Nat. da Base de Crédito | Dropdown | S | S | Default: Não selecioando | Lista das naturezas da base de crédito, disponível na  tabela 4.3.7 do layout de geração da EFD-PIS/PASEP/COFINS, conforme tabela abaixo: | MFS847777 |
| Grupo | Dropdown | S | S | Default: Não selecionado | Irá apresentar a lista de grupos disponíveis para o estabelecimento selecionado. |  |
| Seleção de Serviços | Checkbox | S | S | Default: Não selecionado | Deverão estar disponíveis para seleção todos os códigos de serviços cadastrados na tabela de Códigos de Serviços (SAFX2018). |  |
| Selecionar Todos | Botão | N | N |  | Irá selecionar todos os serviços listados em tela. |  |
| Desmarcar Todos | Botão | N | N |  | Irá desmarcar todos os serviços listados em tela. |  |
| Replicar para os estabelecimentos | Checkbox | N | S | Default: Não selecionado | Deverá listar todos os estabelecimentos da empresa de login do sistema. |  |
| Selecionar Todos | Botão | N | N |  | Irá selecionar todos os serviços listados em tela.  Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado. |  |
| Desmarcar Todos | Botão | N | N |  | Irá desmarcar todos os serviços listados em tela.  Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado. |  |
