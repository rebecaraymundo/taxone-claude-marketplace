# MTZ_Tela_Geracao_Registros_SCP

> Fonte: MTZ_Tela_Geracao_Registros_SCP.docx






THOMSON REUTERS

Matriz da tela Geração dos Registros - EFD-Contribuições para SCP



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

Título da tela: Geração dos Registros


* Descrição não disponível em tela



Exemplos:

Cadastro dos Estabelecimentos
- 001 - Estabelecimento Centralizador de Teste
- 002 - Estabelecimento Descentralizado de Teste
- 003 - Estabelecimento Centralizado de Teste *

Cadastro da SCP
ESTAB		COD_SCP		DESCRIÇÃO_SCP
001		001-14		Descrição da SCP 001-14
003		001-14		Descrição da SCP 001-14
003		002-20		Descrição da SCP 002-15
002		004-40		Descrição da SCP 004-40

Na tela de Geração dos Registros Teremos:
- Estab. Centralizador/SCP: 001/Sócio Ostensivo - Estabelecimento Centralizador de Teste
- Estab. Centralizador/SCP: 001/001-14 - Descrição da SCP 001-14 **
- Estab. Centralizador/SCP: 001/002-20 - Descrição da SCP 002-15 ***
- Estab. Descentralizado/SCP: 002/Sócio Ostensivo - Estabelecimento Descentralizado de Teste
- Estab. Descentralizado/SCP: 002/004-40 - Descrição da SCP 004-40

* Este estabelecimento foi centralizado no estabelecimento "001 - Estabelecimento Centralizador" através da tela de "Centralização da Escrituração de Obrigações Federais".
** Apesar de, no Cadastro da SCP existir informações para o código 001/14 para o estabelecimento 001 e 003, a informação aparece apenas uma vez vinculada ao centralizador.
*** Quando se trata de um estabelecimento centralizado, o código será demonstrado vinculado ao centralizador.


| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-A | Marcos G. de Paula | Definição das regras para a tela de Geração dos Registros da EFD-Contribuições para SCP. |
| OS4316-B | Marcos G. de Paula | Inclusão das opções de geração dos Demonstrativos da Apuração |
|  |  |  |
|  |  |  |


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
| Data Inicial | Data | S | S | Formato: DD/MM/AAAA |  | OS4316-A |
| Data Final | Data | S | S | Formato: DD/MM/AAAA |  | OS4316-A |
| Leiaute | Dropdown | S | S |  | A informação deste campo será demonstrada conforme data inicial e final informadas.  Quando a data final for até 30/06/2012, mostrar o Leiaute “1.0.0”; Quando a data inicial for maior ou igual a 01/07/2012, mostrar o Leiaute “2.0.1”.      Caso não seja informado, no momento da geração, retornar a mensagem: “Informe Leiaute”. | OS4316-A |
| Perfil | Dropdown | S | S |  | Conforme Leiaute parametrizado, carregar os Perfis cadastrados (menu Parâmetros > Perfil).  Caso não seja informado, no momento da geração, retornar a mensagem: “Informe Perfil”. | OS4316-A |
| Tipo de Escrituração | Dropdown | S | S | Default: Original | Exibir as opções: - Original - Retificadora | OS4316-A |
| Núm. Recibo Última Declaração | Editbox | N | S |  |  | OS4316-A |
| Gera NF-s de Entrada sem Crédito | Dropdown | S | S | Default: Não | Exibir as opções: - Sim - Não | OS4316-A |
| Demonstrativo da Apuração por Tipo de Crédito | Checkbox | N | S | Default: não selecionado |  | OS4316-B |
| Demonstrativo da Apuração por Tipo de Contribuição | Checkbox | N | S | Default: não selecionado |  | OS4316-B |
| Demonstrativo da Apuração por Tipo de Natureza da Receita | Checkbox | N | S | Default: não selecionado |  | OS4316-B |
| Geração Multiempresa | Checkbox | N | S | Default: não selecionado |  | OS4316-A |
| Empresa/Estabelecimento | Checkbox | S | S |  | Neste campo serão demonstradas apenas informações de estabelecimentos que foram parametrizados na tela de Cadastro da SCP (Manutenção >> Registro do Bloco 0 >> Cadastro da SCP) e considerando a informação de "Centralização da Escrituração de Obrigações Federais" (módulo: Parâmetros / menu: Preliminares).  Se o estabelecimento parametrizado no Cadastro da SCP for centralizador ou centralizado (pertence a um centralizador), exibir apenas a informação do estabelecimento centralizador, apresentando uma linha para cada Código da SCP cadastrada (se existir mais de um cadastro para o mesmo código, será mostrado apenas uma vez) e uma linha com a descrição "Sócio Ostensivo", com a seguinte formatação:  - Estab. Centralizador/SCP: COD_ESTAB/ Sócio Ostensivo - Descrição do Centralizador  - Estab. Centralizador/SCP: COD_ESTAB/ COD_SCP - Descrição da SCP  Se o estabelecimento parametrizado no Cadastro da SCP não for centralizador e não for centralizado (não pertence a nenhum centralizador), exibir a informação do estabelecimento, apresentando uma linha para cada Código da SCP cadastrada e uma linha com a descrição "Sócio Ostensivo", com a seguinte formatação:  - Estab. Descentralizado/SCP: COD_ESTAB/Sócio Ostensivo - Descrição do Descentralizado - Estab. Descentralizado/SCP: COD_ESTAB/ COD_SCP - Descrição da SCP  Quando for selecionada a opção de Geração Multiempresa, deve ser exibida a relação das empresas que têm estabelecimentos parametrizados na tela de Cadastro da SCP. Na geração das informações, serão geradas informações destes estabelecimentos, atendendo aos critérios acima definidos.  Exemplos abaixo. | OS4316-A |
