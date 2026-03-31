# MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Natureza_Receita

> Fonte: MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Natureza_Receita.docx






THOMSON REUTERS

Matriz da tela/relatório Demonstrativo da Apuração por Tipo de Natureza da Receita


Localização:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu:      Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita
Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	1
1.1.	Diagrama de Casos de Uso	1
1.1.1.	UC001 – Manutenção da Estrutura Padrão	1
1.1.1.1.1.	Fluxo Principal	1
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	1
2.	Regras dos Campos	1
3.	Sugestão de Layout	1
4.	Relatório	1

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
Menu: Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita
Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros.
No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, Código da SCP*, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout.

*Caso seja gerado por SCP.


.



## Sugestão de Layout


## Relatório


Ver documento matriz MTZ_Relatorio_de_Demonstrativo_da_Apuracao_EFD_PISPASEP-COFINS.doc


| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS3583 | Alteração – Tela de Emissão do Relatório Demonstrativo da Apuração | Criação da tela de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Natureza de Crédito’’ |
| OS4316-B | Marcos G. de Paula | Duplicação da tela e relatório com seleção da apuração por SCP. |
| MFS37761 | Liliane V. Assaf | Para o TAX ONE habilitar apenas a opção sintético, pois o relatório analítico passa a ser disponibilizado na opção de menu “Relatórios  Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)” |


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
| Tipo | Texto | S | S | Formato:  Radio Button Group  Default:  Habilitado Sintético | Deve ser informado o tipo de relatório que é emitido.  Conteúdo: Analítico  Sintético  Considerações:  [MFS37761] No TAX ONE o relatório Analítico passou a ser gerado através da opção de menu “Relatórios >> Demonstrativo de Apuração (Crédito/Contribuição/Natureza da Receita)”. Desta forma, apenas a opção Sintético fica habilitada para utilização. No DW as duas opções Sintético e Analítico permanecem habilitadas. | OS3583 MFS37761 |
| Cód. Sit. Tributária Específica | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | O campo Cód. Sit. Tributária Específica deve possuir as opções abaixo.               < > 	   Opção Branco | OS3583 |
| Registro | Texto | S | S | Formato:  Check Box  Default:  Habilitado e Todos Marcados | Esse campo deve possuir as opções abaixo. O campo é de preenchimento obrigatório. Além disso, por default  todas as opções devem ficar marcados. M400 –  M410 –  M800 –  M810 – | OS3583 |
|  |  |  |  |  |  |  |
