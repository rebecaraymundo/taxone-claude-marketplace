# MTZ-DW-Manutencao_SAFX332

- **Fonte:** MTZ-DW-Manutencao_SAFX332.docx
- **Modificado:** 2024-07-29
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Módulo DW

Tabela de Informações de Ressarcimento e Valores Alterados nos Processos Referenciados em Nota Fiscal Eletrônica

__Localização DW__: Menu Básicos, módulo DW, menu Manutenção à Documento Fiscal à Doc\. Fiscal de Mercadoria

__Localização Taxone__: Menu Básicos, módulo DW, menu Manutenção à Novo Documento Fiscal à Doc\. Fiscal de Mercadoria e Serviço

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS652072

Liliane Videira Assaf

Criação da SAFX254

24/07/2024

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Tabela SAFX332 \- Informações de Ressarcimento e Valores Alterados nos Processos Referenciados em Nota Fiscal Eletrônica, associada a SAFX08

Estrutura da tabela: Consultar o Manual Layout\.

Informações gravadas na tabela: __X332\_PROC\_RESSARC\_NFE__

O objetivo dessa tabela é armazenar valores do item do documento fiscal alterados por processo administrativo ou judicial, assim como informações de ressarcimento\. Tais informações pertencem a [NFCom \(Nota Fiscal Fatura Eletrônica de Serviços de Comunicação\)](https://ndd.tech/blog/compliance-fiscal/tire-suas-principais-duvidas-sobre-a-nfcom/) cujo leiaute e regras estão definidos no MOC da NFCOM publicado no Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica \- SVRS\. \(https://dfe\-portal\.svrs\.rs\.gov\.br/NFCOM/ConsultaSchema\)\.\. 

 

# <a id="_Toc451260496"></a>Layout da Tela

__Título da tela: __Ressarcimento/Valores Alterados por Processos NFe

Campos distribuídos nos quadros: 

\- Valores Alterados por Processos – NFCom

\- Ressarcimento em Processos – NFCom

__Valores Alterados por Processos – NFCom:__

Valor Unitário Item: \[              ,00000000\]

Qtde Faturada:       \[                      ,0000\]

Valor Total Item:     \[              ,00000000\]

Valor Desconto:      \[                         ,00\] 

Outras Despesas:   \[                         ,00\]

Valor FCP:              \[                         ,00\]

Devolução Valor do item  \[ X \]

BC ICMS:               \[                         ,00\]

Alíq\. ICMS:             \[                     ,0000\]

Valor ICMS:            \[                         ,00\]

Valor PIS:               \[                         ,00\]

Valor COFINS:       \[                         ,00\]

__Ressarcimento em Processos – NFCom:__

Tipo de Ressarcimento: \[                  \\/\]

Data Referência:            \[dd/mm/aaaa\]

Número de Processo:    \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Número de Protocolo:    \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Observações Processo: \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Informações Adicionais do Produto: \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

__Regra Geral Botões:__

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__FECHA – __Permite sair da tela\.

__Regra Geral: __

- A tabela X332\_PROC\_RESSARC\_NFE é filha da X08\_ITENS\_MERC, com relação 1:1\. Ou seja, só é permitido gravar um registro na X332\_PROC\_RESSARC\_NFE para o item de mercadoria na existente na X08\_ITENS\_MERC\.\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Valor Unitário Item

Alfanumérico

N

S

__Formato: ,00000000__

Campo texto para digitação de número com 13 inteiros e 8 decimais\.

__MFS652072__

Qtde Faturada

Numérico

N

S

__Formato: ,0000__

Campo texto para digitação de número com 11 inteiros e 4 decimais\.

__MFS652072__

Valor Total Item

Numérico

N

S

__Formato: ,00000000__

Campo texto para digitação de número com 13 inteiros e 8 decimais\.

__MFS652072__

Valor Desconto

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Outras Despesas

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Valor FCP\.

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Devolução Valor do item

Alfanumérico

N

S

__Check\-box__

Domínio do campo: 

1 – Devolução do valor do item\.

Se o check\-box for marcado, o campo deve ser gravado com ‘1’\.

Se desmarcado, o campo deve ficar sem preenchimento\.

__MFS652072__

BC ICMS

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Alíq\. ICMS

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 3 inteiros e 4 decimais\.

__MFS652072__

Valor ICMS

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Valor PIS

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Valor COFINS

Numérico

N

S

__Formato: ,00__

Campo texto para digitação de número com 15 inteiros e 2 decimais\.

__MFS652072__

Tipo de Ressarcimento

Alfanumérico

N

S

__Lista__

Domínio do campo:

1 \- Cobrança Indevida

2 – Interrupção

99 \- Outros\.

A lista deve ser composta pelos itens acima mais uma opção em branco\.

O campo será gravado na base com uma das opções acima relacionadas \(‘1’, ‘2’, ‘99’\) ou ficará sem preenchimento, quando escolhida a opção em branco\.

__MFS652072__

Data Referência

Numérico

N

S

__DD/MM/AAAA__

Campo habilitado para preenchimento de uma data\.

__MFS652072__

Número de Processo

Alfanumérico

N

S

Campo texto para livre digitação\.

__MFS652072__

Número de Protocolo 

Alfanumérico

N

S

Campo texto para livre digitação\.

__MFS652072__

Observações Processo

Alfanumérico

N

S

Campo texto para livre digitação\.

__MFS652072__

Informações Adicionais do Produto

Alfanumérico

N

S

Campo texto para livre digitação\.

__MFS652072__

       = = = = = =

