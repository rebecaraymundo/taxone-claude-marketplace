# MTZ_346_SAFX_RETORNO_GUIAS_PAGTO

- **Fonte:** MTZ_346_SAFX_RETORNO_GUIAS_PAGTO.docx
- **Modificado:** 2026-02-27
- **Tamanho:** 197 KB

---

THOMSON REUTERS

 TAX PAYMENTS –  IMPORTAÇÃO \- SAFX346 \(Retorno das Guias de Pagamentos\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Guia de Pagamento

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 877116

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX346

ADO\-1043049

Millys Lopes

Alterar o campo GRUPO\_IMPOSTO de obrigatório para não obrigatório

ADO\-1043049

Millys Lopes

Alterar o nome descrição do campo TIPO\_PAGTO

__Introdução __

 

A nova SAFX de Retorno será responsável por receber os dados fornecidos pelo sistema OBI \(Tax Payments DOOTAX\), que disponibilizará informações sobre o status das guias e outras informações, como pagamentos realizados, pendentes ou cancelados, por exemplo\.

O sistema OBI irá consumir esses dados, realizar o processamento necessário e enviar as informações, através da nova SAFX de Retorno, o Tax One, onde serão utilizadas posteriormente\.

Para o cliente Raízen, é necessário realizar a inversão do código de empresa no sistema Tax One, garantindo que os dados sejam recebidos corretamente\.

Os campos\-chave: Empresa, Estabelecimento, Período, Código de Arrecadação, Código da Receita, Número do Documento de Origem e Status\. Além disso, sempre que houver alteração no status da guia — como, por exemplo, de "Aguardando Pagamento" para "Guia Paga" — a SAFX deverá receber a atualização correspondente\. Esse Retorno  proporcionará os seguintes benefícios:

- Atualização automática do status das guias no __Relatório de Status__ do sistema Tax One\.
- Registro detalhado e confiável dos valores pagos, retornados pela DOOTAX, para o status de __Guias Pagas__\.
- Disponibilização dos dados necessários para a __geração da Guia Complementar__\.
- Atualização de status para possibilitar __cancelamentos__, quando aplicável\.

 

__ __

__Localização:__ 

__             Módulo: __Básicos > Guias de Pagamentos

__                 Menu:__ Guias de Pagamentos

 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX346 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__ 

 

Procedimentos para a Importação da SAFX346: 

 __A importação da SAFX346 deve atender às seguintes premissas de negócio e comportamentos:__

- Os campos obrigatórios e chaves devem estar devidamente preenchidos\.
- O processo deve identificar e atualizar corretamente o status da guia\.

__Resultado da Importação:__  
Se a importação for realizada com sucesso, os dados serão registrados nas seguintes telas:

- __Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Relatório de Status__
- __Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Guia Complementar__

 

__                 __ 

 

 

Regra Geral para validação 

 

1º \) Consistências Básicas: 

 

- Campos Data inválidos 
- Campos Obrigatórios 
- Campos Numéricos inválidos 
- Campo ID da Guia – Vide regra RN01 
- Campo ID do Título – Vide regra RN02
- Campo CNPJ da Empresa – Vide regra RN03
- Campo Código da Empresa – Vide regra RN04
- Campo Código do Estabelecimento – Vide regra RN05 
- Campo Data da Competência – Vide regra RN08
- Campo Tipo do Pagamento – Vide regra RN09 
- Campo Código de Receita – Vide regra RN10 
- Campo Código de Detalhamento da Receita – Vide regra RN11
	- Campo Tipo do Pagamento – Vide regra RN09 
	- Campo Código de Receita – Vide regra RN10 

 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

 

__Índice__

__Campos DOOTAX__

__Campos Tax One__

__Descrição__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

01

content\.\[\]\.companyCode

COD\_EMPRESA

Código da empresa

A

008 

SIM 

\(\*\) 

02

content\.\[\]\.branchCode

COD\_ESTAB

Código do estabelecimento

A

006 

SIM 

\(\*\) 

03

content\.\[\]\.period

PERIODO

Data Apuração

N

008

SIM

NÃO

04

content\.\[\]\.id

ID\_GUIA

ID da guia

N

038

NÃO

NÃO

05

content\.\[\]\.titleId

ID\_TITULO

ID do Título

N

038

NÃO

NÃO

06

content\.\[\]\.companyCnpj

CNPJ\_EMPRESA

CNPJ da empresa

A

014

NÃO

NÃO

07

content\.\[\]\.iest

INSC\_SUBSTITUTA

Inscrição substituta

C

30

NÃO

NÃO

08

content\.\[\]\.ieType

TIPO\_INSC\_SUBSTITUTA

Tipo de inscrição substituta

C

40

NÃO

NÃO

09

content\.\[\]\.docType

TIPO\_PAGTO

Código de Arrecadação

