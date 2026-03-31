# MTZ-OTF-Dividir_DARFs_em_Quotas

- **Fonte:** MTZ-OTF-Dividir_DARFs_em_Quotas.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 32 KB

---

# Módulo – Obrigações de Tributos Federais

# Parametrização da Divisão do DARF em Quotas

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3509

Obrigações de Tributos Federais \- Divisão do DARF em Quotas

O sistema deve permitir uma parametrização para a divisão em quotas\.

## REGRAS DE NEGÓCIO

#### Cód\.

####                                                                                                  Descrição

### DR

__RN01__

Deverá ser criada uma tela para permitir a parametrização da divisão do DARF em quotas\. Essa tela será chamada de “Divisão do DARF em Quotas”\. Essa tela será disponibilizada no menu Outras Obrigações >> DARF’s, antes do menu “Saldo Credor para Compensação dos Tributos Federais”\.

__OS3509__

__RN02__

Deverá ser criado um relatório de conferência para essa tela\.

__OS3509__

__RN03__

Deverão ser criados os seguintes campos nessa tela:

- __Empresa:__ o sistema irá exibir as Empresas licenciadas do sistema e que o usuário tenha permissão de acesso\. O sistema irá exibir a Empresa selecionada no Manager\. Caso nenhuma Empresa esteja selecionada, o campo deverá ficar em branco\. O sistema irá exibir as Empresas a partir da tabela EMPRESA\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ o sistema irá exibir os Estabelecimentos do sistema e que o usuário tenha permissão de acesso\. O sistema irá exibir o Estabelecimento selecionado no Manager\. Caso nenhum Estabelecimento esteja selecionado, o campo deverá ficar em branco\. O sistema irá exibir os Estabelecimentos a partir da tabela ESTABELECIMENTO\. Campo obrigatório de preenchimento\.
- __Código DARF: __o usuário poderá informar o Código DARF\. O sistema deverá permitir que o usuário selecione o Código DARF a partir da tabela X2019\. Campo não obrigatório de preenchimento\.
- __Qtde\. Máxima de Quotas:__ o usuário deverá informar a quantidade máxima de Quotas\. O sistema deverá permitir que o usuário informe as quantidades “2” ou “3”\. Por default, o campo será exibido “em branco”\. Caso o usuário informe um valor diferente de “2” ou “3”, o sistema deverá exibir mensagem de erro informando a ocorrência\. Campo não obrigatório de preenchimento\.
- __Replicar para os Estabelecimentos:__ nessa opção o sistema irá permitir que o usuário replique a parametrização para os outros Estabelecimentos da Empresa selecionada\.

O sistema deverá permitir que os registros dessa tela possam ser incluídos, consultados, alterados e excluídos\.

__OS3509__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

