# MTZ-Importacao_SAFX161

- **Fonte:** MTZ-Importacao_SAFX161.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

    

# Módulo Job Servidor – Importação – Prestação de Serviços de Comunicação e de Telecomunicação Consolidadas \(SAFX161\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX149, conforme o Manual de Layout, o que facilita a consulta\)*

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

30/12/2013

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterados para contemplar os campos descritos abaixo na tabela SAFX161\.

__RN01__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX161

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