String

4000

 NÃO

NÃO

10

content\.\[\]\.revenueCode

COD\_RECEITA

Código da receita

N

020 

SIM 

\(\*\) 

11

content\.\[\]\.revenueDetailCode

DET\_RECEITA

Código do detalhe da receita

N

020 

SIM 

\(\*\) 

12

content\.\[\]\.taxName

GRUPO\_IMPOSTO

Nome do imposto

C

030

NÃO 

NÃO

13

content\.\[\]\.state

UF\_FAVORECIDA

UF favorecida

C

002

NÃO 

NÃO

14

content\.\[\]\.cityCode

COD\_DOC

Código da cidade do documento

N

038

NÃO

NÃO

15

content\.\[\]\.docNum

NUM\_DOC\_ORIGEM

Número do documento

N

019

SIM 

NÃO

16

content\.\[\]\.series

SERIE

Série do documento

C

003

NÃO

NÃO

17

content\.\[\]\.accessKey

CHAVE\_NF

Chave NF

N

044

NÃO

NÃO

18

content\.\[\]\.canceled

IND\_CANCELAMENTO

Indicação de cancelamento

Boolean

4000

NÃO

NÃO

19

content\.\[\]\.canceledMessage

INFO\_CANCELAMENTO

Informações sobre o cancelamento

String

4000

NÃO

NÃO

20

content\.\[\]\.statusId

STATUS

Status

N

038

SIM 

NÃO

21

content\.\[\]\.status

DSC\_STATUS

Descrição do status

c

050

SIM

NÃO

22

content\.\[\]\.principalAmount

VLR\_PRINCIPAL

Valor principal do título

N

038

SIM 

NÃO

23

content\.\[\]\.fecpAmount

VLR\_FECP

Valor do FECP

N

015V002

NÃO

NÃO

24

content\.\[\]\.interestAmount

VLR\_JUROS

Valor dos juros

N

015V002

NÃO 

NÃO

25

content\.\[\]\.fineAmount

VLR\_MULTA

Valor da multa

N

015V002

NÃO 

NÃO

26

content\.\[\]\.restatementAmount

VLR\_ATUAL\_MONETARIA

Valor da atualização monetária

N

038

NÃO

NÃO

27

content\.\[\]\.otherAmount

VLR\_OUTROS

Outros valores

N

038

NÃO

NÃO

28

content\.\[\]\.fecpInterestAmount

VLR\_FECP\_JUROS

Valor dos juros FECP

N

015V002

NÃO

NÃO

29

content\.\[\]\.fecpFineAmount

VLR\_MULTA\_FECP

Valor da multa FECP

N

015V002

NÃO

NÃO

30

content\.\[\]\.totalAmount

VLR\_TOTAL

Valor total

N

038

NÃO

NÃO

31

content\.\[\]\.productCode

COD\_PRODUTO

Código do produto

N

005

NÃO

\(\*\)

32

content\.\[\]\.agreement

CONVENIO

Convênio

C

030

NÃO

\(\*\)

33

content\.\[\]\.favoredCnpj

CNPJ\_FAVORECIDO

CNPJ do favorecido

A

014

NÃO

NÃO

34

content\.\[\]\.favoredIe

INSC\_ESTADUAL\_FAVORECIDO

Inscrição estadual favorecido

C

030

NÃO

NÃO

35

content\.\[\]\.favoredCpf

CPF\_FAVORECIDO

CPF do favorecido

A

014

NÃO

NÃO

36

content\.\[\]\.additionalInfo

INFO\_COMPL\_DOCUMENTO

Informações complementares do documento

C

050

NÃO

NÃO

37

content\.\[\]\.error

IND\_ERRO

Indicador de erro

Boolean

038

NÃO

NÃO

38

content\.\[\]\.errorMessage

MENSAGEM\_ERRO

Mensagem de erro

String

4000

NÃO

NÃO

39

content\.\[\]\.dueDate

DATA\_VENCTO

Data vencimento

N

008

NÃO

NÃO

40

content\.\[\]\.originalDueDate

DATA\_VENCTO\_ORIGINAL

Data vencimento original

N

008

NÃO

NÃO

41

content\.\[\]\.barcode

COD\_BARRAS

Código de barras

String

4000

NÃO

NÃO

42

content\.\[\]\.controlNum

NUM\_CONTROLE

Número de controle

String

4000

NÃO

NÃO

43

content\.\[\]\.issueDate

DATA\_SEFAZ

Data da resposta SEFAZ

N

008

NÃO

NÃO

44

content\.\[\]\.paymentId

ID\_PAGTO

ID pagamento

N

038

NÃO

NÃO

45

content\.\[\]\.paymentDate

DATA\_PAGTO

Data pagamento

N

008

NÃO

NÃO

46

content\.\[\]\.authenticationNum

