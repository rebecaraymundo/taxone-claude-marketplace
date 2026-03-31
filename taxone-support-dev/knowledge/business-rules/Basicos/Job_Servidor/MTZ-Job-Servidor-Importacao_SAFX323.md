# MTZ-Job-Servidor-Importacao_SAFX323

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX323.docx
- **Modificado:** 2023-05-08
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX323

Tabela de Inventário por Produto e Tipo de Avaliação

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS521496

Liliane Assaf

Criação da nova tabela SAFX para carga do Inventário por Produto e Tipo de Avaliação, usada no módulo do i\-SIMP\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX323__ 🡪 vide manual de layout

__Campos que compõe a chave da tabela:__

   Empresa \+ Estabelecimento \+ Data Inventário \+ Grupo Contagem \+ Produto \+ Tipo Avaliação \+ Natureza Estoque \+ Unidade Padrão \+ Almoxarifado \+ Centro de Custo \+ NBM \+ Inscrição Estadual \+ Pessoa Fis/Jur

A manutenção desta tabela é feita no Módulo Data Wharehouse, menu Manutenção 🡪 Estoque 🡪 Inventário por Produto e Tipo de Avaliação\.

__Tabela de Destino:__

A SAFX323 alimenta a tabela definitiva X323\_INVENT\_PROD\_AVAL

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

__Obs__\.: O campo DISCRI\_INVENTARIO não existe na tabela SAFX, só existe na tabela definitiva \(X323\_INVENT\_PROD\_AVAL\), porque é preenchido automaticamente na importação\.   

MFS521496

__RN01__

__Campo Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS521496

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS521496

__RN03__

__Campo 03 \- Data Inventário__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                    90164 “O Campo Data de Inventario e obrigatorio \- deve ser preenchido”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                     93355 “Campo Data de Inventario com formato invalido\.”*

MFS521496

__RN04__

__Campo 04 \- Grupo de Contagem__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um código inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90159 “O Campo de Grupo de Contagem deve ser: <1> ou <2> ou <3> ou <4> ou <5>“”*

Códigos válidos:

1 \- Estoque Próprio, em Poder do Estabelecimento;  
2 \- Estoque Próprio, em Poder de Terceiros;  
3 \- Estoque de Terceiros, em Poder do Estabelecimento;  
4 \- Estoque de Terceiros em poder de Terceiros;  
5 \- Estoque em Depósito Fechado\.

MFS521496

__RN05__

__Campo 05 \- Indicador de Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90035 “Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) nao esta preenchido ou com informacao invalida\.”*

Indicadores válidos:

1 \- Produto;

2 \- Matéria Prima/Insumo;

3 \- Embalagem;

4 \- Material Uso/Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

MFS521496

__RN06__

__Campo 06 – Código do Produto __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90033 \- “Codigo do Produto nao esta preenchido\.”*

