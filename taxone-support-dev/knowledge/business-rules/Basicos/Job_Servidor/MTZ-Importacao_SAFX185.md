# MTZ-Importacao_SAFX185

- **Fonte:** MTZ-Importacao_SAFX185.docx
- **Modificado:** 2025-04-09
- **Tamanho:** 38 KB

---

    

# Módulo Job Servidor \- <a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>Importação \-Apuração da Contribuição Previdenciária sobre a Receita Bruta \- Bloco P \- \(SAFX185\) 

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX185, conforme o Manual de Layout,  o que facilita a consulta\) *

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3584\-DW

Criação da SAFX3584

Será criada uma tabela para atendimento do Bloco P \(Registro P100\), registro específico da escrituração da contribuição previdenciária incidente sobre o valor da receita bruta, prevista na legislação tributária\.

13/04/2012

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

30/12/2013

CH21166\_2014

Alteração da validação do campo 13

Este documento tem como objetivo alterar a validação do preenchimento do campo 13 \- Valor da Base de Cálculo da Contribuição Previdenciária 

sobre a Receita Bruta

10/10/2014

<a id="_Hlk514844290"></a>MFS16783

Alteração do campo 9

Ajuste na obrigatoriedade do campo 09 \- Valor da Receita Bruta Total

27/02/2018

<a id="_Hlk514844419"></a>CH9211\_2018

MFS18679

Alteração do campo 10

Ajuste na obrigatoriedade do campo 09 \- Valor da Receita Bruta do Estabelecimento, correspondente às atividades referidas no campo 05\.

23/05/2018

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

OS3584\-DW

__RN01__

__Campo 01 \- Código da empresa__

 

__Tabela: __SAFX185

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3584\-DW

__RN02__

__Campo 02 \- Código do estabelecimento__

__Tabela: __SAFX185

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__ Chave Primária__

__Obrigatório__

OS3584\-DW

__RN03__

__Campo 03 – Data Inicial__

__Tabela: __SAFX185

__Item: __03

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Data Inicial

__Tipo:__ N

__Tamanho: __008

__Comentário: __Informar a data inicial que a apuração se refere

__Chave Primária__

__Obrigatório__

OS3584\-DW

__RN04__

__Campo 04 – Data Final__

__Tabela: __SAFX185

__Item: __04

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Data Final

__Tipo:__ N

__Tamanho: __008

__Conteúdo do Campo: __Informar a data final que a apuração se refere__ __

__Obrigatório__

__Validação1: __As datas Inicial e Final devem estar dentro do mesmo período, senão, exibir a msg ao usuário\.

__Validação2:__A data final não poderá ser maior que a data inicial, caso contrário, exibir, msg ao usuário\.

__Validação3:__ Se for carregado um registro com um determinado período e o usuário importar um novo registro com datas que estará no intervalo já carregado, esta informação não será considerada\.

OS3584\-DW

__RN05__

__Campo 05 – Indicador da Atividade Econômica__

__Tabela: __SAFX185

__Item: __05

__Nome do Campo: __Será definido pelo A&D__ __

__Descrição: __Informação complementar da composição da Receita 

__Tipo:__ A

__Tamanho__: 008

__Conteúdo do Campo: __Campo destinado à ao código indicador correspondente à atividade sujeita a incidência da Contribuição Previdenciária sobre a Receita Bruta, conforme a tabela 5\.1\.1

__Chave Primária__

__Obrigatório__

__Validação: __O Indicador do Código da Atividade Econômica deve constar na tabela 5\.1\.1 \(TACES75\), caso contrário exibir msg ao usuário\.

OS3584\-DW

__RN06__

__Campo 06 – Código da Receita__

__Tabela: __SAFX185

__Item: __06

__Nome do Campo:__ COD\_CONTA __COD\_RECEITA__

__Descrição: __Código da Receita

__Tipo:__A

__Tamanho: __006

__Obrigatório__

__Chave Primária__

__Comentário:__Código da Receita referente à Contribuição Previdenciária, conforme informado na DCTF\.

Valores Válidos: Grupo do cód\_tributo 34

298501 – Empresas Prestadoras de Serviço de Tecnologia da Informação – TI e Tecnologia da Informação e Comunicação – TCI

298502 	\- Contribuicao Previdenciaria Sobre Receita Bruta \- Empresas Prestadoras de Servicos TI e TIC  \- 13º Salario

299101 \- Contribuição Previdenciária sobre a Receita Bruta – Demais

299102	\-Contribuicao Previdenciaria Sobre Receita Bruta \- Demais  13º Salario 

Atenção: Este campo deve estar cadastrado na dwt\_cod\_receita

OS3584\-DW

__RN07__

__Campo 07 – Código da conta analítica debitada/creditada __

__Tabela: __SAFX185

__Item: __07

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Não Obrigatório__

__Chave Primária__

__Comentário: __Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela     de Plano de Contas \(SAFX2002\)\. 

OS3584\-DW

__RN08__

__Campo 08 – Centro de Custo__

__Tabela: __SAFX185

__Item: __08

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Centro de Custo

__Tipo:__ A

__Tamanho: __020

__Não Obrigatório__

__Comentário: __O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

OS3584\-DW

__RN09__