NUM\_AUTENTICACAO

Número da autenticação

String

4000

NÃO

NÃO

47

content\.\[\]\.payerId

ID\_PAGADOR

ID pagador

N

038

NÃO

NÃO

48

content\.\[\]\.payerCnpj

CNPJ\_PAGADOR

CNPJ pagador

A

014

NÃO

NÃO

49

content\.\[\]\.bankCode

COD\_BANCO

Código do banco

N

003

NÃO

NÃO

50

content\.\[\]\.bankBranchNumber

AGENCIA

Agência

N

005

NÃO

NÃO

51

content\.\[\]\.bankBranchVD

DIG\_AGENCIA

Digito agencia

N

001

NÃO

NÃO

52

content\.\[\]\.bankAccountNumber

CONTA\_CORRENTE

Conta corrente

N

015

NÃO

NÃO

53

content\.\[\]\.bankAccountVD

DIG\_CONTA\_CORRENTE

Dígito conta corrente

N

001

NÃO

NÃO

54

content\.\[\]\.metaField

REGRA\_PAGAMENTO

Objeto JSON com customizações das regras de pagamento associadas à guia

Null

\-

NÃO

NÃO

55

content\.\[\]\.pdfBytes

PDF\_GUIA

Array de bytes do PDF, comprimido usando biblioteca de compressão zlib e codificado em Base64

String

\-

NÃO

NÃO

56

content\.\[\]\.camposExtras

CAMPO\_EXTRA

Campos Extras \-Descrição complementar

C

\-

NÃO

NÃO

57

content\.\[\]\.pixQrCode

QR\_CODE\_PIX

Qr code do pix

String

4000

NÃO

NÃO

58

content\.\[\]\.userImportedFile

LOGIN\_USUARIO

Login do usuário que importou o arquivo

String

4000

NÃO

NÃO

59

content\.\[\]\.debitDate

DAT\_DEBITO

Data de débito

N

008

NÃO

NÃO

60

totalElements

TOTAL\_ELEMENTOS

Total de registros na página

N

038

NÃO

NÃO

61

totalPages

TOTAL\_PAGINAS

Total de páginas

N

038

NÃO

NÃO

62

size

TAMANHO

Tamanho máximo da página \(máx\. 100\)

N

038

NÃO

NÃO

63

number

NUMERO

Número da página

N

038

NÃO

NÃO

64

numberOfElements

NUMERO\_ELEMENTOS

Número de registros na página

N

038

NÃO

NÃO

65

last

ULTIMO

Último

N

038

NÃO

NÃO

66

first

PRIMEIRO

Primeiro

N

038

NÃO

NÃO

67

sort

ORDENACAO

Ordenação

N

038

NÃO

NÃO

ADO\- 877116

1043049

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 877116

__RN01__

__Campo 01 – ID da Guia__

__Tabela: __SAFX346

__Item: __01

__Nome do Campo: __ID\_GUIA

__Descrição: __ID da Guia 

__Tipo: __N

__Tamanho: __038

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o ID da Guia de Pagamento

ADO\- 877116

__RN02__

__Campo 02 – ID do Título__

__Tabela: __SAFX346

__Item: __02

__Nome do Campo:__ ID\_TITULO

__Descrição: ID do Título__

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário:__ 

Informar o Título da Guia de Pagamento 

ADO\- 877116

__RN03__

__Campo 03 – CNPJ da Empresa__

__Tabela: __SAFX346

__Item: __03

__Nome do Campo:__ CNPJ\_EMPRESA

__Descrição: __CNPJ da Empresa 

__Tipo:A__

__Tamanho:__ 014

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o CNPJ da Empresa

ADO\- 877116

__RN04__

__Campo 04 – Código da empresa__

 

__Tabela: __SAFX346

__Item: __04

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ N

__Tamanho: __008

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da Empresa

Exibir a mensagem da TFIX 22 CÓDIGO 90001

ADO\- 877116

__RN05__

__Campo 05 – Código do estabelecimento__

__Tabela: __SAFX346

__Item: __05

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ C

__Tamanho: __006__ __

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do Estabelecimento 

ADO\- 877116

__RN06__

__Campo 06 – Inscrição Substituta__

__Tabela: __SAFX346

__Item: __06

__Nome do Campo: __INSC\_SUBSTITUTA

__Descrição: __Inscrição substituta\.

__Tipo:__ N

__Tamanho:__ 30

__Campo Não Obrigatório__

__Comentário:__

Informar a Inscrição Substituta

Exibir a mensagem da TFIX 22 CÓDIGO 90002

ADO\- 877116

__RN07__

__Campo 07 – Tipo de Inscrição Substituta__

__Tabela: __SAFX346

__Item: __07

__Nome do Campo:__ TIPO\_INSC\_SUBSTITUTA

