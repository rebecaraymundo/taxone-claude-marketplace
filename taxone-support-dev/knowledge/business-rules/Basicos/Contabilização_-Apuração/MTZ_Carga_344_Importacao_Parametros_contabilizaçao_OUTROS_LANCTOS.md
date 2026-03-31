# MTZ_Carga_344_Importacao_Parametros_contabilizaçao_OUTROS_LANCTOS

- **Fonte:** MTZ_Carga_344_Importacao_Parametros_contabilizaçao_OUTROS_LANCTOS.docx
- **Modificado:** 2026-01-20
- **Tamanho:** 145 KB

---

THOMSON REUTERS

 TAX PAYMENTS – IMPORTAÇÃO \- SAFX344 \(Integração de Contabilização – Parâmetros – Outros Lançamentos da Apuração\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Outros Lançamentos

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 973594

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX344

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

Implantar uma interface de parametrização dos "Outros Lançamentos da Apuração", destinada a configurar, de forma simples e segura, os códigos de outros lançamentos contábeis e sua vinculação às contas contábeis\. O objetivo é permitir que o usuário selecione empresa/estabelecimento/UF, defina o grupo de imposto \(Federal ou Estadual\) e escolha tributos como ICMS \(próprio, ST, antecipado, FCP, DIFAL, SCANC\), IPI e PIS/COFINS, aplicando automaticamente as regras de negócio correspondentes para garantir consistência dos dados

__Localização:__

- __Agrupamentos: Básico >> Job Servidor__
- __   Menu: __Carga__ __> Programação > Execução 
- __                        __Importação > Programação > Execução      
-                                      Importação batch > Programação > Execução 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX344 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para a Importação da SAFX344:

A importação da SAFX344 deve seguir as seguintes premissas de negócio e comportamentos:

- Layout e fontes de dados: o arquivo deve obedecer ao Manual de Layout SAFX\(inserir número\) e às estruturas de referência utilizadas pelo sistema: SAFX2002 \(Plano de Contas\), SAFX2003 \(Centro de Custo\), SAFX2006 \(Natureza da Operação\) e SAFX147 \(Operação de Crédito\)\.

__Resultado da Importação:__

Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:

- __Módulo: Manutenção >> Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Outros Lançamentos__
- __Menu: Acesso Principal >> Parâmetros__

__                 __

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Grupo de Imposto \-Vide regra RN 05
- Campo Imposto – Vide regra RN 06
- Campo Outros Lançamentos Contábeis – Vide regra RN 10
- Campo Código da Natureza da Receita – Vide regra RN 11
- Campo Descrição Complementar – Vide regra RN 12
- Campo Descrição da Natureza da Operação – Vide regra RN 14
- Campo Indicador de Situação – Vide regra RN 15
- Campo Indicador de Natureza – Vide regra RN 16
- Campo Código da Conta \(Débito\) – Vide regra RN 17
- Campo Descrição da Conta \(Débito\) – Vide regra RN 18
- Campo Chave de Lançamento \(Débito\) – Vide regra RN 19
- Campo Código da Conta \(Crédito\) – Vide regra RN 25
- Campo Chave de Lançamento \(Crédito\) – Vide regra RN 27
- Campo Usuário – Vide regra RN 33

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

REFERENCIA

O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\. 

C

016

NÃO

NÃO

5

GRUPO\_IMPOSTO

Informar o preenchimento é de âmbito Federal ou Estadual\. Vide regra RN03

C

010

SIM

\(\*\)

6

IMPOSTO

Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\. Vide regra RN04

C

030

SIM

\(\*\)

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

COD\_TIPO\_LIVRO

Informar o código do livro fiscal “108” \(Livro de Apuração\) ou “165” \(Livro de Apuração por Inscrição Estadual Única\)\.

A

003

NÃO

11

OUTRO\_LANCAMENTOS\_CONTABEIS

Identificar os seguintes tipos de lançamentos \(este dado preencher conforme dados da RN07\):   
Saldo Devedor,  
Saldo Credor,   
Total de Crédito,   
Total de Débito,   
F100 \- Demais Receitas   
 F100 \- Demais Créditos\.

C

050

SIM

NÃO

12

COD\_NAT\_REC

Informar o código da Natureza da Receita  da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147 este dado preencher conforme dados da RN07

N

003

SIM

NÃO

13

DESC\_COMPL

Informar a descrição complementar do Documento/Operação\.SAFX147\- este dado preencher conforme dados da RN07

A

255

SIM

NÃO

14

COD\_OPER\_APUR

Informar o Código da Natureza de Operação conforme SAFX2006

A

003

NÃO

NÃO

15

DESCRICAO\_DSC\_OPER\_APUR

Informar a Descrição da Natureza da Operação\. SAFX2006

A

255

SIM

NÃO

16

CHAVE\_LANCTO\_D

Indica que o preenchimento é fixo com o valor '40' para transações de débito\.

N

002

SIM

NÃO

17

COD\_CONTA\_D

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

N

070

SIM

NÃO

18

DESCRICAO\_CONTA\_D

Informar a Descrição da Conta existente na SAFX2002

A

50

SIM

NÃO

19

IND\_SITUACAO\_D

Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

A

001

SIM

NÃO

20

IND\_NATUREZA\_D

Informar o Indicador de Natureza \(débito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

A

001

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

CENTRO\_LUCRO\_D

O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

N

020

NÃO

NÃO

23

TEXTO\_D

Informar o histórico da contabilização contábil

A

020

NÃO

NÃO

24

OBSERVACAO\_D

 Registrar a observação referente ao lançamento\.

A

020

NÃO

NÃO

25

CHAVE\_LANCTO\_C

Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\.

N

002

SIM

NÃO

26

COD\_CONTA\_C

Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

N

070

SIM

NÃO

27

DESCRICAO\_CONTA\_C

Informar a Descrição da Conta existente na SAFX2002

A

050

NÃO

NÃO

28

IND\_SITUACAO\_C

Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

A

001

SIM

NÃO

29

IND\_NATUREZA\_C

Informar o Indicador de Natureza \(crédito\) existente na SAFX2002:  
1\. Ativo  
2\. Passivo  
3\. Despesa

A

001

SIM

NÃO

30

CENTRO\_CUSTO\_C

Informar o Código do Centro de Custo\.

A

050

NÃO

NÃO

31

CENTRO\_LUCRO\_C

Informar o Código do Centro de Custo\.

N

020

NÃO

NÃO

32

TEXTO\_C

Informar o histórico da contabilização contábil

A

020

NÃO

NÃO

33

OBSERVACAO\_C

 Registrar a observação referente ao lançamento\.

A

020

NÃO

NÃO

34

USUARIO

Informar o login do usuário responsável pela gravação dos dados\.

A

014

SIM

NÃO

35

DATA\_PARAMETRO

Informar a Data Início/Inclusão/Alteração\.

N

008

NÃO

NÃO

 

ADO\- 973594

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 973594

__RN01__

__Campo 01 \- Código da empresa__

 

__Tabela: SAFX344__

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

ADO\- 973594

__RN02__

__Campo 02 \- Código do estabelecimento__

__Tabela: SAFX344__

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

ADO\- 973594

__RN03__

__Campo 03 – Unidade Federal__

__Tabela: SAFX344__

__Item: __03

__Nome do Campo:__ UF

__Descrição: __Informar a sigla da Unidade Federativa \(UF\) correspondente ao estabelecimento\.

__Tipo:__ C

__Tamanho: __002

__Campo Não Obrigatório__

__Comentário:__ 

Informa as UFs dos Estabelecimentos previamente selecionados na RN01\. 

ADO\- 973594

__RN04__

__Campo 04 – Referência__

__Tabela: SAFX344__

__Item: __04

__Nome do Campo:__ REFERENCIA

__Descrição: __O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP\.

__Tipo:__ C

__Tamanho: __016

__Campo Não Obrigatório__

__Comentário:__ 

Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP\.

ADO\- 973594

__RN05__

__Campo 05 – Grupo do Imposto__

__Tabela: SAFX344__

__Item: __05

__Nome do Campo:__ IMPOSTO

__Descrição: __Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\. Vide regra RN04

__Tipo:__ C

__Tamanho: __010

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Permitir ao usuário escolher entre as opções ‘Federal’ ou ‘Estadual’

Exibir a mensagem da TFIX 22 CÓDIGO 913312

ADO\- 973594

__RN06__

__Campo 06 – Imposto__

__Tabela: SAFX344__

__Item: __06

__Nome do Campo: __IMPOSTO

__Descrição: __Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual\. Vide regra RN04

__Tipo: C__

__Tamanho: __016

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Este campo informa os tributos que compõem o campo GRUPO\_IMPOSTO \(RN04\), sendo eles, de âmbito Federal: PIS/PASEP\-Cumulativo, PIS/PASEP\-Não Cumulativo, COFINS\- Cumulativo, COFINS\-Não Cumulativo, IPI\. E de âmbito Estadual: ICMS\- Próprio, ICMS\-ST, ICMS\-Antecipado, FCP, DIFAL, SCANC

Exibir a mensagem da TFIX 22 CÓDIGO 913313

ADO\- 973594

__RN07__

__Campo 07 – Local de Negócio __

__Tabela: SAFX344__

__Item: __07

__Nome do Campo: __LOCAL\_NEGOCIO

__Descrição: __O Preenchimento é livre e indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP\.

__Tipo:__ A

__Tamanho:__ 004

__Campo Não Obrigatório__

__Comentário:__

Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário

ADO\- 973594

__RN08__

__Campo 08 – Divisão__

__Tabela: SAFX344__

__Item: __08

__Nome do Campo:__ DIVISAO

__Descrição:__ O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP\.

__Tipo: A__

__Tamanho:__ 004

__Campo Não Obrigatório__

__Comentário:__

Informar o código do segmento/divisão financeira conforme cadastro no SAP\.

ADO\- 973594

__RN09__

__Campo 09 – Centro__

__Tabela: SAFX344__

__Item:__ 09

__Nome do Campo:__ CENTRO

__Descrição:__ O Preenchimento é livre indica a segregação SAP

__Tipo: A__

__Tamanho: __004

__Campo Não Obrigatório__

__Comentário:__

Informar o Centro onde ocorreu a operação que deu origem ao registro\.

ADO\- 973594

__RN10__

__Campo 10 – Código do tipo do Livro__

__Tabela: SAFX344__

__Item:__ 10

__Nome do Campo:__ COD\_TIPO\_LIVRO

__Descrição: __Informar o código do livro fiscal “108” \(Livro de Apuração\) ou “165” \(Livro de Apuração por Inscrição Estadual Única\) 002 – Livro de Apuração IPI

__Tipo:__ A

__Tamanho: __003

__Campo Obrigatório__

__Comentário:__

Este campo informa o tipo do livro para os impostos __ICMS Próprio, ICMS\-ST, ICMS Antecipado, IPI, FCP, DIFAL:__

ADO\- 973594

__RN11__

__Campo 11 – Outros Lançamentos Contábeis  __

__Tabela: SAFX344__

__Item:__ 11

__Nome do Campo:__ OUTROS\_LANCAMENTOS\_CONTABEIS

__Descrição: __Identificar os seguintes tipos de lançamentos \(este dado preencher conforme dados da RN07\): 

\- Saldo Devedor,

\- Saldo Credor, 

\- Total de Crédito, 

\- Total de Débito, 

\- F100 \- Demais Receitas 

\- F100 \- Demais Créditos\.

__Tipo:__ C

__Tamanho: __050

__Campo Obrigatório__

__Comentário:__

Este campo informa aos usuários os valores associados às duas categorias de tributos que podem ser selecionadas, sendo elas: 

- __ICMS Próprio, ICMS\-ST, ICMS Antecipado, IPI, FCP, DIFAL:__
	- Saldo Devedor
	- Saldo Credor
	- Total de Crédito
	- Total de Débito
- __PIS \- Cumulativo, PIS \- Não Cumulativo, COFINS \- Cumulativo e COFINS \- Não Cumulativo:__
	- Saldo Devedor
	- Saldo Credor
	- Total de Crédito
	- Total de Débito
	- F100 \- Demais Receitas
	- F100 \- Demais Créditos

Exibir a mensagem da TFIX 22 CÓDIGO 913316

ADO\- 973594

__RN12__

__Campo 12 – Código da Natureza da Receita__

__Tabela: SAFX344__

__Item: __12

__Nome do Campo:__ COD\_NAT\_REC 

__Descrição: __Informar o código da Natureza da Receita da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147 

__Tipo:__ N

__Tamanho: __003

__Campo Obrigatório__

__Comentário:__

Informar o código da Natureza da Receita da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147 

Exibir a mensagem da TFIX 22 CÓDIGO 913317

ADO\- 973594

__RN13__

__Campo 13 – Descrição Complementar do Documento/Operação__

__Tabela: SAFX344344__

__Item: __13

__Nome do Campo:__ DESC\_COMPL

__Descrição: __Informar a descrição complementar do Documento/Operação\.SAFX147

__Tipo:__ A

__Tamanho: __255

__Campo Obrigatório__

__Comentário:__

Informar a descrição complementar do Documento/Operação \(SAFX147\), fazer concatenação com o campo COD\_NAT\_REC

Exibir a mensagem da TFIX 22 CÓDIGO 913318

ADO\- 973594

__RN14__

__Campo 14 – Código Natureza da Operação__

__Tabela: SAFX344344__

__Item: __14

__Nome do Campo:__ COD\_NATUREZA\_OP

__Descrição: __Informar o Código da Natureza de Operação conforme SAFX2006

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar o Código da Natureza de Operação conforme SAFX2006

Exibir a mensagem da TFIX 22 CÓDIGO 913319

ADO\- 973594

__RN15__

__Campo 15 – Descrição da Natureza da Operação__

__Tabela: SAFX344__

__Item: __15

__Nome do Campo:__ DESCRICAO\_DSC\_OPER\_APUR

__Descrição: __Informar a Descrição da Natureza da Operação\. SAFX2006

__Tipo:__ A

__Tamanho: 255__

__Campo Obrigatório__

__Comentário:__

Informar a Descrição da Natureza da Operação, conforme SAFX2006

Exibir a mensagem da TFIX 22 CÓDIGO 913320

ADO\- 973594

__RN16__

__Campo 16 – Chave de Lançamento \(Débito\)__

__Tabela: SAFX344__

__Item: 16__

__Nome do Campo:__ CHAVE\_LANCTO\_D

__Descrição: __Indica que o preenchimento é fixo com o valor '40' para transações de débito\.

__Tipo:__ N

__Tamanho: __002

__Campo Obrigatório__

__Comentário:__

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito

Exibir a mensagem da TFIX 22 CÓDIGO 913321

ADO\- 973594

__RN17__

__Campo 17 – Código da Conta \(Débito\)__

__Tabela: SAFX344__

__Item: __17

__Nome do Campo:__ COD\_CONTA\_D

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

__Tipo:__ A

__Tamanho: __070

__Campo Obrigatório__

__Comentário:__

Informar o Código da Conta e Subconta \(referente a operações de Débito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)

Exibir a mensagem da TFIX 22 CÓDIGO 913322

ADO\- 973594

__RN18__

__Campo 18 – Descrição da Conta \(Débito\)__

__Tabela: SAFX344__

__Item: 18__

__Nome do Campo:__ DESCRICAO\_CONTA\_D

__Descrição: __Informar a Descrição da Conta existente na SAFX2002

__Tipo:__ A

__Tamanho: __050

__Campo Obrigatório__

__Comentário:__

Informar a Descrição da Conta \(referente a operações de Débito\) existente na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913323

ADO\- 973594

__RN19__

__Campo 19 – Indicador da Situação \(Débito\)__

__Tabela: SAFX344__

__Item: 19__

__Nome do Campo:__ IND\_SITUACAO\_D

__Descrição: __Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913324

__RN20__

__Campo 20 – Indicador da Natureza \(Débito\)__

__Tabela: SAFX344__

__Item: 20__

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

__RN21__

__Campo 20 – Centro de Custo \(Débito\)__

__Tabela: SAFX344__

__Item: 20__

__Nome do Campo:__ CENTRO\_CUSTO\_D

__Descrição: __Informar o Centro de Custo\. O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Tipo:__ N

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Custo \(referente a operações de Débito\) conforme registro prévio na SAFX2003

ADO\- 973594

__RN22__

__Campo 22 – Centro de Lucro \(Débito\)__

__Tabela: SAFX344__

__Item: 22__

__Nome do Campo:__ CENTRO\_LUCRO\_D

__Descrição: __O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo\. Este campo é opcional e serve apenas para controle interno\.

__Tipo:__ N

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Débito\), este campo é opcional e serve apenas para controle interno\.

ADO\- 973594

__RN23__

__Campo 23 – Texto do Histórico \(Débito\)__

__Tabela: SAFX344__

__Item: 23__

__Nome do Campo:__ TEXTO\_D

__Descrição: __Informar o histórico da contabilização contábil__ __

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__ 

__Comentário:__

Informar o histórico da contabilização contábil__ __para transações de débito

ADO\- 973594

__RN24__

__Campo 24 – Observação \(Débito\)__

__Tabela: SAFX344__

__Item: 24__

__Nome do Campo:__ OBSERVAÇÃO\_D

__Descrição: __Registrar a observação referente ao lançamento\.

__Tipo:__ A

__Tamanho: __020

__Campo Não Obrigatório__

__Comentário:__

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito

ADO\- 973594

__RN25__

__Campo 25 – Chave de Lançamento \(Crédito\)__

__Tabela: SAFX344__

__Item: 25__

__Nome do Campo:__ CHAVE\_LANCTO\_C

__Descrição: __Indica que o preenchimento é fixo com o valor '50' para transações de Crédito\.

__Tipo:__ N

__Tamanho: __002

__Campo Obrigatório__

__Comentário:__

Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito

Exibir a mensagem da TFIX 22 CÓDIGO 913326

ADO\- 973594

__RN26__

__Campo 26 – Código da Conta \(Crédito\)__

__Tabela: SAFX344__

__Item: 26__

__Nome do Campo:__ COD\_CONTA\_C

__Descrição: __Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.__ __

__Tipo:__ N

__Tamanho: __070

__Campo Obrigatório__

__Comentário:__

Informar o Código da Conta e Subconta \(referente a operações de Crédito\), que deve estar registrada na Tabela de Plano de Contas \(SAFX2002\)\.

Exibir a mensagem da TFIX 22 CÓDIGO 913327

ADO\- 973594

__RN27__

__Campo 27 – Descrição da Conta \(Crédito\)__

__Tabela: SAFX344__

__Item: 27__

__Nome do Campo:__ DESCRICAO\_CONTA\_C

__Descrição: __Informar a Descrição da Conta existente na SAFX2002

__Tipo:__ A

__Tamanho: __050

__Campo Obrigatório__

__Comentário:__

Informar a Descrição da Conta \(referente a operações de Crédito\) existente na SAFX2002

Exibir a mensagem da TFIX 22 CÓDIGO 913328

ADO\- 973594

__RN28__

__Campo 28 – Indicador de Situação \(Crédito\)__

__Tabela: SAFX344__

__Item: 28__

__Nome do Campo:__ IND\_SITUACAO\_C

__Descrição:__ Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002

__Tipo:__ A

__Tamanho: __001

__Campo Obrigatório__

__Comentário:__

Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa\. O campo assume os seguintes valores: A – Ativa na SAFX2002Exibir a mensagem da TFIX 22 CÓDIGO 913329

__RN29__

__Campo 29 – Indicador da Natureza \(Crédito\)__

__Tabela: SAFX344__

__Item: 29__

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

__RN30__

__Campo 30 – Centro de Custo \(Crédito\)__

__Tabela: : __SAFX

__Item: 30__

__Nome do Campo:__ CENTRO\_CUSTO\_C

__Descrição: __Informar o Código do Centro de Custo\.

__Tipo:__ A

__Tamanho: __050

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Custo\.

ADO\- 973594

__RN31__

__Campo 31 – Centro de Lucro \(Crédito\)__

__Tabela: SAFX344__

__Item: 31__

__Nome do Campo:__ CENTRO\_LUCRO\_C

__Descrição: __Informar o Código do Centro de Lucro\.

__Tipo:__ N

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o Código do Centro de Lucro \(referente a operações de Crédito\), este campo é opcional e serve apenas para controle interno\.

ADO\- 973594

__RN32__

__Campo 32 – Texto do Histórico \(Crédito\)__

__Tabela: SAFX344__

__Item: 32__

__Nome do Campo:__ TEXTO\_C

__Descrição: __Informar o histórico da contabilização contábil

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar o histórico da contabilização contábil__ __para transações de crédito

ADO\- 973594

__RN33__

__Campo 33 – Observação \(Crédito\)__

__Tabela: SAFX344__

__Item: 33__

__Nome do Campo:__ OBSERVACAO\_C

__Descrição: __Registrar a observação referente ao lançamento\.

__Tipo:__ A

__Tamanho: 020__

__Campo Não Obrigatório__

__Comentário:__

Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito

__RN34__

__Campo 34 – Usuário__

__Tabela: SAFX344__

__Item: 34__

__Nome do Campo:__ USUARIO

__Descrição: __Informar o login do usuário responsável pela gravação dos dados\.

__Tipo:__ A

__Tamanho: 014__

__Campo Obrigatório__

__Comentário:__

Informar o login do usuário responsável pela gravação dos dados\.

Exibir a mensagem da TFIX 22 CÓDIGO 913304

__RN35__

__Campo 35 – Data do Parâmetro__

__Tabela: SAFX344__

__Item: 36__

__Nome do Campo:__ DATA\_PARAMETRO

__Descrição: __Informar a Data Início/Inclusão/Alteração\.

__Tipo:__ N

__Tamanho: 008__

__Campo Não Obrigatório__

__Comentário:__

Informar a Data Início/Inclusão/Alteração do parâmetro

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