__Campo 09– Valor da Receita Bruta Total__

__Tabela: __SAFX185

__Item: __09

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da Receita Bruta Total

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Valor da Receita Bruta Total do Estabelecimento no Período da escrituração, sujeitas ou não à incidência da Contribuição Previdenciária sobre a Receita\.

__\[Alterado  MFS16783\]__

__Não Obrigatório__

__Validação: __O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX” deve ser maior que zero\.”

OS3584\-DW

MFS16783

__RN10__

__Campo 10 –__<a id="OLE_LINK15"></a>__Valor da Receita Bruta do Estabelecimento , correspondente às atividades referidas no campo 05__

__Tabela: __SAFX185

__Item:__ 10

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor da Receita Bruta do Estabelecimento , correspondente às atividades referidas no campo 05

__Tipo:__ N

__Tamanho: __015V002 – O campo poderá aceitar o valor zerado “0,00”\.

__Obrigatório__

__Conteúdo do Campo: __Valor da Receita Bruta do Estabelecimento, no período da escrituração, correspondente às atividades listadas nos art\. 7º e 8º da Lei nº 12\.546/2011, sujeitas à incidência da Contribuição Previdenciária sobre a Receita\.

__Validação: __O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX” deve ser maior que zero\. ”

OS3584\-DW

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>CH9211\_2018

MFS18679

__RN11__

__Campo 11 – Valor da Receita das Demais Atividades__

__Tabela: __SAFX185

__Item: __11

__Nome do campo: __Será definido pelo A&D

__Descrição: __Valor da Receita das Demais Atividades__ __

__Tipo:__ N

__Tamanho: __015V002

__Comentário:__\. Valor da Receita Bruta da\(s\) Atividade\(s\) Sujeita\(s\) à Contribuição Previdenciária sobre a Remuneração \(Incisos I e III do art\. 22 da Lei nº 8\.212, de 1991\)

__Não Obrigatório__

OS3584\-DW

__RN12__

__Campo 12 – Valor das Exclusões da Receita Bruta__

__Tabela: __SAFX185

__Item:__ 12

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor das Exclusões da Receita Bruta

__ Tipo:__ N

__Tamanho: __015V002

__Não Obrigatório__

__Conteúdo do Campo: __Valor das Exclusões da Receita Bruta informada no campo 12 \.

OS3584\-DW

__RN13__

__Campo 13 – Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta__

__\[ALTERADA – CH21166\_2014\]__

__Tabela: __SAFX185

__Item: __13

__Nome do Campo: __Será definido pelo A&D

__Descrição:__ Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta 

 \(Campo 13 = Campo 10 – Campo 12\)

__Obrigatório__

__Validação: __

O valor informado neste campo deve ser maior ou igual a zero, então fazer a verificação da seguinte forma:

- Se o valor do Campo 10 e o valor do Campo 12 for igual permitir preencher com zeros \(0,00\);
- Se o valor do Campo 10 for maior que o Campo 12 permitir preencher com zeros \(0,00\) ou a diferença \(a informação correta será de responsabilidade do usuário\);
- Se o valor do Campo 10 for menor que o Campo 12 e o campo 13 receber valor maior que zero exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX\(13\)” deve ser maior que zero\.”

__Observação: __A mensagem é para entender que não haverá valor negativo, pois o valor do campo 12 nunca poderá ser maior que o campo 10, mas ele pode ser zero quando os valores forem iguais\.

OS3584\-DW

CH21166\_2014

__RN14__

__Campo 14 \- Alíquota da Contribuição Previdenciária sobre a Receita Bruta __

__Tabela: __SAFX185

__Item: __14

__Nome do Campo: __Será definido pelo A&D

__Descrição:__ Alíquota da Contribuição Previdenciária sobre a Receita Bruta 

__Tipo:__ N

__Tamanho: __008V004

__Comentário: __Valor da alíquota correspondente à receita da atividade tributável\. A alíquota informada deve constar na Tabela 5\.1\.1

__ Chave Primária__

__ Obrigatório__

__Validação01: __Se o indicador da Atividade Econômica for 99999999 permitir qualquer valor de alíquota, mesmo que não esteja cadastrada na TACES75

__Validação 02__: Se o indicador da Atividade Econômica for diferente de 99999999 , só permitir as alíquotas que estão informada na tabela 5\.1\.1  \(TACES 75\), caso contrário exibir a msg ao usuário\.

__Validação03:__ O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX” deve ser maior que zero\.”

OS3584\-DW

__RN15__

__Campo 15 – Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta__

__Tabela: __SAFX185

__Item: __15

__Nome do Campo: __IND\_PRODUTO __VLR\_CONT\_PREV__

__Descrição: __Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta 

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Informar o valor da Contribuição Previdenciária Apurada sobre a Receita Bruta \(Campo 13 x Campo 14\)

__Obrigatório__

__Validação: __O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX” deve ser maior que zero\.”

OS3584\-DW

__RN16__

__Campo 16  – Descrição complementar do Registro__

__Tabela: __SAFX185

__Item: __16

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Descrição complementar do Registro

__Tipo:__ A

__Tamanho: __255

__Não Obrigatório__

__Comentário: __Descrição complementar do Registro

OS3584\-DW

__RN17__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX185

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