__Descrição:__ Tipo de Inscrição Substituta\.

__Tipo: C__

__Tamanho:__ 40

__Campo Não Obrigatório__

__Comentário:__

Informar o Tipo de Inscrição Substituta

ADO\- 877116

__RN08__

__Campo 08 – Data da Competência__

__Tabela:__ SAFX346

__Item:__ 08

__Nome do Campo:__ DATA\_COMP

__Descrição:__ Data de competência da conta\.

__Tipo: __N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data da Competência da Conta\. Exemplo: AAAAMMDD

ADO\- 877116

__RN09__

__Campo 09 – Tipo de Pagamento __

__Tabela:__ SAFX346

__Item:__ 09

__Nome do Campo:__ TIPO\_PAGTO

__Descrição: __Código de Arrecadação

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário:__

Informar o tipo de pagamento, de acordo com a Guia\.

ADO\- 877116

__RN10__

__Campo 10 – Código de Receita__

__Tabela: __SAFX346

__Item: 10__

__Nome do Campo:__ COD\_RECEITA

__Descrição:__ Código da receita que está sendo paga\.

__Tipo: Number__

__Tamanho:__ 020

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa o Código de Receita\.

Exibir a mensagem da TFIX 22 CÓDIGO 913298 

ADO\- 877116

__RN11__

__Campo 11 – Código de Detalhamento da Receita__

__Tabela:__ SAFX346

__Item:__ 11

__Nome do Campo:__ DET\_RECEITA

__Descrição:__ Código do detalhamento da receita\.

__Tipo: __N

__Tamanho: __020

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa o Detalhamento da Receita\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913299

ADO\- 877116

__RN12__

__Campo 12 – GRUPO de IMPOSTO__

__Tabela: __SAFX346

__Item: __12

__Nome do Campo:__ GRUPO\_IMPOSTO

__Descrição: __Nome do imposto

__Tipo:__ C

__Tamanho: __030

__Campo Não Obrigatório\.__

__Comentário:__

ADO\- 877116

1043049

__RN13__

__Campo 13 – Unidade Federal Favorecida__

__Tabela: __SAFX346

__Item: __13

__Nome do Campo:__ UF\_FAVORECIDA__ __

__Descrição: __UF favorecida 

__Tipo:__ C

__Tamanho: __002

__Campo Não Obrigatório__

__Comentário:__

Este campo informa a Unidade Federal Favorecida conforme a SAFX 163 \(Guia de Recolhimento de Tributos Estaduais – GNRE\), SAFX 223 \(Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig\./Dest \(EC 87/15\)\), SAFX 224 \(Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig\./Dest \(EC 87/15\) – Módulo PIM\), SAFX 305 \(Tabela das Guias de Recolhimento da Apuração do ICMS\)

ADO\- 877116

__RN14__

__Campo 14 – Código do Documento __

__Tabela: __SAFX346

__Item: 14__

__Nome do Campo:__ COD\_DOC

__Descrição: __Código da Cidade do Documento\.

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário:__

Este campo informa Código da Cidade do Documento

ADO\- 877116

__RN15__

__Campo 15 – Número do Documento__

__Tabela: __SAFX346

__Item: 15__

__Nome do Campo:__ NUM\_DOC\_ORIGEM

__Descrição: __Número do Documento

__Tipo:__ N

__Tamanho: __4000

__Campo Obrigatório__

__Comentário:__

Este campo informa o Número do Documento

Exibir a mensagem da TFIX 22 CÓDIGO 913300

ADO\- 877116

__RN16__

__Campo 16 – Série__

__Tabela: __SAFX346

__Item: 16__

__Nome do Campo:__ SERIE\_DOC

__Descrição: __Série do documento

__Tipo:__ C

__Tamanho: __003

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referente a Série do Documento

ADO\- 877116

__RN17__

__Campo 17 – Chave de Nota Fiscal__

__Tabela: __SAFX346

__Item: 17__

__Nome do Campo:__ CHAVE\_NF

__Descrição: __Chave NF

__Tipo:__ N

__Tamanho:__44

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes a Chave de Nota Fiscal

ADO\- 877116

__RN18__

__Campo 18 – Indicação de Cancelamento__

__Tabela: __SAFX346

__Item: 18__

__Nome do Campo:__ IND\_CANCELAMENTO

__Descrição: __Indicação de cancelamento

__Tipo:__ Boolean

__Tamanho: __True/false

__Campo Não Obrigatório__

__Comentário:__

Este campo indica se ocorreu ou não o cancelamento das Guias de Pagamento

ADO\- 877116

__RN19__

__Campo 19 – Informações de Cancelamento__

__Tabela: __SAFX346

__Item: 19__

__Nome do Campo:__ INFO\_CANCELAMENTO

__Descrição: __Informações sobre o cancelamento

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__ 

