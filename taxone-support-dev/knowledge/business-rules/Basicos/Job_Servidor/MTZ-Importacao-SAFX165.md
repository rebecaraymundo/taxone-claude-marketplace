# MTZ-Importacao-SAFX165

- **Fonte:** MTZ-Importacao-SAFX165.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 29 KB

---

# JOB SERVIDOR – IMPORTAÇÃO SAFX165 \(Incorporação Imobiliária – RET\)

__Módulo__: Básicos 🡪 Job Servidor

__Menu1__: Importação 🡪 Programação / Execução

__Menu2__: Importação batch 🡪 Programação / Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4316\-B

Criação de Campos

Criação do campo Código da SCP

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX165

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Campo chave, porém, não obrigatório

Comentário: Código da Sociedade em Conta de Participação

No processo de implementação da OS4316\-B os registros pré\-existentes na SAFX165 não devem ser excluídos\. Eles devem ser atualizados, de modo que a base pré\-existente não seja impactada\.

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316\-B__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