Validação do produto na SAFX2013:

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 05\), o Código do Produto \(campo 06\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90034 \- “Codigo do Produto nao cadastrado\.”*

MFS521496

__RN07__

__Campo 07 – Tipo de Avaliação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*93551 \- “Tipo de Avaliação nao esta preenchido\.”*

MFS521496

__RN08__

__Campo 08 – Natureza de Estoque__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90157 \- “O Campo Codigo da Natureza de Estoque deve ser preenchido”*

Validação da natureza de estoque na SAFX2010:

O código da natureza de estoque informado será validado na Tabela de Naturezas de Estoque \(SAFX2010\)\. Como a X2010 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na tabela de Naturezas de Estoque irá considerar o o Código da Natureza de Estoque \(campo 08\) e o Grupo obtido conforme a regra descrita acima\. Caso a Natureza de Estoque não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90158 \- “O Campo Codigo da Natureza de Estoque nao esta Cadastrado”*

MFS521496

__RN09__

__Campo 09 – Unidade Padrão__

Campo não obrigatório\.

Validação da Unidade Padrão na SAFX2017:

O código da unidade padrão informado será validado na Tabela de Unidade Padrão \(SAFX2017\)\. Como a X2017 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na Tabela de Unidade Padrão irá considerar o Código da Unidade Padrão \(campo 09\) e o Grupo obtido conforme a regra descrita acima\. Caso a Unidade Padrão não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90148 \- “A Unidade Padrao nao esta cadastrada”*

MFS521496

__RN10__

__Campo 10 – Almoxarifado__

Campo não obrigatório\.

Validação do Almoxarifado na SAFX2021:

O código do almoxarifado informado será validado na Tabela de Almoxarifado \(SAFX2021\)\. Como a X2021 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na Tabela de Almoxarifado irá considerar o Código do Almoxarifado \(campo 10\) e o Grupo obtido conforme a regra descrita acima\. Caso o Almoxarifado não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90396 \- “O Codigo de Almoxarifado nao esta cadastrado\.”*

MFS521496

__RN11__

__Campo 11 – Centro de Custo__

Campo não obrigatório\.

Validação do Centro de Custo na SAFX2003:

O código do centro de custo informado será validado na Tabela de Centro de Custo \(SAFX2003\)\. Como a X2003 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na Tabela de Centro de Custo irá considerar o Código do Centro de Custo \(campo 11\) e o Grupo obtido conforme a regra descrita acima\. Caso o Centro de Custo não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90381 \- “O Campo Codigo de Centro de Custo nao esta cadastrado\.”*

MFS521496

__RN12__

__Campo 12 \- Código de Classificação Fiscal \- NBM__

Campo não obrigatório\.

Validação do NBM na SAFX2043:

O código do NBM informado será validado na Tabela de Classificação Fiscal \- NBM \(SAFX2043\)\. Como a X2043 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na Tabela de Classificação Fiscal \- NBM irá considerar o Código do NBM \(campo 12\) e o Grupo obtido conforme a regra descrita acima\. Caso o NBM não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90163 \- “O Campo Codigo NBM nao esta cadastrado\.”*

MFS521496

__RN13__

__Campo 13 – Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90149 \- “O Campo Unidade de Medida nao esta preenchido\.”*

Validação da unidade de medida na SAFX2007:

O código unidade de medida informado será validado na Tabela de Unidade de Medida \(SAFX2007\)\. Como a X2007 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na tabela de Unidade de Medida irá considerar o Código Unidade de Medida \(campo 13\) e o Grupo obtido conforme a regra descrita acima\. Caso a Unidade de Medida não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90150 \- “A Unidade de Medida nao esta cadastrada\.”*

MFS521496

__RN14__

__Campo 14 – Indicador de Pessoa Física/Jurídica__

Campo não obrigatório\.

Quando preenchido com um código inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“92178 \- “O indicador de Pessoa Fisica/Juridica, deve ser preenchido de acordo com: <1>, <2>, <3>, <4> ou <5>\.”*

Códigos válidos:

1 – Fornecedor;  
2 – Cliente;  
3 – Estabelecimento;  
4 – Transportadora;  
5 – Cliente/Fornecedor/Transportadora\.

MFS521496

__RN15__

__Campo 15 – Código de Pessoa Física/Jurídica__

Campo não obrigatório\.

Validação da Pessoa Fis/Jur na SAFX04:

A Pessoa Fis/Jur informada deve ser validada na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. Como a X04 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir da Empresa, Estabelecimento e Data do Inventário\. O grupo de cadastro considerado será o de maior data de validade <= Data do Inventário\. 

A busca na Tabela de Pessoa Física/Jurídica irá considerar o Indicador, Código da Pessoa Fis/Jur \(campos 14 e 15\) e o Grupo obtido conforme a regra descrita acima\. Caso a Pessoa Fis/Jur não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*90124 \- “O Codigo da Pessoa Fisica/Juridica nao esta cadastrado\.”*

MFS521496

__RN16__

__Campo 16 – Inscrição Estadual__

Campo não obrigatório\.

Caso o campo seja preenchido, o conteúdo deve ser validado na tabela de Cadastro de Inscrições Estaduais do Estabelecimento \(ict\_estab\_iestad\) do módulo PIM\.  Caso o código não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*91070 \- “Inscricao Estadual nao cadastrada na Tabela de Inscricoes Estaduais no estabelecimento\.“*

\.

MFS521496

__RN17__

__Campo 17 – Quantidade de Inventário__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90404 \- “Campo Obrigatorio \- informar Quantidade\.”*

MFS521496

__RN18__

__Campo 18 – Custo Unitário__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90267 \- “Campo Obrigatorio \- informar Valor\.”*

MFS521496

__RN19__

__Campo 19 – Custo Total__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90267 \- “Campo Obrigatorio \- informar Valor\.”*

MFS521496

__RN20__

__Campo 20 – Reservado 1__

Campo de preenchimento não obrigatório\.

Caso seja preenchido com um conteúdo não numérico, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90461 \- Valor Decimal ou Numerico com formato invalido\.*

MFS521496

__RN21__

__Campo 21 – Reservado 2__

Campo de preenchimento não obrigatório\.

Caso seja preenchido com um conteúdo não numérico, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90461 \- Valor Decimal ou Numerico com formato invalido\.*

MFS521496

__RN22__

__Campo 22 – Reservado 3__

Campo de preenchimento não obrigatório\.

Caso seja preenchido com um conteúdo não numérico, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*90461 \- Valor Decimal ou Numerico com formato invalido\.*

MFS521496

__RN23__

__Campo 23 – Reservado 4__

Campo de preenchimento não obrigatório\.

MFS521496

__RN24__

__Campo 24 – Reservado 5__

Campo de preenchimento não obrigatório\.

MFS521496

__RN25__

__Campo 25 – Reservado 6__

Campo de preenchimento não obrigatório\.

MFS521496

__RN26__

__Campo 26 – Reservado 7__

Campo de preenchimento não obrigatório\.

MFS521496

__RN27__

__Campo 27 – Reservado 8__

Campo de preenchimento não obrigatório\.

MFS521496

__R28__

__Campo Discri\_Inventario__

Esse campo só existe na tabela definitiva \(X323\_INVENT\_PROD\_AVAL\)\. Ele é gravado com a concatenação dos campos: __Unidade Padrão \+ Almoxarifado \+ Centro de Custo \+ NBM \+ Inscrição Estadual \+ Pessoa Fis/Jur__

Se o campo “Utiliza mais de um NBM e/ou Utiliza mais e uma Insc\. Estadual” no Cadastro do Estabelecimento está __marcado__, então:

   DISCRI\_INVENTÁRIO = nvl\(to\_char\(ident\_und\_padrao\_w\), ' '\) ||

			  nvl\(to\_char\(ident\_almox\_w\), ' '\) ||

			  nvl\(to\_char\(ident\_custo\_w\), ' '\) || 

                    nvl\(to\_char\(ident\_nbm\_w\), ' '\) ||

			  nvl\(p\_insc\_estadual, ' '\) || '\.S'||

			  nvl\(to\_char\(ident\_fis\_jur\_w\), ' '\)

Se o campo “Utiliza mais de um NBM e/ou Utiliza maid e uma Insc\. Estadual” no Cadastro do Estabelecimento está __desmarcado__, então:

  DISCRI\_INVENTÁRIO =  nvl\(to\_char\(ident\_und\_padrao\_w\), ' '\) ||

			  nvl\(to\_char\(ident\_almox\_w\), ' '\) ||

			  nvl\(to\_char\(ident\_custo\_w\), ' '\) ||

			  nvl\(to\_char\(ident\_fis\_jur\_w\), ' '\) 

MFS521496

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