__Comentário:__

Este campo exibe informações referentes ao cancelamento das Guias\.

ADO\- 877116

__RN20__

__Campo 20 \- Status__

__Tabela: __SAFX346

__Item: 20__

__Nome do Campo:__ STATUS

__Descrição: Status da Guia de Pagamento__

__Tipo:__ N

__Tamanho: __38

__Campo Obrigatório__

__Comentário: __Informar  o código do status da guia de pagamento\.

O campo STATUS deve ser preenchido e informar o codigo do status da guia de pagamento\. \(Vide RN21\)

Exibir a mensagem da TFIX 22 CÓDIGO 913340

ADO\- 877116

__RN21__

__Campo 21 – Descrição do Status__

__Tabela: __SAFX346

__Item: 21__

__Nome do Campo:__ DSC\_STATUS

__Descrição: __Descrição do status

__Tipo:__ C

__Tamanho: __50

__Campo Obrigatório__

__Comentário:__

Exibir o status das Guias de Pagamento, podendo variar entre: 1\) Aguardando Guia, 2\) Processando Guia, 3\) Aguardando Pagamento, 4\) Aguardando Aprovação, 5\) Processando Pagamento e 6\) Guia Paga\. Compõe o campo STATUS   
O campo DSC\_STATUS deve ser preenchido e informar a descrição do status da guia de pagamento \(RN20\)

Exibir a mensagem da TFIX 22 CÓDIGO 913341

ADO\- 877116

__RN22__

__Campo 22 – Valor Principal do Título__

__Tabela: __SAFX346

__Item: 22__

__Nome do Campo:__ VLR\_PRINCIPAL

__Descrição: __Valor principal do título

__Tipo:__ N

__Tamanho: __38

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes ao Valor Principal do Título/Documento de Arrecadação

Exibir a mensagem da TFIX 22 CÓDIGO 913296

ADO\- 877116

__RN23__

__Campo 23 – Valor do Fundo Estadual de Combate à Pobreza__

__Tabela: __SAFX346

__Item: 23__

__Nome do Campo:__ VLR\_FECP

__Descrição: __Valor do recolhimento ao Fundo Estadual de Combate à Pobreza\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_principal com o valor da guia excluído o valor do recolhimento ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_principal\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes ao Valor do Fundo Estadual de Combate à Pobreza\.

ADO\- 877116

__RN24__

__Campo 24 – Valor dos Juros__

__Tabela: __SAFX346

__Item: 24__

__Nome do Campo:__ VLR\_JUROS

__Descrição: __Valor dos juros quando o pagamento ocorrer em atraso\. Esse campo foi calculado automaticamente pelo sistema, caso não tenha sido informado na integração\.

__Tipo:__ N

__Tamanho: __015,2

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes ao Valor dos Juros, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente\.

ADO\- 877116

__RN25__

__Campo 25 – Valor da Multa __

__Tabela: __SAFX346

__Item: 25__

__Nome do Campo:__ VLR\_MULTA

__Descrição: __Valor da multa quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes ao Valor da Multa, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente\.

ADO\- 877116

__RN26__

__Campo 26 – Valor de Atualização Monetária__

__Tabela: __SAFX346

__Item: 27__

__Nome do Campo:__ VLR\_ATUAL\_MONETARIA

__Descrição: __Valor da atualização monetária 

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário:__

Informa o Valor de Atualização Monetária\.

ADO\- 877116

__RN27__

__Campo 27 – Outros Valores__

__Tabela: __SAFX346

__Item: 27__

__Nome do Campo:__ VLR\_OUTROS__ __

__Descrição: __Outros valores

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Este campo possui informações referentes a Outros Valores, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS\-ST,ICMS ANTECIPADO, PIS/COFINS, IRPJ\-CSLL, IRPJ\-CSLL, IPI, DIFAL, FCP\.

ADO\- 877116

__RN28__

__Campo 28 \- Valor do Fundo Estadual de Combate à Pobreza – Juros__

__Tabela: __SAFX346

__Item: 28__

__Nome do Campo:__ VLR\_FECP\_JUROS

__Descrição: __Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_juros com o valor dos juros excluído o valor dos juros referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_juros\. Esse campo será calculado automaticamente pelo sistema caso não tenha sido informado na integração\.

__Tipo:__N

__Tamanho: 015V002__

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo possui informações referentes ao Valor de Juros referente ao Fundo Estadual de Combate à Pobreza, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente\.

ADO\- 877116

__RN29__

__Campo 29 – Valor do Fundo Estadual de Combate à Pobreza – Multa__

__Tabela: __SAFX346

__Item: 29__

__Nome do Campo:__ VLR\_FECP\_MULTA

__Descrição: __Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_multa com o valor da multa excluído o valor da multa referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_multa\. Esse campo será calculado automaticamente pelo sistema caso não tenha sido informado na integração\. 

