# MTZ_Carga_Importacao_Contabilizacao_SAFX_347-Retorno de Dados Contabilizados Apuração – Sistema SAP

- **Fonte:** MTZ_Carga_Importacao_Contabilizacao_SAFX_347-Retorno de Dados Contabilizados Apuração – Sistema SAP.docx
- **Modificado:** 2026-02-13
- **Tamanho:** 103 KB

---

THOMSON REUTERS

  IMPORTAÇÃO \- SAFX347 \(Retorno de Dados Contabilizados Apuração – Sistema SAP\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização da Apuração

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 913154

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX 347

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

A nova SAFX 347 de Retorno será responsável por receber os dados fornecidos pelo sistema SAP via OBI, que disponibilizará informações sobre os dados contabilizados para atualização de Status, Estorno e Contabilização Automática \.

O sistema OBI irá consumir esses dados, realizar o processamento necessário e enviar as informações, através da nova SAFX de Retorno, o Tax One, onde serão utilizadas posteriormente\.

- Os dados serão atualizados com base nos __campos\-chave__:__ Empresa, Estabelecimento, Período e Número do Documento Contábil__\.

Sempre que for gerado um __número de documento contábil__, os dados serão retornados ao Tax One, Esse Retorno  proporcionará os seguintes benefícios:

- Atualização automática do __status__ no __Relatório de Status__ do Tax One para __Contabilizado__\.
- Registro do __número do documento contábil__ que originou a contabilização\.
- Disponibilização dos dados necessários para:
	- __Geração de estornos__
	- Criação de um __fluxo de contabilização automática__

__Localização: __

__             Módulo: __Básicos > Guias de Pagamentos

__                 Menu:__ Guias de Pagamentos 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX 347 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para Importação da SAFX

__A importação da SAFX deve atender às seguintes premissas:__

- Todos os campos obrigatórios e chaves devem estar preenchidos corretamente\.
- O processo deve identificar e atualizar o status da guia de forma precisa\.

__Resultado da Importação__

Se a importação for bem\-sucedida, os dados serão registrados nas seguintes telas:

- Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Estorno
- Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Contabilização Automática
- Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Relatório de Status

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Chave de Identificação – Vide regra RN 01
- Campo Período – Vide regra RN 02
- Campo Exercício – Vide regra RN 03
- Campo Grupo de Imposto \-Vide regra RN 13
- Campo Imposto – Vide regra RN 14
- Campo Código de Ajuste \-Vide regra RN 15
- Campo Descrição de Ajuste – Vide regra RN 16
- Campo Chave de Lançamento \(Débito\) – Vide regra RN 19
- Campo Código da Conta \(Débito\) – Vide regra RN 20
- Campo Descrição da Conta \(Débito\) – Vide regra RN 21
- Campo Chave de Lançamento \(Crédito\) – Vide regra RN 28
- Campo Código da Conta \(Crédito\) – Vide regra RN 29
- Campo Descrição da Conta \(Crédito\) – Vide regra RN 30
- Campo Usuário – Vide regra RN 38

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__ADO__

RN00

__Índice__

__Nome do Campo__

__Descrição__

__Tipo__

__Tamanho__

__Obrigatório__

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

CHAVE\_ID

Chave de Rastreabilidade

A

070

SIM

\(\*\)

4

PERIODO

Periodo Mensal da apuração

A

002

SIM

\(\*\)

5

EXERCICIO

Ano da apuração

N

004

SIM

\(\*\)

6

DT\_DOCTO

Data do documento

N

008

NÃO

NÃO 

7

DT\_LANCTO

Data do lançamento

N

008

NÃO

NÃO

8

UF

Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\.

C

002

NÃO

NÃO

9

REFERENCIA

O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\. 

C

016

NÃO

NÃO

10

LOCAL\_NEGOCIO

O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\.

A

004

NÃO

NÃO

11

DIVISAO

O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\.

A

004

NÃO

NÃO

12

CENTRO

O Preenchimento é livre indica a segregação SAP

A

004

NÃO

NÃO

13

GRUPO\_IMPOSTO

Informa se o preenchimento é Federal ou Estadual\.

C

010

SIM

\(\*\)

14

IMPOSTO

Indica os tributos aplicáveis, como ICMS, ICMS\-ST, IPI, DIFAL, FCP, PIS e COFINS\.

C

020

SIM

\(\*\)

15

COD\_AJUSTE

Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-ST, IPI, DIFAL, FCP, PIS e COFINS\.

A

015

SIM

\(\*\)

16

DESCRICAO\_AJUSTE

Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS\-ST, IPI, DIFAL, FCP, PIS e COFINS\.

C

050

SIM

NÃO

17

CHAVE\_LANCTO\_D

Indica que o preenchimento é fixo com o valor '40' para transações de débito\.

N

002

SIM

NÃO

18

COD\_CONTA\_D

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

N

070

SIM

NÃO

19

DESCRICAO\_CONTA\_D

Informar a Descrição da Conta existente na SAFX2002

A

050

SIM

NÃO

20

MONTANTE\_D

Informa o valor do lançamento contábil

N

017V002

SIM

NÃO

21

CENTRO\_CUSTO\_D

Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

N

020

NÃO

NÃO

22

DESCRICAO\_CENTRO\_CUSTO\_D

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

A

050

NÃO

NÃO

23

CENTRO\_LUCRO\_D

O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

N

020

NÃO

NÃO

24

TEXTO\_D

Campo para informar o histórico de lançamento dado preenchido pelo usuário

A

020

NÃO

NÃO

25

OBSERVAÇÃO\_D

 Campo para informar o histórico de lançamento dado preenchido pelo usuário

A

020

NÃO

NÃO

26

CHAVE\_LANCTO\_C

Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\.

N

002

SIM

NÃO

27

COD\_CONTA\_C

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

N

070

SIM

NÃO

28

DESCRICAO\_CONTA\_C

Informar a Descrição da Conta existente na SAFX2002

A

050

SIM

NÃO

29

MONTANTE\_C

Informa o valor do lançamento contábil

N

017V002

SIM

NÃO

30

CENTRO\_CUSTO\_C

Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

A

020

NÃO

NÃO

31

DESCRICAO\_CENTRO\_CUSTO\_C

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

A

050

NÃO

NÃO

32

CENTRO\_LUCRO\_C

Informar o Código do Centro de Custo\.

N

020

NÃO

NÃO

33

TEXTO\_C

Campo para informar o histórico de lançamento dado preenchido pelo usuário

A

020

NÃO

NÃO

34

OBSERVACAO\_C

Campo para informar o histórico de lançamento dado preenchido pelo usuário

A

020

NÃO

NÃO

35

USUARIO

Nome do analista responsável pela contabilização

A

014

SIM

NÃO

36

NRO\_DOC\_CONTABIL

Informa o Número do Documento Contábil criado no SAP 

N

010

SIM

NÃO

 

ADO\- 913154

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 913154

__RN01__

__Campo 01 – Código da Empresa__

__Tabela: SAFX 347__

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da Empresa

__Tipo: A__

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da Empresa 

Exibir a mensagem da TFIX 22 CÓDIGO 90001

__RN02__

__Campo 02 – Código do Estabelecimento  __

__Tabela: SAFX 347__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do Estabelecimento

__Tipo:__ A

__Tamanho:__ 006

__Campo Obrigatório__

__Chave Primária __

__Comentário:__

Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário

Exibir a mensagem da TFIX 22 CÓDIGO 90002

__RN03__

__Campo 03 – Chave de Identificação__

 

__Tabela: SAFX 347__

__Item: __03

__Nome do Campo: __CHAVE\_ID

__Descrição: __Chave de Rastreabilidade

__Tipo:__ A

__Tamanho: __070

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar a Chave de Rastreabilidade 

Exibir a mensagem da TFIX 22 CÓDIGO 913331

ADO\- 913154

__RN04__

__Campo 04 \- Período__

__Tabela: SAFX 347__

__Item: __04

__Nome do Campo: __PERIODO

__Descrição: __Período Mensal da Apuração

__Tipo:__ A

__Tamanho: __002

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Período Mensal da Apuração

Exibir a mensagem da TFIX 22 CÓDIGO 913333

ADO\- 913154

__RN05__

__Campo 05 – Exercício__

__Tabela: SAFX 347__

__Item: __05

__Nome do Campo:__ EXERCICIO

__Descrição: __Ano da apuração

__Tipo:__ N

__Tamanho: __004

__Campo Obrigatório__

__Chave Primária __

__Comentário:__ 

Informar o Ano da Apuração 

Exibir a mensagem da TFIX 22 CÓDIGO 913334

ADO\- 913154

__RN06__

__Campo 06 – Data do Documento__

__Tabela: SAFX 347__

__Item: __06

__Nome do Campo:__ DT\_DOCTO

__Descrição: __Data do Documento

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__ 

Informar a Data do Documento 

ADO\- 913154

__RN07__

__Campo 07 – Data do Lançamento__

__Tabela: SAFX 347__

__Item: __07

__Nome do Campo:__ DT\_LANCTO

__Descrição: __Data do Lançamento

__Tipo:__ N

__Tamanho: __008

__Campo Não Obrigatório__

__Comentário:__

Informar a Data do Lançamento

ADO\- 913154

__RN08__

__Campo 08 – Unidade Federal __

__Tabela: SAFX 347__

__Item:__ 08

__Nome do Campo:__ UF 

__Descrição:__ Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\. 

__Tipo:__ C 

__Tamanho:__ 002 

Campo Não Obrigatório 

__Comentário__:  

Informa as UFs dos Estabelecimentos previamente selecionados\.

ADO\- 913154

__RN09__

__Campo 09 – Referência__

__Tabela: SAFX 347__

__Item:__ 09

__Nome do Campo: __REFERENCIA 

__Descrição: __O Preenchimento é livre e os dados são provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\. 

__Tipo: C__ 

__Tamanho: __016 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP\.

ADO\- 913154

__RN10__

__Campo 10 – Local de Negócio __

__Tabela: SAFX 347__

__Item:__ 10

__Nome do Campo:__ LOCAL\_NEGOCIO 

__Descrição: __O Preenchimento é livre e indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\. 

__Tipo:__ A 

__Tamanho:__ 004 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário 

ADO\- 913154

__RN11__

__Campo 11 – Divisão__

__Tabela: SAFX 347__

__Item: __11

__Nome do Campo:__ DIVISAO 

__Descrição:__ O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\. 

__Tipo: A__ 

__Tamanho:__ 004 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o código do segmento/divisão financeira conforme cadastro no SAP\. 

ADO\- 913154

__RN12__

__Campo 12 – Centro__

__Tabela: SAFX 347__

__Item: 12__

__Nome do Campo:__ CENTRO

__Descrição: __O Preenchimento é livre indica a segregação SAP 

__Tipo: A__

__Tamanho: __004

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Centro onde ocorreu a operação que deu origem ao registro\. 

ADO\- 913154

__RN13__

__Campo 13 – Grupo de Imposto__

__Tabela: SAFX 347__

__Item: __13

__Nome do Campo:__ GRUPO\_IMPOSTO 

__Descrição: __Informa se o preenchimento é Federal ou Estadual\.

__Tipo:__ C 

__Tamanho: __010 

__Campo Obrigatório__ 

__Chave Primária__ 

__Comentário:__  

Permitir ao usuário escolher entre as opções ‘Federal’ ou ‘Estadual’ 

Exibir a mensagem da TFIX 22 CÓDIGO 913312

ADO\- 913154

__RN14__

__Campo 14 – Imposto__

__Tabela: SAFX 347__

__Item: 14__

__Nome do Campo:__ IMPOSTO 

__Descrição: __Indica os tributos aplicáveis, como ICMS, ICMS\-ST, IPI, DIFAL, FCP, PIS e COFINS\.

__Tipo:__ C 

__Tamanho: __020 

__Campo Obrigatório__ 

__Chave Primária__ 

__Comentário:__ 

Este campo informa os tributos que compõem o campo GRUPO\_IMPOSTO \(RN04\), sendo eles, de âmbito Federal: PIS/PASEP\-Cumulativo, PIS/PASEP\-Não Cumulativo, COFINS\- Cumulativo, COFINS\-Não Cumulativo, IPI\. E de âmbito Estadual: ICMS\- Próprio, ICMS\-ST, ICMS\-Antecipado, FCP, DIFAL, SCANC 

Exibir a mensagem da TFIX 22 CÓDIGO 913313

ADO\- 913154

__RN15__

__Campo 15 – Código de Ajuste__

__Tabela: SAFX 347__

__Item: 15__

__Nome do Campo:__ COD\_AJUSTE 

__Descrição: __Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\.  

__Tipo:__ A

__Tamanho: __015

__Campo Obrigatório__ 

__Chave Primária__ 

__Comentário:__ 

Ao selecionar o Grupo de Imposto \(Federal e Estadual\) — ICMS\-Próprio, ICMS\-Antecipado, ICMS\-ST, DIFAL, FCP, IPI, PIS \(Cumulativo e Não Cumulativo\), COFINS \(Cumulativo e Não Cumulativo\) e SCANC — o sistema deve: \(1\) identificar o "Imposto Relacionado"; \(2\) consultar a tabela de ajustes correspondente ao tributo \(para ICMS/DIFAL/FCP/ICMS\-ST usar ICT\_AJUSTE\_ICMS; para IPI/PIS/COFINS/SCANC usar a tabela própria do tributo\); \(3\) recuperar os campos de código e descrição do ajuste; e \(4\) concatenar esses valores para preencher automaticamente o campo "Código de Ajuste"\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913314

__RN16__

__Campo 16 – Descrição de Ajuste__

__Tabela: SAFX 347__

__Item: 16__

__Nome do Campo:__ DESCRICAO\_AJUSTE 

__Descrição: __Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS\-ST, IPI, DIFAL, FCP, PIS e COFINS\.

__Tipo:__ C 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Este campo deve ser concatenado ao campo COD\_AJUSTE \(RN10\) e informa ao usuário a descrição referente ao código de ajuste, conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS 

Exibir a mensagem da TFIX 22 CÓDIGO 913315

__RN17__

__Campo 17 – Chave de Lançamento \(Débito\) __

__Tabela: SAFX 347__

__Item: 17__

__Nome do Campo:__ CHAVE\_LANCTO\_D 

__Descrição: __Indica que o preenchimento é fixo com o valor '40' para transações de débito\. 

__Tipo:__ N 

__Tamanho: __002 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito 

Exibir a mensagem da TFIX 22 CÓDIGO 913321 

ADO\- 913154

__RN18__

__Campo 18 – Código da Conta \(Débito\)__

__Tabela: SAFX 347__

__Item: 18__

__Nome do Campo:__ COD\_CONTA\_D 

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

__Tipo:__ N

__Tamanho: __070 

__Campo Obrigatório__ 

__Comentário:__ 

Informar o Código da Conta e Subconta \(referente a operações de Débito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\) 

Exibir a mensagem da TFIX 22 CÓDIGO 913322

ADO\- 913154

__RN19__

__Campo 19 – Descrição da Conta \(Débito\) __

__Tabela: SAFX 347__

__Item: 19__

__Nome do Campo:__ DESCRICAO\_CONTA\_D 

__Descrição: __Informar a Descrição da Conta existente na SAFX2002 

__Tipo:__ A 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a Descrição da Conta \(referente a operações de Débito\) existente na SAFX2002 

Exibir a mensagem da TFIX 22 CÓDIGO 913323

ADO\- 913154

__RN20__

__Campo 20 – Montante \(Débito\)__

__Tabela: SAFX 347__

__Item: 20__

__Nome do Campo:__ MONTANTE\_D

__Descrição: __Informa o valor do lançamento contábil

__Tipo:__ N

__Tamanho: __017V002

__Campo Obrigatório__

__Comentário:__

Informar o Valor do Lançamento Contábil para transações de Débito

ADO\- 913154

__RN21__

__Campo 21 – Centro de Custo \(Débito\)__

__Tabela: SAFX 347__

__Item: 21__

__Nome do Campo:__ CENTRO\_CUSTO\_D 

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\. 

__Tipo:__ N 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Custo \(referente a operações de Débito\), conforme registro prévio na Tabela de Centro de Custos da SAFX2003

ADO\- 913154

__RN22__

__Campo 22 – Descrição do Centro de Custo \(Débito\)__

__Tabela: SAFX 347__

__Item: 22__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_D 

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\. 

__Tipo:__ A 

__Tamanho: __050 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar a Descrição do Centro de Custo \(referente a operações de Débito\) conforme registro prévio na SAFX2003 

ADO\- 913154

__RN23__

__Campo 23 – Centro de Lucro \(Débito\)__

__Tabela: SAFX 347__

__Item: 23__

__Nome do Campo:__ CENTRO\_LUCRO\_D 

__Descrição: __O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

__Tipo:__ N 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Lucro \(referente a operações de Débito\), este campo é opcional e serve apenas para controle interno\. 

ADO\- 913154

__RN24__

__Campo 24 – Texto do Histórico \(Débito\) __

__Tabela: SAFX 347__

__Item: 24__

__Nome do Campo:__ TEXTO\_D 

__Descrição: __Campo para informar o histórico de lançamento dado preenchido pelo usuário

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__  

__Comentário:__ 

Informar o histórico de lançamento dado preenchido pelo usuário para transações de débito

ADO\- 913154

__RN25__

__Campo 25 – Observação \(Débito\)__

__Tabela: SAFX 347__

__Item: 25__

__Nome do Campo:__ OBSERVAÇÃO\_D 

__Descrição: __Registrar a observação referente ao lançamento\. 

__Tipo:__ A 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito

ADO\- 913154

__RN26__

__Campo 26 – Chave de Lançamento \(Crédito\) __

__Tabela: SAFX 347__

__Item: 26__

__Nome do Campo:__ CHAVE\_LANCTO\_C 

__Descrição: __Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\. 

__Tipo:__ N 

__Tamanho: __002 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito 

Exibir a mensagem da TFIX 22 CÓDIGO 913326 

ADO\- 913154

__RN27__

__Campo 27 – Código da Conta \(Crédito\) __

__Tabela: SAFX 347__

__Item: 27__

__Nome do Campo:__ COD\_CONTA\_C 

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.__ __ 

__Tipo:__ N 

__Tamanho: __070 

__Campo Obrigatório__ 

__Comentário:__ 

Informar o Código da Conta e Subconta \(referente a operações de Crédito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913327

ADO\- 913154

__RN28__

__Campo 28 – Descrição da Conta \(Crédito\)__

__Tabela: SAFX 347__

__Item: 28__

__Nome do Campo:__ DESCRICAO\_CONTA\_C 

__Descrição: __Informar a Descrição da Conta existente na SAFX2002 

__Tipo:__ A 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a Descrição da Conta \(referente a operações de Crédito\) existente na SAFX2002 

Exibir a mensagem da TFIX 22 CÓDIGO 913328 

ADO\- 913154

__RN29__

__Campo 29 – Montante \(Crédito\)__

__Tabela: SAFX__

__Item: 29__

__Nome do Campo:__ MONTANTE\_C

__Descrição: __Informa o valor do lançamento contábil 

__Tipo:__ N

__Tamanho: 017V002__

__Campo Obrigatório__

__Comentário:__

Informar o valor do lançamento contábil para transações de Crédito

ADO\- 913154

__RN30__

__Campo 30 – Centro de Custo \(Crédito\)__

__Tabela: SAFX 347__

__Item: 30__

__Nome do Campo:__ CENTRO\_CUSTO\_C 

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ N 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Custo \(referente a operações de Crédito\), que deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

ADO\- 913154

__RN31__

__Campo 31 – Descrição do Centro de Custo \(Crédito\)__

__Tabela: SAFX 347__

__Item: 31__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_C 

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ A

__Tamanho: 050__

__Campo Não Obrigatório__

__Comentário:__

Informar a Descrição do Centro de Custo \(referente a operações de Crédito\) conforme registro prévio na SAFX2003

ADO\- 913154

__RN32__

__Campo 32 – Centro de Lucro \(Crédito\)__

__Tabela: SAFX__

__Item: 32__

__Nome do Campo:__ CENTRO\_LUCRO\_C

__Descrição: __Informar o Código do Centro de Custo\.

__Tipo:__ N

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Crédito\), este campo é opcional e serve apenas para controle interno

__RN33__

__Campo 33 – Texto do Histórico \(Crédito\) __

__Tabela: SAFX 347__

__Item: 33__

__Nome do Campo:__ TEXTO\_C

__Descrição: __Campo para informar o histórico de lançamento dado preenchido pelo usuário

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o histórico de lançamento dado preenchido pelo usuário para transações de crédito

__RN34__

__Campo 34 – Observação \(Crédito\) __

__Tabela: SAFX 347__

__Item: 34__

__Nome do Campo:__ OBSERVACAO\_C

__Descrição: __Registrar a observação referente ao lançamento\. 

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito

__RN35__

__Campo 35 – Usuário__

__Tabela: SAFX 347__

__Item: 35__

__Nome do Campo:__ USUARIO

__Descrição: __Nome do analista responsável pela contabilização

__Tipo:__ A

__Tamanho: 014__

__Campo Obrigatório__ 

__Comentário:__ 

Informar o login do usuário responsável pela gravação dos dados\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913304 

__RN36__

__Campo 36 – Número do Documento Contábil__

__Tabela: SAFX 347__

__Item: 36__

__Nome do Campo:__ NRO\_DOC\_CONTABIL

__Descrição: __Informa o Número do Documento Contábil criado no SAP\. __ __

__Tipo:__ N

__Tamanho: 010__

__Campo Obrigatório__ 

__Comentário:__ 

Informa o Número do Documento Contábil criado no SAP\.  

Exibir a mensagem da TFIX 22 CÓDIGO 913358

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

