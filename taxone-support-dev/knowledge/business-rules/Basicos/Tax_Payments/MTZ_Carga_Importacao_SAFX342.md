# MTZ_Carga_Importacao_SAFX342 

- **Fonte:** MTZ_Carga_Importacao_SAFX342 .docx
- **Modificado:** 2025-12-03
- **Tamanho:** 119 KB

---

THOMSON REUTERS

 TAX PAYMENTS – IMPORTAÇÃO \- SAFX342 \(Guias de Pagamentos \-Extra Apuração\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Guia de Pagamento

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 768407

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX342\.

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

A tabela SAFX342 foi desenvolvida especificamente para carregar informações relacionadas às guias de pagamento que não estão disponíveis no sistema Tax One\. O principal objetivo desta tabela é facilitar a geração do JSON necessário para a integração com o sistema Tax Payments\.

Adicionalmente, a funcionalidade de importação associada à SAFX342 tem o propósito de trazer dados exclusivos para o Grupo de Impostos 'Extras Apurações'\. Estes dados, ausentes no Tax One, são essenciais para viabilizar a correta geração das guias de pagamento\.

__Localização:__

__             Módulo: __Básicos > Job Servidor

__                 Menu: __Carga__ __> Programação > Execução

__                        __Importação > Programação > Execução     

                                     Importação batch > Programação > Execução

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX342 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para a Importação da SAFX342:

A importação da SAFX342 deve seguir as seguintes premissas de negócio e comportamentos:

- No campo __Grupo de Imposto__, considerar sempre "Extra Apuração"\. Essa informação é exclusivamente para receber os impostos importados via SAFX342\.
- Quando o imposto "Extra Apuração" for importado, o campo __Grupo de Imposto__ na tela __Status__ deverá permanecer com o preenchimento fixo "Aguardando Envio"\. Isso serve para sinalizar ao usuário que será necessário gerar o arquivo JSON\.
- O __Relatório de Guias__ deve ser atualizado automaticamente para receber as informações importadas pela SAFX342\.

__Resultado da Importação:__

Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:

- __Manutenção > Guias de Pagamentos > Status das Guias__
- __Manutenção > Guias de Pagamentos > Relatórios de Guias__

__                 __

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Código de Arrecadação \-Vide regra RN07
- Campo Código de Receita – Vide regra RN08
- Campo Detalhamento da Receita \-Vide regra RN09
- Campo Número do Documento de Origem – Vide regra RN 10
- Campo Unidade Federal Favorecida – Vide regra RN 12
- Campo Cadastro Participante – Vide regra RN 27
- Campo Grupo de Imposto – Vide regra RN 32
- Campo Usuário – Vide regra RN 33
- Campo Status – Vide regra RN 34

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__ADO__

RN00

__Índice__

__Nome do Campo__

__Descrição__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

1

COD\_EMPRESA

Código da Empresa

A

003

SIM

\(\*\)

2

COD\_ESTAB

Código do Estabelecimento

A

006

SIM

\(\*\)

3

COD\_TIPO\_LIVRO

Código do Tipo do Livro

C

003

SIM

\(\*\)

4

PERIODO

Período da Apuração

N

008

SIM

\(\*\)

5

NUM\_GUIA\_PAG

Número da Guia de Pagamento

C

030

SIM

\(\*\)

6

DAT\_GUIA\_PAG

Data da Guia de Pagamento 

N

008

SIM

\(\*\)

7

COD\_ARRECADACAO

Código de Arrecadação

C

020

SIM

\(\*\)

8

COD\_RECEITA

Código de Receita

N

020

SIM

\(\*\)

9

DET\_RECEITA\_

Detalhamento da Receita 

N

020

NÃO

\(\*\)

10

NUM\_DOC\_ORIGEM

Número do Documento de Origem

N

019

SIM

\(\*\)

11

SERIE

Série

C

003

SIM

\(\*\)

12

UF\_FAVORECIDA

Unidade Federal Favorecida

C

002

SIM

\(\*\)

13

CNPJ\_FAVORECIDO

CNPJ Favorecido

C

014

NÃO

\(\*\)

14

IE\_FAVORECIDA

Inscrição Estadual Favorecida

C

030

NÃO

NÃO

15

VLR\_PRINCIPAL

Valor Principal

N

015V002

SIM

NÃO

16

DATA\_VENCIMENTO

Data do Vencimento

N

008

SIM

NÃO

17

DATA\_PAGAMENTO

Data do Pagamento

N

008

SIM

NÃO

18

VLR\_MULTA

Valor da Multa

N

015V002

NÃO

NÃO

19

VLR\_JUROS

Valor dos Juros

N

015V002

NÃO

NÃO

20

INFO\_COMPLEMENTAR

Informação Complementar

C

300

NÃO

NÃO

21

VLR\_FECP

Valor do Fundo Estadual de Combate à Pobreza

N

015V002

NÃO

NÃO

22

VLR\_FECP\_JUROS

Valor do Fundo Estadual de Combate à Pobreza \- Multa

N

015V002

NÃO

NÃO

23

VLR\_FECP\_MULTA

Valor do Fundo Estadual de Combate à Pobreza \- Juros

N

015V002

NÃO

NÃO

24

CONVENIO

Convênio

C

030

NÃO

\(\*\)

25

COD\_PRODUTO

Código do Produto

N

005

NÃO

\(\*\)

26

CHAVE\_DFE

Chave de Documento Fiscal Eletrônico 

N

044

NÃO

NÃO

27

CAD\_PART

Cadastro Participante

O

\-

NÃO

NÃO

27\.1

COD\_PARTICIPANTE

Código do Participante

C

060

SIM

NÃO

27\.2

DATA\_VALID

Data de Validação

N

008

SIM

\(\*\)

27\.3

CNPJ

CNPJ do Participante

N

014

NÃO

\(\*\)

27\.4

CPF

CPF do Participante

N

011

NÃO

\(\*\)

27\.5

ID\_ESTRANGEIRO

ID do Participante

C

020

NÃO

\(\*\)

27\.6

RAZAO\_SOCIAL

Razão Social

C

255

SIM

NÃO

27\.7

NOME\_FANTASIA

Nome Fantasia 

C

255

SIM

NÃO

27\.8

ENDERECO

Endereço

C

060

NÃO

NÃO

27\.9

NUMERO

Número

C

010

NÃO

NÃO

27\.10

COMPLEMENTO

Complemento

C

060

NÃO

NÃO

27\.11

BAIRRO

Bairro

C

060

NÃO

NÃO

27\.12

CEP

CEP

N

008

NÃO

NÃO

27\.13

COD\_MUNICIPIO

Código do Município

N

007

NÃO

NÃO

27\.14

UF

Unidade Federal do Participante

C

002

SIM

NÃO

27\.15

COD\_PAIS

Código do País 

N

005

NÃO

NÃO

27\.16

DDD

DDD

N

002

NÃO

NÃO

27\.17

TELEFONE

Telefone

N

009

NÃO

NÃO

27\.18

EMAIL

E\-mail

C

060

NÃO

NÃO

27\.19

INSC\_ESTADUAL

Inscrição Estadual

C

014

NÃO

NÃO

27\.20

INSC\_MUNICIPAL

Inscrição Municipal 

C

015

NÃO

NÃO

27\.21

SUFRAMA

Inscrição na Suframa

C

009

NÃO

NÃO

28

COD\_MUN\_FAVORECIDO

Código do Município Favorecido

N

007

NÃO

\(\*\)

29

VLR\_OUTROS

Valor Outros

N

015V002

NÃO

NÃO

30

VLR\_BASE\_CALC

Valor da Base de Cálculo

N

015V002

NÃO

NÃO

31

CAMPOS\_EXTRAS

Campos Extras

C

\-

NÃO

NÃO

32

GRUPO\_IMPOSTO

Grupo do Imposto

C

030

SIM

NÃO

33

USUARIO

Usuário

C

100

SIM

NÃO

34

STATUS

Status

C

030

SIM

NÃO

 

ADO\- 768407

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 768407

__RN01__

__Campo 01 \- Código da empresa__

 

__Tabela: __SAFX342

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __008

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da Empresa

Exibir a mensagem da TFIX 22 CÓDIGO 90001

ADO\- 768407

__RN02__

__Campo 02 \- Código do estabelecimento__

__Tabela:__ SAFX342

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006__ __

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do Estabelecimento

Exibir a mensagem da TFIX 22 CÓDIGO 90002

ADO\- 768407

__RN03__

__Campo 03 – Código do Tipo do Livro__

__Tabela: __SAFX342

__Item: __03

__Nome do Campo:__ COD\_TIPO\_LIVRO

__Descrição: __Código do Tipo do Livro

__Tipo:__ C

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__ 

Informe o código 'EXT' do livro de apuração, que corresponde ao imposto 'Extra Apuração'\.

Exibir a mensagem da TFIX 22 CÓDIGO 913307

ADO\- 768407

__RN04__

__Campo 04 – Período__

__Tabela: __SAFX342

__Item: __04

__Nome do Campo:__ PERIODO

__Descrição: __Data da ocorrência ou do encerramento do período

__Tipo:__ N

__Tamanho: __008

__Campo NÃO OB__

__Chave Primária__

__Comentário:__

Informar o Período Relacionado ao Imposto para Extra Apuração e a Data da Ocorrência ou do Encerramento do Período

Exibir a mensagem da TFIX 22 CÓDIGO 913293

ADO\- 768407

__RN05__

__Campo 05 – Número da Guia de Pagamento__

__Tabela: __SAFX342

__Item: __05

__Nome do Campo:__ NUM\_GUIA\_PAG

__Descrição: __

__Tipo:__ C

__Tamanho: __030

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo de preenchimento automático do sistema Tax One gera um número sequencial para cada guia\. Por favor, não preencha este campo manualmente\.

Exibir a mensagem da TFIX 22 CÓDIGO 913306

ADO\- 768407

__RN06__

__Campo 06 – Data da Guia de Pagamento__

__Tabela: __SAFX342

__Item: __06

__Nome do Campo: __DAT\_GUIA\_PAG

__Descrição: __Data de Pagamento da Guia

__Tipo: N__

__Tamanho: __08

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informa a data do pagamento da guia\.

Exibir a mensagem da TFIX 22 CÓDIGO 913295

ADO\- 768407

__RN07__

__Campo 07 – Código de Arrecadação__

__Tabela: __SAFX342

__Item: __07

__Nome do Campo: __COD\_ARRECADACAO

__Descrição: __Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax\. \(ex\.: DARF; GNRE\)

__Tipo:__ C

__Tamanho:__ 020

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código de Arrecadação conforme tabela TACES 119 \(Tabela de Código Tax Payments\) 

Exibir a mensagem da TFIX 22 CÓDIGO 913297

ADO\- 768407

__RN08__

__Campo 08 – Código de Receita__

__Tabela: __SAFX342

__Item: __08

__Nome do Campo:__ COD\_RECEITA

__Descrição:__ Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação\.

__Tipo: N__

__Tamanho:__ 020

__Campo SIM__

__Chave Primária__

__Comentário:__

Este campo informa o Código de Receita conforme tabela TACES 119 \(Tabela de Código Tax Payments \(DOOTAX\)

Exibir a mensagem da TFIX 22 CÓDIGO 913298

ADO\- 768407

__RN09__

__Campo 09 – Detalhamento da Receita__

__Tabela:__ SAFX342

__Item:__ 09

__Nome do Campo:__ DET\_RECEITA

__Descrição:__ Código do detalhamento da receita\.

__Tipo: __N

__Tamanho: __020

__Campo NÃO OBRIGATÓRIO__

__Chave Primária__

__Comentário:__

Este campo informa o detalhamento da receita, conforme a tabela TACES 119 \(Tabela de Código Tax Payments\)\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913299

ADO\- 768407

__RN10__

__Campo 10 – Número do Documento de Origem __

__Tabela:__ SAFX342

__Item:__ 10

__Nome do Campo:__ NUM\_DOC\_ORIGEM

__Descrição: __Número do documento que deu origem ao pagamento\.

__Tipo:__ N

__Tamanho: __019

__Campo SIM__

__Chave Primária__

__Comentário:__

__ Preencher a Chave do ID __

O ID será composto pelos seguintes elementos, com tamanhos ajustados:

1. __Cod\_Empresa:__ 3 caracteres \(Ex\.: "001"\)\.
2. __Cod\_Estabelecimento:__ 6 caracteres \(Ex\.: "000001"\)\.
3. __Cod\_Receita:__ 6 caracteres \(Ex\.: "131701"\)\.
4. __Hora de Geração:__ 4 caracteres \(Ex\.: "1536"\)\.

__Formato Final__

__\[Cod\_Empresa\]\[Cod\_Estabelecimento\]\[Cod\_Receita\]\[Hora\]__

__Exemplo Final:__  
0010000011317011536

Exibir a mensagem da TFIX 22 CÓDIGO 913300

ADO\- 768407

__RN11__

__Campo 11 – Série__

__Tabela: __SAFX342

__Item: __11

__Nome do Campo:__ SERIE

__Descrição: __Série do documento

__Tipo:__ C

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informe o código '01' para série, que corresponde ao imposto 'Extra Apuração'\.

Exibir a mensagem da TFIX 22 CÓDIGO 913308

ADO\- 768407

__RN12__

__Campo 12 – Unidade Federal Favorecida__

__Tabela: __SAFX342

__Item: __12

__Nome do Campo:__ UF\_FAVORECIDA

__Descrição: __Sigla da UF favorecida\.

__Tipo:__ C

__Tamanho: __002

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Este campo deve informar a Unidade Federal Favorecida conforme especificado na tabela TACES 119 \(Tabela de Código Tax Payments\)\. O preenchimento é obrigatório e deve estar em conformidade com o COD\_RECEITA preenchido anteriormente\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913301

ADO\- 768407

__RN13__

__Campo 13 – CNPJ Favorecido__

__Tabela: __SAFX342

__Item: __13

__Nome do Campo:__ CNPJ\_FAVORECIDO

__Descrição: __CNPJ do favorecido\. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\.

__Tipo:__ C

__Tamanho: __014

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o CNPJ do favorecido\. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\.

ADO\- 768407

__RN14__

__Campo 14 – Inscrição Estadual Favorecida__

__Tabela: __SAFX342

__Item: __14

__Nome do Campo:__ IE\_FAVORECIDA

__Descrição: __Inscrição Estadual do favorecido\.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

__Tipo:__ C

__Tamanho: __030

__Campo Não Obrigatório__

__Comentário:__

Informar a sigla da Inscrição Estadual Favorecida

ADO\- 768407

__RN15__

__Campo 15 – Valor Principal__

__Tabela: __SAFX342

__Item: 15__

__Nome do Campo:__ VLR\_PRINCIPAL

__Descrição: __Valor principal do título\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Obrigatório__

__Comentário:__

Informar o Valor da Guia para Recolhimento do Imposto "Extra Apuração"

Exibir a mensagem da TFIX 22 CÓDIGO 913296

ADO\- 768407

__RN16__

__Campo 16 – Data do Vencimento__

__Tabela: __SAFX342

__Item: 16__

__Nome do Campo:__ DATA\_VENCIMENTO

__Descrição: __Informar a data de vencimento da Guia\.

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data do Vencimento\.

Exibir a mensagem da TFIX 22 CÓDIGO 913294

ADO\- 768407

__RN17__

__Campo 17 – Data do Pagamento__

__Tabela: __SAFX342

__Item: 17__

__Nome do Campo:__ DATA\_PAGAMENTO

__Descrição: __Data do Pagamento\. Esse campo será calculado automaticamente pelo sistema Tax Payments\.

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data do Pagamento\.

Exibir a mensagem da TFIX 22 CÓDIGO 913295

ADO\- 768407

__RN18__

__Campo 18 – Valor da Multa __

__Tabela: __SAFX342

__Item: 18__

__Nome do Campo:__ VLR\_MULTA

__Descrição: __Valor da multa quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor da multa quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração Tax Payments

ADO\- 768407

__RN19__

__Campo 19 – Valor dos Juros__

__Tabela: __SAFX342

__Item: 19__

__Nome do Campo:__ VLR\_JUROS

__Descrição: __Valor dos juros quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração\.

__Tipo:__ N

__Tamanho: __015V002

__Campo NÃO Obrigatório__

__Comentário:__

Valor dos juros quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração no Tax Payments

ADO\- 768407

__RN20__

__Campo 20 – Informação Complementar__

__Tabela: __SAFX342

__Item: 20__

__Nome do Campo:__ INFO\_COMPLEMENTAR

__Descrição: __Informação complementar a ser incluída na emissão do título a pagar\.

__Tipo:__ C

__Tamanho: __300

__Campo Não Obrigatório__ 

__Comentário:__

Informação complementar a ser incluída na emissão da guia de pagamento\.

ADO\- 768407

__RN21__

__Campo 21 – Valor do Fundo Estadual de Combate à Pobreza__

__Tabela: __SAFX342

__Item: 21__

__Nome do Campo:__ VLR\_FECP

__Descrição: __Valor do recolhimento ao Fundo Estadual de Combate à Pobreza\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_principal com o valor da guia excluído o valor do recolhimento ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_principal\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor do recolhimento ao Fundo Estadual de Combate à Pobreza\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_principal com o valor da guia excluído o valor do recolhimento ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_principal\.

ADO\- 768407

__RN22__

__Campo 22 – Valor do Fundo Estadual de Combate à Pobreza – Multa__

__Tabela: __SAFX342

__Item: 22__

__Nome do Campo:__ VLR\_FECP\_MULTA

__Descrição: __Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_multa com o valor da multa excluído o valor da multa referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_multa\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor da multa quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração no Tax Payments

ADO\- 768407

__RN23__

__Campo 23 – Valor do Fundo Estadual de Combate à Pobreza – Juros__

__Tabela: __SAFX342

__Item: 23__

__Nome do Campo:__ VLR\_FECP\_JUROS

__Descrição: __Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_juros com o valor dos juros excluído o valor dos juros referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_juros\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\.

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor dos juros quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\.

ADO\- 768407

__RN24__

__Campo 24 – Convênio__

__Tabela: __SAFX342

__Item: 24__

__Nome do Campo:__ CONVENIO

__Descrição: __Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo\. Esse campo é utilizado na geração da GNRE por apuração\.

__Tipo:__ C

__Tamanho: __030

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo\. Esse campo é utilizado na geração da GNRE por apuração\.

ADO\- 768407

__RN25__

__Campo 25 – Código do Produto__

__Tabela: : __SAFX342

__Item: 25__

__Nome do Campo:__ COD\_PRODUTO

__Descrição: __Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração\. Consulte a UF para obter a lista de códigos de produtos válidos\.

__Tipo:__ N

__Tamanho: __005

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração\.

ADO\- 768407

__RN26__

__Campo 26 – Chave de Documentos Fiscal Eletrônico __

__Tabela: __SAFX342

__Item: 26__

__Nome do Campo:__ CHAVE\_DFE

__Descrição: __Chave de acesso do documento fiscal:

Para documentos fiscais eletrônicos, informar a chave com 44 dígitos\.

__Tipo:__ N

__Tamanho: __044

__Campo Não Obrigatório__

__Comentário:__

Chave de acesso do documento fiscal: Para documentos fiscais eletrônicos, informar a chave com 44 dígitos\.

ADO\- 768407

__RN27__

__Campo 27 – Cadastro Participante__

__Tabela: __SAFX342

__Item: 27__

__Nome do Campo:__ CAD\_PART

__Descrição: __Informações do participante \(destinatário, emitente, transportador etc\.\)\. Esse campo deve ser informado quando os dados do participante são exigidos na emissão ou visualização da guia\.

Ver layout do campo na aba "Cadastros", tabela "cad\_part"\.

__Tipo:__ O

__Tamanho: \-__

__Campo Não Obrigatório__

__Comentário:__

O campo CAD\_PART não é obrigatório\. No entanto, se optar por preenchê\-lo, torna\-se necessário informar também os seguintes campos complementares: cod\_participante ,data\_valid, razao\_social, nome\_fantasia e UF\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913302

__Índice__

__Nome do Campo__

__Descrição__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

27\.1

cod\_participante

Código de identificação do participante no sistema

C

060

SIM

NÃO

27\.2

data\_valid

Data de inclusão ou alteração do cadastro do participante

N

008

SIM

\(\*\)

27\.3

cnpj

CNPJ do participante, se Pessoa Jurídica

N

014

NÃO

\(\*\)

27\.4

cpf

CPF do participante, se Pessoa Física

N

011

NÃO

\(\*\)

27\.5

id\_estrangeiro

ID do participante, se estrangeiro

C

020

NÃO

\(\*\)

27\.6

razao\_social

Nome pessoal ou razão social do participante

C

255

SIM

NÃO

27\.7

nome\_fantasia

Nome fantasia, se Pessoa Jurídica

C

255

SIM

NÃO

27\.8

endereco

Endereço, sem o número

C

060

NÃO

NÃO

27\.9

numero

Número do endereço

C

010

NÃO

NÃO

27\.10

complemento

Complemento do endereço

C

060

NÃO

NÃO

27\.11

bairro

Bairro em que o imóvel está situado

C

060

NÃO

NÃO

27\.12

cep

CEP do imóvel

N

008

NÃO

NÃO

27\.13

cod\_municipio

Código do município, conforme tabela do IBGE

N

007

NÃO

NÃO

27\.14

uf

UF do participante

C

002

SIM

NÃO

27\.15

cod\_pais

Código do país, conforme tabela publicada pela RFB

N

005

NÃO

NÃO

27\.16

ddd

DDD telefônico

N

002

NÃO

NÃO

27\.17

telefone

Número do telefone

N

009

NÃO

NÃO

27\.18

email

Endereço de e\-mail

C

060

NÃO

NÃO

27\.19

insc\_estadual

Inscrição estadual do participante, se contribuinte do ICMS

C

014

NÃO

NÃO

27\.20

insc\_municipal

Inscrição municipal do participante, se contribuinte do ISS

C

015

NÃO

NÃO

27\.21

suframa

Inscrição na SUFRAMA

C

009

NÃO

NÃO

ADO\- 768407

__RN27\.1__

__Campo 27\.1 – Código do Participante__

__Tabela: __SAFX342

__Item: 27\.1__

__Nome do Campo:__ COD\_PARTICIPANTE

__Descrição: __Código de identificação do participante no sistema

__Tipo:__ C

__Tamanho: 60__

__Campo Obrigatório__

__Comentário:__

Informar o Código de identificação do participante\. Caso de preenchimento deste campo os demais campos

Exibir a mensagem da TFIX 22 CÓDIGO 913302

ADO\- 768407

__RN27\.2__

__Campo 27\.2 – Data de Validação__

__Tabela: __SAFX342

__Item: 27\.2__

__Nome do Campo:__ DATA\_VALID

__Descrição: __Data de inclusão ou alteração do cadastro do participante

__Tipo:__ N

__Tamanho: 8__

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar a Data de Inclusão ou Alteração do Cadastro do Participante Relacionado ao Campo "Cad\_part"

Exibir a mensagem da TFIX 22 CÓDIGO 913302

ADO\- 768407

__RN27\.3__

__Campo 27\.3 – CNPJ__

__Tabela: __SAFX342

__Item: 27\.3__

__Nome do Campo:__ CNPJ

__Descrição: __CNPJ do participante, se Pessoa Jurídica

__Tipo:__ N

__Tamanho: 14__

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

__I__nformar o CNPJ do participante, se Pessoa Jurídica Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.4__

__Campo 27\.4 – CPF__

__Tabela: __SAFX342

__Item: 27\.4__

__Nome do Campo:__ CPF

__Descrição: __CPF do participante, se Pessoa Física

__Tipo:__ N

__Tamanho: 11__

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o CPF do participante, se Pessoa Física Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.5__

__Campo 27\.5 – ID Estrangeiro__

__Tabela: __SAFX342

__Item: 27\.5__

__Nome do Campo:__ ID\_ESTRANGEIRO

__Descrição: __ID do participante, se estrangeiro

__Tipo:__ C

__Tamanho: 20__

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o ID do participante, se estrangeiro Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.6__

__Campo 27\.6 – Razão Social__

__Tabela: __SAFX342

__Item: 27\.6__

__Nome do Campo:__ RAZAO\_SOCIAL

__Descrição: __Nome pessoal ou razão social do participante

__Tipo:__ C

__Tamanho: 255__

__Campo Obrigatório__

__Comentário:__

Informar o nome pessoal ou razão social do participante Relacionado ao Campo "Cad\_part"

Exibir a mensagem da TFIX 22 CÓDIGO 913302

ADO\- 768407

__RN27\.7__

__Campo 27\.7 – Nome Fantasia__

__Tabela:__ SAFX342

__Item: 27\.7__

__Nome do Campo:__ NOME\_FANTASIA

__Descrição: __

Nome fantasia, se Pessoa Jurídica

__Tipo:__ C

__Tamanho: 255__

__Campo Obrigatório__

__Comentário:__

Informar o nome fantasia, se Pessoa Jurídica Relacionado ao Campo "Cad\_part"

Exibir a mensagem da TFIX 22 CÓDIGO 913302

ADO\- 768407

__RN27\.8__

__Campo 27\.8 – Endereço__

__Tabela: __SAFX342

__Item: 27\.8__

__Nome do Campo:__ ENDERECO

__Descrição: __

Endereço, sem o número

__Tipo:__ C

__Tamanho: 60__

__Campo Não Obrigatório__

__Comentário:__

Informar o endereço, sem o número Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.9__

__Campo 27\.9 – Número __

__Tabela: __SAFX342

__Item: 27\.9__

__Nome do Campo:__ NUMERO

__Descrição: __Número do endereço

__Tipo:__ C

__Tamanho: 10__

__Campo Não Obrigatório__

__Comentário:__

Informar o número do endereço Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.10__

__Campo 27\.10 – Complemento__

__Tabela: __cad\_part

__Item: 27\.10__

__Nome do Campo:__ COMPLEMENTO

__Descrição: __Complemento do endereço

__Tipo:__ C

__Tamanho: 60__

__Campo Não Obrigatório__

__Comentário:__

Informar o Complemento do endereço Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.11__

__Campo 27\.11 – Bairro__

__Tabela: __SAFX342

__Item: 27\.11__

__Nome do Campo:__ BAIRRO

__Descrição: __Bairro em que o imóvel está situado

__Tipo:__ C

__Tamanho: 60__

__Campo Não Obrigatório__

__Comentário:__

Informar o bairro em que o imóvel está situado Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.12__

__Campo 27\.12 – CEP__

__Tabela: __SAFX342

__Item: 27\.12__

__Nome do Campo:__ CEP

__Descrição: __CEP do imóvel

__Tipo:__ N

__Tamanho: 8__

__Campo Não Obrigatório__

__Comentário:__

Informar o CEP relacionado ao "Cad\_part"

ADO\- 768407

__RN27\.13__

__Campo 27\.13 – Código do Município__

__Tabela: __SAFX342

__Item: 27\.13__

__Nome do Campo:__ COD\_MUNICIPIO

__Descrição: __Código do município, conforme tabela do IBGE

__Tipo:__ N

__Tamanho: 7__

__Campo Não Obrigatório__

__Comentário:__

Informar Código do município, conforme tabela do IBGE e Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.14__

__Campo 27\.14 – Unidade Federal__

__Tabela: __SAFX342

__Item: 27\.14__

__Nome do Campo:__ UF

__Descrição: __UF do participante__ __

__Tipo:__ C

__Tamanho: 2__

__Campo Obrigatório__

__Comentário:__

Informar UF do participante

ADO\- 768407

__RN27\.15__

__Campo 27\.15 – Código do País__

__Tabela: __SAFX342

__Item: 27\.15__

__Nome do Campo:__ COD\_PAIS

__Descrição: __Código do país, conforme tabela publicada pela RFB

__Tipo:__ N

__Tamanho: 5__

__Campo Não Obrigatório__

__Comentário:__

Informar Código do país e Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.16__

__Campo 27\.16 – DDD__

__Tabela:__ SAFX342

__Item: 27\.16__

__Nome do Campo:__ DDD

__Descrição: __DDD telefônico

__Tipo:__ N

__Tamanho: 2__

__Campo Não Obrigatório__

__Comentário:__

Informar o DDD telefônico e Relacionado ao Campo "Cad\_part"

ADO\- 768407

__RN27\.17__

__Campo 27\.17 – Telefone__

__Tabela: __SAFX342

__Item: 27\.17__

__Nome do Campo:__ TELEFONE

__Descrição: __Número do telefone

__Tipo:__ N

__Tamanho: 2__

__Campo Não Obrigatório__

__Comentário:__

Informar o telefone e Relacionado ao Campo "Cad\_part"

__RN27\.18__

__Campo 27\.18 – E\-mail__

__Tabela: __SAFX342

__Item: 27\.18__

__Nome do Campo:__ EMAIL

__Descrição: __Endereço de e\-mail__ __

__Tipo:__ C

__Tamanho: 60__

__Campo Não Obrigatório__

__Comentário:__

Informar o endereço do e\-mail e Relacionado ao Campo "Cad\_part"

__RN27\.19__

__Campo 27\.19 – Inscrição Estadual__

__Tabela: __SAFX342

__Item: 27\.19__

__Nome do Campo:__ INSC\_ESTADUAL

__Descrição: __Inscrição estadual do participante, se contribuinte do ICMS__ __

__Tipo:__ C

__Tamanho: 14__

__Campo Não Obrigatório__

__Comentário:__

Informar a Inscrição estadual do participante, se contribuinte do ICMS  e Relacionado ao Campo "Cad\_part"

__RN27\.20__

__Campo 27\.20 – Inscrição Municipal__

__Tabela: __SAFX342

__Item: 27\.20__

__Nome do Campo:__ INSC\_MUNICIPAL

__Descrição: __Inscrição municipal do participante, se contribuinte do ICMS

__Tipo:__ C

__Tamanho: 15__

__Campo Não Obrigatório__

__Comentário:__

Informar a Inscrição municipal do participante, se contribuinte do ICMS  e Relacionado ao Campo "Cad\_part"

__RN27\.21__

__Campo 27\.21 – SUFRAMA__

__Tabela: __SAFX342

__Item: 27\.21__

__Nome do Campo:__ SUFRAMA

__Descrição: __Inscrição na SUFRAMA

__Tipo:__ C

__Tamanho: 9__

__Campo Não Obrigatório__

__Comentário:__

Informar a Inscrição suframa do participante\.

ADO\- 768407

__RN28__

__Campo 28 – Código do Município Favorecido__

__Tabela: __SAFX342

__Item: 28__

__Nome do Campo:__ COD\_MUN\_FAVORECIDO

__Descrição: __Código do município \- Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa

__Tipo:__ N

__Tamanho: __007

__Campo Não Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do município \- Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa

ADO\- 768407

__RN29__

__Campo 29 – Valor Outros__

__Tabela: __SAFX342

__Item: 29__

__Nome do Campo:__ VLR\_OUTROS

__Descrição: __Valor de outras despesas que devam ser utilizadas na geração da guia

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor de outras despesas que devam ser utilizadas na geração da guia "Extra Apuração"

MFS\- 768407

__RN30__

__Campo 30 – Valor da base de Cálculo__

__Tabela: __SAFX342

__Item: 30__

__Nome do Campo:__ VLR\_VASE\_CALC

__Descrição: __Valor de base de cálculo\. Utilizado nas guias que utilizam deste valor para calcular o valor da guia

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o valor de base de cálculo\. Utilizado nas guias que utilizam deste valor para calcular o valor da guia "Extra Apuração"

MFS\- 768407

__RN31__

__Campo 31 – Campos Extras__

__Tabela: __SAFX342

__Item: 31__

__Nome do Campo:__ CAMPOS\_EXTRAS

__Descrição: __Utilizado para enviar um JSON com campos adicionais

__Tipo:__ C

__Tamanho: __\-

__Campo Não Obrigatório__

__Comentário:__

Utilizado para enviar um JSON com campos adicionais

MFS\- 768407

__RN32__

__Campo 32 – Grupo do Imposto__

__Tabela: __SAFX342

__Item: 32__

__Nome do Campo:__ GRUPO\_IMPOSTO

__Descrição__: Informar o grupo de imposto selecionado para a geração da guia de acordo com os impostos 

__Tipo:__ C

__Tamanho: 30__

__Campo Obrigatório__

O preenchimento esperado para este campo é "Extra Apuração"\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913303

MFS\- 768407

__RN33__

__Campo 33 – Usuário__

__Tabela: __SAFX342

__Item: 33__

__Nome do Campo:__ USUARIO

__Descrição: __Informa o usuário

__Tipo: __C

__Tamanho: __100

__Campo Obrigatório__

__Comentário: __

Este campo é obrigatório e deve ser preenchido com o nome ou identificação válida do usuário existente no Tax One\.

Exibir a mensagem da TFIX 22 CÓDIGO 913304

MFS\- 768407

__RN34__

__Campo 34 – Status__

__Tabela: __SAFX342

__Item: 34__

__Nome do Campo:__ STATUS

__Descrição: __Informa o status de guias__ __

__Tipo:__ N

__Tamanho: __003

__Campo Obrigatório__

__Comentário: __

Este campo deve ser preenchido exclusivamente com o valor 'Aguardando Envio'\.

Exibir a mensagem da TFIX 22 CÓDIGO 913305

MFS\- 768407

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