__Tipo:__ N

__Tamanho: 015V002__

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo possui informações referentes ao Valor de Multa referente ao Fundo Estadual de Combate à Pobreza, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente\.

ADO\- 877116

__RN30__

__Campo 30 – Valor Total__

__Tabela: __SAFX346

__Item: 30__

__Nome do Campo:__ VLR\_TOTAL

__Descrição: __Valor total

__Tipo:__ N

__Tamanho: __38

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo possui informações referentes ao Valor Total, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS\-ST,ICMS ANTECIPADO, PIS/COFINS, IRPJ\-CSLL, IRPJ\-CSLL, IPI, DIFAL, FCP\.

ADO\- 877116

__RN31__

__Campo 31 – Código do Produto__

__Tabela: __SAFX346

__Item: 32__

__Nome do Campo:__ COD\_PRODUTO__ __

__Descrição: __Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração\. Consulte a UF para obter a lista de códigos de produtos válidos\.

__Tipo:__ N

__Tamanho: __005

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa o Código do Produto conforme a SAFX 163 \(Guia de Recolhimento de Tributos Estaduais – GNRE\), SAFX 223 \(Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig\./Dest \(EC 87/15\)\), SAFX 224 \(Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig\./Dest \(EC 87/15\) – Módulo PIM\), SAFX 305 \(Tabela das Guias de Recolhimento da Apuração do ICMS\)

ADO\- 877116

__RN32__

__Campo 32 – Convênio__

__Tabela: __SAFX346

__Item: 32__

__Nome do Campo:__ CONVENIO

__Descrição: __Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo\. Esse campo é utilizado na geração da GNRE por apuração\.

__Tipo:__ C

__Tamanho: __030

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo possui informações referentes ao Convênio, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS\-ST,ICMS ANTECIPADO, PIS/COFINS, IPI, DIFAL, FCP\.

ADO\- 877116

__RN33__

__Campo 33 – CNPJ Favorecido__

__Tabela: __SAFX346

__Item: 34__

__Nome do Campo:__ CNPJ\_FAVORECIDO

__Descrição: __CNPJ do favorecido\. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\.

__Tipo:__ A

__Tamanho: __014

__Campo Não Obrigatório__

__Comentário:__

Informar o CNPJ do Favorecido

ADO\- 877116

__RN34__

__Campo 34 – Inscrição Estadual do Favorecido__

__Tabela: __SAFX346

__Item: 34__

__Nome do Campo:__ INSC\_ESTADUAL\_FAVORECIDO

__Descrição: __Inscrição Estadual do favorecido\.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

__Tipo:__ C

__Tamanho: __030

__Campo Não Obrigatório__

__Comentário:__

Esse campo identifica a inscrição estadual do favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

ADO\- 877116

__RN35__

__Campo 35 – CPF do Favorecido__

__Tabela: SAFX346__

__Item: 35__

__Nome do Campo:__ CPF\_FAVORECIDO

__Descrição: __CPF do favorecido

__Tipo:__ A

__Tamanho: __014

__Campo Não Obrigatório__

__Comentário:__

Esse campo identifica o CPF do favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

ADO\- 877116

__RN36__

__Campo 36 – Informações Complementares__

__Tabela: __SAFX346

__Item: 36__

__Nome do Campo:__ INFO\_COMPL\_DOCUMENTO

__Descrição: __Informações complementares do documento 

__Tipo:__ C

__Tamanho: __050

__Campo Não Obrigatório__

__Comentário:__

Exibe as informações complementares referentes ao documento\.

ADO\- 877116

__RN37__

__Campo 37 – Indicador de Erro__

__Tabela: __SAFX346

__Item: 38__

__Nome do Campo:__ IND\_ERRO

__Descrição: __Indicador de erro

__Tipo:__ Boolean

__Tamanho: __True/false

__Campo Não Obrigatório__

__Comentário:__

Este campo indica a possibilidade de ter ocorrido ou não um erro por parte do sistema\.

ADO\- 877116

__RN38__

__Campo 38 – Mensagem de Erro__

__Tabela: __SAFX346

__Item: 39__

__Nome do Campo:__ MENSAGEM\_ERRO

__Descrição: __Mensagem de erro

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário:__

Caso tenha ocorrido um erro, o sistema exibirá uma mensagem especificando o erro que ocorreu\.

ADO\- 877116

__RN39__

__Campo 39 – Data de Vencimento__

__Tabela: __SAFX346

__Item: 39__

__Nome do Campo:__ DATA\_VENCTO

__Descrição: __Informar a data de vencimento da Guia\.

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data do Vencimento  da Guia de Pagamento\.

ADO\- 877116

__RN40__

__Campo 40 – Data de Vencimento Original__

__Tabela: __SAFX346

