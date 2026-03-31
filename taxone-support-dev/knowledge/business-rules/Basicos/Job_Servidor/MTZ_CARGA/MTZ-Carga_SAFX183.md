# MTZ-Carga_SAFX183

- **Fonte:** MTZ-Carga_SAFX183.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 30 KB

---

__         __

# Módulo Job Servidor – Carga SAFX183 \(Demais documentos e Receitas – Lucro Presumido\)

                      Localização: Menu Básicos, Módulo: Job Servidor, item Carga 🡪 Execução

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

Alterar a rotina de carga para que seja considerado o novo campo:

Tabela: SAFX183

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN02__

A rotina de Carga do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCTO da tabela SAFX183 – Demais documentos e Receitas – Lucro Presumido, que deve ser criada com a seguinte estrutura:

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

