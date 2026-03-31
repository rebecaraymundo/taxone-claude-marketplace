# MTZ_Tela_Manutenção_Receita_Bruta_Mensal_Rateio_Créditos_Comuns

> Fonte: MTZ_Tela_Manutenção_Receita_Bruta_Mensal_Rateio_Créditos_Comuns.docx






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
Menu: Manutenção >> Receita Bruta Mensal - Rateio de Créditos Comuns


* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-C | Marcos G. de Paula | Criação do campo Código da SCP. |
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
| Código da SCP | Editbox | N | S | ‘ | Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código. Deverá acessar as informações da tabela SAFX2057.  Este campo deverá ser chave, mas não obrigatório.  Caso não exista estabelecimento selecionado no Manager e o usuário tente selecionar o “Código da SCP”, será exibida mensagem de erro “Estabelecimento não selecionado no Manager. Por gentileza selecionar um estabelecimento e reabrir o módulo.”. | OS4316-C |
