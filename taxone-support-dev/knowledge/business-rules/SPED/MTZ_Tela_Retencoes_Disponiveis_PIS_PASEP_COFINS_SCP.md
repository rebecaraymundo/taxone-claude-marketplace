# MTZ_Tela_Retencoes_Disponiveis_PIS_PASEP_COFINS_SCP

> Fonte: MTZ_Tela_Retencoes_Disponiveis_PIS_PASEP_COFINS_SCP.docx






THOMSON REUTERS

Matriz da tela Retenções Disponíveis - PIS/PASEP e COFINS - menu SCP



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
Menu: Obrigação SCP >> Manutenção >> Controle das Retenções na Fonte – PIS/PASEP
e
Menu: Obrigação SCP >> Manutenção >> Controle das Retenções na Fonte –COFINS

Esta tela deverá ser uma replica da tela de Retenções Disponíveis disponível no menu Obrigação >> Manutenção >> Controle das Retenções na Fonte – PIS/PASEP e Obrigação >> Manutenção >> Controle das Retenções na Fonte – COFINS, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-B | Marcos G. de Paula | Duplicação da tela com inclusão do campo Código da SCP. |
| OS4649 | Elenilson Coutinho | Inclusão de indicadores de Natureza da Retenção |


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
| Código da SCP | Editbox | N | N | ‘ | Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código. Deverá acessar as informações da tabela SAFX2057.  Este campo servirá com base para pesquisa das retenções geradas a partir do processamento realizado pelo menu Obrigações SCP, sendo que, se não for informado na pesquisa nenhum código da SCP para pesquisa, devem ser considerados os registros de crédito gerados para o Sócio Ostensivo, que não tem nenhum código de SCP vinculado. | OS4316-B |
| Natureza da Retenção na Fonte | DropDown | S | S |  | Deverá incluir na lista os indicadores:  51 – Retenção por Órgãos, Autarquias e Fundações Federais 52 – Retenção por outras Entidades da Administração Pública Federal	 53 – Retenção por Pessoa Jurídicas de Direito Privado 54 – Recolhimento por Sociedade Cooperativa 55 – Retenção por Fabricante de Máquinas e Veículos  59 – Outras Retenções – Rendimentos sujeitos à regra específica de incidência cumulativa (art. 8° da Lei n° 10.637/2002 e art. 10 da Lei n° 10.833/2003). | OS4 649 |
