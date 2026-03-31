# MTZ-Job-Servidor-Importacao_SAFX238

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX238.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX238

Tabela de Tipo do Item x NCM

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS5432

Lara Aline

Criação de nova tabela SAFX para carga da parametrização do Tipo do Item x NCM para o Registro 0200\. 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX238 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__   Código da Empresa \+ Código do Estabelecimento \+ NCM \+ Inicio Validade__

A manutenção desta tabela é feita no Módulo EFD – Escrituração Fiscal Digital, menu Parâmetros 🡪 Registro 0200 🡪 Tipo do Item 🡪 Tipo do item x NCM ou Módulo EFD – Escrituração Fiscal Digital das Contribuições, menu Parâmetros 🡪 Registro 0200 🡪 Tipo do Item 🡪 Tipo do item x NCM

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS5432

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS5432

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS5432

__RN04__

__Campo NCM __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        * *“O Campo Codigo NBM deve ser preenchido”*

Crítica da existência do NCM na SAFX2043:

Será verificada a existência do NCM informado na Tabela de Classificação Fiscal \(SAFX2043\), e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                             * *“O Campo Codigo NBM nao esta cadastrado\.”*

MFS5432

__RN03__

__Campo Tipo do Item__

Campo de preenchimento __*obrigatório*__\.

Valores válidos:

00 – Mercadoria para Revenda;

01 – Matéria\-Prima;

02 – Embalagem;

03 – Produto em Processo;

04 – Produto Acabado;

05 – Subproduto;

06 – Produto Intermediário;

07 – Material de Uso e Consumo;

08 – Ativo Imobilizado;

09 – Serviços;

10 – Outros insumos;

99 – Outras

Quando não preenchido, ou quando for um tipo do item inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Tipo do item não preenchido ou inválido”*

MFS5432

__RN06__

__Campo Início Validade __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data de Validade e invalido”*

MFS5432

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

