# MTZ-Importacao_SAFX49

- **Fonte:** MTZ-Importacao_SAFX49.docx
- **Modificado:** 2024-04-11
- **Tamanho:** 32 KB

---

# JOB SERVIDOR – IMPORTAÇÃO SAFX49 \(Tabela das Operações de Importação\)

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

CH4515\_2012

Tratamento de dados para importação batch

Alterado o tratamento para importação batch com relação á data de referência\.

CH2004\_2016

Alteração tratamento para considerar datas

Este documento tem como objetivo alterar o tratamento para o preenchimento da Data da Nota Fiscal \(campo 05\) e a Data da Entrada da Nota Fiscal \(campo 14\)\.

MFS25010

Andréa Rocha

Inclusão de uma nova opção para o campo 72 \- Tipo da DI

MFS32068

Andréa Rocha

Inclusão de um novo campo – 74\-INCOTERM

MFS604387

Liliane Assaf

Criação de campos para atendimento ao SIPROQUIM2

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra Geral__

A importação batch deve considerar a mesma regra que hoje é usada para a importação normal, em que deve considerar as duas datas \(Campo 05 e Campo 14\) de acordo com a seguinte condição:

__\[ALTERADA – CH2004\_2016\]__

A princípio a importação deve considerar apenas a data do campo 14 \(Data Fato Gerador\),

	Se o campo 14 estiver nulo, então o processo deve passar a considerar a data do campo 05\.

Se as datas forem diferentes, ocorre seguinte crítica “Data de movimento informada no registro está fora do período definido para importação\.”\.

__CH4515\_2012__

__CH2004\_2016__

__RN01__

__Campo 17 – COD\_MODELO__

Aceitar a importação do novo código de modelo “58”\.

__OS3564__

__RN02__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX49

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN72__

__Campo Tipo da DI__

Lista de opções para o campo:

0 \- Declaração de Importação

1 \- Declaração Simplificada de Importação

2 – Declaração Única de Importação

Campo não obrigatório\.  Caso o campo esteja preenchido e o conteúdo não for válido, retornar a mensagem:

 “*O tipo de DI deve ser: <0> ou <1> ou <2>\.”*

__MFS25010__

__RN74__

__Campo INCOTERM__

Campo não obrigatório, sem validação de conteúdo\.

__MFS32068__

__RN75__

__Campo Tipo de Intermédio__

Campo de Preenchimento não obrigatório\.

Lista de Opções válidas:

1=Importação por conta própria;  
2=Importação por conta e ordem;  
3=Importação por encomenda;

Quando preenchido com um valor diferente de <1>, <2> e <3> o registro não será importado, e no log de erros será gravada uma mensagem:

*93640 \- O Tipo de Intermédio de ser  <1> ou <2> ou <3>*

__MFS604387__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

