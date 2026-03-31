# MTZ_JOB_SERVIDOR_Importacao_SAFX341

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX341.docx
- **Modificado:** 2026-01-15
- **Tamanho:** 74 KB

---

THOMSON REUTERS

 JOB SERVIDOR – IMPORTAÇÃO \- SAFX341

__              Localização:__

__	Módulo: __Básicos 🡪 Job Servidor

__	Menu: __Carga__ __🡪 Programação 🡪 Execução

__       		__Importação 🡪 Programação 🡪 Execução     

          		Importação batch 🡪 Programação 🡪 Execução

# \(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX341 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS794593

Andréa Rocha

Criação da tabela para importação da SAFX\.

MFS1020267

Andréa Rocha

Alteração da regra de importação para atualizar a coluna Valor Total\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

__SAFX340 – Registro 1400 – SPED\-EFD__

__Tabela Definitiva:__ EFD\_REG\_1400

 

OBRIG

ITEM

DESCRIÇÃO

CAMPO

TAMANHO

TIPO

\(\*\)

01

Código da Empresa

COD\_EMPRESA

003

A

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

006

A

\(\*\)

03

Período Inicial

DATA\_INI

008

N

\(\*\)

04

Período Final

DATA\_FIM

008

N

\(\*\)

05

UF

COD\_ESTADO

002

A

\(\*\)

06

Código do Município

COD\_MUNICIPIO

005

N

07

Indicador do Produto

IND\_PRODUTO

001

A

08

Código do Produto

COD\_PRODUTO

060

A

09

Código da Tabela IPM

COD\_ITEM\_PART\_MUN

060

A

10

Valores Apurados

VLR\_AGREG\_INF

015V002

N

  11

Valores Deduções

VLR\_DED\_INF

015V002

N

MFS794593

RN01

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS794593

RN02

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

Quando não preenchido, o registro não será importado\.

MFS794593

RN03

__Campo Período Inicial__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\. 

O formato deve ser informado no padrão AAAAMMDD\.

Quando o campo não for preenchido ou preenchido com informação que não é uma data válida, o registro não será importado, e no log de erros será gravada uma das mensagens de erro:

*91371 \- Periodo de referencia inicial nao preenchido\.*

*91372 \- Periodo de referencia inicial invalido\.*

MFS794593

RN04

__Campo Período Final__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\. 

O formato deve ser informado no padrão AAAAMMDD\.

Quando o campo não for preenchido ou preenchido com informação que não é uma data válida, o registro não será importado, e no log de erros será gravada uma das mensagens de erro:

*91373 \- Periodo de referencia final nao preenchido\.*

*91374 \- Periodo de referencia final invalido\.*

MFS794593

RN05

__Campo UF__

Campo de preenchimento obrigatório\.

Informar a UF de acordo com a Tabela de ESTADO \(TFIX04\)\.

Quando o campo não for preenchido ou preenchido com informação inválida, o registro não será importado, e no log de erros será gravada uma das mensagens de erro:

*92140 \- O codigo do estado e obrigatorio\.\.*

*50726 \- Erro na recuperacao do estado\.*

MFS794593 

RN06

__Campo Código do Município__

Campo de preenchimento obrigatório\.

Informar o códido de município de acordo com a Tabela de MUNICÍPIO \(TACES06\)\. Utilizar o campo UF para verificar se é um código de município válido\. 

Quando o campo não for preenchido ou preenchido com informação inválida, o registro não será importado, e no log de erros será gravada a mensagem de erro:

*92349 \-O campo Municipio do Registro deve ser preenchido com um municipio valido\.*

MFS794593 

RN07

__Campo Indicador do Produto__

Campo de preenchimento __*não*__ obrigatório\.

Identificadores:

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

Quando o campo for preenchido com informação inválida, o registro não será importado, e no log de erros será gravada a mensagem de erro:

*92851 \-Indicador/Codigo do produto nao cadastrado\.*

MFS794593

RN08

__Campo Produto__

Campo de preenchimento __*não*__ obrigatório\.

Informar o Código do Produto/Mercadoria, de acordo com a Tabela de Produto \(SAFX2013\)\.

Quando o campo for preenchido com informação inválida, o registro não será importado, e no log de erros será gravada a mensagem de erro:

*92446 \-* *O produto informado nao existe na Tabela de Produtos \(SAFX2013\)\.*

Quando o Produto for preenchido e a UF for diferente da UF do estabelecimento, o registro não será importado, e no log de erros será gravada a mensagem de erro:

*93799 \-* *O produto não pode ser informado quando o campo UF for diferente da UF do estabelecimento\.*

MFS794593

RN09

__Campo Código do Item \- IPM__

Campo de preenchimento __*não*__ obrigatório\.

Informar o Código do Item IPM, de acordo com a Tabela de Códigos dos Itens de Participação dos Municípios \(TACES89\)\.  Utilizar o campo UF junto com o código do item IPM para verificar se é um código válido\.  Além disso, deve\-se verificar se a coluna código da tabela da TACES89 é válida de acordo com o campo UF informado, se a UF for igual a UF do estabelecimento, o código da tabela pode ser igual a “5\.9\.1” ou “5\.9\.2”, mas se a UF for diferente da UF do estabelecimento, o código da tabela somente pode ser igual a “5\.9\.2”\.

Quando o campo for preenchido com informação inválida, o registro não será importado, e no log de erros será gravada a mensagem de erro:

*93798 \-* *O Código IPM nao existe na Tabela de Códigos IPM \(TACES89\)\.*

MFS794593

RN10

__Campo Valores Apurados__

Campo de preenchimento __*não*__ obrigatório\.

MFS794593

RN11

__Campo Valores Deduções__

Campo de preenchimento __*não*__ obrigatório\.

__\[MFS1020267\] __Atualização da Coluna Valor Total

Quando um registro for importado, o campo "Valor Total" deve ser atualizado, mesmo que este campo não exista na SAFX\. A atualização deve seguir a seguinte regra:

Valor Total = Valor Apurado Calculado \(VLR\_AGREG\_CALC\) – Deduções Calculada \(VLR\_DED\_CALC\) \+ Outros Valores Informado \(VLR\_AGREG\_INF\) – Outras Deduções Informada \(VLR\_DED\_INF\)

MFS794593

MFS1020267

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

