# MTZ-Exportacao_SAFX05

- **Fonte:** MTZ-Exportacao_SAFX05.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 31 KB

---

__         __

# Módulo Job Servidor – Exportação SAFX05 \(Arquivo de Contas a Pagar\)

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

Elenilson Coutinho

Alteração do tamanho do Campo NUM\_LANCAMENTO

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX05

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN01__

__Campo NUM\_LANCAMENTO__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX05

Item: 27

Nome do Campo: Número do Lançamento

Tipo: A

Tamanho: 040

Obrigatório: Não

Chave: Não

Comentário: Informar o número ou código do lançamento contábil, correspondente ao cadastramento inicial do título\. Atende o Ato Cotepe nr 70/05 \- Registro Z030\.

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

