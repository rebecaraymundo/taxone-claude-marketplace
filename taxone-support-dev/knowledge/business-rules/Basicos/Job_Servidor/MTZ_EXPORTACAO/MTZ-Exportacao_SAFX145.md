# MTZ-Exportacao_SAFX145

- **Fonte:** MTZ-Exportacao_SAFX145.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 32 KB

---

__         __

# Módulo Job Servidor – Exportação SAFX145 \(Contribuição Retida na Fonte\)

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

MFS\-2273

Alteração de Campo

Alteração do Campo Indicador da Natureza Receita

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX145

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN02__

__Campo Indicador da Natureza Receita__

Alterar a rotina de exportação para que seja considerada a inclusão do campo:

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

