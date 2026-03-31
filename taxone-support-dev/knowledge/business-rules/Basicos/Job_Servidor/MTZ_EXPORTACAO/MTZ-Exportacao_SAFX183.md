# MTZ-Exportacao_SAFX183

- **Fonte:** MTZ-Exportacao_SAFX183.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 31 KB

---

__         __

# Módulo Job Servidor – Exportação SAFX183 \(Demais documentos e Receitas – Lucro Presumido\)

__Módulo__: Básicos 🡪 Job Servidor\.

__Menu__: Exportação 🡪 Programação – Execução

              Exportação Batch 🡪 Programação \- Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

OS4579

Alteração no tamanho do campo 

Alteração no tamanho do campo NUM\_LANCTO para 40 posições\.

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX183

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN02__

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCTO da tabela SAFX183 – Demais documentos e Receitas – Lucro Presumido, que deve ser criada com a seguinte estrutura:

__ __

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCTO

A

40

NAO

NAO

__OS4579__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

