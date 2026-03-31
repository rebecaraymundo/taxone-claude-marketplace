# MTZ_Tela_Status_SCP

> Fonte: MTZ_Tela_Status_SCP.docx






THOMSON REUTERS





DOCUMENTO DE REQUISITO


Sumário














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

Título da tela: Status da Obrigação

Funcionamento da tela: através desta tela será possível alterar o status de um arquivo gerado com informações da EFD-Contribuições para empresas que atuam em SCP.



Esta tela é uma réplica da tela de Status da Obrigação do menu “Obrigações”, tendo como diferença o campo “Cód. SCP”, uma vez que foi gerado um arquivo para o Sócio Ostensivo e de “1” a “N” arquivos para as SCPs.

Importante: As informações demonstradas nesta tela devem ser apenas referentes a geração de SCP e não devem demonstrar informações da geração normal. Da mesma forma, através da geração normal não deve ser possível visualizar informações da geração de SCP.


* Descrição não disponível em tela











| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-A | Marcos G. de Paula | Definição das regras para a tela de Status da Obrigação para SCP. |
|  |  |  |
| CH15667/2014 | Julyana Perrucini | Alteração da lista de seleção do campo “Empresa” incluindo tratamento para demonstrar somente as empresas que o usuário tem permissão de acesso no powerlock. |
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
|  |  | S |  |  | [ALTERADA – CH15677_2014] Tratamento: Listar somente as empresas que o usuário tem permissão de acesso no powerlock em User/Company Maintenance – (usuário). | CH15677_2014 |
| Cód. SCP | Editbox |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Período | Editbox | S |  |  |  | OS4316-A |
| Situação |  | S | S |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Observação | Editbox | N | S |  |  | OS4316-A |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
