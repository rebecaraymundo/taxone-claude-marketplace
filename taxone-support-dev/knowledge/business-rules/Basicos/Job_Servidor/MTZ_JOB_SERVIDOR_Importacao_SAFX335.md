# MTZ_JOB_SERVIDOR_Importacao_SAFX335

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX335.docx
- **Modificado:** 2025-11-05
- **Tamanho:** 83 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS651949

Robinson Santana

Criação da tabela para importação da SAFX335\.

MFS\-659355

Alessandra Navatta

Atualização das informações de chave e obrigatoriedade dos campos, conforme indicado abaixo:

Alterações Realizadas:

Série: Não obrigatório

Indicador do Produto, Produto, Item Nota Fiscal: Obrigatórios

Subsérie, Indicador do Produto, Produto: Chave da tabela

MFS\-674150

Alessandra Navatta

Inclusão do campo 14 – Item Nota Fiscal, na chave da tabela

Inclusão de mensagens de crítica na importação \(RN01, RN02, RN03, RN04, RN05, RN06, RN07, RN08, RN09, RN10, RN11,RN12, RN13,RN14, RN15,RN16, RN17,RN19, RN20, RN22, RN23, RN26 e RN27\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

PK

OBRIG

ITEM

DESCRIÇÃO

CAMPO

TAMANHO

TIPO

X

\(\*\)

1

Código da Empresa

COD\_EMPRESA

003

A

X

\(\*\)

2

Código do Estabelecimento

COD\_ESTAB

006

A

X

\(\*\)

3

Data da Escrita Fiscal

DATA\_FISCAL

008

N

X

\(\*\)

4

Movimento Entrada/Saída

MOVTO\_E\_S

001

A

X

\(\*\)

5

Normal ou Devolução

NORM\_DEV

001

A

X

\(\*\)

6

Tipo do Documento

COD\_DOCTO

005

A

X

\(\*\)

7

Indicador da Pessoa Física/Jurídica

IND\_FIS\_JUR

001

A

X

\(\*\)

8

Código do Destinatário/Emitente

COD\_FIS\_JUR

014

A

X

\(\*\)

9

Número do Documento Fiscal

NUM\_DOCFIS

012

A

X

10

Série do Documento Fiscal

SERIE\_DOCFIS

003

A

 X

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

002

A

X 

\(\*\)

12

Indicador do Produto

IND\_PRODUTO

001

A

X 

\(\*\)

13

Produto

COD\_PRODUTO

060

A

 X

\(\*\)

14

Item Nota Fiscal

NUM\_ITEM

005

N

 

15

Código Fiscal

COD\_CFO

004

A

 

16

Natureza de Operação

COD\_NATUREZA\_OP

003

A

 

17

Código NBM

COD\_NBM

010

A

 

18

Preço do Item

VLR\_ITEM

015V002

N

 

19

Código Situação Tributária “A”

COD\_SITUACAO\_A

001

A

 

20

Código Situação Tributária “B”

COD\_SITUACAO\_B

002

A

 

21

Valor do estorno aplicado no item

VLR\_EST\_ITEM

015V002

N

\(\*\)

22

Alíquota do Crédito Outorgado

VLR\_ALIQ\_CRE\_OUTORG

003V004

N

\(\*\)

23

Valor Bruto \- Crédito Outorgado

VLR\_BRUTO\_CRE\_OUTORG

015V002

N

 

24

\(%\) do estorno aplicado no valor do item

PRC\_ESTORNO

003V004

N

 

25

Valor do estorno aplicado no item

VLR\_ESTORNO\_OUTORG\_ITEM

015V002

N

\(\*\)

26

Valor líquido crédito outorgado Fichas 6

VLR\_LIQUIDO\_CRE\_OUTORG

015V002

N

 

27

Observação

OBSERVACAO

100

A

MFS\-651949

MFS\-659355

MFS\-674150

RN01

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

*Exibir a mensagem <<90001>>*

MFS\-651949

MFS\-674150

RN02

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

Quando não preenchido, o registro não será importado\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

*Exibir a mensagem <<90002>>*

MFS\-651949

MFS\-674150

RN03

__Campo Data da Escrita Fiscal__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\. 

O formato deve ser informado no padrão AAAAMMDD\.

Quando não preenchida, ou data inválida, o registro não será importado\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens << 90131\-90209\-90386>>

MFS\-651949

MFS\-674150

RN04

__Movimento Entrada/Saída__

Campo de preenchimento obrigatório\.

Informar o Movimento Entrada/Saída, de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário; 

4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagem <<90129>>

MFS\-651949

MFS\-674150

RN05

__Normal ou Devolução__

Campo de preenchimento obrigatório\.

Informar o motivo da Entrada / Saída, de acordo com:

1 \- Normal;

2 \- Devolução \(Quando se tratar de Devolução de Mercadorias\- Produtos, Insumos, Materiais Uso/Consumo, Ativo, etc\., previstos em legislação\)\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagem <<90130>>

MFS\-651949 MFS\-674150

RN06

__Tipo do Documento__

Campo de preenchimento obrigatório\.

Informar o Tipo de Documento de acordo com a Tabela de Tipo de Documentos \(SAFX2005\)\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens <<90119\-90125\-90470>>

MFS\-651949 MFS\-674150

RN07

__Indicador da Pessoa Física/Jurídica__

Campo de preenchimento obrigatório\.

Informar o Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir a mensagem << 90088>>

MFS\-651949 MFS\-674150

RN08

__Código do Destinatário/Emitente__

Campo de preenchimento obrigatório\.

Informar o Código/Destinatário/Emitente/ Remetente\. Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. 

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens << 90089\-90087\-90124>>

MFS\-651949 MFS\-674150

RN09

__Número do Documento Fiscal__

Campo de preenchimento obrigatório\.

Informar o Número do Documento Fiscal\. 

O Número do Documento Fiscal deve ter tamanho de 6 \(seis\) dígitos, que podem ser alinhados a esquerda ou a direita, porém com os 6 \(seis\) dígitos completos\. 

Para o Setor de Telecomunicações já estão previstos Números com 9 \(nove\) Dígitos, que também devem ser alinhados a esquerda ou a direita, uma vez que o MasterSAF define este campo com 12 \(doze\) dígitos\. 

As instruções do Convênio ICMS No 57/95 determina que números de Documentos Fiscais com Números acima de 6 \(seis\) dígitos, sejam truncados nos dígitos mais significativos\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir a mensagem << 90112>>

MFS\-651949 MFS\-674150

RN10

__Série do Documento Fiscal__

Campo de preenchimento __não__ obrigatório\.

Informar a Série do Documento Fiscal\. 

A ausência deste dado deve ser representada com espaços ou nulo\. Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “CMR”\. 

Com as alterações introduzidas na Legislação os Campos de Séries para ECF devem conter a informação “ECF”, a Partir do Convênio ICMS No 50/00 \(15/09/00\)\.

Quando se Tratar da Escrituração dos Mapas Resumos de Telecomunicações, Energia Elétrica e Gás Canalizado os campos devem vir Nulos, a não ser que haja uma AIDF que contemple este resumo como Uma Obrigação Acessória, tal como os Resumos Diários de ECF\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir a mensagem << 90504>>

MFS\-651949

MFS\-659355

MFS\-674150

RN11

__Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Informar a Subsérie do Documento Fiscal\. 

A ausência deste dado deve ser representada com espaços ou nulo\. Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “CMR”\. 

Com as alterações introduzidas na Legislação os Campos de Séries para ECF devem conter a informação “ECF”, a Partir do Convênio ICMS No 50/00 \(15/09/00\)\. Quando se Tratar da Escrituração dos Mapas Resumos de Telecomunicações, Energia Elétrica e Gás Canalizado os campos devem vir Nulos, a não ser que haja uma AIDF que contemple este resumo como Uma Obrigação Acessória, tal como os Resumos Diários de ECF\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir a mensagem << 90505>>

MFS\-651949

MFS\-674150

RN12

__Indicador do Produto__

Campo de preenchimento obrigatório\.

Identificadores:

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagem << 90035>>

MFS\-651949

MFS\-659355

MFS\-674150

RN13

__Produto__

Campo de preenchimento obrigatório\.

Informar o Código do Produto/Mercadoria, de acordo com as solicitações da dos Convênios ICMS, RIPI e IN SRF, devidamente registradas na Tabela de Produto \(SAFX2013\)\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagens << 90033\-90034\-90032>>

MFS\-651949

MFS\-659355

MFS\-674150

RN14

__Item Nota Fiscal__

Campo de preenchimento obrigatório\.

Informar o número do item da Nota Fiscal\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens << 93663 – 93667>>

MFS\-651949 MFS\-659355

MFS\-674150

RN15

__Código Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Código Fiscal de Operação e Prestação, de acordo com a Tabela de Códigos Fiscais \(SAFX2012\)\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir a mensagem << 90029>>

MFS\-651949

MFS\-674150

RN16

__Natureza de Operação__

Campo de preenchimento __*não*__ obrigatório\.

Os “Códigos da Natureza de Operações” devem estar registrados na Tabela de Natureza de Operações \(SAFX2006\)\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens <<90041\-90044>>

MFS\-651949

MFS\-674150

RN17

__Código NBM__

Campo de preenchimento __*não*__ obrigatório\.

Código de Classificação Fiscal de Produtos relativo ao IPI\. Deve estar registrada na Tabela de Classificação Fiscal \(SAFX2043\)\. 

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagem << 90163>>

MFS\-651949

MFS\-674150

RN18

__Preço do Item__

Campo de preenchimento __*não*__ obrigatório\.

Informar o preço total do item

Os valores devem ser apresentados sem pontuação para inteiros decimais\.

MFS\-651949

RN19

__Código Situação Tributária “A”__

Campo de preenchimento __*não*__ obrigatório\.

Informar o Código da Situação Tributária Estadual "A" \(CST – ICMS \- Origem da Mercadoria\) – TACES03\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagens << 90397\-90516>>

MFS\-651949

MFS\-674150

RN20

__Código Situação Tributária “B”__

Campo de preenchimento __*não*__ obrigatório\.

Informar o Código da Situação Tributária Estadual "B", \(CST – ICMS \- Tributação pelo ICMS\) \- TACES04\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir mensagens << 90398\-90517>>

MFS\-651949

MFS\-674150

RN21

__Valor do estorno aplicado no item__

Campo de preenchimento __*não*__ obrigatório\.

Informar o valor de estorno aplicado no valor do item\.

Os valores devem ser apresentados sem pontuação para inteiros decimais\.

MFS\-651949

RN22

__Alíquota do Crédito Outorgado__

Campo de preenchimento obrigatório\.

Alíquota correspondente ao Crédito Outorgado\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens <<93664 \- 93668>>         


MFS\-651949

MFS\-674150

RN23

__Valor Bruto \- Crédito Outorgado__

Campo de preenchimento obrigatório\.

Informar o valor bruto do crédito outorgado\.

Os valores devem ser apresentados sem pontuação para inteiros decimais\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens <<93665 \- 93669>>  

MFS\-651949

MFS\-674150

RN24

__\(%\) do estorno aplicado no valor do item__

Campo de preenchimento __*não*__ obrigatório\.

Informar o percentual de estorno aplicado no valor do item\.

MFS\-651949

RN25

__Valor do estorno aplicado no item__

Campo de preenchimento __*não*__ obrigatório\.

Valor estorno aplicado ao item do credito outorgado da cat 55

Os valores devem ser apresentados sem pontuação para inteiros decimais\.

MFS\-651949

RN26

__Valor líquido crédito outorgado Fichas 6__

Campo de preenchimento obrigatório\.

Informar o valor líquido do crédito outorgado\.

Os valores devem ser apresentados sem pontuação para inteiros decimais\.

__*\[ALTERAÇÃO MFS\-674150\] *__*– Inclusão de mensagem:*

Exibir as mensagens <<93666 \- 93670>>  

MFS\-651949

MFS\-674150

RN27

__Observação__

Campo de preenchimento __*não*__ obrigatório\.

Informar observações a serem refletidas no meio magnético\.

MFS\-651949

MFS\-674150

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