__Item: 40__

__Nome do Campo:__ DATA\_VENCTO\_ORIGINAL

__Descrição: __data de vencimento original

__Tipo:__ N

__Tamanho: 8__

__Campo Não Obrigatório__

__Comentário:__

Informar a  Data de Vencimento Original da Guia de Pagamento\.

ADO\- 877116

__RN41__

__Campo 41– Código de Barras__

__Tabela:__ SAFX346

__Item: 41__

__Nome do Campo:__ COD\_BARRAS

__Descrição: __Código de Barras

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário:__

Informar o código de barras da Guia de Pagamento\.

ADO\- 877116

__RN42__

__Campo 42 – Número de Controle__

__Tabela: __SAFX346

__Item: 42__

__Nome do Campo:__ NUM\_CONTROLE

__Descrição: __Número de Controle

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário:__

Informar o número de controle do documento de arrecadação\.

ADO\- 877116

__RN43__

__Campo 43 – Data SEFAZ__

__Tabela: __SAFX346

__Item: 43__

__Nome do Campo:__ DATA\_SEFAZ

__Descrição: __Data da resposta do SEFAZ

__Tipo:__ N

__Tamanho: __8

__Campo Não Obrigatório__

__Comentário:__

Informa a data de resposta da Secretaria da Fazenda\.

ADO\- 877116

__RN44__

__Campo 44 – ID do Pagamento__

__Tabela: __SAFX346

__Item: 44__

__Nome do Campo:__ ID\_PAGTO

__Descrição: __ID do pagamento__ __

__Tipo:__ N

__Tamanho:__ 38

__Campo Não Obrigatório__

__Comentário:__

Informa a Identificação do Pagamento

ADO\- 877116

__RN45__

__Campo 45 – Data do Pagamento__

__Tabela: __SAFX346

__Item: 45__

__Nome do Campo:__ DATA\_PAGTO

__Descrição: __Data do Pagamento\. Esse campo será calculado automaticamente pelo sistema Tax Payments\.

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data do Pagamento\. Este campo será calculado automaticamente pelo sistema Tax Payments\.

ADO\- 877116

__RN46__

__Campo 46 – Número de Autenticação__

__Tabela: __SAFX346

__Item: 46__

__Nome do Campo:__ NUM\_AUTENTICACAO

__Descrição: __Número da autenticação 

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário:__

Informar o Número de Autenticação Bancária

ADO\- 877116

__RN47__

__Campo 47 – ID do Pagador__

__Tabela: __SAFX346

__Item: 47__

__Nome do Campo:__ ID\_PAGADOR

__Descrição: __ID do pagador

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar a identificação do pagador 

ADO\- 877116

__RN48__

__Campo 48 – CNPJ do Pagador__

__Tabela: __SAFX346

__Item: 48__

__Nome do Campo:__ CNPJ\_PAGADOR

__Descrição: __CNPJ do pagador

__Tipo:__ A

__Tamanho: __014

__Campo Não Obrigatório__

__Comentário:__

Informar o CNPJ do Pagador 

ADO\- 877116

__RN49__

__Campo 49 – Código do Banco__

__Tabela: __SAFX346

__Item: 49__

__Nome do Campo:__ COD\_BANCO

__Descrição: __Código do banco

__Tipo:__ N

__Tamanho: 003__

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Banco

ADO\- 877116

__RN50__

__Campo 50 – Agência__

__Tabela: __SAFX346

__Item: 50__

__Nome do Campo:__ AGENCIA

__Descrição: __Agência

__Tipo:__ N 

__Tamanho: 005__

__Campo Não Obrigatório__

__Comentário:__

Informar a agência bancária

ADO\- 877116

__RN51__

__Campo 51 – Dígito da Agência__

__Tabela: __SAFX346

__Item: 51__

__Nome do Campo:__ DIG\_AGENCIA

__Descrição__: Dígito da Agência  

__Tipo:__ N

__Tamanho: 001__

__Campo Não Obrigatório__

__Comentário: __

Informar o Dígito que compõe a Agência Bancária

ADO\- 877116

__RN52__

__Campo 52 – Conta Corrente__

__Tabela: __SAFX346

__Item: 52__

__Nome do Campo:__ CONTA\_CORRENTE

__Descrição: __Conta Corrente

__Tipo:__ N 

__Tamanho: 015__

__Campo Não Obrigatório__

__Comentário: __

Informar a Conta Corrente

ADO\- 877116

__RN53__

__Campo 53 – Dígito da Conta Corrente __

__Tabela: __SAFX346

__Item: 53__

__Nome do Campo:__ DIG\_CONTA\_CORRENTE

__Descrição: __Dígito da conta corrente

__Tipo:__ N

__Tamanho: 001__

__Campo Não Obrigatório__

__Comentário: __

