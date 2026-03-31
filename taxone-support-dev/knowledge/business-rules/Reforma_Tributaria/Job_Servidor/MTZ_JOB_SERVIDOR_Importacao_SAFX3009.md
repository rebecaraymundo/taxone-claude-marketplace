# MTZ_JOB_SERVIDOR_Importacao_SAFX3009

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX3009.docx
- **Modificado:** 2025-11-05
- **Tamanho:** 77 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS\-848597

Alessandra Cristina Navatta

Definição das regras de Carga, importação \(Online e Batch\) e Exportação da SAFX3009 \(em atendimento à Reforma Tributária\)\.

MFS\-848597 \(Avaliação MFS\-862496/MFS\-890529\)

Alessandra Cristina Navatta

Inclusão \(9 campos\) – atendimento a NT003 e NT004 de NFS\-e\.

Atenção\! As inclusões e alterações, serão contempladas no pacote da MFS\-848597, uma vez que o desenvolvimento ainda não foi iniciado\.

MFS\-951840

Alessandra Cristina Navatta

Alteração nas regras dos campos de cClass\(RN08 e RN10\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo na tabela SAFX3009:

DESCRIÇÃO

TIPO

TAMANHO

OBRIGATORIEDADE

CHAVE

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data da Escrita Fiscal

N

008

SIM

SIM

Movimento Entrada/Saída

A

001

SIM

SIM

Normal ou Devolução

A

001

SIM

SIM

Tipo do Documento

A

005

SIM

SIM

Indicador da Pessoa Física/Jurídica

A

001

SIM

SIM

Código do Destinatário/Emitente

A

014

SIM

SIM

Número do Documento Fiscal

A

012

SIM

SIM

Série do Documento Fiscal

A

003

NÃO

SIM

Subsérie do Documento Fiscal

A

002

NÃO

SIM

Código do Serviço

A

004

SIM

SIM

Item Documento Fiscal

N

005

SIM

SIM

Código do Município de consumo, fato gerador do IBS / CBS

N

007

NÃO

NÃO

Código de Situação Tributária do Imposto Seletivo

A

003

NÃO

NÃO

Código de Classificação Tributária do Imposto Seletivo

A

006

NÃO

NÃO

Valor da Base de Cálculo do Imposto Seletivo

N

015V002

NÃO

NÃO

Alíquota do Imposto Seletivo 

N

003V004

NÃO

NÃO

Alíquota específica por unidade de medida apropriada do Imposto Seletivo

N

003V004

NÃO

NÃO

Valor do Imposto Seletivo

N

015V002

NÃO

NÃO

Unidade de Medida Tributável do Imposto Seletivo

A

008

NÃO

NÃO

Quantidade Tributável do Imposto Seletivo

N

011V004

NÃO

NÃO

Código de Situação Tributária do IBS e CBS

A

003

NÃO

NÃO

Código de Classificação Tributária do IBS e CBS

A

006

NÃO

NÃO

Base de cálculo do IBS e CBS

N

015V002

NÃO

NÃO

Valor monetário \-Documento Referenciado

N

015V002

NÃO

NÃO

Alíquota do IBS de competência dos Municípios

N

003V004

NÃO

NÃO

Valor do IBS de competência do Município

N

015V002

NÃO

NÃO

Percentual do diferimento do IBS de competência do Município

N

003V004

NÃO

NÃO

Valor do Diferimento do IBS de competência do Município

N

015V002

NÃO

NÃO

Valor da na operação do IBS de competência do Município

N

015V002

NÃO

NÃO

Valor do tributo devolvido do IBS de competência do Município

N

015V002

NÃO

NÃO

Percentual da redução de alíquota do IBS de competência do Município

N

003V004

NÃO

NÃO

Aliquota Efetiva do IBS de competência dos Municípios que será aplicada a Base de Cálculo

N

003V004

NÃO

NÃO

Alíquota da CBS

N

003V004

NÃO

NÃO

Valor da CBS

N

015V002

NÃO

NÃO

Valor da CBS Bruto na operação da CBS

N

015V002

NÃO

NÃO

Valor do tributo devolvido da CBS

N

015V002

NÃO

NÃO

Percentual da redução de alíquota da CBS

N

003V004

NÃO

NÃO

Alíquota Efetiva da CBS que será aplicada a Base de Cálculo

N

003V004

NÃO

NÃO

Código de Situação Tributária do IBS e CBS \- tributação regular

A

003

NÃO

NÃO

Código de Classificação Tributária do IBS e CBS \- tributação regular

A

006

NÃO

NÃO

Valor da alíquota do IBS do Município \- tributação regular

N

003V004

NÃO

NÃO

Valor do Tributo do IBS do Município \- tributação regular

N

015V002

NÃO

NÃO

Valor da alíquota da CBS \- tributação regular

N

003V004

NÃO

NÃO

Valor do Tributo da CBS \- tributação regular

N

015V002

NÃO

NÃO

Código de Classificação do Crédito Presumido do IBS

A

003

NÃO

NÃO

Percentual do Crédito Presumido do IBS

N

003V004

NÃO

NÃO

Alíquota do Crédito Presumido do IBS

N

003V004

NÃO

NÃO

Valor do Crédito Presumido do IBS

N

015V002

NÃO

NÃO

Valor do Crédito Presumido em condição suspensiva do IBS\.

N

015V002

NÃO

NÃO

Código de Classificação do Crédito Presumido da CBS

A

003

NÃO

NÃO

Percentual do Crédito Presumido da CBS

N

003V004

NÃO

NÃO

Alíquota do Crédito Presumido da CBS

N

003V004

NÃO

NÃO

Valor do Crédito Presumido da CBS

N

015V002

NÃO

NÃO

Valor do Crédito Presumido em condição suspensiva da CBS\.

N

015V002

NÃO

NÃO

Alíquota do IBS de competência do Estado \- Compras governamentais

N

003V004

NÃO

NÃO

Valor do Tributo do IBS da UF calculado \- Compras governamentais

N

015V002

NÃO

NÃO

Alíquota do IBS de competência do Município \- Compras governamentais

N

003V004

NÃO

NÃO

Valor do Tributo do IBS do Município calculado \- Compras governamentais

N

015V002

NÃO

NÃO

Alíquota da CBS \- Compras governamentais

N

003V004

NÃO

NÃO

Valor do Tributo da CBS calculado \- Compras governamentais

N

015V002

NÃO

NÃO

Valor Total do Item da Nota

N

015V002

NÃO

NÃO

Número do item do documento referenciado\.

N

003

NÃO

NÃO

MFS\-848597

Avaliação \(MFS\-862496/MFS\-890529\)

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX09, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem: <<913276>> “SAFX09 correspondente a SAFX3009 não localizada”\.

MFS\-848597

RN03

__Campo Código do Município de consumo, fato gerador do IBS / CBS__

Recuperar o código do município da SAFX2097\.

O código deve estar previamente cadastrado na SAFX2097\- Tabela de municípios\. Caso não esteja cadastrado, exibir a mensagem: <<913274>> “Codigo do Municipio de consumo, fato Gerador do IBS/CBS, deve estar previamente cadastrado na tabela de Municipios do ISS \(X2097\_MUNIC\_ISS\)\.”

MFS\-848597

RN04

__Campo Código de Situação Tributária do Imposto Seletivo__

__A definir\.__

MFS\-848597

RN05

__Campo Código de Classificação Tributária do Imposto Seletivo__

__A definir\.__

MFS\-848597

RN06

__Campo Unidade de Medida Tributável do Imposto Seletivo__

Considerar a unidade de medida padrão da SAFX2017 \(campo 01 \- COD\_UND\_PADRAO\)\.

O código deve estar previamente cadastrado na SAFX2017 \- Tabela de Unidade Padrão\. Caso não esteja cadastrado, exibir a mensagem: <<913273>> “Unidade de Medida Tributável do Imposto Seletivo, deve estar previamente cadastrada na SAFX2017 \- Tabela de Unidade Padrão\.”

MFS\-848597

RN07

__Campo Código de Situação Tributária do IBS e CBS__

O código deve estar previamente cadastrado na TACES115\- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem: <<913267>> “Código de Situação Tributária do IBS e CBS, deve estar previamente cadastrada na TACES115 \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.”

MFS\-848597

RN08

__Campo Código de Classificação Tributária do IBS e CBS__

O código deve estar cadastrado na taces116 \-Tabela de Classificação Tributária do IBS e da CST \- Reforma Tributária, caso não esteja cadastrado, exibir a mensagem:<< 913268>> taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913310>

MFS\-848597

MFS\-951840

RN09

__Campo Código de Situação Tributária do IBS e CBS\- Tributação Regular__

O código deve estar previamente cadastrado na TACES115\- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem: <<913269>> “Código de Situação Tributária do IBS e CBS– Tributação Regular, deve estar previamente cadastrada na TACES115 \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.”

MFS\-848597

RN10

__Campo Código de Classificação Tributária do IBS e CBS – Tributação Regular__

O código deve estar cadastrado na taces116 \-Tabela de Classificação Tributária do IBS e da CST \- Reforma Tributária, caso não esteja cadastrado, exibir a mensagem:<< 913270>> estar cadastrado na taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913311>

MFS\-848597

MFS\-951840

RN11

__Campo Código de Classificação do Crédito Presumido do IBS__

O código deve estar previamente cadastrado na tabela TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem: <<913271>> “Código de Classificação do Crédito Presumido do IBS, deve estar previamente cadastrada na TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\.”

MFS\-848597

RN12

__Campo Código de Classificação do Crédito Presumido da CBS__

O código deve estar previamente cadastrado na tabela TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem<<913272>>: “Código de Classificação do Crédito Presumido da CBS, deve estar previamente cadastrada na TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\.”

MFS\-848597

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

