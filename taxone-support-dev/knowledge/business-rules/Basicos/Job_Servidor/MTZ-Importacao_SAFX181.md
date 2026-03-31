# MTZ-Importacao_SAFX181

- **Fonte:** MTZ-Importacao_SAFX181.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 64 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>__Módulo Job Servidor – Importação –__<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>__ Rendimentos Recebidos Acumuladamente – SAFX181__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3528

Rendimentos Recebidos Acumuladamente

Será criada a SAFX181 para carregar as informações de Rendimentos Recebidos Acumuladamente, para atender o layout da DIRF 2012\.

12/01/2012

MFS\-90689

Elisabete Costa 

Criação do campo 104 – VLR\_JUROS\_MORA

27/09/2022

MFS\-94972 

Elisabete Costa

Criação do campo 105 – VALOR\_PG\_ADVOGADO

21/10/2022

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterados para contemplar os campos descritos abaixo na tabela SAFX\.

OS3528

__RN01__

__Campo 01 \- Código da empresa__

 

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3528

__RN02__

__Campo 02 \- Código do estabelecimento__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Obrigatório__

OS3528

__RN03__

__Campo 03 – Ano\_Calendario__

__Item: __03

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Ano Calendário__ __

__Tipo:__ N

__Tamanho: __004

__Comentário: __Campo destinado ao Ano\-Calendário

__Chave Primária__

__Obrigatório__

__Validação:__

Se o ano calendário não está preenchido ou menor que 2011, exibir a seguinte msg: 'Ano Calendário válido a partir de 2011\. Favor preencher corretamente\.'

OS3528

__RN04__

__Campo 04 – ANO\_REFERENCIA__

__Item: __04

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Ano Referência – DIRF

__Tipo:__ N

__Tamanho: __004

__Comentário: __Campo destinado ao Ano Referência – DIRF

__Chave Primária__

__Obrigatório__

__Validações:__

Se o ano calendário não está preenchido ou menor que 2012, exibir a seguinte msg: 'Ano Referência \- DIRF válido a partir de 2012\. Favor preencher corretamente\.'

Se o Intervalo do Ano Calendário e o Ano Referencia\-DIRF for maior que 1, exibir a seguinte msg: 'O intervalo entre Ano Calendário e o Ano Referência \- DIRF não pode ser superior a um ano\. favor preencher corretamente\.'

OS3528

__RN05__

__Campo 05 – Cod\_Receita__

__Item: __05

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código da Receita

__Tipo:__ N

__Tamanho: __004

__Comentário: __Campo destinado ao Código da Receita\.

Valor Válido: 1889

__Chave Primária__

__Obrigatório__

OS3528

__RN06__

__Campo 06 – COD\_FUNC     __

__Item: __06

__Nome do Campo: __A ser definido pelo A&D

__Descrição: : __Código do Funcionário

__Tipo:__N

__Tamanho: __014

__Comentário: __Campo destinado ao Beneficiário 

__Obrigatório__

__Validações:__

Se o Nome do Beneficiário não foi preenchido, exibir a seguinte msg: 'O Beneficiário deve ser preenchido\.'

Se Nome do Beneficiário não estiver cadastrado na x15\_funcionario, exibir a seguinte msg: ‘Beneficiário não existe na tabela de Funcionarios\.’

Se o CPF do Beneficiário não foi preenchido, , exibir a seguinte msg:'O CPF do Beneficiário deve ser preenchido\.'

Se o CPF informado não é um CPF válido, exibir a seguinte msg:'O CPF do Beneficiário não é válido\.'

OS3528

__RN07__

__Campo 07 – PROC\_REQ  __

__Item: __07

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Número do Processo/Requerimento

__Tipo:__ A

__Tamanho: __020

__Comentário:  __Campo destinado ao Número do Processo/Requerimento

__Chave Primária__

__Não Obrigatório__

__RN08__

__Campo 08 – IND\_RRA__

__Item: __08

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Identificador de recebimento recebido acumuladamente

__Tipo:__ N

__Tamanho: __001

__Comentário: __Campo destinado ao Identificador de recebimento recebido acumuladamente

