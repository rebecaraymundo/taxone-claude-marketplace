# MTZ_REINF_Tela_Tipo_Documento

> Fonte: MTZ_REINF_Tela_Tipo_Documento.docx






THOMSON REUTERS

EFD Reinf
Matriz da Tela  - Parametrização do Tipo de Documento



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

Módulo: MasterSAF DW >> SPED >> EFD Reinf
Menu: Retenções Federais >> Parâmetros >> Tipo de Documento

Título da tela: Parâmetrização do Tipo de Documento















| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS6645 | Jefferson Mota | Definição das regras da tela de Parametrização do Tipo de Documento para o EFD Reinf. |
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
| Tipo de Vinculação | ComboBox | S | S | Default: Em Branco | Deve exibir apenas a Lista de Tipo de Documentos da tabela TFIX84, cujo o código de módulo seja referente ao módulo EFD Reinf.   Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Tipo de Vinculação deve ser selecionado”. | MFS6645 |
| Tipo de Documento | Checkbox | S | S | Default: não selecionado | - Local onde deve exibir uma lista com código e descrição dos tipos de documentos, que constam na tabela SAFX2005.  - Quando um Tipo de Documento (SAFX2005) já estiver vinculado com  “Documento Fiscal”, não pode ser exibido para associação com o “Contas a Pagar” e vice-versa;  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Tipo de Documento deve ser Escolhido”. | MFS6645 |
|  |  |  |  |  |  |  |
