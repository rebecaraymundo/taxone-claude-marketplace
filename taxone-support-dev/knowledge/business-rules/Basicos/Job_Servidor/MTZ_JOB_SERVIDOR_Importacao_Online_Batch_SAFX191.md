# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX191

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX191.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 65 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH1749\_2017

\(MFS\-9515\)

Julyana Perrucini

Alteração do campo 10\-Valor total dos Itens para não obrigatório\.

MFS29621

Andréa Rocha

Alterar a regra do campo Modelo de documento

MFS33637

Andréa Rocha

Inclusão do modelo 66 para o campo Modelo de documento

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX191 – Complemento de Fornecimento de Energia Elétrica, Água Canalizada e Gás, que deve ser criada com a seguinte estrutura:

__\[ALTERADA \- CH1749\_2017 \(MFS\-9515\)\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Valor total dos Itens

N

015V002

S N

S

 

CH1749\_2017

\(MFS\-9515\)

RN02

__Valor total dos Itens__

__\[ALTERADA \- CH1749\_2017 \(MFS\-9515\)\]__

Campo de preenchimento não obrigatório\.

*Observação: *O campo passa a ser não obrigatório a partir da MFS\-9515, e quando não for informado na importação, será preenchido com zero, já que não pode ficar nulo por ser campo chave\.

CH1749\_2017

\(MFS\-9515\)

RN03

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