Valores válidos:

1 – Pago pelo declarante

2 – Pago pela justiça

__Chave Primária__

__Obrigatório__

__Validações__

Se o Identificador do RRA não foi preenchido, exibir a seguinte msg: 'O Identificador de recebimento recebido acumuladamente deve ser preenchido\.'

Se o Identificador RRA igual a '2' e o número do processo/requerimento não preenchido , exibir a seguinte msg:'Quando o campo identificador de recebimento recebido acumuladamente for igual a 2, ' \+ & 

'o preenchimento do campo Número do Processo/Requerimento” é obrigatório\.'

__RN09__

__Campo 09 – NATUREZA\_RRA__

__Item: __09

__Nome do Campo: __A ser definido pelo A&D

__Descrição__: Natureza de rendimento recebido acumuladamente__ __

__Tipo:__ A

__Tamanho: __050

__Comentário:  __Campo destinado a Natureza de rendimento recebido acumuladamente

__Chave Primária__

__Não Obrigatório__

OS3528

__RN10__

__Campo 10 –  CPF\_CGC\_RESP\_JUR__

__Item: __10

__Nome do Campo:__ A ser definido pelo A&D

__Descrição:__ CPF do Advogado ou CNPJ do escritório de Advocacia

__Tamanho: __14 posições

__Tipo: __Number

__Comentário:__ Campo destinado ao CPF do Advogado ou CNPJ do escritório de Advocacia 

__Não Obrigatório__

__Validações:__

Se o CPF/CNPJ do Advogado não é valido , exibir a seguinte msg: 'O CPF/CNPJ do Advogado / Escritório de Advocacia não é válido\.'

Se o CPF/CNPJ do Advogado está preenchido e o Nome não está preenchido, exibir a seguinte msg: 'O nome do Advogado / Escritório de Advocacia deve ser preenchido\.'

OS3528

__RN11__

__Campo 11 – NOME\_RESP\_JUR__

__Item: __11

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Nome Advogado/Escritório de Advocacia__ __

__Tipo:__ A

__Tamanho: __150

__Comentário: __Campo destinado ao Nome Advogado/Escritório de Advocacia__ __

__Não Obrigatório__

__Validação:__

Se o Advogado foi preenchido e não existe informação de CPF ou CNPJ, exibir a seguinte msg:'Quando o campo Nome do Advogado / Escritório de Advocacia estiver preenchido, o campo CPF/CNPJ deve ser informado\.'

OS3528

__RN12__

__Campo 12 \- IND\_BENEF\_MOLESTIA__

__Item: __12

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Indica se o  Beneficiário é portador de moléstia grave atestada por laudo médico__ __

__Tipo:__ N

__Tamanho: __001

__Comentário: __Campo destinado ao Beneficiário é portador de moléstia grave atestada por laudo médico__ __

Valores Válidos: 

S – Sim

N\- Não

__Não Obrigatório__

__Validação: __

Quando o Beneficiário não é portador de moléstia grave atestada por laudo medico, os campos de Valor Rend\. Isento não podem estar preenchidos\. Nesta situação exibir a seguinte msg: “O Beneficiário não é portador de moléstia grave atestada por laudo medico, por isso, os campos de Valor Rend\. Isento não podem estar preenchidos\.”

OS3528

__RN13__

__Campo 13 – DATA\_MOLESTIA__

__Item: __13

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Data atribuída pelo laudo

__Tipo:__ N

__Tamanho: __008

__Comentário: __Campo destinado a Data atribuída pelo laudo

__Não Obrigatório__

__Validações: __

 Caso o campo Beneficiário é portador de moléstia grave atestada por laudo médico , estiver marcado, o campo Data atribuída pelo laudo é obrigatório\. Neste caso, se não houver informação no campo, o sistema deve exibir a seguinte msg: O campo Data atribuída pelo laudo é obrigatório, quando o Beneficiário é portador de moléstia grave atestada por laudo médico\.

