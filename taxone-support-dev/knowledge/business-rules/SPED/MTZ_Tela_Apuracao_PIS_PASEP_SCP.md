# MTZ_Tela_Apuracao_PIS_PASEP_SCP

> Fonte: MTZ_Tela_Apuracao_PIS_PASEP_SCP.docx






THOMSON REUTERS

Matriz da tela Apuração PIS/PASEP - menu SCP



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
Menu: Obrigações SCP >> Manutenção >> Apuração PIS/PASEP

Esta tela deverá ser uma replica da tela de Apuração PIS/PASEP disponível no menu Obrigações >> Manutenção >> Apuração PIS/PASEP, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração.

As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros. No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, Código da SCP, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-B | Marcos G. de Paula | Duplicação da tela com inclusão do campo Código da SCP. |
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
| Código da SCP | Editbox | N | N | ‘ | Deverá carregar a informação selecionada referente ao campo no acesso à tela.  Quando se tratar do arquivo do Sócio Ostensivo, exibir a descrição: “Ostensivo”. | OS4316-B |
