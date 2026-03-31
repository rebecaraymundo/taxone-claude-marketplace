# MTZ_Tela_Numero_Ordem

> Fonte: MTZ_Tela_Numero_Ordem.docx






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
Módulo: SPED >> ECD-Escrituração Contábil Digital
Menu: Parâmetros

Título da tela: Número de Ordem



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4745 | Marcos G. de Paula | Atualização das opções disponíveis no campo Tipo de Livro |
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
| Tipo Livro | Alfa | S | S | Formato: Dropdown Default: não preenchido | Considerar a seguinte formatação para exibição:  Z  Razão Auxiliar (Livro Contábil Auxiliar conforme Leiaute definido nos Registros I500) A  Livro Diário Auxiliar com Escrituração Resumida G  Livro Diário (Completa sem Escrituração Auxiliar) R  Livro Diário com Escrituração Resumida (com Escrituração Auxiliar) B  Livro Balancetes Diários e Balanços (Matriz) S  Escrituração SCP Mantida pelo Sócio Ostensivo  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Informar o Livro”. | OS4745 |
| Livro Auxiliar ao Diário | Alfa | N | S | Formato: Dropdown Default: não preenchido | Exibe a relação de Livros Auxiliares ao Diário. Fica habilitado apenas quando o campo Tipo Livro é igual a “Z  Razão Auxiliar (Livro Contábil Auxiliar conforme Leiaute definido nos Registros I500)” ou “A  Livro Diário Auxiliar com Escrituração Resumida” |  |