Caso o campo Beneficiário é portador de moléstia grave atestada por laudo médico , estiver desmarcado, o campo Data atribuída pelo laudo não deve estar preenchido\. Neste caso, se não houver informação no campo, o sistema deve exibir a seguinte msg: O campo Data atribuída pelo laudo só deve ser preenchido, quando o Beneficiário é portador de moléstia grave atestada por laudo médico\.

OS3528

__RN14__

__Campo 14 – VALOR\_REND\_1__

__Item: __14

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Janeiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Janeiro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN15__

__Campo 15 \- VALOR\_REND\_ISENT\_1__

__Item: __15

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Janeiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Janeiro

__Não Obrigatório__

__RN16__

__Campo 16 – VALOR\_PREV\_OFC\_1__

__Item: __16

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Janeiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Janeiro

__Não Obrigatório__

OS3528

__RN17__

__Campo 17 – VALOR\_PENSAO\_1__

__Item: __17

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Janeiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Janeiro

__Não Obrigatório__

OS3528

__RN18__

__Campo 18 – IRRF\_RETIDO\_1__

__Item: __18

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Janeiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Janeiro

__Não Obrigatório__

OS3528

__RN19__

__Campo 19 –  VALOR\_DESP\_JUD\_1__

__Item: __19

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Janeiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Janeiro

__Não Obrigatório__

OS3528

__RN20__

__Campo 20 – QTD\_MESES\_1__

__Item: __20

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Janeiro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Janeiro

__Não Obrigatório__

OS3528

__RN21__

__Campo 21 – VALOR\_REND\_2__

__Item: __21

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Fevereiro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN22__

__Campo 22 \- VALOR\_REND\_ISENT\_2__

__Item: __22

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Fevereiro

__Não Obrigatório__

__RN23__

__Campo 23 – VALOR\_PREV\_OFC\_2__

__Item:__23

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Fevereiro

__Não Obrigatório__

OS3528

__RN24__

__Campo 24 – VALOR\_PENSAO\_2__

__Item: __24

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Fevereiro

__Não Obrigatório__

OS3528

__RN25__

__Campo 25 – IRRF\_RETIDO\_2__

__Item: __25

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Fevereiro

__Não Obrigatório__

OS3528

__RN26__

__Campo 26 –  VALOR\_DESP\_JUD\_2__

__Item: __26

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Fevereiro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Fevereiro

__Não Obrigatório__

OS3528

__RN27__

__Campo 27 – QTD\_MESES\_2__

__Item: __27

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Fevereiro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Fevereiro

__Não Obrigatório__

OS3528

__RN28__

__Campo 28 – VALOR\_REND\_3__

__Item: __28

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Março

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Março

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN29__

__Campo 29 \- VALOR\_REND\_ISENT\_3__

__Item: __29

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Março

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Março

__Não Obrigatório__

__RN30__

__Campo 30 – VALOR\_PREV\_OFC\_3__

__Item:__30

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Março

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Março

__Não Obrigatório__

OS3528

__RN31__

__Campo 31 – VALOR\_PENSAO\_3__

__Item: __31

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Março

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Março

__Não Obrigatório__

OS3528

__RN32__

__Campo 32– IRRF\_RETIDO\_3__

__Item: __32

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Março

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Março

__Não Obrigatório__

OS3528

__RN33__

__Campo 33 –  VALOR\_DESP\_JUD\_3__

__Item: __33

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Março

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Março

__Não Obrigatório__

OS3528

__RN34__

__Campo 34 – QTD\_MESES\_3__

__Item: __34

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Março

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Março

__Não Obrigatório__

OS3528

__RN35__

__Campo 35 – VALOR\_REND\_4__

__Item: __35

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Abril

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Abril

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN36__

__Campo 36\- VALOR\_REND\_ISENT\_4__

__Item: __36

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Abril

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Abril

__Não Obrigatório__

__RN37__

__Campo 37 – VALOR\_PREV\_OFC\_4__

__Item: __37

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Abril

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Abril

__Não Obrigatório__

OS3528

__RN38__

__Campo 38– VALOR\_PENSAO\_4__

__Item: __38

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Abril

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Abril

__Não Obrigatório__

OS3528

__RN39__

__Campo 39 – IRRF\_RETIDO\_4__

