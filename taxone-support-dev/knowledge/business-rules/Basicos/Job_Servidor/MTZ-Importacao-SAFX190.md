# MTZ-Importacao-SAFX190

- **Fonte:** MTZ-Importacao-SAFX190.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 31 KB

---

# JOB SERVIDOR – IMPORTAÇÃO SAFX190 \(Fornecimento de Energia Elétrica, Água Canalizada e Gás \- Consolidados\)

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

CH1749\_2017

\(MFS\-9515\)

Alteração do campo 12\-Valor Total acumulado dos documentos

Alteração do campo 12\-Valor Total acumulado dos documentos para não obrigatório\.

MFS29621

Andréa Rocha

Alterar a regra do campo Modelo de documento

MFS33637

Andréa Rocha

Inclusão do modelo 66 para o campo Modelo de documento

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Campo 25\-Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX190

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN02__

__Campo 12\-Valor Total acumulado dos documentos__

__\[ALTERADA – CH1749\_2017 \(MFS\-9515\)\]__

Tabela: SAFX190

Item: A ser reservado pelo A&D

Nome do Campo: Valor Total acumulado dos documentos

Tipo: N

Tamanho: 15,2

Comentário: Valor Total acumulado dos documentos

Campo obrigatório

O campo passa a ser não obrigatório a partir da MFS\-9515, e quando não for informado na importação, será preenchido com zero, já que não podem ficar nulo por ser campo chave\.

__CH1749\_2017__

__\(MFS\-9515\)__

__RN03__

__Campo 03\-Modelo de Documento__

__\[MFS29621\]__

__\[MFS33637\] – Inclusão do modelo 66__

Este campo trabalha com os códigos de modelos da Tabela de Modelos de Documento \(SAFX2024\), somente serão aceitos os códigos de modelos iguais a “01”, “06”, “28”, “29”, “55” e “66”\.

__MFS29621__

__MFS33637__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

