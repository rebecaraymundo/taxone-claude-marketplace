# MTZ_Tela_Detalhamento_por_Codigo_Receita_COFINS

> Fonte: MTZ_Tela_Detalhamento_por_Codigo_Receita_COFINS.docx






THOMSON REUTERS

Matriz da tela Detalhamento por Código de Receita (Visão Débito DCTF) -  M605



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
Módulo: SPED >> EFD- Contribuições Financeira/Assemelhada
Menu: Obrigações >> Manutenção >> Apuração COFINS

Deverá ser criada a tela “Detalhamento por Código de Receita (Visão Débito DCTF) – M605” para que seja possível realizar a geração do registro M605 da EFD-Contribuições.

Esta tela será acessada através de nova aba inserida na tela de Apuração COFINS. Estará no mesmo nível da aba Detalhamento da Contribuição – M610 por ser registro filho do M600 – Contribuição para COFINS no período.

Deverá ser criada a tela de lista, permitindo a visualização das informações gravadas e a tela de detalhe, que será acessada na inserção de novas informações ou a partir de uma linha da tela de listagem.


* Descrição não disponível em tela










| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS3810-H1 | Marcelo Souza | Criação da tela Detalhamento por Código de Receita (Visão Débito DCTF) Registro – M605. |
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
| Nº do Campo | Dropdownlist | S | S | Default: não informado | Opções validas na lista: 08 – Valor da Contribuição Não-Cumulativa 12 – Valor da Contribuição Cumulativa  Este campo deverá ser chave. | OS3810-H1 |
| Cód. de Receita | Dropdown | S | S | - | Campo Cód. de Receita no formato drowdown do Mastersaf DW. Deverá acessar as informações da tabela TACES14.  Este campo deverá ser chave. | OS3810-H1 |
| Valor do Débito | Editbox | S | S | - |  | OS3810-H1 |
