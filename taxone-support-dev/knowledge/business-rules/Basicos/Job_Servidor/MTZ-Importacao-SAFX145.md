# MTZ-Importacao-SAFX145

- **Fonte:** MTZ-Importacao-SAFX145.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 30 KB

---

# JOB SERVIDOR – IMPORTAÇÃO SAFX145 \(Contribuição Retida na Fonte\)

__Módulo__: Básicos 🡪 Job Servidor

__Menu1__: Importação 🡪 Programação / Execução

__Menu2__: Importação batch 🡪 Programação / Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

MFS\-2273

Alteração de Campo

Alteração do Campo Indicador da Natureza Receita

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX145

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN02__

__Campo Indicador da Natureza Receita__

Alterar a rotina de importação e importação batch para que seja considerada a inclusão do campo:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Indicador da Natureza Receita

N

001

NÃO

SIM

Obs: Caso não preenchido deverá ser gravado “9” na tabela\.

__MFS\-2273__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

