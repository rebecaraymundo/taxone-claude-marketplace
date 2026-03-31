# MTZ_JOB_SERVIDOR_Exportacao_SAFX2102

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX2102.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 65 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3835\-C1

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX2102\.

MFS26811

Andréa Rocha

Alteração da regra do campo Indicador de Classificação DRE\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2102 \- Códigos de Aglutinação Balanço/DRE/DLPA/DMPL, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Código de Aglutinação

A

070

SIM

SIM

Número de Ordem

N

004

SIM

SIM

Descrição da Conta Aglutinadora

A

100

SIM

SIM

Indicador de Balanço DRE

A

001

SIM

SIM

Indicador de Natureza

A

001

NÃO

NÃO

Indicador de Classificação DRE

A

001

NÃO

NÃO

Nível

A

005

SIM

SIM

Expressão de Ordem

A

4000

NÃO

NÃO

 

OS3835\-C1

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C1

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C1

RN04

__Campo Código de Aglutinação__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Codigo de Aglutinacao deve ser preenchido”\.

Na importação, se o COD\_CONTA\_AGLUT não estiver pré\-cadastrado como Balanço Patrimonial ou Demonstração de Resultado e o campo IND\_BALANCO\_DRE for igual ‘L’ ou ‘M’, deverá exibir a seguinte mensagem de erro:

“Código de Aglutinação não cadastrado em Balanço Patrimonial ou Demonstração de Resultado\.”\.

Satisfeita a condição acima, e o registro importado ou o registro pré\-existente da conta aglutinadora \(como Balanço Patrimonial / Demonstração de Resultado\) esteja com os campos IND\_NATUREZA = ‘3’ ou ‘4’ ou IND\_CLASSIF\_DRE = ‘2’, deverá ser exibida a mensagem de erro e não será permitida a importação:

“Não é permitida a inclusão de códigos de aglutinação DLPA/DMPL que seja Subtotalizador/Totalizador, ou que tenha pré\-cadastrado como Subtotalizador/Totalizador\. Favor corrigir\.”

OS3835\-C1

RN05

__Campo Número de Ordem__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Numero de ordem não preenchido”\.

Caso seja importado um registro na SAFX2102 com o mesmo Número de Ordem o sistema não deverá permitir a importação e deverá exibir mensagem de erro, de acordo com respectivo IND\_BALANCO\_DRE:

Se IND\_BALANCO\_DRE =B 

“Não é permitido Nº\. de Ordem repetido na Balanço Patrimonial\. Favor efetuar a devida correção\.”\.

Se IND\_BALANCO\_DRE =D 

“Não é permitido Nº\. de Ordem repetido na Demonstração de Resultado\. Favor efetuar a devida correção\.”\.

Se IND\_BALANCO\_DRE =L 

“Não é permitido Nº\. de Ordem repetido na DLPA\. Favor efetuar a devida correção\.”\.

Se IND\_BALANCO\_DRE =M 

“Não é permitido Nº\. de Ordem repetido na DMPL\. Favor efetuar a devida correção\.”\.

OS3835\-C1

RN06

__Campo Descrição da Conta Aglutinadora__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: 

“O Campo Descrição da Tabela deve ser preenchido”\.

OS3835\-C1

RN07

__Campo Índicador de Balanço DRE__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido ou seja preenchido com valor diferente de <B>, <D>, <L> ou <M>, deve ser exibida mensagem de erro:  
“Indicador de Aglutinação deve ser preenchido com <B>, <D>, <L> ou <M>”\.

OS3835\-C1

RN08

__Campo Indicador de Natureza__

Preencher de acordo com o Indicador da Natureza de Balanço\.

Este campo somente deverá ser preenchido caso o IND\_BALANCO\_DRE = ’B’\. 

Quando houver registro com IND\_BALANCO\_DRE <> ‘B’ e o Campo Indicador de Natureza estiver preenchido, deverá impedir a importação e apresentar a mensagem:

“Indicador de Natureza so deve ser preenchido para Codigo de Aglutinacao do Balanco Patrimonial \(Indicador de Balanco e DRE = B\)” B’”

Quando o IND\_BALANCO\_DRE = ‘B’, então deverá permitir somente os registros <1>, <2>, <3> ou <4> para o Campo Indicador de Natureza e não deve permitir registro no Campo Indicador de Classificação DRE\.

Na condição acima:

Se o valor do Campo Indicador de Natureza informado for diferente de <1>, <2>, <3> ou <4>, apresentar mensagem:

“Indicador de Natureza do Balanco deve ser preenchido <1>, <2>, <3> ou <4>, para Codigo de Aglutinacao do Balanco Patrimonial \(Indicador de Balanco e DRE = B\)”

Se tiver valor no Campo Indicador de Classificação DRE, apresentar mensagem:

“Indicador de Classificacao DRE nao deve ser preenchido para Codigo de Aglutinacao do Balanco Patrimonial \(Indicador de Balanco e DRE = B\)”

OS3835\-C1

RN09

__Campo Indicador de Classificação DRE__

Preencher de acordo com o Indicador de Classificação do DRE\. 

Este campo somente deverá ser preenchido caso o IND\_BALANCO\_DRE = ’D’\. 

Quando houver registro com IND\_BALANCO\_DRE <> ‘D’ e o Campo Indicador de Classificação DRE estiver preenchido, deverá impedir a importação e apresentar a mensagem:

““Indicador de Classificação DRE so deve ser preenchido para Codigo de Aglutinacao da Demonstracao de Resultado \(Indicador de Balanco e DRE = D\)”

Quando o IND\_BALANCO\_DRE = ‘D’, então deverá permitir somente os registros <1> ou <2> ou <3> ou <4> ou <5> ou <6> para o Campo Indicador de Classificação DRE e não deve permitir registro no Campo Indicador de Natureza\.

Na condição acima:

Se o valor do Campo Indicador de Classificação DRE informado for diferente de <1> ou <2> ou <3> ou <4> ou <5> ou <6>, apresentar mensagem:

“Indicador de Classificação DRE deve ser preenchido <1> ou <2> ou <3> ou <4> ou <5> ou <6> para Codigo de Aglutinacao da Demonstração de Resultado \(Indicador de Balanco e DRE = D\)”

Se tiver valor no Campo Indicador de Natureza, apresentar mensagem:

“Indicador de Natureza do Balanco nao deve ser preenchido para Codigo de Aglutinacao da Demonstracao de Resultado \(Indicador de Balanco e DRE = D\)”

OS3835\-C1/

MFS26811

RN10

__Campo Nível__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Nível deve ser preenchido”\.

OS3835\-C1

RN11

__Campo Expressão de Ordem__

Preencher o campo Expressão de Ordem Subtotalizador/Totalizador\.

OS3835\-C1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

