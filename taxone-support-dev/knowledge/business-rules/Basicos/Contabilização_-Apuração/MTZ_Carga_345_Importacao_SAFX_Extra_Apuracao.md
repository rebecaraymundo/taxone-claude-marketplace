# MTZ_Carga_345_Importacao_SAFX_Extra_Apuracao

- **Fonte:** MTZ_Carga_345_Importacao_SAFX_Extra_Apuracao.docx
- **Modificado:** 2026-02-24
- **Tamanho:** 109 KB

---

THOMSON REUTERS

Contabilização da Apuração – IMPORTAÇÃO \- SAFX345 \(Integração – Contabilização – Extra Apuração\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização > Relatório de Status

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 768407

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX345 \.

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

A tabela SAFX 345 foi desenvolvida especificamente para carregar informações relacionadas aos impostos de contabilização de extra apuração\. O principal objetivo desta tabela é viabilizar o correto processo de contabilização no sistema SAP, contemplando os impostos do grupo de impostos "Extras Apurações", tanto em âmbito estadual, em alinhamento com as parametrizações contábeis já existentes no módulo de Contabilização do Tax One\.

Com isso, a SAFX 345 passa a ser o repositório específico para os lançamentos de extra apuração que envolvem contabilização, assegurando que todas as informações necessárias estejam disponíveis para o SAP com o detalhamento exigido pelos processos fiscais e contábeis, reduzindo falhas de parametrização, evitando ausência de dados para determinados impostos e mantendo a consistência entre o Tax One, os livros fiscais e o sistema SAP\.

# Localização:

__             Módulo: __Básicos > Job Servidor

__                 Menu: __Carga__ __> Programação > Execução

__                        __Importação > Programação > Execução     

                                     Importação batch > Programação > Execução

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX 345 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para a Importação da SAFX:

A importação da SAFX deve seguir as seguintes premissas de negócio e comportamentos:

- No campo __Grupo de Imposto__, considerar sempre "Extra Apuração"\. Essa informação é exclusivamente para retornar os impostos importados via SAFX\.
- Layout e fontes de dados: o arquivo deve obedecer ao Manual de Layout SAFX 345 e às estruturas de referência utilizadas pelo sistema: SAFX2002 \(Plano de Contas\), SAFX2003 \(Centro de Custo\)\.

__Resultado da Importação:__

Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:

- __Módulo: Manutenção > Contabilização da Apuração > Tela de Geração, Tela de Status, Relatório de Status__
- __Menu: Acesso Principal >> Relatório de Status__

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Chave de Identificação – Vide regra RN01
- Campo Grupo de Imposto – Vide regra RN 02
- Campo Imposto – Vide regra RN 03
- Campo Período – Vide regra RN 07
- Campo Exercício – Vide regra RN 08
- Campo Código de Ajuste – Vide regra 13
- Campo Descrição de Ajuste – Vide regra 14
- Campo Usuário – Vide regra 36
- Campo CNPJ – Vide regra 38

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

Campo destinado ao código da Empresa\. Vide regra RN00 

A

003

SIM

\(\*\)

2

COD\_ESTABELECIMENTO 

Campo destinado ao código do Estabelecimento\. Vide regra RN01 

A

006

SIM

\(\*\)

3

CHAVE\_ID 

Chave de Rastreabilidade 

A

050

SIM

\(\*\)

4

GRUPO\_IMPOSTO 

Informar o preenchimento é de âmbito Federal ou Estadual\. Vide regra RN03 

C

010

SIM

\(\*\)

5

IMPOSTO 

Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\. Vide regra RN04 

C

020

SIM

\(\*\)

6

UF 

Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\.  

C

002

NÃO

NÃO

7

PERIODO 

Informa o mês correspondente apuração 

A

002

SIM

\(\*\)

8

EXERCICIO 

Informa o Ano da apuração 

N

004

SIM

\(\*\)

9

REFERENCIA 

O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\.  

C

016

NÃO

NÃO

10

LOCAL\_NEGÓCIO 

O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\. 

A

004

NÃO

NÃO

11

DIVISÃO 

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

COD\_AJUSTE 

Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\.  

A

015

SIM

\(\*\)

14

DESCRICAO\_AJUSTE 

Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\.  

C

050

SIM

NÃO

15

CHAVE\_LANCTO\_D 

Indica que o preenchimento é fixo com o valor '40' para transações de débito\. 

N

002

SIM

NÃO

16

COD\_CONTA\_D 

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

N

070

SIM

NÃO

17

DESCRICAO\_CONTA\_D 

Informar a Descrição da Conta existente na SAFX2002 

A

050

SIM

NÃO

18

MONTANTE\_D 

Informa o valor do lançamento contábil 

N

011V002

SIM

NÃO

19

CENTRO\_CUSTO\_D 

Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\. 

N

020

NÃO

NÃO

20

DESCRICAO\_CENTRO\_CUSTO\_D 

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\. 

A

050

NÃO

NÃO

21

CENTRO\_LUCRO\_D 

O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\. 

N

020

NÃO

NÃO

22

TEXTO\_D 

Campo para informar o histórico de lançamento dado preenchido pelo usuário 

A

020

NÃO

NÃO

23

OBSERVAÇÃO\_D 

Registrar a observação referente ao lançamento\. 

A

020

NÃO

NÃO

24

CHAVE\_LANCTO\_C 

Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\. 

N

002

SIM

NÃO

25

COD\_CONTA\_C 

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

N

070

SIM

NÃO

26

DESCRICAO\_CONTA\_C 

Informar a Descrição da Conta existente na SAFX2002 

A

050

SIM

NÃO

27

MONTANTE\_C 

Informa o valor do lançamento contábil 

N

011V002

SIM

NÃO

28

CENTRO\_CUSTO\_C 

Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\. 

A

050

NÃO

NÃO

29

DESCRICAO\_CENTRO\_CUSTO\_C 

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\. 

A

050

NÃO

NÃO

30

CENTRO\_LUCRO\_C 

Informar o Código do Centro de Lucro\. 

N

020

NÃO

NÃO

31

TEXTO\_C 

Campo para informar o histórico de lançamento dado preenchido pelo usuário 

A

020 

NÃO

NÃO

32

OBSERVACAO\_C 

Registrar a observação referente ao lançamento\. 

A

020 

NÃO

NÃO

33

USUARIO 

Informar o login do usuário responsável pela gravação dos dados\. 

A

014

SIM

NÃO

34

CNPJ 

Controle interno informar CNPJ Do estabelecimento para lançamento contábil 

A

014

SIM

NÃO

35

DT\_DOCTO

Data do lançamento Contábil

N

008

NÃO

NÃO

36

DT\_LANCTO

Data do documento

N

008

NÃO

NÃO

 

ADO\- 768407

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 768407

__RN01__

__Campo 01 – Código da Empresa__

__Tabela: __SAFX 345

__Item: __04

__Nome do Campo:__ COD\_EMPRESA

__Descrição: __Campo destinado ao código da Empresa\.

__Tipo:__ A

__RN02__

__Campo 02 – Código do Estabelecimento__

__Tabela: __SAFX 345

__Item: __05

__Nome do Campo:__ COD\_ESTABELECIMENTO

__Descrição: __Campo destinado ao código do Estabelecimento\.

__Tipo:__ A

__Tamanho: __006

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do Estabelecimento

Exibir a mensagem da TFIX 22 CÓDIGO 90002

__RN03__

__Campo 03 – Chave de Identificação__

 

__Tabela: __SAFX 345

__Item: __01

__Nome do Campo: __CHAVE\_ID

__Descrição: __Chave de Rastreabilidade

__Tipo:__ A

__Tamanho: __050

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar a Chave de Rastreabilidade

Exibir a mensagem da TFIX 22 CÓDIGO 913331

ADO\- 768407

__RN04__

__Campo 04– Grupo de Imposto__

__Tabela:__ SAFX 345

__Item: __02

__Nome do Campo: __GRUPO\_IMPOSTO

__Descrição: __Informar o preenchimento é de  Extra Apur

__Tipo:__ C

__Tamanho: __010

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa descrição Extra\_ Apur

Exibir a mensagem da TFIX 22 CÓDIGO 913359

 

ADO\- 768407

__RN05__

__Campo 05 – Imposto__

__Tabela: __SAFX 345

__Item: __03

__Nome do Campo:__ IMPOSTO

__Descrição: __Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\.

__Tipo:__ C

__Tamanho: __020

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo preencher como ICMS\-ST

Exibir a mensagem da TFIX 22 CÓDIGO 913332

ADO\- 768407

ADO\- 768407

__RN06__

__Campo 06 – Unidade Federal__

__Tabela: __SAFX 345

__Item: __06

__Nome do Campo: __UF

__Descrição: __Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\.  

__Tipo: C__

__Tamanho: __002

__Campo Não Obrigatório__

__Comentário:__

Informa as UFs dos Estabelecimentos previamente selecionados

ADO\- 768407

__RN07__

__Campo 07 – Período__

__Tabela: __SAFX 345

__Item: __07

__Nome do Campo: __PERIODO

__Descrição: __Informa o mês correspondente apuração 

__Tipo:__ A

__Tamanho:__ 002

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o mês correspondente à Apuração

Exibir a mensagem da TFIX 22 CÓDIGO 913333

ADO\- 768407

__RN08__

__Campo 08 – Exercício__

__Tabela: __SAFX 345

__Item: __08

__Nome do Campo:__ EXERCICIO

__Descrição:__ Informa o ano da apuração

__Tipo: N__

__Tamanho:__ 004

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o ano da apuração

Exibir a mensagem da TFIX 22 CÓDIGO 913334

ADO\- 768407

__RN09__

__Campo 09 – Referência__

__Tabela:__ SAFX 345

__Item:__ 09

__Nome do Campo:__ REFERENCIA

__Descrição:__ O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\.  

__Tipo: __C

__Tamanho: __016

__Campo NÃO OBRIGATÓRIO__

__Comentário:__

Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP\.

ADO\- 768407

__RN10__

__Campo 10 – Local de Negócio __

__Tabela:__ SAFX 345

__Item:__ 10

__Nome do Campo:__ LOCAL\_NEGOCIO

__Descrição: __O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\. 

__Tipo:__ A

__Tamanho: __004

__Campo Não Obrigatório__

__Comentário:__

Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário 

ADO\- 768407

__RN11__

__Campo 11 – Divisão__

__Tabela: __SAFX 345

__Item: __11

__Nome do Campo:__ DIVISAO

__Descrição: __O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\. 

__Tipo: A__ 

__Tamanho:__ 004 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o código do segmento/divisão financeira conforme cadastro no SAP\. 

ADO\- 768407

__RN12__

__Campo 12 – Centro__

__Tabela: __SAFX 345

__Item: __12

__Nome do Campo:__ CENTRO

__Descrição: __O Preenchimento é livre indica a segregação SAP 

__Tipo: A__

__Tamanho: __004

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Centro onde ocorreu a operação que deu origem ao registro\. 

ADO\- 768407

__RN13__

__Campo 13 – Código de Ajuste__

__Tabela: __SAFX 345

__Item: __13

__Nome do Campo:__ COD\_AJUSTE

__Descrição: __Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP

__Tipo:__ A

__Tamanho: __015

__Campo Obrigatório__ 

__Chave Primária__ 

__Comentário:__ 

Ao selecionar o Grupo de Imposto \(Federal e Estadual\) — ICMS\-Próprio, IPI— o sistema deve: \(1\) identificar o "Imposto Relacionado"; \(2\) consultar a tabela de ajustes correspondente ao tributo \(para ICMS/DIFAL/FCP/ICMS\-ST usar ICT\_AJUSTE\_ICMS; para IPI usar a tabela própria do tributo\); \(3\) recuperar os campos de código e descrição do ajuste; e \(4\) concatenar esses valores para preencher automaticamente o campo "Código de Ajuste"\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913335

ADO\- 768407

__RN14__

__Campo 14 – Descrição do Ajuste__

__Tabela: __SAFX 345

__Item: __14

__Nome do Campo:__ DESCRICAO\_AJUSTE

__Descrição: __DESCRICAO\_AJUSTE 

__Descrição: __Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS\-ST, IPI, DIFAL, FCP\.

__Tipo:__ C 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Este campo deve ser concatenado ao campo COD\_AJUSTE \(RN10\) e informa ao usuário a descrição referente ao código de ajuste, conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI

Exibir a mensagem da TFIX 22 CÓDIGO 913315

ADO\- 768407

__RN15__

__Campo 15 – Chave de Lançamento \(Débito\)__

__Tabela: __SAFX 345

__Item: 15__

__Nome do Campo:__ CHAVE\_LANCTO\_D 

__Descrição: __Indica que o preenchimento é fixo com o valor '40' para transações de débito\. 

__Tipo:__ N 

__Tamanho: __002 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito 

Exibir a mensagem da TFIX 22 CÓDIGO 913321 

ADO\- 768407

__RN16__

__Campo 16 – Código da Conta \(Débito\)__

__Tabela: __SAFX 345

__Item: 16__

__Nome do Campo:__ COD\_CONTA\_D 

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

__Tipo:__ N

__Tamanho: __070 

__Campo Obrigatório__ 

__Comentário:__ 

Informar o Código da Conta e Subconta \(referente a operações de Débito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\) 

Exibir a mensagem da TFIX 22 CÓDIGO 913322

ADO\- 768407

__RN17__

__Campo 17 – Descrição da Conta \(Débito\)__

__Tabela: __SAFX 345

__Item: 17__

__Nome do Campo:__ DESCRICAO\_CONTA\_D 

__Descrição: __Informar a Descrição da Conta existente na SAFX2002 

__Tipo:__ A 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a Descrição da Conta \(referente a operações de Débito\) existente na SAFX2002 

Exibir a mensagem da TFIX 22 CÓDIGO 913323

ADO\- 768407

__RN18__

__Campo 18 – Montante \(Débito\)__

__Tabela: __SAFX

__Item: 18__

__Nome do Campo:__ MONTANTE\_D

__Descrição: __Informa o valor do lançamento contábil

__Tipo:__ N

__Tamanho: __011V002

__Campo Obrigatório__

__Comentário:__

Informar o Valor do Lançamento Contábil para transações de Débito

Exibir a mensagem da TFIX 22 CÓDIGO 913336

ADO\- 768407

__RN19__

__Campo 19 – Centro de Custo \(Débito\)__

__Tabela: __SAFX 345

__Item: 19__

__Nome do Campo:__ CENTRO\_CUSTO\_D 

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\. 

__Tipo:__ N 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Custo \(referente a operações de Débito\), conforme registro prévio na Tabela de Centro de Custos da SAFX2003

ADO\- 768407

__RN20__

__Campo 20 – Descrição do Centro de Custo \(Débito\)__

__Tabela: __SAFX 345

__Item: 20__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_D 

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\. 

__Tipo:__ A 

__Tamanho: __050 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar a Descrição do Centro de Custo \(referente a operações de Débito\) conforme registro prévio na SAFX2003 

ADO\- 768407

__RN21__

__Campo 21 – Centro de Lucro \(Débito\)__

__Tabela: __SAFX 345

__Item: 21__

__Nome do Campo:__ CENTRO\_LUCRO\_D

__Descrição: __O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

__Tipo:__ N 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Lucro \(referente a operações de Débito\), este campo é opcional e serve apenas para controle interno\. 

ADO\- 768407

__RN22__

__Campo 22 – Texto do Histórico \(Débito\) __

__Tabela: SAFX__ 345

__Item: 22__

__Nome do Campo:__ TEXTO\_D 

__Descrição: __Campo para informar o histórico de lançamento dado preenchido pelo usuário

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__  

__Comentário:__ 

Informar o histórico de lançamento dado preenchido pelo usuário para transações de débito

ADO\- 768407

__RN23__

__Campo 23 – Observação \(Débito\)__

__Tabela: SAFX__ 345

__Item: 23__

__Nome do Campo:__ OBSERVAÇÃO\_D 

__Descrição: __Registrar a observação referente ao lançamento\. 

__Tipo:__ A 

__Tamanho: __020 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito

ADO\- 768407

__RN24__

__Campo 24 – Chave de Lançamento \(Crédito\) __

__Tabela: SAFX__ 345

__Item: 24__

__Nome do Campo:__ CHAVE\_LANCTO\_C 

__Descrição: __Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\. 

__Tipo:__ N 

__Tamanho: __002 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito 

Exibir a mensagem da TFIX 22 CÓDIGO 913326 

ADO\- 768407

__RN25__

__Campo 25 – Código da Conta \(Crédito\) __

__Tabela: SAFX__ 345

__Item: 25__

__Nome do Campo:__ COD\_CONTA\_C 

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.__ __ 

__Tipo:__ N 

__Tamanho: __070 

__Campo Obrigatório__ 

__Comentário:__ 

Informar o Código da Conta e Subconta \(referente a operações de Crédito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913327

ADO\- 768407

__RN26__

__Campo 26 – Descrição da Conta \(Crédito\)__

__Tabela: SAFX__ 345

__Item: 26__

__Nome do Campo:__ DESCRICAO\_CONTA\_C 

__Descrição: __Informar a Descrição da Conta existente na SAFX2002 

__Tipo:__ A 

__Tamanho: __050 

__Campo Obrigatório__ 

__Comentário:__ 

Informar a Descrição da Conta \(referente a operações de Crédito\) existente na SAFX2002 

Exibir a mensagem da TFIX 22 CÓDIGO 913328 

ADO\- 768407

__RN27__

__Campo 27 – Montante \(Crédito\)__

__Tabela: SAFX__ 345

__Item: 27__

__Nome do Campo:__ MONTANTE\_C

__Descrição: __Informa o valor do lançamento contábil 

__Tipo:__ N

__Tamanho: 011V002__

__Campo Obrigatório__

__Comentário:__

Informar o valor do lançamento contábil para transações de Crédito

Exibir a mensagem da TFIX 22 CÓDIGO 913337

ADO\- 768407

__RN28__

__Campo 28 – Centro de Custo \(Crédito\)__

__Tabela: SAFX__ 345

__Item: 28__

__Nome do Campo:__ CENTRO\_CUSTO\_C 

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ A 

__Tamanho: __050 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o Código do Centro de Custo \(referente a operações de Crédito\), que deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

ADO\- 768407

__RN29__

__Campo 29 – Descrição do Centro de Custo \(Crédito\)__

__Tabela: SAFX__ 345

__Item: 29__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_C 

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ A

__Tamanho: 050__

__Campo Não Obrigatório__

__Comentário:__

Informar a Descrição do Centro de Custo \(referente a operações de Crédito\) conforme registro prévio na SAFX2003

ADO\- 768407

__RN30__

__Campo 30 – Centro de Lucro \(Crédito\)__

__Tabela: SAFX__ 345

__Item: 30__

__Nome do Campo:__ CENTRO\_LUCRO\_C

__Descrição: __Informar o Código do Centro de Custo\.

__Tipo:__ N

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Crédito\), este campo é opcional e serve apenas para controle interno

ADO\- 768407

__RN31__

__Campo 31 – Texto do Histórico \(Crédito\) __

__Tabela: SAFX__ 345

__Item: 31__

__Nome do Campo:__ TEXTO\_C

__Descrição: __Campo para informar o histórico de lançamento dado preenchido pelo usuário

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar o histórico de lançamento dado preenchido pelo usuário para transações de crédito

ADO\- 768407

__RN32__

__Campo 32 – Observação \(Crédito\) __

__Tabela: SAFX__ 345

__Item: 32__

__Nome do Campo:__ OBSERVACAO\_C

__Descrição: __Registrar a observação referente ao lançamento\. 

__Tipo:__ A 

__Tamanho: 020__ 

__Campo Não Obrigatório__ 

__Comentário:__ 

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito

ADO\- 768407

__RN33__

__Campo 33 – Usuário__

__Tabela: SAFX__ 345

__Item: 33__

__Nome do Campo:__ USUARIO

__Descrição: __Nome do analista responsável pela contabilização

__Tipo:__ A

__Tamanho: 014__

__Campo Obrigatório__ 

__Comentário:__ 

Informar o login do usuário responsável pela gravação dos dados\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913304 

ADO\- 768407

__RN34__

__Campo 34 – CNPJ__

__Tabela: __SAFX 345

__Item: 34__

__Nome do Campo:__ CNPJ

__Descrição: __Controle interno \- informar o CNPJ do estabelecimento para lançamento contábil 

__Tipo:__ A

__Tamanho: 014__

__Campo Obrigatório__

__Comentário: __

Informar CNPJ do Estabelecimento para Lançamento Contábil

Exibir a mensagem da TFIX 22 CÓDIGO 913338

ADO\- 768407

__RN35__

__Campo 35 – DT\_DOCTO__

__Tabela: __SAFX 345

__Item: 35__

__Nome do Campo:__ DT\_DOCTO

__Descrição: __

__Tipo:__ N

__Tamanho: 008__

__Campo Não Obrigatório__ 

__Comentário: __Data do lançamento Contábil informado pelo usuário

ADO\- 768407

__RN36__

__Campo 36 – DT\_LANCTO__

__Tabela: __SAFX 345

__Item: 36__

__Nome do Campo:__ DT\_LANCTO

__Descrição: __

__Tipo:__ N

__Tamanho: 008__

__Campo Não Obrigatório__ 

__Comentário: __Data do documento contábil informado pelo usuário

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

