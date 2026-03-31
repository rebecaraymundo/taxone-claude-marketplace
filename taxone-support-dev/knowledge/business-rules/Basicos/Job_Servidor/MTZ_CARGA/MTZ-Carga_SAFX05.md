# MTZ-Carga_SAFX05

- **Fonte:** MTZ-Carga_SAFX05.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 30 KB

---

__         __

# Módulo Job Servidor – Carga SAFX05 \(Arquivo de Contas a Pagar\)

                      Localização: Menu Básicos, Módulo: Job Servidor, item Carga 🡪 Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

OS4579

Elenilson Coutinho

Alteração no tamanho do campo NUM\_LANCAMENTO 

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de carga para que seja considerado o novo campo:

Tabela: SAFX05

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN02__

__Campo NUM\_LANCAMENTO__

Alterar a rotina de carga para que seja considerado o novo campo:

Tabela: SAFX05

Item: 27

Nome do Campo: Número do Lançamento

Tipo: A

Tamanho: 040

Obrigatório: Não

Chave: Não

Comentário: Número ou código do lançamento contábil, correspondente ao cadastramento inicial do título\. Atende ao Ato Cotepe nr 70/05 \- Registro Z030\.

__OS4579__