__Item: __39

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Abril

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Abril

__Não Obrigatório__

OS3528

__RN40__

__Campo 40 –  VALOR\_DESP\_JUD\_4__

__Item: __40

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Abril

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Abril

__Não Obrigatório__

OS3528

__RN41__

__Campo  41 – QTD\_MESES\_4__

__Item: __41

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Abril

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Abril

__Não Obrigatório__

OS3528

__RN42__

__Campo 42 – VALOR\_REND\_5__

__Item: __42

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Maio

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Maio

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN43__

__Campo 43 \- VALOR\_REND\_ISENT\_5__

__Item: __43

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Maio

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Maio

__Não Obrigatório__

__RN44__

__Campo 44– VALOR\_PREV\_OFC\_5__

__Item:__44

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Maio

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Maio

__Não Obrigatório__

OS3528

__RN45__

__Campo 45– VALOR\_PENSAO\_5__

__Item: __45

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Maio

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Maio

__Não Obrigatório__

OS3528

__RN46__

__Campo 46 – IRRF\_RETIDO\_5__

__Item: __46

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Maio

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Maio

__Não Obrigatório__

OS3528

__RN47__

__Campo 47–  VALOR\_DESP\_JUD\_5__

__Item: __47

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Maio

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Maio

__Não Obrigatório__

OS3528

__RN48__

__Campo 48 – QTD\_MESES\_5__

__Item: __48

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Maio

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Maio

__Não Obrigatório__

OS3528

__RN49__

__Campo 49 – VALOR\_REND\_6__

__Item: __49

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Junho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Junho

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN50__

__Campo 50 \- VALOR\_REND\_ISENT\_6__

__Item: __50

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Junho

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Junho

__Não Obrigatório__

__RN51__

__Campo 51– VALOR\_PREV\_OFC\_6__

__Item:__51

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Junho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Junho

__Não Obrigatório__

OS3528

__RN52__

__Campo 52 – VALOR\_PENSAO\_6__

__Item: __52

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Junho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Junho

__Não Obrigatório__

OS3528

__RN53__

__Campo 53 – IRRF\_RETIDO\_6__

__Item: __53

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Junho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Junho

__Não Obrigatório__

OS3528

__RN54__

__Campo 54 –  VALOR\_DESP\_JUD\_6__

__Item: __54

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Junho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Junho

__Não Obrigatório__

OS3528

__RN55__

__Campo 55 – QTD\_MESES\_6__

__Item: __55

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Junho

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Junho

__Não Obrigatório__

OS3528

__RN56__

__Campo 56 – VALOR\_REND\_7__

__Item: 5__6

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Julho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Julho

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN57__

__Campo 57\- VALOR\_REND\_ISENT\_7__

__Item: __57

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Julho

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Julho

__Não Obrigatório__

__RN58__

__Campo 58 – VALOR\_PREV\_OFC\_7__

__Item:5__8

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Julho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Julho

__Não Obrigatório__

OS3528

__RN59__

__Campo 59 – VALOR\_PENSAO\_7__

__Item: 5__2

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Julho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Julho

__Não Obrigatório__

OS3528

__RN60__

__Campo 60 – IRRF\_RETIDO\_7__

__Item: 5__3

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Julho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Julho

__Não Obrigatório__

OS3528

__RN61__

__Campo 61 –  VALOR\_DESP\_JUD\_7__

__Item: 61__

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Julho

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Julho

__Não Obrigatório__

OS3528

__RN62__

__Campo 62 – QTD\_MESES\_7__

__Item: __62

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Julho

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Julho

__Não Obrigatório__

OS3528

__RN63__

__Campo 63– VALOR\_REND\_8__

__Item: __63

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Agosto

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Agosto

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN64__

__Campo 64\- VALOR\_REND\_ISENT\_8__

__Item: __64

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Agosto

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Agosto

__Não Obrigatório__

__RN65__

__Campo 65 – VALOR\_PREV\_OFC\_8__

__Item:__65

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Agosto

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Agosto

__Não Obrigatório__

OS3528

__RN66__

__Campo 66 – VALOR\_PENSAO\_8__

