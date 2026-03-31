# MTZ_Tela_Cadastro_SCP

> Fonte: MTZ_Tela_Cadastro_SCP.docx






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
Módulo: MasterSAF DW >> SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco 0

E

Módulo: MasterSAF DW >> Básicos >> Mastersaf DW
Menu: Manutenção >> Cadastros >> Cadastro da SCP (0035)
(inserir esta chamado entre os acessos à tela de “Bem Patrimonial” e “Canais de Distribuição / Obras”)


Título da tela: Cadastro da SCP



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316 | Marcos G. de Paula | Definição das regras da tela de Cadastro da SCP. |
| OS4745 | Marcos G. de Paula | Criação do campo Data de Validade Final e disponibilização da tela no módulo “Básicos” |


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
| Estabelecimento | Dropdown | S | S |  | Campo do tipo lista que demonstra a relação de estabelecimentos vinculados à empresa que acessou o módulo. | OS4316 |
| Data de Validade | Editbox | S | S | Formato: DD/MM/AAAA |  | OS4316 |
| Data de Validade Final | Editbox | N | S | Formato: DD/MM/AAAA | A data informada neste campo deve ser maior ou igual a data informada no campo Data de Validade. Caso seja menor, retornar mensagem de erro: “A data de validade Final deve ser maior que a data de validade inicial”. | OS4745 |
| Código da SCP | Editbox | S | S |  |  | OS4316 |
| Descrição da SCP | Editbox | N | S |  |  | OS4316 |
| Informação Complementar | Editbox | N | S |  |  | OS4316 |
