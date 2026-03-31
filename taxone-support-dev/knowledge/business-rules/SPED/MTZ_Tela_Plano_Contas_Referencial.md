# MTZ_Tela_Plano_Contas_Referencial

> Fonte: MTZ_Tela_Plano_Contas_Referencial.docx






THOMSON REUTERS

Matriz da tela de Plano de Contas Referencial



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
Menu: Manutenção

Título da tela: Plano de Contas Referencial



* Descrição não disponível em tela


| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4745 | Marcos G. de Paula | Atualização das opções disponíveis no campo Entidade Responsável. |
| MFS8620 | Lara Aline | Atualização das opções disponíveis no campo Entidade Responsável. |
| MFS17883 | João Henrique | Inclusão da opção 10 - Financeiras – Lucro Presumido. |
| MFS17892 | João Henrique | Atualização da versão do plano de contas referencial para 4.00 |
| MFS23870 | João Henrique | Atualização da versão do plano de contas referencial para 5.00 |
| MFS-60592 | Alessandra Cristina Navatta | Atualizada a especificação, considerando a versão 6.00 do plano de contas (apesar de não ser escopo da demanda)  Atualização da versão do plano de contas referencial para 7.00 |
| MFS-81170 | Alessandra Cristina Navatta | Atualização da versão do plano de contas referencial. Inclusão da versão 8.00 |
| MFS-511450 | Elisabete Costa | Atualização da versão do plano de contas referencial. Inclusão da versão 9.00 |
| MFS-599648 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 10.00 |
| MFS-749696 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 11.00 |
| MFS977310 | Rogério Ohashi | O objetivo dessa demanda é incluir as colunas de Data Inicial e Data Final, conforme informação da TFIX64, Somente para o código “00-SUSEP” |
| MFS-1035615 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 12.00 |


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
| Entidade Responsável | Alfa | S | S | Formato: Dropdown | Considerar a seguinte formatação para exibição:  00 - SUSEP 10 - Secretaria da Receita Federal 20 - Banco Central do Brasil (Cosif) 1 - PJ em Geral 2 - PJ em Geral - Lucro Presumido 3 - Financeiras 4 - Seguradoras 5 - Imunes e Isentas em Geral 6 - Financeiras - Imunes e Isentas 7 - Seguradoras - Imunes e Isentas 8 - Entidades Fechadas de Previdência Complementar 9 - Partidos Políticos 10 - Financeiras – Lucro Presumido/Secretaria da Receita Federal  Excluir a opção 10 - Secretaria da Receita Federal da lista, pois a mesma será atendida juntamente com a opção 10 - Financeiras – Lucro Presumido/Secretaria da Receita Federal.  Com base no conteúdo indicado neste campo, serão demonstradas as contas contábeis da TFIX64 na lista abaixo. Esta demonstração deve respeitar o que foi indicado no campo Versão, ou seja, para demonstração da listagem teremos uma combinação de Versão + Entidade Responsável indicada pelo usuário.  Ex.: Se o usuário seleciona Versão “1.00” e Entidade Responsável “00 – SUSEP”, na listagem abaixo serão demonstradas apenas as contas da Versão “1.00” e Entidade “00 – SUSEP”.  [ALTERAÇÃO-MFS977310] AlteraçãoTela Plano de Conta Referencial “00-SUSEP”  Conforme solicitação do cliente IRB, foram incluídas as colunas de Data Inicial e Data Final, conforme inforação da TFIX64. (somente para SUSEP). | OS4745 MFS8620 MFS17883 |
| Versão | N | S | S | DropDownList | Nesse campo serão exibidas as versões do plano de contas referencial. 1.00 2.00 3.00 4.00 5.00 6.00 7.00  8.00  9.00 10.00 11.00 12.00  Opção Default: Exibir a versão mais atual | MFS17892 MFS23870 MFS-60592 MFS-81170 MFS-511450 MFS-599648 MFS-749696 MFS-1035615 |