__Item: __66

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Agosto

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Agosto

__Não Obrigatório__

OS3528

__RN67__

__Campo 67 – IRRF\_RETIDO\_8__

__Item: __67

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Agosto

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Agosto

__Não Obrigatório__

OS3528

__RN68__

__Campo 68 –  VALOR\_DESP\_JUD\_8__

__Item: __68

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Agosto

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Agosto

__Não Obrigatório__

OS3528

__RN69__

__Campo 69 – QTD\_MESES\_8__

__Item: __69

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Agosto

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Agosto

__Não Obrigatório__

OS3528

__RN70__

__Campo 70 – VALOR\_REND\_9__

__Item: __70

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Setembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Setembro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN71__

__Campo 71 \- VALOR\_REND\_ISENT\_9__

__Item: __71

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Setembro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Setembro

__Não Obrigatório__

__RN72__

__Campo 72 – VALOR\_PREV\_OFC\_9__

__Item:__72

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Setembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Setembro

__Não Obrigatório__

OS3528

__RN73__

__Campo 73 – VALOR\_PENSAO\_9__

__Item: __73

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Setembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Setembro

__Não Obrigatório__

OS3528

__RN74__

__Campo 74 – IRRF\_RETIDO\_9__

__Item:__65

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Setembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Setembro

__Não Obrigatório__

OS3528

__RN75__

__Campo 75 –  VALOR\_DESP\_JUD\_9__

__Item: __66

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Setembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Setembro

__Não Obrigatório__

OS3528

__RN76__

__Campo 76 – QTD\_MESES\_9__

__Item: __76

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Setembro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Setembro

__Não Obrigatório__

OS3528

__RN77__

__Campo 77 – VALOR\_REND\_10__

__Item: 77__

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Outubro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Outubro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN78__

__Campo 78 \- VALOR\_REND\_ISENT\_10__

__Item: __78

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Outubro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Outubro

__Não Obrigatório__

__RN79__

__Campo 79– VALOR\_PREV\_OFC\_10__

__Item:__79

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Outubro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Outubro

__Não Obrigatório__

OS3528

__RN80__

__Campo 80– VALOR\_PENSAO\_10__

__Item: __80

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Outubro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Outubro

__Não Obrigatório__

OS3528

__RN81__

__Campo 81 – IRRF\_RETIDO\_10__

__Item: __81

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Outubro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Outubro

__Não Obrigatório__

OS3528

__RN82__

__Campo 82 –  VALOR\_DESP\_JUD\_10__

__Item:__82

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Outubro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Outubro

__Não Obrigatório__

OS3528

__RN83__

__Campo 83 – QTD\_MESES\_10__

__Item: __83

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Outubro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Outubro

__Não Obrigatório__

OS3528

__RN84__

__Campo 84– VALOR\_REND\_11__

__Item: __84

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Novembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Novembro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN85__

__Campo 85 \- VALOR\_REND\_ISENT\_11__

__Item: __85

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Novembro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Novembro

__Não Obrigatório__

__RN86__

__Campo 86– VALOR\_PREV\_OFC\_11__

__Item:__86

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Novembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Novembro

__Não Obrigatório__

OS3528

__RN87__

__Campo 87– VALOR\_PENSAO\_11__

__Item: __87

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Novembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Novembro

__Não Obrigatório__

OS3528

__RN88__

__Campo 88 – IRRF\_RETIDO\_11__

__Item: __88

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Novembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Novembro

__Não Obrigatório__

OS3528

__RN89__

__Campo 89–  VALOR\_DESP\_JUD\_11__

__Item: __89

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Novembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Novembro

__Não Obrigatório__

OS3528

__RN90__

__Campo 90 – QTD\_MESES\_11__

__Item: __90

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Novembro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Novembro

__Não Obrigatório__

OS3528

__RN91__

__Campo 91 – VALOR\_REND\_12__

__Item: __91

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Dezembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Dezembro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN92__

__Campo 92 \- VALOR\_REND\_ISENT\_12__

__Item: __92

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Dezembro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Dezembro

__Não Obrigatório__

