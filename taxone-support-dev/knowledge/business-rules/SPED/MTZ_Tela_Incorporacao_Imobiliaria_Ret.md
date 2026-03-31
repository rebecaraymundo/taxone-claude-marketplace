# MTZ_Tela_Incorporação_Imobiliaria_Ret

> Fonte: MTZ_Tela_Incorporação_Imobiliaria_Ret.docx






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
Menu: Manutenção >> Incorporação Imobiliária – Ret (1800)

* Descrição não disponível em tela

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-B | Marcos G. de Paula | Criação do campo Código da SCP. |
| CH14608_2015 | Lara Aline | Alteração na nomenclatura do campo Insc. Imobiliária para Incorporação Imobiliária. |


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
| Código da SCP | Editbox | N | S |  | Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código. Deverá acessar as informações da tabela SAFX2057.  Este campo deverá ser chave, mas não obrigatório. | OS4316-B |
| Inc. Imobiliária | Alfanumérico | S | S |  | Altera a nomenclatura do campo Insc. Imobiliária para Inc. Imobiliária.  Alterar também a mensagem de erro 92242 da TFIX22 de “Inscricao Imobiliaria não informada e invalida” para “Incorporação Imobiliária não informada e inválida”. | CH14608_2015 |
