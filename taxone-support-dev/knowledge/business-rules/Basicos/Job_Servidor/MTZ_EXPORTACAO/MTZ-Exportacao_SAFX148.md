# MTZ-Exportacao_SAFX148

- **Fonte:** MTZ-Exportacao_SAFX148.docx
- **Modificado:** 2024-04-17
- **Tamanho:** 29 KB

---

__         __

# Módulo Job Servidor – Exportação SAFX148 \(Bens do Ativo Imobilizado Com Base nos Encargos de Depreciação e no valor de aquisição\)

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

MFS\-626368

Alessandra Cristina Navatta

Inclusão da regra do campo Número da Parcela do CREDPIS \(este campo não foi criado por esta demanda\), apenas foi documentado \(reversa – RN02\)

Inclusão dos campos Data da Baixa e Indicador do Motivo da Baixa na importação da SAFX148 \(RN03 e RN04\)

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX148

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN02__

__Campo Número da Parcela do CREDPIS__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX148

Item: 30

Nome do Campo: Número da Parcela do CREDPIS

Nome da tabela: NUM\_PARC\_CREDPIS

Tipo: N

Tamanho: 03

Campo Não Obrigatório

Comentário: Informar o número da parcela de apropriação do crédito de CREDPIS\.

__Atenção: O campo de item 30, não foi criado nesta demanda, foi apenas documentado\.__

MFS\-626368

__RN03__

__Campo Data da Baixa__

Alterar a rotina de carga para que seja considerado o novo campo:

Tabela: SAFX148

Item: 30

Nome do Campo: Data da Baixa

Nome da tabela: DATA\_BAIXA

Tipo: N

Tamanho: 08

Campo Não Obrigatório

Comentário: Data da Baixa do bem, referente aos tributos PIS/PASEP e COFINS\.

MFS\-626368

__RN04__

__Campo Indicador do Motivo da Baixa__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX148

Item: 31

Nome do Campo: Indicador do Motivo da Baixa

Nome da tabela: IND\_MOTIVO\_BAIXA

Tipo: A

Tamanho: 01

Campo Não Obrigatório

Comentário: Indicador do Motivo da Baixa do bem, referente aos tributos PIS/PASEP e COFINS\. 

Opções válidas: 

1 \- Venda

2 \- Obsolescência ou sucateamento

3 \- Sinistros;

4 \- Doação;

6 \- Outros;

7 – Automática

MFS\-626368

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