__RN93__

__Campo 93 – VALOR\_PREV\_OFC\_12__

__Item:93__

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Dezembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Dezembro

__Não Obrigatório__

OS3528

__RN94__

__Campo 94 – VALOR\_PENSAO\_12__

__Item: __94

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Dezembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Dezembro

__Não Obrigatório__

OS3528

__RN95__

__Campo 95 – IRRF\_RETIDO\_12__

__Item: __95

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Dezembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Dezembro

__Não Obrigatório__

OS3528

__RN96__

__Campo 96 –  VALOR\_DESP\_JUD\_12__

__Item: __96

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Dezembro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Dezembro

__Não Obrigatório__

OS3528

__RN97__

__Campo 97 – QTD\_MESES\_12__

__Item: __97

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Quantidade de meses de Dezembro

__Tipo:__ N

__Tamanho: __004

Sendo 3 inteiros e 1 decimal

__Comentário: __Campo destinado a Quantidade de meses de Dezembro

__Não Obrigatório__

OS3528

__RN98__

__Campo 98 – VALOR\_REND\_13__

__Item: __98

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Tributável de Décimo Terceiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Tributável de Décimo Terceiro

__Não Obrigatório__

__Validação:__

Se o Valor dos Rendimentos Tributáveis\(por mês\) está preenchido com valor maior que zero e o correspondente da Qtd de Meses não está preenchido ou é igual a zero, exibir a seguinte msg: 'Rendimento recebido acumuladamente foi preenchido sem a informação da quantidade de meses\.'

OS3528

__RN99__

__Campo 99 \- VALOR\_REND\_ISENT\_13__

__Item: __99

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Rendimento Isento Moléstia Grave de Dezembro

__Tipo:__ N

__Tamanho: __015

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Rendimento Isento Moléstia Grave de Dezembro

__Não Obrigatório__

__RN100__

__Campo 100 – VALOR\_PREV\_OFC\_13__

__Item:__100

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Previdência Oficial de Décimo Terceiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Previdência Oficial de Décimo Terceiro

__Não Obrigatório__

OS3528

__RN101__

__Campo 101 – VALOR\_PENSAO\_13__

__Item: __101

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Pensão Alimentícia de Décimo Terceiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor da Pensão Alimentícia de Décimo Terceiro

__Não Obrigatório__

OS3528

__RN102__

__Campo 102 – IRRF\_RETIDO\_13__

__Item: __102

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Imposto Retido de Décimo Terceiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor do Imposto Retido de Décimo Terceiro

__Não Obrigatório__

OS3528

__RN103__

__Campo 103 –  VALOR\_DESP\_JUD\_13__

__Item: __103

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor das Despesas de Ação Judicial de Décimo Terceiro

__Tipo:__ N

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: __Campo destinado ao Valor das Despesas da Ação Judicial de Décimo Terceiro

__Não Obrigatório__

OS3528

__RN104__

__Campo 104 –  VLR\_JUROS\_MORA__

__Item:__ 104

__Descrição:__ Valor de rendimento isento anual relativo aos Juros de Mora recebidos 

__Tipo:__ N

__Tamanho:__ 015

Sendo 13 inteiros e 2 decimais

__Comentário:__ rendimento isento anual relativo aos Juros de Mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função

__Não Obrigatório__

MFS\-90689

__RN105__

__Campo 11 – VALOR\_PG\_ADVOGADO__

__Item: __

__Nome do Campo: __

__Descrição: Valor pago para o advogado __

__Tipo: N__

__Tamanho: 015__

Sendo 13 inteiros e 2 decimais

__Comentário: Campo destinado ao Valor Pago para o advogado __

__Não Obrigatório__

__Validação:__

__Se os campos CPF\_CGC\_ RES\_JUR e NOME\_RESP\_JUR estiverem preenchidos e não existe informação do valor exibir a seguinte msg: 'Quando o campo Nome do Advogado / Escritório de Advocacia estiver preenchido, o campo “Valor pago ao advogado” deve ser informado\.'__

__Inclusão do campo “Valor Pago para Advogado”__

MFS\-94972

