# MTZ-Job-Servidor-Importacao_SAFX2086

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2086.docx
- **Modificado:** 2020-10-20
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2086

Tabela de Códigos de Ajustes Provenientes de NF's \(SPED FISCAL\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS34482

Andréa Rocha

Criação de nova tabela SAFX para carga dos Códigos de Ajustes Provenientes de NF's \(SPED FISCAL\)\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX2086 🡪 vide manual de layout

Campo que compõe a chave da tabela:

__   Código de Ajuste do SPED__

A manutenção desta tabela é feita no Módulo Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Ajustes Provenientes de NF's \(SPED FISCAL\)

Tabela de Destino:

A SAFX2086 alimenta a tabela definitiva DWT\_COD\_AJUSTE\_SPED

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campo chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS34482

__RN01__

__Campo 01 \-  Código do Estado__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Campo UF nao esta preenchido”*

Crítica da existência da UF na tabela Estado:

Verificar se a UF está cadastrada na tabela Estado\. Caso a UF não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Campo UF não esta cadastrado”*

MFS34482

__RN02__

__Campo 02 \- Código do Ajuste do SPED __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Codigo de ajuste do SPED nao esta preenchido”*

MFS34482

__RN03__

__Campo 03 \- Descrição__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Descricao do codigo de ajuste nao esta preenchida”*

MFS34482

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

