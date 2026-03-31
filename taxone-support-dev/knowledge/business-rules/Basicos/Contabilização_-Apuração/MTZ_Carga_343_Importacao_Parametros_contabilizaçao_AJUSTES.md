# MTZ_Carga_343_ Importacao_Parametros_contabilizaçao_AJUSTES

- **Fonte:** MTZ_Carga_343_ Importacao_Parametros_contabilizaçao_AJUSTES.docx
- **Modificado:** 2026-01-16
- **Tamanho:** 103 KB

---

THOMSON REUTERS

 TAX PAYMENTS – IMPORTAÇÃO \- SAFX343 \(Integração de Contabilização – Parâmetros – Ajustes de Apurações Contábeis\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Ajustes da Apuração

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 973613

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX343

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

Implantar uma interface de parametrização na SAFX343 que permita ao usuário configurar, validar e manter os códigos de ajuste de apuração de tributos \(ICMS, ICMS Antecipado, ICMS\-ST, IPI, PIS/COFINS e SCANC\) por âmbito Federal/Estadual, viabilizando, ao término da apuração, a associação automática e consistente desses ajustes às contas contábeis e centros correspondentes\.

__Localização:__

- __Agrupamentos: Básico >> Job Servidor__
- __   Menu: __Carga__ __> Programação > Execução 
- __                        __Importação > Programação > Execução      
-                                      Importação batch > Programação > Execução 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX343 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para a Importação da SAFX343:

A importação da SAFX343 deve seguir as seguintes premissas de negócio e comportamentos:

- Layout e fontes de dados: o arquivo deve obedecer ao Manual de Layout SAFX\(inserir número\) e às estruturas de referência utilizadas pelo sistema: SAFX2002 \(Plano de Contas\), SAFX2003 \(Centro de Custo\) \), SAFX2006 \(Natureza da Operação\) e SAFX147 \(Operação de Crédito\)\.

__Resultado da Importação:__

Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:

- __Módulo: Manutenção >> Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Ajustes da Apuração __
- __Menu: Acesso Principal >> Parâmetros__

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Grupo de Imposto \-Vide regra RN04
- Campo Imposto – Vide regra RN05
- Campo Código de Ajuste \-Vide regra RN10
- Campo Descrição de Ajuste – Vide regra RN 11
- Campo Indicador de Situação – Vide regra RN 12
- Campo Indicador de Natureza – Vide regra RN 13
- Campo Código da Conta \(Débito\) – Vide regra RN 14
- Campo Descrição da Conta \(Débito\) – Vide regra RN 15
- Campo Chave de Lançamento \(Débito\) – Vide regra RN 16
- Campo Código da Conta \(Crédito\) – Vide regra RN 22
- Campo Chave de Lançamento \(Crédito\) – Vide regra RN 24
- Campo Usuário – Vide regra RN 30

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

UF

Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\. 

C

002

NÃO

NÃO

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

030

SIM

\(\*\)

6

REFERENCIA

O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\. 

C

016

NÃO

NÃO

7

LOCAL\_NEGOCIO

O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\.

A

004

NÃO

NÃO

8

DIVISAO

O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\.

A

004

NÃO

NÃO

9

CENTRO

O Preenchimento é livre indica a segregação SAP

A

004

NÃO

NÃO

10

COD\_AJUSTE

Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\. Vide regra RN06

A

015

SIM

\(\*\)

11

DESCRICAO\_AJUSTE

Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\. Vide regra RN06

C

050

SIM

NÃO

12

CHAVE\_LANCTO\_D

Indica que o preenchimento é fixo com o valor '40' para transações de débito\.

N

002

SIM

NÃO

13

COD\_CONTA\_D

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

A

070

SIM

NÃO

14

DESCRICAO\_CONTA\_D

Informar a Descrição da Conta existente na SAFX2002

A

050

SIM

NÃO

15

IND\_SITUACAO\_D

Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

A

001

SIM

NÃO

16

IND\_NATUREZA\_D

