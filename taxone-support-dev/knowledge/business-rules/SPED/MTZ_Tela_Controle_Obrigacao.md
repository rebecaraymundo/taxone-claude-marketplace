# MTZ_Tela_Controle_Obrigacao

> Fonte: MTZ_Tela_Controle_Obrigacao.docx






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

Título da tela: Controle da Obrigação



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4745 | Marcos G. de Paula | Atualização das opções disponíveis no campo Tipo de Livro |
| MFS-46921 | Alessandra Cristina Navatta | Regra da aba ‘’Livros Auxiliares ao Diário e do campo “Informar Hash Code”, da aba Livros Principais ” |


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
| Livro | Alfa | S | S | Formato: Dropdown Default: não preenchido | Considerar a seguinte formatação para exibição:  G - Livro Diário (Completa sem Escrituração Auxiliar) R - Livro Diário com Escrituração Resumida (com Escrituração Auxiliar) B - Livro Balancetes Diários e Balanços (Matriz) S - Escrituração SCP Mantida pelo Sócio Ostensivo  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Informar o Livro”. | OS4745 |
| Aba Livros Auxiliares ao Balanço | - | - | - | desabilitada | Habilitar a aba, quando selecionados os livros:   R – Livro Diário com Escrituração Resumida (com Escrituração Auxiliar) B – Livro Balancetes Diários e Balanços (Matriz)   Quando a aba for habilitada, disponibilizar no campo Tipo de Livro as opções:  Para os livros ‘R – Livro Diário com Escrituração Resumida (com Escrituração Auxiliar)’ e  ‘B – Livro Balancetes Diários e Balanços (Matriz)’, para o livro:  A – Livro Diário Auxiliar ao com Escrituração Resumida;  Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555); | MSF-46921 |
| Informar Hash Code | - | - | - | habilitada | Campo Informar Hash Code  Disponibilizar este campo na tela (aba Livros Principais), quando o campo ‘Livro’ estiver preenchido com:  B – Livro Balancetes Diários e Balanços (Matriz); R – Livro Diário com escrituração Resumida (Com Escrituração Auxiliar); | MSF-46921 |
