# MTZ_Tela_Creditos_Disponiveis_PIS_PASEP_COFINS_SCP

> Fonte: MTZ_Tela_Creditos_Disponiveis_PIS_PASEP_COFINS_SCP.docx






THOMSON REUTERS

Matriz da tela Créditos Disponíveis - PIS/PASEP e COFINS - menu SCP



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
Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP
e
Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – COFINS

Esta tela deverá ser uma replica da tela de Créditos Disponíveis disponível no menu Obrigação >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP e Obrigação >> Manutenção >> Controle dos Créditos Fiscais – COFINS, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4316-B | Marcos G. de Paula | Duplicação da tela com inclusão do campo Código da SCP. |  |
| MFS28515 | Andréa Rocha | Incluir uma nova opção para o campo Status. | 18/10/2019 |
| MFS34355 | Liliane Assaf | Alteração no tratamento dos créditos prescritos com mais de 5 anos. Desfazendo a alteração feita pela MFS28515 | 28/06/2020 |


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
| Código da SCP | Editbox | N | N |  | Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código. Deverá acessar as informações da tabela SAFX2057.  Este campo servirá com base para pesquisa dos créditos gerados a partir do processamento realizado pelo menu Obrigações SCP, sendo que, se não for informado na pesquisa nenhum código da SCP para pesquisa, devem ser considerados os registros de crédito gerados para o Sócio Ostensivo, que não tem nenhum código de SCP vinculado. | OS4316-B |
| Status | Listbox | N | S |  | Campo somente para consulta.  Valores que compõe esse campo: - Disponível - Fechado  O campo vai ser habilitado para alteração, com as seguintes opções: - Disponível - Cancelado por Prazo de Prescrição  Obs.:  Quando o Status for igual a “Fechado”, não ficará habilitado para alteração. | MFS28515 MFS34355 |
