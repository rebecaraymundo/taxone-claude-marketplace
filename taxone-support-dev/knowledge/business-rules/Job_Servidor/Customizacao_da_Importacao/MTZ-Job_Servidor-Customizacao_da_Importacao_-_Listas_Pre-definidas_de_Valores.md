---
source: "MTZ-Job Servidor-Customizacao da Importacao - Listas Pré-definidas de Valores.docx"
category: Job_Servidor
converted: auto
---





THOMSON REUTERS

Módulo Básicos - Job Servidor


Tela de Listas Pré-definidas de Valores


Localização: Menu Básicos, módulo Job Servidor, menu Importação  Customização da Importação  Listas Pré-definidas de Valores





DOCUMENTO DE REQUISITO






Sumário

**1.	Regras Gerais	2**
2.	Layout da Tela	3
3.	Regras de Funcionamento dos Campos	4
4.	Consistências:	4


# Regras Gerais

Muitos clientes DW criam processos customizados para completarem o preenchimento de campos da SAFX, visto que a informação não é extraída do sistema de origem.

Com o advendo do TAX ONE os processos customizados não podem mais ser utilizados, visto que a base de dados é mantida pela Thomson Reuters.

Desta forma, para continuar permitindo o preenchimento dos campos que não são carregados via interface, estamos propondo uma solução onde é possível criar regras de preenchimentos de campos da SAFX a serem executadas no momento da importação.

Esta solução é composta pelas seguintes funcinalidades:
Tela de Cadatro das Listas Pré-definidas de Valores;
Tela de Cadastro de Regras para Importação;
Execução das regras de preenchimento pelo processo de importação Online;
Execução das regras de preenchimento pelo processo de importação Batch (apenas pela opção de Importação por Tabela SAFX).

Este documento matriz tem como objetivo definir o funcionamento da Tela de Cadastro de Lista de Valores.

As regras de preenchimento muitas vezes podem referenciar a um conjunto de valores.  Nesta tela será possível criar uma lista e atribuir vários itens para a mesma. Exemplo:
Lista:     001 - CFOP DE IMPORTACAO
Valores: 3100 – Importação de produtos alimentíceos
3200 – Importação de aço
3300 – Importação de madeira



# Layout da Tela

Tabela: CAD_IMP_LISTA e CAD_VAL_IMP_LISTA


Lista de Valores: [código]   [descrição                                                                                              ]

Itens da Lista:
[ x ] Código:      [                                                                                                   ]
Descrição:  [                                                                                                                                                                        ]
[ x ] Código:       [                                                                                                   ]
Descrição:  [                                                                                                                                                                        ]
[ x ] Código:       [                                                                                                   ]
Descrição: [                                                                                                                                                                        ]
[Incluir]  [Excluir]



Botões da barra de menu:



# Regras de Funcionamento dos Campos





# Consistências:

4.1 – Ao acionar um dos botões Novo, Abre ou Fecha, caso a Lista de Valores não tenha sido salva, dar mensagem padrão do sistema.

4.2 – Ao acionar um dos botões Novo, Abre ou Fecha, caso os Itens da Lista de Valores, incluídos, alterados ou excluídos, não tenham sido salvos, dar mensagem padrão do sistema.

4.3 – Não permitir salvar Lista de Valores sem item. Ao salvar a Lista, se não existir item, exibir mensagem abaixo e não salvar.
“A lista de valor deve conter pelo menos um item”

4.4 – Não permitir excluir Lista de Valores que estiver sendo utilizada por alguma regra. Ao acionar o botão Exclui do menu, caso isso ocorra, exibir mensagem abaixo e não efetuar a exclusão da lista.
“Não é permitida a exclusão da lista, pois a mesma está sendo referenciada em regras da importação”


= = = = = =

---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS30336 | Liliane Assaf | Criação da tela de cadastro da lista de valores. Esta MFS compõe a solução do atendimento a demanda que cria regras para preenchimendo de campos da SAFX, que não vem preenchidos pela interface. Os campos que possuem regras definidas, serão preenchidos no momento da importação através da execução das regras. | 27/09/2019 |
|  |  |  |  |
|  |  |  |  |


---

| NOVO | Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar a uma nova Lista de Valores |
| --- | --- |
| ABRE | Exibe janela de pesquisa das Listas de Valores já cadastrada. Apresenta os campos Código e Descrição da Lista de Valores, para que o usuário selecione a que desejar ser exibida em tela. |
| EXCLUI | Opção para excluir uma Lista de Valores. |
| CONFIRMA | Opção para salvar os dados da Lista de Valores e dos seus itens que estão sendo incluídos / alterados ou excluídos. |
| RELATÓRIO | Esta opção permite imprimir os dados da Lista de valores e dos seus itens.  Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Código da Lista de Valores | Alfanumérico | S | S |  |  |
| Descrição da Lista de Valores | Alfanumérico | S | S |  |  |
| Botão Incluir |  |  |  |  | Através deste botão uma linha é criada com os campos Código e Descrição em branco. Para que a inclusão dos itens seja salva, é necessário a selecão do botão Confirma. |
| Botão Excluir |  |  |  |  | Através desse botão, os itens da lista que estão selecionados, são excluídos da lista.  Para que a exclusção dos itens seja salva, é necessário a selecão do botão Confirma. |
| Código do Item da Lista | Alfanumérico | S | S |  | Tamanho até 100 caracteres. |
| Descrição do Item da Lista | Alfanumérico | S | S |  | Tamanho até 200 caracteres. |
