# MTZ_JOB_SERVIDOR_Importacao_SAFX3007

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX3007.docx
- **Modificado:** 2026-03-24
- **Tamanho:** 100 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS\-848597

Alessandra Cristina Navatta

Definição das regras de Carga, importação \(Online e Batch\) e Exportação da SAFX3007 \(em atendimento à Reforma Tributária\)\.

MFS\-848597 \(Avaliação MFS\-862496/MFS\-890529\)

Alessandra Cristina Navatta

Inclusão \(16 campos\), Alteração \(4 campos\) – atendimento a NT003 e NT004 de NFS\-e\.

Atenção\! As inclusões e alterações, serão contempladas no pacote da MFS\-848597, uma vez que o desenvolvimento ainda não foi iniciado\.

MFS\-951840

Alessandra Cristina Navatta

Alteração nas regras dos campos de cClass\(RN23 e RN25\)

MFS\-1011288

Alessandra Cristina Navatta

Remover a obrigatoriedade do campo Tipo de Ente Governamental \(RN18\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo na tabela SAFX3007:

__Campo__

__Tipo__

__Tam\.__

__Obrigatoriedade__

__Chave__

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

Indicador Pessoa Física/Jurídica

A

001

SIM

SIM

Código/Destinatário/Emitente/ Remetente

A

014

SIM

SIM

Número do Documento Fiscal/ Número do Mapa Resumo de Caixa

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

Código do Município de consumo, fato gerador do IBS / CBS

N

007

 NÃO

NÃO

Tipo de Chave DF\-e

N

001

 SIM

NÃO

Descrição de chave DF\-e

A

255

 NÃO

NÃO

Finalidade da Emissão \(NF\-e\)

N

001

NÃO

NÃO

Finalidade da Emissão \(NFS\-e\)

N

001

NÃO

NÃO

Tipo de Nota de Débito

A

002

 NÃO

NÃO

Tipo de Nota de Crédito 

A

002

 NÃO

NÃO

Indica operação com Consumidor final 

N

001

NÃO

NÃO

Indica operação de uso e consumo pessoal

N

001

NÃO

NÃO

Indicador da operação de fornecimento

A

010

NÃO

NÃO

Destinatário dos Serviços

N

001

NÃO

NÃO

Indicador de presença do comprador no estabelecimento comercial no momento da operação

N

001

NÃO

NÃO

Indicador de intermediador/marketplace

N

001

 NÃO

NÃO

Indicador de compra governamental

N

001

 NÃO

NÃO

Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis

N

001

 NÃO

NÃO

Tipo de ente governamental

N

001

 NÃO

NÃO

Percentual de redução de alíquota em compra governamental 

N

003V004

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

Alíquota do IBS de competência das UF

N

003V004

 NÃO

NÃO

Valor do IBS de competência da UF

N

015V002

 NÃO

NÃO

Percentual do diferimento do IBS de competência da UF

N

003V004

 NÃO

NÃO

Valor do Diferimento do IBS de competência da UF

N

015V002

 NÃO

NÃO

Valor do tributo devolvido do IBS de competência da UF

N

015V002

 NÃO

NÃO

Percentual da redução de alíquota do IBS de competência da UF

N

003V004

 NÃO

NÃO

Aliquota Efetiva do IBS de competência das UF que será aplicada a Base de Cálculo

N

003V004

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

Valor da operação do IBS de competência do Município

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

Percentual do diferimento da CBS

N

003V004

 NÃO

NÃO

Valor do Diferimento da CBS

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

Valor da alíquota do IBS da UF \- tributação regular

N

003V004

 NÃO

NÃO

Valor do Tributo do IBS da UF \- tributação regular

N

015V002

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

Alíquota do Crédito Presumido do CBS

N

003V004

 NÃO

NÃO

Valor do Crédito Presumido da CBS

N

015V002

 NÃO

NÃO

Valor do Crédito Presumido em condição suspensiva da CBS

N

015V002

 NÃO

NÃO

Quantidade tributada na monofasia

N

011V004

 NÃO

NÃO

Alíquota ad rem do IBS

N

003V004

 NÃO

NÃO

Alíquota ad rem da CBS

N

003V004

 NÃO

NÃO

Valor do IBS monofásico

N

015V002

 NÃO

NÃO

Valor da CBS monofásica

N

015V002

 NÃO

NÃO

Quantidade tributada sujeita à retenção na monofasia do IBS e da CBS

N

011V004

 NÃO

NÃO

Alíquota ad rem do IBS sujeito a retenção

N

003V004

 NÃO

NÃO

Valor do IBS monofásico sujeito a retenção 

N

015V002

 NÃO

NÃO

Alíquota ad rem da CBS sujeito a retenção

N

003V004

 NÃO

NÃO

Valor da CBS monofásico sujeito a retenção 

N

015V002

 NÃO

NÃO

Quantidade tributada retida anteriormente do IBS e da CBS

N

011V004

 NÃO

NÃO

Alíquota ad rem do IBS retido anteriormente

N

003V004

 NÃO

NÃO

Valor do IBS retido anteriormente

N

015V002

 NÃO

NÃO

Alíquota ad rem da CBS retida anteriormente

N

003V004

 NÃO

NÃO

Valor da CBS retida anteriormente

N

015V002

 NÃO

NÃO

Percentual do diferimento do imposto monofásico do IBS

N

003V004

 NÃO

NÃO

Valor do IBS mono diferido\.

N

015V002

 NÃO

NÃO

Percentual do diferimento do imposto monofásico da CBS

N

003V004

 NÃO

NÃO

Valor do CBS Mono diferido

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

Chave de acesso do DF\-e referenciado

N

044

 NÃO

NÃO

Total do imposto seletivo

N

015V002

 NÃO

NÃO

Valor total da BC do IBS e da CBS

N

015V002

 NÃO

NÃO

Valor total do diferimento do IBS de competência da UF

N

015V002

 NÃO

NÃO

Valor total de devolução de tributos do IBS de competência da UF

N

015V002

 NÃO

NÃO

Valor total do IBS de competência da UF

N

015V002

 NÃO

NÃO

Valor total do diferimento do IBS do Município 

N

015V002

 NÃO

NÃO

Valor total de devolução de tributos do IBS do Município 

N

015V002

 NÃO

NÃO

Valor total do IBS do Município 

N

015V002

 NÃO

NÃO

Valor total do IBS

N

015V002

 NÃO

NÃO

Valor total do crédito presumido do IBS

N

015V002

 NÃO

NÃO

Valor total do crédito presumido em condição suspensiva do IBS

N

015V002

 NÃO

NÃO

Valor total do crédito presumido da CBS

N

015V002

 NÃO

NÃO

Valor total do crédito presumido em condição suspensiva da CBS

N

015V002

 NÃO

NÃO

Valor total do diferimento da CBS

N

015V002

 NÃO

NÃO

Valor total de devolução de tributos da CBS

N

015V002

 NÃO

NÃO

Valor total da CBS

N

015V002

 NÃO

NÃO

Total do IBS monofásico

N

015V002

 NÃO

NÃO

Total da CBS monofásica

N

015V002

 NÃO

NÃO

Total do IBS monofásico sujeito a retenção

N

015V002

 NÃO

NÃO

Total da CBS monofásica sujeita a retenção

N

015V002

 NÃO

NÃO

Total do IBS monofásico retido anteriormente

N

015V002

 NÃO

NÃO

Total da CBS monofásica

N

015V002

 NÃO

NÃO

Valor total da nota com IBS / CBS / IS 

N

015V002

 NÃO

NÃO

MFS\-848597

Avaliação \(MFS\-862496/MFS\-890529\)

MFS\-1011288

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX07, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem <<913258>>: “SAFX07 correspondente a SAFX3007 não localizada\.”

MFS\-848597

RN03

__Campo Código do Município de consumo, fato gerador do IBS / CBS__

Recuperar o código do município da SAFX2097\.

O código deve estar previamente cadastrado na SAFX2097\- Tabela de municípios\. Caso não esteja cadastrado, exibir a mensagem: <<913274>> “Codigo do Municipio de consumo, fato Gerador do IBS/CBS, deve estar previamente cadastrado na tabela de Municipios do ISS \(X2097\_MUNIC\_ISS\)\.”

MFS\-848597

RN04

__Tipo de Chave DF\-e__

Lista de Valores válidos: 1,2,3,9

Informar o Tipo de chave DF\-e

Lista de Valores válidos:

1\-NFS\-e

2\-NF\-e

3\-CT\-e

9\-Outro

Campo de preenchimento obrigatório, caso, não preenchido, retornar a mensagem <<913277>>: Campo Tipo de Chave DF\-e deve ser preenchido__\.__

Caso seja informado um conteúdo diferente dos que são aceitos, retornar mensagem <<913278>>: “Campo Tipo de chave DF\-e Inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3> ou <9>\.”

RN05

__Descrição de Chave DF\-e__

Este campo é de preenchimento exclusivo e obrigatório, quando Tipo de Chave DF\-e estiver preenchido com <9>

Caso Tipo de Chave DF\-e estiver preenchido com <9> e este campo não for preenchido, retornar a mensagem<<913279>>: “Campo Descrição de Chave DF\-e deve ser preenchido, quando Tipo de Chave DF\-e for preenchido com <9>”\.

Caso Tipo de Chave DF\-e estiver preenchido com informação diferente de <9> e este campo for preenchido, retornar a mensagem <913280>: “Campo Descrição de Chave DF\-e não deve ser preenchido, quando Tipo de Chave DF\-e for preenchido com informação diferente de <9>”\.

Avaliação \(MFS\-862496/MFS\-890529\)

RN06

__Campo Finalidade da Emissão \(NF\-e\)__

Lista de Valores válidos: @,1,2, 3, 4, 5, 6

Informar a finalidade da emissão da NF\-e:

Lista de valores válidos:

@ \(nulo\)

1 \- NFe normal

2 \- NFe complementar

3 \- NFe de ajuste

4 \- Devolução/Retorno

5 \- Nota de crédito

6 \- Nota de débito

Se campo Tipo de chave DF\-e estiver preenchido com 2\-NF\-e e este campo não estiver preenchido, exibir a mensagem <<913259>>: “Campo Finalidade da Emissão \(NFe\) deve ser preenchido, quando Tipo de Chave DF\-e igual a ‘2\-NF\-e’\.”

Caso seja informado um conteúdo diferente dos que são aceitos, retornar mensagem <<913281>>: “Campo Finalidade de Emissão NF\-e Inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3> ou <4> ou <5> ou <6>\.”

MFS\-848597

Avaliação \(MFS\-862496/MFS\-890529\)

RN07

__Indicador da finalidade da emissão de NFS\-e __

Lista de Valores válidos:@,0

Informar a finalidade da emissão da NFS\-e:

Lista de valores válidos:

@ \(nulo\)

0\-NFS\-e regular

Campo de preenchimento obrigatório, quando se tratar de NFS\-e\. Se tipo de chave DFe estiver preenchido com 1\-NFS\-e e o campo estiver sem preenchimento, ou nulo, retornar a mensagem <<913282>>: “Campo Indicador da finalidade da emissão de NFS\-e, deve ser preenchido com 0 – NFS\-e regular\.”

Se tipo de chave DFe estiver preenchido com informação diferente de 1\-NFS\-e e o campo estiver preenchido com informação diferente de nulo, retornar a mensagem <<913283>>: “O campo Indicador da finalidade da emissão de NFS\-e, deve ser preenchido apenas quando tipo de chave DFe igual 1\-NFS\-e\.”

Avaliação \(MFS\-862496/MFS\-890529\)

RN08

__Campo Tipo de Nota de Débito __

Lista de Valores válidos: @, 01,02, 03, 04, 05, 06, 07\.

Informar o tipo de Nota de Débito\.

Lista de valores válidos:

@ \(nulo\)

01 \- Transferência de créditos para Cooperativas;

02 \- Anulação de Crédito por Saídas Imunes/Isentas;

03 \- Débitos de notas fiscais não processadas na apuração;

04 \- Multa e juros;

05 \- Transferência de crédito de sucessão;

06 \- Pagamento antecipado; 

07 \- Perda em estoque

Caso seja informado um conteúdo diferente, retornar mensagem <<913260>>: “Campo Tipo de Nota de Débito Inválido\. Conteúdo do campo deve ser igual a <01> ou <02> ou <03> ou <04> ou <05> ou <06> ou <07>\.”

MFS\-848597

RN09

__Campo Tipo de Nota de Crédito__

Lista de Valores válidos: @, 01,02\.

Informar o tipo de Nota de Crédito\.

Lista de valores válidos:

@ \(nulo\)

01 \- Multa e juros; 

02 \- Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM \(art\. 450, § 1º, LC 214/25\)

Caso seja informado um conteúdo diferente, retornar mensagem <<913261>>: “Campo Tipo de Nota de Crédito Inválido\. Conteúdo do campo deve ser igual a <01> ou <02>\.”

MFS\-848597

RN10

__Campo Indica Operação com Consumidor Final __

Lista de Valores válidos: @, 0,1\.

Informar a indicação da operação com Consumidor final, quando NF\-e\.

Lista de valores válidos:

@ \(nulo\)

0 \- Normal;

1 \- Consumidor final\.

Se campo Tipo de chave DF\-e estiver preenchido com 2\- NF\-e e este campo não estiver preenchido, ou se preenchido, mas, com  um valor inválido retornar mensagem <<913262>>: “Quando campo Tipo de chave DF\-e = ‘2\- NF\-e’ o campo Indica Operação com Consumidor Final,  é de preenchimento obrigatório e deve ser igual a <0> ou <1>\.”

MFS\-848597

RN11

__Campo Operação de uso ou consumo pessoal__

Lista de valores válidos: @, 0, 1

Indica operação de uso ou consumo pessoal, quando NFS\-e

Lista de valores válidos:

@ \(nulo\)

0\-Não

1\-Sim

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo não estiver preenchido, retornar a mensagem <<913284>>: “Campo Indica Operação de uso ou consumo pessoal, deve ser preenchido, quando NFS\-e\.”

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo estiver preenchido e não for um valor válido para NFS\-e, retornar mensagem <<913285>>: “Campo Indica Operação de uso ou consumo pessoal com valor Inválido para NFS\-e\. Conteúdo do campo deve ser igual a <0> ou <1>\.”

Avaliação \(MFS\-862496/MFS\-890529\)

RN12

__Indicador da operação de fornecimento__

Informar o código do indicador da operação de fornecimento, conforme cadastrado na tabela indicador de operação\.

Campo de preenchimento obrigatório e exclusivo, quando se tratar de NFS\-e\. 

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo não estiver preenchido, retornar a mensagem <<913286>>\. “Campo Indicador da operação de fornecimento deve ser preenchido, quando NFS\-e\.”

Se campo Tipo de chave DF\-e estiver preenchido com informação diferente de 1\- NFS\-e e este campo estiver preenchido, retornar a mensagem <<913287>>\. “O campo Indicador da operação de fornecimento deve ser preenchido, apenas quando NFS\-e\.”

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo estiver preenchido, com informação que não está cadastrado na tabela de operação de fornecimento, exibir a mensagem <<913291>>\. “O código do indicador da operação de fornecimento deve estar previamente cadastrado na TACES120 – Tabela de Códigos de Indicadores das Operações de Consumo\.”

Avaliação \(MFS\-862496/MFS\-890529\)

RN13

__Campo Destinatários dos Serviços__

Lista de Valores Válidos:@, 0,1

A respeito do Destinatário dos serviços, lista dos valores válidos:

@ \(nulo\)

0 – o destinatário é o próprio tomador/adquirente identificado na NFS\-e \(tomador=adquirente=destinatário\);

1 – o destinatário não é o próprio adquirente, podendo ser outra pessoa, física ou jurídica \(ou equiparada\), ou um estabelecimento diferente do indicado como tomador \(tomador=adquirente≠destinatário\);

Campo de preenchimento obrigatório, quando se tratar de NFS\-e\.

Campo de preenchimento obrigatório e exclusivo, quando se tratar de NFS\-e\. 

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo não estiver preenchido ou se Tipo de chave DF\-e estiver preenchido com valor diferente de 1\- NFS\-e e este campo estiver preenchido, retornar a mensagem <<913289>>\. “Campo Destinatário dos serviços é de preenchimento obrigatório e exclusivo, quando tipo de chave DF\-e for NFS\-e\.”

Se campo Tipo de chave DF\-e estiver preenchido com 1\- NFS\-e e este campo estiver preenchido e não for um valor válido para NFS\-e, retornar mensagem <<913290>>: “Campo destinatário dos serviços com valor Inválido para NFS\-e\. Conteúdo do campo deve ser igual a <0> ou <1>\.”

Avaliação \(MFS\-862496/MFS\-890529\)

RN14

__Campo Indicador de Presença do Comprador no Estabelecimento Comercial no Momento da Operação__

Lista de Valores válidos: @, 0, 1, 2, 3, 4, 5, 9\.

Informar o indicador de presença do comprador no estabelecimento comercial no momento da operação

Lista de valores válidos: 

@ \(nulo\)

0 \- Não se aplica \(por exemplo, Nota Fiscal complementar ou de ajuste\); 

1 \- Operação presencial;

2 \- Operação não presencial, pela Internet; 

3 \- Operação não presencial, Tele atendimento; 

4 \- NFC\-e em operação com entrega a domicílio; 

5 \- Operação presencial, fora do estabelecimento; 

9 \- Operação não presencial, outros\.

Caso seja informado um conteúdo diferente, retornar mensagem <<913263>>: “Campo Indicador de Presença do Comprador no Estabelecimento Comercial no Momento da Operação Inválido\. Conteúdo do campo deve ser igual a <0> ou <1> ou <2> ou <3> ou <4> ou <5> ou <9>\.”

MFS\-848597

RN15

__Campo Indicador de Intermediador/Marketplace__

Lista de Valores válidos: @,0,1\.

Informar o indicador de intermediador/marketplace\.

Lista de valores válidos:

@ \(nulo\)

0 \- Operação sem intermediador \(em site ou plataforma própria\)

1 \- Operação em site ou plataforma de terceiros \(intermediadores/marketplace\)

Caso seja informado um conteúdo diferente, retornar mensagem <<913264>>: “Campo Indicador de Intermediador/Marketplace Inválido\. Conteúdo do campo deve ser igual a <0> ou <1>\.”

MFS\-848597

RN16

__Campo Indicador de Compra Governamental__

Lista de Valores válidos:@, 0,1\.

Informar o Indicador de Compra Governamental\.

Lista de valores válidos:

@ \(nulo\)

0 \- Não;

1 – Sim

Caso seja informado um conteúdo diferente, retornar mensagem <<913265>>: “Campo Indicador de Compra Governamental Inválido\. Conteúdo do campo deve ser igual a <0> ou <1>\.”

MFS\-848597

RN17

__Campo Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis__

Lista de Valores válidos: @, 1, 2, 3, 4, 5\.

Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis: 

Lista de Valores válidos:

@ \(nulo\)

1 – Fornecimento com pagamento posterior; 

2 \- Recebimento do pagamento com fornecimento já realizado; 

3 – Fornecimento com pagamento já realizado; 

4 – Recebimento do pagamento com fornecimento posterior; 

5 – Fornecimento e recebimento do pagamento concomitantes\.

Caso seja informado um conteúdo diferente, retornar mensagem <<913288>>: “Campo Tipo de Operação Inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3> ou <4> ou <5>\.”

Avaliação \(MFS\-862496/MFS\-890529\)

RN18

__Campo Tipo de Ente Governamental__

Lista de Valores válidos: @, 1, 2, 3, 4\.

Informar o tipo de ente governamental\.

Lista de Valores Válidos:

@ \(nulo\)

1\-União

2\-Estado

3\-Distrito Federal

4\-Município

\[Exclusão MFS\-1011288\] – Exclusão da obrigatoriedade do campo

Campo de preenchimento obrigatório, caso, não preenchido, retornar a mensagem <<913292>>: “Campo Tipo de Ente Governamental deve ser preenchido\.”

Caso seja informado um conteúdo diferente, retornar mensagem <<913266>>: “Campo Tipo de Ente Governamental Inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3> ou <4>\.”

MFS\-848597

Avaliação \(MFS\-862496/MFS\-890529\)

MFS\-1011288

RN19

__Campo Código de Situação Tributária do Imposto Seletivo__

__A definir\.__

MFS\-848597

RN20

__Campo Código de Classificação Tributária do Imposto Seletivo__

__A definir\.__

MFS\-848597

RN21

__Campo Unidade de Medida Tributável do Imposto Seletivo__

Considerar a unidade de medida padrão da SAFX2017 \(campo 01 \- COD\_UND\_PADRAO\)\.

O código deve estar previamente cadastrado na SAFX2017 \- Tabela de Unidade Padrão\. Caso não esteja cadastrado, exibir a mensagem: <<913273>> “Unidade de Medida Tributável do Imposto Seletivo, deve estar previamente cadastrada na SAFX2017 \- Tabela de Unidade Padrão\.”

MFS\-848597

RN22

__Campo Código de Situação Tributária do IBS e CBS__

O código deve estar previamente cadastrado na TACES115\- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem <<913267>>: “Código de Situação Tributária do IBS e CBS, deve estar previamente cadastrada na TACES115 \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.”

MFS\-848597

RN23

__Campo Código de Classificação Tributária do IBS e CBS__

O código deve estar cadastrado na taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913310>>: “Código de Classificação Tributária do IBS e CBS, deve estar previamente cadastrada na TACES117 \- Tabela de Código de Situação Tributária x Classificação Tributária e vinculado ao CST informado\.”

MFS\-848597

MFS\-951840

RN24

__Campo Código de Situação Tributária do IBS e CBS\- Tributação Regular__

O código deve estar previamente cadastrado na TACES115\- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem <<913269>>: “Código de Situação Tributária do IBS e CBS– Tributação Regular, deve estar previamente cadastrada na TACES115 \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.”

MFS\-848597

RN25

__Campo Código de Classificação Tributária do IBS e CBS – Tributação Regular__

O código deve estar cadastrado na taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913311>>: Cod Classificação Tributária do IBS e CBS da Trib Reg, deve estar previamente cadastrada na TACES117 \- Tabela de Código de Situação Tributária x Classificação Tributária e vinculado ao CST informado\.

MFS\-848597

MFS\-951840

RN26

__Campo Código de Classificação do Crédito Presumido do IBS__

O código deve estar previamente cadastrado na tabela TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem: <<913271>> “Código de Classificação do Crédito Presumido do IBS, deve estar previamente cadastrada na TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\.

MFS\-848597

RN27

__Campo Código de Classificação do Crédito Presumido da CBS__

O código deve estar previamente cadastrado na tabela TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\. Caso não esteja cadastrado, exibir a mensagem: <<913272>> “Código de Classificação do Crédito Presumido da CBS, deve estar previamente cadastrada na TACES118 \- Tabela de Código de Crédito Presumido do IBS e do CBS\- Reforma Tributária\.”

MFS\-848597

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

