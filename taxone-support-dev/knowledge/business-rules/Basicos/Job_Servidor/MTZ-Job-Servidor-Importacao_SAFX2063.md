# MTZ-Job-Servidor-Importacao_SAFX2063

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2063.docx
- **Modificado:** 2020-12-28
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2063

Tabela de Códigos de Informação Adicional da Apuração \(SPED FISCAL\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS46357

Andréa Rocha

Criação de nova tabela SAFX para carga dos Códigos de de Informação Adicional da Apuração \(SPED FISCAL\)\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX2063 🡪 vide manual de layout

Campo que compõe a chave da tabela:

__   Código da Informação Adicional__

A manutenção desta tabela é feita no Módulo SPED\-EFD, menu Parâmetros 🡪 Registro E115/1925 🡪 Informações Adicionais da Apuração \(Registros E115/1925\)

Tabela de Destino:

A SAFX2063 alimenta a tabela definitiva EFD\_INF\_ADIC\_APUR\.

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campo chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS46357

__RN01__

__Campo 01 \-  UF__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Campo UF nao esta preenchido”*

Crítica da existência da UF na tabela Estado:

Verificar se a UF está cadastrada na tabela Estado\. Caso a UF não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Campo UF não esta cadastrado”*

MFS46357

__RN02__

__Campo 02 \- Código da Informação Adicional__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Codigo da Informação Adicional nao esta preenchido”*

MFS46357

__RN03__

__Campo 03 \- Descrição__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Descricao do Código da Informação Adicional nao esta preenchida”*

MFS46357

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

