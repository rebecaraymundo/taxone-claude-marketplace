# MTZ-Job-Servidor-Importacao_SAFX991

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX991.docx
- **Modificado:** 2021-05-20
- **Tamanho:** 32 KB

---

# JOB SERVIDOR – SAFX991 \(Capa Redução Z\)

__Módulo__: Básicos 🡪 Job Servidor

__Menu1__: Importação 🡪 Programação / Execução

__Menu2__: Importação batch 🡪 Programação / Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3564

Novo código de modelo – 58\.

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra Geral__

__RN01__

__Campo 03 \- COD\_MODELO__

Aceitar a importação do novo código de modelo “58”\.

OS3564

__RN02__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX991

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