Informar o Dígito que compõe a Conta Corrente

ADO\- 877116

__RN54__

__Campo 54 – Objeto JSON__

__Tabela: __SAFX346

__Item: 55__

__Nome do Campo:__ OBJETO\_JSON

__Descrição: __Objeto JSON com customizações das regras de pagamento associadas à guia

__Tipo:__ Null

__Tamanho: \-__

__Campo Não Obrigatório__

__Comentário: __

Informar o Objeto JSON com customizações das regras de pagamento associadas à guia

ADO\- 877116

__RN55__

__Campo 55 – Array Bytes__

__Tabela: __SAFX346

__Item: 55__

__Nome do Campo:__ ARRAY\_BYTES

__Descrição: __Array de bytes do PDF, comprimido usando biblioteca de compressão Zlib e codificado em Base64

__Tipo:__ String

__Tamanho: \-__

__Campo Não Obrigatório__

__Comentário: __

Informar o array de bytes do PDF, comprimido usando biblioteca de compressão Zlib e codificado em Base64\.

ADO\- 877116

__RN56__

__Campo 56 – Conteúdo JSON__

__Tabela: __SAFX346

__Item: 57__

__Nome do Campo:__ CONTEUDO\_JSON

Descrição: Conteúdo que foi recebido no atributo campos extras do JSON

__Tipo:__ C

__Tamanho: __\-

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes ao conteúdo que foi recebido no atributo campos extras do JSON

ADO\- 877116

__RN57__

__Campo 57 – QR Code do PIX__

__Tabela: __SAFX346

__Item: 57__

__Nome do Campo:__ QR\_CODE\_PIX

__Descrição: __QR Code do PIX

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário: __

__Comentário: __

Informar o QR Code da transação realizada através do PIX

ADO\- 877116

__RN58__

__Campo 58 – Login do Usuário__

__Tabela: __SAFX346

__Item: 58__

__Nome do Campo:__ LOGIN\_USUARIO

__Descrição: __Login do usuário que importou o arquivo

__Tipo:__ String

__Tamanho: __4000

__Campo Não Obrigatório__

__Comentário: __

Informar o Login de Usuário que importou o arquivo

ADO\- 877116

__RN59__

__Campo 59 – Data de Débito__

__Tabela: __SAFX346

__Item: 59__

__Nome do Campo:__ DAT\_DEBITO

__Descrição: __Data de Débito

__Tipo:__ N

__Tamanho: 008__

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes a Data de Débito\.

ADO\- 877116

__RN60__

__Campo 60 – Total de Elementos__

__Tabela: __SAFX346

__Item: 60__

__Nome do Campo:__ TOTAL\_ELEMENTOS

__Descrição: __Total de Registros/Elementos da página

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Informar o Total de Registros da Página

ADO\- 877116

__RN61__

__Campo 61 – Total de Páginas__

__Tabela: __SAFX346

__Item: 61__

__Nome do Campo:__ TOTAL\_PAGINAS

__Descrição: __Total de páginas

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Informar o Total de Páginas

ADO\- 877116

__RN62__

__Campo 62 – Tamanho__

__Tabela: __SAFX346

__Item: 62__

__Nome do Campo:__ TAMANHO

__Descrição: __Tamanho máximo da página \(máximo 100\)

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes ao Tamanho Máximo de Páginas

ADO\- 877116

__RN63__

__Campo 63 – Número__

__Tabela: __SAFX346

__Item: 63__

__Nome do Campo:__ NUMERO

__Descrição: __Número da página

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes ao Número da Página

ADO\- 877116

__RN64__

__Campo 64 – Número de Elementos__

__Tabela: __SAFX346

__Item: 64__

__Nome do Campo:__ NUMERO\_ELEMENTOS

__Descrição: __Número de registros da página

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes ao Número de Registros da Página

ADO\- 877116

__RN65__

__Campo 65 – Último__

__Tabela: __SAFX346

__Item: 65__

__Nome do Campo:__ ULTIMO

__Descrição: __Retorna a informação se a página atual é a última

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações permitindo ao usuário saber se a página atual é a última

ADO\- 877116

__RN66__

__Campo 66 – Primeiro__

__Tabela: __SAFX346

__Item: 66__

__Nome do Campo:__ PRIMEIRO

__Descrição: __Retorna informação se a página atual é a primeira

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações permitindo ao usuário verificar se a página atual é a primeira

ADO\- 877116

__RN67__

__Campo 67 – Ordenação__

__Tabela: __SAFX346

__Item: 67__

__Nome do Campo:__ ORDENACAO

__Descrição:__ É utilizado na ordenação do resultado

__Tipo:__ N

__Tamanho: __038

__Campo Não Obrigatório__

__Comentário: __

Este campo possui informações referentes a Ordenação do Resultado

ADO\- 877116

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