Informar o Indicador de Natureza \(débito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

A

001

SIM

NÃO

17

CENTRO\_CUSTO\_D

Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

N

020

NÃO

NÃO

18

DESCRICAO\_CENTRO\_CUSTO\_D

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

A

050

NÃO

NÃO

19

CENTRO\_LUCRO\_D

O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

N

020

NÃO

NÃO

20

TEXTO\_D

Informar o histórico da contabilização contábil

A

020

NÃO

NÃO

21

OBSERVACAO\_D

 Registrar a observação referente ao lançamento\.

A

020

NÃO

NÃO

22

CHAVE\_LANCTO\_C

Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\.

N

002

SIM

NÃO

23

COD\_CONTA\_C

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

N

070

SIM

NÃO

24

DESCRICAO\_CONTA\_C

Informar a Descrição da Conta existente na SAFX2002

A

050

SIM

NÃO

25

IND\_SITUACAO\_C

Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

A

001

SIM

NÃO

26

IND\_NATUREZA\_C

Informar o Indicador de Natureza \(crédito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

A

001

SIM

NÃO

27

CENTRO\_CUSTO\_C

Informar o Código do Centro de Custo\.

A

050

NÃO

NÃO

28

DESCRICAO\_CENTRO\_CUSTO\_C

Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

A

050

NÃO

NÃO

29

CENTRO\_LUCRO\_C

Informar o Código do Centro de Lucro\.

N

020

NÃO

NÃO

30

TEXTO\_C

Informar o histórico da contabilização contábil

A

020

NÃO

NÃO

31

OBSERVACAO\_C

Registrar a observação referente ao lançamento\.

A

020

NÃO

NÃO

32

USUARIO

Informar o login do usuário responsável pela gravação dos dados\.

A

014

SIM

NÃO

33

DATA\_PARAMETRO

Informar a Data Início/Inclusão/Alteração\.

N

008

NÃO

NÃO

 

ADO\- 973613

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 973613

__RN01__

__Campo 01 \- Código da empresa__

 

__Tabela: SAFX343__

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Campo destinado ao código da Empresa\. Vide regra RN00

__Tipo:__ A

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da Empresa

Exibir a mensagem da TFIX 22 CÓDIGO 90001

ADO\- 973613

__RN02__

__Campo 02 \- Código do estabelecimento__

__Tabela: SAFX343__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Campo destinado ao código do Estabelecimento\. Vide regra RN01

__Tipo:__ A

__Tamanho: __006__ __

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do Estabelecimento

Exibir a mensagem da TFIX 22 CÓDIGO 90002

ADO\- 973613

__RN03__

__Campo 03 – Unidade Federal__

__Tabela: SAFX343__

__Item: __03

__Nome do Campo:__ UF

__Descrição: __Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\.

__Tipo:__ C

__Tamanho: __002

__Campo Não Obrigatório__

__Comentário:__ 

Informa as UFs dos Estabelecimentos previamente selecionados na RN01\. 

ADO\- 973613

__RN04__

__Campo 04 – Grupo de Imposto__

__Tabela: SAFX343__

__Item: __04

__Nome do Campo:__ GRUPO\_IMPOSTO

__Descrição: __Informar o preenchimento é de âmbito Federal ou Estadual\. Vide regra RN03

__Tipo:__ C

__Tamanho: __010

__Campo Obrigatório__

__Chave Primária__

__Comentário:__ 

Permitir ao usuário escolher entre as opções ‘Federal’ ou ‘Estadual’

Exibir a mensagem da TFIX 22 CÓDIGO 913312

ADO\- 973613

__RN05__

__Campo 05 – Imposto__

__Tabela: SAFX343__

__Item: __05

__Nome do Campo:__ IMPOSTO

__Descrição: __Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\. Vide regra RN04

__Tipo:__ C

__Tamanho: __030

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa os tributos que compõem o campo GRUPO\_IMPOSTO \(RN04\), sendo eles, de âmbito Federal: PIS/PASEP\-Cumulativo, PIS/PASEP\-Não Cumulativo, COFINS\- Cumulativo, COFINS\-Não Cumulativo, IPI\. E de âmbito Estadual: ICMS\- Próprio, ICMS\-ST, ICMS\-Antecipado, FCP, DIFAL, SCANC

Exibir a mensagem da TFIX 22 CÓDIGO 913313

ADO\- 973613

__RN06__

__Campo 06 – Referência__

__Tabela: SAFX343__

__Item: __06

__Nome do Campo: __REFERENCIA

__Descrição: __O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\.

__Tipo: C__

__Tamanho: __016

__Campo Não Obrigatório__

__Comentário:__

Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP\.

ADO\- 973613

__RN07__

__Campo 07 – Local de Negócio __

__Tabela: SAFX343__

__Item: __07

__Nome do Campo: __LOCAL\_NEGOCIO

__Descrição: __O Preenchimento é livre e indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\.

__Tipo:__ A

__Tamanho:__ 004

__Campo Não Obrigatório__

__Comentário:__

Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário

ADO\- 973613

__RN08__

__Campo 08 – Divisão__

__Tabela: SAFX343__

__Item: __08

__Nome do Campo:__ DIVISAO

__Descrição:__ O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\.

__Tipo: A__

__Tamanho:__ 004

__Campo Não Obrigatório__

__Comentário:__

Informar o código do segmento/divisão financeira conforme cadastro no SAP\.

ADO\- 973613

__RN09__

__Campo 09 – Centro__

__Tabela: SAFX343__

__Item:__ 09

__Nome do Campo:__ CENTRO

__Descrição:__ O Preenchimento é livre indica a segregação SAP

__Tipo: __N

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar o Centro onde ocorreu a operação que deu origem ao registro\.

ADO\- 973613

__RN10__

__Campo 10 – Código de Ajuste __

__Tabela: SAFX343__

__Item:__ 10

__Nome do Campo:__ COD\_AJUSTE

__Descrição: __Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS\. 

__Tipo:__ N

__Tamanho: __019

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Ao selecionar o Grupo de Imposto \(Federal e Estadual\) — ICMS\-Próprio, ICMS\-Antecipado, ICMS\-ST, DIFAL, FCP, IPI, PIS \(Cumulativo e Não Cumulativo\), COFINS \(Cumulativo e Não Cumulativo\) e SCANC — o sistema deve: \(1\) identificar o "Imposto Relacionado"; \(2\) consultar a tabela de ajustes correspondente ao tributo \(para ICMS/DIFAL/FCP/ICMS\-ST usar ICT\_AJUSTE\_ICMS; para IPI/PIS/COFINS/SCANC usar a tabela própria do tributo\); \(3\) recuperar os campos de código e descrição do ajuste; e \(4\) concatenar esses valores para preencher automaticamente o campo "Código de Ajuste"\.

Exibir a mensagem da TFIX 22 CÓDIGO 913314

ADO\- 973613

__RN11__

__Campo 11 – Descrição de Ajuste__

__Tabela: SAFX343__

__Item: __11

__Nome do Campo:__ DESCRICAO\_AJUSTE

__Descrição: __Série do documento

__Tipo:__ C

__Tamanho: __003

__Campo Obrigatório__

__Comentário:__

Este campo deve ser concatenado ao campo COD\_AJUSTE \(RN10\) e informa ao usuário a descrição referente ao código de ajuste, conforme a apuração dos tributos ICMS, ICMS\-Antecipado, ICMS\-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS

Exibir a mensagem da TFIX 22 CÓDIGO 913315

ADO\- 973613

__RN12__

__Campo 12 – Chave de Lançamento \(Débito\)__

__Tabela: SAFX343__

__Item: 12__

__Nome do Campo:__ CHAVE\_LANCTO\_D

__Descrição: __Indica que o preenchimento é fixo com o valor '40' para transações de débito\.

__Tipo:__ N

__Tamanho: __002

__Campo Obrigatório__

__Comentário:__

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito

Exibir a mensagem da TFIX 22 CÓDIGO 913321

ADO\- 973613

__RN13__

__Campo 13 – Código da Conta \(Débito\)__

__Tabela: SAFX343__

__Item: __13

__Nome do Campo:__ COD\_CONTA\_D

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

__Tipo:__ A

__Tamanho: __070

__Campo Obrigatório__

__Comentário:__

Informar o Código da Conta e Subconta \(referente a operações de Débito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)

Exibir a mensagem da TFIX 22 CÓDIGO 913322

ADO\- 973613

__RN14__

__Campo 14 – Descrição da Conta \(Débito\)__

__Tabela: SAFX343__

__Item: 14__

__Nome do Campo:__ DESCRICAO\_CONTA\_D

__Descrição: __Informar a Descrição da Conta existente na SAFX2002

__Tipo:__ A

__Tamanho: __050

__Campo Obrigatório__

__Comentário:__

Informar a Descrição da Conta \(referente a operações de Débito\) existente na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913323

ADO\- 973613

__RN15__

__Campo 15 – Indicador da Situação \(Débito\)__

__Tabela: SAFX344__

__Item: 15__

__Nome do Campo:__ IND\_SITUACAO\_D

__Descrição: __Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913324

__RN16__

__Campo 16 – Indicador da Natureza \(Débito\)__

__Tabela: SAFX344__

__Item: 16__

__Nome do Campo:__ IND\_NATUREZA\_D

__Descrição: __Informar o Indicador de Natureza \(débito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar o Indicador de Natureza \(débito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa 

Exibir a mensagem da TFIX 22 CÓDIGO 913325

__RN17__

__Campo 17 – Centro de Custo \(Débito\)__

__Tabela: SAFX343__

__Item: 17__

__Nome do Campo:__ CENTRO\_CUSTO\_D

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ N

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Custo \(referente a operações de Débito\) conforme registro prévio na SAFX2003 

ADO\- 973613

__RN18__

__Campo 18 – Descrição do Centro de Custo \(Débito\) __

__Tabela: SAFX343__

__Item: 18__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_D

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ A

__Tamanho: __050

__Campo Não Obrigatório__

__Comentário:__

Informar a Descrição do Centro de Custo \(referente a operações de Débito\) conforme registro prévio na SAFX2003

ADO\- 973613

__RN19__

__Campo 19 – Centro de Lucro \(Débito\)__

__Tabela: SAFX343__

__Item: 19__

__Nome do Campo:__ CENTRO\_LUCRO\_D

__Descrição: __O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

__Tipo:__ N

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Débito\), este campo é opcional e serve apenas para controle interno\.

ADO\- 973613

__RN20__

__Campo 20 – Texto do Histórico \(Débito\)__

__Tabela: SAFX343__

__Item: 20__

__Nome do Campo:__ TEXTO\_D

__Descrição: __Informar o histórico da contabilização contábil__ __

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__ 

__Comentário:__

Informar o histórico da contabilização contábil__ __para transações de débito

ADO\- 973613

__RN21__

__Campo 21 – Observação \(Débito\)__

__Tabela: SAFX343__

__Item: 21__

__Nome do Campo:__ OBSERVAÇÃO\_D

__Descrição: __Registrar a observação referente ao lançamento\.

__Tipo:__ A

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito

ADO\- 973613

__RN22__

__Campo 22 – Chave de Lançamento \(Crédito\)__

__Tabela: SAFX343__

__Item: 22__

__Nome do Campo:__ CHAVE\_LANCTO\_C

__Descrição: __Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\.

__Tipo:__ N

__Tamanho: __002

__Campo Obrigatório__

__Comentário:__

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito

Exibir a mensagem da TFIX 22 CÓDIGO 913326

ADO\- 973613

__RN23__

__Campo 23 – Código da Conta \(Crédito\)__

__Tabela: SAFX343__

__Item: 23__

__Nome do Campo:__ COD\_CONTA\_C

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.__ __

__Tipo:__ N

__Tamanho: __070

__Campo Obrigatório__

__Comentário:__

Informar o Código da Conta e Subconta \(referente a operações de Crédito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

Exibir a mensagem da TFIX 22 CÓDIGO 913327

ADO\- 973613

__RN24__

__Campo 24 – Descrição da Conta \(Crédito\)__

__Tabela: SAFX343__

__Item: 24__

__Nome do Campo:__ DESCRICAO\_CONTA\_C

__Descrição: __Informar a Descrição da Conta existente na SAFX2002

__Tipo:__ A

__Tamanho: __050

__Campo Obrigatório__

__Comentário:__

Informar a Descrição da Conta \(referente a operações de Crédito\) existente na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913328

ADO\- 973613

__RN25__

__Campo 25 – Indicador de Situação \(Crédito\)__

__Tabela: SAFX344__

__Item: 25__

__Nome do Campo:__ IND\_SITUACAO\_C

__Descrição:__ Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913329

__RN26__

__Campo 26 – Indicador da Natureza \(Crédito\)__

__Tabela: SAFX344__

__Item: 26__

__Nome do Campo:__ IND\_NATUREZA\_C

__Descrição:__ Informar o Indicador de Natureza \(crédito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário: __

Informar o Indicador de Natureza \(crédito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

Exibir a mensagem da TFIX 22 CÓDIGO 913330

__RN27__

__Campo 27 – Centro de Custo \(Crédito\)__

__Tabela: SAFX343__

__Item: 27__

__Nome do Campo:__ CENTRO\_CUSTO\_C

__Descrição: __Informar o Código do Centro de Custo\.

__Tipo:__ A

__Tamanho: __050

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Custo\.

ADO\- 973613

__RN28__

__Campo 28 – Descrição do Centro de Custo \(Crédito\)__

__Tabela: SAFX343__

__Item: 28__

__Nome do Campo:__ DESCRICAO\_CENTRO\_CUSTO\_C

__Descrição: __Informar o Centro de Custo\. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ A

__Tamanho: __050

__Campo Não Obrigatório__

__Comentário:__

Informar a Descrição do Centro de Custo \(referente a operações de Crédito\) conforme registro prévio na SAFX2003

ADO\- 973613

__RN29__

__Campo 29 – Centro de Lucro \(Crédito\)__

__Tabela: SAFX343__

__Item: 29__

__Nome do Campo:__ CENTRO\_LUCRO\_C

__Descrição: __Informar o Código do Centro de Lucro\.

__Tipo:__ N

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Crédito\), este campo é opcional e serve apenas para controle interno\.

ADO\- 973613

__RN30__

__Campo 30 – Texto do Histórico \(Crédito\)__

__Tabela: SAFX343__

__Item: 30__

__Nome do Campo:__ TEXTO\_C

__Descrição: __Informar o histórico da contabilização contábil

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o histórico da contabilização contábil__ __para transações de crédito

ADO\- 973613

__RN31__

__Campo 31 – Observação \(Crédito\)__

__Tabela: SAFX343__

__Item: 31__

__Nome do Campo:__ OBSERVACAO\_C

__Descrição: __Registrar a observação referente ao lançamento\.

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito

ADO\- 973613

__RN32__

__Campo 32 – Usuário__

__Tabela: SAFX343__

__Item: 32__

__Nome do Campo:__ USUARIO

__Descrição: __Informar o login do usuário responsável pela gravação dos dados\.

__Tipo:__ A

__Tamanho: 014__

__Campo Obrigatório__

__Comentário:__

Informar o login do usuário responsável pela gravação dos dados\.

Exibir a mensagem da TFIX 22 CÓDIGO 913304

ADO\- 973613

__RN33__

__Campo 33 – Data do Parâmetro__

__Tabela: SAFX343__

__Item: 33__

__Nome do Campo:__ DATA\_PARAMETRO

__Descrição: __Informar a Data Início/Inclusão/Alteração\.

__Tipo:__ N

__Tamanho: 008__

__Campo Não Obrigatório__

__Comentário:__

Informar a Data Início/Inclusão/Alteração do parâmetro

ADO\- 973613

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

